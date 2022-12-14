global_intersections = []

def count_frauds(sets):
    count = 0
    for set in sets:
        for i in set:
            if i.isalpha() and i.isupper():
                count += (ord(i) - 38)
            if i.isalpha() and i.islower():
                count += (ord(i) - 96)
    return(count)

with open('Day 3/input.txt') as f:
    lines = f.readlines()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sets = []
for counter, i in enumerate(lines, 1):
    sets.append(i)
    if len(sets) > 2:
        set1 = set(sets[0])
        set2 = set(sets[1])
        set3 = set(sets[2])
        intersect_1 = set1.intersection(set2)
        intersect_2 = intersect_1.intersection(set3)
        intersect_2.discard('\n')
        global_intersections.append(intersect_2)
        sets= []

count = count_frauds(global_intersections)
print(count)

  
