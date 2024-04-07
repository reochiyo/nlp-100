#Way1
count = 0
with open('popular-names.txt', 'r') as f:
    for line in f:
        count += 1
print(count)

#Way2
with open('popular-names.txt', 'r') as f:
    lines = f.readlines()
print(len(lines))

#Way3
print(sum([1 for _ in open('popular-names.txt', 'r')]))

#wcコマンド：wc popular-names.txt