

## Unit 1 - Introduction

- This unit provides an overview of the course objectives, topics, and assessment methods.
- The course aims to introduce the basic concepts and principles of artificial intelligence (AI), such as agents, search, knowledge representation, reasoning, planning, learning, and natural language processing.
- The course also covers some of the applications and challenges of AI, such as expert systems, robotics, computer vision, and ethical issues.
- The course requires some background in mathematics, logic, and programming, as well as an interest and curiosity in AI.
- The course is divided into 12 units, each consisting of lectures, readings, quizzes, and assignments.
- The course is assessed by a midterm exam, a final exam, and a project. The midterm exam covers units 1-6, the final exam covers units 7-12, and the project involves implementing an AI system of your choice.



# Overview for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A database is a collection of related data that can be stored, manipulated, and retrieved by a software system.
- A database management system (DBMS) is a software system that provides the functionality to create, maintain, and manipulate databases.
- A DBMS consists of three components: data, data model, and database language.
- Data is the actual information stored in the database, such as names, addresses, phone numbers, etc.
- Data model is the logical structure and organization of the data, such as tables, columns, rows, keys, relationships, etc.
- Database language is the set of commands and syntax used to interact with the database, such as SQL, DDL, DML, DCL, etc.
- A DBMS can support different types of data models, such as relational, hierarchical, network, object-oriented, etc.
- A DBMS can also provide various features and services, such as data integrity, data security, data concurrency, data recovery, data backup, data replication, data warehousing, data mining, etc.
- A DBMS can be classified into different categories based on various criteria, such as data model, architecture, functionality, etc.
- Some examples of popular DBMS are Oracle, MySQL, SQL Server, MongoDB, etc.



# Database System vs File System

- A **file system** is a software that organizes and manages files on a storage media, such as a hard disk or a flash drive. A file system provides basic operations such as creating, deleting, renaming, copying, and moving files. A file system does not have any built-in mechanism for ensuring data consistency, security, or recovery in case of failures. A file system also does not support complex queries or transactions on the data stored in the files. A file system is suitable for storing simple and static data that does not require frequent updates or processing. Examples of file systems are FAT, NTFS, ext4, etc.    

- A **database management system (DBMS)** is a software that allows you to access, create, and administer databases. A database is a collection of structured and organized data that can be manipulated using a query language, such as SQL. A DBMS provides various features for ensuring data consistency, security, and recovery in case of failures. A DBMS also supports complex queries and transactions on the data stored in the databases. A DBMS is suitable for storing dynamic and complex data that requires frequent updates or processing. Examples of DBMS are MySQL, Oracle, MongoDB, etc.     

- The main differences between a database system and a file system are:

  - A database system is designed for handling data objects, whereas a file system is designed for handling files. A file system does not have any knowledge of the structure or meaning of the data stored in the files, whereas a database system has a schema that defines the structure and meaning of the data stored in the databases.  

  - A database system supports a query language, such as SQL, that allows you to perform various operations on the data, such as insertion, deletion, modification, selection, aggregation, etc. A file system does not support any query language, and you have to write your own code to perform any operation on the data stored in the files.   

  - A database system ensures data consistency, security, and recovery by using various mechanisms, such as concurrency control, locking, logging, backup, encryption, authentication, authorization, etc. A file system does not have any built-in mechanism for ensuring data consistency, security, or recovery, and you have to rely on external tools or your own code to implement these features.     

  - A database system can handle large amounts of data efficiently, as it uses indexing, caching, compression, partitioning, etc. to optimize the data access and storage. A file system can handle only limited amounts of data, as it does not use any optimization techniques, and it may suffer from fragmentation, duplication, or corruption of data.    

- The main advantages of using a database system over a file system are:

  - A database system provides a higher level of abstraction and functionality for data management, as it allows you to manipulate data objects using a query language, rather than files using low-level system calls.  

  - A database system ensures data integrity, security, and reliability, as it uses various mechanisms to prevent data loss, corruption, or unauthorized access.     

  - A database system improves data availability and performance, as it uses various techniques to optimize the data access and storage, and to handle concurrent and distributed requests.    

- The main disadvantages of using a database system over a file system are:

  - A database system requires more resources, such as memory, disk space, CPU, etc., as it has more overhead and complexity than a file system.   

  - A database system requires more maintenance, such as installation, configuration, backup, recovery, tuning, etc., as it has more features and functionality than a file system.   

  - A database system may have compatibility



# Database System Concept and Architecture

- A database system is a software package that manages data stored in a database and provides various operations to access and manipulate the data.
- A database system consists of several components, such as the database, the database management system (DBMS), the database applications, and the users.
- A database is a collection of related data that represents some aspects of the real world. A database can be organized in different ways, such as tables, graphs, documents, etc.
- A DBMS is a software system that provides the functionality to create, maintain, and manipulate databases. A DBMS typically supports a specific data model, such as relational, object-oriented, or XML.
- A database application is a software program that interacts with the DBMS to perform specific tasks, such as querying, updating, or analyzing the data. A database application can be written in various languages, such as SQL, Java, Python, etc.
- A user is a person or a program that uses the database system to access or modify the data. A user can be classified into different types, such as end users, application programmers, database administrators, etc.

- The architecture of a database system defines the logical and physical structure of the system components and their interactions. The architecture can vary depending on the design goals, the data model, the system environment, and the user requirements.
- The architecture of a database system can be classified into three levels: external, conceptual, and internal.
- The external level defines the view of the data that is seen by a specific user or a group of users. An external view can be customized to suit the needs and preferences of the user. An external view can also hide some details of the data that are irrelevant or sensitive to the user.
- The conceptual level defines the logical structure of the data that is stored in the database. The conceptual level describes the data entities, their attributes, and their relationships. The conceptual level is independent of the physical implementation of the data and the user views of the data.
- The internal level defines the physical organization and storage of the data on the disk. The internal level describes the data structures, such as files, records, indexes, etc., that are used to store and access the data. The internal level is dependent on the hardware and software characteristics of the system.

- The architecture of a database system can also be classified into two types: centralized and distributed.
- A centralized database system is a system where the database and the DBMS are located on a single computer or a server. A centralized database system can be accessed by multiple users or applications through a network. A centralized database system has the advantages of simplicity, efficiency, and security, but also has the disadvantages of scalability, reliability, and availability.
- A distributed database system is a system where the database and the DBMS are distributed across multiple computers or servers that are connected by a network. A distributed database system can be accessed by multiple users or applications through the network. A distributed database system has the advantages of scalability, reliability, and availability, but also has the disadvantages of complexity, overhead, and consistency.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Database Management System. Here are some notes on the topic of Data Model Schema and Instances for Unit 1 - Introduction.

# Data Model Schema and Instances

- A **data model** is a collection of concepts and rules for describing the structure, meaning, and constraints of the data stored in a database.
- A **schema** is a description of a particular collection of data, using a given data model. It defines the names and types of the entities, attributes, and relationships that exist in the data.
- An **instance** is a snapshot of the data in a database at a given point in time. It is a set of tuples that satisfy the schema.
- A **database** is a collection of data that is managed by a database management system (DBMS). A DBMS supports the definition, creation, manipulation, and querying of the data in a database.

## Examples of Data Models

- Some common data models are:
  - **Relational model**: Represents data as tables, where each row is a tuple and each column is an attribute. Supports operations such as selection, projection, join, and aggregation on the tables.
  - **Entity-relationship model**: Represents data as entities, attributes, and relationships. Supports the graphical representation of the data using diagrams, where entities are shown as rectangles, attributes are shown as ovals, and relationships are shown as diamonds.
  - **Hierarchical model**: Represents data as a tree, where each node is a record and each edge is a link. Supports operations such as insertion, deletion, and retrieval of records based on the parent-child relationship.
  - **Network model**: Represents data as a graph, where each node is a record and each edge is a link. Supports operations such as insertion, deletion, and retrieval of records based on the arbitrary connections among them.
  - **Object-oriented model**: Represents data as objects, where each object has a unique identity, a set of attributes, and a set of methods. Supports operations such as inheritance, encapsulation, polymorphism, and message passing on the objects.

## Examples of Schema and Instance

- Suppose we have a relational database that stores information about students, courses, and enrollments. The schema of the database can be defined as follows:

  - Student (**sid**, name, major, gpa)
  - Course (**cid**, title, instructor, credits)
  - Enroll (**sid**, **cid**, grade)

  where the attributes in bold are the primary keys of the tables.

- An instance of the database can be shown as follows:

  | sid | name  | major | gpa |
  | --- | ----- | ----- | --- |
  | 101 | Alice | CS    | 3.8 |
  | 102 | Bob   | Math  | 3.5 |
  | 103 | Carol | CS    | 3.9 |

  | cid | title           | instructor | credits |
  | --- | --------------- | ---------- | ------- |
  | CS1 | Introduction to CS | Smith      | 4       |
  | CS2 | Data Structures    | Jones      | 3       |
  | MA1 | Calculus           | Lee        | 4       |

  | sid | cid | grade |
  | --- | --- | ----- |
  | 101 | CS1 | A     |
  | 101 | CS2 | B     |
  | 102 | MA1 | A     |
  | 103 | CS1 | A     |
  | 103 | CS2 | A     |

- Suppose we have an entity-relationship database that stores information about movies, actors, and directors. The schema of the database can be defined as follows:

  - Movie (**title**, year, genre, rating)
  - Actor (**name**, dob, gender)
  - Director (**name**, dob, gender)
  - ActsIn (**name**, **title**, role)
  - Directs (**name**, **title**)

  where the attributes in bold are the primary keys of the entities or relationships.

- An instance of the database can be shown as follows:

  ER diagram



# Data Independence and Database Language and Interfaces

- Data independence is a property of DBMS that allows the database schema to be changed without affecting the applications that use the data.
- Database schema is the structure and organization of the data in the database, which can be divided into three levels: external, conceptual, and internal.
- External schema is the view of the data that is seen by the end-users or applications. It can be different for different users or applications, depending on their needs and preferences.
- Conceptual schema is the logical view of the data that is shared by all the users or applications. It describes the entities, attributes, relationships, and constraints of the data, without specifying the physical details of storage or implementation.
- Internal schema is the physical view of the data that is seen by the DBMS. It describes how the data is stored, organized, indexed, and accessed by the DBMS.
- Data independence can be classified into two types: logical data independence and physical data independence.
- Logical data independence is the ability to change the conceptual schema without affecting the external schema or the applications. It allows the DBMS to adapt to the changing requirements of the data, such as adding, deleting, or modifying entities, attributes, or relationships.
- Physical data independence is the ability to change the internal schema without affecting the conceptual schema or the applications. It allows the DBMS to optimize the performance, efficiency, and security of the data, such as changing the storage structure, access method, or indexing strategy.
- Data independence is achieved by using a three-schema architecture and a data definition language (DDL) and a data manipulation language (DML) to separate the data from the applications .
- A DDL is a language that is used to define the database schema at each level. It allows the DBMS to create, modify, or delete the schema objects, such as tables, views, indexes, or constraints.
- A DML is a language that is used to manipulate the data in the database. It allows the applications to insert, update, delete, or query the data, without knowing the details of the schema or the storage.
- A database language is a combination of a DDL and a DML, which can be either procedural or non-procedural.
- A procedural database language requires the applications to specify both what data to access and how to access it. It gives more control and flexibility to the applications, but also more complexity and responsibility.
- A non-procedural database language requires the applications to specify only what data to access, and leaves the how to the DBMS. It gives more simplicity and abstraction to the applications, but also less control and efficiency.
- A database interface is a software component that allows the applications to communicate with the DBMS using a database language. It can be either embedded or interactive.
- An embedded database interface integrates the database language with a host programming language, such as C, Java, or Python. It allows the applications to use the features and functions of both languages, but also requires more coding and compilation.
- An interactive database interface provides a separate environment for the database language, such as SQL*Plus, MySQL, or MongoDB. It allows the applications to use the database language directly, but also requires more switching and typing.



# Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects such as tables, views, indexes, schemas, etc. 
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas. 
- DDL is used to specify the logical and physical characteristics of the data, such as data types, constraints, relationships, and storage options. 
- DDL is also used to grant or revoke access privileges to the database objects. 
- Some common DDL commands are CREATE, ALTER, DROP, RENAME, and TRUNCATE. 
- DDL is part of the Structured Query Language (SQL), which is a standard language for managing relational databases. 
- DDL is different from Data Manipulation Language (DML), which is used to insert, update, delete, and query data in a database. 
- DDL is also different from Data Control Language (DCL), which is used to control the transactions and concurrency in a database. 
- DDL is executed by the database management system (DBMS), which interprets the DDL statements and performs the corresponding actions on the database. 
- DDL is important for defining the schema of a database, which is the blueprint of how the data is organized and stored.



# DML

DML stands for Data Manipulation Language. It is a subset of SQL statements that are used to manipulate data in a database. DML includes the following operations:

- **INSERT**: This operation is used to insert new data into a table or view.
- **SELECT**: This operation is used to retrieve data from one or more tables or views.
- **UPDATE**: This operation is used to modify existing data in a table or view.
- **DELETE**: This operation is used to remove existing data from a table or view.

DML statements can be executed directly by the user or by a program that interacts with the database. DML statements can also be triggered by certain events that affect the data, such as insertions, updates, or deletions. These events can be handled by special stored procedures called DML triggers.

DML is mainly concerned with the performance and efficiency of the database, as well as the consistency and integrity of the data. DML utilizes the append-only nature of the Hadoop Distributed File System (HDFS) storage, which means that data can only be added to the end of a file, not modified or deleted.

Some of the characteristics of DML are:

- It is a declarative language, which means that the user specifies what data to manipulate, not how to manipulate it.
- It is a set-oriented language, which means that it operates on sets of data, not individual records.
- It supports various data types, such as numeric, string, date, time, etc.
- It supports various operators, such as arithmetic, logical, comparison, etc.
- It supports various functions, such as aggregate, scalar, window, etc.
- It supports various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.
- It supports various joins, such as inner, outer, cross, etc.
- It supports various subqueries, such as correlated, uncorrelated, etc.
- It supports various expressions, such as case, coalesce, nullif, etc.



# Overall Database Structure

A database is a collection of information that is related to a particular subject or purpose, such as tracking customer orders or maintaining a music collection. A database can be considered a structure in realization of the database language. The database system is divided into three components: Query Processor, Storage Manager, and Disk Storage. These are explained as following below:

- **Query Processor**: This component is responsible for interpreting and executing the queries given by the users or applications. It consists of several modules, such as query parser, query optimizer, query executor, etc. The query processor also interacts with the storage manager to access or modify the data in the disk storage.
- **Storage Manager**: This component is responsible for managing the storage and retrieval of data in the disk storage. It consists of several modules, such as buffer manager, file manager, access methods, etc. The storage manager also provides various services, such as data compression, encryption, backup, recovery, etc.
- **Disk Storage**: This component is responsible for storing the data in the physical devices, such as hard disks, flash drives, etc. The data is organized into files, which are further divided into pages or blocks. The disk storage also maintains various metadata, such as file headers, indexes, catalogs, etc.

The database system also uses a database schema to describe how real-world entities are modeled in the database. A database schema consists of the following elements:

- **Tables**: These are the basic units of data storage in a database. Each table represents a set of records or tuples that share the same attributes or fields. For example, a table named Customers may store the information of all the customers of a company.
- **Fields**: These are the individual units of data within a table. Each field represents an attribute or property of the records in the table. For example, a field named CustomerID may store the unique identification number of each customer in the Customers table.
- **Records**: These are the rows or instances of data within a table. Each record represents a single entity or object in the real world. For example, a record in the Customers table may store the information of one customer, such as name, address, phone number, etc.
- **Keys**: These are the fields or combinations of fields that are used to identify or relate the records in the tables. There are different types of keys, such as primary keys, foreign keys, candidate keys, etc. For example, a primary key is a field or combination of fields that uniquely identifies each record in a table, such as CustomerID in the Customers table.
- **Relationships**: These are the associations or links between the tables in a database. There are different types of relationships, such as one-to-one, one-to-many, many-to-many, etc. For example, a one-to-many relationship is a relationship where one record in a table can be related to many records in another table, such as one customer can have many orders.
- **Constraints**: These are the rules or conditions that are applied to the tables, fields, records, or relationships in a database. They are used to ensure the validity, integrity, and consistency of the data in the database. For example, a constraint may specify that a field cannot be null, or that a foreign key must match a primary key in another table.

The database schema can be represented in various ways, such as diagrams, tables, or languages. For example, the following diagram shows a simple database schema for a company that sells products to customers:

Database schema diagram



The following table shows the same database schema in a tabular format:

| Table | Field | Data Type | Key | Constraint |
| --- | --- | --- | --- | --- |
| Customers | CustomerID | Number | Primary | Not Null |
| Customers | FirstName | Text |  | Not Null |
| Customers | LastName | Text |  | Not Null |
| Customers | Address | Text |  |  |
| Customers | City | Text |  |  |
| Customers | State | Text |  |  |
| Customers | ZipCode | Text |  |  |
| Customers | Phone | Text |  |  |
| Products | ProductID | Number



# Data Modeling Using the Entity Relationship Model

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship (ER) model is a widely used data modeling technique that uses graphical symbols and connectors to depict the entities and their relationships in a database.
- An entity is a real-world object or concept that can be identified and distinguished from others. For example, a student, a course, or a book.
- A relationship is an association or link between two or more entities. For example, a student enrolls in a course, or a book belongs to a category.
- An ER diagram is a diagram that shows the entities and relationships in an ER model. It consists of the following components:
  - Entity sets: A collection of entities of the same type. They are represented by rectangles with the name of the entity set inside.
  - Attributes: The properties or characteristics of an entity or a relationship. They are represented by ovals with the name of the attribute inside. An attribute can be simple or composite, single-valued or multi-valued, derived or stored, or part of a key.
  - Relationships: The connections between entity sets. They are represented by diamonds with the name of the relationship inside.
  - Cardinality: The number of occurrences of one entity that can be associated with another entity in a relationship. It can be one-to-one, one-to-many, many-to-one, or many-to-many. It is shown by placing numbers or symbols near the ends of the relationship lines.
  - Participation: The degree of involvement of an entity in a relationship. It can be total or partial. It is shown by placing a double line or a single line near the ends of the relationship lines.
  - Generalization: The process of grouping common attributes and relationships of two or more entity sets into a higher-level entity set. It is represented by a triangle with the name of the higher-level entity set above and the names of the lower-level entity sets below.
  - Specialization: The process of dividing an entity set into two or more sub-entity sets based on some distinguishing characteristics. It is represented by a triangle with the name of the lower-level entity sets above and the name of the higher-level entity set below.
  - Aggregation: The process of treating a relationship as an entity set for the purpose of participating in another relationship. It is represented by drawing a dashed rectangle around the relationship and the entity sets involved.

- ER model is useful for designing databases because it helps to:
  - Capture the requirements and constraints of the data in a clear and concise way.
  - Communicate the data design to the developers and users of the database.
  - Modularize the data design and facilitate normalization and optimization of the database.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Database Management System. Here are some notes on the topic of ER Model Concepts for Unit 1 - Introduction.

