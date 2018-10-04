"Import packages from AIMA"
from search import *
import matplotlib.pyplot as plt
import numpy as np

class SensorNetworksProblem(Problem):
    
    def __init__(self, initial, sensors_range, grid, defined_actions):
        
        super().__init__(initial)
        # Defines grid
        self.grid = grid
        self.defined_actions = defined_actions
        self.n = len(grid)
        assert self.n > 0
        self.m = len(grid[0])
        assert self.m > 0
    
    def actions(self, state):
        """ Defines possible actions from the current state"""
        # Mover sensor izquierda, arriba abajo. Validar que es posible porque no esta fuera del grid
        # o que los sensores esten "encimados"
        # return allowed_actions
        # una lista de las combinaciones de las acciones aplicadas para cada sensor
        allowed_actions = []
        for action in self.defined_actions:
            next_state = vector_add(state, self.defined_actions[action])
            if next_state[0] >= 0 and next_state[1] >= 0 and next_state[0] <= self.n - 1 and next_state[1] <= self.m - 1:
                allowed_actions.append(action)

        return allowed_actions
        
    def result(self, state, action):
        """ Toma un estado y aplica la acción determinada """
       # return applyaction(state,action)
        return vector_add(state, self.defined_actions[action])

    def value(self, state):
        """ Evalua un estado """
        x, y = state
        assert 0 <= x < self.n
        assert 0 <= y < self.m
        return self.grid[x][y]


sensors_range = [3,2,2,1]
initial = [(1,1), (1,5), (4,5), (5,3)] # Dónde empiezan nuestros 4 sensores
grid = [[1,1,0,0,1,0], [1,0,0,1,1,1], [0,0,1,1,1,1], [1,1,1,1,1,1], [0,0,0,1,1,1], [1,1,1,1,0,0]] #definido en el ejercicio
defined_actions = {'E': (1, 0), 'N': (0, 1), 'S': (0, -1), 'W': (-1, 0)}





myproblem = SensorNetworksProblem(initial, sensors_range, grid, defined_actions)

solutions = {myproblem.value(simulated_annealing(myproblem)) for i in range(100)}
max(solutions)

G = np.random.choice([0, 1], size=(6, 6), p=[0.25, 0.75])
print(G)
