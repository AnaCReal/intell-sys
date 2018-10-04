import matplotlib.pyplot as plt
import numpy as np
import random as r


sensors_range = [3,2,2,1]
initial = [(1,1), (1,5), (4,5), (5,3)] # Dónde empiezan nuestros 4 sensores
grid = [[1,1,0,0,1,0], [1,0,0,1,1,1], [0,0,1,1,1,1], [1,1,1,1,1,1], [0,0,0,1,1,1], [1,1,1,1,0,0]]

init_grid = grid
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 1:
            init_grid[i][j] ='-' 
        else:
            init_grid[i][j] ='#'

print(init_grid)

#initial = [(0,0), (0,4), (3,4), (4,2)]
sgrid = init_grid
for i in range(0, len(sensors_range)):
    sensor_size = sensors_range[i]
    for j in range (0, len(sgrid)):
        for k in range (0, len(sgrid[j])):
            g = [j,k]
            #print (g)
            x, y = initial[i]
            x1 = x-1
            y1 = y-1
            if np.all(np.asarray((x1, y1)) == np.asarray(g)):
                rng = sensors_range [i] 
                for n in range (0, rng):
                    for m in range (0, rng):
                        if sgrid [j+m][k] == '-':
                            sgrid [j+m][k] = i+1
                        if sgrid [j+m][k+n] == '-':
                            sgrid [j+m][k+n] = i+1
                        if sgrid [j][k+n] == '-':
                            sgrid [j][k+n] = i+1
print (sgrid)

X=0
for j in range (0, len(sgrid)):
        for k in range (0, len(sgrid[j])):
            if sgrid [j][k] == '-':
               X=X+1
X = 24-X
print(X)

r.seed()
init_bees = []
for i in range(10):
    init_bees.append([(r.randint(1, 5), r.randint(1, 5)) for k in range(4)])
print(init_bees)

ev_bees = []

sgrid = init_grid
    
for i in range(0, len(sensors_range)):
    sensor_size = sensors_range[i]
    for j in range (0, len(sgrid)):
        for k in range (0, len(sgrid[j])):
            g = [j,k]
            #print (g)
            x, y = init_bees[0][i]
            x1 = x-1
            y1 = y-1
            if np.all(np.asarray((x1, y1)) == np.asarray(g)):
                rng = sensors_range [i] 
                for n in range (0, rng):
                    for m in range (0, rng):
                        if sgrid [j+m][k] == '-':
                            sgrid [j+m][k] = i+1
                        if sgrid [j+m][k+n] == '-':
                            sgrid [j+m][k+n] = i+1
                        if sgrid [j][k+n] == '-':
                            sgrid [j][k+n] = i+1
print(sgrid)
X=0
for j in range (0, len(sgrid)):
        for k in range (0, len(sgrid[j])):
            if sgrid [j][k] == '-':
               X=X+1
X = 24-X
ev_bees.append(X)
#print(X)
print(sgrid)    
print(ev_bees)





