frauds = 0

with open('Day 4/input.txt') as f:
    lines = f.readlines()

for line in lines:
    pair = line.split(',')
    pretty_first = pair[0].split('-')   #['6', '90']
    pretty_second = pair[1].split('-')  #['91', '91']
    print(pretty_first, pretty_second)

    if (int(pretty_first[1]) < int(pretty_second[0])) or (int(pretty_first[0]) > int(pretty_second[1])):
        print('worth it')
    else:
        print('fraud!')
        frauds += 1
print(frauds)

