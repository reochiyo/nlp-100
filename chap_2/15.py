import sys
n = int(sys.argv[1])
with open('popular-names.txt', 'r') as f, open('tail.txt', 'w') as out_file:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if i > len(lines) - n:
            out_file.write(line)
        else:
            continue

# tailコマンドで確認：tail -n 5 popular-names.txt > tail.txt