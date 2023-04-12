

# Database Management Systems Mapping with Virtual Lab Lab

- Database management systems (DBMS) are software applications that store, manipulate, and query data in a structured or semi-structured format.
- DBMS can be classified into different types based on the data model, such as relational, hierarchical, network, object-oriented, document, graph, etc.
- DBMS can also be categorized based on the vendor, such as Oracle, MySQL, SQL Server, MongoDB, Neo4j, etc.
- A virtual lab is a simulated environment that allows users to perform experiments or tasks using virtual machines, software, and network connections.
- A virtual lab can be used to teach or learn database management concepts and skills, such as data modeling, normalization, SQL, transactions, concurrency control, security, etc.
- A virtual lab can also be used to test or compare different DBMS or data models, such as MySQL vs SQL Server, relational vs document, etc.
- A virtual lab can be created using various tools and platforms, such as Azure Lab Services, Labguru, Labworks, etc.
- A virtual lab can have different features and functionalities, such as user management, template creation, resource allocation, monitoring, reporting, etc.
- A virtual lab can have different benefits and challenges, such as cost-effectiveness, flexibility, scalability, accessibility, security, reliability, etc.



## Name of the Experiment for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- One possible name of the experiment is **Setting up and querying relational databases using Azure Lab Services**.
- The objective of this experiment is to learn how to create, manage, and query relational databases using MySQL and SQL Server on Azure Lab Services.
- The steps of this experiment are:

  - Create a lab account and a lab on Azure Lab Services.
  - Create a virtual machine template with MySQL Database Server and SQL Server 2019 server installed.
  - Configure the network settings and firewall rules to allow access to the database servers.
  - Create a lab class and assign students to the virtual machines.
  - Provide students with instructions on how to connect to the database servers using MySQL Workbench and SQL Server Management Studio.
  - Provide students with exercises on creating, modifying, and querying relational databases using SQL commands.
  - Monitor and manage the lab resources and student progress using the Azure Lab Services portal.

- The expected outcomes of this experiment are:

  - Students will be able to create and manage relational databases using MySQL and SQL Server.
  - Students will be able to perform basic and advanced SQL queries on relational databases.
  - Students will be able to understand the concepts and principles of relational database management systems.
  - Students will be able to use Azure Lab Services as a platform for learning and teaching database management.



## Database Management Lab for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Database management lab is a practical course that teaches the students how to create and manipulate various database systems using SQL and other tools.
- Database management lab covers the following topics:
  - Database concepts and terminology
  - Entity-relationship model and database design
  - Relational model and relational algebra
  - SQL queries and data manipulation
  - Database security and integrity
  - Database administration and performance tuning
- Database management lab requires the students to have access to a database management system (DBMS) such as MySQL, Oracle, SQL Server, etc. and a suitable interface such as phpMyAdmin, SQL Developer, etc.
- Database management lab can be conducted in a physical or virtual lab environment. A virtual lab is a cloud-based service that provides the students with a pre-configured and isolated lab environment where they can practice their database skills without affecting the real system.
- Database management lab can be mapped with a virtual lab service such as Azure Lab Services, which offers the following benefits:
  - Flexible and scalable lab creation and management
  - Cost-effective and pay-as-you-go pricing model
  - Secure and compliant data protection and access control
  - Integrated and interactive learning experience
  - Customizable and reusable lab templates and scenarios
- Database management lab can be assessed using various methods such as quizzes, assignments, projects, etc. The students can demonstrate their learning outcomes by applying their database knowledge and skills to solve real-world problems and scenarios.



# Data Definition Language(DDL) Statements

- Data Definition Language (DDL) is a group of SQL statements that you can execute to manage database objects, such as tables, views, functions, and policies   .
- Using DDL statements, you can perform powerful commands in your database such as creating, modifying, and dropping objects   .
- DDL commands are usually executed in a SQL browser or stored procedure.
- Some common DDL commands are:
  - CREATE: to create a new database object, such as a table or a view  .
  - ALTER: to modify an existing database object, such as adding or removing a column or changing a data type  .
  - DROP: to delete a database object, such as a table or a view  .
  - RENAME: to change the name of a database object, such as a table or a view .
  - TRUNCATE: to remove all the data from a table, but not the table itself .
