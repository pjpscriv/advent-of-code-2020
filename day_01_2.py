file = open('input/day_01_1.txt')
nums = [int(x) for x in file.readlines()]
file.close()

for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
