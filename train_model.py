import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('dataset/mental_health_sentiment.csv')
X = data['text']
y = data['sentiment']

vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

with open('model/sentiment_model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)

print('Model trained and saved')
