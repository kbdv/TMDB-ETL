import pytest
import pandas as pd
import numpy as np
import sqlite3



# setting variables
database = '../kb_movies.db'
cols = {'title', 'genres', 'release_date', 'rating'}

# Loading the bronze and silver tables
with sqlite3.connect(database) as con:
    df_bronze = pd.read_sql_query("SELECT * FROM movies_bronze", con)
    df_silver = pd.read_sql_query("SELECT * FROM movies_silver", con)


#-----------------------------------------------

# 1. verify that the columns are correct in bronze and silver table
def test_col():
    for df in [df_bronze, df_silver]:
        assert cols == set(df.columns)



# 2. verify that there are no nulls in silver
def test_nulls():
    for df in [df_silver]:
        assert df.isna().sum().sum() == 0


# 3. verify that there are no duplicates in silver
def test_dupes():
    for df in [df_silver]:
        assert df.duplicated().sum() == 0


# 4. verify the datatypes in bronze and silver
def test_types():
    for df in [df_bronze, df_silver]:
        for col in cols:
            if col == 'rating':
                assert df[col].dtype == 'float64'
            else:
                assert df[col].dtype == 'O' or df[col].dtype == str


# 5. verify the range of ratings for bronze and silver
def test_rating_range():
    for df in [df_bronze, df_silver]:
        assert df['rating'].between(0,10).any()



# 6. verify that at least the bronze, silver and bookmarks table exist
def verify_num_tables():
    with sqlite3.connect(database) as con:
        tables = con.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
    assert ['movies_bronze, movies_silver, movies_bookmark'] in tables


# 7 Verify that the main query for our app is valid 
def verify_app_query():    
    with sqlite3.connect(database) as con:
        df_app = pd.read_sql_query(f'''
            SELECT * 
            FROM movies_silver
            WHERE strftime('%m %Y', release_date) == strftime('%m %Y', date('now','start of month','-1 month'))
            ORDER BY rating DESC;
            ''', con)
    assert not df_app.empty

