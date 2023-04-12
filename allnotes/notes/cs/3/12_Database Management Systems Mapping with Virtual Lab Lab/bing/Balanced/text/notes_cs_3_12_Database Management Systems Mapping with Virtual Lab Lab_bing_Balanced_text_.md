

## Name of the Lab for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- A possible name for the lab is **Database Management for Relational Databases Lab**.
- The lab aims to teach the basic concepts and skills of database management using relational database management systems (RDBMS) such as MySQL and SQL Server.
- The lab consists of a virtual machine template that contains both MySQL Database Server and SQL Server 2019 server, which are installed and configured for the students to use.
- The lab also provides a set of exercises and assignments that cover topics such as data modeling, SQL queries, database design, normalization, transactions, concurrency control, security, and backup and recovery.
- The lab enables the students to learn how to create, manipulate, and query relational databases using different RDBMS tools and languages.
- The lab also exposes the students to the challenges and best practices of database management in real-world scenarios.
- The lab is suitable for introductory courses in database management for computer science or related majors.
- The lab can be set up and managed using Azure Lab Services, which is a cloud-based platform that allows instructors to create and share virtual labs with their students.
- The lab can be accessed by the students from any device and location, as long as they have an internet connection and a web browser.
- The lab can be customized and scaled according to the instructor's preferences and the class size.



## Name of the Experiment for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- The name of the experiment is **Database Design and Normalization**.
- The objective of the experiment is to learn how to design a relational database schema and apply normalization techniques to reduce data redundancy and anomalies.
- The steps of the experiment are:

  - Identify the entities, attributes, and relationships in a given problem domain.
  - Draw an entity-relationship (ER) diagram to represent the conceptual schema of the database.
  - Convert the ER diagram to a relational schema using mapping rules.
  - Apply normalization rules to decompose the relations into smaller ones that satisfy higher normal forms.
  - Verify the correctness and completeness of the database design using functional dependencies and normal forms.

- The expected outcome of the experiment is to have a normalized relational database schema that can store and retrieve data efficiently and accurately.



## Database Management Lab for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Database Management Lab is a practical course that teaches the students how to use and implement database management systems (DBMS) for storing, manipulating, and querying data.
- DBMS are software packages that provide a standard and efficient way of organizing, accessing, and managing data in a database.
- A database is a collection of related data that represents some aspects of the real world. A database can be relational or non-relational, depending on how the data is structured and stored.
- A relational database is a database that organizes data into tables, where each table has a set of columns (attributes) and rows (records). A table can be linked to another table by using a common attribute, called a foreign key. This creates a relationship between the tables, hence the name relational database.
- A non-relational database is a database that does not follow the table structure of a relational database. Instead, it stores data in different formats, such as documents, graphs, key-value pairs, etc. A non-relational database is also known as a NoSQL database, which stands for Not only SQL.
- SQL (Structured Query Language) is the standard language for interacting with relational databases. It allows the users to create, modify, delete, and query data in a database. SQL has two main components: DDL (Data Definition Language) and DML (Data Manipulation Language).
- DDL is used to define the structure and schema of a database, such as creating, altering, and dropping tables, views, indexes, etc.
- DML is used to manipulate the data in a database, such as inserting, updating, deleting, and selecting records from tables, views, etc.
- A view is a virtual table that shows a subset or a combination of data from one or more tables. A view does not store data, but rather queries data from the underlying tables when needed. A view can be used to simplify complex queries, provide security, or hide details from the users.
- An index is a data structure that improves the performance of queries by providing faster access to data in a table. An index is created on one or more columns of a table, and it stores the values of those columns and their corresponding locations in the table. An index can be clustered or non-clustered, depending on how the data is sorted and stored in the index.
- A high-level programming language extension is a feature that allows the users to embed SQL statements in a programming language, such as C, Java, Python, etc. This enables the users to combine the power of SQL with the functionality of a programming language, such as loops, variables, functions, etc. A high-level programming language extension can be either static or dynamic, depending on how the SQL statements are processed and executed.
- A static extension is one that requires the SQL statements to be pre-compiled and checked for syntax and semantic errors before execution. A static extension provides better performance and security, but less flexibility and portability. An example of a static extension is Embedded SQL.
- A dynamic extension is one that allows the SQL statements to be constructed and executed at run-time. A dynamic extension provides more flexibility and portability, but less performance and security. An example of a dynamic extension is JDBC (Java Database Connectivity).
- A front-end tool is a software application that provides a graphical user interface (GUI) for interacting with a database. A front-end tool can be used to create, modify, delete, and query data in a database, as well as to design and implement forms, reports, menus, etc. A front-end tool can be either standalone or web-based, depending on how the application is accessed and deployed.
- A form is a GUI component that allows the users to enter, edit, and view data in a database. A form can have various elements, such as text boxes, buttons, checkboxes, radio buttons, etc. A form can also have triggers, which are actions that are executed when a certain event occurs, such as opening, closing, validating, or submitting a form.
- A report is a GUI component that allows the users to display and print data from a database in a formatted and organized way. A report can have various elements, such as headers, footers, labels, fields, charts, etc. A report can also have parameters, which are values that are entered by the users to filter or customize the data in the report.
- A menu is a GUI component that allows the users to navigate and access the different functions and features of a front-end tool or application. A menu can have various



## Data Definition Language (DDL) Statements

- Data Definition Language (DDL) is a subset of SQL that is used to define the structure and schema of a database.
- DDL statements can create, modify, or delete database objects such as tables, indexes, columns, constraints, views, and users.
- DDL statements are executed by the database system to create or update the metadata of the database.
- Some common DDL statements are:
  - CREATE: used to create a new database object.
  - ALTER: used to modify an existing database object.
  - DROP: used to delete an existing database object.
  - TRUNCATE: used to remove all the data from a table without deleting the table itself.
  - RENAME: used to change the name of a database object.
