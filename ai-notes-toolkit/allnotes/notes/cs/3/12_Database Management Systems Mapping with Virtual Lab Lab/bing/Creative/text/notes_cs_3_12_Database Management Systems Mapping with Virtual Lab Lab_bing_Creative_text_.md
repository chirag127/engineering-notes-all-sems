

## Name of the Lab for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- The name of the lab is **Database Management Systems Mapping with Virtual Lab Lab**.
- The lab is designed to help students learn and practice the concepts and skills of database management systems, such as data modeling, relational algebra, SQL, normalization, indexing, query optimization, concurrency control, and recovery.
- The lab consists of two parts: a **mapping** part and a **virtual lab** part.
- The mapping part is a web-based tool that allows students to create and manipulate data models using the entity-relationship (ER) diagram notation. Students can also map their ER diagrams to relational schemas and generate SQL statements to create and populate the tables in a database.
- The virtual lab part is a web-based platform that provides access to a MySQL database server and a graphical user interface (GUI) for executing SQL queries and viewing the results. Students can also use the GUI to create, modify, and delete tables, indexes, views, and triggers in the database.
- The lab is intended to complement the theoretical lectures and assignments of the course and to provide hands-on experience with database management systems. The lab also helps students to prepare for the practical exams and projects of the course.



## Name of the Experiment for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- A possible name for the experiment is **Database Management for Relational Databases using Azure Lab Services**.
- The experiment aims to teach the basic concepts and skills of relational database management systems (RDBMS) using two popular examples: MySQL and SQL Server.
- The experiment involves setting up a virtual machine template in a lab with both MySQL Database Server and SQL Server 2019 server installed and configured.
- The experiment also provides some sample databases and queries for students to practice and learn the common operations and features of RDBMS, such as creating tables, inserting data, querying data, joining tables, aggregating data, etc.
- The experiment can be conducted using Azure Lab Services, which is a cloud-based platform that allows instructors to create and manage virtual labs for their classes.
- The experiment can benefit from the features and advantages of Azure Lab Services, such as:
  - Scalability: Azure Lab Services can handle large numbers of students and virtual machines without compromising performance or availability.
  - Security: Azure Lab Services provides encryption, authentication, and authorization to protect the data and resources in the labs.
  - Cost-effectiveness: Azure Lab Services charges only for the actual usage of the virtual machines, and offers discounts for academic institutions.
  - Flexibility: Azure Lab Services allows instructors to customize the virtual machine templates, the lab policies, the lab schedules, and the lab assignments according to their needs and preferences.
  - Accessibility: Azure Lab Services enables students to access the labs from any device and location with an internet connection.



## Database Management Lab for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Database Management Lab is a practical course that teaches the students how to use and implement database management systems (DBMS) for storing, manipulating, and querying data.
- DBMS are software packages that provide a standard and efficient way of organizing, accessing, and managing data in a database.
- A database is a collection of related data that represents some aspects of the real world. A database can be relational or non-relational, depending on how the data is structured and stored.
- A relational database is a database that organizes data into tables, where each table has a set of columns (attributes) and rows (records). A table can be linked to another table by using a common attribute, called a foreign key. This creates a relationship between the tables, hence the name relational database.
- A non-relational database is a database that does not follow the table structure of a relational database. Instead, it stores data in different formats, such as documents, graphs, key-value pairs, etc. A non-relational database is also known as a NoSQL database, as it does not use the Structured Query Language (SQL) for querying data.
- SQL is the standard language for interacting with relational databases. It allows the users to define, manipulate, and query data in a database. SQL has two main components: Data Definition Language (DDL) and Data Manipulation Language (DML).
- DDL is used to create, alter, and drop the structure of a database, such as tables, views, indexes, etc. DDL commands include CREATE, ALTER, DROP, etc.
- DML is used to insert, update, delete, and retrieve data from a database. DML commands include INSERT, UPDATE, DELETE, SELECT, etc.
- A view is a virtual table that shows a subset or a combination of data from one or more tables. A view does not store data, but only references the data from the underlying tables. A view can be used to simplify complex queries, provide security, or hide the details of the database structure.
- A trigger is a special type of stored procedure that executes automatically when a certain event occurs in the database, such as inserting, updating, or deleting data. A trigger can be used to enforce business rules, maintain data integrity, or perform auditing tasks.
- A stored procedure is a set of SQL statements that can be stored and executed as a single unit in the database. A stored procedure can be used to encapsulate complex logic, improve performance, or reuse code.
- A front-end tool is a software application that provides a graphical user interface (GUI) for interacting with a database. A front-end tool can be used to create forms, menus, reports, charts, etc. that display or manipulate data from a database.
- A form is a GUI component that allows the users to enter or edit data in a database. A form can have various elements, such as text boxes, buttons, checkboxes, etc. that are linked to the attributes of a table or a view.
- A menu is a GUI component that allows the users to navigate through different options or functions in a front-end tool. A menu can have various items, such as commands, submenus, separators, etc. that are linked to the actions or features of a front-end tool.
- A report is a GUI component that allows the users to view or print data from a database in a formatted and organized way. A report can have various elements, such as headers, footers, labels, fields, etc. that are linked to the attributes of a table or a view.
- A virtual lab is a software platform that simulates a real-world environment for learning and experimenting with database concepts and technologies. A virtual lab can provide access to various types of databases, such as MySQL, Oracle, MongoDB, etc. and allow the users to perform various tasks, such as creating, querying, or modifying data in a database.
- A virtual lab can also provide feedback, guidance, or assessment for the users based on their performance or progress in the lab. A virtual lab can be used to enhance the learning outcomes, reduce the cost and complexity, or increase the accessibility and flexibility of a database management lab.



