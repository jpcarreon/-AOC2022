def arrayToInt(array): 
    newArray = []
    for i in array:
        try:
            newArray.append(int(i))
        except:
            newArray.append(i)
    return newArray

def walk(array, threshold):
    count = 0
    for i in array:
        count += 1
        if (i >= threshold):
            break

    return count

def part1(data):
    cols = len(data)
    rows = len(data[0])
    visible = (cols * 2 + rows * 2) - 4

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            left = data[i][:j]
            right = data[i][j + 1:]
            up = [data[k][j] for k in range(i)]
            down = [data[k][j] for k in range(i + 1, cols)]

            if any([data[i][j] > max(k) for k in [left, right, up, down]]):
                visible += 1

    return visible

def part2(data):
    cols = len(data)
    rows = len(data[0])
    score = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            left = data[i][:j]
            right = data[i][j + 1:]
            up = [data[k][j] for k in range(i)]
            down = [data[k][j] for k in range(i + 1, cols)]

            left.reverse()
            up.reverse()
            k = data[i][j]
            
            currentScore = walk(left, k) * walk(right, k) * walk(up, k) * walk(down, k)
            score = max(score, currentScore)
            
    return score


fp = open("../Input/08_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(arrayToInt(i))

print(part1(inputNum))
print(part2(inputNum))