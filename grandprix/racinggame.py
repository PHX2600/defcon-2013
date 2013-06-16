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

def findNextMove(aTable, pos):
  #possible moves
  possibleMoves = [0]
  if (pos + 1 < 5):
    possibleMoves.append(1)
  if (pos -1 >= 0):
    possibleMoves.append(-1)

  #get the best moves
  bestMoves = []
  currentMax = 0;
  for move in possibleMoves:
    if (aTable[7][pos+move] > currentMax):
      bestMoves = [move];
      currentMax = aTable[7][pos+move]
    elif (aTable[7][pos+move] == currentMax):
      bestMoves.append(move)
  
  #closest to center
  closest = 100
  bestMove = 0
  for element in bestMoves:
    if (abs(2 - (pos+element)) < closest):
      bestMove = element
      closest = abs(2 - (pos+element))
      
  if (bestMove == 0):
    return "\n"
  elif (bestMove == -1):
    return "l\n"
  else:
    return "r\n"
    
def createPathTable(pt, state):
  #initialize the table
  returnState = [[0 for col in range(8)] for row in range(5)]
  returnState[0][pt] = state[0][pt];
  #expand the table
  for row in range(2,8):
    for col in range(5):
      if (col-1 >= 0 && returnState[row-1][col-1] == 1):
        returnState[row][col] += state[row][col];
      elif (col+1 < 5 && returnState[row-1][col+1] == 1):
        returnState[row][col] += state[row][col];
      elif (returnState[row-1][col] == 1):
        returnState[row][col] += state[row][col];
  return returnState;

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
