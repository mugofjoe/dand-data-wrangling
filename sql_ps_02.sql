/*
##  Alright, now that you're warmed up let's get down to business!

##  In this problem set we'll pretend the Chinook database is the data for your own personal music shop!
##  We'll be marketing your shop and hosting Music Festival using answers we get from 
##  the data stored in your database.
##  Let's get started :)

##  First, you'd like to run a promotion targeting the 3 countries with the 
##  highest number of invoices.  

##  Write a query that returns the 3 countries with the highest number of invoices, along with the number ##  of invoices for these countries.
*/

-- Q-U-E-R-I


SELECT BillingCountry, COUNT(*)
FROM Invoice
GROUP BY BillingCountry
ORDER BY COUNT(*) DESC
LIMIT 3;

/*
##  The customer who has spent the most money will be declared your best customer.
##  They definitely deserve an email thanking them for their patronage :)  

##  Build a query that returns the person who has the highest sum of all invoices,
##  along with their email, first name, and last name.
*/

select Customer
.Email, Customer.FirstName, Customer.LastName, Invoices.Total
from Customer
join
(select CustomerId, sum(Total) as Total
from Invoice
group by CustomerId)
as Invoices
on Invoices.CustomerId = Customer.CustomerId
order by Invoices.Total DESC
limit 1;

