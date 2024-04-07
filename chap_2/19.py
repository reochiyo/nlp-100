from collections import Counter

with open('popular-names.txt', 'r') as f:
    lines = f.readlines()

names = [line.split('\t')[0] for line in lines]
name_freq = Counter(names)

for name, freq in name_freq.most_common():
    print(f'{name}: {freq}')

# 確認コマンド：cut -f 1 popular-names.txt | sort | uniq -c | sort -nr