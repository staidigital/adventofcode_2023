import os, copy
path = os.getcwd()
data = open(path + "/1/data.txt").readlines()
calibrationSum = 0
ref = "0123456789"

# Part 1
for elm in data:
    nums = []
    for i in range(len(elm)):
        if elm[i] in ref:
            nums.append(elm[i])
    if len(nums) == 1:
        calibrationSum += int(nums[0]*2)
    else:
        calibrationSum += int(nums[0] + nums[-1])

print(calibrationSum)