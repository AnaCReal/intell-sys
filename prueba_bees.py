import matplotlib.pyplot as plt
import numpy as np
import random as r
import heapq


sensors_range = [3,2,2,1]
initial = [(1,1), (1,5), (4,5), (5,3)] # Dónde empiezan nuestros 4 sensores
grid = [[1,1,0,0,1,0], [1,0,0,1,1,1], [0,0,1,1,1,1], [1,1,1,1,1,1], [0,0,0,1,1,1], [1,1,1,1,0,0]]

def copy(grid):
    init_grid = []
    for row in grid:
        temp_row =[]
        for elem in row:
            temp_row.append(elem)
        init_grid.append(temp_row)
    return init_grid
init_grid = copy(grid)

def eval_s(grid):
    X=0
    for j in range (0, len(grid)):
            for k in range (0, len(grid[j])):
                if grid [j][k] == '-':
                   X=X+1
    #X = 24-X
    #print(X)
    return X
    
def eval_num(grid):
    X=0
    for j in range (0, len(grid)):
            for k in range (0, len(grid[j])):
                if grid [j][k] == '-':
                   X=X+1
    return -X


def printmat(grid):
    for i in range(0,6):
        for j in range(0,6):
            print(grid[i][j], end="  ")
        print()

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 1:
            init_grid[i][j] ='-' 
        else:
            init_grid[i][j] ='#'

def eval_mat(grid, sensors_range, locations):
    for i in range(0, len(sensors_range)):
        sensor_size = sensors_range[i]
        for j in range (0, len(grid)):
            for k in range (0, len(grid[j])):
                g = [j,k]
                #print (g)
                print('Functions index', i)
                print('Functions Locations', locations[i])
                if np.all(np.asarray(locations[i]) == np.asarray(g)):
                    rng = sensors_range [i] 
                    for n in range (0, rng):
                        for m in range (0, rng):
                            if grid [j+m][k] == '-':
                                grid [j+m][k] = i+1
                            if grid [j+m][k+n] == '-':
                                grid [j+m][k+n] = i+1
                            if grid [j][k+n] == '-':
                                grid [j][k+n] = i+1
    return grid


printmat(init_grid)
print()
#initial = [(0,0), (0,4), (3,4), (4,2)]
initial = [(3, 2), (3, 4), (0, 0), (0, 2)] 
sgrid = copy(init_grid)

printmat(eval_mat(sgrid, sensors_range, initial))
eval_s(eval_mat(sgrid, sensors_range, initial))

r.seed()
init_bees = []

for i in range(10):
    bees = []
    for j in range(len(sensors_range)):
        bees.append([r.randint(0, 5-sensors_range[j]-1), r.randint(0, 5-sensors_range[j]-1)])
    init_bees.append(bees)

print(init_bees)
print(init_bees[0])

ev_bees = []

#for i in range(10):
#    sgrid = copy(init_grid)
#    printmat(eval_mat(sgrid, sensors_range, init_bees[i]))
#    eval_s(eval_mat(sgrid, sensors_range, init_bees[i]))
#    ev_bees.append(eval_num(eval_mat(sgrid, sensors_range, init_bees[i])))
    
 #   print()
#print(ev_bees)

new_bees = [[[1, 1], [1, 0], [0, 2], [0, 2]]eev, [[0, 1], [2, 1], [0, 0], [3, 0]], [[0, 1], [2, 2], [2, 1], [1, 1]], [[0, 1], [0, 1], [1, 2], [1, 1]], [[0, 0], [0, 0], [0, 0], [2, 0]], [[1, 0], [0, 1], [1, 2], [3, 1]], [[[1, 1], [0, 0], [2, 1], [2, 1]], [[1, 1], [0, 0], [2, 1], [2, 1]]], [[[1, 1], [0, 0], [2, 1], [2, 1]], [[1, 1], [1, 2], [1, 1], [2, 2]]]]

ev_new_bees = []

for i in range(10):
    sgrid = copy(init_grid)
    printmat(eval_mat(sgrid, sensors_range, new_bees[i]))
    eval_s(eval_mat(sgrid, sensors_range, new_bees[i]))
    ev_new_bees.append(eval_num(eval_mat(sgrid, sensors_range, new_bees[i])))
    
    print()
print(ev_new_bees)





