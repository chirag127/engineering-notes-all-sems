### DML

DML stands for Data Manipulation Language. It is a subset of SQL that allows users to manipulate data stored in a database. DML statements are used to insert, update, delete, and retrieve data from a database. In this section, we will look at the different types of DML statements.

#### INSERT Statement

The INSERT statement is used to add new rows to a table. Here is the syntax:

```
INSERT INTO table_name(column1, column2, ...)
VALUES(value1, value2, ...);
```

#### UPDATE Statement

The UPDATE statement is used to modify existing rows in a table. Here is the syntax:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE some_column = some_value;
```

#### DELETE Statement

The DELETE statement is used to remove rows from a table. Here is the syntax:

```
DELETE FROM table_name
WHERE some_column = some_value;
```

#### SELECT Statement

The SELECT statement is used to retrieve data from one or more tables. Here is the syntax:

```
SELECT column1, column2, ...
FROM table_name
WHERE some_column = some_value;
```

#### Advantages of DML

- DML allows users to manipulate data stored in a database.
- DML statements are easy to learn and use.
- DML allows users to retrieve data from one or more tables using the SELECT statement.

#### Disadvantages of DML

- DML statements can be complex and difficult to write.
- DML statements can be time-consuming to execute on large databases.
- DML statements can cause data integrity issues if not used properly.

#### Examples of DML

Here are some examples of DML statements:

```
INSERT INTO employees(name, age, salary) VALUES('John', 35, 50000);

UPDATE employees SET salary = 55000 WHERE name = 'John';

DELETE FROM employees WHERE name = 'John';

SELECT name, age, salary FROM employees WHERE age > 30;
```

#### Applications of DML

DML is used in a wide range of applications, including:

- Online transaction processing (OLTP) systems
- Business intelligence (BI) systems
- Data warehousing systems
- E-commerce applications

In conclusion, DML is a powerful subset of SQL that allows users to manipulate data stored in a database. It is essential for anyone working with databases to understand DML statements and their syntax.