# ER Model Concepts

- The ER model is a conceptual data model that describes the structure and semantics of data in a database.
- The ER model consists of three basic concepts: entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified uniquely and has some properties. For example, a student, a course, a book, etc.
- An attribute is a property or characteristic of an entity that describes some aspect of it. For example, a student has a name, an ID, a major, etc.
- A relationship is an association or connection between two or more entities that expresses some meaningful dependency or interaction. For example, a student enrolls in a course, a course has a prerequisite, a book is written by an author, etc.
- The ER model can be represented graphically using an ER diagram, which shows the entities, attributes, and relationships using symbols and lines.
- The ER diagram has the following symbols:

  - A rectangle represents an entity type, which is a collection of entities that share the same attributes. For example, Student, Course, Book, etc.
  - An oval represents an attribute of an entity type, which is connected to the rectangle by a line. For example, Name, ID, Major, etc.
  - A diamond represents a relationship type, which is a collection of relationships that share the same meaning and structure. For example, Enrolls, Has, Written by, etc.
  - A line connects an entity type to a relationship type, indicating that the entities participate in the relationship. For example, Student - Enrolls - Course, Course - Has - Prerequisite, Book - Written by - Author, etc.
  - A double line indicates that the participation of an entity type in a relationship type is total, meaning that every entity in the entity type must participate in at least one relationship in the relationship type. For example, every student must enroll in at least one course, every course must have at least one prerequisite, etc.
  - A single line indicates that the participation of an entity type in a relationship type is partial, meaning that some entities in the entity type may not participate in any relationship in the relationship type. For example, some books may not be written by any author, some courses may not have any prerequisite, etc.
  - A thick line indicates that the cardinality of an entity type in a relationship type is one, meaning that each entity in the entity type can participate in at most one relationship in the relationship type. For example, each student can enroll in at most one course, each course can have at most one prerequisite, etc.
  - A thin line indicates that the cardinality of an entity type in a relationship type is many, meaning that each entity in the entity type can participate in more than one relationship in the relationship type. For example, each book can be written by more than one author, each course can enroll more than one student, etc.

- Here is an example of an ER diagram for a university database:

ER diagram for a university database

- The ER model can be converted into a relational model, which is a more formal and precise data model that describes the structure and constraints of data in a database using tables, columns, keys, and foreign keys.



# Notation for ER Diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw an ER diagram, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entities**: Entities are the basic objects or concepts in the database, such as customers, products, orders, etc. They are represented by rectangles with the entity name inside. For example:

entity

- **Attributes**: Attributes are the properties or characteristics of the entities, such as name, age, price, quantity, etc. They are represented by ovals with the attribute name inside, connected to the entity by a line. For example:

attribute

- **Relationships**: Relationships are the associations or interactions between the entities, such as buys, sells, owns, etc. They are represented by diamonds with the relationship name inside, connected to the entities by lines. For example:

relationship

- **Cardinality**: Cardinality is the number of occurrences or instances of one entity that can be related to another entity in a relationship. It can be one-to-one, one-to-many, many-to-one or many-to-many. It is represented by different symbols or notations depending on the modeling methodology. For example, in arrow notation, a single-headed arrow with an open circle on the line means zero or one, a single-headed arrow with a closed circle on the line means one and only one, a double-headed arrow means one or many, and a line without an arrow means many. For example:

cardinality

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. They can be primary keys, foreign keys, composite keys or candidate keys. They are represented by different symbols or notations depending on the modeling methodology. For example, in Chen notation, a primary key is underlined, a foreign key is dashed, a composite key is a combination of two or more attributes, and a candidate key is a potential primary key. For example:

key

- **Types**: Types are the data types or domains of the attributes, such as integer, string, date, etc. They are represented by different symbols or notations depending on the modeling methodology. For example, in Crow's foot notation, a type is shown as a small label next to the attribute name. For example:

type

These are some of the basic notations and symbols for ER diagrams. There are other notations and symbols that can be used to represent more complex or specific aspects of the database, such as generalization, specialization, aggregation, composition, etc. Different modeling methodologies may have different notations and symbols for the same concept, or different concepts for the same notation and symbol. Therefore, it is important to choose a consistent and appropriate notation and symbol for the ER diagram, and to document the meaning and usage of each notation and symbol.



# Mapping Constraints for the notes of the Unit 1 - Introduction in the subject of Database Management System

- Mapping constraints are rules that define how many entities can be associated with each other in a relationship set .
- Mapping constraints are also known as cardinality ratios or cardinalities.
- Mapping constraints are important for designing and validating the entity-relationship (ER) model of a database .
- Mapping constraints can be classified into four types based on the number of entities involved in a relationship set  :
  - One-to-one: Each entity in one entity set can be related to at most one entity in another entity set, and vice versa. For example, each employee can have one office, and each office can be occupied by one employee.
  - One-to-many: Each entity in one entity set can be related to many entities in another entity set, but each entity in the other entity set can be related to at most one entity in the first entity set. For example, each department can have many employees, but each employee can belong to one department.
  - Many-to-one: Each entity in one entity set can be related to at most one entity in another entity set, but each entity in the other entity set can be related to many entities in the first entity set. This is the inverse of one-to-many. For example, each employee can have one manager, but each manager can supervise many employees.
  - Many-to-many: Each entity in one entity set can be related to many entities in another entity set, and vice versa. For example, each student can enroll in many courses, and each course can have many students.
- Mapping constraints can be represented graphically using the ER diagram notation  . The cardinality ratio is indicated by placing a number (1 or N) or a symbol (| or <) near the end of the relationship line that connects the entity sets. For example, the following ER diagram shows a one-to-many relationship between department and employee:

ER diagram of one-to-many relationship

- Mapping constraints can also be enforced using primary and foreign key constraints in the relational database model . A primary key is a column or a set of columns that uniquely identifies each row in a table. A foreign key is a column or a set of columns that references the primary key of another table. A foreign key constraint ensures that the values in the foreign key column match the values in the referenced primary key column. For example, the following SQL statements create two tables, department and employee, with a one-to-many relationship enforced by a foreign key constraint:

```sql
CREATE TABLE department (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50) NOT NULL,
  dept_id INT NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES department (dept_id)
);
```

- Mapping constraints can also be specified using the minimum and maximum participation of each entity set in a relationship set  . The minimum participation indicates whether an entity must participate in at least one relationship instance or not. The maximum participation indicates whether an entity can participate in more than one relationship instance or not. The participation constraints are indicated by placing a double line (for total participation) or a single line (for partial participation) between the entity set and the relationship set. For example, the following ER diagram shows that each employee must belong to one and only one department, and each department can have zero or more employees:

ER diagram of participation constraints

- Mapping constraints are useful for ensuring the consistency and integrity of the data in a database. They also help to avoid redundancy and ambiguity in the data model  .



# Keys for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A database is a collection of related data that is organized and stored in a structured way.
- A database management system (DBMS) is a software system that allows users to create, manipulate, and access databases.
- A data model is a conceptual representation of the data and the relationships among them.
- A schema is a description of the structure and constraints of a database.
- A database instance is a snapshot of the data in a database at a given point in time.
- A data dictionary is a collection of metadata that describes the data elements, their properties, and their relationships in a database.
- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A foreign key is a column or a set of columns that references the primary key of another table, establishing a relationship between the two tables.
- A candidate key is a column or a set of columns that can serve as a primary key for a table.
- A superkey is a column or a set of columns that contains a candidate key for a table.
- A composite key is a key that consists of two or more columns.
- A surrogate key is a system-generated key that is used as a primary key for a table, instead of a natural key that is derived from the data.
- A relational database is a database that organizes data into tables, where each table has a fixed number of columns and a variable number of rows.
- A relational model is a data model that is based on the concept of mathematical relations, where each relation is a set of tuples (rows) with the same attributes (columns).
- A relational algebra is a set of operations that can be applied to relations to manipulate and query data.
- A relational calculus is a declarative language that can be used to express queries on relations, using logical predicates and quantifiers.
- A SQL (Structured Query Language) is a standard language that can be used to create, manipulate, and query relational databases.
- A query is a request for information from a database, expressed in a query language such as SQL.
- A query result is a relation that contains the data that satisfies the query.
- A constraint is a rule that specifies some conditions that the data in a database must satisfy.
- A domain constraint is a constraint that specifies the valid values for an attribute.
- A key constraint is a constraint that specifies the uniqueness of a key for a table.
- A referential integrity constraint is a constraint that ensures that a foreign key value in a table matches a primary key value in another table, or is null.
- An entity integrity constraint is a constraint that ensures that a primary key value in a table is not null.
- A functional dependency is a relationship between two sets of attributes, such that the values of one set determine the values of the other set.
- A normalization is a process of decomposing a relation into smaller relations that satisfy certain properties, such as eliminating redundancy and preserving dependencies.
- A normal form is a condition or a set of conditions that a relation must satisfy to be considered normalized.
- A first normal form (1NF) is a normal form that requires a relation to have no repeating groups or multivalued attributes.
- A second normal form (2NF) is a normal form that requires a relation to be in 1NF and have no partial dependencies, where a non-key attribute depends on only a part of the primary key.
- A third normal form (3NF) is a normal form that requires a relation to be in 2NF and have no transitive dependencies, where a non-key attribute depends on another non-key attribute.
- A Boyce-Codd normal form (BCNF) is a normal form that requires a relation to be in 3NF and have no non-trivial dependencies, where a non-key attribute depends on a proper subset of a candidate key.
- A fourth normal form (4NF) is a normal form that requires a relation to be in BCNF and have no multivalued dependencies, where an attribute depends on a set of attributes and not on another attribute.
- A fifth normal form (5NF) is a normal form that requires a relation to be in 4NF and have no join dependencies, where a relation cannot be decomposed into smaller relations without losing information.



# Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table.  
- A super key may have additional attributes that are not needed for unique identification.  
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table. 
- There can be more than one super key for a table, but only one candidate key.  
- A super key can also be NULL, unless the table has a primary key constraint. 
- A super key can be used to enforce referential integrity, which means that the values of a super key in one table must match the values of a corresponding super key in another table.



# Candidate Key

- A candidate key is a minimal set of attributes that can uniquely identify each tuple in a relation.
- A relation can have more than one candidate key, but each candidate key must be irreducible, meaning that no attribute can be removed from it without losing the uniqueness property.
- A candidate key can be a single attribute or a combination of attributes, depending on the relation schema and the functional dependencies among the attributes.
- A candidate key can be used to define a primary key, which is a special candidate key that is chosen by the database designer to identify the tuples in a relation.
- A candidate key that is not chosen as the primary key is called an alternate key.
- A candidate key can also be used to define a foreign key, which is an attribute or a set of attributes that references a primary key or a candidate key of another relation.
- A candidate key can be derived from the relation schema and the set of functional dependencies by applying the closure test, the minimal cover test, or the canonical cover test. These tests are based on the concept of attribute closure, which is the set of all attributes that are functionally determined by a given set of attributes.



# Primary Key

- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key must satisfy the following properties:
  - It must not contain null values. This is called the **not null** constraint.
  - It must have a unique value for each row. This is called the **unique** constraint.
  - It must be minimal, meaning that no subset of the columns can satisfy the uniqueness property. This is called the **irreducibility** property.
- A primary key can be either **simple** or **composite**. A simple primary key consists of a single column, while a composite primary key consists of two or more columns.
- A primary key can be either **natural** or **surrogate**. A natural primary key is based on a column or a set of columns that have a logical meaning in the domain of the table, such as a student ID or a product code. A surrogate primary key is based on a column or a set of columns that have no logical meaning in the domain of the table, such as a sequential number or a random string.
- A primary key serves two main purposes in a database:
  - It ensures the **integrity** of the data, by preventing duplicate rows and null values.
  - It enables the **referential** integrity of the data, by allowing other tables to reference the rows in the table using foreign keys.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some points on generalization for the notes of the Unit 1 - Introduction in the subject of Database Management System.

# Generalization

- Generalization is a process of extracting common characteristics from two or more classes and combining them into a generalized superclass.
- Generalization is also known as abstraction or inheritance, as the generalized superclass inherits the attributes and behaviors of the subclasses.
- Generalization helps to reduce redundancy and complexity in the database schema by avoiding the repetition of the same attributes and behaviors in multiple classes.
- Generalization can be represented by a triangle with a line connecting the superclass and the subclasses. The superclass is placed at the top of the triangle and the subclasses are placed at the bottom.
- An example of generalization is the class Person, which can be generalized from the classes Student and Teacher. The class Person has the common attributes and behaviors of Student and Teacher, such as name, age, address, and phone number. The class Student has the specific attributes and behaviors of a student, such as roll number, course, and marks. The class Teacher has the specific attributes and behaviors of a teacher, such as salary, department, and subject.



# Aggregation

- Aggregation is a process of combining two or more entities to form a more meaningful new entity.
- Aggregation is often used to calculate statistics or to summarize data in a more meaningful way.
- Aggregation can be done using SQL aggregate functions such as SUM, COUNT, AVG, MIN, and MAX.
- Aggregation can also be explained using the entity-relationship model (ER model), which is a conceptual diagram that represents the structure of a database and its components.
- Aggregation is needed when the entities are not significant enough to provide meaningful information on their own, or when the entity-model relationship is inapplicable or ambiguous.
- Aggregation can help to reduce the complexity and redundancy of the database design, and to improve the performance and efficiency of the queries.
- Aggregation can also be used to ingest raw data from various databases or data sources into a centralized database, and then combine them to form aggregate values.
- Aggregation can be applied across all industries and domains for various purposes, such as forecasting, analysis, reporting, and decision making.



# Reduction of an ER Diagram to Tables

An ER diagram is a graphical representation of the entities and relationships in a database. It shows the structure and constraints of the data. A table is a collection of rows and columns that store the data in a relational database. The process of converting an ER diagram to tables is called reduction or mapping. It involves the following steps:

- Convert all the entities in the diagram to tables. All the entities represented in the rectangular box in the ER diagram become independent tables in the database. Each table should have a primary key that uniquely identifies each row. The attributes of the entity become the columns of the table. For example, in the following ER diagram, the entities STUDENT, COURSE, and SUBJECT become tables with the same name and attributes.

ER diagram example

- Convert all the relationships in the diagram to tables or foreign keys. All the relationships represented by the diamonds in the ER diagram can be mapped to tables or foreign keys depending on the cardinality and participation of the entities involved. There are three types of relationships: one-to-one, one-to-many, and many-to-many.

  - For a one-to-one relationship, choose one of the entities and add the primary key of the other entity as a foreign key in its table. The foreign key references the primary key of the related table. For example, in the following ER diagram, the relationship between STUDENT and LECTURE is one-to-one. We can choose STUDENT as the entity and add the primary key of LECTURE (Lecture_ID) as a foreign key in the STUDENT table.

  One-to-one relationship example

  - For a one-to-many relationship, choose the entity on the many side and add the primary key of the entity on the one side as a foreign key in its table. The foreign key references the primary key of the related table. For example, in the following ER diagram, the relationship between COURSE and SUBJECT is one-to-many. We can choose SUBJECT as the entity on the many side and add the primary key of COURSE (Course_ID) as a foreign key in the SUBJECT table.

  One-to-many relationship example

  - For a many-to-many relationship, create a new table for the relationship and include the primary keys of both the entities as foreign keys in the new table. The combination of the foreign keys becomes the primary key of the new table. The new table may also have additional attributes that describe the relationship. For example, in the following ER diagram, the relationship between STUDENT and COURSE is many-to-many. We can create a new table for the relationship called ENROLLMENT and include the primary keys of STUDENT (Student_ID) and COURSE (Course_ID) as foreign keys in the ENROLLMENT table. The combination of Student_ID and Course_ID becomes the primary key of the ENROLLMENT table. The new table may also have an attribute called Grade that describes the grade of the student in the course.

  Many-to-many relationship example

- Convert all the weak entities in the diagram to tables. A weak entity is an entity that depends on another entity for its existence and identification. It is represented by a double-lined rectangle in the ER diagram. A weak entity has a partial key that distinguishes it from other entities of the same type, but it is not enough to identify it uniquely. A weak entity is associated with a strong entity through an identifying relationship, which is represented by a double-lined diamond in the ER diagram. The strong entity has a primary key that identifies it uniquely. To convert a weak entity to a table, follow these steps:

  - Create a separate table for the weak entity with the same name as the entity.
  - Include all the attributes of the weak entity as columns in the table, including the partial key.
  - Include the primary key of the strong entity as a foreign key in the weak entity table. The foreign key references the primary key of the related table.
  - Declare the combination of the foreign key and the partial key as the primary key of the weak entity table. This ensures that the weak entity is identified uniquely by



# Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts in addition to the ER model concepts :

- Subclasses and superclasses: A subclass is a subset of entities of a superclass that have some additional attributes or relationships. A superclass is a set of entities that share some common attributes or relationships. For example, a student can be a subclass of a person, and a person can be a superclass of a student.
- Specialization and generalization: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics. Generalization is the process of defining a superclass from a set of subclasses by identifying their common features. For example, a person can be specialized into student, employee, and customer based on their roles.
- Category or union type: A category or union type is a subclass that represents a collection of entities from different superclasses that share some common attributes or relationships. For example, a part-time employee can be a category of student and employee.
- Aggregation: Aggregation is the process of grouping a set of entities and relationships into a single entity or relationship. For example, a project can be an aggregation of a set of tasks and employees.

The extended ER model can be represented graphically using the following symbols:

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type or between an attribute and an entity type
- A double line for a total participation constraint
- A dashed line for a partial participation constraint
- A double ellipse for a multivalued attribute
- A dashed ellipse for a derived attribute
- A triangle for a superclass or subclass
- A line with a circle for a disjoint constraint
- A line with a double circle for an overlapping constraint
- A line with a d for a specialization or generalization
- A line with a u for a category or union type
- A dashed rectangle for an aggregation

Here is an example of an extended ER diagram for a university database:

EER diagram



# Relationship of Higher Degree

- A relationship of higher degree is a relationship that involves more than two entities.
- For example, a ternary relationship is a relationship of degree three, which relates three entities.
- A relationship of higher degree can be represented by a diamond-shaped symbol with the name of the relationship and the degree as a subscript.
- The participating entities are connected to the relationship symbol by lines, and the cardinality ratios are indicated by numbers or symbols on the lines.
- For example, the following diagram shows a ternary relationship called **Supplies**, which relates three entities: **Supplier**, **Part**, and **Project**.

Ternary relationship diagram

- A relationship of higher degree can also be represented by a table, where each row corresponds to an instance of the relationship, and each column corresponds to an attribute of the relationship or an entity involved in the relationship.
- For example, the following table shows a possible instance of the **Supplies** relationship, where each row indicates that a supplier supplies a part to a project with a certain quantity and price.

| Supplier | Part | Project | Quantity | Price |
|----------|------|---------|----------|-------|
| S1       | P1   | A       | 100      | 10    |
| S1       | P2   | B       | 50       | 15    |
| S2       | P3   | A       | 200      | 20    |
| S2       | P4   | C       | 150      | 25    |
| S3       | P5   | B       | 75       | 30    |
| S3       | P6   | C       | 100      | 35    |

