import  p_30

results = p_30.read_mecab('neko.txt.mecab')

verb_surface_list=[]
for line in results:
    for text in line:
        if text['pos'] == '動詞':
            verb_surface_list.append(text['surface'])

print(verb_surface_list[:10])