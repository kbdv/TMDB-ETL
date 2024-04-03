# variables

database ='kb_movies.db'
main_query = '''
    SELECT * 
    FROM movies_silver
    WHERE strftime('%m %Y', release_date) == strftime('%m %Y', date('now','start of month','-1 month'))
    ORDER BY rating DESC;
        '''
bookmarks_query = '''
    SELECT * 
    FROM movies_bookmarks;
        '''
base_url = 'https://api.themoviedb.org/3'

cols = {'title', 'genres', 'release_date', 'rating'}

server = "https://tmdb-host.azurewebsites.net"

mock_rows = [
    {'title':'blankTitle1','genres':'blankGenres1', 'release_date':'2000-01-01', 'rating':0.0},
    {'title':'blankTitle2','genres':'blankGenres2', 'release_date':'2010-01-01', 'rating':4.0},
    {'title':'blankTitle3','genres':'blankGenres3', 'release_date':'2020-01-01', 'rating':5.0}
]
mock_row ={
    'title':'blankTitle',
    'genres':'blankGenre', 
    'release_date':'2000-01-01', 
    'rating':0.0
}
mock_list = {'list':['one', 'two', 'three']}