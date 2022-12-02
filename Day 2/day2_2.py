total_score = 0

table = {
    'A': 'C', # Rock beats scissors
    'B': 'A', # Paper beats rock
    'C': 'B'  # Scissors beat paper
}

win = 6
draw = 3

# X = lose, Y = draw, Z = win

with open('Day 2/input2.txt') as f:
    lines = f.readlines()
for each in lines:
    if each[2] == 'Y':
        total_score += draw
        total_score += ord(each[0]) - 64  # We take the Elf's move and count the pts
        continue
    if each[2] == 'Z':
        total_score += win
        our_move = ''
        for option in table:
            if table[option] == each[0]:
                our_move = option
        total_score += ord(our_move) - 64
    else:
        our_move = table[each[0]]
        total_score += ord(our_move) - 64

print(total_score)
    
