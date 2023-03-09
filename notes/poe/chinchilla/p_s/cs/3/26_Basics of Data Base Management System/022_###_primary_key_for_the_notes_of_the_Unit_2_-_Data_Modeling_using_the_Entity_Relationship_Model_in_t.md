### Primary Key

A primary key is a unique identifier for each record in a database table. It is a column or a set of columns that uniquely identifies each row in a table. A primary key cannot be null, meaning that it must have a value for each record in the table. 

#### Advantages of Primary Key

- Ensures data integrity: A primary key ensures that each record in a table is unique and helps to prevent duplicate data from being entered into the database.
- Supports data relationships: A primary key can be used to create relationships between tables. For example, a foreign key in one table can reference the primary key in another table to establish a relationship between the two tables.
- Improves query performance: A primary key can improve the performance of queries that involve searching for or sorting data in a table. 

#### Disadvantages of Primary Key

- Can be difficult to choose: Choosing a primary key can be difficult, especially if there are multiple columns that could be used. 
- Can be slow for large tables: If a table has a large number of records, searching for data based on the primary key can be slow. 

#### Examples of Primary Key

- In a table of customers, the primary key could be the customer ID number.
- In a table of employees, the primary key could be the employee ID number.

#### ASCII Diagram

```
+--------------------------+
|     Customer Table       |
+--------------------------+
| CustomerID (Primary Key) |
| Name                     |
| Address                  |
+--------------------------+
```

#### Code Example

```
CREATE TABLE Customers (
    CustomerID int NOT NULL PRIMARY KEY,
    Name varchar(255),
    Address varchar(255)
);
```

#### Applications of Primary Key

- Primary keys are used in relational databases to ensure data integrity and to establish relationships between tables.
- Primary keys can be used to create indexes, which can improve the performance of queries that involve searching or sorting data in a table.
- Primary keys can be used to enforce referential integrity, which ensures that data in related tables is consistent.