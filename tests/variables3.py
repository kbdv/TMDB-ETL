# variables

server = "https://tmdb-host.azurewebsites.net"
database = "./kb_movies.db"
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

cols = {'title', 'genres', 'release_date', 'rating'}