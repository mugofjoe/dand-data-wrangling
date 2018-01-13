/*
Chinook Database
https://chinookdatabase.codeplex.com/
*/

select strftime('%Y',InvoiceDate), sum(Total)
from invoice
group by strftime('%Y',InvoiceDate)
order by sum(Total) desc;


"SELECT sql, statement FROM Udacious WHERE queryId = 35;"
