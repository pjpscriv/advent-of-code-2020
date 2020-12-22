def count_diffs(nums):
    diffs = [0, 0, 0]
    nums = [0] + nums
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if 1 <= diff <= 3:
            diffs[diff-1] = diffs[diff-1] + 1
        else:
            raise Exception('Unexpected diff:', diff)
    diffs[2] = diffs[2] + 1
    print('Diffs:', diffs)
    print('1s*3s:', diffs[0]*diffs[2])


f = open('input/day_10.txt')
numbers = [int(x) for x in f.readlines()]
f.close()

numbers.sort()

count_diffs(numbers)
