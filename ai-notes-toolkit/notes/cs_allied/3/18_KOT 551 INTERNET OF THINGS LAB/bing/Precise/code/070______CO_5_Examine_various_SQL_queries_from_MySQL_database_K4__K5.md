#### CO 5 Examine various SQL queries from MySQL database K4, K5

Structured Query Language (SQL) is a standard language used to manage and manipulate data stored in relational databases. MySQL is one of the most popular open-source relational database management systems that use SQL.

Here are some common SQL queries used in MySQL:

1. **SELECT** - used to retrieve data from one or more tables.
```SQL
SELECT column1, column2, ...
FROM table_name;
```

2. **INSERT INTO** - used to insert new records into a table.
```SQL
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

3. **UPDATE** - used to modify existing records in a table.
```SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

4. **DELETE** - used to delete existing records from a table.
```SQL
DELETE FROM table_name
WHERE condition;
```

5. **CREATE TABLE** - used to create a new table.
```SQL
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

6. **ALTER TABLE** - used to add, modify, or delete columns in an existing table.
```SQL
ALTER TABLE table_name
ADD column_name datatype;
```

7. **DROP TABLE** - used to delete an existing table.
```SQL
DROP TABLE table_name;
```

8. **CREATE INDEX** - used to create an index on one or more columns.
```SQL
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

9. **DROP INDEX** - used to delete an existing index.
```SQL
ALTER TABLE table_name
DROP INDEX index_name;
```

These are just some of the many SQL queries that can be used in a MySQL database. It is important to have a good understanding of these queries to effectively manage and manipulate data in a MySQL database.