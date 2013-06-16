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
    data = s.recv(1024)
#    data = data.replace(' ', '1')
#    data = data.replace('~',"0").replace('T',"0").replace('P',"0").replace('Z',"0").replace('r',"0").replace('c',"0").replace('x',"0").replace('X',"0").replace('s',"0").replace
    print data
    track = ''.join('')
    lines = data.split('\n')[1:9] # 10 = Current position
    state = [] 
    for line in lines:
      state.append([0 for i in line[1:-1] if not (i == '1')])
        
    #for i in state:
      #print i
    return state

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
    return [0, "\n"]
  elif (bestMove == -1):
    return [-1, "l\n"]
  else:
    return [1, "r\n"]
    
def createPathTable(pt, state):
  #initialize the table
  returnState = [[0 for col in range(5)] for row in range(8)]
  print state
  print returnState
  returnState[0][pt] = state[0][pt];
  #expand the table
  for row in range(2,8):
    for col in range(5):
      if (col-1 >= 0 and returnState[row-1][col-1] == 1):
        returnState[row][col] += state[row][col];
      elif (col+1 < 5 and returnState[row-1][col+1] == 1):
        returnState[row][col] += state[row][col];
      elif (returnState[row-1][col] == 1):
        returnState[row][col] += state[row][col];
  return returnState;


def createAggregateTable(tables):
  returnTable = [[0 for col in range(5)] for row in range(8)]
  for table in tables:
    for row in range(len(table)):
      for column in range(len(table[row])):
        returnTable[row][column] += table[row][column]
  return returnTable

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("grandprix.shallweplayaga.me", 2038))
    s.recv(1024)
    s.send('\n')
    pos = 2
    while 1:
      state = parseTrack(s)
      grids = []
      for end in range(5):
        grids.append(createPathTable(end, state))
      grid = createAggregateTable(grids)
      nextMove = findNextMove(grid, pos)
      pos += nextMove[0]
      s.send(nextMove[1])

if __name__ == "__main__":
    main()
