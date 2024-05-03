from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

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