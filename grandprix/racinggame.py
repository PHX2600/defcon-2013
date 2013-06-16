#!/usr/bin/python
#'''
#racinggame.py

#u - player
#~ - snake/crash
#T - tree/crash
#P - person/crash
#Z - zebra/crash
#r - rock/crash
#c - car/crash
#X - road block/ crash
#| - wall/crash - restrict movement to the 5 positions between the walls

#At any give time it needs to be able to predict 5 steps ahead.
#Needs to be moving forward at every step.
#Avoid all objects in front of you between the walls.

#Starting screen:

#|-----|
#|     |
#|     |
#|     |
#|     |
#|     |
#|     |
#|     |
#|     |
#|  u  |
#|-----|
#'''

import math
import socket
import numpy as np

def moveForward(s):
    s.send("\n")

def moveLeft(s):
    s.send("l\n")

def moveRight(s):
    s.send("r\n")

def parseTrack(s):
    trackList = []
    data = s.recv(1024)
    if 'Press return to start' in data:
      print data  
    num = 0
    lines = s.recv(1024).split('\n')
    print lines
    i = 0
    
def createAggregate(grid1, grid2, grid3, grid4, grid5):
    a = np.matrix(grid1)
    b = np.matrix(grid2)
    c = np.matrix(grid3)
    d = np.matrix(grid4)
    e = np.matrix(grid5)

    return a+b+c+d+e

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("grandprix.shallweplayaga.me", 2038))
    s.recv(1024)
    s.send('\n')
    parseTrack(s)

if __name__ == "__main__":
    main()
