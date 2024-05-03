from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re

def Process(lines):
    sign_regrex = re.compile('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`|＄＃＠£â€™é\n]')
    lines = sign_regrex.sub("", lines)
    lines = re.sub("(\d+)", r" \1 ", lines)
    texts = lines.split(" ")
    texts = list(filter(lambda x:x, texts))
    word_list = list(map(lambda x:x.lower(), texts))
    return word_list

train = pd.read_csv('train.txt', sep='\t')
valid = pd.read_csv('valid.txt', sep='\t')
test = pd.read_csv('test.txt', sep='\t')

vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')

X_train = vectorizer.fit_transform(train['TITLE'])
X_valid = vectorizer.transform(valid['TITLE'])
X_test = vectorizer.transform(test['TITLE'])

pd.DataFrame(X_train.toarray(), columns=vectorizer.get_feature_names_out()).to_csv('train.feature.txt', sep='\t', index=False)
pd.DataFrame(X_valid.toarray(), columns=vectorizer.get_feature_names_out()).to_csv('valid.feature.txt', sep='\t', index=False)
pd.DataFrame(X_test.toarray(), columns=vectorizer.get_feature_names_out()).to_csv('test.feature.txt', sep='\t', index=False)