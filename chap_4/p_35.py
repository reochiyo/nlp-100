import  p_30
from collections import Counter

results = p_30.read_mecab('neko.txt.mecab')

word_list=[]
for line in results:
    for text in line:
        if text['pos'] != '記号' and text['pos'] != '助詞' and text['pos'] != '助動詞':
            word_list.append(text['base'])

word_counter = Counter(word_list)

print(word_counter.most_common()[:10])