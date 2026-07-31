# CO 5 Examine various SQL queries from MySQL database K4, K5

MySQL is an open-source relational database management system that uses Structured Query Language (SQL) to manage and manipulate data. SQL is a standard language for managing and querying relational databases.

Here are some common SQL queries that can be used in a MySQL database:

1. SELECT: The SELECT statement is used to query a database and retrieve data from one or more tables. The basic syntax of the SELECT statement is as follows:
```
SELECT column1, column2, ...
FROM table_name;
```

2. INSERT: The INSERT statement is used to add new records to a table. The basic syntax of the INSERT statement is as follows:
```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

3. UPDATE: The UPDATE statement is used to modify existing records in a table. The basic syntax of the UPDATE statement is as follows:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

4. DELETE: The DELETE statement is used to delete existing records from a table. The basic syntax of the DELETE statement is as follows:
```
DELETE FROM table_name
WHERE condition;
```

5. CREATE: The CREATE statement is used to create a new table in a database. The basic syntax of the CREATE statement is as follows:
```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

6. ALTER: The ALTER statement is used to add, modify, or delete columns in an existing table. The basic syntax of the ALTER statement is as follows:
```
ALTER TABLE table_name
ADD column_name datatype;
```

7. DROP: The DROP statement is used to delete a table from a database. The basic syntax of the DROP statement is as follows:
```
DROP TABLE table_name;
```

These are some of the basic SQL queries that can be used in a MySQL database. It is important to note that the syntax and usage of these queries may vary depending on the specific version of MySQL being used. It is always a good idea to consult the official MySQL documentation for the most up-to-date information.