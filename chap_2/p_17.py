with open('popular-names.txt', 'r') as f:
    lines = f.readlines()
unique_strings = set(line.split()[0] for line in lines)
print(unique_strings)

# 確認コマンド：cut -f 1 popular-names.txt | sort | uniq