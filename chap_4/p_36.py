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

most_common_10 = word_counter.most_common()[:10]

words, counts = zip(*most_common_10)

plt.figure(figsize=(10, 6))
plt.bar(words, counts)
plt.title('出現頻度が高い10語とその出現頻度')
plt.xlabel('単語')
plt.ylabel('出現頻度')
plt.show()