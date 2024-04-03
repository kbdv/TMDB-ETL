# python 3.10.11


# This file creates the endpoints for our REST API.

# imports
import calendar
import sqlite3
from datetime import datetime
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS


# variables
from variables2 import database, main_query, bookmarks_query


# ------------------------------------------------------
# We create a class for our dataframe so that we can update it from any scope in this file.
class MyDataFrame:
    def __init__(self):
        self.df = pd.DataFrame()

# Create a single instance of that class
data = MyDataFrame()


app = Flask(__name__)   
CORS(app)       # Enable Cross Origin requests



# ------------------------------------------------------
# The default page. It load all movies of the previous month.
@app.route('/', methods=['GET'])
def retrieve_all_movies():
    with sqlite3.connect(database) as con:
        data.df = pd.read_sql_query(main_query,con)
    return jsonify(data.df.to_dict(orient='records'))


# Retrieve list of genres but only for the previous month's movies
@app.route('/genres', methods=['GET'])      
def retrieve_genres():
    with sqlite3.connect(database) as con:
        df_genre = pd.read_sql_query(main_query,con)
        genres = df_genre['genres'].unique()
        unique_genres = set() # creating a set for unique values of df['genres']

        # looping through the values of df['genres'] and extracting each string within the lists
        for genre in genres:
            if len(genre.split(', '))==1: 
                if genre not in unique_genres and genre != "":
                    unique_genres.add(genre)
            else:
                for string in genre.split(', '):
                    if string not in unique_genres and genre != "":
                        unique_genres.add(string)
    return jsonify(list(unique_genres))


# Retrieve the bookmarks table
@app.route('/bookmarks', methods=['GET'])
def retrieve_bookmarks():
    with sqlite3.connect(database) as con:
        df_bookmarks = pd.read_sql_query(bookmarks_query,con)
    return jsonify(df_bookmarks.to_dict(orient='records'))


# Sorting active dataframe by date descending
@app.route('/sort-date-desc', methods=['GET'])
def sort_date_desc():
    data.df = data.df.sort_values(by='release_date', ascending=False)   
    return jsonify(data.df.to_dict(orient='records'))


# Sorting active dataframe by date ascending
@app.route('/sort-date-asc', methods=['GET'])
def sort_date_asc():
    data.df = data.df.sort_values(by='release_date', ascending=True)   
    return jsonify(data.df.to_dict(orient='records'))


# Sorting active dataframe by rating descending
@app.route('/sort-rating-desc', methods=['GET'])
def sort_rating_desc():
    data.df = data.df.sort_values(by='rating', ascending=False)   
    return jsonify(data.df.to_dict(orient='records'))


# Sorting active dataframe by rating ascending
@app.route('/sort-rating-asc', methods=['GET'])
def sort_rating_asc():
    data.df = data.df.sort_values(by='rating', ascending=True)   
    return jsonify(data.df.to_dict(orient='records'))


# Filtering the current active dataframe by genre
@app.route('/filter-genre/<genre>', methods=['GET'])
def filter_by_genre(genre):
    segments = main_query.split('ORDER',1)
    genre_filter_query = f"{segments[0]} AND LOWER(genres) LIKE LOWER('%{genre}%')\nORDER {segments[1]}"
    with sqlite3.connect(database) as con:
        data.df = pd.read_sql_query(genre_filter_query,con)
    return jsonify(data.df.to_dict(orient='records'))


# Adding a new bookmark
@app.route('/add-bookmark', methods=['POST'])
def add_bookmark():
    data = request.json # retrieve the data sent to this endpoint
    df_add = pd.DataFrame([data]) 
    with sqlite3.connect(database) as con:
        df_add.to_sql('movies_bookmarks', con, if_exists='append', index=False)
    return 'Bookmark added', 200



