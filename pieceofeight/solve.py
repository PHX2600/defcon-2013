#!/usr/bin/python

import socket

def moveUp(s):
    s.send("u\n")

def moveDown(s):
    s.send("d\n")

def moveLeft(s):
    s.send("l\n")

def moveRight(s):
    s.send("r\n")


def parsePuzzle(s):
    puzList = []
    num = 0
    lines = s.recv(1024).split('\n')
    i = 0
    for line in lines:
        if( (i == 3) or (i == 8) or (i == 13) ):
            if(line[3] == ' '):
                num = 0
            else:
                num = int(line[3])
            print line

            puzList.append(num)

            if(line[9] == ' '):
                num = 0
            else:
                num = int(line[9])

            puzList.append(num)

            if(line[15] == ' '):
                num = 0
            else:
                num = int(line[15])

            puzList.append(num)

        i = i + 1
    return puzList

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pieceofeight2.shallweplayaga.me", 8273))
puzList = parsePuzzle(s)
print puzList
moveLeft(s)
puzList = parsePuzzle(s)
print puzList

