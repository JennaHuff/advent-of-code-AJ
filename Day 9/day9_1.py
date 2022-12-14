def move_LR(board, ins):
    global x
    global y
    for i in range(step):
        if ins[0] == 'U':
            board[x][y] = ' '
            x += 1
            board[x][y] = 'H'
        if ins[0] == 'D':
            board[x][y] = ' '
            x -= 1
            board[x][y] = 'H'
        if ins[0] == 'R':
            board[x][y] = ' '
            y += 1
            board[x][y] = 'H'
        if ins[0] == 'L':
            board[x][y] = ' '
            y -= 1
            board[x][y] = 'H'
    return board


with open('Day 9/test.txt') as f:
    lines = f.readlines()

board = []
for i in range(500):
    tab = []
    for j in range(500):
        tab.append('+')
    # tab.append('\n')
    board.append(tab)

y = 250
x = 250


board[x][y] = 'H'

board[0][0] = '0'
board[0][1] = 'X'
board[1][0] = 'F'


for command in lines:
    ins = [command[0], int(command[2])]
    step = ins[1]
    board = move_LR(board, ins)
# print(x, y)
# print(board)

# command = "L 2"
# ins = [command[0], int(command[2])]
# step = ins[1]

# board, x, y = move_LR(board, ins, x, y)

# print(x, y)
# print(board)


# # def move_UD(board, ins, x, y):
# #     for i in range(step):
# #         if ins[0] == 'U':
# #             board[x][y] = ' '
# #             x -= 1
# #             try:
# #                 board[x][y] = 'H'
# #             except:
# #                 board[x].append('H')
# #         if ins[0] == 'D':
# #             board[x][y] = ' '
# #             x += 1
# #             try:
# #                 board[x][y] = 'H'
# #             except:
# #                 board[x].insert(0, 'H')
# #       return board, x, y

# x = 0
# y = 0
# tab = []
# for line in lines:
#     if line[0] == 'L': x -= 1
#     if line[0] == 'R': x += 1
#     tab.append(x)
# print(min(tab))
# print(max(tab))

# tab = []
# for line in lines:
#     if line[0] == 'U': y -= 1
#     if line[0] == 'D': y += 1
#     tab.append(y)
# print(min(tab))
# print(max(tab))

board.reverse()
with open('Day 9/output.txt', 'w') as g:
    for tab in board:
        g.write(''.join(tab) + '\n')