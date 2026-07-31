## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

SQL (Structured Query Language) is a standard language used to communicate with relational database management systems (RDBMS) such as Oracle and MySQL. It is used to perform various operations on the data stored in the database, including data manipulation and data definition.

Here are some key points to remember when writing SQL statements using Oracle or MySQL:

1. SQL is not case-sensitive, but it is a good practice to write keywords in uppercase and identifiers (such as table and column names) in lowercase.
2. SQL statements can be written on one or multiple lines and must end with a semicolon (;).
3. Comments can be added to SQL statements using `--` for single-line comments or `/* ... */` for multi-line comments.
4. Oracle and MySQL have their own specific SQL syntax and functions, so it is important to consult the respective documentation when writing SQL statements for these RDBMS.
5. SQL statements can be divided into two main categories: Data Definition Language (DDL) and Data Manipulation Language (DML).
6. DDL statements are used to define, modify, or delete database objects such as tables, views, and indexes. Some common DDL statements include `CREATE`, `ALTER`, and `DROP`.
7. DML statements are used to manipulate the data stored in the database. Some common DML statements include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
8. When writing `SELECT` statements, it is important to specify the columns to be retrieved and the table(s) from which to retrieve the data. The `WHERE` clause can be used to filter the data based on specific conditions.
9. When writing `INSERT`, `UPDATE`, or `DELETE` statements, it is important to specify the table(s) to be affected and the conditions under which the data should be modified or deleted.
10. It is a good practice to test SQL statements on a small set of data or a test database before running them on a production database to avoid unintended data loss or corruption.