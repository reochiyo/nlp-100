import  p_30

results = p_30.read_mecab('neko.txt.mecab')

verb_base_list=[]
for line in results:
    for text in line:
        if text['pos'] == '動詞':
            verb_base_list.append(text['base'])

print(verb_base_list[:10])