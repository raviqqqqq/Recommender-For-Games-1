#This script contains the logic for the filter based recommendation system
#Function for fuzzy searching
import pandas as pd
from thefuzz import fuzz, process
import numpy as np

def recommend_game(title, category, genre):
    df = pd.read_csv('Steam_Cleaned.csv')
    df.drop(columns = ['Unnamed: 0'], inplace = True)
    df = df.loc[df['steam_appid'] != 2639280]
    df.drop(columns = ['steam_appid','lang','name_translated', 'dev_translated', 'pub_translated', 'n_achievements','review_score','review_score_desc', 'positive_percentual','metacritic', 'is_free', ], inplace = True)

    # No Input case 
    if title == '' and category == ['None'] and genre == ['None']:
        return None 

    
    # if we get title we intialize fuzzy searching 
    if title:
        df['similarity'] = df['name'].apply(lambda x: fuzz.token_sort_ratio(title, x))

    # Create filter conditions dynamically
    conditions = []

    if category and 'None' not in category:
        conditions.append(df['categories'].str.contains('|'.join([c.lower() for c in category]), case=False))

    if genre and 'None' not in genre:
        conditions.append(df['genres'].str.contains('|'.join([g.lower() for g in genre]), case=False))

    # Apply all conditions
    if conditions:
        df = df.loc[pd.concat(conditions, axis=1).all(axis=1)]

    # Sort if title similarity is used
    if title:
        df = df.sort_values(by='similarity', ascending=False)

    return df if not df.empty else None

