import  p_30
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib 

results = p_30.read_mecab('neko.txt.mecab')

word_list=[]
for line in results:
    for text in line:
        if text['pos'] != '記号' and text['pos'] != '助詞' and text['pos'] != '助動詞':
            word_list.append(text['surface'])

word_counter = Counter(word_list)

most_common_order = word_counter.most_common()

words, counts = zip(*most_common_order)

plt.figure(figsize=(10, 6))
plt.hist(counts, bins=100)
plt.title('出現頻度のヒストグラム')
plt.xlabel('出現頻度')
plt.ylabel('単語の種類')
plt.show()