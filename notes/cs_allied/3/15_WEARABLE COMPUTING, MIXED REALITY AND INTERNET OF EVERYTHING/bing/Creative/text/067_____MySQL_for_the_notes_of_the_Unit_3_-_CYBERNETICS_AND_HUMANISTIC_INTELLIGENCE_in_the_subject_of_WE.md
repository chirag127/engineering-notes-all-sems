### MySQL

MySQL is a relational database management system (RDBMS) that allows us to store, manipulate, and retrieve data in a structured way. MySQL is free, open-source, and widely used for various applications. In this section, we will learn some basic concepts and operations of MySQL.

#### What is a database?

A database is a collection of related data that is organized in a logical way. A database can have one or more tables, which are the main units of data storage. A table consists of rows and columns, where each row represents a record and each column represents an attribute or a field. For example, a table of students can have columns such as id, name, age, and grade.

#### What is SQL?

SQL stands for Structured Query Language, which is a standard language for communicating with databases. SQL allows us to perform various tasks on the data, such as creating, updating, deleting, querying, and joining tables. SQL has a set of keywords, operators, and syntax rules that we need to follow to write valid SQL statements.

#### How to connect to MySQL?

To connect to MySQL, we need to have a MySQL server running on our computer or a remote host. We also need a MySQL client, which is a program that allows us to interact with the MySQL server. There are different types of MySQL clients, such as command-line, graphical, or web-based. One of the most common MySQL clients is the mysql command-line tool, which we can use to enter SQL commands and see the results.

To connect to MySQL using the mysql command-line tool, we need to provide the following information:

- The hostname or IP address of the MySQL server
- The username and password of a MySQL user
- The name of the database that we want to use

For example, the following command connects to the MySQL server on the local host, using the root user and the test database:

```sql
mysql -h localhost -u root -p test
```

After entering the password, we will see a prompt like this:

```sql
mysql>
```

This means that we are connected to the MySQL server and ready to enter SQL commands.

#### How to create a table in MySQL?

To create a table in MySQL, we use the CREATE TABLE statement, which has the following syntax:

```sql
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  ...
);
```

The table_name is the name of the table that we want to create. The column names and datatypes define the structure of the table. A datatype specifies the type and size of the data that can be stored in a column, such as integer, varchar, date, etc.

For example, the following statement creates a table called students with four columns: id, name, age, and grade.

```sql
CREATE TABLE students (
  id INT,
  name VARCHAR(50),
  age INT,
  grade VARCHAR(2)
);
```

To verify that the table is created, we can use the SHOW TABLES command, which lists all the tables in the current database.

```sql
SHOW TABLES;
```

The output should look like this:

```sql
+----------------+
| Tables_in_test |
+----------------+
| students       |
+----------------+
```

#### How to insert data into a table in MySQL?

To insert data into a table in MySQL, we use the INSERT INTO statement, which has the following syntax:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

The table_name is the name of the table that we want to insert data into. The column names and values specify the data that we want to insert. The values must match the datatypes of the columns and be enclosed in single quotes if they are strings.

For example, the following statement inserts a new record into the students table with the values 1, 'Alice', 18, and 'A'.

```sql
INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
```

To insert multiple records at once, we can use the following syntax:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES
(value1, value2, ...),
(value3, value4, ...),
...
;
```

For example, the following statement inserts three more records into the students table.

```sql
INSERT INTO students (id, name, age, grade) VALUES
(2, 'Bob', 19, 'B'),
(3, 'Charlie', 20, 'C

```
