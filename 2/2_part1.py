import os
path = os.getcwd()
data = open(path + "/2/data.txt").readlines()
data = [elem.strip("\n") for elem in data]
possible_games = []
num_ref = "0123456789"

for elem in data:
    possible = True
    game = elem.split(":")
    for i in range(len(game[1])-1):
        current, next = game[1][i], game[1][i+1]
        if game[1][i] in num_ref and game[1][i+1] in num_ref:
            num = int(game[1][i] + game[1][i+1])
            color = game[1][i+3]
            if (num > 12 and color == "r") or (num > 13 and color == "g") or (num > 14 and color == "b"):
                possible = False
                break
    possible_games.append(game) if possible else None

id_sum = 0
for game in possible_games:
    id_sum += int(game[0].split(" ")[1])

print(id_sum)