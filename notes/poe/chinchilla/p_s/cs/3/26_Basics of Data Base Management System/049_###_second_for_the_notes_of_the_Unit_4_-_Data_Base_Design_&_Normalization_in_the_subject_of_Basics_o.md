### Second Normal Form (2NF)

Second Normal Form (2NF) is a level of database normalization that is achieved when a table is in First Normal Form (1NF) and all non-key columns are functionally dependent on the table's primary key.

#### Requirements for 2NF

For a table to be in 2NF, it must meet the following requirements:

1. Be in First Normal Form (1NF)
2. Have a primary key defined
3. All non-key columns must be dependent on the entire primary key, not just a part of it.

#### Advantages of 2NF

1. Reduces data redundancy and improves data accuracy.
2. Ensures consistent data across the database.
3. Simplifies database maintenance.
4. Improves database performance.

#### Disadvantages of 2NF

1. Can lead to complex database designs.
2. Can be time-consuming to normalize large databases.

#### Example of 2NF

Consider a table that stores sales data for a company. The table has the following columns: `OrderID`, `CustomerID`, `CustomerName`, `ProductID`, `ProductName`, `Quantity`, and `Price`. In this table, the primary key is `OrderID`. However, the columns `CustomerName` and `ProductName` are not dependent on the entire primary key, but only on `CustomerID` and `ProductID`, respectively. To bring this table to 2NF, we would split it into two tables: `Orders` and `Products`. The `Orders` table would have columns `OrderID`, `CustomerID`, `Quantity`, and `Price`, while the `Products` table would have columns `ProductID` and `ProductName`.

#### Applications of 2NF

2NF is used in the design of relational databases to ensure data integrity and consistency. It is an essential step in the normalization process, which helps to eliminate data redundancies and anomalies. By following the rules of 2NF, database designers can create efficient and effective database structures that facilitate easy data retrieval and management.