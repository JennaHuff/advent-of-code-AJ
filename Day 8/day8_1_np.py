import numpy as np
import copy

tree_count = 0
with open('Day 8/input.txt') as f:
    lines = f.readlines()

tab_of_trees = copy.deepcopy(lines)
for i, line in enumerate(lines):
    tab_of_trees[i] = list(line.replace('\n', ''))
    
    

forrest = np.asarray(tab_of_trees)
forrest.reshape((99, 99))
chopped_forrest = copy.deepcopy(forrest)


def count_trees_y(forrest, chopped_forrest):
    for i, col in enumerate(forrest):
        tallest_tree = -1
        for j, tree in enumerate(forrest[:,i]):
            if int(tree) > tallest_tree:
                tallest_tree = int(tree)
                chopped_forrest[j][i] = 'x'

def count_trees_x(forrest, chopped_forrest):
    for i, col in enumerate(forrest):
        tallest_tree = -1
        for j, tree in enumerate(col):
            if int(tree) > tallest_tree:
                tallest_tree = int(tree)
                chopped_forrest[i][j] = 'x'


print(forrest)        
count_trees_y(forrest, chopped_forrest)
count_trees_y(np.flipud(forrest), np.flipud(chopped_forrest))
count_trees_x(forrest, chopped_forrest)
count_trees_x(np.fliplr(forrest), np.fliplr(chopped_forrest))

for row in chopped_forrest:
    for tree in row:
        if tree == 'x':
            tree_count += 1
print(tree_count)
with open('Day 8/output.txt', 'w') as g:
    for line in chopped_forrest:
        g.write(str(''.join(line))+'\n')
