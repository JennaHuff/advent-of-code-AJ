# answer 1130 is too low

def count(test_inp):
    for i, letter in enumerate(test_inp[1:]):
        counter = set()
        if i+14 >= len(test_inp)+1: break
        ree = i + 14
        for j in test_inp[i:ree]:
            counter.add(j)
        # print(counter)
        # print(len(counter))
        if len(counter) == 14:
            print(counter, i + 14)
            return

with open('Day 6/input.txt') as f:
    lines = f.readline()


count('mjqjpqmgbljsphdztnvjfqwrcgsmlb')

count(lines)






