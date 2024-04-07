count = 0
with open('popular-names.txt', 'r') as f, open('col1.txt', 'w') as col1, open('col2.txt', 'w') as col2:
    for line in f:
        if count == 0:
            col1.write(line.strip())
            count += 1
        elif count == 1:
            col2.write(line.strip())
            count += 1
        else:
            break

# cutコマンドで確認：cut -f 1 popular-names.txt > col1.txt 
# cutコマンドで確認：cut -f 2 popular-names.txt > col2.txt