#!/usr/bin/python

import socket, time, re

# Initilize socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('diehard.shallweplayaga.me', 4001))

# Go to jug problem room
s.send('n\n')
time.sleep(.2)
s.send('n\n')
time.sleep(.2)
s.send('n\n')
time.sleep(.2)
s.send('n\n')
time.sleep(.2)
s.send('n\n')
time.sleep(.2)
s.send('n\n')
time.sleep(.2)
s.send('e\n')
time.sleep(.2)
s.send('n\n')
time.sleep(.2)
s.send('w\n')
time.sleep(.2)
s.send('n\n')
time.sleep(.2)

print s.recv(4096)


# Get blue jug value
s.send('look blue jug\n')
time.sleep(.2)
str = s.recv(1024)
blue = [int(i) for i in str.split() if i.isdigit()]

blueCurrent = blue[0]
blueMax     = blue[1]

print blue


# Get red jug value
s.send('look red jug\n')
time.sleep(.2)
str = s.recv(1024)
red = [int(i) for i in str.split() if i.isdigit()]

redCurrent = red[0]
redMAx     = red[1]

print red


# Get target value
s.send('look inscription\n')
time.sleep(.2)
str = s.recv(1024)
targetArray = [int(i) for i in str.split() if i.isdigit()]

target = targetArray[0]

print target

# Pick up the damned jugs
s.send('get blue jug')
s.send('get red jug')

while (redCurrent != target && blueCurrent != target):

    if (blueMax < redMax):

        s.send('')


    if (redMax < blueMax):

