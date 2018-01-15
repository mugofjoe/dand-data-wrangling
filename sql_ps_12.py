##
## How many unique customers have purchased a Jazz track?
##
import sqlite3
import pandas as pd

# Fetch records from either chinook.db
db = sqlite3.connect("D:/Software/sqlite_windows/Chinook_Sqlite.sqlite")
c = db.cursor()

QUERY = '''
select COUNT(*)
from (
select CUS.CustomerId
from Customer CUS
join Invoice INV on INV.CustomerId = CUS.CustomerID
join InvoiceLine INL on INL.InvoiceId = INV.InvoiceId
join Track TRC on TRC.TrackId = INL.TrackId
join Genre GNR on GNR.GenreId = TRC.GenreId
where GNR.Name = 'Jazz'
group by CUS.CustomerId) as QRY1;


'''
c.execute(QUERY)
rows = c.fetchall()

df = pd.DataFrame(rows)
print df

db.close()