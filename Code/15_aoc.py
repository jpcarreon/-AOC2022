import re

def manhattanDist(src, dest):
    return abs(src[0] - dest[0]) + abs(src[1] - dest[1])

def part1(sensors, beacons, yval):
    locations = set()
    
    for i, j in sensors.items():
        k = i[0]
        while True:
            loc = (k, yval)
            if manhattanDist(i, loc) <= j and loc not in beacons:
                locations.add(loc)
            else: break
            k += 1

        k = i[0]
        while True:
            loc = (k, yval)
            if manhattanDist(i, loc) <= j and loc not in beacons:
                locations.add(loc)
            else: break
            k -= 1

    return len(locations)

def part2(sensors, limit):    
    for y in range(limit + 1):

        ranges = []
        for sensor, k in sensors.items():
            check = manhattanDist(sensor, (sensor[0], y))
            if check > k: continue

            check = k - check
            lowBound = sensor[0] - check if sensor[0] - check >= 0 else 0
            upBound = sensor[0] + check if sensor[0] + check <= limit else limit 
            ranges.append((lowBound, upBound))

        formedRange = ranges.pop(0)
        while len(ranges) > 1:
            curr = ranges.pop(0)

            if (curr[1] + 1 >= formedRange[0] and curr[1] <= formedRange[1]):
                formedRange = (min(formedRange[0], curr[0]), max(formedRange[1], curr[1]))
            elif (formedRange[1] + 1 >= curr[0] and formedRange[1] <= curr[1]):
                formedRange = (min(formedRange[0], curr[0]), max(formedRange[1], curr[1]))
            else:
                ranges.append(curr)
            
            if (formedRange[1] < min([i[0] for i in ranges])):
                return  formedRange[1] * 4000000 + y

fp = open("../Input/15_input.txt", "r").read().split("\n")

beacons = set()
sensors = {}
for i in fp: 
    i = re.sub(r"(Sensor\sat|closest\sbeacon\sis\sat)\s", "", i).split(": ")
    sensor = i[0].split("=")
    beacon = i[1].split("=")
    
    sensor = (int(sensor[1][:-3]), int(sensor[-1]))
    beacon = (int(beacon[1][:-3]), int(beacon[-1]))
    
    sensors[sensor] = manhattanDist(sensor, beacon)
    beacons.add(beacon)

print(part1(sensors, beacons, 2000000))
print(part2(sensors, 4000000))