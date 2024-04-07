with open('popular-names.txt', 'r') as f, open('result.txt', 'w') as out_file:
    for line in f:
        out_file.write(line.strip().replace('\t', ' ') + '\n')

#sedコマンドで確認：sed 's/\t/ /g' popular-names.txt > result.txt