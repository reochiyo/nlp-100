import sys
n = int(sys.argv[1])
with open('popular-names.txt', 'r') as f, open('head.txt', 'w') as out_file:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if i <= n:
            out_file.write(line)
        else:
            break

# headコマンドで確認：head -n 5 popular-names.txt > head.txt