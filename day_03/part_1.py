file = open('input.txt')
nums = [line.strip() for line in file.readlines()]
file.close()


slope = [3, 1]

# Position: x, y
sled = [0, 0]
count = 0
while sled[1] < len(nums):
    if nums[sled[1]][sled[0]] == '#':
        count += 1

    sled[0] = (sled[0] + slope[0]) % len(nums[0])

    sled[1] = sled[1] + slope[1]

print(count)
