# Points: 1 for Rock, 2 for Paper, and 3 for Scissors
# A for Rock, B for Paper, and C for Scissors in Elf-speak
# X for Rock, Y for Paper, and Z for Scissors in
# Win: 6pts, draw: 3pts, lose: 0pts

total_score = 0

table = {
    'A': 'C', # Rock beats scissors
    'B': 'A', # Paper beats rock
    'C': 'B'  # Scissors beat paper
}

win = 6
draw = 3

with open('Day 2/input2.txt') as f:
    lines = f.readlines()
for each in lines:
    if each[0] == chr(ord(each[2]) - 23):   # -23: 'X' becomes 'A', 'Y' becomes 'B'
        print(f"It's a draw! {each[0]} {chr(ord(each[2]) - 23)}")
        total_score += draw
        total_score += ord(each[2]) - 87    # -87 == (ord('X') - 1): 'X' is one point
        continue
    if table[chr(ord(each[2]) - 23)] == each[0]:
        print(f"Player wins! {each[0]} {chr(ord(each[2]) - 23)}")
        total_score += win
        total_score += ord(each[2]) - 87
    else:
        print(f"Elf wins! {each[0]} {chr(ord(each[2]) - 23)}")
        total_score += ord(each[2]) - 87

print(total_score)