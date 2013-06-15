import socket

def solveJugs(red, blue, target):
  if (blue > red):
    largerStr = "blue jug"
    larger = blue
    smallerStr = "red jug"
    smaller = red
  else:
    smallerStr = "blue jug"
    smaller = blue
    largerStr = "red jug"
    larger = red
  actions = []
  current = 0
  actions.append("get " + largerStr + "\n");
  actions.append("get " + smallerStr + "\n");
  while (not (current == target)):
    while (current + smaller < larger):
      actions.append("fill " + smallerStr + "\n");
      actions.append("pour " + smallerStr + " into " + largerStr + "\n");
      current += smaller
      if (current == target):
        break;
    if (current == target):
      break;
    actions.append("fill " + smallerStr + "\n");
    actions.append("pour " + smallerStr + " into " + largerStr + "\n");
    actions.append("empty " + largerStr + "\n");
    actions.append("pour " + smallerStr + " into " + largerStr + "\n");
    current = current + smaller - larger
  actions.append("put " + largerStr + " onto scale\n");
  actions.append("drop " + smallerStr + "\n")
  actions.append("look\n")
  sendStr = ""
  for i in actions:
    sendStr += i
  s.send(sendStr)

global s;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect(("diehard.shallweplayaga.me", 4001));

while(True):
  recvStr = s.recv(4096)
  print recvStr
  splitRecv = recvStr.split("\n");
  room = []
  for line in splitRecv:
    if " is sitting in the room." in line:
      firstIndex = line.find("A ") + 2
      lastIndex = line.find(" is sitting in the room.")
      room.append(line[firstIndex:lastIndex])
  strin = raw_input(">")
  if (strin[0:4] == "jugs"):
    splitString = strin.split(" ")
    blue = int(splitString[1])
    red = int(splitString[2])
    target = int(splitString[3])
    solveJugs(blue, red, target)
  elif (strin[0:4] == "auto"):
    breakWhile = False
    counter = 0
    while(True):
      counter += 1
      print counter
      blue = 0
      red = 0
      target = 0
      s.send("look red jug\nlook blue jug\nlook inscription\n")
      while (blue == 0 or red == 0 or target == 0):
        data = s.recv(4096)
        if counter > 20: print data
        lines = data.split("\n")
        for line in lines:
          if "blue jug holds" in line:
            firstIndex = line.find(" of ") + 4
            lastIndex = line.find("gallons")
            blue = int(line[firstIndex:lastIndex])
          elif "red jug holds" in line:
            firstIndex = line.find(" of ") + 4
            lastIndex = line.find("gallons")
            red = int(line[firstIndex:lastIndex])
          elif "To get to the next stage" in line:
            firstIndex = line.find("put ") + 4
            lastIndex = line.find("gallons")
            target = int(line[firstIndex:lastIndex])
          elif "hexidecimal" in line:
            breakWhile = True
            break
          if counter == 21:
            breakWhile = True
            break
      if (breakWhile):
        print data
        break
      solveJugs(red, blue, target)
      direction = ""
      while (direction == ""):
        data = s.recv(4096)
        if counter > 20: print data
        lines = data.split("\n")
        for line in lines:
          if "Exits: " in line:
            firstIndex = line.find(": ") + 2
            direction = line[firstIndex:len(line)]
          if not "jug" in line:
            print line
      s.send(direction + "\n")
      data = s.recv(4096)
      lines = data.split("\n")
      for line in lines:
        if "hexidecimal" in line:            
          break
      if counter > 20: print data
  elif (strin[0:4] == "surv"):
    for objects in room:
      s.send("look " + objects + "\n")
    s.send("look inscription\n");
  elif (not (strin == "...")):
    s.send(strin + "\n")
