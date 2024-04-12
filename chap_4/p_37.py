import  p_30
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib 

results = p_30.read_mecab('neko.txt.mecab')

cat_list=[]
for line in results:
    word_list = []
    Flag = False
    for text in line:
        if text['surface'] == '猫':
            Flag = True
        if text['pos'] != '記号' and text['pos'] != '助詞' and text['pos'] != '助動詞' and text['surface'] != '猫':
            word_list.append(text['surface'])
    if Flag:
        cat_list.extend(word_list)

cat_counter = Counter(cat_list)

most_common_10 = cat_counter.most_common()[:10]

words, counts = zip(*most_common_10)

plt.figure(figsize=(10, 6))
plt.bar(words, counts)
plt.title('「猫」とよく共起する10語とその出現頻度')
plt.xlabel('単語')
plt.ylabel('出現頻度')
plt.show()