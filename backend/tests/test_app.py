# python 3.10.11

# This file defines a set of tests for our REST API endpoints.
# The tests can be run by entering the command 'pytest' in the terminal.


# imports
import pytest
import pandas as pd
import numpy as np
import sqlite3
import json
import requests
import unittest
from unittest.mock import patch, Mock


# variables
from backend.variables2 import server, database, mock_rows, mock_row, mock_list
database = './' + database


# Functions to test
def get_bookmarks():
    response = requests.get(server + '/bookmarks')
    return response.json()
def get_genres():
    response = requests.get(server + '/genres')
    return response.json()
def get_sort_date_desc():
    response = requests.get(server + '/sort-date-desc')
    return response.json()
def get_sort_date_asc():
    response = requests.get(server + '/sort-date-asc')
    return response.json()
def get_sort_rating_desc():
    response = requests.get(server + '/sort-rating-desc')
    return response.json()
def get_sort_rating_asc():
    response = requests.get(server + '/sort-rating-asc')
    return response.json()
def get_filter_genre(genre):
    response = requests.get(server + f'/filter-genre/{genre}')
    return response.json()
def post_add_bookmark(bookmark):
    body = json.dumps(bookmark)
    response = requests.post(server + '/add-bookmark', json=body)
    return response.json()




# ------------------------------------------------------
# 1. verify that the backend connects
def test_backend_connect():
    assert requests.head(server).status_code == 200

# 2. verify get_bookmarks()
class TestGetBookmarks(unittest.TestCase):
    @patch('requests.get')
    def test_get_bookmarks(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_rows
        mock_get.return_value = mock_response

        data = get_bookmarks()
        mock_get.assert_called_with(server + '/bookmarks')
        self.assertEqual(data, mock_rows)

# 3. verify get_genres()
class TestGetGenres(unittest.TestCase):
    @patch('requests.get')
    def test_get_genres(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_list
        mock_get.return_value = mock_response

        data = get_genres()
        mock_get.assert_called_with(server + '/genres')
        self.assertEqual(data, mock_list)


# 4. verify get_sort_date_desc()
class TestSortByDateDesc(unittest.TestCase):
    @patch('requests.get')
    def test_get_sort_date_desc(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_rows
        mock_get.return_value = mock_response

        data = get_sort_date_desc()
        mock_get.assert_called_with(server + '/sort-date-desc')
        self.assertEqual(data, mock_rows)

# 5. verify get_sort_date_asc()
class TestSortByDateAsc(unittest.TestCase):
    @patch('requests.get')
    def test_get_sort_date_asc(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_rows
        mock_get.return_value = mock_response

        data = get_sort_date_asc()
        mock_get.assert_called_with(server + '/sort-date-asc')
        self.assertEqual(data, mock_rows)

# 6. verify get_sort_rating_desc()
class TestSortByRatingDesc(unittest.TestCase):
    @patch('requests.get')
    def test_get_sort_rating_desc(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_rows
        mock_get.return_value = mock_response

        data = get_sort_rating_desc()
        mock_get.assert_called_with(server + '/sort-rating-desc')
        self.assertEqual(data, mock_rows)

# 7. verify get_sort_rating_asc()
class TestSortByRatingAsc(unittest.TestCase):
    @patch('requests.get')
    def test_get_sort_rating_asc(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_rows
        mock_get.return_value = mock_response

        data = get_sort_rating_asc()
        mock_get.assert_called_with(server + '/sort-rating-asc')
        self.assertEqual(data, mock_rows)

# 8. verify get_filter_genre(genre)
class TestFilterByGenre(unittest.TestCase):
    @patch('requests.get')
    def test_get_filter_genre(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_rows
        mock_get.return_value = mock_response

        genre = 'comedy'
        data = get_filter_genre(genre)
        mock_get.assert_called_with(server + f'/filter-genre/{genre}')
        self.assertEqual(data, mock_rows)

# 9. verify post_add_bookmark(bookmark)
class TestAddBookmark(unittest.TestCase):
    @patch('requests.post')
    def test_post_add_bookmark(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {'status': 200}
        mock_post.return_value = mock_response

        data = post_add_bookmark(mock_row)
        mock_post.assert_called_with(server + '/add-bookmark', json = json.dumps(mock_row))
        self.assertEqual(data, {'status': 200})