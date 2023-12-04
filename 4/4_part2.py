import os, math
path = os.getcwd()
data = open(path + "/4/data.txt", "r").readlines()
data = [x.strip() for x in data]
cards = [card.split(":") for card in data]
for card in cards:
    card.append(1)
total_cards_num = 0

for i, card in enumerate(cards):
    nums_in_card = card[1].split("|")
    nums_in_card = [card.strip() for card in nums_in_card]
    winning_nums = nums_in_card[0].split(" ")
    winning_nums = [x for x in winning_nums if x != "" and x != " "]
    my_nums = nums_in_card[1].split(" ")
    my_nums = [x for x in my_nums if x != "" and x != " "]
    correct_nums = [x for x in winning_nums if x in my_nums]
    for j in range(card[2]):
        if len(correct_nums) > 0:
            for k in range(len(correct_nums)):
                cards[i+k+1][2] += 1
for card in cards:
    total_cards_num += card[2]
print(total_cards_num)