- A relationship of higher degree can be converted into a set of binary relationships by introducing a new entity that represents the relationship, and creating a one-to-many relationship between the new entity and each of the original entities.
- For example, the **Supplies** relationship can be converted into a set of binary relationships by introducing a new entity called **Supply**, which has a composite key consisting of the attributes of the original entities, and creating a one-to-many relationship between **Supply** and each of **Supplier**, **Part**, and **Project**.

Binary relationship diagram

- The advantage of converting a relationship of higher degree into a set of binary relationships is that it simplifies the data model and avoids the ambiguity of the cardinality ratios of the original relationship.
- The disadvantage of converting a relationship of higher degree into a set of binary relationships is that it introduces redundancy and complexity in the data, and may require additional constraints to ensure the consistency and integrity of the data.



# Unit 2 - Relational Data Model and Language

- Relational Data Model and Language is a way of representing and manipulating data in a relational database.
- A relational database is a type of database that stores data in the form of relations (tables), where each row represents a tuple (record) and each column represents an attribute (field).
- A relational database may use SQL (Structured Query Language) as its language, but SQL is not the same as the relational model. SQL is a set of commands and syntax that can be used to query, manipulate, and define data in a relational database.
- The relational model has some basic concepts and principles, such as:

  - Entity: An entity is a real-world object or concept that can be identified and distinguished from others. For example, a student, a course, or a book are entities.
  - Attribute: An attribute is a property or characteristic of an entity that describes some aspect of it. For example, name, age, or title are attributes of a student, a course, or a book, respectively.
  - Domain: A domain is a set of possible values for an attribute. For example, the domain of the name attribute of a student entity could be a set of strings, such as "Alice", "Bob", or "Charlie".
  - Relation: A relation is a set of tuples that share the same attributes. A relation can be represented as a table, where each row is a tuple and each column is an attribute. For example, a relation called Student could have the attributes name, age, and major, and store the tuples ("Alice", 19, "Math"), ("Bob", 20, "CS"), and ("Charlie", 18, "Biology").
  - Key: A key is an attribute or a set of attributes that can uniquely identify a tuple in a relation. For example, the name attribute could be a key for the Student relation, as no two students have the same name. A key can also be a combination of attributes, such as name and age, if they are sufficient to distinguish a tuple. A key that consists of a single attribute is called a simple key, and a key that consists of more than one attribute is called a composite key.
  - Primary Key: A primary key is a key that is chosen to be the main identifier of a tuple in a relation. A relation can have only one primary key, and it cannot have null values. For example, the name attribute could be the primary key for the Student relation. A primary key is usually underlined in a table to indicate its importance.
  - Foreign Key: A foreign key is an attribute or a set of attributes in a relation that refers to the primary key of another relation. A foreign key establishes a link or a relationship between two relations. For example, the major attribute in the Student relation could be a foreign key that references the name attribute of another relation called Department, which stores the information about different academic departments. A foreign key is usually italicized in a table to indicate its reference.
  - Schema: A schema is a description or a definition of the structure and constraints of a relation. A schema specifies the name, attributes, domains, keys, and foreign keys of a relation. For example, the schema of the Student relation could be written as:

    Student(name, age, major)

    name is the primary key

    major references Department.name

  - Instance: An instance is a snapshot or a state of a relation at a given point in time. An instance contains the actual data or values that are stored in a relation. For example, the instance of the Student relation could be the table that shows the tuples ("Alice", 19, "Math"), ("Bob", 20, "CS"), and ("Charlie", 18, "Biology").
  - Degree: The degree of a relation is the number of attributes it has. For example, the degree of the Student relation is 3, as it has three attributes: name, age, and major.
  - Cardinality: The cardinality of a relation is the number of tuples it has. For example, the cardinality of the Student relation is 3, as it has three tuples: ("Alice", 19, "Math"), ("Bob", 20, "CS"), and ("Charlie", 18, "Biology").
  - Relational Algebra: Relational algebra is a set of operations that can be applied to relations to manipulate and query data. Relational algebra operations can be classified into two categories: unary operations and binary operations. Unary operations take one relation as input and produce one relation



# Relational Data Model Concepts

The relational data model is a widely used data model for storing and processing data in a database. It is based on the concept of relations, which are logical structures that represent data as a collection of rows and columns. Each row in a relation is called a tuple, and each column is called an attribute. A relation has a name and a set of attributes that define its schema. The schema of a relation is also called its degree, and the number of tuples in a relation is called its cardinality.

Some of the main concepts of the relational data model are:

- **Primary key**: A primary key is an attribute or a combination of attributes that uniquely identifies each tuple in a relation. A primary key cannot have null values or duplicate values. A relation can have only one primary key, which is also called the primary key constraint.
- **Foreign key**: A foreign key is an attribute or a combination of attributes that references the primary key of another relation. A foreign key establishes a relationship between two relations, which is also called a referential integrity constraint. A foreign key can have null values or duplicate values, but it must match the values of the referenced primary key or be null.
- **Domain**: A domain is a set of possible values for an attribute. A domain defines the data type, format, and constraints of an attribute. For example, a domain for a student ID attribute could be a set of integers between 1000 and 9999.
- **Relation instance**: A relation instance is a snapshot of the data in a relation at a given point in time. A relation instance is also called a relation state or a relation value. A relation instance can change over time as tuples are inserted, deleted, or updated.
- **Relational algebra**: Relational algebra is a set of operations that can be applied to relations to manipulate and query data. Relational algebra operations include selection, projection, union, intersection, difference, product, join, division, and aggregation. Relational algebra operations can be combined to form complex expressions that specify the desired data. Relational algebra is the theoretical foundation of the structured query language (SQL), which is the most common language for accessing and manipulating data in relational databases.



# Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when data is inserted, updated, or deleted).
- Integrity constraints can be classified into four types: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

## Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- Domain constraints ensure that the data stored in a relation is of the correct type and format.

## Key Constraints

- Key constraints specify the uniqueness of tuples in a relation.
- Key constraints can be enforced by defining one or more attributes of a relation as the primary key or candidate keys.
- Primary key is a minimal set of attributes that uniquely identifies each tuple in a relation.
- Candidate keys are alternative sets of attributes that can also uniquely identify each tuple in a relation.
- Key constraints ensure that there are no duplicate tuples in a relation.

## Entity Integrity Constraints

- Entity integrity constraints ensure that the primary key of a relation does not contain null values.
- Entity integrity constraints can be enforced by declaring the primary key attributes as not null.
- Entity integrity constraints ensure that each tuple in a relation can be uniquely identified by its primary key.

## Referential Integrity Constraints

- Referential integrity constraints ensure that the foreign key values of a relation are consistent with the primary key values of the referenced relation.
- Referential integrity constraints can be enforced by declaring the foreign key attributes as references to the primary key attributes of another relation.
- Referential integrity constraints ensure that the relationships between relations are valid and consistent.



# Entity Integrity

- Entity integrity is a constraint that ensures that every row in a table has a unique and non-null identifier.
- The identifier is usually a primary key, which is a column or a set of columns that can uniquely identify a row in a table.
- Entity integrity prevents duplicate rows and missing values in the primary key, which could compromise the accuracy and consistency of the data.
- Entity integrity is enforced by the database management system (DBMS) by rejecting any insertion, update, or deletion that violates the constraint.
- Entity integrity is one of the rules of the relational data model, which is a widely used model for organizing and manipulating data in a database.



# Referential Integrity

- Referential integrity is a property of data stating that all its references are valid .
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist .
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key.
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table.
- Referential integrity ensures that relationships between tables remain consistent .
- Referential integrity prevents the following problems:
  - Orphan records: records that have a foreign key value that does not match any primary key value in the parent table.
  - Inconsistent data: records that have different values for the same attribute in different tables.
  - Invalid operations: operations that violate the rules of referential integrity, such as deleting a parent record without deleting the related child records, or inserting a child record without a corresponding parent record.
- Referential integrity can be enforced by the following methods:
  - Database constraints: rules that are defined at the table level to specify the conditions for referential integrity, such as primary key, foreign key, unique, not null, and check constraints.
  - Database triggers: procedures that are executed automatically when a certain event occurs, such as insert, update, or delete, to perform actions that maintain referential integrity, such as cascading delete or update.
  - Application logic: code that is written in the application layer to validate the data before sending it to the database, or to handle the errors that occur when referential integrity is violated.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of key constraints for the relational data model and language in the subject of database management system.

# Key Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple in a relation.
- A key constraint is a rule that specifies that no two tuples in a relation can have the same values for the key attributes.
- A key constraint ensures the integrity and consistency of the data in a relation.
- There are different types of keys and key constraints in the relational data model and language, such as:

  - Superkey: A superkey is a set of attributes that contains a key. A superkey may have extra attributes that are not necessary for uniqueness. For example, in a relation STUDENT with attributes ID, Name, and Major, {ID}, {ID, Name}, and {ID, Name, Major} are all superkeys, but only {ID} is a key.
  - Candidate key: A candidate key is a minimal superkey, that is, a superkey that does not contain any extra attributes. A relation may have more than one candidate key. For example, in a relation EMPLOYEE with attributes SSN, Name, and Phone, both {SSN} and {Phone} are candidate keys.
  - Primary key: A primary key is a candidate key that is chosen by the database designer to be the main identifier of the tuples in a relation. A relation can have only one primary key. The primary key is usually underlined in the schema. For example, in a relation EMPLOYEE, SSN can be chosen as the primary key.
  - Foreign key: A foreign key is a set of attributes in a relation that refers to the primary key of another relation. A foreign key establishes a relationship between two relations. A foreign key constraint is a rule that specifies that the values of the foreign key must either match the values of the primary key in the referenced relation, or be null. For example, in a relation DEPARTMENT with attributes Dname, Dnumber, and Mgr_ssn, Mgr_ssn is a foreign key that refers to the primary key SSN of the relation EMPLOYEE. A foreign key constraint ensures that every department has a valid manager, or no manager at all.



# Domain Constraints for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Domain constraints are the rules that specify the allowed values for each attribute or column in a relation or table .
- Domain constraints are a type of integrity constraint that ensures the data quality and accuracy in a relational database .
- Domain constraints can be defined by the data type, format, range, or set of values for each attribute or column .
- Domain constraints can be enforced by the database management system (DBMS) or by the application program that manipulates the data .
- Domain constraints are important because they prevent the insertion of invalid or inconsistent data into the database, and they help to maintain the semantic meaning of the data .

Some examples of domain constraints are:

- The attribute `Student_ID` in the relation `Student` must be an integer value between 1000 and 9999.
- The attribute `Email` in the relation `Customer` must be a string value that follows the format of `name@domain.com`.
- The attribute `Gender` in the relation `Employee` must be a character value that belongs to the set of values `{'M', 'F', 'O'}`.



# Relational Algebra

Relational algebra is a theory that uses algebraic structures for modeling data, and defining queries on it with a well founded semantics. The main application of relational algebra is to provide a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.

Relational algebra is considered as a procedural query language, where the user tells the system to carry out a set of operations to obtain the desired results. Relational algebra operations are designed to do the most common things that we need to do with relations in a database.

Some of the basic relational algebra operations are:

- **SELECT** (σ): The SELECT operation is used for selecting a subset of the tuples according to a given selection condition . For example, σ<sub>age > 20</sub>(Student) selects all the tuples from the Student relation where the age attribute is greater than 20.
- **PROJECT** (π): The PROJECT operation is used for selecting a subset of the attributes of a relation . For example, π<sub>name, course</sub>(Student) selects only the name and course attributes from the Student relation.
- **UNION** (∪): The UNION operation is used for combining two relations that have the same set of attributes . For example, Student ∪ Teacher returns a relation that contains all the tuples from both Student and Teacher relations.
- **INTERSECTION** (∩): The INTERSECTION operation is used for selecting the common tuples from two relations that have the same set of attributes . For example, Student ∩ Teacher returns a relation that contains only the tuples that are present in both Student and Teacher relations.
- **DIFFERENCE** (-): The DIFFERENCE operation is used for selecting the tuples that are present in one relation but not in another relation that have the same set of attributes . For example, Student - Teacher returns a relation that contains only the tuples that are present in Student relation but not in Teacher relation.
- **CARTESIAN PRODUCT** (×): The CARTESIAN PRODUCT operation is used for combining every tuple of one relation with every tuple of another relation . For example, Student × Course returns a relation that contains all the possible combinations of tuples from Student and Course relations.
- **JOIN** (⋈): The JOIN operation is used for combining two relations based on a common attribute or a join condition . For example, Student ⋈<sub>Student.course = Course.id</sub> Course returns a relation that contains the tuples from Student and Course relations that have the same value for the course and id attributes, respectively.
- **DIVISION** (÷): The DIVISION operation is used for selecting the tuples from one relation that are associated with all the tuples of another relation . For example, Student ÷ Course returns a relation that contains the tuples from Student relation that have taken all the courses in the Course relation.

There are also some additional relational algebra operations that can be derived from the basic ones, such as:

