#pip install pandas
#pip install scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('news+aggregator/newsCorpora.csv', sep='\t', header=None, names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

df = df[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]

df = df.sample(frac=1, random_state=0)

train, valid_test = train_test_split(df, test_size=0.2)
valid, test = train_test_split(valid_test, test_size=0.5)

train[['CATEGORY', 'TITLE']].to_csv('train.txt', sep='\t', index=False)
valid[['CATEGORY', 'TITLE']].to_csv('valid.txt', sep='\t', index=False)
test[['CATEGORY', 'TITLE']].to_csv('test.txt', sep='\t', index=False)

print('【Category distribution】')
print('train:', train['CATEGORY'].value_counts())
print('valid:', valid['CATEGORY'].value_counts())
print('test:', test['CATEGORY'].value_counts())