

## Name of the Lab for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- A possible name for the lab is **Database Management with Azure Lab Services**.
- The lab aims to teach the basic concepts and skills of database management for relational databases using two popular systems: MySQL and SQL Server.
- The lab uses Azure Lab Services, a cloud-based platform that allows instructors to create and manage virtual machine templates for their classes.
- The lab consists of the following steps:

  - Setting up a lab account and a virtual machine template with MySQL and SQL Server installed and configured.
  - Creating a lab class and inviting students to join the lab.
  - Assigning lab exercises and projects to students that involve creating, querying, and manipulating databases using MySQL and SQL Server.
  - Monitoring and grading students' progress and performance using the lab dashboard and reports.

- The lab benefits from the following features of Azure Lab Services:

  - Scalability: The lab can accommodate any number of students and virtual machines without compromising performance or availability.
  - Security: The lab protects the data and resources of the instructor and the students using encryption, authentication, and access control mechanisms.
  - Cost-effectiveness: The lab only charges for the actual usage of the virtual machines, and offers discounts for academic institutions.
  - Flexibility: The lab allows the instructor to customize the virtual machine template, the lab class, and the lab exercises according to their preferences and objectives.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Database Management Systems Mapping with Virtual Lab Lab. Here is the content for the topic of Name of the Experiment:

## Name of the Experiment

- The name of the experiment is **Database Design using Entity-Relationship Diagrams**.
- The objective of this experiment is to learn how to design a database schema using entity-relationship (ER) diagrams, which are graphical representations of the entities, attributes, relationships, and constraints in a database.
- The steps of this experiment are:

  1. Identify the entities, attributes, and relationships in a given problem statement or scenario.
  2. Draw an ER diagram using the symbols and notation for entities, attributes, relationships, cardinalities, and participation constraints.
  3. Validate the ER diagram by checking for errors, ambiguities, and redundancies.
  4. Convert the ER diagram into a relational schema using the mapping rules for entities, attributes, relationships, and constraints.
  5. Test the relational schema by creating tables and inserting sample data using SQL commands.

- The expected outcome of this experiment is to be able to design a database schema using ER diagrams and to understand the mapping rules for converting ER diagrams into relational schemas.



## Database Management Lab for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Database management is the process of storing, manipulating, and retrieving data from a database using a database management system (DBMS).
- A DBMS is a software system that provides a standard way of creating, maintaining, and querying databases using a structured query language (SQL).
- A database is a collection of related data organized in tables, which consist of rows (records) and columns (attributes).
- A virtual lab is a simulated environment that allows students to perform experiments and learn concepts related to database management systems.
- The objective of the database management lab is to provide students with practical exposure to the design, implementation, and operation of relational databases using a DBMS.
- The database management lab covers the following topics:

  - Data definition language (DDL) commands: These are SQL commands that are used to create, modify, and delete database objects such as tables, views, indexes, and constraints.
  - Data manipulation language (DML) commands: These are SQL commands that are used to insert, update, delete, and retrieve data from tables and views.
  - High-level programming language extensions: These are features that allow SQL statements to be embedded in a programming language such as C, Java, or Python, or to use stored procedures and functions to perform complex tasks on the database.
  - Front-end tools: These are graphical user interfaces (GUIs) that allow users to interact with the database and perform various operations such as creating queries, forms, reports, and charts.
  - Forms, triggers, and menus: These are components that enhance the functionality and usability of the database applications. Forms are used to collect and display data from the user, triggers are used to execute actions automatically when certain events occur on the database, and menus are used to provide navigation and options to the user.
  - Reports: These are documents that present the data from the database in a formatted and summarized way, such as tables, charts, graphs, and dashboards.

- The database management lab consists of a series of experiments that require the students to perform various tasks on a given database using a DBMS. The experiments are designed to test the students' understanding and skills on the topics covered in the lab.
- The database management lab also provides the students with the opportunity to map their theoretical knowledge to a virtual lab environment, where they can access and manipulate a remote database server using a web browser. The virtual lab allows the students to practice and learn the concepts of database management systems in a realistic and interactive way.



## Data Definition Language(DDL) Statements

- Data Definition Language (DDL) is a group of SQL statements that you can execute to manage database objects, such as tables, views, functions, and policies   .
- Using DDL statements, you can perform powerful commands in your database such as creating, modifying, and dropping objects   .
- DDL commands are usually executed in a SQL browser or stored procedure.
- Some common DDL commands are:
  - CREATE: to create a new database object   .
  - ALTER: to modify an existing database object   .
  - DROP: to delete a database object   .
  - RENAME: to change the name of a database object .
  - TRUNCATE: to remove all the data from a table .
