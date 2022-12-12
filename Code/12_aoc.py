import heapq as hq

def convertMaze(input):
    maze = []
    start = [0, -1]
    end = [0, -1]
    startLoc = []

    for i in range(len(input)): 
        if ("S" in input[i]):
            start[0] = i
            start[1] = input[i].rfind("S")

        if ("E" in input[i]):
            end[0] = i
            end[1] = input[i].rfind("E")

        newArray = []
        for j in range(len(input[i])):
            newArray.append(ord(input[i][j].lower()) - 96)
            if (input[i][j] == "a"):
                startLoc.append([i, j])

        maze.append(newArray)

    return [maze, start, end, startLoc]

def checkPath(maze, src, dest, goal):
    src = maze[src[0]][src[1]]
    dest = maze[dest[0]][dest[1]]

    if src + 1 >= dest:
        return True
    else:
        return False

def checkSides(maze, c, goal):
    neighbors = []

    if c[0] + 1 < len(maze) and checkPath(maze, c, [c[0] + 1, c[1]], goal):
        neighbors.append([c[0] + 1,c[1]])

    if c[0] - 1 != -1 and checkPath(maze, c, [c[0] - 1, c[1]], goal):
        neighbors.append([c[0] - 1,c[1]])

    if c[1] + 1 < len(maze[0]) and checkPath(maze, c, [c[0], c[1] + 1], goal):
        neighbors.append([c[0],c[1] + 1])
    
    if c[1] - 1 != -1 and checkPath(maze, c, [c[0], c[1] - 1], goal):
        neighbors.append([c[0],c[1] - 1])

    return neighbors

def dijkstra(input, start, end):
    pathRec = {}
    distRec = {}
    distRec[(start[0], start[1])] = 0
    pathRec[(start[0], start[1])] = 0
    pq = []
    hq.heappush(pq, [0, start])

    while (len(pq) != 0):
        index = hq.heappop(pq)[1]

        for i in checkSides(input, index, end):
            if (i[0], i[1]) in distRec: continue

            newDist = distRec[(index[0], index[1])] + input[i[0]][i[1]]

            if (i[0], i[1]) not in distRec or newDist < distRec[(i[0], i[1])]:
                distRec[(i[0], i[1])] = newDist
                pathRec[(i[0], i[1])] = (index[0], index[1])
                hq.heappush(pq, [newDist, i])
    return pathRec

def part1(input, start, end):
    pathRec = dijkstra(input, start,end)
    record = -1
    current = (end[0], end[1])

    if (current not in pathRec): return 999999
    while (current != 0):
        current = pathRec[current]
        record += 1

    return record

def part2(input, aLoc, end):
    minRecord = 999999
    for i in aLoc:
        rec = part1(input, i, (end[0], end[1]))
        minRecord = min(minRecord, rec)

    return minRecord

input = open("../Input/12_input.txt", "r").read().split("\n")

maze, start, end, startLoc = convertMaze(input)

print(part1(maze, start, end))
print(part2(maze, startLoc, end))