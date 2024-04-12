import  p_30

results = p_30.read_mecab('neko.txt.mecab')

no_list=[]
for line in results:
    for i in range(1, len(line)-1):
        if line[i-1]['pos'] == '名詞' and line[i]['surface'] == 'の' and line[i+1]['pos'] == '名詞':
            no_list.append(line[i-1]['surface']+line[i]['surface']+line[i+1]['surface'])
print(no_list[:10])