global_count = 0

def split_str(str_inp):
    str1 = str_inp[:len(str_inp) // 2]
    str2 = str_inp[len(str_inp) // 2:]
    return str1, str2

def check_for_frauds(str1, str2):
    frauds = set()
    for i in str2:
        if str1.count(i):
            frauds.add(i)
    return(frauds)

def count_frauds(set):
    count = 0
    for i in set:
        if i.isalpha() and i.isupper():
            count += (ord(i) - 38)
        if i.isalpha() and i.islower():
            count += (ord(i) - 96)
    return(count)


with open('Day 3/input.txt') as f:
    lines = f.readlines()
for i in lines:
    split_ruck = split_str(i)
    frauds = check_for_frauds(split_ruck[0], split_ruck[1])
    count = count_frauds(frauds)
    global_count += count

print(global_count)

