/*
##  Now that we know that our customers love rock music, we can decide which musicians to 
##  invite to play at the concert. 

##  Let's invite the artists who have written the most rock music in our dataset.
##  Write a query that returns the Artist name and total track count of the top 10 rock bands. 
*/
-- 1297
-- QUERIESRFUN



select Artist.Name, count(Genre.Name)
from Genre
    join Track on Track.GenreId = Genre.GenreId
    join Album on Album.AlbumId = Track.AlbumId
    join Artist on Artist.ArtistId = Album.ArtistId
where Genre.Name = 'Rock'
group by Artist.Name
order by count(*) desc
limit 10;