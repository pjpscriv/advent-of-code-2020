def find_exception(numbers):
    for i in range(25, len(numbers)):
        candidates = numbers[(i - 25):i]
        if not contains_sum(candidates, numbers[i]):
            print('Exception found:',numbers[i])
            break


def contains_sum(nums, sum):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == sum and nums[i] != nums[j]:
                return True
    return False


f = open('input/day_09.txt')
numbers = [int(x) for x in f.readlines()]
f.close()

find_exception(numbers)
