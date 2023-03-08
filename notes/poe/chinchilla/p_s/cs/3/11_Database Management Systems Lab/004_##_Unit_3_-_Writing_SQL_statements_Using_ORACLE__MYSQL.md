## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

Structured Query Language (SQL) is a standard language used to manage and manipulate relational databases. In this unit, we will learn how to write SQL statements using ORACLE/MYSQL, which are popular RDBMS systems.

### SQL Statements

SQL statements are used to interact with the database. There are different types of SQL statements, including:

- Data Definition Language (DDL) statements: Used to create, modify, and delete database objects such as tables, indexes, and constraints.
- Data Manipulation Language (DML) statements: Used to insert, update, and delete data in a table.
- Data Query Language (DQL) statements: Used to retrieve data from one or more tables.

### ORACLE

ORACLE is a popular RDBMS system used by many organizations worldwide. It uses SQL as its database language, and it has a rich set of features that make it suitable for managing large databases. Some of the features of ORACLE include:

- High availability: ORACLE has built-in features for ensuring high availability, such as Real Application Clusters (RAC) and Data Guard.
- Scalability: ORACLE can handle large amounts of data and users, making it suitable for enterprise-level databases.
- Security: ORACLE has advanced security features, such as Transparent Data Encryption (TDE) and Advanced Security Option (ASO).

### MYSQL

MYSQL is another popular RDBMS system used by many organizations worldwide. It is an open-source database management system that uses SQL as its language. Some of the features of MYSQL include:

- Ease of use: MYSQL is easy to install and use, making it suitable for small to medium-sized databases.
- Performance: MYSQL has a fast performance, especially when handling read-intensive workloads.
- Scalability: MYSQL can handle large amounts of data and users, making it suitable for enterprise-level databases.

### Writing SQL Statements

To write SQL statements, we need to use keywords and syntax that are specific to the RDBMS system we are using. Here are some examples of SQL statements:

- Creating a table in ORACLE:

```sql
CREATE TABLE employees (
  id NUMBER(10) PRIMARY KEY,
  name VARCHAR2(50) NOT NULL,
  department VARCHAR2(50) NOT NULL,
  salary NUMBER(10, 2)
);
```

- Inserting data into a table in MYSQL:

```sql
INSERT INTO employees (id, name, department, salary)
VALUES (1, 'John Doe', 'Sales', 5000.00);
```

- Retrieving data from a table in ORACLE:

```sql
SELECT * FROM employees WHERE department = 'Sales';
```

### Advantages and Disadvantages

ORACLE and MYSQL have their advantages and disadvantages. Here are some of them:

#### ORACLE

Advantages:

- High availability
- Scalability
- Security

Disadvantages:

- Expensive licensing
- Complex architecture
- Steep learning curve

#### MYSQL

Advantages:

- Ease of use
- Performance
- Affordable

Disadvantages:

- Limited features compared to ORACLE
- Limited community support
- Limited scalability compared to ORACLE

### Applications

ORACLE and MYSQL are used in various applications, including:

- Enterprise-level databases
- Web applications
- Data warehousing
- Business intelligence

In conclusion, learning how to write SQL statements using ORACLE/MYSQL is essential for managing and manipulating relational databases. By understanding the syntax and features of these RDBMS systems, we can create, modify, and query databases efficiently and effectively.