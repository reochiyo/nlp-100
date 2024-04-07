with open('popular-names.txt', 'r') as f:
    lines = f.readlines()

sorted_lines = sorted(lines, key=lambda line: int(line.split('\t')[2]), reverse=True)

for line in sorted_lines:
    print(line, end='')

#確認コマンド：sort -k 3 -n -r popular-names.txt