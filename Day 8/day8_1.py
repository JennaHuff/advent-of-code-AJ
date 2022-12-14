import copy
# 1910 too high
# 1543, 1534 too low

tree_count = 0


with open('Day 8/input.txt') as f:
    lines = f.readlines()


forrest = []
for line in lines:
    forrest.append(list(line.replace('\n', '')))


def count_row_l_to_r(row):
    global tree_count
    tallest_tree = -1
    for i, tree in enumerate(row):
        if tree == '':
            return(row)
        if tree.isnumeric() and int(tree) > tallest_tree:
            tallest_tree = int(tree)
            row[i] += ''
            tree_count += 1
    return(row)

def count_row_r_to_l(row):
    global tree_count
    tallest_tree = -1
    for i, tree in enumerate(row[::-1], 1):
        if tree == '':
            return(row)
        if tree.isnumeric() and int(tree) > tallest_tree:
            tallest_tree = int(tree)
            row[-i] += ''
            tree_count += 1
    return(row)

def count_col_top_to_bot(tab):
    global tree_count
    for i, col in enumerate(tab[0]):
        tallest_tree = -1
        for j, row in enumerate(tab):
            if tab[j][i].isnumeric() and int(tab[j][i]) > tallest_tree:
                tallest_tree = int(tab[j][i])
                tab[j][i] = ''
                tree_count += 1
    return tab
        
def count_col_bot_to_top(tab):
    global tree_count
    jon = copy.deepcopy(tab)
    jon.reverse()
    for i, col in enumerate(jon[0]):
        tallest_tree = -1
        for j, row in enumerate(jon):
            if jon[j][i].isnumeric() and int(jon[j][i]) > tallest_tree:
                tallest_tree = int(jon[j][i])
                jon[j][i] = ''
                tree_count += 1
    jon.reverse()
    return jon
        
for row in forrest:
    # row.reverse()
    # row = count_row_l_to_r(row)
    # row.reverse()
    count_row_r_to_l(row)
print(forrest)
for row in forrest:
    row = count_row_l_to_r(row)
print(forrest)




    # j = count_row_r_to_l(j)
# print(forrest)





# forrest = count_col_bot_to_top(forrest)
# print(forrest)
# forrest = count_col_top_to_bot(forrest)
# print(forrest)






# 552 count_col_top_to_bot
# 496 count_col_bot_to_top
# total = 1048

# 509 count_row_r_to_l
    # 1547 should be 1557
# 532 count_row_l_to_r
    # 1563 should be 1580
# total = 1041 but is 1038 either way

# 1038 both sideways
# 1045 both top/bot



with open('Day 8/output.txt', 'w') as g:
    for line in forrest:
        g.write(str(''.join(line)+'\n'))

print(tree_count)