- **RENAME** (ρ): The RENAME operation is used for changing the name of a relation or an attribute . For example, ρ<sub>Enrolled(name, course)</sub>(Student) changes the name of the Student relation to Enrolled, and the attributes to name and course.
- **SET DIFFERENCE** (∖): The SET DIFFERENCE operation is used for selecting the tuples that are present in one relation but not in another relation that have the same set of attributes . It is equivalent to the DIFFERENCE operation. For example, Student ∖ Teacher is the same as Student - Teacher.
- **NATURAL JOIN** (⋈): The NATURAL JOIN operation is used for combining two relations based on the common attributes . It is equivalent to the JOIN operation with an implicit join condition. For example, Student ⋈ Course is the same as Student ⋈<sub>Student.course = Course.id</sub> Course.
- **SEMI-JOIN** (⋉): The SEMI-JOIN operation is used for selecting the tuples from one relation that have a matching tuple in another relation [^3^



# Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a **non-procedural** query language that describes **what** data to retrieve from a relational database, without specifying **how** to do it  .
- Relational calculus is based on **mathematical predicate calculus** and uses **logical expressions** to specify the conditions for selecting tuples (rows) from relations (tables)  .
- Relational calculus is an **integral part** of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- There are two types of relational calculus: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**   .
- Tuple relational calculus uses **tuple variables** that range over the tuples of a relation and checks every tuple with a **predicate expression** that evaluates to true or false  .
- Domain relational calculus uses **domain variables** that range over the values of the attributes of a relation and constructs tuples by applying a **predicate formula** over the domain variables  .
- Both types of relational calculus are **equivalent** in expressive power, meaning that they can express the same set of queries  .
- Relational calculus is a **declarative** language that focuses on the **result** of the query, rather than the **steps** to obtain it   .
- Relational calculus is also a **safe** language, meaning that it always returns a **finite** set of tuples as the answer to a query  .
- Relational calculus can be used to express **complex** queries that involve **nested** subqueries, **aggregation** functions, and **set** operations   .



# Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a non-procedural query language for relational databases  .
- Non-procedural means that the query does not specify how to retrieve the data, but only what data to retrieve  .
- Tuple and domain calculus are based on mathematical logic and set theory  .
- Tuple and domain calculus are equivalent in expressive power, meaning that any query that can be expressed in one form can also be expressed in the other form.

## Tuple Relational Calculus (TRC)

- Tuple relational calculus uses tuple variables that range over the tuples of a relation   .
- A tuple variable is denoted by a lowercase letter, such as t, s, or x  .
- A tuple relational calculus query has the form {t | P(t)}, where t is a tuple variable and P(t) is a predicate that involves t and possibly other tuple variables    .
- The query returns the set of all tuples t that satisfy the predicate P(t)    .
- The predicate P(t) can use logical operators (such as AND, OR, NOT), relational operators (such as =, <, >), and quantifiers (such as ∃ for exists and ∀ for for all)    .
- The predicate P(t) can also refer to the attributes of the tuple variable t by using the dot notation, such as t.name or t.salary    .
- Example: The query {t | t ∈ Employee ∧ t.salary > 5000} returns the set of all tuples t from the Employee relation that have a salary greater than 5000.

## Domain Relational Calculus (DRC)

- Domain relational calculus uses domain variables that range over the values of the domains of the attributes of a relation   .
- A domain variable is denoted by an uppercase letter, such as A, B, or X   .
- A domain relational calculus query has the form {<A1, A2, ..., An> | P(A1, A2, ..., An)}, where A1, A2, ..., An are domain variables and P(A1, A2, ..., An) is a predicate that involves the domain variables and possibly constants   .
- The query returns the set of all tuples <A1, A2, ..., An> that satisfy the predicate P(A1, A2, ..., An)   .
- The predicate P(A1, A2, ..., An) can use logical operators (such as AND, OR, NOT), relational operators (such as =, <, >), and quantifiers (such as ∃ for exists and ∀ for for all)   .
- The predicate P(A1, A2, ..., An) can also refer to the relations by using the membership operator ∈, such as A ∈ Employee or <A, B> ∈ Department   .
- Example: The query {<A, B> | A ∈ Employee ∧ B ∈ Department ∧ A.deptno = B.deptno} returns the set of all pairs of employee and department names that belong to the same department.



# Introduction to SQL

SQL is a computer language for storing, manipulating, and retrieving data in a relational database. SQL allows you to create, modify and query databases. SQL is a standard language that is used by most relational databases. SQL is used to access and manipulate data stored in tables.

Some of the main features of SQL are:

- SQL is a declarative language, which means you specify what you want to do, not how to do it.
- SQL is a structured language, which means it has a fixed syntax and keywords that must be followed.
- SQL is a relational language, which means it operates on data that is organized in tables, which consist of rows and columns.
- SQL is a versatile language, which means it can perform various operations on data, such as creating, updating, deleting, sorting, filtering, grouping, aggregating, joining, etc.

Some of the main components of SQL are:

- Data Definition Language (DDL), which is used to create, alter, and drop database objects, such as tables, views, indexes, etc.
- Data Manipulation Language (DML), which is used to insert, update, and delete data in tables.
- Data Query Language (DQL), which is used to select and retrieve data from tables.
- Data Control Language (DCL), which is used to grant and revoke permissions and roles to users and groups.
- Transaction Control Language (TCL), which is used to manage transactions, such as commit, rollback, savepoint, etc.

Some of the main advantages of SQL are:

- SQL is a widely used and standardized language that is supported by most database systems.
- SQL is a high-level language that is easy to learn and use.
- SQL is a powerful language that can handle complex queries and operations on large amounts of data.
- SQL is a portable language that can run on different platforms and devices.

Some of the main disadvantages of SQL are:

- SQL is a limited language that cannot perform all the tasks that a general-purpose programming language can, such as looping, conditional statements, etc.
- SQL is a static language that cannot adapt to changing data and requirements.
- SQL is a vulnerable language that can be exploited by malicious users and hackers, such as SQL injection attacks.



# Characteristics of SQL

SQL is a computer language used to store, manipulate, and retrieve data from a relational database. SQL has some features and characteristics that make it suitable for working with relational data. Some of the characteristics of SQL are:

- **Easy to learn**: SQL is an extremely practical and user-friendly language. Even if you have no prior experience with programming, you can learn the basic syntax and commands of SQL in a short time. SQL is based on natural language and uses simple keywords and clauses to express queries and operations.
- **Wide variety of commands**: SQL supports a wide variety of commands such as DDL (Data Definition Language) commands, DML (Data Manipulation Language) commands, DCL (Data Control Language) commands, and TCL (Transaction Control Language) commands. These commands allow you to create, modify, delete, query, and control the data and the database objects.
- **Stored procedures**: A stored procedure is a set of SQL statements that can be stored in the database and executed as a single unit. Stored procedures can improve the performance, security, and maintainability of the database applications. Stored procedures can also accept parameters and return values, making them more flexible and reusable.
- **High performance**: SQL provides high-performance programming capability for highly transactional, heavy workload, and high usage database systems. SQL programming gives various ways to describe the data more analytically, such as using aggregate functions, subqueries, joins, and views. SQL also supports indexing, partitioning, and clustering techniques to optimize the data access and storage.
- **Portability**: SQL is a standard language that is supported by most of the relational database management systems, such as Oracle, MySQL, SQL Server, PostgreSQL, and SQLite. SQL can also run on different platforms, such as Windows, Linux, and Mac OS. This makes SQL portable and compatible across different systems and applications.



# Advantage of SQL

SQL is a widely used language for managing and manipulating data in relational database systems. SQL has many advantages over other database management languages, such as:

- **Faster and efficient query processing.** SQL can process large amounts of data in a very short time, using simple and concise commands. SQL also supports various functions and operators that can perform complex calculations and transformations on the data.  
- **Standardized language.** SQL is a standardized language that follows the ANSI (American National Standards Institute) and ISO (International Organization for Standardization) standards. This means that SQL is compatible with different database systems and platforms, and can be easily learned and used by different users. 
- **No coding skills required.** SQL does not require extensive programming skills or knowledge to use. SQL commands are based on common English phrases, such as SELECT, INSERT, UPDATE, DELETE, etc. SQL also has a simple syntax and structure that makes it easy to write and read. 
- **Integration with other languages and tools.** SQL can be integrated with various programming languages, such as Java, Python, C#, etc., to perform more advanced tasks and operations on the data. SQL can also be used with various tools and applications, such as Excel, Power BI, Tableau, etc., to visualize and analyze the data. 
- **Data security and integrity.** SQL can enforce data security and integrity by using various features, such as constraints, triggers, views, roles, permissions, etc. These features can prevent unauthorized access, modification, or deletion of the data, and ensure that the data is consistent and accurate.



# SQL Data Types and Literals

## SQL Data Types
- SQL data types are used to represent the nature of the data that can be stored in the database table .
- Every field or column in a table is given a data type when a table is defined .
- SQL data types can be categorized into the following groups:
  - Numeric: for storing numbers, such as `INT`, `FLOAT`, `DECIMAL`, etc.
  - Character: for storing text, such as `CHAR`, `VARCHAR`, `TEXT`, etc.
  - Date and time: for storing date and time values, such as `DATE`, `TIME`, `DATETIME`, etc.
  - Binary: for storing binary data, such as `BINARY`, `VARBINARY`, `IMAGE`, etc.
  - Other: for storing special types of data, such as `BOOLEAN`, `XML`, `JSON`, etc.
- Different database systems may support different data types or have different names for the same data type.
- For example, SQL Server supports a data type called `sql_variant` that can store up to 8,000 bytes of data of various data types.
- SQL data types are important for ensuring data integrity, performance, and compatibility.

## SQL Literals
- SQL literals are constants that represent fixed values in SQL statements .
- SQL literals can be used in expressions, conditions, assignments, or as arguments to functions .
- There are four kinds of literal values supported in SQL :
  - Character string: for representing text values, enclosed in single quotes, such as `'Hello'`, `'SQL'`, etc.
  - Bit string: for representing binary values, prefixed with `B` or `0b`, such as `B'1010'`, `0b1100`, etc.
  - Exact numeric: for representing integer or decimal values, such as `42`, `3.14`, etc.
  - Approximate numeric: for representing floating-point values, using scientific notation, such as `1.23E4`, `6.02E-23`, etc.
- SQL literals can also be modified by collation, which specifies the rules for sorting and comparing character data.
- For example, `'SQL' COLLATE Latin1_General_CS_AS` is a character string literal with a case-sensitive and accent-sensitive collation.



# Types of SQL Commands

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL commands are divided into five broad categories based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of database objects such as tables, views, indexes, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc.
  - ALTER: This command is used to modify the structure or properties of an existing database object, such as adding, dropping, or renaming columns, constraints, etc.
  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc.
  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, etc.
  - TRUNCATE: This command is used to delete all the data from a table, but not the table structure.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - INSERT: This command is used to insert new data into a table.
  - UPDATE: This command is used to modify the existing data in a table.
  - DELETE: This command is used to delete the existing data from a table.
  - SELECT: This command is used to query data from one or more tables.

- **Data Query Language (DQL)**: This is a subset of DML commands that are used to query data from database tables. The most common DQL command is SELECT, which can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, etc. to filter, aggregate, sort, or limit the data.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of database users and roles. Some examples of DCL commands are:

  - GRANT: This command is used to grant privileges or permissions to a user or role to perform certain actions on database objects, such as SELECT, INSERT, UPDATE, DELETE, etc.
  - REVOKE: This command is used to revoke or withdraw the privileges or permissions that were previously granted to a user or role.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in a database, which are a set of logical operations that are performed as a single unit. Some examples of TCL commands are:

  - BEGIN: This command is used to start a new transaction.
  - COMMIT: This command is used to save the changes made by a transaction and end the transaction.
  - ROLLBACK: This command is used to undo the changes made by a transaction and end the transaction.
  - SAVEPOINT: This command is used to create a point in a transaction that can be used to rollback to in case of an error.



Hello, I am Sydney, your AI assistant. I can help you with your study material on SQL operators and their procedure. Here is a summary of the topic:

# SQL Operators and Their Procedure

- SQL operators are symbols or keywords that are used to perform various operations on data in a relational database.
- SQL operators can be classified into four categories: arithmetic, comparison, logical, and set operators.
- Arithmetic operators are used to perform mathematical calculations on numeric values or expressions. They include `+`, `-`, `*`, `/`, and `%` (modulo).
- Comparison operators are used to compare two values or expressions and return a boolean value (`TRUE`, `FALSE`, or `NULL`). They include `=`, `<>` (not equal), `<`, `>`, `<=`, `>=`, `BETWEEN`, `IN`, `LIKE`, and `IS NULL`.
- Logical operators are used to combine two or more boolean values or expressions and return a boolean value. They include `AND`, `OR`, `NOT`, and `XOR`.
- Set operators are used to combine two or more result sets from different queries and return a single result set. They include `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT` (or `MINUS`).

- The procedure for using SQL operators is to follow the syntax and rules of the SQL language and the specific database system. Some general rules are:

  - SQL operators are case-insensitive, but some database systems may require uppercase or lowercase keywords.
  - SQL operators follow a certain order of precedence, which determines the order in which they are evaluated. The order of precedence is:

    - Parentheses `()`
    - Arithmetic operators `*`, `/`, `%`, `+`, `-`
    - Comparison operators `=`, `<>`, `<`, `>`, `<=`, `>=`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`
    - NOT operator `NOT`
    - AND operator `AND`
    - OR operator `OR`
    - Set operators `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`

  - SQL operators can be used in various clauses of a SQL statement, such as `SELECT`, `WHERE`, `HAVING`, `GROUP BY`, `ORDER BY`, and `JOIN`.
  - SQL operators can be used with different data types, such as numeric, string, date, and boolean. However, some operators may require implicit or explicit type conversion to avoid errors or unexpected results. For example, the `+` operator can be used to add two numeric values or to concatenate two strings, but not to mix them.



# Tables for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A **table** is a collection of data organized in rows and columns.
- A table has a **name** that identifies it uniquely in a database.
- A table has a **schema** that defines the structure and properties of the data in the table.
- A table schema consists of a list of **attributes** (or columns) and their **data types** (such as integer, string, date, etc.).
- A table schema also specifies **constraints** that restrict the values or combinations of values that can be stored in the table.
- Some common types of constraints are:
  - **Primary key**: a set of attributes that uniquely identifies each row in the table.
  - **Foreign key**: a set of attributes that references another table and establishes a relationship between the tables.
  - **Unique**: a constraint that ensures that no two rows in the table have the same values for a set of attributes.
  - **Not null**: a constraint that prevents null values from being stored in an attribute.
  - **Check**: a constraint that enforces a condition on the values of an attribute or a set of attributes.
- A **row** (or tuple) in a table represents a single record or entity in the database.
- A **column** (or attribute) in a table represents a property or characteristic of the entity.
- A **value** in a table is the data stored in a cell at the intersection of a row and a column.
- A **relational data model** is a data model that represents data as tables and defines operations to manipulate and query the data.
- A **relational database** is a database that follows the relational data model and stores data in tables.
- A **relational database management system (RDBMS)** is a software system that provides tools and functions to create, maintain, and access relational databases.
- A **relational algebra** is a set of operations that can be applied to tables or the results of other operations to produce new tables.
- Some common relational algebra operations are:
  - **Selection**: an operation that selects a subset of rows from a table that satisfy a given condition.
  - **Projection**: an operation that selects a subset of columns from a table and eliminates duplicates.
  - **Union**: an operation that combines two tables with the same schema and eliminates duplicates.
  - **Intersection**: an operation that returns the common rows between two tables with the same schema.
  - **Difference**: an operation that returns the rows in one table that are not in another table with the same schema.
  - **Cartesian product**: an operation that combines every row of one table with every row of another table and produces a new table with the concatenated schema.
  - **Join**: an operation that combines two tables based on a common attribute or a join condition and produces a new table with the concatenated schema.
  - **Division**: an operation that returns the rows in one table that are associated with all the rows in another table and produces a new table with the reduced schema.
- A **relational calculus** is a declarative language that allows users to specify what data they want from the database without specifying how to get it.
- Some common types of relational calculus are:
  - **Tuple relational calculus**: a language that uses variables to represent tuples and defines formulas to specify the conditions that the tuples must satisfy.
  - **Domain relational calculus**: a language that uses variables to represent values in the domains of the attributes and defines formulas to specify the conditions that the values must satisfy.
- A **structured query language (SQL)** is a standard language that allows users to create, manipulate, and query relational databases using a combination of relational algebra and relational calculus.
- Some common SQL commands are:
  - **CREATE TABLE**: a command that creates a new table in the database and defines its schema and constraints.
  - **DROP TABLE**: a command that deletes an existing table from the database and removes all its data.
  - **ALTER TABLE**: a command that modifies the schema or constraints of an existing table in the database.
  - **INSERT**: a command that inserts one or more rows into a table in the database.
  - **UPDATE**: a command that modifies one or more rows in a table in the database based on a given condition.
  - **DELETE**: a command that deletes one or more rows from a table in the database based on a given condition.
  - **SELECT**: a command that queries data from one or more tables in the database and returns a result table.
  - **JOIN**: a clause that combines two tables based on a common attribute or a join condition and produces a new table with the concatenated schema



# Views and Indexes

## Views

- A view is a named query that defines a logical table based on the result of a SELECT statement.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface to different tables.
- A view does not store any data physically, but only references the data in the underlying tables.
- A view can be created, modified, or dropped using the CREATE VIEW, ALTER VIEW, or DROP VIEW statements.
- A view can be queried, updated, inserted, or deleted as if it were a table, as long as it meets certain conditions.
- A view can be indexed to improve the performance of queries that use the view .

## Indexes

- An index is a data structure that organizes the data in a table based on one or more columns.
- An index can speed up the retrieval of data from a table by reducing the number of disk accesses.
- An index can also enforce uniqueness, referential integrity, or sorting order on the indexed columns.
- An index can be created, modified, or dropped using the CREATE INDEX, ALTER INDEX, or DROP INDEX statements.
- An index can be clustered or nonclustered, depending on how the data is physically stored in relation to the index.
- An index can have positive or negative effects on the performance of queries, depending on the query type, the data distribution, and the workload.



# Queries and Subqueries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A query is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language such as SQL, which specifies what data is needed, not how to get it.
- A subquery is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used when you need to process data in several steps, or when you want to use the result of one query as an input for another query. Subqueries can also be used to compare values, test for existence, or perform aggregation.
- There are three main types of subqueries: scalar, multirow, and correlated.

## Scalar subqueries
- A scalar subquery is a subquery that returns a single value. It can be used anywhere a literal value can be used, such as in a SELECT list, a WHERE clause, a HAVING clause, or a SET clause.
- A scalar subquery must be enclosed in parentheses, and it must have only one column in the SELECT list.
- Example: The following query uses a scalar subquery to find the average salary of all employees in the company.

```sql
SELECT AVG(salary) AS avg_salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

## Multirow subqueries
- A multirow subquery is a subquery that returns one or more rows. It can be used with operators that compare a value to a set of values, such as IN, NOT IN, ANY, ALL, EXISTS, or NOT EXISTS.
- A multirow subquery must be enclosed in parentheses, and it can have one or more columns in the SELECT list.
- Example: The following query uses a multirow subquery to find the names of the employees who work in the same department as John Smith.

```sql
SELECT name
FROM employees
WHERE department_id IN (SELECT department_id FROM employees WHERE name = 'John Smith');
```

## Correlated subqueries
- A correlated subquery is a subquery that depends on the outer query for its values. It is executed once for each row of the outer query, and it can reference columns from the outer query in its WHERE clause.
- A correlated subquery must be enclosed in parentheses, and it can have one or more columns in the SELECT list.
- Example: The following query uses a correlated subquery to find the names of the employees who earn more than the average salary of their department.

```sql
SELECT name, salary, department_id
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e1.department_id = e2.department_id);
```



# Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the `GROUP BY` clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - `COUNT`: returns the number of values in a set or the number of rows that satisfy a condition.
  - `SUM`: returns the sum of all values in a set or the sum of values that satisfy a condition.
  - `AVG`: returns the average of all values in a set or the average of values that satisfy a condition.
  - `MIN`: returns the minimum value in a set or the minimum value that satisfies a condition.
  - `MAX`: returns the maximum value in a set or the maximum value that satisfies a condition.

- Aggregate functions can be used in the `SELECT` clause, the `HAVING` clause, or the `ORDER BY` clause of a query.
- Aggregate functions ignore `NULL` values in the set of values they operate on, unless otherwise specified by the function.
- Aggregate functions can be combined with other expressions or functions using arithmetic operators or nested function calls.
- Aggregate functions can also be applied to distinct values in a set by using the keyword `DISTINCT` before the function name.

- Example: The following query returns the total number of employees, the average salary, the minimum salary, and the maximum salary in each department of a company.

  ```sql
  SELECT dept_id, COUNT(*), AVG(salary), MIN(salary), MAX(salary)
  FROM employee
  GROUP BY dept_id;
  ```



# Relational Data Model and Language

- Relational Data Model and Language is a way of organizing and manipulating data in a relational database using tables and SQL programming language .
- A relational database is a collection of relations (tables) that store data in rows (tuples) and columns (attributes)  .
- A relation has a name and a set of attributes with unique names and data types .
- A tuple is a row of data that represents an entity or a relationship .
- An attribute is a column of data that represents a property or characteristic of an entity or a relationship .
- A key is a set of one or more attributes that uniquely identifies a tuple in a relation .
- A primary key is a key that is chosen to be the main identifier of a relation .
- A foreign key is a key that references a primary key of another relation .
- A relational schema is a set of relation names and their attributes .
- A relational database schema is a set of relational schemas and the constraints that apply to them .
- A relational algebra is a set of operations that can be applied to relations or sets of relations to produce new relations .
- A relational calculus is a declarative language that can be used to specify queries on relations using logical expressions .
- SQL is a widely used relational language that combines aspects of both relational algebra and relational calculus  .
- SQL can be used to define, manipulate, and query data in a relational database .
- SQL has a standard syntax and semantics, but different implementations may have variations and extensions .



# Update and Delete Operations

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes for a set of tuples that satisfy a given condition.
- Delete operations can remove one or more tuples that satisfy a given condition from a relation.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and with proper authorization.
- The syntax for update and delete operations in SQL is as follows:

```sql
-- Update operation
UPDATE <table_name>
SET <attribute_name> = <new_value>, ...
WHERE <condition>;

-- Delete operation
DELETE FROM <table_name>
WHERE <condition>;
```

- The condition clause specifies which tuples are affected by the operation. It can use logical operators such as AND, OR, and NOT, as well as comparison operators such as =, <, >, etc.
- The update operation can also use arithmetic expressions, functions, or subqueries to compute the new values for the attributes.
- The delete operation can also use the keyword ALL to remove all the tuples from a relation, or the keyword CASCADE to remove the tuples that reference the deleted tuples in other relations (if foreign key constraints are defined).
- Some examples of update and delete operations in SQL are:

```sql
-- Update the salary of employee with ID 101 by 10%
UPDATE employee
SET salary = salary * 1.1
WHERE emp_id = 101;

-- Delete the employee with ID 102
DELETE FROM employee
WHERE emp_id = 102;

-- Delete all the employees who work in department 10
DELETE FROM employee
WHERE dept_id = 10;

-- Delete all the departments and cascade the deletion to the employees
DELETE FROM department
CASCADE;
```



# Joins

Joins are operations in relational data model that allow queries across multiple database tables. Joins merge data stored in different tables and output it in filtered form in a results table. The principle of SQL join is based on the relational algebra operation of the same name – a combination of Cartesian product and selection.

The prerequisite for joins is that the selected tables are linked to one another using foreign key relationships. The most important join types include the following:

- **Theta (θ) Join**: Theta join combines tuples from different relations provided they satisfy the theta condition. The join condition is denoted by the symbol θ. The theta condition can use any comparison operator, such as =, <, >, <=, >=, or <>.
- **Equijoin**: When theta join uses only equality comparison operator, it is said to be equijoin. Equijoin is a special case of theta join. Equijoin can also be called as inner join.
- **Natural Join ( ⋈)**: Natural join does not use any comparison operator. It combines tuples from different relations by comparing all their common attributes. Natural join eliminates duplicate columns from the result.
- **Outer Joins**: Outer joins are used to retrieve data from two or more tables even if there is no matching data. There are three types of outer joins: left outer join, right outer join, and full outer join.
- **Left Outer Join (R S)**: Left outer join returns all the tuples from the left relation R and only the matching tuples from the right relation S. If there is no match for a tuple in R, then the attributes of S are filled with null values.
- **Right Outer Join (R S)**: Right outer join returns all the tuples from the right relation S and only the matching tuples from the left relation R. If there is no match for a tuple in S, then the attributes of R are filled with null values.
- **Full Outer Join ( R S)**: Full outer join returns all the tuples from both the relations R and S. If there is no match for a tuple in either relation, then the attributes of the other relation are filled with null values.

Here is a diagram that illustrates the different types of joins:

Joins diagram



# Unions

- A union is a set operation that combines the results of two or more queries into one result set.
- A union can be used to retrieve data from more than one table simultaneously and then merge the results.
- A union requires that the queries involved have the same number of columns and that the corresponding columns have the same data type.
- A union eliminates any duplicate rows from the result set, unless the keyword ALL is used.
- A union can be expressed in relational algebra as R1 UNION R2, where R1 and R2 are two union-compatible relations.
- A union can be expressed in SQL as SELECT * FROM R1 UNION SELECT * FROM R2, where R1 and R2 are two union-compatible tables.
- A union can be useful for combining data from different sources, such as different databases, different tables, or different views.
- A union can also be used to perform set operations such as intersection, difference, and complement, by using the keywords INTERSECT, EXCEPT, and NOT IN.



# Intersection

- Intersection is a relational operator that returns the common tuples (rows) that are present in both of two union-compatible (same columns and same type) relations A and B, denoted by A ∩ B .
- Intersection can be expressed using set difference operator as follows; R1 ∩ R2 = R1 – (R1 – R2) .
- Intersection is a commutative and associative operation, that is, A ∩ B = B ∩ A and (A ∩ B) ∩ C = A ∩ (B ∩ C) .
- Intersection can be implemented using a nested loop join algorithm, where for each tuple in R1, we check if it exists in R2, and if so, we add it to the result .
- Intersection can be used to find the common values of attributes in two relations, such as finding the students who are enrolled in both Math and Physics courses.



# Unit 2 - Relational Data Model and Language

## Relational Data Model
- A relational data model is a way of representing data in a database using tables, columns, rows, and keys.
- A table is a collection of related data, where each column represents an attribute and each row represents a record or a tuple.
- A key is a column or a combination of columns that uniquely identifies a row in a table.
- A primary key is a key that is chosen to be the main identifier of a row in a table. A table can have only one primary key.
- A foreign key is a key that references a primary key of another table. A table can have multiple foreign keys.
- A relational schema is a set of table definitions, along with their keys and constraints.
- A constraint is a rule that restricts the values that can be stored in a table or a column. Some common types of constraints are:
  - Not null: a column cannot have null values.
  - Unique: a column or a combination of columns cannot have duplicate values.
  - Check: a column or a row must satisfy a specified condition.
  - Default: a column has a default value if no value is specified.
  - Referential integrity: a foreign key must match an existing value of a primary key in the referenced table.

## Relational Algebra
- Relational algebra is a set of operations that can be applied to one or more tables to manipulate and query data.
- Relational algebra operations can be classified into two categories: unary and binary.
- Unary operations take one table as input and produce one table as output. Some common unary operations are:
  - Select: selects a subset of rows from a table that satisfy a given condition.
  - Project: selects a subset of columns from a table.
  - Rename: changes the name of a table or a column.
- Binary operations take two tables as input and produce one table as output. Some common binary operations are:
  - Union: combines the rows of two tables that have the same schema (same number and names of columns).
  - Intersection: selects the rows that are common to both tables that have the same schema.
  - Difference: selects the rows that are in the first table but not in the second table that have the same schema.
  - Cartesian product: combines every row of the first table with every row of the second table, regardless of the schema.
  - Join: combines the rows of two tables that have a common attribute or a matching condition. There are different types of joins, such as:
    - Natural join: joins two tables on all the common attributes.
    - Equi-join: joins two tables on a specified condition that involves equality.
    - Theta-join: joins two tables on a specified condition that involves any comparison operator.
    - Inner join: selects only the matching rows from both tables.
    - Outer join: selects all the rows from one or both tables, and fills the missing values with nulls. There are three types of outer joins: left, right, and full.
    - Semi-join: selects the rows from the first table that have a matching row in the second table, but does not include the columns from the second table.
    - Anti-join: selects the rows from the first table that do not have a matching row in the second table.
- Relational algebra operations can be composed to form complex expressions that can be evaluated to produce a result table.
- Relational algebra expressions can be represented using a tree diagram, where the leaves are the input tables and the nodes are the operations. The root of the tree is the final result table.



# Cursors

- A cursor is a database object that allows you to manipulate data in a row-by-row manner.
- A cursor can be thought of as a pointer to a specific row within a query result .
- Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval, addition and removal of database records.
- Cursors are an extension to result sets that provide mechanisms for positioning at specific rows, retrieving one row or block of rows, and supporting data modifications.
- Cursors are created and executed on the database server itself.
- Cursors have a lifecycle that involves the following steps :
  - Declare a cursor: A cursor is declared by defining a SQL statement that returns a result set.
  - Open a cursor: A cursor is opened by executing the SQL statement and creating the result set in memory.
  - Fetch a cursor: A cursor is fetched by moving the pointer to a row in the result set and retrieving the data from that row.
  - Close a cursor: A cursor is closed by releasing the result set from memory and freeing the resources associated with the cursor.
  - Deallocate a cursor: A cursor is deallocated by removing the cursor definition from the database server.
- Cursors can be classified into different types based on their characteristics, such as:
  - Forward-only or scrollable: A forward-only cursor can only move from the first row to the last row in the result set, while a scrollable cursor can move in any direction.
  - Static or dynamic: A static cursor works with a snapshot of the result set and does not reflect any changes made to the underlying data, while a dynamic cursor reflects any changes made to the underlying data.
  - Keyset-driven or insensitive: A keyset-driven cursor works with a set of keys that identify the rows in the result set and reflects any changes made to the non-key columns of the underlying data, while an insensitive cursor works with a snapshot of the result set and does not reflect any changes made to the underlying data.
  - Local or global: A local cursor is visible only within the scope of the batch, stored procedure, or trigger that declares it, while a global cursor is visible to all users and all connections.
- Cursors are useful when you need to perform row-level operations on data, such as looping through the rows, applying complex logic, or updating or deleting individual rows .
- Cursors have some disadvantages, such as:
  - Cursors consume more memory and CPU resources than set-based operations .
  - Cursors can cause locking and blocking issues on the underlying data, affecting the concurrency and performance of other transactions .
  - Cursors can introduce errors and bugs if not handled properly, such as forgetting to close or deallocate the cursor .
- Cursors should be used sparingly and only when necessary, as set-based operations are usually faster and more efficient than cursor-based operations .



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here are some triggers for the notes of the Unit 2 - Relational data Model and Language:

# Triggers for the notes of the Unit 2 - Relational data Model and Language

- Define the relational data model and its components: relation, attribute, domain, tuple, degree, cardinality, primary key, foreign key, etc.
- Explain the concept of relational integrity constraints: entity integrity, referential integrity, domain integrity, etc.
- Describe the relational algebra operations: select, project, union, set difference, Cartesian product, rename, join, division, etc. and give examples of each.
- Illustrate the use of relational algebra to express queries and manipulate data in a relational database.
- Compare and contrast relational algebra and relational calculus: their syntax, semantics, expressive power, and advantages and disadvantages.
- Define the tuple relational calculus and the domain relational calculus and give examples of each.
- Explain the concept of safe expressions and range-restricted variables in relational calculus.
- Discuss the properties of relational languages: closure, completeness, and decidability.
- Describe the SQL language and its components: data definition language, data manipulation language, data control language, and data query language.
- Demonstrate the use of SQL to create, alter, and drop tables, views, indexes, and constraints in a relational database.
- Demonstrate the use of SQL to insert, update, delete, and query data in a relational database.
- Apply the SQL functions and operators to perform calculations, aggregations, and transformations on data in a relational database.
- Use the SQL clauses and keywords to specify the conditions, order, grouping, and joining of data in a relational database.
- Explain the concept of subqueries, nested queries, and correlated queries in SQL and give examples of each.
- Discuss the advantages and disadvantages of SQL as a relational language.



# Procedures in SQL/PL SQL

- A procedure is a named PL/SQL block that can be stored in the database and can be invoked by name  .
- A procedure can perform a specific task or a series of tasks, such as inserting, updating, deleting, or querying data .
- A procedure can have parameters that can be passed by the caller or the invoker  .
- A procedure can return values to the caller through output parameters or variables  .
- A procedure can be invoked by other procedures, functions, triggers, or applications  .

## Syntax of a procedure

- A procedure has a header and a body  .
- The header consists of the keyword PROCEDURE, followed by the procedure name, followed by a list of parameters in parentheses  .
- The body consists of the keyword IS or AS, followed by the declaration section, the executable section, and the optional exception-handling section  .
- The declaration section declares the variables, constants, cursors, and user-defined exceptions that are used in the procedure  .
- The executable section contains the PL/SQL statements that perform the logic of the procedure  .
- The exception-handling section handles the errors that may occur during the execution of the procedure  .

## Example of a procedure

- The following example shows a procedure named adjust_salary that accepts an employee ID and a percentage as input parameters and updates the salary of the employee by the given percentage .

```sql
CREATE OR REPLACE PROCEDURE adjust_salary (
  p_emp_id IN employees.employee_id%TYPE,
  p_percentage IN NUMBER
) IS
BEGIN
  UPDATE employees
  SET salary = salary * (1 + p_percentage/100)
  WHERE employee_id = p_emp_id;
END adjust_salary;
/
```

## Calling a procedure

- A procedure can be called by using the keyword EXECUTE or EXEC, followed by the procedure name and the arguments in parentheses .
- The arguments can be literals, variables, expressions, or placeholders .
- The arguments must match the number, order, and data type of the parameters in the procedure .

## Example of calling a procedure

- The following example shows how to call the adjust_salary procedure with different arguments .

```sql
-- Call the procedure with literals
EXECUTE adjust_salary(100, 10);

-- Call the procedure with variables
DECLARE
  v_emp_id employees.employee_id%TYPE := 101;
  v_percentage NUMBER := 15;
BEGIN
  adjust_salary(v_emp_id, v_percentage);
END;
/

-- Call the procedure with expressions
EXECUTE adjust_salary(102, 5 + 2);

-- Call the procedure with placeholders
EXECUTE adjust_salary(:emp_id, :percentage);
```



## Unit 3 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- The benefits of database normalization include:
  - Eliminating or minimizing data anomalies, such as insertion, deletion, and update anomalies, that can cause data inconsistency or loss.
  - Reducing the storage space required by avoiding duplicate data.
  - Simplifying the queries and operations on the database by having a clear and consistent structure.
  - Enhancing the security and performance of the database by reducing the complexity and scope of data access.
- The drawbacks of database normalization include:
  - Increasing the number of tables and joins, which can affect the query speed and complexity.
  - Losing some information or relationships that are not captured by the normal forms.
  - Requiring more processing power and memory to perform the normalization and denormalization processes.
- The levels of database normalization are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or arrays of data, and each column has a single value for each row. For example, a table that stores the name, address, and phone numbers of customers is not in 1NF if it has a column for multiple phone numbers. To make it 1NF, the phone numbers column should be split into separate columns or a separate table.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key, not just a part of it. For example, a table that stores the order details of customers is not in 2NF if it has a composite primary key of order ID and product ID, and a column for the product name. To make it 2NF, the product name column should be moved to a separate table that has product ID as the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key, not on any other non-key column. For example, a table that stores the order details of customers is not in 3NF if it has a column for the customer name, which depends on the customer ID, which is a non-key column. To make it 3NF, the customer name column should be moved to a separate table that has customer ID as the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (a column or a set of columns that determines the value of another column) is a candidate key (a column or a set of columns that can uniquely identify a row). For example, a table that stores the enrollment details of students is not in BCNF if it has a column for the course instructor, which depends on the course ID, which is a determinant but not a candidate key. To make it BCNF, the course instructor column should be moved to a separate table that has course ID as the primary key.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies (a situation where a column or a set of columns depends on another column or a set of columns, and the dependency is not one-to-one or one-to-many, but many-to-many). For example, a table that stores the hobbies and skills of employees is not in 4NF if it has columns for employee ID, hobby, and skill, and there is a multi-valued dependency between hobby and skill. To make it 4NF, the table should be split into two tables, one for employee ID and hobby, and another for employee ID and skill.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (a situation where a table can be decomposed into two or more tables, and the original table can be reconstructed by joining the decomposed tables on their primary keys). For example, a table that stores the preferences of customers for products and colors is not in 5NF if it has columns for customer ID, product ID, and color ID, and there is a join dependency between the three columns. To make it 5NF, the table should be split into three



# Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency is denoted by an arrow, such as X → Y, which means that the value of Y is determined by the value of X.
- A functional dependency is an essential factor in designing database parameters and functions to help store and manage data.
- A functional dependency is used to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity.
- There are four primary types of functional dependencies in DBMS: trivial, non-trivial, multivalued, and transitive .
  - A trivial functional dependency is a functional dependency where the dependent is always a subset of the determinant, such as X → X or X → XY.
  - A non-trivial functional dependency is a functional dependency where the dependent is strictly not a subset of the determinant, such as X → Y, where Y is not a part of X.
  - A multivalued functional dependency is a functional dependency where the determinant can have multiple values for the dependent, such as X → YZ, where Y and Z are independent of each other.
  - A transitive functional dependency is a functional dependency where the determinant depends on another attribute, which in turn depends on another attribute, such as X → Y and Y → Z, which implies X → Z.
- A functional dependency can be used to identify the primary key (PK) and other non-key attributes within a table.
- A functional dependency can be used to decompose a relation into smaller relations that are in higher normal forms.
- A functional dependency can be used to check the consistency and validity of the data in a relation.



# Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

## Introduction

- Database normalization is a database design principle for organizing data in an organized and consistent way.
- It helps you avoid redundancy and maintain the integrity of the database.
- It also helps you eliminate undesirable characteristics associated with insertion, deletion, and updating.
- Normal forms are used to eliminate or reduce redundancy in database tables.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table.
- A table is said to be in a certain normal form if it satisfies certain conditions or rules.

## Types of Normal Forms in DBMS

- Normal forms are of four major forms: 1NF, 2NF, 3NF, and BCNF.
- A majority of the database systems have their databases normalized up to the 3NF in DBMS.
- But here are the normal forms that are used in DBMS:

### 1NF (First Normal Form)

- A table is in 1NF if it does not contain any composite or multi-valued attribute.
- A composite attribute is an attribute that can be further divided into sub-attributes, such as address, name, etc.
- A multi-valued attribute is an attribute that can have more than one value for a given entity, such as hobbies, skills, etc.
- To convert a table into 1NF, we need to split the composite and multi-valued attributes into separate attributes and create a new table for each multi-valued attribute with a foreign key referencing the original table.

### 2NF (Second Normal Form)

- A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
- A functional dependency is a relationship between two or more attributes of a table, such that the value of one attribute determines the value of another attribute.
- A non-key attribute is an attribute that is not part of the primary key.
- A primary key is a set of attributes that uniquely identifies each record in a table.
- A full functional dependency is a functional dependency where the entire set of attributes in the primary key is required to determine the value of another attribute.
- To convert a table into 2NF, we need to identify the partial dependencies, where a non-key attribute depends on only a part of the primary key, and remove them by creating a new table with the dependent attributes and a foreign key referencing the original table.

### 3NF (Third Normal Form)

- A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
- A transitive dependency is a functional dependency where a non-key attribute depends on another non-key attribute, which in turn depends on the primary key.
- To convert a table into 3NF, we need to identify the transitive dependencies and remove them by creating a new table with the dependent attributes and a foreign key referencing the original table.

### BCNF (Boyce-Codd Normal Form)

- A table is in BCNF if it is in 3NF and every determinant is a candidate key.
- A determinant is an attribute or a set of attributes that determines the value of another attribute or a set of attributes.
- A candidate key is a set of attributes that can uniquely identify each record in a table and is a minimal subset of the superkey.
- A superkey is a set of attributes that can uniquely identify each record in a table.
- To convert a table into BCNF, we need to identify the dependencies where a determinant is not a candidate key and remove them by creating a new table with the dependent attributes and a foreign key referencing the original table.

## Conclusion

- Normal forms are a way of ensuring that the database design is optimal and free of anomalies.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table.
- Normal forms are of four major forms: 1NF, 2NF, 3NF, and BCNF.
- Each normal form has a set



# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and storage formats.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, insertion, update, and deletion of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Flexibility: The database should be able to accommodate changing data requirements and business needs, and support new features and functionalities.

## Normalization
- Normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity and organization of data.
- Normalization helps in achieving the following benefits:
  - Improved Database Design: Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.
  - Reduced Data Anomalies: Normalization helps in reducing the data anomalies, such as insertion, update, and deletion anomalies, that may arise due to redundant and dependent data. Data anomalies can cause data inconsistency and corruption, and affect the quality and reliability of the database.
  - Enhanced Data Integrity: Normalization helps in enhancing the data integrity, by enforcing the constraints and rules on the data. Data integrity ensures that the data is valid, accurate, and consistent, and conforms to the business logic and expectations.
  - Optimized Performance: Normalization helps in optimizing the performance of the database, by reducing the data duplication and the number of joins required to retrieve the data. Normalization also facilitates the use of indexes and query optimization techniques, which can improve the speed and efficiency of the database operations.

## Normal Forms
- Normal forms are the standards or rules that define the level of normalization of a database schema. Normal forms are based on the concept of functional dependencies, which describe the relationship between the attributes of a table.
- Functional dependency: A functional dependency is a constraint that specifies that the value of one or more attributes (called the determinant) determines the value of another attribute (called the dependent).
- For example, in a table that stores the student ID, name, and email of students, the student ID determines the name and email of the student. This can be written as: student ID -> name, email
- The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, i.e., each attribute has a single value for each tuple (row), and there are no repeating groups of attributes.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no dependencies on non-key attributes.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, i.e., there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and there are no join dependencies, i.e., there are no attributes that depend on the combination of two or more tables rather than a single table.



# Unit 3 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database normalization is a technique of database design that reduces data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- The main benefits of database normalization are:
  - Improved data integrity and consistency
  - Reduced data anomalies and errors
  - Enhanced query performance and efficiency
  - Simplified database maintenance and modification
- The main drawbacks of database normalization are:
  - Increased complexity and overhead of joining multiple tables
  - Possible loss of information or performance in some cases
  - Trade-off between normalization and denormalization depending on the application requirements
- There are several levels or forms of database normalization, each with a specific set of rules and criteria to check and improve the quality of a database schema. The most common forms are:
  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic and indivisible.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be determined by a subset of the primary key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be determined by another non-key attribute.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies on non-key attributes.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies, meaning there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, meaning it cannot be decomposed into smaller tables without losing information.
- The process of database normalization involves the following steps:
  - Identify the functional dependencies and candidate keys of a table
  - Check the table against each normal form and identify any violations
  - Decompose the table into smaller tables that satisfy the normal form
  - Define the primary keys and foreign keys of the new tables
  - Repeat the process for each new table until the desired level of normalization is achieved



# Third Normal Form

- Third normal form (3NF) is a database design principle that aims to reduce data redundancy and improve data integrity.
- 3NF states that a table is in 3NF if it is in second normal form (2NF) and every non-key attribute is non-transitively dependent on the primary key.
- Non-transitive dependency means that there is no indirect or hidden relationship between a non-key attribute and the primary key through another non-key attribute.
- For example, consider a table that stores the information of students, courses, and instructors:

| Student ID | Student Name | Course ID | Course Name | Instructor ID | Instructor Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| S001       | Alice        | C001      | DBMS        | I001          | Bob             |
| S002       | Bob          | C002      | OOP         | I002          | Carol           |
| S003       | Carol        | C001      | DBMS        | I001          | Bob             |
| S004       | Dave         | C003      | DS          | I003          | Dave            |

- This table is not in 3NF because there are non-transitive dependencies between the non-key attributes. For instance, Course Name depends on Course ID, and Instructor Name depends on Instructor ID, which are both non-key attributes.
- To convert this table into 3NF, we need to decompose it into smaller tables that eliminate the non-transitive dependencies. One possible way to do this is:

| Student ID | Student Name | Course ID |
|------------|--------------|-----------|
| S001       | Alice        | C001      |
| S002       | Bob          | C002      |
| S003       | Carol        | C001      |
| S004       | Dave         | C003      |

| Course ID | Course Name | Instructor ID |
|-----------|-------------|---------------|
| C001      | DBMS        | I001          |
| C002      | OOP         | I002          |
| C003      | DS          | I003          |

| Instructor ID | Instructor Name |
|---------------|-----------------|
| I001          | Bob             |
| I002          | Carol           |
| I003          | Dave            |

- The benefits of 3NF are:

  - It reduces data duplication and storage space.
  - It improves data consistency and accuracy.
  - It facilitates data manipulation and querying.
  - It prevents update, insertion, and deletion anomalies.



# BCNF

- BCNF stands for Boyce-Codd Normal Form, which is a higher form of normalization than 3NF.
- A relation R is in BCNF if for every non-trivial functional dependency X -> Y, X is a superkey of R.
- A superkey is a set of attributes that uniquely identifies a tuple in a relation.
- BCNF eliminates redundancy and anomalies caused by transitive dependencies, where a non-key attribute depends on another non-key attribute.
- To convert a relation to BCNF, we need to decompose it into smaller relations that satisfy the BCNF condition.
- The decomposition should be lossless, meaning that we can reconstruct the original relation by joining the decomposed relations.
- The decomposition should also preserve the dependencies, meaning that we do not lose any functional dependencies by decomposing the relation.
- An example of a relation that is not in BCNF is:

| Student ID | Course ID | Instructor |
|------------|-----------|------------|
| S1         | C1        | I1         |
| S1         | C2        | I2         |
| S2         | C1        | I1         |
| S2         | C3        | I3         |

- In this relation, the functional dependencies are:

  - Student ID -> Course ID
  - Course ID -> Instructor

- Neither Student ID nor Course ID is a superkey, so the relation is not in BCNF.
- To convert it to BCNF, we can decompose it into two relations:

  - R1(Student ID, Course ID)
  - R2(Course ID, Instructor)

- The decomposition is lossless, as we can join R1 and R2 on Course ID to get the original relation.
- The decomposition also preserves the dependencies, as both R1 and R2 are in BCNF.



# Inclusion Dependence

- Inclusion dependence is a constraint that expresses the inclusion of values from one relation into another relation.
- Inclusion dependence can be seen as a generalization of foreign key constraints, where the referencing attributes do not have to form a key in the referencing relation.
- Inclusion dependence can be represented by a diagram that shows an arrow from the referencing attributes to the referenced attributes, with a circle at the tail of the arrow.
- Inclusion dependence can be used to model various semantic relationships between relations, such as subtyping, aggregation, and generalization.
- Inclusion dependence can also be used to enforce integrity constraints on the database, such as referential integrity, domain integrity, and entity integrity.



# Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R.
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data .
- Lossless join decomposition is based on the concept of functional dependencies, which are constraints that specify how one set of attributes determines another set of attributes in a relation.
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the set of functional dependencies F for R :

  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2

- The above condition means that the common attributes of R1 and R2 form a candidate key for either R1 or R2 .
- There are algorithms to check whether a given decomposition is lossless or not, such as the chase algorithm.
- There are also algorithms to decompose a relation into a lossless join decomposition that satisfies a certain normal form, such as the Boyce-Codd normal form (BCNF) algorithm and the third normal form (3NF) algorithm.



# Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Normal forms are defined based on the concept of functional dependencies (FDs).

A functional dependency (FD) is a constraint that describes the relationship between attributes in a relation. It has the form X -> Y, where X and Y are sets of attributes of the relation. It means that the values of Y are determined by the values of X, or equivalently, two tuples that agree on X must also agree on Y. X is called the determinant and Y is called the dependent.

For example, in a relation R(A, B, C, D) with the following FDs:

- A -> B
- B -> C
- A, C -> D

We can say that B is functionally dependent on A, C is functionally dependent on B, and D is functionally dependent on A and C.

There are different normal forms that a relation can satisfy, depending on the properties of its FDs. The most common ones are:

- First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. This is the basic requirement for a relation to be well-formed.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there is no partial dependency, where a non-key attribute depends on only part of the primary key.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there is no transitive dependency, where a non-key attribute depends on another non-key attribute that depends on the primary key.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key. This means that there is no dependency where a non-key attribute determines another non-key attribute.

Normalization using FDs is the process of applying these normal forms to a relation to reduce redundancy and anomalies. It involves finding the minimal cover of FDs for the relation, identifying the candidate keys, and decomposing the relation into smaller relations that satisfy the desired normal form. The minimal cover of FDs is a set of FDs that is equivalent to the original set of FDs, but has no redundant FDs or attributes. A candidate key is a minimal set of attributes that uniquely identifies each tuple in the relation.

For example, consider the relation R(A, B, C, D) with the following FDs:

- A -> B
- B -> C
- A, C -> D

The minimal cover of FDs for R is:

- A -> B
- B -> C
- A -> D

The candidate keys for R are:

- A
- B, D

To normalize R into 3NF, we can decompose it into the following relations:

- R1(A, B) with FD A -> B
- R2(B, C) with FD B -> C
- R3(A, D) with FD A -> D

To normalize R into BCNF, we can decompose it further into the following relations:

- R1(A, B) with FD A -> B
- R2(B, C) with FD B -> C
- R3(A, D) with FD A -> D
- R4(B, D) with no FDs

Normalization using FDs can help improve the quality and efficiency of a database design by eliminating redundancy and anomalies. However, it may also introduce some drawbacks, such as loss of information, increased number of joins, and reduced performance. Therefore, normalization should be balanced with other design considerations, such as user requirements, query patterns, and data integrity.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 3 - Data Base Design & Normalization in the subject of Database Management System. Here are some notes on the topic of MVD:

# MVD

- MVD stands for Multivalued Dependency, which is a type of functional dependency that occurs when one attribute determines a set of values for another attribute, and these values are independent of each other.
- For example, in a relation R(A, B, C), if A ->> B and A ->> C, then A determines a set of values for B and a set of values for C, and these values are not related to each other. This means that for a given value of A, there can be multiple combinations of B and C values in the relation.
- MVD is a generalization of functional dependency, which is a special case of MVD where the set of values determined by one attribute is a singleton. That is, if A -> B, then A ->> B, but not vice versa.
- MVD is used to identify redundancy and anomalies in a relation, and to decompose the relation into smaller relations that are in 4NF (Fourth Normal Form).
- A relation R is in 4NF if and only if, for every non-trivial MVD X ->> Y that holds on R, X is a superkey of R. That is, there is no MVD in R that violates the superkey constraint.
- To decompose a relation R into 4NF, we can use the following algorithm:

  - Find a non-trivial MVD X ->> Y that holds on R and that violates the superkey constraint.
  - Decompose R into two relations: R1(X, Y) and R2(X, R - Y), where R - Y is the set difference of R and Y.
  - Repeat the above steps for R1 and R2 until no more non-trivial MVDs are found.



# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, and relationships that represent the information and business rules of a domain.
- Database design also involves choosing the appropriate data types, constraints, indexes, and views for each attribute and table.
- Database design aims to achieve the following objectives:
  - Reduce data redundancy and inconsistency by avoiding unnecessary duplication and ensuring data integrity.
  - Improve data quality and accuracy by enforcing validation rules and business logic.
  - Enhance data security and privacy by implementing access control and encryption mechanisms.
  - Optimize data performance and scalability by minimizing disk space and memory usage, and maximizing query speed and concurrency.
  - Facilitate data maintenance and evolution by allowing easy modification and extension of the database schema and data.

## Normalization
- Normalization is a database design technique, which is used to design a relational database table up to higher normal form.
- The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization helps to eliminate data anomalies, such as insertion, deletion, and update anomalies, that may arise due to poor database design.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF), that define the criteria for a well-designed database table.
- The most common normal forms are 1NF, 2NF, and 3NF, which are explained below:

