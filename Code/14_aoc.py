def checkSides(walls, c):
    # R L D U
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    collision = [0, 0, 0, 0]

    for i in range(len(dirs)):
        check = (c[0] + dirs[i][0], c[1] + dirs[i][1])
        if check in walls:
            collision[i] = 1
    
    return collision

def sink(obstacles, c, maxDepth):
    # DL, DR
    dirs = [(-1, 1), (1, 1)]

    down = True
    downLeft = (c[0] + dirs[0][0], c[1] + dirs[0][1]) in obstacles
    downRight = (c[0] + dirs[1][0], c[1] + dirs[1][1]) in obstacles

    while not downLeft or not downRight or not down:
        if not down:
            c = (c[0], c[1] + 1)
        elif not downLeft:
            c = (c[0] + dirs[0][0], c[1] + dirs[0][1])
        elif not downRight:
            c = (c[0] + dirs[1][0], c[1] + dirs[1][1])

        down = (c[0], c[1] + 1) in obstacles
        downLeft = (c[0] + dirs[0][0], c[1] + dirs[0][1]) in obstacles
        downRight = (c[0] + dirs[1][0], c[1] + dirs[1][1]) in obstacles

        if c[1] > maxDepth: return None
        
    return c


def part1(walls):
    obstacles = walls.copy()
    maxDepth = max([i[1] for i in walls])
    sandLoc = set()
    infSand = False

    while not infSand:
        sandCoords = (500, 0)
        while True:
            sides = checkSides(obstacles, sandCoords)
            
            if sides[2] != 1:
                sandCoords = (sandCoords[0], sandCoords[1] + 1)

                if sandCoords[1] > maxDepth:
                    infSand = True
                    break
            else:
                sandCoords = sink(obstacles, sandCoords, maxDepth)

                if sandCoords is not None:
                    obstacles.add(sandCoords)
                    sandLoc.add(sandCoords)
                else: infSand = True
                break

    return len(sandLoc)

def part2(walls, maxDepth):
    obstacles = walls.copy()
    sandLoc = set()
    infSand = False

    while not infSand:
        sandCoords = (500, 0)
        while True:
            sides = checkSides(obstacles, sandCoords)
            
            if sides[2] != 1:
                sandCoords = (sandCoords[0], sandCoords[1] + 1)

            else:
                sandCoords = sink(obstacles, sandCoords, maxDepth)

                if sandCoords is not (500, 0):
                    obstacles.add(sandCoords)
                    sandLoc.add(sandCoords)
                else: 
                    sandLoc.add(sandCoords)
                    infSand = True
                break

    return len(sandLoc)

fp = open("../Input/14_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

walls = set()
for i in inputNum:
    i = i.split(" -> ")
    
    for j in range(len(i) - 1):
        x, y = eval(i[j])
        x2, y2 = eval(i[j + 1])

        if x == x2:
            src = min(y, y2)
            dest = max(y, y2)
            for k in range(src, dest + 1):
                walls.add((x, k))
        
        elif y == y2:
            src = min(x, x2)
            dest = max(x, x2)
            for k in range(src, dest + 1):
                walls.add((k, y))


print(part1(walls))


maxDepth = max([i[1] for i in walls]) + 2
minX = min([i[0] for i in walls]) - 200
maxX = max([i[0] for i in walls]) + 200

for i in range(minX, maxX):
    walls.add((i, maxDepth))

print(part2(walls, maxDepth))