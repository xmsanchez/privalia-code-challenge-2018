#encoding=utf8
import time

end = False
arr = [
        ["X","X","X","X","X","X","X","X","X"],
        ["X"," "," ","X"," "," "," "," ","X"],
        ["X"," "," ","X"," "," "," "," ","X"],
        ["X","P"," ","X"," "," "," "," ","X"],
        ["X"," "," ","X"," ","X","X"," ","X"],
        ["X"," "," ","X"," "," ","X"," ","X"],
        ["X"," "," ","X"," "," ","X"," ","X"],
        ["X"," "," "," "," "," ","X"," ","X"],
        ["X"," "," "," "," ","X","X"," ","X"],
        ["X"," "," "," "," ","X"," "," ","X"],
        ["X"," "," "," "," ","X"," "," ","X"],
        ["X"," "," "," "," ","X"," "," ","X"],
        ["X","X","X","X","X","X","X","G","X"]
        ]

closedl = []
openl = []

def dist(x1,y1,x2,y2):
    d = (x2-x1) + (y2-y1)
    print("d: " + str(d))
    return d

def printm(arr):
    for line in arr:
        print(str(line))

def obst(x,y):
    global arr
    if arr[y][x] == "X":
        return True
    else:
        return False

def findp(p,g):
    global closedl
    global openl
    found = False
    x1 = p["x"]
    x2 = g["x"]
    y1 = p["y"]
    y2 = g["y"]

    tempx = x1
    tempy = y1

    temparr = []
    while not Found:
        temparr.append(obst(tempx + 1, tempy))
        temparr.append(obst(tempx - 1, tempy))
        temparr.append(obst(tempx, tempy + 1))
        temparr.append(obst(tempx, tempy - 1))
        
        for item in temparr:
            if item is True:
                closedl.append(item)
            else: 
                openl.append(item)

p = {"x":3,"y":1}
g = {"x":12,"y":7}

while end is False:
    # Mostrem la maze
    printm(arr)
    # Calculem la distància
    d = dist(p["x"],p["y"],g["x"],g["y"])
        
    time.sleep(1)