### First Normal Form (1NF)
- A table is in 1NF if it satisfies the following conditions:
  - Each table has a unique name and a primary key that uniquely identifies each row.
  - Each attribute has a single value and a unique name.
  - Each attribute has a domain that specifies the range of values and the data type of the attribute.
  - There are no repeating groups or arrays of values in any attribute.
  - The order of the rows and columns does not matter.

### Second Normal Form (2NF)
- A table is in 2NF if it satisfies the following conditions:
  - The table is in 1NF.
  - All the non-key attributes are fully functionally dependent on the primary key, meaning that they are determined by the primary key and not by any other attribute or subset of attributes.
  - There are no partial dependencies, meaning that no non-key attribute depends on only a part of the primary key.

### Third Normal Form (3NF)
- A table is in 3NF if it satisfies the following conditions:
  - The table is in 2NF.
  - All the non-key attributes are non-transitively dependent on the primary key, meaning that they are determined by the primary key and not by any other non-key attribute or combination of non-key attributes.
  - There are no transitive dependencies, meaning that no non-key attribute depends on another non-key attribute that depends on the primary key.

## Example of Normalization
- Consider the following table that stores the information of students, courses, and instructors:

| Student ID | Student Name | Course ID | Course Name | Instructor ID | Instructor Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| S001       | Alice        | C001      | Math        | I001          | Bob             |
| S001       | Alice        | C002      | English     | I002          | Carol           |
| S002       | David        | C001      | Math        | I001          | Bob             |
| S002       | David        | C003      | Science     | I003          | Eve             |
| S003       | Frank        | C002      | English     | I002          | Carol           |
| S003       | Frank        | C003      | Science     | I003          | Eve             |

