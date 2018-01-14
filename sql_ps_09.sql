/*
Create the InvoiceLine table.
*/

-- CREATE TABLE InvoiceLine
-- (
--     InvoiceLineId INTEGER PRIMARY KEY,
--     UnitPrice NUMERIC(10,2),
--     Quantity INTEGER,
--     FOREIGN KEY (InvoiceId) REFERENCES Invoice (InvoiceId)
--                 ON DELETE NO ACTION ON UPDATE NO ACTION,
--     FOREIGN KEY ([TrackId]) REFERENCES [Track] ([TrackId])
--                 ON DELETE NO ACTION ON UPDATE NO ACTION

-- );


CREATE TABLE InvoiceLine
(
    InvoiceLineId INTEGER PRIMARY KEY,
    UnitPrice NUMERIC(10,2),
    Quantity INTEGER,
    FOREIGN KEY (InvoiceId) REFERENCES Invoice (InvoiceId)
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES [Track] ([TrackId])
                ON DELETE NO ACTION ON UPDATE NO ACTION

);