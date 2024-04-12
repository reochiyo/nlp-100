#参考：https://zenn.dev/sinozu/articles/44f58dddb25c03f8f05e
#brew install mecab mecab-ipadic
#pip install mecab-python3
#git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
#cd mecab-ipadic-neologd
#./bin/install-mecab-ipadic-neologd -n
#echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
#tagger = MeCab.Tagger("-r /dev/null -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd")とする

import MeCab

tagger = MeCab.Tagger("-r /dev/null -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd")

with open('neko.txt', 'r', encoding='utf-8') as f1, open('neko.txt.mecab', 'w', encoding='utf-8') as f2:
    lines = f1.readlines()
    for text in lines:
        result = tagger.parse(text)
        f2.write(result)