import numpy as np

with open('Day 8/input.txt') as f:
    lines = f.readlines()

def count_x(forrest):
    new_row = []
    for row in forrest:
        for i in range(0, len(row)):
            for score, j in enumerate(row[i+1:], 1):
                if int(row[i]) <= int(j):
                    new_row.append(score)
                    break
    return "'".join(new_row)

a = [line.replace('\n', '') for line in lines]
b = [count_x(line) for line in a]


with open('Day 8/output.txt', 'w') as g:
    print(b)
        




# normal_trees = [b]
# trees = np.asarray(b, dtype=object)

# new_forrest = [count_x(row) for row in trees]
