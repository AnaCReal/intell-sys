# Othello game
# Author: Dr. Santiago Enrique Conant Pablos
# Last modification: September 2018

import random
from games import (GameState, Game, infinity)

# ______________________________________________________________________________
# Alpha-Beta Minimax Search

def alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    player = game.to_move(state)

    # Functions used by alphabeta
    def max_value(state, alpha, beta, depth):
        #print('max_value')
        #game.display(state)
        if cutoff_test(state, depth):
            v = eval_fn(state, player)
            #print('max:',v)
            return v
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                #print('max:',v)
                return v
            alpha = max(alpha, v)
        #print('max:',v)
        return v

    def min_value(state, alpha, beta, depth):
        #print('min_value')
        #game.display(state)
        if cutoff_test(state, depth):
            v = eval_fn(state, player)
            #print('min:',v)
            return v
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v <= alpha:
                #print('min:',v)
                return v
            beta = min(beta, v)
        #print('min:',v)
        return v

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or
                   (lambda state, depth: depth == d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action

#_______________________________________________________________________________
# Auxiliary functions

class Othello(Game):
    """Plays Othello on an N x N board, with MAX (first player) playing with the
       black chips. A state contains information about the next player to play,
       a cached utility, a list of movements in the form of a list of positions
       (x, y), and a board, in the form of a dictionary with data
       {(x, y): Player}, where Player is 'W' for white chips and 'B' for black
       chips."""

    def __init__(self, N=8):
        self.N = N
        moves = [(x, y) for x in range(1, N+1) for y in range(1, N+1)]
        m = N // 2
        m1 = m + 1
        moves.remove((m, m))
        moves.remove((m, m1))
        moves.remove((m1, m))
        moves.remove((m1, m1))
        # Always starts the black player
        self.initial = GameState(to_move='B', utility=0,
                                 board={(m, m):'W',(m, m1): 'B',
                                        (m1, m):'B',(m1, m1):'W'}, moves=moves)

    def actions(self, state):
        """The legal movements are the positions that are aligned with another
           chip of the same color of the player that moves, forming a segment
           of a straight line that contains at least one chip of the opponent."""
        return self.legal_moves(state.moves, state.board, state.to_move)

    def legal_moves(self, smoves, board, player):
        """Determines the legal movements of a player on a board."""
        moves = []
        for (x, y) in smoves:
            if self.change_dir(x, y, -1, -1, board, player) \
               or self.change_dir(x, y, -1, 0, board, player) \
               or self.change_dir(x, y, -1, 1, board, player) \
               or self.change_dir(x, y, 0, -1, board, player) \
               or self.change_dir(x, y, 0, 1, board, player) \
               or self.change_dir(x, y, 1, -1, board, player) \
               or self.change_dir(x, y, 1, 0, board, player) \
               or self.change_dir(x, y, 1, 1, board, player):     
                moves.append((x, y))
        return moves

    def change_dir(self, x, y, xd, yd, board, player):
        """Determines a location that will change the color of at least one
           chip of the opponent"""

        def find_player(x, y):
            """Determines if another player's chip is found in one direction"""
            x += xd
            y += yd
            while (x, y) in board:
                if board[(x, y)] == player:
                    return True
                else:
                    x += xd
                    y += yd
            return False

        x1 = x + xd
        y1 = y + yd
        if (x1, y1) in board and player != board[(x1, y1)]:
            return find_player(x1, y1)
        else:
            return False

    def result(self, state, move):

        def change_player(xd, yd):
            """Changes the chips to the player's color in one direction"""
            x, y = move
            if self.change_dir(x, y, xd, yd, board, player):
                x += xd
                y += yd
                while (x, y) in board:
                    if board[(x, y)] == player: return
                    else:
                        board[(x, y)] = player
                        x += xd
                        y += yd

        board = state.board.copy()
        moves = list(state.moves)
        player = state.to_move
        if move in self.actions(state):
            board[move] = player
            change_player(-1, -1)
            change_player(-1, 0)
            change_player(-1, 1)
            change_player(0, -1)
            change_player(0, 1)
            change_player(1, -1)
            change_player(1, 0)
            change_player(1, 1)
            moves.remove(move)
            return GameState(to_move=('W' if player == 'B' else 'B'),
                             utility=self.compute_utility(board, move, player),
                             board=board, moves=moves)
        else:
            return GameState(to_move=('W' if player == 'B' else 'B'),
                             utility=self.compute_utility(board, move, player),
                             board=board, moves=moves)
                    
    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        return state.utility if player == 'B' else -state.utility

    def terminal_test(self, state):
        "A state is terminal if none of the players has actions"
        laB = len(self.legal_moves(state.moves, state.board, 'B'))
        laW = len(self.legal_moves(state.moves, state.board, 'W'))
        return (laB + laW) == 0

    def display(self, state):
        """Displays the state of the game board"""
        board = state.board
        print(' ', end=' ')
        for y in range(1, self.N+1): print(y, end=' ')
        print()
        for x in range(1, self.N+1):
            print(x, end=' ')
            for y in range(1, self.N+1):
                print(board.get((x, y), '.'), end=' ')
            print()

    def compute_utility(self, board, move, player):
        """Returns the difference between the number of black and white pieces"""
        pieces = list(board.values())
        return pieces.count('B') - pieces.count('W')

# ______________________________________________________________________________
# evaluation function

def eval_fn(state, player):
    """A very simple evaluation function"""
    evaluation = 1
    if player == 'B':
        return evaluation
    else:
        return -evaluation

# ______________________________________________________________________________
# Player for Games

def query_player(game, state):
    "Make a move by querying standard input."
    actions = game.actions(state)
    to_move = "Black's" if game.to_move(state) == 'B' else "Whites'"
    if not actions: return None
    while True:
        print(to_move, end=' ')
        move_string = input('move? ')
        try:
            move = eval(move_string)
        except:
            move = move_string
        if move in actions:
            return move

def random_player(game, state):
    "A player that chooses a legal move at random."
    actions = game.actions(state)
    return random.choice(actions) if actions else None

def alphabeta_player(depth=2, eval_fn=eval_fn):
    """A team player that decides after depth plies and evaluates
    the states using the eval_fn function of the team"""
    return (lambda game, state:
            alphabeta_search(state, game, d=depth, eval_fn=eval_fn))

def display_move(player, move):
    "Display a player's move"
    if player == 'B':
        print('Black', end=' ')
    else:
        print('White', end=' ')
    print("player selects", move)

def play_game(game, *players):
    """Play an n-person, move-alternating game."""
    state = game.initial
    print('INITIAL BOARD')
    plays = 0
    while True:  
        plays += 1
        print('PLAY #', plays)
        for player in players:
            game.display(state)
            move = player(game, state)
            display_move(state.to_move, move)
            state = game.result(state, move)
            if game.terminal_test(state):
                game.display(state)
                utility = game.utility(state, game.to_move(game.initial))
                if utility > 0:
                    print('Black player wins!!')
                elif utility < 0:
                    print('White player wins!!')
                else:
                    print('Tie: Nobody wins!!')
                pieces = list(state.board.values())
                print('Black chips =', pieces.count('B'))
                print('White chips =', pieces.count('W'))
                return utility

# Examples of calls for playing some games between agents that decide
# using the MINIMAX with alpha-beta pruning, between players that decide
# randomly, and between human players.
# Additionally, in the call you can combine the types of players, change the
# size of the board, and change the depth of the look ahead and the
# evalutation function for the alphabeta_players.
#
#play_game(Othello(), alphabeta_player(), alphabeta_player())
#play_game(Othello(), random_player, random_player)
#play_game(Othello(), query_player, query_player)
play_game(Othello(), random_player, query_player)
  
