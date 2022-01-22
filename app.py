from flask import Flask
from flask import jsonify
from flask import request
import json
import pandas as pd
import numpy as np
from recommender import *

app = Flask(__name__)

url_large = 'https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv'


#  column names for book.csv file 

columns_of_books_table = ['book_id','goodreads_book_id','best_book_id','work_id','books_count','isbn',
                            'isbn13','authors','original_publication_year','original_title','title',
                            'language_code','average_rating','ratings_count','work_ratings_count',
                            'work_text_reviews_count','ratings_1','ratings_2','ratings_3','ratings_4',
                            'ratings_5','image_url','small_image_url']

data = pd.read_csv(url_large, nrows=100)
data.fillna(value='field is empty', inplace = True)

all_books = data.to_json(orient='records', indent=4)

books = data.values.tolist()

# home page

@app.route('/', methods=['GET'])
def home():
    return json.dumps('API for recommendation systems: search by title (GET /api/books/recommend?title=Title Of Book) and it will return other similar books as json format')

# return all books from csv file

@app.route('/api/books/all', methods=['GET'])
def api_all():
    return all_books

# fix errors for finding books by title

@app.route('/api/books', methods=['GET'])
def api_title():
    
    if 'title' in request.args:
        title = str(request.args['title'])
    else:
        return json.dumps("Error: No title field provided. Please specify a title.")

    results = list()
    
    for book in books:
        if title.lower() in book[10].lower():
            results.append(book)

    results_df = pd.DataFrame(results, columns=columns_of_books_table)

    return results_df.to_json(orient='records', indent=4)




# fix errors for recommendation method

@app.route('/api/books/recommend', methods=['GET'])
def api_recommend():

    recommended_books = []

    if 'title' in request.args:
        title = str(request.args['title'])
        
        recommended_books = book_recommender(title)
        
    else:
        return json.dumps('Error: No title field provided. Please specify a title.')


    try:
        return recommended_books
    except:
        return jsonify("error occured")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)