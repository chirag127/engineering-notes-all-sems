### DML in PL/SQL for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

PL/SQL is a procedural language designed specifically for the Oracle Database management system. It includes a set of programming language features that enable developers to build complex applications and manage data efficiently. One of the most important features of PL/SQL is DML, or Data Manipulation Language. 

DML is the set of commands used to manage and manipulate data within a database. In PL/SQL, DML is used to insert, update and delete data from tables. The following are the most commonly used DML statements in PL/SQL:

- INSERT: This statement is used to insert new data into a table. The syntax for the insert statement is as follows:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

- UPDATE: This statement is used to modify existing data within a table. The syntax for the update statement is as follows:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- DELETE: This statement is used to remove data from a table. The syntax for the delete statement is as follows:

```sql
DELETE FROM table_name WHERE condition;
```

In addition to these basic DML statements, PL/SQL also supports more advanced features such as subqueries, joins and transactions. These features allow developers to write more complex queries and manipulate data in powerful ways.

One of the advantages of using DML in PL/SQL is that it provides a high level of control and security over data. By using transactions and other advanced features, developers can ensure that data is managed in a consistent and secure manner.

However, there are also some disadvantages to using DML in PL/SQL. For example, it can be more complex and time-consuming to write and maintain PL/SQL code compared to other programming languages. Additionally, PL/SQL is specific to Oracle databases, which can limit its usefulness in certain situations.

Overall, DML in PL/SQL is a powerful tool for managing and manipulating data within a database. By understanding the basics of DML and how to use it effectively, developers can build robust and efficient applications that leverage the full power of Oracle databases.