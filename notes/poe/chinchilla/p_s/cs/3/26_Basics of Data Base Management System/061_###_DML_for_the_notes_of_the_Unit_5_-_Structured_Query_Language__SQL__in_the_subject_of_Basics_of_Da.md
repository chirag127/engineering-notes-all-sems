### DML for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

DML stands for Data Manipulation Language. It is a subset of SQL that is used to modify, insert, delete, and update data in a database. In this unit, we will discuss the various DML commands that are used to manipulate data in a database.

#### INSERT command

The INSERT command is used to add new data into a table. The syntax for the INSERT command is as follows:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

#### UPDATE command

The UPDATE command is used to modify existing data in a table. The syntax for the UPDATE command is as follows:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

#### DELETE command

The DELETE command is used to remove data from a table. The syntax for the DELETE command is as follows:

```
DELETE FROM table_name
WHERE condition;
```

#### SELECT command

The SELECT command is used to retrieve data from one or more tables in a database. The syntax for the SELECT command is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

#### MERGE command

The MERGE command is used to combine data from two tables into one. The syntax for the MERGE command is as follows:

```
MERGE INTO table1
USING table2
ON (condition)
WHEN MATCHED THEN
    UPDATE SET column1 = value1, column2 = value2, ...
WHEN NOT MATCHED THEN
    INSERT (column1, column2, ...) VALUES (value1, value2, ...);
```

#### Advantages of DML

- DML allows for the manipulation of data in a database, making it easy to modify, insert, delete, and update data as needed.
- DML is easy to learn and use, even for beginners who are just getting started with SQL.

#### Disadvantages of DML

- DML can be slow when working with large amounts of data, as it requires multiple queries to be executed in order to manipulate the data in a table.

#### Examples of DML

Here are some examples of DML commands:

- Inserting a new record into a table:

```
INSERT INTO customers (name, email, phone)
VALUES ('John Smith', 'john@example.com', '555-1234')
```

- Updating an existing record in a table:

```
UPDATE customers
SET email = 'john.smith@example.com', phone = '555-4321'
WHERE id = 1
```

- Deleting a record from a table:

```
DELETE FROM customers
WHERE id = 1
```

#### Applications of DML

DML is used in a variety of applications, including:

- E-commerce websites, where DML is used to manage customer data, order information, and shipping details.
- Healthcare systems, where DML is used to manage patient data, medical records, and test results.
- Financial institutions, where DML is used to manage customer account information, transaction data, and investment portfolios.