import os
import math
import re

os.system("cls")
print("\n\nNEW INPUT\n")

def arrayToInt(array): 
    newArray = []
    for i in array:
        try:
            newArray.append(int(i))
        except:
            newArray.append(i)
    return newArray

def inc2dArray(array, x = 1): return [[j + x for j in i] for i in array]

def dictDeepCopy(dictionary): return {i: j.copy() for i,j in dictionary.items()}

def part1(input):
    pass

def part2(input):
    pass

fp = open("../Input/10_input2.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

print(inputNum)
print(part1(inputNum))
print(part2(inputNum))