- DDL statements are different from Data Manipulation Language (DML) statements, which are used to insert, update, and delete data from database objects .
- DDL statements are also different from Data Control Language (DCL) statements, which are used to grant and revoke permissions and roles to users and groups .
- Here is an example of a DDL statement that creates a table named `students` with four columns: `id`, `name`, `age`, and `grade` :

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  grade CHAR(1) CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
);
```



## Data Manipulation Language(DML) Statements

- Data manipulation language (DML) statements are used to access and manipulate data in existing schema objects, such as tables and views  .
- DML statements can update, insert, and delete data from the tables  .
- DML statements are part of a transaction, which is a sequence of one or more SQL statements that are treated as a unit. A transaction can be committed or rolled back as a whole.
- The main DML statements are:
  - **SELECT**: retrieves data from one or more tables or views   .
  - **INSERT**: adds one or more rows of data to a table or view    .
  - **UPDATE**: modifies one or more columns of data in a table or view    .
  - **DELETE**: removes one or more rows of data from a table or view    .
  - **MERGE**: combines the data from two tables and updates or inserts the result into a third table   .
  - **CALL**: executes a stored procedure or function  .
  - **EXPLAIN PLAN**: displays the execution plan of a SQL statement .
  - **LOCK TABLE**: locks one or more tables or views in a specified mode .
- DML statements can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT, to filter, aggregate, sort, and limit the data that is returned or affected  .
- DML statements can also use subqueries, joins, and set operators to combine data from multiple tables or views  .
- DML statements can be executed interactively using tools such as SQL*Plus or SQL Developer, or embedded in programs written in languages such as Java, C#, or Python .



## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a component of SQL (Structured Query Language) that is used to retrieve and manipulate data in a relational database management system  .
- DQL statements are used to query the data contained in schema objects, such as tables, views, indexes, etc .
- The purpose of DQL is to get some schema relation based on the query passed to it, and to impose order upon it.
- The most common DQL statement is the SELECT statement, which allows you to select data from one or more tables or views, and apply various filters, joins, aggregations, and sorting options  .
- The syntax of the SELECT statement is as follows:

```sql
SELECT [DISTINCT] column_list
FROM table_list
[WHERE condition]
[GROUP BY column_list]
[HAVING condition]
[ORDER BY column_list [ASC | DESC]];
```

- The SELECT statement can also be used with subqueries, which are queries nested within another query, to perform complex operations on the data .
- Some examples of DQL statements are:

```sql
-- Select all the data from the employees table
SELECT * FROM employees;

-- Select the name and salary of the employees who work in the sales department
SELECT name, salary
FROM employees
WHERE department = 'sales';

-- Select the average salary of each department, and order the result by descending order of the average salary
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- Select the name and salary of the employees who earn more than the average salary of their department
SELECT name, salary
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);
```

- DQL is an essential part of SQL, as it allows you to access and manipulate the data stored in a database    .
- DQL is also the basis for other SQL commands, such as DML (Data Manipulation Language), which is used to insert, update, and delete data, and DCL (Data Control Language), which is used to grant and revoke permissions on the data  .
- DQL can be used with various database management systems, such as MySQL, Oracle, SQL Server, Postgres, etc .
- DQL can also be used with various tools and applications, such as virtual labs, which are online platforms that allow you to practice and learn SQL skills in a simulated environment.



## Transaction Control Language(TCL) statements

Transaction Control Language (TCL) is a type of SQL command that is used to manage transactions in a database. Transactions are a way of grouping multiple SQL statements into a single unit of work, so that either all of the statements are executed, or none of them are. This helps to ensure the consistency and integrity of the data in the database.

TCL commands are used to keep track of the modifications that DML statements (such as INSERT, DELETE, and UPDATE) make. TCL allows the statements to be grouped together into logical transactions.

The main TCL commands are:

- **COMMIT**: It is used to save the transactions in the database. It marks the end of a successful transaction and makes the changes permanent .
- **ROLLBACK**: It is used to restore the database to that state which was last committed. It undoes the changes made by the transaction and cancels its effects .
- **SAVEPOINT**: It is used to create a point in the transaction where the changes done till that point will be unchanged and all the transactions after that point will be rolled back. It allows partial rollback of a transaction .
- **SET TRANSACTION**: It is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write mode, etc.

Here is an example of using TCL commands in SQL:

```sql
-- Begin a transaction
BEGIN;

-- Insert a record into the employee table
INSERT INTO employee (id, name, salary) VALUES (101, 'Alice', 5000);

-- Create a savepoint
SAVEPOINT sp1;

-- Update the salary of Alice
UPDATE employee SET salary = 6000 WHERE id = 101;

-- Rollback to the savepoint
ROLLBACK TO sp1;

-- Commit the transaction
COMMIT;
```

In this example, the transaction begins with the BEGIN command and ends with the COMMIT command. The INSERT statement is executed and saved in the database. The UPDATE statement is executed but not saved, because it is rolled back to the savepoint sp1. The savepoint sp1 preserves the state of the database after the INSERT statement. The final result is that the employee table has one record with id 101, name Alice, and salary 5000.



## Statement for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- A database management system (DBMS) is a software tool that enables users to manage a database easily.
- A database is a collection of data that is organized so that it can be accessed, manipulated, and updated by users or applications.
- A virtual lab is a simulated environment that allows users to perform experiments or tasks without the need for physical equipment or resources.
- Database management systems mapping with virtual lab lab is a subject that covers the theory, design, development, and management of modern relational databases using a virtual lab environment.
- The main topics of this subject are:
  - Entity-relationship modeling: a technique for representing the data and relationships in a database using graphical symbols and diagrams.
  - Normalization: a process of organizing the data in a database to reduce redundancy and improve data integrity.
  - Structured query language (SQL): a standard language for defining, manipulating, and querying data in a relational database.
  - Database management: the activities and tasks involved in maintaining, securing, and optimizing the performance of a database.
- The main objectives of this subject are:
  - To provide students with a level of knowledge that allows them to be effective managers of relational databases in a business environment.
  - To enable students to design and implement relational databases using entity-relationship modeling and normalization techniques.
  - To teach students how to use SQL to perform various operations on data in a relational database.
  - To expose students to the virtual lab environment and its benefits for learning and practicing database management skills.
  - To help students make informed decisions based on data analysis and interpretation using database management systems.

