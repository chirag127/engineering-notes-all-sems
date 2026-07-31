### DML for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

Data Manipulation Language (DML) is an essential component of any database management system (DBMS) that enables users to manipulate data stored in a database. DML is a sub-language of Structured Query Language (SQL) that allows users to insert, update, and delete data from a database. This section will provide an overview of DML and its various commands.

#### DML Commands

1. **INSERT:** The INSERT command is used to add new data to a table in the database. The syntax for the INSERT command is as follows:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

2. **UPDATE:** The UPDATE command is used to modify existing data in a table. The syntax for the UPDATE command is as follows:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

3. **DELETE:** The DELETE command is used to remove data from a table. The syntax for the DELETE command is as follows:

```
DELETE FROM table_name
WHERE condition;
```

4. **SELECT:** The SELECT command is used to retrieve data from one or more tables in a database. The syntax for the SELECT command is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

#### Key Concepts

1. **Transactions:** A transaction is a sequence of operations that are treated as a single unit of work. The ACID (Atomicity, Consistency, Isolation, and Durability) properties ensure that transactions are executed reliably and consistently.

2. **Views:** A view is a virtual table that is based on the result of a SELECT statement. Views provide an easy way to retrieve data from one or more tables without having to write complex queries.

3. **Indexes:** Indexes are used to improve the performance of database queries by providing a quick way to locate data. Indexes can be created on one or more columns of a table.

#### Conclusion

DML is an essential component of any database management system. It enables users to manipulate data stored in a database using various commands such as INSERT, UPDATE, DELETE, and SELECT. Understanding DML is essential for database developers and administrators to ensure that data is stored, retrieved, and manipulated efficiently.