import os, math
path = os.getcwd()
data = open(path + "/5/data.txt", "r").readlines()
data = [x.strip() for x in data]
seeds = [int(x) for x in data[0].split(" ") if x.isdigit()]

maps = []
tempList = []
for i, map in enumerate(data[1:]):
    if map == "":
        maps.append(tempList)
        tempList = []
    else:
        tempList.append(map)
maps.append(tempList)

def getDestinations(seeds, map):
    destinations = []
    for i, seed in enumerate(seeds):
        for j, range in enumerate(map):
            mapper = range.split(" ")
            mapper = [int(x) for x in mapper if x.isdigit()]
            if int(seed) >= mapper[1] and seed <= mapper[1] + mapper[2]:
                destinations.append(mapper[0] + int(seed) - mapper[1])
        if len(destinations) == i:
            destinations.append(seed)
    return destinations

for map in maps:
    seeds = getDestinations(seeds, map[1:])
    
print(min(seeds))