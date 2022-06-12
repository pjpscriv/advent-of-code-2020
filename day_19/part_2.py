from email import message

LOOP_LIMIT = 2

node_map = {}

class Rule:
    id = None
    char = None
    child_id_lists = []

    def __init__(self, line):
        id, content = line.strip().split(':')
        self.id = int(id)
        if '"' in content:
            self.char = content.strip().strip('"')
        else:
            self.child_id_lists = []
            for sub_rule_string in content.split('|'):
                sub_rule_ids = list(map(lambda x: int(x), sub_rule_string.strip().split(' ')))
                self.child_id_lists.append(sub_rule_ids)
            # print(self.child_id_lists)


def parse_rules(lines):
    rules = []
    for line in lines:
        if not ':' in line:
            break
        rules.append(Rule(line))
    return rules


def parse_messages(lines):
    messages = []
    parsing_on = False
    for line in lines:
        line = line.strip()
        if not parsing_on:
            if line == '':
                parsing_on = True
        else:
            messages.append(line)
    return messages

def generate_valid_messages(node, loop_track={}):
    # print(f'Node {node.id}')
    loop_track[node.id] = loop_track.get(node.id, 0) + 1
    if loop_track.get(8, 0) > LOOP_LIMIT or loop_track.get(11, 0) > LOOP_LIMIT:
        print(f'Hit limit for {node.id} ({loop_track.get(node.id)})')
        return set()
    if node.char != None:
        return set([node.char])
    else:
        messages = set()
        # print(node.child_id_lists)
        for id_list in node.child_id_lists:
            existing_messages = set()
            for child_node in map(lambda id: node_map[id], id_list):
                needs_copy = 8 in loop_track.keys() or 11 in loop_track.keys()
                new_loop_track = loop_track.copy() if needs_copy else {}
                new_messages = generate_valid_messages(child_node, new_loop_track)
                if len(existing_messages) == 0:
                    existing_messages = new_messages
                else:
                    combined_messages = set()
                    for old in existing_messages:
                        for new in new_messages:
                            combined_messages.add(old + new)
                    existing_messages = combined_messages
            messages = messages.union(existing_messages)
        return messages


def get_parent_ids(rules, node_map):
    all_ids = set(node_map.keys())
    child_ids = set([id
        for rule in rules
        for id_list in rule.child_id_lists
        for id in id_list
    ])
    return list(all_ids.difference(child_ids))


f = open('input_2.txt')
lines = f.readlines()
f.close()

rules = parse_rules(lines)
messages = parse_messages(lines)

print(f'Parsed {len(rules)} rules')
print(f'Parsed {len(messages)} messages')

for rule in rules:
    node_map[rule.id] = rule

parents = get_parent_ids(rules, node_map)
print(f'Parent node(s): {parents}')


# m42 = generate_valid_messages(node_map[42])
# m42_lens = set(map(lambda m: len(m), m42))
# print(f'Mssages for 42 ({len(m42)} possible): \n\tMax len: {max(m42_lens)}\n\tMin len {min(m42_lens)}')

m31 = generate_valid_messages(node_map[31])
m31_lens = set(map(lambda m: len(m), m31))
print(f'Mssages for 31 ({len(m31)} possible): \n\tMax len: {max(m31_lens)}\n\tMin len {min(m31_lens)}')


m11 = generate_valid_messages(node_map[11])
m11_lens = set(map(lambda m: len(m), m11))
print(f'Mssages for 11 ({len(m11)} possible): \n\tMax len: {max(m11_lens)}\n\tMin len {min(m11_lens)}')



# possible_messages = generate_valid_messages(node_map[parents[0]], {})
# print(f'{len(possible_messages)} possible messages')
# valid_messages = list(filter(lambda m : m in possible_messages, messages))
# print(f'Valid Messages: {len(valid_messages)} of {len(messages)}')
