import os
path = os.getcwd()
data = open(path + "/2/data.txt").readlines()
data = [elem.strip("\n") for elem in data]
num_ref = "0123456789"
power_sum = 0

for elem in data:
    possible = True
    game = elem.split(":")
    handsInGame = game[1].split(";")
    highestBlue, highestGreen, highestRed = 0, 0, 0
    currentGameHighest = {"red": 0, "green": 0, "blue": 0}
    for hand in handsInGame:
        cubes = hand.split(",")
        cubes = [cube.strip(" ") for cube in cubes]
        for cube in cubes:
            currentCube = cube.split(" ")
            color = currentCube[1]
            num = currentCube[0]
            if color == "red" and int(num) > currentGameHighest["red"]:
                currentGameHighest["red"] = int(num)
            elif color == "green" and int(num) > currentGameHighest["green"]:
                currentGameHighest["green"] = int(num)
            elif color == "blue" and int(num) > currentGameHighest["blue"]:
                currentGameHighest["blue"] = int(num)
    power_sum += currentGameHighest["red"] * currentGameHighest["green"] * currentGameHighest["blue"]

print(power_sum)




