# python 3.10.11

# This file defines a set of tests for our ETL notebook.
# The tests can be run by entering the command 'pytest' in the terminal.

# imports
import pytest
import pandas as pd
import numpy as np
import sqlite3
import requests
import sys

# variables
from variables3 import database, cols



#-----------------------------------------------
# 1. verify that the tables 'movies_bronze', 'movies_silver' 'movies_bookmarks' and 'genre_list' exist in the database
def test_db_exist():
    with sqlite3.connect(database) as con:
        df_tables = pd.read_sql_query(f'''
            SELECT name 
            FROM sqlite_master 
            WHERE type='table' AND name in ('movies_bronze', 'movies_silver', 'movies_bookmarks', 'genre_list');
        ''', con)
        assert df_tables.shape[0] == 4


#-----------------------------------------------
# Loading the tables
with sqlite3.connect(database) as con:
    df_bronze = pd.read_sql_query("SELECT * FROM movies_bronze", con)
    df_silver = pd.read_sql_query("SELECT * FROM movies_silver", con)
    df_genres = pd.read_sql_query("SELECT * FROM genre_list", con)


#-----------------------------------------------
# 2. verify that the columns are correct in bronze and silver table
def test_col():
    for df in [df_bronze, df_silver]:
        assert cols == set(df.columns)



# 3. verify that there are no nulls in silver and genre_list
def test_nulls():
    for df in [df_silver, df_genres]:
        assert df.isna().sum().sum() == 0


# 4. verify that there are no duplicates in silver and genre_list
def test_dupes():
    for df in [df_silver, df_genres]:
        assert df.duplicated().sum() == 0


# 5. verify the datatypes in bronze and silver
def test_types():
    for df in [df_bronze, df_silver]:
        for col in cols:
            if col == 'rating':
                assert df[col].dtype == 'float64'
            else:
                assert df[col].dtype == 'O' or df[col].dtype == str


# 6. verify the range of ratings for bronze and silver
def test_rating_range():
    for df in [df_bronze, df_silver]:
        assert df['rating'].between(0,10).any()


# 7. verify the columns of genre_list
def test_col_genres():
    assert set(['id', 'name']) == set(df_genres.columns)

# 8. verify the types of genre_list
def test_type_genres():
    assert df_genres['id'].dtype == 'int64' and df_genres['name'].dtype == 'O'


# 9. verify that the main query for our REST API is valid 
def test_verify_app_query():    
    with sqlite3.connect(database) as con:
        df_app = pd.read_sql_query(f'''
            SELECT * 
            FROM movies_silver
            WHERE strftime('%m %Y', release_date) == strftime('%m %Y', date('now','start of month','-1 month'))
            ORDER BY rating DESC;
            ''', con)
    assert not df_app.empty
