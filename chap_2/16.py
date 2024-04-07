import sys
n = int(sys.argv[1])
with open('popular-names.txt', 'r') as f:
    lines = f.readlines()
for i in range(n):
    with open(f'split_{i}.txt', 'w') as out_file:
        for line in lines[i*(len(lines)//n):(i+1)*(len(lines)//n)]:
            out_file.write(line)

# splitコマンドで確認：split -l $(expr $(wc -l < popular-names.txt) / N) popular-names.txt split_