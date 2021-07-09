import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_path,categories_path):
    messages_df = pd.read_csv(messages_path)
    categories_df = pd.read_csv(categories_path)
    df = pd.merge(messages_df, categories_df, on="id")
    return df

def clean_data(df):
    #Create a new column for all the items in categories and extract the values from them
    #First to split them into all the columns
    categories = df.categories.str.split(';',expand=True)
    #Get column names from the first row
    row = categories.iloc[0]
    category_colnames = [x[:-2] for x in row]
    #Rename categories columns with the list we jsut created
    categories.columns = category_colnames
    #Extract the values
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1:]

        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    #Change all the 2's to 1's
    categories = categories.replace([2],1)
    #Next, drop the old categories column
    df = df.drop('categories', axis = 1)
    #Then merge df with the categories df
    df = pd.concat([df, categories], axis=1)
    #Drop all the duplicates
    df.drop_duplicates(inplace=True)
    return df

def save_data(df):
    engine = create_engine(f'sqlite:///DisasterResponse.db')
    df.to_sql('DisasterData', engine, if_exists='replace' index=False)

def main():

    messages_path = 'messages.csv'
    categories_path = 'categories.csv'
    database_path = 'DisasterResponse'

    print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_path, categories_path))
    df = load_data(messages_path, categories_path)

    print('Cleaning data...')
    df = clean_data(df)

    print('Saving data...\n    DATABASE: {}'.format(database_path))
    save_data(df)

    print('Cleaned data saved to database!')

if __name__ == '__main__':
    main()
