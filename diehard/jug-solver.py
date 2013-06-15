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
out = s.recv(1024)
blue = [int(i) for i in out.split() if i.isdigit()]

blueCurrent = blue[0]
blueMax     = blue[1]

print blueMax


# Get red jug value
s.send('look red jug\n')
time.sleep(.2)
out = s.recv(1024)
red = [int(i) for i in out.split() if i.isdigit()]

redCurrent = red[0]
redMax     = red[1]

print redMax


# Get target value
s.send('look inscription\n')
time.sleep(.2)
out = s.recv(1024)
targetArray = [int(i) for i in out.split() if i.isdigit()]

target = targetArray[0]

print target


# Pick up the goddamn jugs
s.send('get blue jug\n')
time.sleep(.2)
s.send('get red jug\n')
time.sleep(.2)


# Set small and large values
if (blueMax < redMax):

    small = 'blue'
    large = 'red'

elseif (redMax < bleMax):

    small = 'red'
    large = 'blue'

else:

    exit(1)


while (redCurrent != target and blueCurrent != target):

    # Fill the small jug
    s.send('fill ' + small + ' jug\n')
    time.sleep(.2)

    # Pour small into large
    s.send('pour ' + small + ' jug into ' + large + ' jug\n')
    time.sleep(.2)
    out = s.recv(1024)

    print out
