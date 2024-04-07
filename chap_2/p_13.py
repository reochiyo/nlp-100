with open('col1.txt', 'r') as col1, open('col2.txt', 'r') as col2, open('merge.txt', 'w') as out_file:
    for line1, line2 in zip(col1, col2):
        out_file.write(line1.strip() + '\t' + line2.strip() + '\n')

# pasteコマンドで確認：paste col1.txt col2.txt > merge.txt