## Data Definition Language (DDL) Statements

- Data Definition Language (DDL) is a subset of SQL that is used to define the structure and schema of a database .
- DDL statements allow the user or the database administrator (DBA) to create, modify, or delete database objects such as tables, indexes, columns, and users  .
- DDL statements are different from Data Manipulation Language (DML) statements, which are used to insert, update, or delete data from the database.
- Some of the common DDL statements are:
  - CREATE: This statement is used to create a new database object, such as a table, an index, or a user  .
  - ALTER: This statement is used to modify an existing database object, such as adding, deleting, or renaming a column, or changing the data type of a column  .
  - DROP: This statement is used to delete an existing database object, such as a table, an index, or a user  .
  - TRUNCATE: This statement is used to remove all the data from a table, but not the table itself .
- The syntax and usage of DDL statements may vary depending on the database system and the SQL dialect .
- DDL statements are executed by the database system and affect the metadata of the database, which is the information about the database objects and their properties .
- DDL statements are usually followed by a COMMIT or a ROLLBACK statement, which are used to save or undo the changes made by the DDL statements .



## Data Manipulation Language(DML) Statements

- Data Manipulation Language (DML) is a subset of SQL that is used to access and modify data in existing tables   .
- DML statements can perform operations such as inserting, updating, deleting, and querying data in a database   .
- DML statements are part of a transaction, which is a logical unit of work that either succeeds or fails as a whole .
- The most common DML statements are:
  - **SELECT**: retrieves data from one or more tables or views  .
  - **INSERT**: adds one or more rows of data to a table or view   .
  - **UPDATE**: modifies one or more columns of data in a table or view   .
  - **DELETE**: removes one or more rows of data from a table or view   .
  - **MERGE**: combines the data from two tables and updates or inserts the result into a third table .
  - **CALL**: executes a stored procedure or function .
  - **EXPLAIN PLAN**: displays the execution plan of a SQL statement .
  - **LOCK TABLE**: locks one or more tables or views to prevent concurrent access .
- DML statements can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT, to filter, aggregate, sort, and limit the data that is returned or modified .
- DML statements can also use subqueries, joins, and set operators to combine data from multiple tables or sources .
- DML statements can be executed interactively using tools such as SQL*Plus or SQL Developer, or embedded in programs using languages such as Java, C#, or Python .
- DML statements can be used to perform various tasks, such as:
  - Populating tables with initial data or test data .
  - Updating or deleting data based on certain conditions or criteria .
  - Querying data for analysis or reporting purposes .
  - Performing data transformations or calculations .
  - Implementing business logic or rules .



## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a component of SQL (Structured Query Language) that is used to retrieve and manipulate data in a relational database management system   .
- DQL statements are used to query the data contained in schema objects, such as tables, views, indexes, etc .
- The purpose of DQL is to get some schema relation based on the query passed to it, and to impose order upon it.
- The most common DQL statement is the SELECT statement, which allows you to specify the columns, tables, conditions, and order of the data you want to retrieve    .
- The syntax of the SELECT statement is as follows:

