# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is an open-source relational database management system that uses SQL as its query language.

## SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you send to the database; after that, you expect the database will respond to the question by sending back the data.

There are different types of SQL queries, depending on the purpose and complexity of the query. Some of the common types are:

- Data Definition Language (DDL) queries: These queries are used to create, alter, or delete the structure of the database objects, such as tables, views, indexes, etc. For example, `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, etc.
- Data Manipulation Language (DML) queries: These queries are used to insert, update, or delete the data in the database tables. For example, `INSERT INTO`, `UPDATE`, `DELETE`, etc.
- Data Query Language (DQL) queries: These queries are used to select and retrieve the data from the database tables. For example, `SELECT`, `WHERE`, `GROUP BY`, etc.
- Data Control Language (DCL) queries: These queries are used to grant or revoke the permissions and access rights to the database objects. For example, `GRANT`, `REVOKE`, etc.
- Transaction Control Language (TCL) queries: These queries are used to manage the transactions in the database, such as committing or rolling back the changes. For example, `COMMIT`, `ROLLBACK`, etc.

## MySQL Database

MySQL is a widely used relational database management system that supports SQL as its query language. MySQL is free and open-source, and it is ideal for both small and large applications. MySQL has many features, such as:

- High performance and scalability
- Cross-platform compatibility
- Multiple storage engines
- Full-text search and indexing
- Stored procedures and triggers
- Replication and backup
- Security and encryption
- User-defined functions and variables

## How to Query a MySQL Database

To query a MySQL database, you need to have a database management application, such as MySQL Workbench, Sequel Pro, or phpMyAdmin. You also need to connect your database to the application, using the host name, port number, user name, and password of your database server.

Once you are connected, you can use the following steps to query a MySQL database:

1. Understand your database and its hierarchy. A MySQL database consists of one or more schemas, which contain one or more tables, which contain one or more columns and rows of data. You can use the `SHOW` command to list the schemas, tables, and columns in your database. For example, `SHOW DATABASES`, `SHOW TABLES`, `SHOW COLUMNS FROM table_name`, etc.
2. Find out which fields are in your tables. Each table has a set of columns, which define the attributes of the data stored in the table. Each column has a name, a data type, and some constraints, such as primary key, foreign key, unique, not null, etc. You can use the `DESCRIBE` command to see the details of the columns in a table. For example, `DESCRIBE table_name`.
3. Begin writing a SQL query to pull your desired data. Depending on the type and complexity of the query, you may need to use different keywords, clauses, operators, and functions to specify the data you want to retrieve, filter, sort, group, or manipulate. You can use the `SELECT` command to start a query, and then use other clauses, such as `FROM`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, `JOIN`, etc. to refine the query. For example, `SELECT column1, column2 FROM table1 WHERE column3 = 'value' ORDER BY column4 DESC;`.
4. Execute the query and view the results. You can use the `RUN` or `EXECUTE` button in your database management application to run the query and see the results in a tabular format. You can also use the `LIMIT` clause to limit the number of rows returned by the query. For example, `SELECT * FROM table1 LIMIT 10;`.
5. Save or export the query and the results. You can use the `