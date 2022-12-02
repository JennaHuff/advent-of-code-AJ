with open('Day 1/input.txt') as f:
    lines = f.readlines()

most_fed_elf = 0
counter = 0
for each in lines:
    if each == '\n':
        if counter > most_fed_elf:
            most_fed_elf = counter
        counter = 0
    else:
        counter += int(each)

print(most_fed_elf)