#https://qiita.com/musaprg/items/9a572ad5c4e28f79d2ae
#brew install crf++
#brew install mecab mecab-ipadic
#git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
#cd mecab-ipadic-neologd
#./bin/install-mecab-ipadic-neologd -n
#brew install cabocha
#pip install mecab-python3
#git clone https://github.com/taku910/cabocha.git
#cd cabocha
#pip insatll python/

import CaboCha

def parse_text(input_file, output_file):
    c = CaboCha.Parser()
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            tree = c.parse(line)
            f_out.write(tree.toString(CaboCha.FORMAT_XML))

input_file = 'ai.ja.txt'
output_file = 'ai.ja.txt.parsed'
parse_text(input_file, output_file)