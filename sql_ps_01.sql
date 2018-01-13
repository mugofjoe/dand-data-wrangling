/*
Chinook Database
https://chinookdatabase.codeplex.com/
*/

-- what year has the largest total sales
select strftime('%Y',InvoiceDate), sum(Total)
from invoice
group by strftime('%Y',InvoiceDate)
order by sum(Total) desc;


select sum(total)
from (select count(*) as total
    from Invoice
    group by BillingCountry
    order by total desc
limit 5);


select count
(*) as total 
from Invoice
group by BillingCountry
order by total desc
limit 5;

-- Hidden code pieces:
-- 1 - U
-- 2 - D
-- 3 - A

-- Find customers whose total invoice amount is higher than the avarage.
-- Return the city, state, country and total

select BillingCity, BillingState, BillingCountry, Total
from Invoice,
    (select avg(Total) as average
    from Invoice) as subquery
where Total > average;


-- what is the name, city, state, country, and total
-- of customers with above average invoice totals?
select FirstName, LastName, BillingCity, BillingState, BillingCountry, Total
from Invoice join Customer on Invoice.CustomerId = Customer.CustomerId join
    (select avg(Total) as average
    from Invoice) as subquery 
where Total > average;