- DDL statements can be used to map with virtual lab lab, which is a tool that allows you to create and manipulate databases using a graphical user interface (GUI) or a command-line interface (CLI).
- To use DDL statements in virtual lab lab, you need to:
  - Connect to a database server using your credentials.
  - Select a database to work with.
  - Write and execute DDL statements in the SQL editor or use the GUI to create and modify database objects.
  - View the results of your DDL statements in the output window or the object browser.
  - Save and export your DDL statements as a script file or a report file.

: https://www.vlab.co.in/best-labs/dbms-lab



# Data Manipulation Language(DML) Statements

- Data manipulation language (DML) statements are used to access and manipulate data in existing schema objects, such as tables, views, or indexes  .
- DML statements can update, insert, and delete data from the tables  .
- DML statements are part of a transaction, which is a sequence of one or more SQL statements that are treated as a unit .
- A transaction can be committed, which means the changes made by the DML statements are made permanent in the database, or rolled back, which means the changes are undone and the database is restored to its previous state .
- The most common DML statements are:
  - **SELECT**: retrieves data from one or more tables or views  .
  - **INSERT**: adds one or more rows of data to a table or a view  .
  - **UPDATE**: modifies one or more columns of data in a table or a view  .
  - **DELETE**: removes one or more rows of data from a table or a view  .
  - **MERGE**: combines the data from two tables and updates or inserts the result into a third table .
  - **CALL**: executes a stored procedure or a function .
  - **EXPLAIN PLAN**: displays the execution plan of a SQL statement .
  - **LOCK TABLE**: locks one or more tables or views to prevent concurrent access by other transactions .
- DML statements can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, OFFSET, etc., to filter, aggregate, sort, or limit the data returned  .
- DML statements can also use subqueries, joins, unions, and other operators to combine data from multiple tables or views  .
- DML statements can be executed interactively using tools such as SQL*Plus or SQL Developer, or embedded in programs written in languages such as Java, C#, Python, etc .



# Data Query Language (DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a subset of SQL (Structured Query Language) that is used to retrieve data from a relational database.
- DQL statements are composed of clauses, expressions, predicates, and keywords that specify the criteria for the data to be returned.
- The most common DQL statement is the SELECT statement, which has the following syntax:

```sql
SELECT [DISTINCT] column_list
FROM table_list
[WHERE search_condition]
[GROUP BY group_by_list]
[HAVING search_condition]
[ORDER BY order_by_list]
[LIMIT row_limit]
[OFFSET row_offset];
```

- The SELECT clause specifies the columns or expressions to be returned in the result set. The DISTINCT keyword eliminates duplicate rows from the result set.
- The FROM clause specifies the tables or views to be queried. The tables or views can be joined using various join types, such as inner join, left join, right join, full join, cross join, natural join, etc.
- The WHERE clause specifies the filter condition for the rows to be returned. The condition can be a logical expression that combines multiple predicates using logical operators, such as AND, OR, NOT, etc.
- The GROUP BY clause specifies the grouping criteria for the rows to be aggregated. The grouping columns or expressions must be included in the SELECT clause. The GROUP BY clause is often used with aggregate functions, such as SUM, AVG, COUNT, MIN, MAX, etc.
- The HAVING clause specifies the filter condition for the groups to be returned. The condition can be a logical expression that involves aggregate functions or grouping columns or expressions.
- The ORDER BY clause specifies the sorting order for the rows or groups to be returned. The order can be ascending (ASC) or descending (DESC). The default order is ascending. The ORDER BY clause can also use column aliases or ordinal numbers to refer to the columns or expressions in the SELECT clause.
- The LIMIT clause specifies the maximum number of rows or groups to be returned. The LIMIT clause can be used for pagination or performance optimization.
- The OFFSET clause specifies the number of rows or groups to be skipped before returning the result set. The OFFSET clause can be used for pagination or performance optimization.

