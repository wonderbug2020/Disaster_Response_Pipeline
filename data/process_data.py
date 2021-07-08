import sys
import pandas as pd

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
    categories.head()
    #Next, drop the old categories column
    df = df.drop('categories', axis = 1)
    #Then merge df with the categories df
    df = pd.concat([df, categories], axis=1)
    #Drop all the duplicates
    df.drop_duplicates(inplace=True)
    return df

def save_data(df, database_name):
    pass
