from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

x_train = pd.read_csv('train.feature.txt', sep='\t')

train = pd.read_csv('train.txt', sep='\t')
y_train = train['CATEGORY']

model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)

#CountVectorizerのインスタンスを作成
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')

#ボキャブラリの学習
vectorizer.fit(x_train)

#記事の見出しの例
example_headline = "Apple launches new product"

#記事の見出しを特徴量に変換
x = vectorizer.transform([example_headline])

#引数の方を変換
x_data = pd.DataFrame(x)

#ロジスティック回帰モデルでカテゴリを予測
predicted_category = model.predict(x_data)

#予想確率の計算
predicted_probability = model.predict_proba(x)

print(f'Predicted category:{predicted_category}')
print(f'Predicted probability:{predicted_probability}')
