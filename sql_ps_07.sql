/*
##  The show was a huge hit! Congratulations on all your hard work :)  
##  After the popularity of your first show you've decided to jump on the
##  railway for an Alternative & Punk tour through France!  

##  What does the alternative punk scene look like throughout French 
##  cities in your dataset?

##  Return the BillingCities in France, followed by the total number of 
##  tracks purchased for Alternative & Punk music.
##  Order your output so that the city with the highest total number of
##  tracks purchased is on top.
*/
-- 2240
-- 244
-- QUERIESRFU

select Invoice.BillingCity, COUNT(*) as NumTracks
from Invoice
    join InvoiceLine on InvoiceLine.InvoiceId = Invoice.InvoiceId
    join Track on Track.TrackId = InvoiceLine.TrackId
    join Genre on Genre.GenreId = Track.GenreId
where Genre.Name = 'Alternative & Punk'
    and BillingCountry = 'France'
group by Invoice.BillingCity
order by COUNT(*) desc;


select Album.Title, Track.Name, MediaType.Name
from Track
    join MediaType on MediaType.MediaTypeId = Track.MediaTypeId
    join Album on Album.AlbumId = Track.AlbumId
where MediaType.Name = 'Protected MPEG-4 video file';

/**
HIDDEN PHRASE 1 of 3: 


"SELECT sql, statement FROM Udacious WHERE queryId = 35;"


After unlocking all the phrases you'll be ready to collect your gift at the end of the course :)
**/


-- HIDDEN PHRASE: Table Name: Udacious
-- COLUMNS: problemSet INTEGER, node INTEGER,  queryId INTEGER, title TEXT, sql TEXT, statement TEXT"

-- DVDs with the highest sales
select Album.Title, sum((InvoiceLine.UnitPrice * InvoiceLine.Quantity))
from InvoiceLine
    join Track on Track.TrackId = InvoiceLine.TrackId
    join MediaType on MediaType.MediaTypeId = Track.MediaTypeId
    join Album on Album.AlbumId = Track.AlbumId
where MediaType.Name = 'Protected MPEG-4 video file'
group by Album.Title
order by sum((InvoiceLine.UnitPrice * InvoiceLine.Quantity)) desc
limit 3;


