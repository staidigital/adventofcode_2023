import os, math
path = os.getcwd()
data = open(path + "/3/data.txt").readlines()
data = [elem.strip() for elem in data]
data = [elem + "." for elem in data]
ref_nums = "0123456789"
gears_sum = 0

def findEntireNumber(text, index):
    num_start_index, num_end_index = index, index
    while num_start_index > 0 and text[num_start_index-1] in ref_nums:
        num_start_index -= 1
    while num_end_index < len(text) and text[num_end_index+1] in ref_nums:
        num_end_index += 1
    return [num_start_index, num_end_index]


for i in range(0, len(data)):
    for j in range(0, len(data[i])-1):
        gears = []
        if data[i][j] == "*":
            k = j - 1 if j - 1 > 0 else j
            endRange = j + 1 if j + 1 < len(data[i]) else j
            while k <= endRange:
                currentGearLenth = len(gears)
                if i != 0 and data[i-1][k] in ref_nums:
                    num_indexes = findEntireNumber(data[i-1], k)
                    gears.append(data[i-1][num_indexes[0]:num_indexes[1]+1])
                    k = num_indexes[1] + 1
                else:
                    k += 1
            k = j - 1 if j - 1 > 0 else j
            while k <= endRange:
                if data[i][k] in ref_nums:
                    num_indexes = findEntireNumber(data[i], k)
                    gears.append(data[i][num_indexes[0]:num_indexes[1]+1])
                    k = num_indexes[1] + 1
                else:
                    k += 1
            k = j - 1 if j - 1 > 0 else j
            while k <= endRange:
                if i != len(data)-1 and data[i+1][k] in ref_nums:
                    num_indexes = findEntireNumber(data[i+1], k)
                    gears.append(data[i+1][num_indexes[0]:num_indexes[1]+1])
                    k = num_indexes[1] + 1
                else:
                    k += 1
            if len(gears) == 2:
                print(gears)
                gears_sum += int(gears[0])*int(gears[1])
print(gears_sum)