- DDL statements are different from Data Manipulation Language (DML) statements, which are used to insert, update, delete, or query the data in a database.
- DDL statements are also different from Data Control Language (DCL) statements, which are used to grant or revoke permissions and access rights to database objects.
- DDL statements can be used to map the logical design of a database to its physical implementation, by specifying the storage, indexing, partitioning, and distribution of the data.
- DDL statements can also be used to enforce data integrity and security constraints, such as primary keys, foreign keys, check constraints, and user roles.
- DDL statements can be executed interactively using a command-line interface, a graphical user interface, or a web-based interface, or they can be embedded in a program or script using a programming language or a framework.
- DDL statements can be tested and validated using a virtual lab environment, which is a simulated or emulated platform that mimics the behavior and functionality of a real database system. A virtual lab can help users to learn and practice DDL statements without affecting the actual database.



## Data Manipulation Language(DML) Statements

- Data manipulation language (DML) statements are used to access and manipulate data in existing schema objects, such as tables, views, or indexes  .
- DML statements can update, insert, delete, or select data from the database   .
- DML statements are part of a transaction, which is a sequence of one or more SQL statements that are treated as a unit by the database . A transaction can be committed (made permanent) or rolled back (undone) by the user or the database system .
- The most common DML statements are:
  - **SELECT**: retrieves data from one or more tables or views    . It can also perform calculations, aggregations, joins, filters, and other operations on the retrieved data    .
  - **INSERT**: adds one or more rows of data to a table or a view    . It can also specify the values for each column or use a subquery to get the values from another table or view    .
  - **UPDATE**: modifies one or more columns of data in a table or a view    . It can also use a subquery to get the new values from another table or view    .
  - **DELETE**: removes one or more rows of data from a table or a view    . It can also use a subquery to specify which rows to delete from another table or view    .
- Some other DML statements are:
  - **MERGE**: combines the functionality of INSERT and UPDATE statements by inserting new rows or updating existing rows based on a condition    .
  - **CALL**: invokes a stored procedure or a function    .
  - **EXPLAIN PLAN**: displays the execution plan of a SQL statement, which shows how the database will access the data    .
  - **LOCK TABLE**: locks one or more tables or views in a specified mode to prevent other users from modifying the data    .
- DML statements can be used in various contexts, such as interactive SQL tools, application programs, scripts, or stored procedures  .
- DML statements can be affected by various factors, such as constraints, triggers, indexes, privileges, or performance  .



## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a component of SQL (Structured Query Language) that is used to retrieve and manipulate data in a relational database management system  .
- DQL statements are used to perform queries on the data within schema objects, such as tables, views, or indexes .
- The purpose of DQL is to get some schema relation based on the query passed to it, and to impose order upon it.
- The most common DQL statement is the SELECT statement, which allows you to select data from one or more tables or views, and apply filters, joins, aggregations, or sorting to the result set  .
- Some examples of DQL statements are:

  - SELECT * FROM employees; -- This statement selects all the data from the employees table.
  - SELECT name, salary FROM employees WHERE department = 'Sales'; -- This statement selects the name and salary columns from the employees table, where the department is 'Sales'.
  - SELECT e.name, e.salary, d.name AS department FROM employees e JOIN departments d ON e.department_id = d.id ORDER BY e.salary DESC; -- This statement selects the name and salary of the employees, and the name of their department, from the employees and departments tables, using a join condition on the department_id column, and sorts the result by salary in descending order.
  - SELECT AVG(salary) AS average_salary FROM employees; -- This statement calculates the average salary of the employees, and assigns it an alias of average_salary.

- DQL statements can be executed using various tools, such as command-line interfaces, graphical user interfaces, or web applications, depending on the database system and the user preference .
- DQL statements can also be embedded in other programming languages, such as Java, Python, or PHP, to interact with the database from the application code .



## Transaction Control Language(TCL) statements

- Transaction Control Language (TCL) is a type of SQL command that is used to manage transactions in a database.
- Transactions are a way of grouping multiple SQL statements into a single unit of work, so that either all of the statements are executed, or none of them are.
- This helps to ensure the consistency and integrity of the data in the database.
- TCL commands are used to keep track of the modifications that DML statements make.
- TCL also allows you to organise statements into logical transactions.
- The main TCL commands are:
  - **COMMIT**: It is used to save the transactions in the database . It marks the end of a successful transaction.
  - **ROLLBACK**: It is used to restore the database to that state which was last committed . It undoes the changes made by the previous SQL statements in the current transaction.
  - **SAVEPOINT**: It is used to create a point in the transaction where the changes done till that point will be unchanged and all the transactions after that point will be rolled back . It allows you to partially commit or rollback a transaction.
  - **SET TRANSACTION**: It is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write mode, etc. It must be the first statement in a transaction.



## Statement for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- A database management system (DBMS) is a software tool that enables users to manage a database easily.
- A database is a collection of data that is organized so that it can be accessed, manipulated, and updated by users or applications.
- A virtual lab is a simulated environment that allows users to perform experiments or tasks without the need for physical equipment or resources.
- Database management systems mapping with virtual lab lab is a subject that covers the theory, design, development, and management of modern relational databases using a virtual lab environment.
- The subject aims to provide students with the following learning outcomes:
  - Understand the concepts and principles of relational databases and data models.
  - Apply entity-relationship modeling, normalization, and structured query language (SQL) to design and implement databases.
  - Use a virtual lab tool to create, query, and manipulate databases in a simulated environment.
  - Evaluate the performance, security, and integrity of databases and database management systems.
  - Develop skills in database administration, backup, recovery, and tuning.

