import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from utils.preprocessing import clean_text

def load_data(file_path):
    texts = []
    emotions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if ';' in line:
                text, emotion = line.rsplit(';', 1)
                texts.append(clean_text(text))
                emotions.append(emotion.strip())
    return pd.DataFrame({'text': texts, 'emotion': emotions})

#load and save cleaned datasets
train_df = load_data('data/train.txt')
test_df = load_data('data/test.txt')

train_df.to_csv('data/emotion_train.csv', index=False)
test_df.to_csv('data/emotion_test.csv', index=False)

#train model
X_train, y_train = train_df['text'], train_df['emotion']
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])
model.fit(X_train, y_train)

#save model
joblib.dump(model, 'model/emotion_model.pkl')
print("Model trained and saved as emotion_model.pkl")
