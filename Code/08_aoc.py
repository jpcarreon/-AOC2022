def arrayToInt(array): 
    newArray = []
    for i in array:
        try:
            newArray.append(int(i))
        except:
            newArray.append(i)
    return newArray

def getColumn(matrix, idx): return [row[idx] for row in matrix]

def checkVisibility(data, num, c):
    visible = [1, 1, 1, 1]
    col = getColumn(data, c[1])

    # left
    for i in range(c[1]):
        if (data[c[0]][i] >= num):
            visible[0] = 0
            break

    # right
    for i in range(len(data[0]) - 1, c[1], -1):
        if (data[c[0]][i] >= num):
            visible[1] = 0
            break

    # up
    for i in range(c[0]):
        if (col[i] >= num):
            visible[2] = 0
            break

    # down
    for i in range(len(col) - 1, c[0], -1):
        if (col[i] >= num):
            visible[3] = 0
            break
    
    return visible

def part1(data):
    visible = (len(data[0]) * 4) - 4

    for i in range(1, len(data[0]) - 1):
        for j in range(1, len(data) - 1):
            result = checkVisibility(data, data[i][j], [i, j])

            if (max(result) == 1):
                visible += 1
            
    return visible
    
def countVisibility(data, num, c):
    visible = [0, 0, 0, 0]
    col = getColumn(data, c[1])

    # left
    for i in range(c[1] - 1, -1, -1):
        visible[0] += 1
        if (data[c[0]][i] >= num):
            break

    # right
    for i in range(c[1] + 1, len(data[0])):
        visible[1] += 1
        if (data[c[0]][i] >= num):
            break

    # up
    for i in range(c[0] - 1, -1, -1):
        visible[2] += 1
        if (col[i] >= num):
            break

    # down
    for i in range(c[0] + 1, len(data)):
        visible[3] += 1
        if (col[i] >= num):
            break

    return visible[0] * visible[1] * visible[2] * visible[3] 

def part2(data):
    score = 0

    for i in range(1, len(data[0]) - 1):
        for j in range(1, len(data) - 1):
            result = countVisibility(data, data[i][j], [i, j])
            score = max(score, result)

    return score


fp = open("../Input/08_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(arrayToInt(i))

print(part1(inputNum))
print(part2(inputNum))