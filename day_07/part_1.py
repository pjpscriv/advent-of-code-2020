def parse_lines(lines):
    # Given a bag, tells you what bags can contain it
    outer_bags = {}

    for line in lines:
        bags = line.split('contain')

        outer_bag = bags[0][:-6]
        inner_bags = bags[1][:-1].strip(' ').split(',')

        if not inner_bags[0].startswith('no'):
            for bag_line in inner_bags:
                tokens = bag_line.strip().split(' ')
                inner_bag = tokens[1] + ' ' + tokens[2]
                amount = int(tokens[0])

                if inner_bag in outer_bags.keys():
                    outer_bags[inner_bag] += [(outer_bag, amount)]
                else:
                    outer_bags[inner_bag] = [(outer_bag, amount)]

    return outer_bags



def get_outer_bag_names(bag_list, bag):
    # Is an outmost bag
    if not bag in bag_list.keys():
        return [bag]

    # Get outer bags
    else:
        names = []
        for outer_bag in bag_list[bag]:
            names += [outer_bag[0]] + get_outer_bag_names(bag_list, outer_bag[0])
        return names



file = open('input.txt')
lines = [l.strip() for l in file.readlines()]
file.close()

goes_inside = parse_lines(lines)

bag = 'shiny gold'

bag_names = get_outer_bag_names(goes_inside, bag)

bag_names_set = set(bag_names)

print(len(bag_names_set))
