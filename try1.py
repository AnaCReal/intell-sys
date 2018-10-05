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


for i in range(0,6):
    for j in range(0,6):
        print(init_grid[i][j], end="  ")
    print()

print()

#initial = [(0,0), (0,4), (3,4), (4,2)]
initial = [(3, 2), (3, 4), (0, 0), (0, 2)] 
sgrid = init_grid

for i in range(0, len(sensors_range)):
    sensor_size = sensors_range[i]
    for j in range (0, len(grid)):
        for k in range (0, len(grid[j])):
            g = [j,k]
            #print (g)
            if np.all(np.asarray(initial[i]) == np.asarray(g)):
                rng = sensors_range [i] 
                for n in range (0, rng):
                    for m in range (0, rng):
                        if sgrid [j+m][k] == '-':
                            sgrid [j+m][k] = i+1
                        if sgrid [j+m][k+n] == '-':
                            sgrid [j+m][k+n] = i+1
                        if sgrid [j][k+n] == '-':
                            sgrid [j][k+n] = i+1
for i in range(0,6):
    for j in range(0,6):
        print(sgrid[i][j], end="  ")
    print()
print()

X=0
for j in range (0, len(sgrid)):
        for k in range (0, len(sgrid[j])):
            if sgrid [j][k] == '-':
               X=X+1
X = 24-X
print(X)

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
for i in range(0,6):
    for j in range(0,6):
        print(sgrid[i][j], end="  ")
    print()

print()

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
    for j in range(len(sensors_range)):
        init_bees.append([(r.randint(0, 5-sensors_range[j]-1), r.randint(0, 5-sensors_range[j]-1))])
print(init_bees)

ev_bees = []

s1grid = init_grid

for i in range(0, len(sensors_range)):
    sensor_size = sensors_range[i]
    for j in range (0, len(s1grid)):
        for k in range (0, len(s1grid[j])):
            g = [j,k]
            #print (g)
            x, y = init_bees[0][i]
            x1 = x-1
            y1 = y-1
            if np.all(np.asarray((x1, y1)) == np.asarray(g)):
                rng = sensors_range [i] 
                for n in range (0, rng):
                    for m in range (0, rng):
                        if s1grid [j+m][k] == '-':
                            s1grid [j+m][k] = i+1
                        if s1grid [j+m][k+n] == '-':
                            s1grid [j+m][k+n] = i+1
                        if s1grid [j][k+n] == '-':
                            s1grid [j][k+n] = i+1
for i in range(0,6):
    for j in range(0,6):
        print(s1grid[i][j], end="  ")
    print()

print()

#print(sgrid)
X=0
for j in range (0, len(sgrid)):
        for k in range (0, len(sgrid[j])):
            if s1grid [j][k] == '-':
               X=X+1
X = 24-X
ev_bees.append(X)
#print(X)
#print(sgrid)    
print(ev_bees)





