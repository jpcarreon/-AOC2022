def part1(input):
    rules = {
        "A X": 4, "A Y": 8, "A Z": 3,
        "B X": 1, "B Y": 5, "B Z": 9,
        "C X": 7, "C Y": 2, "C Z": 6
    }
    score = 0
    for i in input:
        score += rules[i]

    return score

def part2(input):
    rules = {
        "A X": 3, "A Y": 4, "A Z": 8,
        "B X": 1, "B Y": 5, "B Z": 9,
        "C X": 2, "C Y": 6, "C Z": 7
    }

    score = 0
    for i in input:
        score += rules[i]

    return score

fp = open("../Input/02_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)


print(part1(inputNum))
print(part2(inputNum))