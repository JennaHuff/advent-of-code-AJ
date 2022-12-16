frauds = 0

with open('Day 4/input.txt') as f:
    lines = f.readlines()

for line in lines:
    pair = line.split(',')
    pretty_first = pair[0].split('-')   # ['6', '90']
    pretty_second = pair[1].split('-')  # ['91', '91']
    print(pretty_first, pretty_second)
    
    set_1 = set()
    set_2 = set()

    for i in range(int(pretty_first[0]), int(pretty_first[1])+1):
        set_1.add(i)
    for i in range(int(pretty_second[0]), int(pretty_second[1])+1):
        set_2.add(i)


    if set_1.difference(set_2) and set_2.difference(set_1):
        print('worth it')
    else:
        print('fraud!')
        frauds += 1 
    print(frauds)