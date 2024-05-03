from sklearn.linear_model import LogisticRegression
import pandas as pd

#特徴量データの読み込み
x_train = pd.read_csv('train.feature.txt', sep='\t')

#ラベルデータの読み込み
train = pd.read_csv('train.txt', sep='\t')
y_train = train['CATEGORY']

#ロジスティック回帰モデルの学習
model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)