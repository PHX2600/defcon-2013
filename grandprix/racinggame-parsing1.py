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
import random
import math
import socket

def moveForward(s):
    s.send("\n")

def moveLeft(s):
    s.send("l\n")

def moveRight(s):
    s.send("r\n")

def parseTrack(s):
    data = s.recv(1024)
    data = data.replace(' ', '1')
    data = data.replace('~',"0").replace('T',"0").replace('P',"0").replace('Z',"0").replace('r',"0").replace('c',"0").replace('x',"0")
    lines = data.split('\n')[1:9] # 10 = Current position
    state = [] 
    for line in lines:
      state.append([int(i) for i in line[1:-1]])
        
    print len(state)
    for i in state:
      print i
    return state

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("grandprix.shallweplayaga.me", 2038))
    data = s.recv(1024)
    s.send('\n')
    while 1:
      parseTrack(s)

if __name__ == "__main__":
    main()
