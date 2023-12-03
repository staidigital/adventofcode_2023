import os, math
path = os.getcwd()
data = open(path + "/3/data.txt").readlines()
data = [elem.strip() for elem in data]
ref_nums = "0123456789"
parts_sum = 0

def findEntireNumber(text, index):
    num = ""
    for i in range(len(text)):
        if text[i] in ref_nums:
            num += text[i]
        else:
            break
    return num

for i in range(0, len(data)):
    j = 0
    while j < len(data[i])-1:
        if data[i][j] in ref_nums:
            entireNumber = findEntireNumber(data[i][j:], j)
            endRange = j + len(entireNumber) + 1 if j + len(entireNumber) + 1 < len(data[i]) else j + len(entireNumber)
            startRange = j - 1 if j - 1 > 0 else j
            for k in range(startRange,endRange):
                if data[i-1][k] not in ref_nums and data[i-1][k] != "." and i != 0:
                    parts_sum += int(entireNumber)
                if data[i][k] not in ref_nums and data[i][k] != ".":
                    parts_sum += int(entireNumber)
                if i != len(data)-1 and data[i+1][k] not in ref_nums and data[i+1][k] != ".":
                    parts_sum += int(entireNumber)
            j = j + len(entireNumber)
        else:
            j += 1
print(parts_sum)