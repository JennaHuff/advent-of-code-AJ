# not 982247
# not 1277098

answer = 0

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.weight = 0
        self.parent = parent
        self.children = {}

    def count_children(self):
        global answer
        for child in self.children:
            self.children[child].count_children()
            self.weight += self.children[child].weight
        if self.weight <= 100000:
            print(self.name, len(self.children), self.weight)
            answer += self.weight


def createNode(name, parent):
    node = Node(name, parent)
    return node

with open('test_input.txt') as f:
    lines = f.readlines()


nodes = {}

# creer le node /
nodes['/'] = createNode('/', None)
working_dir = nodes['/']
print(nodes)

for i, line in enumerate(lines[1:]):
    if 'cd ..' in line:
        # changer le node courant en arriere
        working_dir = working_dir.parent
    if '$ cd' in line and 'cd ..' not in line:
        # changer le node courant en avant
        working_dir = working_dir.children[line.split()[2]] # $ cd a --> 'a'
    if 'dir ' in line:
        # ajouter le node à la liste des enfants du node courant
        name = line.split()[1]
        working_dir.children[name] = createNode(name, working_dir)
    # si size
    if line[0].isnumeric():     # 197934 sgwz.cdz
        # augmenter le poids du node courant
        working_dir.weight += int(line.split()[0])

nodes['/'].count_children()

print(f"the answer is: {answer}")
