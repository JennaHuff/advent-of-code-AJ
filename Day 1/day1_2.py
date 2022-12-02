with open('Day 1/input.txt') as f:
    lines = f.readlines()

most_fed_elves = [0]
counter = 0
for each in lines:
    if each == '\n':
        if counter > most_fed_elves[0]:
            most_fed_elves.append(counter)
            most_fed_elves.sort()
            if len(most_fed_elves) > 3:
                most_fed_elves.pop(0)
        counter = 0
    else:
        counter += int(each)

print(sum(most_fed_elves))