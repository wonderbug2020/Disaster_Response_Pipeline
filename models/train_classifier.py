import pandas as pd
import re
import pickle
from sqlalchemy import create_engine

import nltk
nltk.download(['punkt', 'wordnet'])

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

def load_data():
    engine = create_engine('sqlite:///../data/DisasterResponse.db')
    df = pd.read_sql_table('DisasterData', engine)
    X = df.message
    y = df.drop(['id','message', 'original', 'genre'], axis=1)
    category_names = y.columns
    return X, y#, category_names


def tokenize(text):
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    '''Loads in the data, splits out into training and tests sets then runs a randomforestclassifier model
    '''
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    # train classifier
    pipeline.fit(X_train, y_train)

    return pipeline


def save_model(model):
    pickle.dump(model, open('model_2.pkl', 'wb'))

def main():
    model = build_model()
    save_model(model)

if __name__ == '__main__':
    main()
