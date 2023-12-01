import os, copy, math
path = os.getcwd()
data = open(path + "/1/data.txt").readlines()

calibrationSum = 0
ref_nums = "0123456789"
ref_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Part 2
for elm in data:
    nums = []
    for i in range(len(elm)):
        if elm[i] in ref_nums:
            nums.append(elm[i])
        else:
            for word in ref_words:
                if elm[i:i+len(word)] == word:
                    nums.append(str(ref_words.index(word)))
    if len(nums) == 1:
        calibrationSum += int(nums[0]*2)
    else:
        calibrationSum += int(nums[0] + nums[-1])

print(calibrationSum)