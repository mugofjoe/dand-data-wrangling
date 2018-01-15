##  Congratulations on making it to the end!
##  Use the Hidden Phrases you've collected to fill in this script :)

database = "Awesome.db"
'''
HIDDEN MESSAGE #2: Fill in your table Schema!
###########################
#   Table Name: Udacious  #
###########################
     problemSet INTEGER, 
     node INTEGER,  
     queryId INTEGER, 
     title TEXT, 
     sql TEXT, 
     statement TEXT      
'''

QUERY = "SELECT sql, statement FROM Udacious WHERE queryId = 35;"

##  Have a look at how far you've come in your SQL journey.
##  Here are some examples of possible solutions to problems you've solved.
'''Remember your first query from WAY BACK in the first exercise?'''
#QUERY = '''SELECT sql, statement FROM Udacious WHERE lesson=1 AND exercise=1 AND queryId=7'''
'''How about when you started getting REALLY good in lesson 2?'''
#QUERY = '''SELECT sql, statement FROM Udacious WHERE lesson=2 AND exercise=9;'''
'''And by earlier this lesson you were busy building your own database already!'''
#QUERY = '''SELECT sql, statement FROM Udacious WHERE lesson=3 AND exercise=4 AND queryId = 31;'''

##  You've come a long way and it's awesome to see what you've accomplished!
##  Now take your new SQL skills and go explore the world :)


#  QUERY = '''SELECT sql, statement FROM Udacious WHERE lesson=1 AND exercise=1 AND queryId=7'''
            
SELECT  Composer, Name            
FROM    Track                     
WHERE   Composer = 'Jimi Hendrix';


'''How about when you started getting REALLY good in lesson 2?'''
# QUERY = '''SELECT sql, statement FROM Udacious WHERE lesson=2 AND exercise=9;'''

SELECT    Artist.Name as Artist, COUNT(Genre.Name) as count
FROM      Genre                                            
JOIN      Track                                            
ON        Genre.GenreId = Track.GenreId                    
JOIN      Album                                            
ON        Track.AlbumId = Album.AlbumId                    
JOIN      Artist                                           
ON        Album.ArtistId = Artist.ArtistId                 
WHERE     Genre.Name = 'Rock'                              
GROUP BY  Artist                                           
ORDER BY  count                                            
DESC      LIMIT 10;