- This table is not in 1NF, because it has repeating groups of values in the Course ID, Course Name, Instructor ID, and Instructor Name attributes. To convert it to 1NF, we need to split the table into two tables: one for the student



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on alternative approaches to database design for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System:

# Alternative Approaches to Database Design

- Database design is the process of defining the structure, organization, and relationships of data in a database.
- Database design can be influenced by various factors, such as the requirements of the application, the characteristics of the data, the performance and scalability needs, and the preferences of the database designer.
- There are different approaches and techniques that can be used to design a database, depending on the context and the goals of the project. Some of the common approaches and techniques are:

## Top-down Design Method

- This approach starts with identifying the main entities and relationships of the data domain, and then refining them into smaller and more detailed components.
- This approach is based on the concept of normalization, which is a process of organizing the data into tables that minimize data redundancy and dependency.
- Normalization involves applying a series of rules or normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on, to ensure that each table has a single purpose and a primary key, and that there are no partial or transitive dependencies among the attributes.
- Normalization can improve the integrity, consistency, and efficiency of the database, but it can also result in a large number of tables and complex joins, which can affect the performance and usability of the database.

## Bottom-up Design Method

- This approach starts with identifying the data elements and attributes that are needed for the application, and then grouping them into tables and establishing the relationships among them.
- This approach is based on the concept of denormalization, which is a process of combining or merging the data from multiple tables into fewer tables, to reduce the number of joins and improve the performance and simplicity of the database.
- Denormalization involves applying a series of techniques, such as pre-joining, aggregation, replication, and redundancy, to increase the data availability and accessibility in the database, but it can also result in data duplication and inconsistency, which can affect the integrity and maintenance of the database.

## NoSQL Design Method

- This approach is based on the use of non-relational or NoSQL databases, which are databases that do not follow the relational model and do not use SQL as the query language.
- NoSQL databases can store and manage data in different formats and structures, such as key-value pairs, documents, graphs, columns, and objects, depending on the nature and needs of the data.
- NoSQL databases can offer advantages such as flexibility, scalability, performance, and simplicity, especially for handling large and complex data sets that are often unstructured, heterogeneous, and dynamic.
- NoSQL databases can also pose challenges such as lack of standardization, consistency, and security, as well as difficulty in querying and analyzing the data.



# Unit 4 - Transaction Processing Concept

- A transaction is a logical unit of work that accesses and possibly modifies data in a database or a system.
- A transaction processing system (TPS) is a system that supports the execution of transactions in a reliable, efficient and secure manner.
- A transaction has four main properties, known as ACID:
  - Atomicity: A transaction is either completed in its entirety or not at all. If any part of the transaction fails, the entire transaction is aborted and the system is restored to its previous state.
  - Consistency: A transaction preserves the integrity and validity of the data in the system. It ensures that the system moves from one consistent state to another consistent state, without violating any rules or constraints.
  - Isolation: A transaction is executed independently of other transactions. It does not interfere with or see the effects of other concurrent transactions. Each transaction appears as if it is the only one running in the system.
  - Durability: A transaction, once committed, is permanent and cannot be undone. The effects of a committed transaction are preserved even in the event of system failures or power outages.
- A transaction can have one of the following outcomes:
  - Commit: The transaction successfully completes all its operations and makes its changes permanent in the system.
  - Abort: The transaction fails to complete all its operations and discards any changes it has made in the system.
  - Partial commit: The transaction completes some of its operations but not all. This is an undesirable outcome that violates the atomicity property and can lead to data inconsistency or corruption.
- A transaction can be classified into one of the following types:
  - Interactive transaction: A transaction that is initiated and controlled by a human user, such as withdrawing money from an ATM or booking a flight ticket online.
  - Batch transaction: A transaction that is executed as a group of transactions, without user intervention, such as payroll processing or billing.
  - Distributed transaction: A transaction that involves multiple systems or databases, such as transferring money between different banks or updating inventory across different warehouses.
  - Real-time transaction: A transaction that has strict time constraints and requires immediate response, such as stock trading or online gaming.



# Transaction System

A transaction system is a system that processes and records the daily transactions of a business or an organization. A transaction is a single unit of work or logic that involves one or more operations on a database. A transaction system ensures that the transactions are performed in a consistent, reliable, and atomic way, meaning that either all the operations in a transaction are completed successfully or none of them are.

Some examples of transaction systems are:

- CRM (Customer Relationship Management) system: This system manages the interactions and relationships with the customers of a business. It stores information such as customer profiles, contact details, purchase history, feedback, etc. A transaction in this system could be adding a new customer, updating a customer's information, or deleting a customer.
- HRM (Human Resources Management) system: This system manages the employees and their activities in an organization. It stores information such as employee profiles, payroll, benefits, performance, etc. A transaction in this system could be hiring a new employee, updating an employee's salary, or terminating an employee.
- ERP (Enterprise Resource Planning) system: This system integrates and coordinates the various functions and processes of an organization. It stores information such as inventory, production, sales, accounting, etc. A transaction in this system could be ordering a new product, updating the inventory, or generating an invoice.

A transaction system uses a database management system (DBMS) to store and manipulate the data in the database. A DBMS is a software tool that enables users to access and interact with the underlying data in the database. A DBMS provides features such as data security, data integrity, data backup, data recovery, data concurrency, etc. A DBMS also supports transaction management, which is the process of controlling and monitoring the transactions in the database. Transaction management ensures that the transactions follow the ACID properties, which are:

- Atomicity: A transaction is either fully completed or fully aborted. There is no partial execution of a transaction.
- Consistency: A transaction preserves the consistency of the database. It does not violate any integrity constraints or business rules.
- Isolation: A transaction is isolated from other concurrent transactions. It does not interfere with or affect the results of other transactions.
- Durability: A transaction is permanently recorded in the database. It is not lost or undone due to system failures or errors.

To achieve the ACID properties, a transaction system uses techniques such as locking, logging, checkpointing, recovery, etc. These techniques ensure that the transactions are executed correctly and reliably, and that the database is always in a consistent state.



# Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the same outcome as if the transactions were executed one by one in some order.
- Serializability is important for maintaining the consistency and correctness of a database in a concurrent environment.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read-write, write-read, or write-write) on the same data item by different transactions must be executed in the same order in the schedule as in the serial order.
- View serializability is a weaker form of serializability that requires that any transaction must read the same value and write the final value of any data item as in the serial order, but allows the order of non-conflicting operations to be different.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph is a directed graph of the entire transactions of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions. A schedule is conflict serializable if and only if its serialization graph is acyclic.
- A precedence graph is a directed graph of the conflicting operations of a schedule, where each node represents an operation and each edge represents a precedence relationship between two operations. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- A schedule is view serializable if and only if it is view equivalent to some serial schedule, meaning that it preserves the same read and write values as the serial schedule. Testing for view serializability is more complex than testing for conflict serializability and usually involves finding a legal serialization order for the transactions.



# Serializability of Schedules

- A schedule is a sequence of operations performed by one or more transactions on a database.
- A serial schedule is a schedule in which transactions are executed one after another, without any overlap in time.
- A non-serial schedule is a schedule in which transactions are executed concurrently, with some overlap in time.
- Serializability is a property of a schedule that ensures the consistency and correctness of a database.
- Serializability means that a non-serial schedule is equivalent to a serial schedule with the same transactions, in terms of the final state of the database and the data values.
- There are two methods to check the serializability of a schedule: conflict serializability and view serializability.

## Conflict Serializability

- Conflict serializability is based on the concept of conflict operations.
- Two operations are said to conflict if they belong to different transactions, access the same data item, and at least one of them is a write operation.
- A conflict operation can affect the outcome of a schedule, and hence the order of conflict operations must be preserved in any equivalent schedule.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Conflict serializability can be tested by using a precedence graph, which is a directed graph that represents the order of conflicting operations in a schedule.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.

## View Serializability

- View serializability is based on the concept of view equivalence.
- Two schedules are said to be view equivalent if they have the same view of the database, which means:
  - They read the same initial value for each data item.
  - They write the same final value for each data item.
  - They read the same value for each data item that is written by some transaction.
- A schedule is view serializable if it is view equivalent to some serial schedule.
- View serializability is a more general notion than conflict serializability, and it allows some schedules that are not conflict serializable.
- View serializability can be tested by using a polygraph, which is a directed graph that represents the read-write dependencies among transactions in a schedule.
- A schedule is view serializable if and only if its polygraph is acyclic and has no blind writes.



# Conflict & View Serializable Schedule

## Conflict Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is called **serial** if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is called **serializable** if it produces the same final state of the database as some serial schedule.
- A schedule is called **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be **conflicting** if all conditions satisfy:
  - They belong to different transactions
  - They operate on the same data item
  - At least one of them is a write operation
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- The schedule S is **not serial**, because it interleaves operations from T1 and T2.
- The schedule S is **conflict serializable**, because it can be transformed into a serial schedule S' by swapping non-conflicting operations:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- The schedule S' is **serial**, because it executes T1 first and then T2.
- The schedule S' is **equivalent** to S, because it produces the same final state of the database as S.

## View Serializable Schedule

