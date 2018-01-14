/*
##  It would be really helpful to know what type of music everyone likes before 
##  throwing this festival.
##  Lucky for us we've got the data to find out!  
##  We should be able to tell what music people like by figuring out what music they're buying.

##  Write a query that returns the BillingCity,total number of invoices 
##  associated with that particular genre, and the genre Name.

##  Return the top 3 most popular music genres for the city Prague
##  with the highest invoice total (you found this in the previous quiz!)
*/
-- 14
-- 76

select Invoice.BillingCity, COUNT(*), Genre.Name
from Invoice
    join InvoiceLine on InvoiceLine.InvoiceId = Invoice.InvoiceId
    join Track on Track.TrackId = InvoiceLine.TrackId
    join Genre on Genre.GenreId = Track.GenreId
where BillingCity = "Prague"
group by Genre.Name
order by COUNT(Genre.Name) desc
limit 3;