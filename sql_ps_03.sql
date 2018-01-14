/*
##  Rock Music Lives on!  After the success of your recent email campaign,  
##  you're interested in targeting your long standing Rock Music audience!
##  You'll need to collect a list of emails containing each of your Rock Music listeners.

##  Use your query to return the email, first name, last name, and Genre of all Rock Music listeners!
##  Return you list ordered alphabetically by email address starting with A.
##  Can you find a way to deal with duplicate email addresses so no one receives multiple emails?
*/

select Customer.Email, Customer.FirstName, Customer.LastName, Genre.Name
from Customer
    join Invoice on Invoice.CustomerId = Customer.CustomerId
    join InvoiceLine on InvoiceLine.InvoiceId = Invoice.InvoiceId
    join Track on Track.TrackId = InvoiceLine.TrackId
    join Genre on Genre.GenreId = Track.GenreId
where Genre.Name = "Rock"
)
group by Customer.CustomerId
order by Customer.Email ASC;
