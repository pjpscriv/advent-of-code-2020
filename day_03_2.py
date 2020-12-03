file = open('input/day_03_1.txt')
nums = [line.strip() for line in file.readlines()]
file.close()


slopes = [[1, 1],
          [3, 1],
          [5, 1],
          [7, 1],
          [1, 2]]

product = 1

for slope in slopes:
    # Position: x, y
    sled = [0, 0]
    count = 0
    while sled[1] < len(nums):
        if nums[sled[1]][sled[0]] == '#':
            count += 1

        sled[0] = (sled[0] + slope[0]) % len(nums[0])

        sled[1] = sled[1] + slope[1]

    product = product * count

print(product)
