with open('Day 5/input.txt') as f:
    lines = f.readlines()

tab_y = []
for j in range(8):
    tab_x = []
    for i in range(1, len(lines[7]) - 1, 4):
        tab_x.append(list(lines[j])[i])
    tab_y.append(tab_x)

cols = []
for i in range(9):
    rows = []
    cols.append(rows)

for j in range(9):
    for i in range(7, -1, -1):
        if tab_y[i][j] != ' ':
            cols[j].append(tab_y[i][j])
        
for line in lines[10:]:
    instruction = line
    ins_list = instruction.split()

    qty = int(ins_list[1])
    start = int(ins_list[3]) - 1
    end = int(ins_list[5]) - 1

    temp = []
    for x in range(qty):
        temp.append(cols[start][len(cols[start])-1])
        cols[start].pop(len(cols[start])-1)
    temp.reverse()
    cols[end].extend(temp)

for counter, i in enumerate(cols):
    print(counter, i)

lasts = []
for i in cols:
    lasts.append(i[len(i) - 1])
print(''.join(lasts))





# for i in cols:
#     for j in range(qty):
#         cols[8].append(i[len(i)-1])
#         i.pop(len(i)-1)
                
# for counter, i in enumerate(cols):
#     print(counter, i)

########## qty times, do these 2 things
#     cols[end].append(cols[start][3])
#     cols[start][y] = ' '


# move 2 from *start* to *end* --> move 2 from 1 to 7
# cols[end].append(cols[start][3])
# cols[start][y] = ' '






