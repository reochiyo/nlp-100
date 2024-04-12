import  p_30

results = p_30.read_mecab('neko.txt.mecab')

noun_list=[]
for line in results:
    word=""
    count=0
    for i in range(len(line)):
        if line[i]['pos'] == '名詞':
            word+=line[i]['surface']
            count+=1
        else:
            if count >= 2:
                noun_list.append(word)
            word=""
            count=0

print(noun_list[:10])