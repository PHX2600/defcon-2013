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

# Get red jug value
s.send('look red jug\n')
time.sleep(.2)
str = s.recv(1024)
redArray = [int(i) for i in str.split() if i.isdigit()]

red = redArray[1]

print red

# Get blue jug value
s.send('look blue jug\n')
time.sleep(.2)
str = s.recv(1024)
blueArray = [int(i) for i in str.split() if i.isdigit()]

blue = blueArray[1]

print blue

# Get target value
s.send('look inscription\n')
time.sleep(.2)
str = s.recv(1024)
targetArray = [int(i) for i in str.split() if i.isdigit()]

target = targetArray[0]

print target
