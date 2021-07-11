import pandas as pd
import sys
import re
import pickle
from sqlalchemy import create_engine

import nltk
nltk.download(['punkt', 'wordnet'])

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

def load_data(database_path):
    engine = create_engine(f'sqlite:///{database_path}')
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


def build_model(database_path):
    '''Loads in the data, splits out into training and tests sets then runs a randomforestclassifier model
    '''
    database_path = database_path
    X, y = load_data(database_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier(verbose=2)))
    ])

    params = {
        'clf__estimator__n_estimators': [50, 150]
    }

    cv = GridSearchCV(pipeline, param_grid=params)
    cv.fit(X_train, y_train)
    #y_pred = cv.predict(X_test)

    return cv, X_test, y_test#X_test, y_test

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    #precision = precision_score(y_test, y_pred)
    #recall = recall_score(y_test, y_pred)
    #f1 = f1_score(y_test, y_pred)
    Y_pred = pd.DataFrame(y_pred, columns=y_test.columns)

    for column in y_test.columns:
        print(f'Model performance on category {column}')
        print(classification_report(y_test[column],Y_pred[column]))



def save_model(model, model_path):
    pickle.dump(model, open(f'{model_path}', 'wb'))

def main():
    if len(sys.argv) == 3:
        database_path, model_path = sys.argv[1:]
        print('Please be paitent as the model is built')
        model, X_test, y_test = build_model(database_path)
        #model, y_pred, y_test = build_model(database_path)
        print('evaluating the model')
        evaluate_model(model, X_test, y_test)
        print(f'Saving model as: {model_path}')
        save_model(model, model_path)

if __name__ == '__main__':
    main()
