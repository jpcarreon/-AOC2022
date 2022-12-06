def findMarker(input, rollover):
    for i in range(0, len(input) - rollover):
        if len(set(input[i:i + rollover])) == rollover:
            return i + rollover

fp = open("../Input/06_input.txt", "r").read().strip()

print(findMarker(fp, 4))
print(findMarker(fp, 14))