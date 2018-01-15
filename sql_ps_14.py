##
##  Congratulations on making it to the end!
## Use the Hidden Phrases you've collected to fill in this script :)
##
import sqlite3
import pandas as pd

# Fetch records from either chinook.db
db = sqlite3.connect("D:/Software/sqlite_windows/Chinook_Sqlite.sqlite")
c = db.cursor()

QUERY = '''
select Genre.Name, COUNT(*)
from Track, (select avg(Milliseconds) as AverageLength from Track),
Genre
where Track.Milliseconds < AverageLength
and Genre.GenreId = Track.GenreId
group by Genre.Name
order by COUNT(*) DESC
'''
c.execute(QUERY)
rows = c.fetchall()

df = pd.DataFrame(rows)
print df

db.close()