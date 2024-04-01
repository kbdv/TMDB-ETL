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