- Some examples of DQL statements are:

```sql
-- Select all columns from the customers table
SELECT * FROM customers;

-- Select the first name, last name, and email of the customers whose country is 'USA'
SELECT first_name, last_name, email
FROM customers
WHERE country = 'USA';

-- Select the total number of orders and the average order amount for each customer
SELECT customer_id, COUNT(*) AS total_orders, AVG(order_amount) AS avg_order_amount
FROM orders
GROUP BY customer_id;

-- Select the customer name and the total order amount for the customers who have placed more than 10 orders
SELECT c.first_name || ' ' || c.last_name AS customer_name, SUM(o.order_amount) AS total_order_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(*) > 10;

-- Select the top 5 products by sales amount in descending order
SELECT p.product_name, SUM(o.order_amount) AS sales_amount
FROM products p
JOIN order_details od ON p.product_id = od.product_id
JOIN orders o ON od.order_id = o.order_id
GROUP BY p.product_id, p.product_name
ORDER BY sales_amount DESC
LIMIT 5;
```

- DQL statements can be executed using various tools or applications, such as command-line interfaces, graphical user interfaces, web browsers, programming languages, etc.
- DQL statements can be tested and verified using virtual lab environments, such as SQL Fiddle, DB Fiddle, SQLZOO, etc. These environments allow users to create and populate tables, write and run queries, and see the results online.



# Transaction Control Language(TCL) statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Transaction Control Language (TCL) is a language that manages transactions within the database. Transactions are a sequence of operations that are performed as a single logical unit of work. Transactions ensure the consistency and integrity of the database by following the ACID properties (Atomicity, Consistency, Isolation, and Durability).
- TCL commands are used to execute, save, or undo the changes made by the Data Manipulation Language (DML) statements, such as INSERT, UPDATE, or DELETE. TCL commands also allow the statements to be grouped together into logical transactions.
- The main TCL commands are:
  - COMMIT: This command saves all the changes made by the DML statements in the current transaction to the database. It also ends the current transaction and starts a new one. COMMIT ensures that the database state is changed from one consistent state to another consistent state.
  - ROLLBACK: This command undoes all the changes made by the DML statements in the current transaction and restores the database to its previous state. It also ends the current transaction and starts a new one. ROLLBACK ensures that the database state remains consistent in case of any error or failure.
  - SAVEPOINT: This command creates a named point in the current transaction that can be used to roll back to a specific state within the transaction. It allows partial undoing of the changes made by the DML statements. SAVEPOINTs can be nested within a transaction.
  - SET TRANSACTION: This command sets the characteristics of the current transaction, such as the isolation level, the read/write mode, or the name. It must be the first statement of a transaction. SET TRANSACTION ensures that the transaction is executed according to the specified parameters.



## Statement for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- A database management system (DBMS) is a software tool that enables users to manage a database easily.
- A database is a collection of data that is organized so that it can be accessed, manipulated, and updated efficiently.
- A spatial database is a type of database that stores and manages spatial data, such as geographic features, coordinates, and topology.
- A virtual lab is a simulated environment that allows users to perform experiments or tasks without the need for physical equipment or resources.
- Database management systems mapping with virtual lab lab is a subject that covers the theory, design, development, and management of spatial databases using a virtual lab environment.
- The objectives of this subject are to:
  - Understand the concepts and principles of spatial data and spatial databases.
  - Learn how to model, design, and implement spatial databases using entity-relationship modeling, normalization, and structured query language (SQL) .
  - Learn how to use a virtual lab tool to create, manipulate, query, and analyze spatial databases.
  - Learn how to apply spatial database techniques to various domains, such as geography, remote sensing, urban planning, and natural resource management .
- The topics covered in this subject are:
  - Introduction to spatial data and spatial databases 
  - Spatial data models and structures 
  - Spatial query languages and operators 
  - Spatial indexing and access methods 
  - Spatial data analysis and processing 
  - Spatial database design and implementation 
  - Virtual lab tool for spatial databases
  - Spatial database applications and case studies

