# Primary Key

- A primary key is a column or a combination of columns in a relational database table that uniquely identifies each record in the table .
- A primary key is a choice of candidate key, which is a minimal superkey, meaning that it has the smallest possible number of columns that can uniquely identify each record .
- A primary key can be either natural or surrogate. A natural key is based on real-world observables, such as a social security number or an email address. A surrogate key is created to function as a key and not used for identification outside the database, such as an auto-incremented ID or a UUID .
- A primary key must be entered when a record is created, and it should never be changed. It must not contain null values .
- A primary key is used as a unique identifier to quickly parse data within the table and to link to related information in other tables through foreign keys  .
- A primary key can be simple or composite. A simple primary key consists of a single column, while a composite primary key consists of two or more columns.