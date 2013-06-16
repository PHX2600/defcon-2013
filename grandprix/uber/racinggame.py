#!/usr/bin/env python
'''
racinggame.py

u - player
~ - snake/crash
T - tree/crash
P - person/crash
Z - zebra/crash
r - rock/crash
c - car/crash
X - road block/ crash
| - wall/crash - restrict movement to the 5 positions between the walls

At any give time it needs to be able to predict 5 steps ahead.
Needs to be moving forward at every step.
Avoid all objects in front of you between the walls.

Starting screen:

|-----|
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|  u  |
|-----|

'''

import random
import math
import socket
import numpy as np

grid1 = [[0,1,0,1,0],
         [1,0,1,0,1],
         [0,1,0,1,0],
         [1,0,1,0,1],
         [0,1,0,1,0],
         [1,0,1,0,1],
         [0,1,0,1,0],
         [1,0,1,0,1]]

grid2 = [[0,0,0,0,0],
         [1,0,1,0,1],
         [0,0,0,0,0],
         [1,0,1,0,1],
         [0,0,0,0,0],
         [1,0,1,0,1],
         [0,0,0,0,0],
         [1,0,1,0,1]]

grid3 = [[0,0,0,0,0],
         [1,1,1,1,1],
         [0,0,0,0,0],
         [1,1,1,1,1],
         [0,0,0,0,0],
         [1,1,1,1,1],
         [0,0,0,0,0],
         [1,1,1,1,1]]

grid4 = [[0,0,0,0,0],
         [1,0,0,0,0],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [0,0,0,0,0],
         [1,0,0,0,0]]

grid5 = [[1,0,0,0,0],
         [1,0,0,0,0],
         [1,0,0,0,0],
         [1,0,0,0,0],
         [1,0,0,0,0],
         [1,0,0,0,0],
         [1,0,0,0,0],
         [1,0,0,0,0]]

def moveForward(s):
    s.send("\n")

def moveLeft(s):
    s.send("l\n")

def moveRight(s):
    s.send("r\n")

'''def getState(s):
    trackList = []
    rawTrack = s.recv(1024).split('\n')
    for i in rawTrack:
        trackList.append(i)
    for row in range(len(trackList)):
        for pos in range(len(trackList[row])):
            if trackList[row][pos] == " ":
                trackList[row][pos] = 1
            else:
                trackList[row][pos] = 0
    print len(trackList)'''

def createAggregate(grid1, grid2, grid3, grid4, grid5):
    a = np.matrix(grid1)
    b = np.matrix(grid2)
    c = np.matrix(grid3)
    d = np.matrix(grid4)
    e = np.matrix(grid5)

    return a+b+c+d+e
    
def main():
    '''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("grandprix.shallweplayaga.me", 2038))
    greeting = s.recv(1024)
    print greeting
    s.send("\n")'''

    blah = createAggregate(grid1, grid2, grid3, grid4, grid5)
    print blah[7][2]

if __name__ == "__main__":
    main()