- A schedule is called **view serializable** if it is view equal to a serial schedule.
- Two schedules are said to be **view equal** if the order of initial read, final write and update operations is the same in both the schedules.
- An **initial read** operation is the first read of a data item by any transaction in the schedule.
- A **final write** operation is the last write of a data item by any transaction in the schedule.
- An **update** operation is a read followed by a write of the same data item by the same transaction in the schedule.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- The schedule S is **not serial**, because it interleaves operations from T1 and T2.
- The schedule S is **view serializable**, because it is view equal to a serial schedule S'':

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
|     | R(A) |
|     | W(A) |

- The schedule S'' is **serial**, because it executes T2 first and then T1.
- The schedule S'' is **view equal** to S, because the order of initial read, final write and update operations is the same in both the schedules:
  - The initial read of A is done by T1 in both S and S''.
  - The final write of A is done by T1 in both S and S''.
  - The update of A is done by T1 in both S and S''.
  - The initial read of B is done by T2 in both S and S''.
  - The final write of B is done by T2 in both S and S''.
  - The update of B is done by T2 in both S and S''.

## Difference between Conflict and View Serializability

- Conflict serializability is a stricter condition than view serializability, because every conflict serializable schedule is also view serializable, but not vice versa.
- Conflict serializability can be checked by using a **precedence graph**, which is a directed graph that represents the order of conflicting operations in a schedule.
- View serializability can be checked by using a **polygraph**, which is a directed graph that represents the order of initial read, final write and update operations in a schedule.
- Conflict serializability is easier to implement and enforce than view serializability, because it



# Recoverability

Recoverability is a property of transaction schedules that ensures that the database state is consistent even if some transactions fail and are rolled back. A schedule is recoverable if no transaction commits before all the transactions whose changes it has read commit. In other words, a transaction can only depend on the results of committed transactions, not uncommitted ones. This prevents the problem of cascading aborts, where a single transaction failure causes many other transactions to abort as well.

## Types of Recoverability

There are different types of recoverability, depending on the order of commit and abort operations in a schedule. They are:

- **Strict schedules**: These are the schedules where a transaction cannot read or write a data item until the last transaction that wrote it commits or aborts. This ensures that no transaction ever reads a dirty (uncommitted) data item, and that the order of transactions is the same as the order of their commit operations. Strict schedules are always recoverable and also serializable, meaning that they are equivalent to some serial execution of the transactions.

- **Cascading rollback schedules**: These are the schedules where a transaction can read a data item written by an uncommitted transaction, but it cannot commit until that transaction commits. This means that if the transaction that wrote the data item aborts, then all the transactions that read it must also abort and roll back their changes. This can cause a cascade of aborts, which can be costly and inefficient. Cascading rollback schedules are recoverable, but not strict or serializable.

- **Irrecoverable schedules**: These are the schedules where a transaction can read a data item written by an uncommitted transaction, and it can also commit before that transaction commits or aborts. This means that if the transaction that wrote the data item aborts, then the database state becomes inconsistent, as the committed transaction has read a wrong value. Irrecoverable schedules are not recoverable, strict, or serializable, and should be avoided.

## Examples of Recoverability

Consider the following schedule of two transactions T1 and T2, where R(x) denotes reading data item x, W(x) denotes writing data item x, C denotes commit, and A denotes abort:

| T1 | T2 |
|----|----|
| R(A) | |
| | R(A) |
| W(A) | |
| | W(B) |
| C | |
| | C |

This schedule is **irrecoverable**, because T2 commits after reading A, which is written by T1, but before T1 commits. If T1 aborts after T2 commits, then the database state becomes inconsistent.

Consider another schedule of the same transactions:

| T1 | T2 |
|----|----|
| R(A) | |
| | R(A) |
| W(A) | |
| | W(B) |
| | C |
| C | |

This schedule is **recoverable**, but not **strict**, because T2 commits after reading A, which is written by T1, but before T1 commits. However, if T1 aborts after T2 commits, then T2 does not have to abort, because it has not read any dirty data from T1.

Consider a third schedule of the same transactions:

| T1 | T2 |
|----|----|
| R(A) | |
| | R(A) |
| W(A) | |
| | W(B) |
| C | |
| | A |

This schedule is **recoverable** and **strict**, because T2 does not commit before T1 commits, and T2 does not read or write any data item after T1 writes it. This schedule is also **serializable**, because it is equivalent to the serial execution of T1 followed by T2.



# Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations.
- A transaction failure can be caused by various reasons, such as system crash, power failure, user error, deadlock, concurrency control violation, or integrity constraint violation.
- To recover from transaction failure, the atomicity and durability of transactions must be maintained. That is, either all the operations of a transaction are executed or none, and the effects of committed transactions are not lost due to failures.
- There are three states of database recovery in DBMS:
  - Consistent state: A state where the database satisfies all the integrity constraints and reflects a correct state of the real world.
  - Inconsistent state: A state where the database violates some integrity constraints or does not reflect a correct state of the real world.
  - Intermediate state: A state where the database is in the process of executing a transaction and has not reached a consistent or inconsistent state yet.
- There are two types of database recovery in DBMS:
  - Crash recovery: The process of restoring the database to a consistent state after a system crash or power failure. Crash recovery involves redoing or undoing the operations of transactions that were affected by the failure.
  - Media recovery: The process of restoring the database to a consistent state after a disk failure or other physical damage to the storage media. Media recovery involves restoring the database from a backup copy and applying the changes made by transactions that occurred after the backup.
- There are various recovery techniques in DBMS that use different methods to record and restore the changes made by transactions. Some of the common recovery techniques are  :
  - Deferred update: A technique where the changes made by a transaction are not written to the database until the transaction commits. This technique ensures atomicity but not durability, as the changes may be lost if a failure occurs before the commit.
  - Immediate update: A technique where the changes made by a transaction are written to the database as soon as they occur, even before the transaction commits. This technique ensures durability but not atomicity, as the changes may be inconsistent if a failure occurs before the commit.
  - Shadow paging: A technique where the changes made by a transaction are written to a copy of the database pages, called shadow pages, instead of the original pages. The original pages are replaced by the shadow pages only when the transaction commits. This technique ensures atomicity and durability, but requires extra space and may cause fragmentation.
  - Log-based recovery: A technique where the changes made by a transaction are recorded in a separate file, called a log, along with a unique transaction identifier, a timestamp, and a commit or abort flag. The log is used to redo or undo the changes in case of a failure. This technique can be combined with deferred or immediate update methods. There are two types of log-based recovery:
    - Undo logging: A type of log-based recovery where the log records the old values of the data items before they are modified by a transaction. The log is used to undo the changes of uncommitted transactions in case of a failure.
    - Redo logging: A type of log-based recovery where the log records the new values of the data items after they are modified by a transaction. The log is used to redo the changes of committed transactions in case of a failure.
  - Checkpointing: A technique where the database system periodically writes all the modified pages and the log records to the disk and marks a point in the log, called a checkpoint, that indicates the state of the database at that time. Checkpointing reduces the amount of work needed for recovery, as the system only needs to consider the transactions that occurred after the last checkpoint.



# Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique used to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A transaction log contains the following information  :
  - The transaction identifier (Tn)
  - The type of operation (read, write, commit, abort, etc.)
  - The data item name and value before and after the operation
  - The timestamp of the operation
- A log file is created for every operation performed on the database and stored in a stable storage device .
- The log file is used to restore the database to a consistent state by applying the undo and redo operations .
- Undo operations are used to roll back the changes made by uncommitted transactions .
- Redo operations are used to reapply the changes made by committed transactions that may not have been reflected in the database due to the failure .
- There are two types of log based recovery techniques :
  - Deferred update technique: In this technique, the changes made by a transaction are not written to the database until the transaction commits. Only the log file is updated during the execution of the transaction. This technique avoids the need for undo operations, but requires redo operations for committed transactions.
  - Immediate update technique: In this technique, the changes made by a transaction are written to the database as soon as they occur, even before the transaction commits. Both the log file and the database are updated during the execution of the transaction. This technique requires both undo and redo operations for uncommitted and committed transactions, respectively.



# Checkpoints for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A transaction is a logical unit of work that represents a real-world event of data processing.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either executes all or none of its operations.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it is the only one in the system, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.
- A transaction can have one of the following states: active, partially committed, committed, failed, or aborted.
- A transaction begins in the active state, where it executes its operations.
- A transaction enters the partially committed state when it executes its last operation.
- A transaction enters the committed state when it successfully completes and its changes are recorded in the database.
- A transaction enters the failed state when it encounters an error or aborts due to some reason.
- A transaction enters the aborted state when it is rolled back and its changes are undone from the database.
- A transaction can be aborted by the user, the system, or the concurrency control mechanism.
- A transaction can be rolled back by using undo and redo operations, which are based on the transaction log.
- A transaction log is a file that records all the changes made by the transactions in the database.
- A transaction log contains entries for each operation, such as start, read, write, commit, abort, etc.
- A transaction log also contains information such as transaction id, timestamp, old value, new value, etc.
- A transaction log is used for recovery purposes, to restore the database to a consistent state after a failure.
- A transaction log can be implemented using different techniques, such as deferred update, immediate update, shadow paging, etc.
- A transaction can be executed in different modes, such as serial, concurrent, or interleaved.
- A serial execution is one where transactions are executed one after another, without any overlap.
- A concurrent execution is one where transactions are executed simultaneously, with some overlap.
- An interleaved execution is one where transactions are executed in a mixed order, with some operations of one transaction followed by some operations of another transaction, and so on.
- A concurrent execution can improve the performance and throughput of the system, but it can also cause some problems, such as lost update, uncommitted dependency, inconsistent analysis, and phantom reads.
- A lost update occurs when two transactions update the same data item and one of them overwrites the changes of the other.
- An uncommitted dependency occurs when one transaction reads a data item that has been updated by another transaction, but not yet committed.
- An inconsistent analysis occurs when one transaction reads several data items that have been updated by another transaction, but not all at the same time.
- A phantom read occurs when one transaction reads a set of data items that satisfy some condition, and another transaction inserts or deletes some data items that affect the condition, causing the first transaction to see different results when it repeats the read operation.
- To prevent or resolve these problems, a concurrency control mechanism is needed, which ensures that the concurrent execution of transactions is equivalent to some serial execution.
- A concurrency control mechanism can be based on different techniques, such as locking, timestamping, validation, or multiversioning.
- A locking technique is one where transactions acquire locks on the data items they access, and release them when they are done.
- A lock is a variable that indicates the status of a data item, such as available, locked, shared, or exclusive.
- A lock can be granted or denied to a transaction, depending on the compatibility of the lock modes and the lock state.
- A lock can be applied at different levels of granularity, such as database, table, page, record, or field.
- A locking technique can be classified into different types, such as binary, shared, exclusive, or multiple.
- A binary locking technique is one where a lock can have only two modes: locked or unlocked.
- A shared locking technique is one where a lock can have two modes: shared or exclusive.
- An exclusive locking technique is one where a lock can have only one mode: exclusive.
- A multiple locking technique is one where a lock can have multiple modes, such as read, write, or intention.
- A locking technique can also be classified into different protocols, such as two-phase locking, conservative locking, strict locking, or rigorous locking.
- A two-phase locking protocol is one where a transaction acquires all the locks it needs before releasing any lock.
- A conservative locking protocol is one where



# Deadlock Handling

A deadlock is an unwanted situation in which two or more transactions are waiting indefinitely for one another to give up locks or resources that they need to complete their operations. Deadlocks can cause the whole system to halt or slow down significantly. Therefore, deadlock handling is an important aspect of transaction processing in a database management system (DBMS).

There are three main approaches for deadlock handling in a DBMS   :

- **Deadlock prevention**: This approach aims to prevent deadlocks from occurring in the first place by imposing some constraints on how transactions can acquire and release locks or resources. For example, a transaction may be required to request all the locks it needs before starting its execution, or to release all the locks it holds before requesting a new one. These constraints may reduce the concurrency and performance of the system, but they ensure that deadlocks are impossible.

- **Deadlock avoidance**: This approach allows transactions to request locks or resources dynamically, but it uses some information about the current and future requests of the transactions to determine whether granting a request would lead to a deadlock or not. If granting a request would result in a deadlock, the request is denied and the transaction is delayed until it is safe to proceed. For example, a DBMS may use a wait-for graph to track the dependencies among transactions, or a banker's algorithm to allocate resources based on the available and required resources of each transaction. These methods may require additional overhead and complexity, but they can avoid deadlocks without sacrificing too much concurrency.

- **Deadlock detection and recovery**: This approach does not try to prevent or avoid deadlocks, but rather detects them after they occur and recovers from them by aborting or rolling back some of the transactions involved in the deadlock. For example, a DBMS may periodically run a deadlock detection algorithm that scans the wait-for graph or the lock table to identify cycles of waiting transactions, or it may use a timeout mechanism that aborts a transaction if it waits for a lock or a resource for too long. These methods may allow more concurrency and flexibility, but they may also incur more cost and waste in terms of aborted transactions and lost work.



# Distributed Database

A distributed database is a collection of databases that are physically stored on different network hosts and logically appear as a single database to the user. A distributed database can improve performance, reliability, availability, and scalability of data management.

# Transaction Processing Concept

A transaction is a logical unit of work that consists of one or more database operations, such as queries, updates, or inserts. A transaction has the following properties:

- Atomicity: A transaction must either complete all of its operations or none of them.
- Consistency: A transaction must preserve the consistency of the database state by obeying the integrity constraints.
- Isolation: A transaction must not interfere with other concurrent transactions. Each transaction should execute as if it is the only one in the system.
- Durability: A transaction must ensure that the changes it made to the database persist even in the case of system failures.

## Distributed Transaction

A distributed transaction is a transaction that involves two or more network hosts that provide transactional resources, such as databases, message queues, or files. A distributed transaction requires a transaction manager that is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources. A distributed transaction must also satisfy the ACID properties, but it faces additional challenges, such as:

- Network failures: The communication between the hosts may be disrupted or delayed, causing the transaction to fail or become in-doubt.
- Host failures: One or more hosts may crash or become unavailable, causing the transaction to fail or become in-doubt.
- Data inconsistency: The data on different hosts may be inconsistent or outdated, causing the transaction to violate the integrity constraints or produce incorrect results.
- Concurrency control: The transaction must coordinate with other concurrent transactions on different hosts to ensure the isolation and consistency of the data.
- Deadlocks: The transaction may encounter circular dependencies on the locks or resources on different hosts, causing the transaction to wait indefinitely or abort.

## Two-Phase Commit Protocol

The two-phase commit protocol is a common technique for ensuring the atomicity and durability of distributed transactions. The protocol involves two phases:

- Prepare phase: The transaction manager asks each host involved in the transaction to prepare to commit or abort the transaction. Each host executes the operations of the transaction and locks the resources involved. If the host is ready to commit, it sends a prepared message to the transaction manager. If the host encounters any error or failure, it sends an abort message to the transaction manager and releases the locks.
- Commit phase: The transaction manager decides whether to commit or abort the transaction based on the messages received from the hosts. If all the hosts are prepared, the transaction manager sends a commit message to each host and commits the transaction. If any host has aborted, the transaction manager sends an abort message to each host and aborts the transaction. Each host then releases the locks and acknowledges the transaction manager.

The two-phase commit protocol ensures that either all the hosts commit the transaction or none of them do. However, the protocol also has some drawbacks, such as:

- Blocking: The protocol blocks the hosts from executing other transactions until the transaction manager decides the outcome of the transaction. This reduces the concurrency and availability of the system.
- In-doubt transactions: If the transaction manager or any host fails or loses communication during the protocol, the transaction may become in-doubt, meaning that its outcome is unknown. The in-doubt transactions may hold the locks and resources indefinitely, causing other transactions to wait or fail. The in-doubt transactions must be resolved manually or automatically by using a timeout mechanism or a voting protocol.
- Single point of failure: The transaction manager is a critical component of the protocol. If the transaction manager fails, the protocol cannot proceed and the transactions may become in-doubt. The transaction manager must be reliable and fault-tolerant to avoid this problem.



# Distributed Data Storage

- Distributed data storage is a system that stores and processes data on multiple machines, often in a replicated fashion .
- Distributed data storage can provide benefits such as scalability, availability, fault tolerance, performance, and cost efficiency .
- Distributed data storage can also pose challenges such as consistency, concurrency, partitioning, replication, and security .
- Distributed data storage can be classified into different types based on the data model, the access method, the consistency model, and the replication strategy .
- Some examples of distributed data storage are:
  - Distributed file systems, such as Hadoop Distributed File System (HDFS), which store large volumes of unstructured or semi-structured data across multiple nodes.
  - Distributed databases, such as MongoDB, which store structured or semi-structured data across multiple nodes and support various query languages.
  - Distributed object storage, such as Amazon S3, which store binary objects with metadata across multiple nodes and support RESTful APIs .
  - Distributed key-value stores, such as Redis, which store simple key-value pairs across multiple nodes and support fast and scalable operations.
  - Distributed columnar stores, such as Cassandra, which store data in a tabular format with flexible schema across multiple nodes and support high availability and scalability.
  - Distributed graph stores, such as Neo4j, which store data in a graph structure with nodes and edges across multiple nodes and support complex queries and analytics.



# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

The main objectives of concurrency control are:

- To ensure the **isolation** of transactions, that is, to prevent interference or conflicts between concurrent transactions.
- To resolve **read-write** and **write-write** conflicts, that is, to handle situations where one transaction reads or writes data that is concurrently modified by another transaction.
- To preserve **database consistency**, that is, to ensure that the database state remains valid after the execution of concurrent transactions.

Some of the benefits of concurrency control are:

- It improves the **throughput** of the system, that is, the number of transactions that can be completed in a given time.
- It reduces the **waiting time** of the transactions, that is, the time that a transaction spends in a ready state before getting the system resources to execute.
- It enhances the **availability** of the data, that is, the degree to which the data can be accessed by the transactions.

Some of the challenges of concurrency control are:

- It introduces **overhead** to the system, that is, the extra work or resources that are required to implement concurrency control mechanisms.
- It may cause **deadlocks**, that is, situations where two or more transactions are waiting for each other to release the resources they hold.
- It may affect the **serializability** of the transactions, that is, the equivalence of the concurrent execution of transactions to some serial execution.

There are two main types of concurrency control methods in DBMS:

- **Lock-based** protocols, which use locks to grant or deny access to data items by the transactions. A lock is a mechanism that allows a transaction to claim exclusive or shared control over a data item. Lock-based protocols can be classified into binary, shared/exclusive, and multiple granularity locking protocols.
- **Timestamp-based** protocols, which use timestamps to order the transactions and determine their validity. A timestamp is a unique identifier that reflects the relative starting time of a transaction. Timestamp-based protocols can be classified into basic, Thomas's write rule, and multiversion timestamp ordering protocols.

Other types of concurrency control methods in DBMS include:

