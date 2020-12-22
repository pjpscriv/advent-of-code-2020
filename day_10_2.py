class Adapter():
    def __init__(self, value):
        self.value = value
        self.one = None
        self.two = None
        self.thr = None
        self.arrangements = 0

    def __str__(self):
        out = '({})'.format(self.value)
        if not self.one is None:
            out += ' +1\n' + self.one.__str__()
        elif not self.two is None:
            out += ' +2\n' +self.two.__str__()
        elif not self.thr is None:
            out += ' +3\n' +self.thr.__str__()
        else:
            out += ' End'
        return out


adapter_list = {}


def create_adapter_tree(numbers, index):
    value = numbers[index]
    if value in adapter_list.keys():
        return adapter_list[value]
    else:
        adapter = Adapter(value)
        for i in range(index+1,index+4):
            if len(numbers) <= i:
                break
            n = numbers[i]
            diff = n - adapter.value
            if diff == 1:
                adapter.one = create_adapter_tree(numbers, i)
            elif diff == 2:
                adapter.two = create_adapter_tree(numbers, i)
            elif diff == 3:
                adapter.thr = create_adapter_tree(numbers, i)
            else:
                break 
        adapter_list[value] = adapter
        return adapter


def get_arrangements(tree):
    # Has been calculated
    if tree.arrangements != 0:
        return tree.arrangements
    
    # Is final value
    if tree.one is None and tree.two is None and tree.thr is None:
        tree.arrangements = 1
        return 1
    
    # Recurse
    if not tree.one is None:
        tree.arrangements += get_arrangements(tree.one)
    if not tree.two is None:
        tree.arrangements += get_arrangements(tree.two)
    if not tree.thr is None:
        tree.arrangements += get_arrangements(tree.thr)
    return tree.arrangements


f = open('input/day_10.txt')
numbers = [int(x) for x in f.readlines()]
f.close()

numbers.sort()
numbers = [0] + numbers + [max(numbers)+3]

tree = create_adapter_tree(numbers, 0)

count = get_arrangements(tree)

print(count)