```sql
SELECT column1, column2, ...
FROM table1, table2, ...
WHERE condition1, condition2, ...
ORDER BY column1, column2, ... ASC|DESC;
```

- The SELECT statement can be used with various clauses and operators to perform complex queries, such as joins, subqueries, aggregations, functions, etc    .
- Some examples of DQL statements are:

```sql
-- Select all the data from the employees table
SELECT * FROM employees;

-- Select the name and salary of the employees who work in the sales department
SELECT name, salary
FROM employees
WHERE department = 'sales';

-- Select the name and average salary of each department
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- Select the name and salary of the employees who earn more than the average salary of their department
SELECT e.name, e.salary
FROM employees e
WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);

-- Select the name and phone number of the customers who have placed orders in the last month
SELECT c.name, c.phone
FROM customers c
JOIN orders o
ON c.id = o.customer_id
WHERE o.date > DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
ORDER BY c.name;
```

- DQL statements are used to perform various tasks in a database, such as data analysis, reporting, data mining, etc   .
- DQL statements are also used to test and verify the data integrity and consistency in a database   .
- DQL statements are executed by the database engine, which parses, optimizes, and executes the query, and returns the result set to the user or application   .
- DQL statements can be written and executed using various tools and interfaces, such as command-line, graphical user interface, web browser, application programming interface, etc   .



## Transaction Control Language(TCL) statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Transaction Control Language (TCL) is a language that manages transactions within the database. Transactions are logical units of work that consist of one or more SQL statements that are executed as a whole  .
- TCL commands are used to control the changes made by the Data Manipulation Language (DML) statements, such as INSERT, UPDATE, and DELETE   .
- TCL commands also allow the statements to be grouped together into logical transactions, which can be committed or rolled back as a unit .
- The main TCL commands are:
  - COMMIT: This command saves all the changes made by the DML statements in the database and ends the current transaction   .
  - ROLLBACK: This command undoes all the changes made by the DML statements in the current transaction and restores the database to its previous state before the transaction started   .
  - SAVEPOINT: This command creates a named point in the current transaction that can be used to roll back to a specific state within the transaction .
  - SET TRANSACTION: This command sets the properties of the current transaction, such as isolation level, read-only or read-write mode, and transaction name.
- TCL commands help to maintain the consistency and integrity of the database and ensure that the transactions follow the ACID properties, which are:
  - Atomicity: A transaction is either completed in its entirety or not at all .
  - Consistency: A transaction transforms the database from one consistent state to another consistent state .
  - Isolation: A transaction is executed independently of other concurrent transactions and does not interfere with them .
  - Durability: The effects of a committed transaction are permanent and do not get lost due to system failures .
- TCL commands can be used in SQL queries or in stored procedures, triggers, and functions.
- TCL commands can be executed automatically by the database system or manually by the user.
- Examples of TCL commands are:

  - COMMIT: `COMMIT;`
  - ROLLBACK: `ROLLBACK;`
  - SAVEPOINT: `SAVEPOINT sp1;`
  - ROLLBACK TO SAVEPOINT: `ROLLBACK TO sp1;`
  - SET TRANSACTION: `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`



## Statement for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- A database management system (DBMS) is a software tool that enables users to manage a database easily.
- A database is a collection of data that is organized so that it can be accessed, manipulated, and updated efficiently.
- A spatial database is a database that stores and manages spatial data, such as geographic coordinates, shapes, maps, and images.
- A virtual lab is a simulated environment that allows users to perform experiments or tasks without using physical equipment or resources.
- Database management systems mapping with virtual lab lab is a subject that covers the theory, design, development, and management of spatial databases using virtual lab software.
- The objectives of this subject are to:
  - Understand the concepts and principles of spatial data and spatial databases.
  - Learn how to use entity-relationship modeling, normalization, and structured query language (SQL) to design and implement spatial databases .
  - Explore the features and functions of various spatial database management systems (SDBMS) and virtual lab software .
  - Apply the knowledge and skills of spatial database management to real-world problems and scenarios .
- The topics of this subject include:
  - Introduction to spatial data and spatial databases .
  - Spatial data models and structures .
  - Spatial query languages and operations .
  - Spatial indexing and access methods .
  - Spatial data analysis and processing .
  - Spatial data visualization and presentation .
  - Spatial database design and implementation .
  - Spatial database management systems and virtual lab software .
  - Spatial database applications and case studies .

