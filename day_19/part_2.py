from email import message
from functools import reduce
from math import ceil

LOOP_LIMIT = 2

rule_map = {}
result_map = {}

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
                sub_rule_ids = [int(x) for x in sub_rule_string.strip().split(' ')]
                self.child_id_lists.append(sub_rule_ids)

    def __repr__(self):
        if self.char != None:
            return f"{self.id}: \"{self.char}\""
        if len(self.child_id_lists) > 0:
            child_id_str = ' | '.join([' '.join([str(y) for y in x]) for x in self.child_id_lists])
            return f"{self.id}: {child_id_str}"
        else:
            raise Exception(f'The Rule {self.id} is malformed')


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


def generate_valid_messages(node):
    if node.char != None:
        return set([node.char])
    else:
        messages = set()
        for id_list in node.child_id_lists:
            existing_messages = set()
            for child_node in map(lambda id: rule_map[id], id_list):

                if child_node in result_map.keys():
                    new_messages = result_map.get(child_node)
                else:
                    new_messages = generate_valid_messages(child_node)

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


# split into chunks of 8
# 0 = 8 11
# 8 = (42)+
# 11 = 42 (42 31)* 31
def is_valid_message(message, result_map):
    chunks = [message[i*8:(i+1)*8] for i in range(len(message) // 8)]

    start_valid = chunks[0] in result_map[42]
    end_valid = chunks[-1] in result_map[31]
    rest = chunks[1:]

    cut = ceil(len(rest) / 2)

    rest_1 = rest[:cut]
    rest_2 = rest[cut:]

    rest_1_valid = reduce(lambda a, b: a and b in result_map[42], rest_1, True)
    rest_2_valid = True
    hit_31 = False
    for c in rest_2:
        if c in result_map[42]:
            if hit_31:
                rest_2_valid = False
        elif c in result_map[31]:
            hit_31 = True
        else:
            rest_2_valid = False

    valid = (start_valid and end_valid and rest_1_valid and rest_2_valid)
    return valid


f = open('input_2.txt')
lines = f.readlines()
f.close()

rules = parse_rules(lines)
messages = parse_messages(lines)

print(f'Parsed {len(rules)} rules')
print(f'Parsed {len(messages)} messages')

for rule in rules:
    rule_map[rule.id] = rule

m42 = generate_valid_messages(rule_map[42])
m42_lens = set(map(lambda m: len(m), m42))
print(f'Messages for Rule 42 ({len(m42)} possible): \n\tMax len: {max(m42_lens)}\n\tMin len {min(m42_lens)}')
result_map[42] = m42

m31 = generate_valid_messages(rule_map[31])
m31_lens = set(map(lambda m: len(m), m31))
print(f'Messages for Rule 31 ({len(m31)} possible): \n\tMax len: {max(m31_lens)}\n\tMin len {min(m31_lens)}')
result_map[31] = m31

print(f'Saved results: {list(result_map.keys())}')

valid_messages = list(filter(lambda m : is_valid_message(m, result_map), messages))
print(f'Valid Messages: {len(valid_messages)} of {len(messages)}')
