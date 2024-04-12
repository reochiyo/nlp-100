import  p_30
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib 
import numpy as np

results = p_30.read_mecab('neko.txt.mecab')

word_list=[]
for line in results:
    for text in line:
        if text['pos'] != '記号' and text['pos'] != '助詞' and text['pos'] != '助動詞':
            word_list.append(text['surface'])

word_counter = Counter(word_list)

most_common_order = word_counter.most_common()

words, counts = zip(*most_common_order)

counts_sorted = sorted(counts, reverse=True)

ranks = np.arange(1, len(counts_sorted) + 1)

plt.figure(figsize=(10, 6))
plt.plot(ranks, counts_sorted)
plt.xscale('log')
plt.yscale('log')
plt.title('Zipfの法則')
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.show()