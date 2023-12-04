import os, math
path = os.getcwd()
data = open(path + "/4/data.txt", "r").readlines()
data = [x.strip() for x in data]
cards = [card.split(":") for card in data]
score_total = 0

for card in cards:
    nums_in_card = card[1].split("|")
    nums_in_card = [card.strip() for card in nums_in_card]
    winning_nums = nums_in_card[0].split(" ")
    winning_nums = [x for x in winning_nums if x != "" and x != " "]
    my_nums = nums_in_card[1].split(" ")
    my_nums = [x for x in my_nums if x != "" and x != " "]
    scoring_nums = [x for x in winning_nums if x in my_nums]
    score_total += 2**(len(scoring_nums)-1) if len(scoring_nums) > 0 else 0

print(int(score_total))