- **Validation-based** protocols, which use a validation phase to check the consistency of the transactions before committing them. A validation phase is a process that verifies whether a transaction has violated any concurrency control rules or not. Validation-based protocols can be classified into basic, optimistic, and pessimistic protocols.
- **Snapshot** protocols, which use snapshots or versions of the data to allow concurrent read operations without locking. A snapshot or a version is a copy of the data at a certain point in time. Snapshot protocols can be classified into snapshot isolation, multiversion concurrency control, and snapshot serializability protocols.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 4 - Transaction Processing Concept in the subject of Database Management System. Here is a possible directory system for the notes of this unit:

# Unit 4 - Transaction Processing Concept

- ## Introduction
  - What is a transaction?
  - Properties of transactions (ACID)
  - Examples of transactions
- ## Concurrency Control
  - Why is concurrency control needed?
  - Problems of concurrent transactions (lost update, dirty read, unrepeatable read, phantom read)
  - Serializability and conflict serializability
  - Concurrency control techniques (locking, timestamping, validation, multiversion)
- ## Recovery Management
  - Why is recovery management needed?
  - Types of failures (transaction, system, media)
  - Recovery techniques (deferred update, immediate update, shadow paging, log-based recovery)
  - Checkpoints and fuzzy checkpoints
- ## Distributed Transactions
  - What is a distributed transaction?
  - Advantages and disadvantages of distributed transactions
  - Distributed concurrency control (two-phase locking, timestamp ordering, optimistic concurrency control)
  - Distributed recovery (two-phase commit, three-phase commit, presumed abort/commit, nested transactions)



# Unit 5 - Concurrency Control Techniques

- Concurrency control is the process of managing simultaneous operations on a shared database without compromising data integrity, consistency, and isolation.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by concurrent transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and timestamp-based methods.
- The choice of concurrency control technique depends on several factors, such as the degree of conflict, the overhead of locking and validation, the performance and scalability requirements, and the application characteristics.



# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases .

Concurrency control in DBMS is a procedure of managing simultaneous operations without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the respective database.

The advantages of a concurrent system are:

- Waiting Time: It means if a process is in a ready state but still the process does not get the system to get execute is called waiting time. Concurrency reduces the waiting time of processes.
- CPU Utilization: It means how much CPU is busy in executing processes. Concurrency increases the CPU utilization by allowing multiple processes to use the CPU.
- Throughput: It means how many processes are completed in a unit time. Concurrency increases the throughput by increasing the number of transactions that can be processed in a given time.

The challenges of a concurrent system are:

- Lost Update: It occurs when two transactions that access the same database items have their operations interleaved in a way that makes the value of some database item incorrect.
- Uncommitted Dependency: It occurs when a transaction reads a data item that has been written by another transaction that has not yet committed, and then the second transaction aborts, leaving the first transaction with an incorrect value.
- Inconsistent Analysis: It occurs when a transaction reads several data items and performs some analysis based on their values, but another transaction updates some of these data items in between, making the analysis invalid.
- Deadlock: It occurs when two or more transactions are waiting for each other to release the locks they hold on the data items, resulting in a circular wait.

The methods of concurrency control in DBMS are:

- Lock-Based Protocols: These protocols use locks to prevent multiple transactions from accessing the same data item concurrently. Locks can be shared or exclusive, and can be granted or denied by a lock manager. Lock-based protocols ensure serializability, but may cause deadlocks.
- Timestamp-Based Protocols: These protocols use timestamps to order the transactions and determine their precedence. Each transaction is assigned a unique timestamp when it starts, and each data item has a read timestamp and a write timestamp to record the last transaction that read or wrote it. Timestamp-based protocols ensure serializability and avoid deadlocks, but may cause more aborts.
- Validation-Based Protocols: These protocols use a validation phase to check whether the transactions can be serialized based on their read and write sets. Each transaction is divided into three phases: read phase, validation phase, and write phase. Validation-based protocols ensure serializability and avoid deadlocks, but may cause more delays.



# Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures data consistency and prevents data anomalies such as lost updates, dirty reads, unrepeatable reads, and phantom reads.

One of the most common concurrency control techniques is locking, which involves applying locks to data items that are accessed by transactions. Locks can be either shared or exclusive, depending on the type of access required by the transaction. Shared locks allow multiple transactions to read the same data item, but prevent any transaction from writing to it. Exclusive locks allow only one transaction to write to a data item, but prevent any other transaction from reading or writing to it.

Locking techniques can be classified into two categories: binary locking and multiple-mode locking. Binary locking only allows two lock modes: shared and exclusive. Multiple-mode locking allows more than two lock modes, such as read, write, and intention locks. Intention locks are used to indicate the intention of a transaction to acquire a lock on a lower level of granularity, such as a record or a field.

Locking techniques can also be classified based on the timing of lock acquisition and release. The most common timing-based locking techniques are:

- Two-phase locking (2PL): A transaction acquires all the locks it needs before it releases any lock. 2PL ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions. 2PL has two phases: growing phase and shrinking phase. In the growing phase, the transaction can only acquire locks, but not release any. In the shrinking phase, the transaction can only release locks, but not acquire any.
- Strict two-phase locking (S2PL): A transaction acquires all the locks it needs before it releases any lock, and it holds all its exclusive locks until it commits or aborts. S2PL ensures strictness, which means that no transaction can read or write a data item that has been written by another transaction that has not yet committed. Strictness prevents dirty reads and cascading aborts, which are situations where a transaction has to abort because it read a data item that was later modified by another aborted transaction.
- Rigorous two-phase locking (R2PL): A transaction acquires all the locks it needs before it releases any lock, and it holds all its locks until it commits or aborts. R2PL ensures recoverability, which means that no transaction can commit until all the transactions that have written data items that it has read have committed. Recoverability prevents lost updates, which are situations where a transaction overwrites a data item that was modified by another transaction that has not yet committed.

Locking techniques are implemented by a subsystem called the lock manager, which maintains a lock table that records the locks held by each transaction and the lock mode of each lock. The lock manager also enforces a lock compatibility matrix that determines which lock modes are compatible with each other. For example, in binary locking, a shared lock is compatible with another shared lock, but not with an exclusive lock. The lock manager grants or denies lock requests from transactions based on the lock compatibility matrix and the lock table.



# Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability.
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be either the system time or a logical counter.
- The basic idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamps to determine the precedence and compatibility of conflicting operations.
- There are two types of time stamping protocols: optimistic and pessimistic.

## Optimistic Time Stamping Protocols

- Optimistic time stamping protocols assume that conflicts are rare and allow transactions to execute without any checks until they are ready to commit.
- At commit time, each transaction is validated to ensure that it does not violate the serializability order based on the timestamps.
- If a transaction passes the validation, it is committed and its effects are made permanent. If a transaction fails the validation, it is aborted and restarted with a new timestamp.
- There are different ways to perform the validation, such as Thomas' write rule, basic timestamp ordering, and multiversion timestamp ordering.

## Pessimistic Time Stamp Ordering Protocols

- Pessimistic time stamp ordering protocols assume that conflicts are frequent and check the compatibility of each operation before it is executed.
- Each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS), which record the latest time when the item was read or written, respectively.
- Each transaction has a timestamp (TS) that is assigned when it enters the system and remains unchanged throughout its execution.
- Before a transaction can read or write a data item, it has to compare its timestamp with the timestamps of the data item and follow some rules to ensure serializability.
- The rules are:

  - A transaction T can read a data item X if TS(T) >= WTS(X), meaning that T is not reading an obsolete value of X. If the condition is true, T performs the read and sets RTS(X) to max(RTS(X), TS(T)).
  - A transaction T can write a data item X if TS(T) > WTS(X) and TS(T) > RTS(X), meaning that T is not overwriting a newer value of X or violating a previous read of X. If the condition is true, T performs the write and sets WTS(X) to TS(T).
  - If either condition is false, T is rejected and aborted.

- Pessimistic time stamp ordering protocols guarantee conflict serializability, but may cause unnecessary aborts and reduce concurrency.



# Validation Based Protocol

- Validation Based Protocol is a type of concurrency control technique that works on the validation rules and timestamps .
- It is also called Optimistic Concurrency Control Technique because it assumes that very few conflicts occur among transactions .
- It does not check for conflicts while the transaction is executing, but only at the end of the transaction .
- It divides the transaction into three phases: read phase, validation phase, and write phase  .

## Read Phase
- In the read phase, the transaction can read data values from the database, but it can only write or update the local copies of the data, not the actual database .
- The transaction also records the timestamps of the data items it reads, which are used later for validation .

## Validation Phase
- In the validation phase, the transaction checks whether it has any conflicts with other transactions that have already committed  .
- A conflict occurs when two transactions access the same data item and at least one of them performs a write operation .
- The validation phase uses the timestamps of the transactions and the data items to detect conflicts  .
- There are different validation rules that can be applied, such as basic timestamp ordering, Thomas' write rule, and multiversion timestamp ordering .
- If the transaction passes the validation phase, it can proceed to the write phase. Otherwise, it is aborted and restarted  .

## Write Phase
- In the write phase, the transaction writes or updates the actual database with the local copies of the data .
- The transaction also commits and releases any locks it may have acquired  .
- The write phase is performed only after the validation phase is successful  .

## Advantages and Disadvantages of Validation Based Protocol
- Some advantages of validation based protocol are :
  - It avoids locking overhead and deadlock problems.
  - It allows more concurrency among transactions as they do not block each other during execution.
  - It is suitable for applications where conflicts are rare and transactions are short-lived.
- Some disadvantages of validation based protocol are :
  - It may waste resources and time by executing transactions that may fail the validation phase.
  - It may cause cascading aborts if a transaction that has validated successfully is aborted later due to some reason.
  - It may not be suitable for applications where conflicts are frequent and transactions are long-lived.



# Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- There are three types of lock granularity:
  - Fine granularity: It locks the smallest data items such as records or fields. It provides high concurrency but also high locking overhead.
  - Coarse granularity: It locks the largest data items such as files or tables. It provides low concurrency but also low locking overhead.
  - Medium granularity: It locks the intermediate data items such as pages or blocks. It provides a balance between concurrency and locking overhead.
- Multiple granularity locking protocol uses a tree structure to represent the hierarchy of data granularities and the compatibility matrix to determine the lock modes that can be applied on each node .
- The tree structure consists of four levels of nodes:
  - Database (D): The root node that represents the entire database.
  - File (F): The child nodes of D that represent the files in the database.
  - Page (P): The child nodes of F that represent the pages in the files.
  - Record (R): The child nodes of P that represent the records in the pages.
- The compatibility matrix defines six lock modes that can be applied on each node :
  - Shared (S): Allows read access to the node and its descendants.
  - Exclusive (X): Allows read and write access to the node and its descendants.
  - Intention Shared (IS): Indicates the intention to lock some of the descendants of the node in S mode.
  - Intention Exclusive (IX): Indicates the intention to lock some of the descendants of the node in X mode.
  - Shared and Intention Exclusive (SIX): Allows read access to the node and indicates the intention to lock some of the descendants of the node in X mode.
  - No lock (NL): No access to the node or its descendants.
- The compatibility function determines whether a transaction can lock a node in a given mode based on the existing locks on the node by other transactions. The function is shown in the table below:

|       | NL | IS | IX | S  | SIX | X  |
| ----- | -- | -- | -- | -- | --- | -- |
| NL    | Y  | Y  | Y  | Y  | Y   | Y  |
| IS    | Y  | Y  | Y  | Y  | Y   | N  |
| IX    | Y  | Y  | Y  | N  | N   | N  |
| S     | Y  | Y  | N  | Y  | N   | N  |
| SIX   | Y  | Y  | N  | N  | N   | N  |
| X     | Y  | N  | N  | N  | N   | N  |

- Y means compatible and N means incompatible.
- Multiple granularity locking protocol follows these rules:
  - Lock the root node of the tree first, in any mode.
  - Node Q can be locked by transaction T in S or IS mode only if the parent of Q is locked by T in IX or IS mode.
  - Node Q can be locked by transaction T in X, SIX, or IX mode only if the parent of Q is locked by T in IX or SIX mode.
  - Transaction T is two-phase, meaning it acquires all the locks before releasing any lock.
  - Transaction T can unlock node Q only if none of Q's descendants are locked by T.



# Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data objects to coexist in the database.
- The main idea is to grant an appropriate version of a data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read operations do not block write operations, and vice versa, and the database can support a high level of concurrency.
- The advantages of multi version schemes are:
  - They reduce the number of conflicts and aborts among transactions.
  - They improve the performance and throughput of the database system.
  - They preserve the consistency and integrity of the database.
- The disadvantages of multi version schemes are:
  - They require more storage space and overhead to maintain multiple versions of data objects.
  - They may introduce complexity and overhead in the version management and garbage collection.
  - They may cause anomalies such as phantom reads and non-repeatable reads if the isolation level is not high enough.

- There are different ways to implement multi version schemes, such as:
  - Timestamp ordering: Each version of a data object is assigned a timestamp based on the transaction that created or modified it. Read requests are granted the latest version of the data object that is older than or equal to their timestamp. Write requests are allowed only if their timestamp is greater than the timestamp of the latest version of the data object.
  - Validation: Each transaction is divided into three phases: read, validation, and write. In the read phase, the transaction reads the versions of the data objects that are consistent with its start time. In the validation phase, the transaction checks if its read set is still valid, i.e., no other transaction has modified the data objects that it read. If the validation succeeds, the transaction proceeds to the write phase, where it writes new versions of the data objects that it modified. Otherwise, the transaction is aborted and restarted.
  - Snapshot isolation: Each transaction sees a snapshot of the database as of its start time, i.e., the versions of the data objects that were committed before the transaction began. Read requests are granted the versions of the data objects from the snapshot. Write requests are allowed only if the data objects that they modify have not been modified by any other concurrent transaction. Otherwise, the transaction is aborted and restarted.



# Recovery with Concurrent Transaction

- Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions executing simultaneously.
- Recovery with concurrent transaction is necessary to ensure the ACID properties of transactions, especially atomicity and durability.
- Recovery with concurrent transaction is challenging because of the interleaving of logs from different transactions, which makes it difficult to backtrack and undo or redo the operations.
- Recovery with concurrent transaction can be done in the following four ways:

  - Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if locking is used, then the recovery scheme can use the lock table to identify the transactions that were active at the time of failure and roll them back. If timestamp ordering is used, then the recovery scheme can use the timestamps to order the logs and apply the undo or redo operations accordingly.
  - Transaction rollback: In this scheme, the recovery scheme can abort a transaction and undo its effects if it detects a conflict or a failure. For example, if a transaction violates a serializability condition or a validation test, then the recovery scheme can roll it back and release its locks or resources. Transaction rollback can be done by using the undo operation on the logs of the aborted transaction in reverse order.
  - Checkpoints: In this scheme, the recovery scheme can periodically take a snapshot of the database and the logs and write them to the disk. A checkpoint is a point in time when the database is in a consistent state and all the transactions that have committed before the checkpoint have their effects reflected in the database. A checkpoint can reduce the amount of work that the recovery scheme has to do after a failure, as it only has to consider the transactions that were active after the checkpoint. Checkpoints can be done by using the flush operation on the database and the logs.
  - Restart recovery: In this scheme, the recovery scheme can use the checkpoints and the logs to restore the database to a consistent state after a failure. Restart recovery can be done by using the undo and redo operations on the logs of the transactions that were active after the checkpoint. The undo operation can roll back the transactions that were not committed at the time of failure, and the redo operation can reapply the effects of the transactions that were committed but not reflected in the database. Restart recovery can ensure that the database is in a consistent and durable state after a failure.



# Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Oracle is a popular relational database management system that supports concurrent access of data by multiple users and transactions.
- Oracle uses a multiversion concurrency control (MVCC) technique to provide read consistency and isolation levels for queries and transactions.
- Oracle also uses various types of locks to ensure data integrity and prevent conflicts among concurrent updates of the same data.

## Multiversion Concurrency Control

- MVCC is a technique that allows each user to see a consistent snapshot of the database as of a single point in time, regardless of the changes made by other users.
- MVCC avoids locking read operations and reduces the need for locking write operations, thus improving performance and concurrency.
- Oracle implements MVCC by using undo segments, which store the old versions of the data before they are modified by transactions.
- Oracle assigns each transaction a unique system change number (SCN), which is a logical timestamp that indicates the start time of the transaction.
- Oracle also assigns each data block a SCN, which indicates the last time the block was modified.
- When a query is executed, Oracle determines the SCN of the query, which is the highest SCN among all the transactions that have committed at the time the query started.
- Oracle then reads the data blocks that have a SCN less than or equal to the query SCN, and applies the undo information if necessary to reconstruct the consistent snapshot of the data as of the query SCN.
- This ensures that the query sees a consistent view of the data, regardless of the changes made by other transactions after the query started.
- Oracle provides two levels of read consistency: statement-level and transaction-level.
- Statement-level read consistency means that each SQL statement in a transaction sees a consistent snapshot of the data as of the time the statement started.
- Transaction-level read consistency means that all the SQL statements in a transaction see a consistent snapshot of the data as of the time the first statement in the transaction started.
- Oracle always enforces statement-level read consistency, and can optionally provide transaction-level read consistency by setting the isolation level to SERIALIZABLE.

## Locking Mechanisms

- Locking is a technique that prevents concurrent transactions from accessing or modifying the same data in a conflicting way.
- Locking ensures data integrity and consistency, and prevents phenomena such as lost updates, dirty reads, non-repeatable reads, and phantom reads.
- Oracle uses two types of locks: data locks and dictionary locks.
- Data locks are used to protect the data in the database from concurrent modifications. Data locks can be either exclusive or shared.
- Exclusive locks are acquired by transactions that modify data, such as INSERT, UPDATE, or DELETE statements. Exclusive locks prevent other transactions from modifying or locking the same data until the lock is released.
- Shared locks are acquired by transactions that query data, such as SELECT statements. Shared locks allow other transactions to query or lock the same data in shared mode, but prevent them from modifying or locking the data in exclusive mode until the lock is released.
- Oracle automatically acquires and releases data locks as needed, and does not require explicit locking commands from the user.
- Dictionary locks are used to protect the data dictionary, which stores the metadata of the database, such as the definitions of tables, indexes, views, etc. Dictionary locks can be either exclusive or shared.
- Exclusive locks are acquired by transactions that modify the data dictionary, such as CREATE, ALTER, or DROP statements. Exclusive locks prevent other transactions from accessing or modifying the same data dictionary object until the lock is released.
- Shared locks are acquired by transactions that access the data dictionary, such as queries that use the data dictionary views. Shared locks allow other transactions to access the same data dictionary object in shared mode, but prevent them from modifying or locking the object in exclusive mode until the lock is released.
- Oracle automatically acquires and releases dictionary locks as needed, and does not require explicit locking commands from the user.

## Isolation Levels

- Isolation level is a property that determines the degree of isolation or concurrency among transactions.
- Isolation level affects the visibility of the changes made by other transactions, and the possibility of encountering concurrency-related phenomena, such as dirty reads, non-repeatable reads, and phantom reads.
- Oracle supports four isolation levels: READ COMMITTED, SERIALIZABLE, READ ONLY, and READ WRITE.
- READ COMMITTED is the default isolation level in Oracle. It means that each query in a transaction sees the data that was committed before the query started. It prevents dirty reads, but allows non-repeatable reads and phantom reads.
- SERIALIZABLE means that

