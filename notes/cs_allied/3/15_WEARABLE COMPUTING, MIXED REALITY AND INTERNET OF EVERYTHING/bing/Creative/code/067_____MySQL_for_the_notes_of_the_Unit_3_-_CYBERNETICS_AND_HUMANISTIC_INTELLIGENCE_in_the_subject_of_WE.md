### MySQL

MySQL is a relational database management system (RDBMS) that allows us to store, manipulate, and retrieve data in a structured way. MySQL is free, open-source, and widely used for various applications. In this section, we will learn some basic concepts and operations of MySQL.

#### What is a database?

A database is a collection of related data that is organized in a logical way. A database can have one or more tables, which are the main units of data storage. A table consists of rows and columns, where each row represents a record and each column represents an attribute or a field. For example, a table named `students` can store information about students, such as their names, IDs, majors, and grades.

#### What is SQL?

SQL stands for Structured Query Language, which is a standard language for interacting with databases. SQL allows us to perform various tasks on the data, such as creating, updating, deleting, querying, and manipulating. SQL has a set of keywords, syntax, and rules that we need to follow to write valid SQL statements. For example, the following SQL statement creates a table named `students` with four columns:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  major VARCHAR(50),
  grade FLOAT
);
```

#### How to connect to MySQL?

To connect to MySQL, we need a MySQL server, a MySQL client, and a MySQL user account. A MySQL server is a software that runs on a computer and manages the databases. A MySQL client is a software that allows us to communicate with the MySQL server. A MySQL user account is a set of credentials that grants us access to the databases and permissions to perform operations on them.

There are different ways to connect to MySQL, depending on the type of client we use. One of the most common ways is to use the `mysql` command-line client, which is a program that we can run in a terminal or a command prompt. To use the `mysql` client, we need to provide the following information:

- The hostname or the IP address of the MySQL server. If the server is running on the same computer as the client, we can use `localhost` or `127.0.0.1`.
- The port number of the MySQL server. The default port is `3306`.
- The username and the password of the MySQL user account. The default username is `root` and the default password is empty.
- The name of the database that we want to use. If we don't specify a database, we can use the `USE` command later to switch to a database.

For example, the following command connects to the MySQL server running on `localhost` with the username `root` and the password `1234`, and uses the database named `school`:

```bash
mysql -h localhost -P 3306 -u root -p1234 school
```

If the connection is successful, we will see a prompt like this:

```bash
mysql>
```

We can then type SQL statements and press `Enter` to execute them. To exit the `mysql` client, we can type `exit` or `quit` and press `Enter`.

#### How to create a database?

To create a database, we can use the `CREATE DATABASE` command, followed by the name of the database. For example, the following command creates a database named `school`:

```sql
CREATE DATABASE school;
```

We can use the `SHOW DATABASES` command to list all the databases on the server:

```sql
SHOW DATABASES;
```

We can use the `USE` command to switch to a database that we want to use:

```sql
USE school;
```

We can use the `DROP DATABASE` command to delete a database, followed by the name of the database. For example, the following command deletes the database named `school`:

```sql
DROP DATABASE school;
```

#### How to create a table?

To create a table, we can use the `CREATE TABLE` command, followed by the name of the table and the definition of the columns. Each column has a name, a data type, and optionally some constraints. For example, the following command creates a table named `students` with four columns:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  major VARCHAR(50),
  grade FLOAT
);
```

The data type specifies the kind of data that can be stored in the column, such as `INT` for integers, `VARCHAR` for variable-length strings, and `