def find_exception(numbers):
    for i in range(25, len(numbers)):
        candidates = numbers[(i - 25):i]
        if not contains_sum(candidates, numbers[i]):
            return numbers[i]


def contains_sum(nums, res):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == res and nums[i] != nums[j]:
                return True
    return False


def find_set(nums, res):
    for i in range(len(nums)-2):
        for j in range(i+2, len(nums)):
            if sum(nums[i:j]) > res:
                break
            elif sum(nums[i:j]) == res:
                print('Found range! min+max:', min(nums[i:j])+max(nums[i:j]))


f = open('input/day_09.txt')
numbers = [int(x) for x in f.readlines()]
f.close()


ex = find_exception(numbers)

print('Exception:', ex)

find_set(numbers, ex)
