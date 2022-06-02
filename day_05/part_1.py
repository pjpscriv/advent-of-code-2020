def parse_seat(seat):

    row = 0
    for i in range(7):
        if seat[i] == 'B':
            row += 2 ** (6-i)

    col = 0
    for i in range(3):
        if seat[7+i] == 'R':
            col += 2 ** (2-i)

    return (row * 8) + col


file = open('input.txt')
nums = [parse_seat(x) for x in file.readlines()]
file.close()

print(max(nums))
