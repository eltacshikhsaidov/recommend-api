import numpy as np
import pandas as pd
import json
from sklearn.cluster import KMeans
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

url_large = 'https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv'
df = pd.read_csv(url_large, nrows=10000)
df.fillna(value='field is empty', inplace = True)

df2 = df.copy()

df2.loc[ (df2['average_rating'] >= 0) & (df2['average_rating'] <= 1), 'rating_between'] = "between 0 and 1"
df2.loc[ (df2['average_rating'] > 1) & (df2['average_rating'] <= 2), 'rating_between'] = "between 1 and 2"
df2.loc[ (df2['average_rating'] > 2) & (df2['average_rating'] <= 3), 'rating_between'] = "between 2 and 3"
df2.loc[ (df2['average_rating'] > 3) & (df2['average_rating'] <= 4), 'rating_between'] = "between 3 and 4"
df2.loc[ (df2['average_rating'] > 4) & (df2['average_rating'] <= 5), 'rating_between'] = "between 4 and 5"

rating_df = pd.get_dummies(df2['rating_between'])
language_df = pd.get_dummies(df2['language_code'])

features = pd.concat([rating_df, 
                      language_df, 
                      df2['average_rating'], 
                      df2['ratings_count']], axis=1)

min_max_scaler = MinMaxScaler()
features = min_max_scaler.fit_transform(features)

model = neighbors.NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
model.fit(features)
dist, idlist = model.kneighbors(features)

def book_recommender(book_name):
    book_df = pd.DataFrame()

    try:
        book_id = df2[df2['original_title'] == book_name.title()].index
        book_id = book_id[0]
        for newid in idlist[book_id]:
            mask = df2['book_id'] == newid
            df_new = pd.DataFrame(df2[mask])
            book_df = book_df.append(df_new)
        return book_df.to_json(orient='records', indent=4)
    except:
        return json.dumps("there is no such a book based on your search.")