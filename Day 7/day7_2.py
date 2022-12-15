candidates = []
class Node:
    def __init__(self, name, parent):
        self.name = name
        self.weight = 0
        self.parent = parent
        self.children = {}


    def count_children(self):
        global candidates
        for child in self.children:
            self.children[child].count_children()
            self.weight += self.children[child].weight
        if self.weight >= 268_565:  # total_needed_space - unused_space
            candidates.append((self.weight))


def createNode(name, parent):
    node = Node(name, parent)
    return node


with open('test_input.txt') as f:
    lines = f.readlines()
    

nodes = {}

# creer le node /
nodes['/'] = createNode('/', None)
working_dir = nodes['/']

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

total_space = 70_000_000
used_space = 40_268_565 # nodes['/'].weight
unused_space = 29_731_435 # total_space - used_space
total_needed_space = 30_000_000
need_to_be_freed = 268_565 # total_needed_space - unused_space

nodes['/'].count_children()

print(min(candidates))


