file = open('input/day_01.txt')
nums = [int(x) for x in file.readlines()]
file.close()

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(nums[i] * nums[j])
