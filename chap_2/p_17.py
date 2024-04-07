with open('popular-names.txt', 'r') as f, open('unique_strings.txt', 'w') as out_file:
    lines = f.readlines()
    unique_strings = set(line.split()[0] for line in lines)
    for string in unique_strings:
        out_file.write(string + '\n')
    print(unique_strings)

# 確認コマンド：cut -f 1 popular-names.txt | sort | uniq > unique_strings.txt