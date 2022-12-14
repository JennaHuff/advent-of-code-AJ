# not 982247

class Node:
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.children = []
    
    def count_children(self):
        for child in self.children:
            self.weight += child.weight


def createNode(name):
    node = Node(name)
    return node


def calculate_children_sum():
    for node in nodes:
        nodes[node].count_children()


with open('Day 7/test_input.txt') as f:
    lines = f.readlines()


nodes = {}

for i, line in enumerate(lines, 1):     # creates an object for each dir, adds it to a dict
    if '$ cd' in line and '..' not in line:
        dir_name = line.split()[2]
        nodes[dir_name] = createNode(dir_name) # create every explored dir
        for sub_line in lines[i:]:
            if 'cd ..' in sub_line or  '$ cd' in sub_line:
                break
            if sub_line[0].isnumeric():     # 197934 sgwz.cdz
                nodes[dir_name].weight += int(sub_line.split()[0])
for i, line in enumerate(lines, 1):     # links all dirs to dirs they may contain
    if '$ cd' in line and '..' not in line:
        dir_name = line.split()[2]
        for sub_line in lines[i:]:
            if 'cd ..' in sub_line or  '$ cd' in sub_line:
                break
            if 'dir' in sub_line:
                nodes[dir_name].children.append(nodes[sub_line.split()[1]])
        
        
calculate_children_sum()


answer = 0
for node in nodes:
    if nodes[node].weight <= 100000:
        answer += nodes[node].weight
        print(nodes[node].weight, answer)

print(answer)
