def parse_lines(lines):
    # Given a bag, tells you what bags it contains
    bags = {}
    
    for line in lines:
        bag_line = line.split('contain')

        outer_bag = bag_line[0][:-6]
        inner_bags = bag_line[1][:-1].strip(' ').split(',')

        if not inner_bags[0].startswith('no'):
            for bag_line in inner_bags:
                tokens = bag_line.strip().split(' ')
                inner_bag = tokens[1] + ' ' + tokens[2]
                amount = int(tokens[0])

                if outer_bag in bags.keys():
                    bags[outer_bag] += [(inner_bag, amount)]
                else:
                    bags[outer_bag] = [(inner_bag, amount)]
    
    return bags



def count_inner_bags(bag_list, bag):
    # Is an inner bag
    if not bag in bag_list.keys():
        return 0
    
    # Count inner bags
    else:
        count = 0
        for inner_bag in bag_list[bag]:
            count += (1 + count_inner_bags(bag_list, inner_bag[0])) * inner_bag[1]
        return count



file = open('input/day_07.txt')
lines = [l.strip() for l in file.readlines()]
file.close()

inner_bags = parse_lines(lines)

bag = 'shiny gold'

bag_count = count_inner_bags(inner_bags, bag)

print(bag_count)
