##
## How many pop songs have an MPEG audio file type?
##
import sqlite3
import pandas as pd

# Fetch records from either chinook.db
db = sqlite3.connect("D:/Software/sqlite_windows/Chinook_Sqlite.sqlite")
c = db.cursor()

QUERY = '''
select COUNT(*)
-- Track.TrackId, Track.Name, Genre.Name, MediaType.Name
from Track
join Genre on Genre.GenreId = Track.GenreId
join MediaType on MediaType.MediaTypeId = Track.MediaTypeId
where MediaType.Name = 'MPEG audio file' and Genre.Name = 'Pop'
'''
c.execute(QUERY)
rows = c.fetchall()

df = pd.DataFrame(rows)
print df

db.close()