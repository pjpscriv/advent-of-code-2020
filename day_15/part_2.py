# Guarding against a ridiculous, currently non-existent edge case
def last_indices_diff(list, item):
    if list.count(item) < 2:
        raise Exception(f'There must be 2 or more items of value {item} in the list')
    indices = [i for (i, x) in enumerate(list) if x == item]
    return indices[-1] - indices[-2]


f = open('input.txt')
starters = [int(i) for i in f.readline().split(',')]
f.close()

turn = 1
last_spoken = 0
last_turn_map = {}

for num in starters:
    last_turn_map[num] = turn
    turn += 1

last_spoken = starters[-1]
if starters.count(last_spoken) < 2:
    last_spoken = 0
else:
    last_spoken = last_indices_diff(starters, last_spoken)
turn += 1


while turn <= 30000000:
    last_turn = last_turn_map.get(last_spoken, 0)
    last_turn_map[last_spoken] = turn - 1

    if last_turn == 0:
        last_spoken = 0
    else:
        last_spoken = (turn - 1) - last_turn
    turn += 1


print(f'Turn {turn-1}: {last_spoken}')
