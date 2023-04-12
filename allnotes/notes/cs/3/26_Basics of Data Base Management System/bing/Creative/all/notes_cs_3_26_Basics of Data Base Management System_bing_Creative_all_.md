

## Unit 1 - Introduction

- In this unit, you will learn about the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be divided into two main branches: symbolic AI and sub-symbolic AI.
  - Symbolic AI is based on the idea of using symbols and rules to represent and manipulate knowledge. Examples of symbolic AI include expert systems, logic programming, and knowledge representation and reasoning.
  - Sub-symbolic AI is based on the idea of using numerical and statistical methods to model and simulate complex phenomena. Examples of sub-symbolic AI include neural networks, evolutionary algorithms, and fuzzy logic.
- AI can also be classified according to the level of intelligence and the type of task it can perform. Some common categories are:
  - Artificial narrow intelligence (ANI): AI that can perform a specific task or domain, such as playing chess, recognizing faces, or translating languages.
  - Artificial general intelligence (AGI): AI that can perform any intellectual task that a human can, such as understanding and reasoning about the world, learning from experience, and communicating with natural language.
  - Artificial superintelligence (ASI): AI that can surpass human intelligence in all aspects, such as creativity, wisdom, and social skills.
  - Reactive AI: AI that can respond to stimuli and situations without any memory or learning. Examples include simple reflex agents and finite state machines.
  - Limited memory AI: AI that can store and use some information from the past to improve its performance. Examples include learning agents and reinforcement learning.
  - Theory of mind AI: AI that can understand and model the mental states, emotions, and intentions of other agents. Examples include social robots and natural language understanding.
  - Self-aware AI: AI that can have a sense of self, consciousness, and self-improvement. Examples include artificial neural networks and artificial life.
- AI has many applications and benefits for various fields and domains, such as medicine, education, entertainment, business, and security. However, AI also poses some challenges and risks, such as ethical, social, and legal issues, such as privacy, bias, accountability, and human dignity.



# An overview of database management system

- A database management system (DBMS) is a software system that manages databases, which are collections of data organized in a structured way.
- A DBMS provides an interface for users and applications to perform various operations on the data, such as creating, reading, updating, deleting, querying, and analyzing.
- A DBMS also provides functions for data security, integrity, consistency, concurrency, backup, and recovery.
- A DBMS can support different types of databases, such as relational, hierarchical, network, object-oriented, document, graph, and NoSQL databases.
- A DBMS consists of several components, such as:
  - Storage engine: This component is responsible for storing and retrieving data from the physical storage devices, such as disks or memory.
  - Query processor: This component is responsible for parsing, optimizing, and executing queries on the data, using a query language, such as SQL.
  - Transaction manager: This component is responsible for ensuring that transactions, which are units of work that access and modify data, are executed in a correct and consistent manner, following the ACID properties (atomicity, consistency, isolation, and durability).
  - Metadata manager: This component is responsible for maintaining the metadata, which is data about the data, such as the schema, constraints, indexes, and statistics.
  - Buffer manager: This component is responsible for managing the buffer pool, which is a cache of data pages in memory, to improve the performance of data access.
  - Recovery manager: This component is responsible for recovering the database from failures, such as system crashes or power outages, by using techniques such as logging and checkpointing.
  - Security manager: This component is responsible for enforcing the security policies and rules on the data, such as authentication, authorization, encryption, and auditing.
- A DBMS can be classified into different categories, based on various criteria, such as:
  - Data model: This criterion refers to the way the data is structured and manipulated in the database, such as relational, hierarchical, network, object-oriented, document, graph, and NoSQL models.
  - Architecture: This criterion refers to the way the DBMS components are organized and distributed, such as centralized, client-server, peer-to-peer, or cloud-based architectures.
  - License: This criterion refers to the way the DBMS software is owned and distributed, such as proprietary, open-source, or freeware licenses.
  - Usage: This criterion refers to the way the DBMS software is used and specialized for different purposes, such as general-purpose, analytical, operational, or embedded DBMSs.



# Database System vs File System

- A **file system** is a software that organizes and manages files on a storage media, such as a hard disk or a flash drive. A file system provides basic operations such as creating, deleting, renaming, moving, and copying files and folders. A file system does not have any built-in mechanism for ensuring data consistency, security, integrity, or recovery in case of failures or errors .
- A **database management system (DBMS)** is a software that allows you to access, create, and administer databases. A database is a collection of structured data that is organized in tables, records, and fields. A DBMS provides advanced operations such as querying, updating, and manipulating data using a query language, such as SQL. A DBMS also has features for ensuring data consistency, security, integrity, and recovery in case of failures or errors  .
- A DBMS is generally better than a file system for most applications that involve storing and processing large amounts of data. Some of the advantages of using a DBMS over a file system are     :
  - **Data abstraction**: A DBMS hides the details of how the data is stored and accessed from the application, and provides a logical view of the data using a data model, such as the relational model. A file system exposes the physical structure and location of the files and folders to the application, and requires the application to handle the low-level details of reading and writing data.
  - **Data independence**: A DBMS allows you to change the structure or location of the data without affecting the application, as long as the logical view of the data remains the same. A file system requires you to modify the application if you change the structure or location of the files and folders.
  - **Data consistency**: A DBMS ensures that the data is consistent and valid according to the defined rules and constraints, such as primary keys, foreign keys, and integrity constraints. A file system does not have any mechanism for enforcing such rules and constraints, and relies on the application to ensure data consistency.
  - **Data security**: A DBMS provides features for controlling the access and permissions of the data, such as authentication, authorization, encryption, and auditing. A file system does not have any built-in features for data security, and depends on the operating system or the application to provide such features.
  - **Data recovery**: A DBMS provides features for recovering the data in case of failures or errors, such as transactions, logging, backup, and restore. A file system does not have any built-in features for data recovery, and requires the application to implement such features.
  - **Data manipulation**: A DBMS provides a query language, such as SQL, for manipulating the data in a declarative and expressive way. A file system requires the application to use a programming language, such as C or Java, for manipulating the data in an imperative and verbose way.
  - **Data sharing**: A DBMS allows multiple users and applications to access and update the data concurrently and efficiently, using features such as locking, concurrency control, and isolation levels. A file system does not have any mechanism for managing concurrent access to the data, and requires the application to handle the synchronization and coordination of the data access.
  - **Data performance**: A DBMS optimizes the performance of the data access and processing, using features such as indexing, caching, query optimization, and query execution plans. A file system does not have any features for optimizing the data performance, and relies on the application to implement such features.



# Database System Concepts and Architecture

- A database system is a software system that manages and manipulates data stored in a database.
- A database system consists of the following components:
  - A database, which is a collection of data organized in a logical manner.
  - A database management system (DBMS), which is a software system that provides the functionality to create, maintain, and manipulate the database.
  - A database application, which is a software program that interacts with the database through the DBMS to perform specific tasks.
  - A database user, which is a person or a software agent that accesses the database through the database application or directly through the DBMS.
- A database system can be classified according to its architecture, which is the way the components are distributed and communicate with each other.
- The main types of database system architectures are:
  - Centralized, where the database, the DBMS, and the database application run on a single computer system.
  - Client-server, where the database and the DBMS run on a server system, and the database application runs on one or more client systems that communicate with the server through a network.
  - Distributed, where the database is partitioned and replicated across multiple computer systems, and the DBMS and the database application run on each system or a subset of them.
- The database system architecture affects the performance, scalability, availability, reliability, security, and cost of the database system.



# Views of Data – Levels of Abstraction

- Views of data in DBMS describe the abstraction of data at three levels: physical, logical, and view level.
- Data abstraction is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data independence is the property that allows data at a certain level to be modified without affecting the data at higher levels.

## Physical Level

- The physical level of abstraction defines how data is stored in the storage and also reveals its access path.
- It is the lowest level of data abstraction and it tells us how the data is actually stored in memory.
- The access methods like sequential or random access and file organization methods like B+ trees and hashing are used for the same.
- The physical level is also called the internal level.

## Logical Level

- The logical level of abstraction defines what data is stored in the database and the relationships among the data.
- It is the middle level of data abstraction and it tells us what data is stored and how it is organized.
- The logical level is independent of the physical level and it can be represented by a conceptual diagram like an ER model.
- The logical level is also called the conceptual level.

## View Level

- The view level of abstraction describes the application which the users use to retrieve the information from the database.
- It is the highest level of data abstraction and it describes only a part of the database and hides some information to the user.
- At the view level, computer users see a set of application programs that hide details of data types.
- The view level is also called the external level.



# Data Models

A data model is a type of data model that determines the logical structure of a database. It fundamentally determines in which manner data can be stored, organized and manipulated. Data models are fundamental entities to introduce abstraction in a DBMS. Data models ensure consistency in naming conventions, default values, semantics, security while ensuring quality of the data.

There are different types of data models, such as:

- **Relational data model**: This type of model designs the data in the form of rows and columns within a table. Each row represents a record and each column represents an attribute. The tables are related to each other by using primary and foreign keys. This model is based on the mathematical concept of relation and is widely used in relational database management systems (RDBMS)  .
- **Entity-relationship data model**: This type of model is the logical representation of data as objects and relationships among them. An object can be an entity, which is a real-world thing with properties and behaviors, or an attribute, which is a property of an entity. A relationship is an association between two or more entities. This model is often used to design conceptual schemas and is represented by using diagrams  .
- **Object-based data model**: This type of model is an extension of the ER model with notions of functions, encapsulation, and object identity, as well. An object is a combination of data and methods that operate on the data. Objects can be organized into classes, which define the common properties and behaviors of a group of objects. Objects can also inherit properties and behaviors from other classes. This model is suitable for complex data structures and applications  .
- **Hierarchical data model**: This type of model represents one-to-many relationships in a treelike format. In this model, each record has one parent record and zero or more child records. The records are organized into a hierarchy based on their level of detail. This model is simple and efficient for accessing data, but it has limitations in expressing complex relationships and queries .
- **Network data model**: This type of model is similar to the hierarchical model, but it allows many-to-many relationships between records. In this model, each record can have multiple parent and child records. The records are connected by using pointers or links. This model is more flexible and expressive than the hierarchical model, but it is also more complex and difficult to maintain .
- **Dimensional data model**: This type of model is used for data analysis and reporting purposes. In this model, data is organized into facts and dimensions. A fact is a numerical measure of a business event, such as sales or revenue. A dimension is a descriptive attribute of a fact, such as time, location, or product. This model is represented by using a cube, where each side of the cube represents a dimension and the cells of the cube represent the facts .
- **Graph data model**: This type of model is used for representing complex and interconnected data, such as social networks, web pages, or biological data. In this model, data is represented by nodes and edges. A node is an entity with properties and labels. An edge is a relationship between two nodes with a direction and a type. This model is flexible and scalable for querying and analyzing data, but it requires specialized tools and techniques .



# Schema and Instances for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- A database is a collection of organized data that can be stored and managed in multiple databases using a software program called a database management system (DBMS)  .
- A database schema is an abstract design that represents the storage of data in a database. It describes both the organization of data and the relationships between tables in a given database  .
- A database schema is considered the "blueprint" of a database, which defines the structure, constraints, and operations that can be performed on the data .
- A database schema can be divided into three levels: external, conceptual, and internal  .
  - The external schema is the view of the database that is seen by a specific user or application. It defines what data and operations are relevant and accessible to them  .
  - The conceptual schema is the view of the database that is seen by the database administrator. It defines the logical structure and meaning of the data, without specifying the physical details of storage  .
  - The internal schema is the view of the database that is seen by the DBMS. It defines the physical representation and organization of the data, as well as the access methods and performance optimization techniques  .
- A database instance is a sample of data from a database at a single moment in time. It is the data stored in a database that satisfies the schema  .
- A database instance can change over time as data is inserted, updated, deleted, or queried by users or applications  .
- A database instance can be represented by a set of tables, each containing a set of rows and columns that store the values of the data  .
- A database instance can be identified by a unique name or identifier, and can be accessed by connecting to the DBMS using a specific username and password  .
- A database instance can be backed up, restored, copied, or migrated to another database or system  .



# Data Independence

Data independence is the property of a database management system (DBMS) that allows the database schema to be changed without affecting the application programs that use the database. Data independence is important for maintaining the consistency and integrity of the data, as well as for supporting multiple views of the data.

Data independence is of two types:

- **Physical data independence**: This is the ability to modify the physical schema of the database without affecting the logical schema or the external schema. The physical schema defines how the data is stored, organized, and accessed on the physical storage devices. For example, changing the file structure, indexing method, or storage location of the data does not affect the queries or operations that use the data.

- **Logical data independence**: This is the ability to modify the logical schema of the database without affecting the external schema or the application programs. The logical schema defines the structure and relationships of the data, such as tables, columns, keys, and constraints. For example, adding, deleting, or renaming a table or a column does not affect the views or reports that use the data.

Some benefits of data independence are:

- It reduces the complexity and cost of developing and maintaining the application programs, as they do not need to be modified or recompiled whenever the database schema changes.
- It enhances the flexibility and scalability of the database, as it can be adapted to changing requirements and new technologies without affecting the existing applications.
- It improves the security and privacy of the data, as different users can have different views of the data according to their access rights and needs.



# Database Languages and Interfaces

- Database languages are the means of communication between the users and the database management system (DBMS).
- Database interfaces are the tools or applications that allow the users to interact with the database using the database languages.
- The DBMS must provide appropriate languages and interfaces for each category of users, such as database administrators, application programmers, end users, etc.
- The types of languages and interfaces provided by a DBMS may vary depending on the functionality and the user category targeted by each interface.
- Some of the common types of database languages and interfaces are:

  - Data definition language (DDL): This is the language used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, etc. For example, SQL is a widely used DDL for relational databases.
  - Data manipulation language (DML): This is the language used to manipulate the data stored in the database, such as inserting, updating, deleting, or querying data. For example, SQL is also a DML for relational databases.
  - Data control language (DCL): This is the language used to control the access and security of the database, such as granting or revoking permissions, roles, or privileges to users or groups. For example, SQL is also a DCL for relational databases.
  - Transaction control language (TCL): This is the language used to manage the transactions in the database, such as committing, rolling back, or saving changes made by a transaction. For example, SQL is also a TCL for relational databases.
  - Menu-based interfaces: These are the interfaces that present the user with lists of options (called menus) that lead the user through the database operations. These interfaces are suitable for web clients or browsing.
  - Forms-based interfaces: These are the interfaces that display the data or allow the user to enter the data in predefined forms or templates. These interfaces are suitable for data entry or modification.
  - Graphical user interfaces (GUI): These are the interfaces that use graphical elements such as icons, buttons, menus, etc. to facilitate the user interaction with the database. These interfaces are suitable for visualizing or exploring the data.
  - Natural language interfaces: These are the interfaces that allow the user to communicate with the database using natural language, such as English, instead of formal database languages. These interfaces are suitable for casual or novice users.
  - Application program interfaces (API): These are the interfaces that allow the application programmers to access the database using predefined functions or methods in a programming language, such as Java, Python, etc. These interfaces are suitable for developing custom applications or integrating with other systems .



# Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects in a database.
- Database objects include tables, views, schemas, indexes, sequences, aliases, locations, and users.
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas.
- DDL is used to specify the properties and constraints of the data, such as data types, primary keys, foreign keys, and check conditions.
- DDL is also used to grant or revoke permissions and privileges to users or roles on database objects.
- Some common DDL commands are CREATE, ALTER, DROP, RENAME, and TRUNCATE.
- DDL is different from Data Manipulation Language (DML), which is used to insert, update, delete, and query data in a database.
- DDL is also different from Data Control Language (DCL), which is used to control the access and security of data in a database.
- DDL is a part of the Structured Query Language (SQL), which is a standard language for interacting with relational databases.
- DDL can be executed interactively or embedded in a program or script.



# DML for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

- DML stands for Data Manipulation Language    .
- It is one of the types of SQL queries  that are responsible for making any change in the data present in SQL databases .
- The DML commands in SQL are:
  - SELECT: retrieve data from one or more tables  .
  - INSERT: insert new data into a table  .
  - UPDATE: modify existing data in a table  .
  - DELETE: delete data from a table  .
  - MERGE: insert, update, or delete data based on a join condition.
- The DML commands are not auto-committed, which means that the changes made by them are not permanent to the database until they are explicitly committed by the user.
- The DML commands can be used with clauses such as WHERE, GROUP BY, HAVING, ORDER BY, etc. to filter, aggregate, or sort the data  .
- The DML commands can also be used with subqueries, joins, and views to perform complex operations on the data  .
- DML is different from DDL (Data Definition Language), which is used to create or modify the structure or the schema of the table   .
- DML is also different from DCL (Data Control Language), which is used to grant or revoke permissions or access rights to the data .



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Basics of Data Base Management System. Here is the overall database structure for the notes of the Unit 1 - Introduction:

# Overall Database Structure

- A database is a collection of related data that represents some aspect of the real world.
- A database management system (DBMS) is a software system that enables users to define, create, maintain, and control access to the database.
- A database system consists of four components: data, hardware, software, and users.
- Data is the actual information stored in the database, such as facts, figures, text, images, etc.
- Hardware is the physical devices that support the database system, such as disks, processors, memory, etc.
- Software is the set of programs that manage the database and provide various functions, such as data definition, data manipulation, data control, etc.
- Users are the people who interact with the database system, such as database administrators, application programmers, end users, etc.
- A database system can be classified into different types based on the data model, the logical structure of the data, such as relational, hierarchical, network, object-oriented, etc.
- A database system can also be classified into different types based on the distribution of the data, such as centralized, distributed, parallel, etc.
- A database system can also be classified into different types based on the usage of the data, such as operational, analytical, data warehouse, data mart, etc.



# Transaction Management in DBMS

- Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations.
- A transaction is a program unit whose execution may or may not change the contents of a database.
- Transactions are used to manage concurrency and ensure data integrity in a database.
- A transaction is a set of logically related operations, such as transferring money from one account to another, or booking a flight ticket.
- A transaction usually means that the data in the database has changed.
- A transaction has four main properties, also known as ACID properties:
  - Atomicity: A transaction is either completed in its entirety or not at all. If any part of the transaction fails, the whole transaction is aborted and the database is restored to its previous state  .
  - Consistency: A transaction must preserve the consistency of the database, meaning that it must follow the rules and constraints defined by the database schema  .
  - Isolation: A transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only one running on the database  .
  - Durability: A transaction must ensure that the changes made by it are permanent and persist even in the case of system failures or power outages  .
- Transaction management in a DBMS involves the following steps:
  - Begin transaction: The DBMS marks the start of a transaction and assigns a unique identifier to it.
  - Execute transaction: The DBMS executes the SQL statements that make up the transaction and records the changes in a temporary buffer.
  - Commit transaction: The DBMS verifies that the transaction has completed successfully and writes the changes to the database permanently.
  - Rollback transaction: The DBMS aborts the transaction and undoes the changes made by it in case of any failure or error.
- Transaction management in a DBMS also involves the following concepts:
  - Concurrency control: The DBMS ensures that multiple transactions can access the database simultaneously without violating the ACID properties.
  - Locking: The DBMS uses locks to prevent concurrent transactions from accessing the same data item at the same time.
  - Deadlock: The DBMS detects and resolves situations where two or more transactions are waiting for each other to release locks on the same data item.
  - Logging: The DBMS maintains a log of all the transactions and their actions on the database to facilitate recovery in case of system failures.
  - Recovery: The DBMS restores the database to a consistent state after a system failure by using the log and the ACID properties.



# Storage Management for the Notes of the Unit 1 - Introduction in the Subject of Basics of Database Management System

- Storage management is the method by which organizations ensure data integrity, access, policy/regulation compliance, and effective storage resource use.
- Storage management involves developing a plan to provision, configure, back up, and monitor data storage infrastructure to prevent data loss, performance slowdowns, and access problems.
- A database management system (DBMS) must store data persistently in files or datasets of some sort. Depending on the DBMS, table spaces and index spaces each may require one, or possibly more, files to store the actual data.
- A DBMS also uses primary devices for data storage, such as the CPU’s main memory, the CPU’s registers and otherwise known as the internal memory and the cache memory of the server that is accessible to the CPU for an uninterrupted data flow.
- Data storage system can be explained as the capacity secured by the database management system in the memory of the server allocated for the database and the related operations.
- Data storage management can offer numerous advantages, such as :
  - Reducing costs by optimizing storage utilization and eliminating unnecessary data duplication.
  - Improving performance by allocating data to the appropriate storage tiers and devices based on access frequency and latency requirements.
  - Enhancing security by encrypting data at rest and in transit, and applying access controls and audit trails.
  - Ensuring availability by implementing backup and recovery procedures, and replicating data across multiple locations.
  - Supporting compliance by retaining data according to retention policies and regulations, and disposing data securely when no longer needed.
  - Enabling analytics by providing better visibility into the data, and facilitating data extraction and transformation.



# Database Users and Administrator

Database users and administrator are the people who are accessing or working with the database. The primary aim of the database management system (DBMS) is to store the data or information and retrieve it whenever it is needed by the database users. There are different types of database users and administrator, depending on their roles and responsibilities. Here are some of the common types of database users and administrator:

- **Native Users**: These are the database users who are communicating with the database through an already written program. For example, when a student logs in to an online learning platform, the program will interact with the database to authenticate the student and display the relevant courses and materials. Native users do not need to know the details of the database or the query language. They just use the interface provided by the program.

- **Application Programmers**: These are the software developers and programming professionals who write the programs that access the database. They use a programming language such as Java, Python, C#, etc. and a query language such as SQL, NoSQL, etc. to manipulate the data in the database. They need to know the logical structure and schema of the database, as well as the syntax and semantics of the query language.

- **Casual Users**: These are the database users who occasionally access the database for some specific purpose. They may use a general-purpose query language such as SQL or a graphical user interface (GUI) to submit queries to the database. They do not need to be familiar with the database structure or the query language, but they need to know what information they want and how to formulate the query.

- **Sophisticated Users**: These are the database users who have a good knowledge of the database system and the query language. They can use the query language to perform complex and specialized operations on the database. They may also use some application programs to access the database, but they can also write their own queries and programs. They may be data analysts, data scientists, researchers, etc. who need to extract and analyze data from the database.

- **Database Administrator (DBA)**: Database administrator (DBA) is a person or a team who defines the schema and also controls the three levels of the database. The three levels are the physical level, the logical level, and the view level. The DBA is responsible for creating, maintaining, and securing the database. The DBA also grants and revokes permissions and privileges to other database users and administrator. The DBA has full control of the database and can use a superuser account to perform any operation on the database  .



## Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is the process of designing and documenting the structure and relationships of data in a database.
- The Entity Relationship Model (ER Model) is a graphical notation for representing data models using entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified uniquely and has some properties of interest. For example, a student, a course, or a department.
- An attribute is a property or characteristic of an entity that describes some aspect of it. For example, a student entity may have attributes such as name, ID, major, and GPA.
- A relationship is an association or link between two or more entities that expresses some semantic meaning or constraint. For example, a student entity may have a relationship with a course entity that indicates that the student is enrolled in the course.
- The ER Model can be represented using diagrams that show the entities, attributes, and relationships in a database schema. The diagrams use symbols such as rectangles, ovals, diamonds, and lines to denote different components of the model.
- The ER Model can be used to design and validate the logical structure of a database before implementing it in a specific database management system (DBMS).
- The ER Model can also be used to communicate and document the data requirements and design decisions of a database to various stakeholders, such as users, developers, and administrators.



# ER Model Concepts

The ER model is a conceptual data model that describes the data requirements of a system in terms of entities, attributes, relationships, and constraints. It is used to design and document the logical structure of a database. The ER model consists of the following concepts:

- **Entity**: An entity is a real-world object or thing that can be identified uniquely. For example, a student, a course, a book, etc. An entity has a set of properties or attributes that describe its characteristics. For example, a student entity may have attributes like name, roll number, age, etc.

- **Entity type**: An entity type is a collection of entities that share the same attributes. For example, student is an entity type that contains all the student entities in a database. An entity type is represented by a rectangle in an ER diagram.

- **Entity set**: An entity set is a subset of an entity type that contains the entities that participate in a particular relationship. For example, enrolled is an entity set that contains the student entities that are enrolled in a course.

- **Attribute**: An attribute is a property or characteristic of an entity or a relationship. For example, name, age, roll number, etc. are attributes of a student entity. An attribute is represented by an oval in an ER diagram.

- **Attribute domain**: An attribute domain is a set of possible values for an attribute. For example, the domain of the age attribute of a student entity may be the set of positive integers.

- **Key attribute**: A key attribute is an attribute that uniquely identifies an entity in an entity set. For example, roll number is a key attribute of a student entity. A key attribute is underlined in an ER diagram.

- **Composite attribute**: A composite attribute is an attribute that can be divided into sub-attributes. For example, name is a composite attribute that can be divided into first name, middle name, and last name. A composite attribute is represented by an oval with ovals inside it in an ER diagram.

- **Multivalued attribute**: A multivalued attribute is an attribute that can have more than one value for a given entity. For example, phone number is a multivalued attribute of a student entity, as a student may have more than one phone number. A multivalued attribute is represented by a double oval in an ER diagram.

- **Derived attribute**: A derived attribute is an attribute that can be derived from other attributes. For example, age is a derived attribute of a student entity, as it can be derived from the date of birth attribute. A derived attribute is represented by a dashed oval in an ER diagram.

- **Relationship**: A relationship is an association or link between two or more entities. For example, enrolled is a relationship between student and course entities, as it indicates which student is enrolled in which course. A relationship has a degree, which is the number of entity types involved in the relationship. For example, enrolled is a binary relationship, as it involves two entity types. A relationship is represented by a diamond in an ER diagram.

- **Relationship type**: A relationship type is a collection of relationships that share the same meaning and properties. For example, enrolled is a relationship type that contains all the enrolled relationships in a database. A relationship type is represented by a diamond with a name inside it in an ER diagram.

- **Relationship set**: A relationship set is a subset of a relationship type that contains the relationships that participate in a particular entity set. For example, enrolled is a relationship set that contains the enrolled relationships between the student and course entity sets.

- **Role**: A role is the function or purpose of an entity in a relationship. For example, in the enrolled relationship, student plays the role of enrollee and course plays the role of enrollee. A role is represented by a name near the entity type in an ER diagram.

- **Cardinality ratio**: A cardinality ratio is the number of entities that can be associated with another entity in a relationship. For example, in the enrolled relationship, the cardinality ratio of student to course is many-to-one, as a student can be enrolled in many courses, but a course can have only one student. A cardinality ratio is represented by a number or a symbol near the entity type in an ER diagram.

- **Participation constraint**: A participation constraint is a constraint that specifies whether the participation of an entity type in a relationship type is mandatory or optional. For example, in the enrolled relationship, the participation of student is mandatory, as every student must be enrolled in at least one course, but the participation of course is optional, as some courses may



# Notation for ER diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols that can be used to draw an ER diagram, depending on the level of detail and the type of database. Some of the common notations and symbols are:

- **Entity**: An entity is a real-world object or concept that can be identified and stored in the database. It is represented by a rectangle with the entity name inside. For example, Student, Course, Department, etc.

- **Attribute**: An attribute is a property or characteristic of an entity that can be used to describe or identify it. It is represented by an oval with the attribute name inside, connected to the entity by a line. For example, Name, ID, Age, etc. There are different types of attributes, such as:

  - **Simple attribute**: An attribute that cannot be divided into smaller parts. For example, Name, Age, etc.
  - **Composite attribute**: An attribute that can be divided into smaller parts. For example, Address, which can be composed of Street, City, State, etc.
  - **Single-valued attribute**: An attribute that can have only one value for each entity. For example, ID, Name, etc.
  - **Multi-valued attribute**: An attribute that can have more than one value for each entity. For example, Phone, Email, etc. It is represented by a double oval.
  - **Derived attribute**: An attribute that can be derived or calculated from other attributes. For example, Age, which can be derived from Date of Birth. It is represented by a dashed oval.

- **Relationship**: A relationship is an association or link between two or more entities that share some common information or interact with each other. It is represented by a diamond with the relationship name inside, connected to the entities by lines. For example, Enrolls, Teaches, Belongs to, etc. There are different types of relationships, such as:

  - **One-to-one relationship**: A relationship where each entity in one entity set is associated with at most one entity in another entity set. For example, each student has one advisor, and each advisor advises one student. It is represented by a single line between the entities.
  - **One-to-many relationship**: A relationship where each entity in one entity set is associated with zero or more entities in another entity set, but each entity in the other entity set is associated with at most one entity in the first entity set. For example, each department has many courses, but each course belongs to one department. It is represented by a single line on the side of the one entity and a crow's foot on the side of the many entity.
  - **Many-to-many relationship**: A relationship where each entity in one entity set is associated with zero or more entities in another entity set, and each entity in the other entity set is also associated with zero or more entities in the first entity set. For example, each student can enroll in many courses, and each course can have many students. It is represented by a crow's foot on both sides of the entities.

- **Cardinality**: Cardinality is the number of instances of one entity that can or must be associated with each instance of another entity. It is represented by a number or a symbol on the line connecting the entities. For example, 1, N, M, etc. There are different types of cardinality, such as:

  - **Minimum cardinality**: The minimum number of instances of one entity that must be associated with each instance of another entity. It is represented by a small circle for zero or a small line for one on the line near the entity. For example, a student must enroll in at least one course, so the minimum cardinality is one on the side of the course entity.
  - **Maximum cardinality**: The maximum number of instances of one entity that can be associated with each instance of another entity. It is represented by a number or a crow's foot for many on the line near the entity. For example, a student can enroll in at most four courses, so the maximum cardinality is four on the side of the course entity.

- **Participation**: Participation is the degree to which each entity is involved in a relationship. It can be either total or partial. Total participation means that every entity in an entity set must participate in the relationship, while partial participation means that some entities in an entity set may not participate in the relationship. It is represented by a double line for total



# Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Database Management System

Mapping constraints are also known as the cardinality ratio. They express the number of entities to which another entity can be related via a relationship set. They are useful in describing the relationship sets that involve more than two entity sets. There are two types of mapping constraints in the entity relationship model:

- Mapping cardinality or cardinality ratio: This corresponds to the number of relationship occurrences an entity can be involved in an entity relationship model. For binary relationship set R on an entity set A and B, there are four possible mapping cardinalities:

  - One to one: An entity in A is related to at most one entity in B, and an entity in B is related to at most one entity in A.
  - One to many: An entity in A is related to any number of entities in B, but an entity in B is related to at most one entity in A.
  - Many to one: An entity in A is related to at most one entity in B, but an entity in B is related to any number of entities in A.
  - Many to many: An entity in A is related to any number of entities in B, and an entity in B is related to any number of entities in A.

- Participation constraints: This specifies whether the existence of an entity depends on its being related to another entity via the relationship set. There are two types of participation constraints:

  - Total participation: Every entity in the entity set participates in at least one relationship in the relationship set. This is also called existence dependency.
  - Partial participation: Some entities in the entity set may not participate in any relationship in the relationship set. This is also called weak entity.



# Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical and conceptual tool for data modeling using entities, attributes, and relationships.
- Entities are the basic objects or concepts that are stored in a database, such as people, places, things, or events. Entities are represented by rectangles in an ER diagram.
- Attributes are the properties or characteristics of entities, such as name, age, address, or phone number. Attributes are represented by ovals in an ER diagram.
- Relationships are the associations or connections between entities, such as works for, owns, or studies. Relationships are represented by diamonds in an ER diagram.
- Cardinality is the number of instances of one entity that can or must be associated with each instance of another entity. Cardinality can be one-to-one, one-to-many, many-to-one, or many-to-many. Cardinality is shown by placing numbers or symbols near the relationship diamond in an ER diagram.
- Participation is the degree to which each entity is involved in a relationship. Participation can be total or partial. Total participation means that every instance of an entity must participate in the relationship, while partial participation means that some instances of an entity may not participate in the relationship. Participation is shown by placing a double line or a single line between the entity and the relationship in an ER diagram.
- Keys are the attributes or combinations of attributes that uniquely identify each instance of an entity. Keys can be primary, candidate, or foreign. Primary keys are the chosen keys that are used to refer to the entity instances, while candidate keys are the alternative keys that could have been chosen as primary keys. Foreign keys are the attributes of one entity that refer to the primary keys of another entity. Keys are shown by underlining the attribute names in an ER diagram.



# Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- A super key can also be NULL, which means that the attribute value is unknown or missing.
- A table can have more than one super key, but only one primary key, which is a chosen candidate key  .
- A super key can be used to enforce referential integrity, which means that the values of a foreign key in one table must match the values of a primary key or a unique key in another table.
- A super key can also be used to define functional dependencies, which means that the values of some attributes are determined by the values of other attributes.



# Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a relational database  .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and removing any attribute from it would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier for the relation.
- The other candidate keys that are not chosen as the primary key are called alternate keys or secondary keys.
- A candidate key can be a single attribute or a combination of attributes, depending on the data requirements and constraints.
- A candidate key should satisfy the following properties:
  - Uniqueness: No two tuples in the relation should have the same values for the candidate key attributes.
  - Irreducibility: No subset of the candidate key attributes should have the uniqueness property.
  - Non-nullability: The candidate key attributes should not have null values in any tuple.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of primary key for the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System.

# Primary Key
- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key is a constraint that enforces the uniqueness and non-nullability of the values in the key column(s).
- A primary key can be used to reference the table in other tables or queries, and to ensure the integrity of the data in the database.
- A primary key can be either simple or composite, depending on the number of columns involved.
  - A simple primary key is a single column that uniquely identifies each row in a table.
  - A composite primary key is a combination of two or more columns that uniquely identifies each row in a table.
- A primary key should be chosen based on the following criteria:
  - The values in the key column(s) should be stable and rarely change over time.
  - The values in the key column(s) should be short and simple, to reduce the storage space and improve the performance of the queries.
  - The values in the key column(s) should be meaningful and relevant to the data in the table, and not arbitrary or artificial.
  - The values in the key column(s) should not contain any sensitive or confidential information, such as passwords or personal identifiers.
- A primary key can be defined in different ways, such as:
  - Using the PRIMARY KEY clause in the CREATE TABLE statement, to specify the column(s) that form the primary key of the table.
  - Using the ALTER TABLE statement, to add or modify the primary key of an existing table.
  - Using the CONSTRAINT clause, to name the primary key constraint and optionally specify the index type and other options.
- A primary key can be dropped or disabled using the DROP CONSTRAINT or DISABLE CONSTRAINT clauses in the ALTER TABLE statement, respectively.
- A primary key can be referenced by a foreign key in another table, to establish a relationship between the two tables and enforce the referential integrity of the data.
- A primary key can be used in various operations and functions, such as:
  - Joining tables based on the matching values in the key column(s).
  - Filtering or sorting data based on the values in the key column(s).
  - Creating indexes or views based on the key column(s).
  - Generating unique identifiers or sequences based on the key column(s).



# Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Generalization is a bottom-up approach in which two lower level entities combine to form a higher level entity .
- In generalization, the higher level entity can also combine with other lower level entities to make further higher level entity.
- In generalization, the higher level entity inherits the properties of all the lower level entities.
- Generalization is used to hide the details of a set of objects and extract their common properties.
- Generalization is represented by a triangle with the word "is-a" above it .
- An example of generalization is the entity PERSON, which can be generalized from the entities STUDENT and TEACHER .

Generalization Example

- The entity PERSON has the common attributes of STUDENT and TEACHER, such as name, address, phone, etc .
- The entity PERSON can also have its own attributes, such as date of birth, gender, etc .
- The entity PERSON can also be further generalized with other entities, such as EMPLOYEE, CUSTOMER, etc .

Generalization Example 2

- Generalization is useful for reducing redundancy and complexity in the data model.
- Generalization is also useful for representing hierarchical relationships among entities.



# Aggregation in Entity Relationship Model

- Aggregation is a concept in the entity relationship model that allows us to represent a relationship between a relationship set and an entity set as a single entity set.
- Aggregation is useful when we want to model a relationship involving a relationship set and another entity set, and then participate that aggregated entity set in another relationship.
- Aggregation helps us to avoid creating redundant or complex relationships and to simplify the design of the entity relationship diagram.
- Aggregation is represented by drawing a dashed rectangle around the relationship set and the entity set that are involved in the aggregation, and then connecting the rectangle to another entity set or relationship set by a solid line.

## Example of Aggregation

- Consider the following scenario: A center offers various courses, and each course is taught by a teacher. A visitor can enroll in one or more courses offered by a center. We want to model the relationship between the visitor and the course-teacher pair.
- One way to model this is to use a ternary relationship called Enrolls that involves the entity sets Visitor, Course, and Teacher. However, this would create a redundancy, as the relationship between Course and Teacher is already captured by the relationship set Offers.
- A better way to model this is to use aggregation. We can treat the relationship set Offers as an entity set, and call it CourseOffering. Then, we can create a binary relationship called Enrolls between Visitor and CourseOffering. This way, we avoid the redundancy and simplify the design.
- The following diagram shows the aggregation in the entity relationship model:

aggregation example



# Reduction of an ER Diagram to Tables

- An ER diagram is a graphical representation of the entities and relationships in a database.
- A table is a collection of rows and columns that store data in a database.
- The process of converting an ER diagram to tables is also known as mapping or mapping schema.
- The purpose of converting an ER diagram to tables is to create a logical schema of the database that can be implemented in a relational database management system (RDBMS).
- The basic rules for converting an ER diagram to tables are :

  - Convert all the entities in the diagram to tables. All the entities represented in the rectangular box in the ER diagram become independent tables in the database.
  - Convert all the attributes in the diagram to columns. All the attributes represented in the oval shape in the ER diagram become columns in the corresponding tables.
  - Convert all the primary keys in the diagram to primary keys in the tables. All the attributes that are underlined in the ER diagram become primary keys in the corresponding tables. A primary key is a column or a combination of columns that uniquely identifies a row in a table.
  - Convert all the relationships in the diagram to foreign keys or new tables. All the relationships represented in the diamond shape in the ER diagram can be mapped to foreign keys or new tables depending on the cardinality and participation of the entities involved. A foreign key is a column or a combination of columns that references a primary key in another table. A new table is created when a relationship has attributes or when it is a many-to-many relationship.

- The following are some examples of converting different types of relationships in the ER diagram to tables  :

  - One-to-one relationship: A one-to-one relationship is a relationship between two entities where each entity can be related to at most one instance of the other entity. For example, a person can have at most one passport and a passport can belong to at most one person. To convert a one-to-one relationship to tables, we can choose one of the entities and add the primary key of the other entity as a foreign key in its table. Alternatively, we can create a new table for the relationship and include the primary keys of both entities as foreign keys in the new table. For example, the ER diagram below shows a one-to-one relationship between PERSON and PASSPORT entities.

    One-to-one relationship

    To convert this ER diagram to tables, we can choose the PERSON entity and add the PASSPORT_NO attribute as a foreign key in its table. Alternatively, we can create a new table for the relationship and include the PERSON_ID and PASSPORT_NO attributes as foreign keys in the new table. The tables are shown below.

    | PERSON_ID | NAME | AGE | PASSPORT_NO |
    |-----------|------|-----|-------------|
    | 101       | Alice| 25  | P123        |
    | 102       | Bob  | 30  | P456        |
    | 103       | Carol| 28  | P789        |

    | PASSPORT_NO | ISSUE_DATE | EXPIRY_DATE |
    |-------------|------------|-------------|
    | P123        | 01-01-2020 | 31-12-2025  |
    | P456        | 15-02-2020 | 14-02-2026  |
    | P789        | 10-03-2020 | 09-03-2026  |

    | PERSON_PASSPORT | PERSON_ID | PASSPORT_NO |
    |-----------------|-----------|-------------|
    | 1               | 101       | P123        |
    | 2               | 102       | P456        |
    | 3               | 103       | P789        |

  - One-to-many relationship: A one-to-many relationship is a relationship between two entities where one entity can be related to many instances of the other entity, but the other entity can be related to at most one instance of the first entity. For example, a department can have many employees, but an employee can belong to at most one department. To convert a one-to-many relationship to tables, we can choose the entity on the many side and add the primary key of the entity on the one side as a foreign key in its table. For example, the ER diagram below shows a one-to-many relationship between DEPARTMENT and EMPLOYEE entities.

    ![One-to-many relationship](



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the extended ER model for the unit 2 of the subject of Basics of Data Base Management System.

# Extended ER Model

- The extended ER model (or enhanced ER model) is a high-level or conceptual data model that incorporates extensions to the original ER model, used in the design of databases.
- The extended ER model was developed to reflect more precisely the properties and constraints that are found in complex databases, such as object-oriented databases, temporal databases, spatial databases, etc.
- The extended ER model includes the following concepts in addition to the ER model concepts :
  - Subclasses and superclasses: A subclass is a subset of entities of a superclass that share some common attributes or relationships distinct from other entities of the superclass. A superclass is a set of entities that have some common attributes or relationships shared by all its subclasses. For example, a superclass PERSON can have subclasses STUDENT and TEACHER, each with their own attributes and relationships.
  - Specialization and generalization: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics of the entities in the superclass. Generalization is the reverse process of abstraction, where common properties of lower-level entities are grouped together to form a higher-level entity. For example, a specialization of PERSON can be based on the attribute occupation, and a generalization of STUDENT and TEACHER can be PERSON.
  - Category or union type: A category or union type is a subclass that represents a collection of entities from different entity types that share some common features. A category or union type is also called a shared subclass, because it is a subclass of more than one superclass. For example, a category or union type EMPLOYEE can be a subclass of both STUDENT and TEACHER, if some persons can be both students and teachers.
  - Aggregation: Aggregation is the process of treating a relationship as a higher-level entity, which can participate in other relationships or have attributes of its own. Aggregation is used to represent a part-whole or a component-of relationship between an entity and a relationship. For example, an aggregation of the relationship WORKS_ON between EMPLOYEE and PROJECT can be treated as an entity ASSIGNMENT, which can have an attribute budget or a relationship with another entity DEPARTMENT.



# Relationships of Higher Degree

- A relationship is an association between two or more entities in an ER model.
- The degree of a relationship is the number of entities that participate in it.
- A binary relationship has a degree of two, meaning it involves two entities.
- A ternary relationship has a degree of three, meaning it involves three entities.
- A higher degree relationship has a degree of more than three, meaning it involves more than three entities.
- Higher degree relationships are rare and complex, and they should be avoided if possible.
- Higher degree relationships can be converted into binary relationships by introducing new entity types or relationship types.
- For example, a quaternary relationship R between entities A, B, C, and D can be replaced by a new entity type E and four binary relationships between E and A, E and B, E and C, and E and D.
- To read a higher degree relationship, we need to isolate two out of the participating entities and see how they relate to the third one, and repeat this for all possible pairs.
- For example, to read a ternary relationship R between entities A, B, and C, we need to see how A and B relate to C, how A and C relate to B, and how B and C relate to A.



## Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table consists of rows (records) and columns (attributes).
- A primary key is a column or a combination of columns that uniquely identifies each row in a table.
- A foreign key is a column or a combination of columns that references a primary key in another table, to establish a relationship between the tables.
- A relationship is a logical association between two or more tables, based on a common attribute or a foreign key.
- There are three types of relationships: one-to-one, one-to-many, and many-to-many.
- A one-to-one relationship occurs when each row in one table is related to exactly one row in another table.
- A one-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to at most one row in the first table.
- A many-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to zero or more rows in the first table.
- A many-to-many relationship requires a third table, called a junction table or an associative table, to store the combinations of primary keys from the two related tables.
- A relational schema is a graphical representation of the structure and relationships of a relational database, using symbols and notation to indicate the tables, columns, keys, and relationships.
- A relational model is a set of rules and constraints that define how data is stored and manipulated in a relational database, such as the entity integrity rule, the referential integrity rule, and the normalization rules.
- The entity integrity rule states that no primary key column can have a null value, to ensure the uniqueness of each row in a table.
- The referential integrity rule states that any foreign key value must either match a primary key value in the referenced table, or be null, to ensure the consistency of the data across the tables.
- Normalization is a process of organizing the data in a relational database into tables that are free of anomalies, redundancies, and dependencies, to improve the efficiency and integrity of the database.
- There are several levels of normalization, each with a specific goal and a set of criteria to meet. The most common levels are the first normal form (1NF), the second normal form (2NF), and the third normal form (3NF).
- The first normal form (1NF) requires that each table has a primary key, and that each column contains atomic values, meaning no repeating groups or nested tables.
- The second normal form (2NF) requires that each table is in 1NF, and that each non-key column is fully dependent on the primary key, meaning no partial dependencies.
- The third normal form (3NF) requires that each table is in 2NF, and that each non-key column is non-transitively dependent on the primary key, meaning no transitive dependencies.



# Introduction to Relational Database

- A relational database is a type of database that stores and provides access to data points that are related to one another   .
- A relational database organizes data into rows and columns, which collectively form a table  .
- Data is typically structured across multiple tables, which can be joined together via a primary key or a foreign key .
- A primary key is a unique identifier for each row in a table, such as an ID number .
- A foreign key is a column or a set of columns that references a primary key in another table, such as a customer ID in an order table .
- Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables .
- The relational model was proposed by Edgar F. Codd in 1970 as a way of overcoming the limitations of hierarchical and network databases .
- The relational model consists of three components: data structure, data integrity, and data manipulation .
- Data structure refers to the way data is organized into tables, columns, and rows .
- Data integrity refers to the rules and constraints that ensure the accuracy and consistency of data, such as primary key, foreign key, and referential integrity .
- Data manipulation refers to the operations that can be performed on data, such as querying, updating, inserting, and deleting data, using a standard language such as SQL (Structured Query Language) .
- Relational databases are also typically associated with transactional databases, which execute commands, or transactions, collectively.
- A transaction is a logical unit of work that must be either completed entirely or not at all, to ensure the consistency and reliability of data.
- A popular example that is used to illustrate this is a bank transfer. A defined amount is withdrawn from one account, and then it is deposited within another.
- Relational databases are widely used in various domains, such as business, education, health care, and government, to store and manage large amounts of structured data   .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of relational database structure for the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System.

# Relational Database Structure

- A relational database is a collection of data organized into tables, where each table consists of rows and columns.
- Each row in a table represents a record or a tuple, and each column represents an attribute or a field of the record.
- Each table has a primary key, which is a column or a combination of columns that uniquely identifies each record in the table.
- A table can also have foreign keys, which are columns that refer to the primary key of another table, establishing a relationship between the tables.
- A relational database can have multiple tables, and each table can have multiple relationships with other tables.
- A relational database follows a set of rules, called the relational model, which defines how the data is structured, manipulated, and enforced.
- The relational model is based on the concept of mathematical relations, which are sets of ordered pairs of values that satisfy certain properties.
- The relational model also defines a set of operations, called relational algebra, which can be used to query and manipulate the data in a relational database.
- Some of the basic operations of relational algebra are selection, projection, join, union, intersection, difference, and division.
- A relational database can be accessed and manipulated using a query language, such as SQL (Structured Query Language), which allows users to specify what data they want to retrieve or modify, without specifying how to do it.
- A relational database can also be designed using a graphical notation, called the entity-relationship (ER) model, which depicts the entities, attributes, and relationships in a database using symbols and diagrams.
- An entity is an object or a concept that can be identified and distinguished from others, such as a person, a product, or an event.
- An attribute is a property or a characteristic of an entity, such as a name, a price, or a date.
- A relationship is an association or a connection between two or more entities, such as a customer buying a product, or a product belonging to a category.
- An ER model can be converted into a relational database schema, which is a formal description of the tables, columns, keys, and constraints in a database.



# Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relation .
- A domain defines the **data type** and the **constraints** for an attribute .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- A domain is also **homogeneous**, meaning that all the values in the domain have the same data type and constraints.
- A domain can be **named** or **unnamed**. A named domain has a unique identifier that can be referenced by multiple attributes. An unnamed domain is defined by the attribute itself.
- A domain can be **simple** or **composite**. A simple domain has only one component, such as integer or string. A composite domain has multiple components, such as date or address.
- A domain can be **scalar** or **nonscalar**. A scalar domain has a single value, such as number or boolean. A nonscalar domain has a collection of values, such as array or set.

## Examples of domains

- The domain of **StudentID** is the set of all possible student identification numbers, such as {123456, 234567, 345678, ...}. It is a simple, scalar, and named domain with an integer data type and a uniqueness constraint.
- The domain of **Name** is the set of all possible names, such as {"Alice", "Bob", "Charlie", ...}. It is a simple, scalar, and unnamed domain with a string data type and a length constraint.
- The domain of **DOB** is the set of all possible dates of birth, such as {01/01/2000, 02/02/2001, 03/03/2002, ...}. It is a composite, scalar, and unnamed domain with a date data type and a range constraint.
- The domain of **Courses** is the set of all possible courses that a student can enroll in, such as {"CS101", "CS102", "CS103", ...}. It is a simple, nonscalar, and unnamed domain with a string data type and a cardinality constraint.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System:

# Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table consists of rows and columns.
- A table is also called a relation, and each row is called a tuple or a record. Each column is called an attribute or a field.
- A primary key is a column or a combination of columns that uniquely identifies each row in a table. A foreign key is a column or a combination of columns that references a primary key in another table, to establish a relationship between the tables.
- A relational schema is a description of the structure and constraints of a relational database. It specifies the name, attributes, and primary key of each table, and the foreign key constraints between the tables.
- A relational algebra is a set of operations that can be applied to one or more tables to manipulate and query data. Some common relational algebra operations are selection, projection, join, union, intersection, difference, and division.
- A relational calculus is a declarative language that expresses queries in terms of variables and predicates, without specifying the order of operations. It is based on mathematical logic and set theory. There are two types of relational calculus: tuple relational calculus and domain relational calculus.
- A query language is a language that allows users to interact with a relational database. It can be either procedural or non-procedural. A procedural query language requires users to specify how to obtain the desired data, such as SQL. A non-procedural query language requires users to specify what data they want, without specifying how to obtain it, such as QBE.
- A functional dependency is a constraint that expresses a relationship between attributes of a table. It states that the value of one or more attributes determines the value of another attribute. For example, if A and B are attributes of a table, and A -> B is a functional dependency, it means that for any two rows in the table, if they have the same value for A, they must have the same value for B.
- A normal form is a property of a relational schema that indicates the degree of redundancy and inconsistency in the data. The higher the normal form, the less redundancy and inconsistency. There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
- A normalization is a process of decomposing a table into smaller tables that satisfy higher normal forms, to reduce redundancy and inconsistency, and improve data integrity and efficiency. A denormalization is a process of combining smaller tables into larger tables that satisfy lower normal forms, to improve performance and usability, at the cost of some redundancy and inconsistency.



# Tuples in Relational Database

- A tuple is one record or row in a relational database  .
- A tuple contains all the data for an individual entity or object in the database .
- A tuple consists of a set of attribute-value pairs, where each attribute corresponds to a column or field in the database, and each value belongs to a specific data type   .
- A tuple can be identified by a primary key, which is a unique attribute or combination of attributes that distinguishes it from other tuples in the same table .
- A tuple can also have foreign keys, which are attributes that reference the primary keys of other tuples in different tables, to establish relationships between them  .
- A tuple can be manipulated by various operations, such as insertion, deletion, update, selection, projection, join, etc., using a query language such as SQL  .
- A tuple can be stored in a page or block of memory in the database, which has a fixed size and can hold one or more tuples. Some databases can distribute a single tuple across multiple pages if it exceeds the available space.



# Relations and Relational Database Schema

- A **relation** is a set of tuples that have the same attributes. A tuple is a single row of data in a table. An attribute is a column or field name of a table. A relation can also be called a table or a relation variable.
- A **relational schema** is a collection of relation schemas for a whole database. A relation schema is a specification of the name, attributes, and constraints of a relation. A relational schema can also be called a database schema or a schema.
- A relational schema describes the structure and constraints of data representing in a particular domain  . It does not contain any actual data, but only the meta-data or the blueprint of the data.
- A relational schema can be represented by using the following notation:

  Relation_Name (Attribute1, Attribute2, ..., AttributeN)

  where Relation_Name is the name of the relation, and Attribute1, Attribute2, ..., AttributeN are the names of the attributes. For example:

  Student (Student_ID, Name, Major, GPA)

  is a relation schema for a relation that stores information about students.

- A relational schema can also show the primary key, foreign key, and other constraints of a relation by using additional symbols and annotations. For example:

  Student (**Student_ID**, Name, Major, GPA, *Advisor_ID*)

  is a relation schema for a relation that stores information about students, where Student_ID is the primary key, and Advisor_ID is a foreign key that references the Advisor relation.

- A relational schema can be displayed graphically by using an entity-relationship (ER) diagram or a relational diagram. An ER diagram shows the entities, attributes, and relationships in a database, while a relational diagram shows the relations, attributes, and keys in a database. For example:

  ER diagram

  is an ER diagram for a database that stores information about a massively multiplayer online role-playing game (MMORPG).

  Relational diagram

  is a relational diagram for a database that stores information about books, authors, and publishers.

- The benefits of using a relational schema are:

  - It provides a clear and concise description of the data and its structure in a database.
  - It facilitates the design, implementation, and maintenance of a database by ensuring data integrity, consistency, and security.
  - It enables the use of a relational database management system (RDBMS) to manipulate and query the data in a database using a standard language such as SQL .



# Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of data in a relational database.
- Integrity constraints can be defined at the schema level (when the database is created or modified) or at the instance level (when data is inserted, updated, or deleted).
- Integrity constraints can be classified into four types: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

## Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for each attribute.
- Domain constraints ensure that the data stored in a relation conforms to the intended meaning and semantics of the attribute.

## Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by defining primary keys, candidate keys, or alternate keys for each relation.
- Key constraints ensure that there are no duplicate tuples in a relation and that each tuple can be uniquely referenced.

## Entity Integrity Constraints

- Entity integrity constraints ensure that the primary key of a relation does not contain null values.
- Entity integrity constraints can be enforced by declaring the primary key as not null or by using a default value for the primary key.
- Entity integrity constraints ensure that each tuple in a relation represents a distinct entity and that the primary key can be used to identify the entity.

## Referential Integrity Constraints

- Referential integrity constraints ensure that the foreign key of a relation either matches the primary key of another relation or is null.
- Referential integrity constraints can be enforced by declaring the foreign key as a foreign key constraint and specifying the referenced relation and attribute(s).
- Referential integrity constraints ensure that the relationships between entities are consistent and that the foreign key can be used to refer to the related entity.



# Entity Integrity in Relational Database

- Entity integrity is a form of data integrity that ensures that each entity (row or record) in a table has a unique and non-null identifier (primary key).
- Entity integrity is one of the three types of integrity constraints in the relational data model, along with referential integrity and domain integrity.
- Entity integrity prevents duplicate or missing data in a table, and ensures that each entity can be uniquely identified and accessed by the primary key.
- Entity integrity is enforced by the database system by checking the primary key values for each entity before inserting, updating, or deleting data in a table.
- Entity integrity can be violated by:
  - Inserting a new entity with a primary key value that already exists in the table.
  - Inserting a new entity with a null primary key value.
  - Updating an existing entity with a primary key value that already exists in the table.
  - Updating an existing entity with a null primary key value.
  - Deleting an existing entity without specifying its primary key value.
- Entity integrity can be maintained by:
  - Defining a primary key for each table in the relational model, and ensuring that it is not null and unique for each entity.
  - Using a surrogate key (an artificial or generated value) as the primary key if the natural key (an attribute or combination of attributes that uniquely identifies an entity) is not suitable or available.
  - Using a composite key (a combination of two or more attributes) as the primary key if a single attribute is not sufficient or meaningful to identify an entity.
  - Using a foreign key (an attribute or combination of attributes that references the primary key of another table) to link entities across tables and enforce referential integrity.



# Referential Integrity

- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- Referential integrity requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist.
- Referential integrity is enforced by using primary keys and foreign keys .
- A primary key is a column or a set of columns that uniquely identifies each row in a table .
- A foreign key is a column or a set of columns that references a primary key in another table .
- Referential integrity constraints prevent the following actions :
  - Inserting a record in a table that contains a foreign key without a corresponding record in the referenced table.
  - Updating a primary key value in a table that is referenced by a foreign key in another table without updating the foreign key value accordingly.
  - Deleting a record in a table that is referenced by a foreign key in another table without deleting the referencing record or setting the foreign key value to null.
- Referential integrity ensures data integrity, consistency, and accuracy in a relational database .



# Key Constraints in Relational Database

Key constraints are rules that ensure the integrity and uniqueness of data in a relational database. They are applied on the columns or attributes that are used as keys to identify and relate the rows in a table. There are different types of key constraints in a relational database, such as:

- **Primary key constraint**: This constraint requires every entry in the given column or set of columns to be both unique and not NULL, and allows you to use that column or set of columns to identify each individual row in the table. A table can have only one primary key constraint, which can be either clustered or nonclustered. For example, in a table of students, the student ID can be a primary key.

- **Foreign key constraint**: This constraint requires every entry in the given column or set of columns to match an existing value in the primary key column or set of columns of another table, and ensures the referential integrity between the two tables. A table can have multiple foreign key constraints, which can reference the same or different tables. For example, in a table of courses, the course ID can be a foreign key that references the primary key of another table of course details.

- **Unique key constraint**: This constraint requires every entry in the given column or set of columns to be unique, but allows NULL values. A table can have multiple unique key constraints, which can be either clustered or nonclustered. For example, in a table of students, the email address can be a unique key.

- **Check key constraint**: This constraint requires every entry in the given column or set of columns to satisfy a specified condition or expression. A table can have multiple check key constraints, which can apply to the same or different columns. For example, in a table of students, the age can be a check key that ensures the value is greater than zero.

- **Not NULL key constraint**: This constraint requires every entry in the given column or set of columns to have a value and not be NULL. A table can have multiple not NULL key constraints, which can apply to the same or different columns. For example, in a table of students, the name can be a not NULL key.



# Domain Constraints for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Domain constraints are a type of user-defined column that helps us to arrange the data we have entered according to the datatype.
- A domain integrity constraint is a set of rules that restricts the kind of attributes or values a column or relation can hold in the database table.
- The domain means a range of values. In mathematics, the concept of Domain means the allowed values for a function. Similarly, in DBMS, the Domain Constraint specifies the domain or set of values.
- There are two types of constraints that come under domain constraint and they are:
  - Domain Constraints – Not Null: Null values are the values that are unassigned or we can also say that which are unknown. The not null constraint is used to specify that the column must not accept null values.
  - Domain Constraints – Check: It defines a condition that each row must satisfy which means it checks the validity of the data entered into the column.
- Domain constraints can be defined using the CREATE TABLE or ALTER TABLE statements in SQL. For example:
```sql
CREATE TABLE Student
(
  Roll_no int NOT NULL,
  Name varchar(50) NOT NULL,
  Age int CHECK (Age>=18),
  Gender char(1) CHECK (Gender IN ('M','F')),
  PRIMARY KEY (Roll_no)
);
```
- Domain constraints can also be defined using rules in SQL Server. A rule is a named object that contains a condition for the data in a column. For example:
```sql
CREATE RULE AgeRule
AS
@Age >= 18
GO
CREATE TABLE Student
(
  Roll_no int NOT NULL,
  Name varchar(50) NOT NULL,
  Age int,
  Gender char(1) CHECK (Gender IN ('M','F')),
  PRIMARY KEY (Roll_no)
);
GO
EXEC sp_bindrule 'AgeRule', 'Student.Age'
GO
```
- Domain constraints are important to ensure the data quality and integrity in the database. They prevent the insertion of invalid or inconsistent data that may cause errors or anomalies in the database operations.



# Relational Algebra and Relational Calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a procedural language that specifies how to construct a new relation from one or more existing relations in the database.
- Relational calculus is a declarative language that specifies what data to retrieve from the database without specifying how to do it.
- Both languages are equivalent in expressive power, meaning that any query that can be expressed in one language can also be expressed in the other language. This is known as Codd's theorem.

## Relational Algebra

- Relational algebra consists of a set of basic operations that take one or more relations as input and produce a new relation as output.
- The basic operations are:
  - Selection: selects a subset of tuples from a relation that satisfy a given condition.
  - Projection: selects a subset of attributes from a relation and eliminates duplicates.
  - Union: combines two relations with the same set of attributes and eliminates duplicates.
  - Set difference: returns the tuples that are in one relation but not in another relation with the same set of attributes.
  - Cartesian product: combines two relations by forming all possible pairs of tuples from both relations.
  - Rename: assigns a new name to a relation or an attribute.
- Relational algebra also defines additional operations that are derived from the basic operations, such as:
  - Intersection: returns the tuples that are common to both relations with the same set of attributes.
  - Join: combines two relations by matching tuples based on a join condition.
  - Division: returns the tuples from one relation that are associated with all tuples from another relation.
  - Aggregate functions: apply a function to a set of tuples and return a single value, such as sum, count, average, etc.
  - Grouping and sorting: group tuples by one or more attributes and sort them by one or more attributes.

## Relational Calculus

- Relational calculus consists of a set of formulas that define relations in terms of other relations in the database.
- The formulas are composed of variables, constants, logical connectives, quantifiers, and predicates that refer to relations and attributes in the database.
- There are two types of relational calculus: tuple relational calculus and domain relational calculus.
- Tuple relational calculus uses variables that range over tuples of a relation and predicates that involve the attributes of the relation.
- Domain relational calculus uses variables that range over the domains of attributes and predicates that involve the values of the attributes.
- Both types of relational calculus are equivalent in expressive power, meaning that any query that can be expressed in one type can also be expressed in the other type.
- Relational calculus is a safe language, meaning that any query that can be expressed in it will always return a finite set of tuples as a result.



# Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a non-procedural query language for relational databases  .
- Relational calculus allows users to specify what data they want to retrieve from the database, without specifying how to do it .
- Tuple and domain calculus differ in the way they use variables to represent data in the database.

## Tuple Relational Calculus (TRC)

- Tuple relational calculus uses tuple variables that range over the tuples of a relation  .
- A tuple variable is denoted by a lowercase letter, such as t, and can be used to refer to the attribute values of a tuple.
- A tuple relational calculus query consists of a formula that evaluates to true or false for each tuple in the database .
- The result of a tuple relational calculus query is the set of all tuples that make the formula true .
- A tuple relational calculus formula can use logical connectives (and, or, not), comparison operators (=, <, >, etc.), and quantifiers (for all, there exists)  .
- A tuple relational calculus formula can also use subqueries, which are formulas that refer to other relations.
- An example of a tuple relational calculus query is:

  {t.name | Student(t) and t.age > 18}

  This query returns the names of all students who are older than 18.

## Domain Relational Calculus (DRC)

- Domain relational calculus uses domain variables that range over the values of a domain  .
- A domain is a set of possible values for an attribute, such as integers, strings, dates, etc.
- A domain variable is denoted by an uppercase letter, such as X, and can be used to refer to a single value in a domain.
- A domain relational calculus query consists of a formula that evaluates to true or false for each combination of values in the domains of the database .
- The result of a domain relational calculus query is the set of all combinations of values that make the formula true .
- A domain relational calculus formula can use logical connectives, comparison operators, and quantifiers, similar to tuple relational calculus .
- A domain relational calculus formula can also use subqueries, which are formulas that refer to other relations, but with domain variables instead of tuple variables.
- An example of a domain relational calculus query is:

  {X | Student(name, age) and X = name and age > 18}

  This query returns the names of all students who are older than 18.



# Basic Operations – Selection and Projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database  .
- Selection operation targets records (rows) or specific entities in a relational database. It filters the rows that satisfy a given condition or predicate .
- Projection operation targets attributes (columns) or specific properties in a relational database. It selects the columns that are specified in the query  .
- In SQL, the SELECT statement combines both selection and projection operations in a single query.
- The syntax of the SELECT statement is as follows:

```sql
SELECT column_list
FROM table_name
WHERE condition;
```

- The column_list specifies the attributes or columns to be projected. The * symbol can be used to select all the columns.
- The table_name specifies the relation or table to be queried.
- The condition specifies the predicate or criteria to be applied for selection. The WHERE clause is optional and can be omitted if no condition is required.
- Some examples of the SELECT statement are:

```sql
-- Select all the columns and rows from the table student
SELECT * FROM student;

-- Select the name and age columns from the table student
SELECT name, age FROM student;

-- Select the name and age columns from the table student where age is greater than 18
SELECT name, age FROM student WHERE age > 18;
```



# Set-theoretic operations for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

Set-theoretic operations are the standard mathematical operations on sets that can be applied to relations in a relational database. These operations are binary, meaning that they operate on two relations at a time. The two relations must be union compatible, meaning that they have the same number and type of attributes, and the same domain for each attribute. The result of a set-theoretic operation is also a relation that is union compatible with the operands.

The main set-theoretic operations are:

- **Union**: The union of two relations R and S, denoted by R ∪ S, is the relation that contains all the tuples that are either in R or in S or in both. The union operation eliminates any duplicate tuples from the result. For example, if R and S are two relations with the same schema of (name, age), then R ∪ S is the relation that contains all the distinct (name, age) pairs from both R and S.

- **Intersection**: The intersection of two relations R and S, denoted by R ∩ S, is the relation that contains all the tuples that are common to both R and S. For example, if R and S are two relations with the same schema of (name, age), then R ∩ S is the relation that contains all the (name, age) pairs that are present in both R and S.

- **Difference**: The difference of two relations R and S, denoted by R - S, is the relation that contains all the tuples that are in R but not in S. For example, if R and S are two relations with the same schema of (name, age), then R - S is the relation that contains all the (name, age) pairs that are in R but not in S.

- **Cartesian product**: The Cartesian product of two relations R and S, denoted by R × S, is the relation that contains all the possible combinations of tuples from R and S. The schema of the Cartesian product is the concatenation of the schemas of R and S. For example, if R is a relation with the schema of (name, age) and S is a relation with the schema of (city, country), then R × S is the relation with the schema of (name, age, city, country) that contains all the possible (name, age, city, country) tuples from R and S.

Set-theoretic operations are useful for manipulating and combining relations in a relational database. They can be used to express complex queries and operations in a concise and elegant way. They can also be combined with other relational algebra operations, such as selection, projection, and join, to form more powerful expressions.



# Join Operations

Join operations are used to combine data from two or more tables in a relational database based on some common attributes or conditions. Join operations are essential for querying data across multiple tables and performing complex analysis.

## Types of Join Operations

There are different types of join operations that can be used depending on the desired result and the relationship between the tables. Some of the common types of join operations are:

- **Inner join**: This type of join returns only the rows that match the join condition in both tables. It is the most commonly used type of join and can be written as `JOIN` or `INNER JOIN`.
- **Left outer join**: This type of join returns all the rows from the left table and the matching rows from the right table. If there is no match for a row in the left table, the right table columns are filled with null values. It can be written as `LEFT JOIN` or `LEFT OUTER JOIN`.
- **Right outer join**: This type of join returns all the rows from the right table and the matching rows from the left table. If there is no match for a row in the right table, the left table columns are filled with null values. It can be written as `RIGHT JOIN` or `RIGHT OUTER JOIN`.
- **Full outer join**: This type of join returns all the rows from both tables, regardless of whether they match the join condition or not. If there is no match for a row in either table, the other table columns are filled with null values. It can be written as `FULL JOIN` or `FULL OUTER JOIN`.
- **Cross join**: This type of join returns the Cartesian product of the two tables, which means every row in the first table is paired with every row in the second table. It can be written as `CROSS JOIN`.

## Syntax of Join Operations

The general syntax of join operations in SQL is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

The `column_list` specifies the columns to be retrieved from the tables. The `table1` and `table2` are the names of the tables to be joined. The `join_condition` specifies the criteria for matching the rows from the tables. It usually involves a comparison operator (such as `=` or `<>`) and a common attribute (such as a foreign key or a primary key) from both tables.

For example, suppose we have two tables: `customers` and `orders`, where `customers.customer_id` is the primary key of the `customers` table and `orders.customer_id` is the foreign key of the `orders` table that references the `customers` table. To join these two tables and retrieve the customer name and the order date for each order, we can use the following query:

```sql
SELECT customers.name, orders.order_date
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

This query will return the rows that have the same `customer_id` value in both tables, which means the customers who have placed at least one order.

## Examples of Join Operations

To illustrate the different types of join operations, let us use the following sample tables: `employees` and `departments`, where `employees.dept_id` is the foreign key that references the `departments.dept_id` column.

| employees | | | | |
| --- | --- | --- | --- | --- |
| emp_id | name | salary | dept_id | manager |
| 1 | Alice | 5000 | 10 | Bob |
| 2 | Bob | 6000 | 10 | NULL |
| 3 | Charlie | 4000 | 20 | David |
| 4 | David | 7000 | 20 | NULL |
| 5 | Eve | 3000 | NULL | NULL |

| departments | | |
| --- | --- | --- |
| dept_id | dept_name | location |
| 10 | Sales | New York |
| 20 | Marketing | London |
| 30 | Finance | Tokyo |

### Inner Join

To join the `employees` and `departments` tables and retrieve the employee name, department name, and location for each employee, we can use an inner join as follows:

```sql
SELECT employees.name, departments.dept_name, departments.location
FROM employees
JOIN departments
ON employees.dept_id = departments.dept_id;
```

This query will return the following result:

| name | dept_name | location |
| --- | --- | --- |
| Alice | Sales | New York |
| Bob | Sales | New York |
| Charlie



## Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing data into tables with well-defined relationships and constraints.
- The main steps of database design and normalization are:

  - **Requirement analysis**: Identify the purpose, scope, and objectives of the database system, and gather the data requirements from the users and stakeholders.
  - **Conceptual design**: Create a high-level abstract model of the data using an entity-relationship (ER) diagram, which shows the entities, attributes, and relationships involved in the database system.
  - **Logical design**: Map the conceptual model to a logical model using a data model, such as the relational model, which defines the tables, columns, keys, and constraints for the database system.
  - **Normalization**: Apply the rules of normalization to the logical model to eliminate any anomalies, such as update, insertion, or deletion anomalies, that may arise due to data redundancy or dependency.
  - **Physical design**: Implement the logical model in a specific database management system (DBMS), and optimize the performance, security, and usability of the database system.

- The main rules of normalization are:

  - **First normal form (1NF)**: A table is in 1NF if every column contains only atomic values, and there are no repeating groups or arrays within a column.
  - **Second normal form (2NF)**: A table is in 2NF if it is in 1NF and every non-key column is fully functionally dependent on the primary key, and not on any subset of the primary key.
  - **Third normal form (3NF)**: A table is in 3NF if it is in 2NF and every non-key column is non-transitively dependent on the primary key, and not on any other non-key column.
  - **Boyce-Codd normal form (BCNF)**: A table is in BCNF if it is in 3NF and every determinant is a candidate key, and not a proper subset of any candidate key.
  - **Fourth normal form (4NF)**: A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, which occur when a column depends on another column that has more than one value for a given key.
  - **Fifth normal form (5NF)**: A table is in 5NF if it is in 4NF and there are no join dependencies, which occur when a table can be decomposed into two or more tables that can be joined back together without losing any information.



# Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database .
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency acts as a constraint between the two sets of attributes and is an essential factor in designing database parameters and functions.
- A functional dependency is denoted by an arrow, such as X -> Y, which means that the value of Y is determined by the value of X  .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A dependent is always a subset of the determinant, such as X -> X or X -> XY.
  - Non-trivial functional dependency: A dependent is strictly not a subset of the determinant, such as X -> Y, where Y is not a part of X.
  - Multivalued functional dependency: A determinant can have more than one dependent, such as X -> YZ, where Y and Z are independent of each other.
  - Transitive functional dependency: A dependent is determined by another dependent, such as X -> Y and Y -> Z, which implies X -> Z.
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization .
- Normalization is the process of organizing the data in a database to minimize data redundancy and improve data integrity .
- Normalization involves applying a series of normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on, to the relations in a database .
- Each normal form has a set of criteria that the relations must satisfy to be in that normal form .
- Functional dependencies are used to check whether a relation satisfies the criteria of a normal form or not .
- For example, to be in 2NF, a relation must be in 1NF and have no partial dependencies, which means that no non-key attribute is dependent on a part of the primary key .
- Functional dependencies help to identify the primary key and the non-key attributes of a relation, and to determine whether there are any partial dependencies or not .



# Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity. Normalization is the process of applying these rules to a database schema. There are different levels of normalization, called normal forms, that correspond to different conditions that a table must satisfy. The higher the normal form, the more normalized the table is. The most common normal forms are:

- **First Normal Form (1NF)**: A table is in 1NF if it does not contain any composite or multi-valued attributes. This means that each attribute has a single value and each row has a unique identifier (primary key).
- **Second Normal Form (2NF)**: A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there are no partial dependencies, where an attribute depends on only a part of the primary key.
- **Third Normal Form (3NF)**: A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there are no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.
- **Boyce-Codd Normal Form (BCNF)**: A table is in BCNF if it is in 3NF and every determinant is a candidate key. This means that there are no non-trivial functional dependencies, where a non-key attribute determines another non-key attribute.

The following table shows an example of a table that is not normalized and how it can be transformed into different normal forms by decomposing it into smaller tables.

| Student ID | Name | Course ID | Course Name | Instructor |
|------------|------|-----------|-------------|------------|
| 101        | Alice | CS101     | Programming | Bob        |
| 101        | Alice | CS102     | Data Structures | Carol     |
| 102        | Bob   | CS101     | Programming | Bob        |
| 103        | Carol | CS103     | Database Systems | Dave      |
| 103        | Carol | CS104     | Operating Systems | Eve       |

- This table is not in 1NF because it has a composite attribute (Student ID, Course ID) as the primary key and a multi-valued attribute (Course Name, Instructor) for each course.
- To convert it to 1NF, we can split the table into two tables: one for students and one for courses. The primary key of the students table is Student ID and the primary key of the courses table is Course ID. We also add a foreign key (Student ID) to the courses table to link it to the students table.

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Course ID | Course Name | Instructor | Student ID |
|-----------|-------------|------------|------------|
| CS101     | Programming | Bob        | 101        |
| CS102     | Data Structures | Carol     | 101        |
| CS101     | Programming | Bob        | 102        |
| CS103     | Database Systems | Dave      | 103        |
| CS104     | Operating Systems | Eve       | 103        |

- These tables are in 1NF but not in 2NF because the courses table has a partial dependency: Course Name and Instructor depend on Course ID, not on the whole primary key (Course ID, Student ID).
- To convert it to 2NF, we can split the courses table into two tables: one for course details and one for course enrollments. The primary key of the course details table is Course ID and the primary key of the course enrollments table is (Course ID, Student ID). We also add a foreign key (Course ID) to the course enrollments table to link it to the course details table.

| Course ID | Course Name | Instructor |
|-----------|-------------|------------|
| CS101     | Programming | Bob        |
| CS102     | Data Structures | Carol     |
| CS103     | Database Systems | Dave      |
| CS104     | Operating Systems | Eve       |

| Course ID | Student ID |
|-----------|------------|
| CS101     | 101        |
| CS102     | 101        |
| CS101     |



# Unit 4 - Data Base Design & Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database.
- Database design involves identifying the entities, attributes, and relationships that are relevant to the data requirements and organizing them into tables and columns.
- Database design also involves defining the constraints, indexes, views, triggers, and other features that ensure the integrity, performance, and security of the database.
- Database design follows a set of principles and guidelines that help in creating a well-structured and normalized database.

## Database Normalization
- Database normalization is a method in relational database design which helps properly organize data tables.
- The process aims to create a system that faithfully represents information and relationships without data loss or redundancy.
- Database normalization involves decomposing tables into smaller and simpler ones based on the functional dependencies and the level of data redundancy.
- Database normalization reduces the chances of data anomalies, such as insertion, deletion, and update anomalies, that can compromise the consistency and accuracy of the database.
- Database normalization also improves the efficiency and flexibility of the database by reducing the storage space and the number of joins required for querying the data.

## Normal Forms
- Normal forms are the standards or rules that define the level of normalization of a database or a table.
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes such that the value of one set determines the value of the other set.
- Normal forms are hierarchical, meaning that a higher normal form implies that the lower normal forms are also satisfied.
- The most common normal forms are:

  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute has a single value for each record.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key or the candidate key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key or the candidate key, meaning that there are no functional dependencies between non-key attributes.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning that there are no partial or transitive dependencies on non-key attributes.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies, meaning that there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, meaning that it cannot be decomposed into smaller tables without losing information.



# Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design by eliminating unnecessary or redundant data elements and ensuring that each table contains only related data.
- There are several levels of normalization, each with a specific set of criteria that a table must satisfy to be in that normal form. The most common levels are:

  - First normal form (1NF): A table is in 1NF if it has no repeating groups or arrays of data, and each column contains only atomic values (i.e., values that cannot be further divided into smaller parts).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (i.e., a column or a set of columns that uniquely determines another column) is a candidate key (i.e., a minimal set of columns that uniquely identifies a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and it has no multi-valued dependencies (i.e., situations where a column or a set of columns can have more than one value for a given primary key value).
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and it cannot be further decomposed into smaller tables without losing information or introducing redundancy.

- The process of normalization involves analyzing the data requirements and the relationships among the data elements, and then applying the normalization rules to create a set of normalized tables that can store the data efficiently and accurately.
- The benefits of normalization include:

  - Avoiding data anomalies, such as insertion, deletion, and update anomalies, that can occur when data is duplicated or inconsistent across tables.
  - Reducing the storage space and memory usage by eliminating redundant data.
  - Improving the performance and scalability of the database by simplifying the queries and reducing the number of joins and indexes.
  - Enhancing the security and integrity of the data by enforcing the constraints and rules at the table level.
  - Facilitating the maintenance and modification of the database by minimizing the impact of changes on other tables and applications.

- The drawbacks of normalization include:

  - Increasing the complexity and difficulty of the database design by requiring more tables and columns and more careful analysis of the data and the dependencies.
  - Increasing the number of joins and foreign keys that are needed to retrieve the data from multiple tables, which can affect the query speed and readability.
  - Losing some of the natural and intuitive representation of the data by breaking it into smaller and more abstract tables.

- Therefore, normalization is not a rigid or absolute rule, but a guideline and a trade-off between the advantages and disadvantages of different levels of normalization. Depending on the nature and purpose of the data and the application, some degree of denormalization (i.e., relaxing some of the normalization rules) may be acceptable or desirable to optimize the database performance and usability.



# Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- 3NF was originally defined by E. F. Codd in 1971.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two non-prime attributes, such that one non-prime attribute determines another non-prime attribute through the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name.
  - The primary key is (Student ID, Course ID).
  - The non-prime attributes are Student Name, Course Name, Instructor ID, Instructor Name.
  - There is a transitive dependency between Course ID and Instructor ID, because Course ID determines Instructor ID through the primary key.
  - There is also a transitive dependency between Instructor ID and Instructor Name, because Instructor ID determines Instructor Name.
  - To convert this table to 3NF, we need to remove the transitive dependencies by creating separate tables for Course and Instructor, as shown below:

| Student ID | Student Name | Course ID |
|------------|--------------|-----------|
| 101        | Alice        | C1        |
| 102        | Bob          | C2        |
| 103        | Charlie      | C3        |
| 104        | David        | C1        |

| Course ID | Course Name | Instructor ID |
|-----------|-------------|---------------|
| C1        | Math        | I1            |
| C2        | Physics     | I2            |
| C3        | Chemistry   | I3            |

| Instructor ID | Instructor Name |
|---------------|-----------------|
| I1            | Eve             |
| I2            | Frank           |
| I3            | Grace           |

- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the 3NF.
  - The 3NF always ensures functional dependency preserving and lossless decomposition.
  - The 3NF reduces the storage space and improves the performance of the database.



# BCNF

BCNF stands for Boyce-Codd Normal Form. It is a form of database normalization that ensures that there are no anomalies or redundancies in the data. BCNF is a stricter version of 3NF (Third Normal Form), which requires that every non-prime attribute is fully functionally dependent on the primary key, and that there are no transitive dependencies.

A table is in BCNF if and only if for every functional dependency X -> Y, X is a superkey of the table. A superkey is a set of attributes that uniquely identifies a tuple in the table. A candidate key is a minimal superkey, meaning that no subset of the candidate key is a superkey.

To check if a table is in BCNF, we need to find all the functional dependencies and all the candidate keys in the table. Then, we need to verify that for each functional dependency, the left-hand side is a superkey. If not, the table is not in BCNF and needs to be decomposed into smaller tables that are in BCNF.

## Example

Consider the following table that stores information about students, courses, and instructors.

| Student ID | Course ID | Instructor ID | Instructor Name | Grade |
|------------|-----------|---------------|-----------------|-------|
| S1         | C1        | I1           | Alice           | A     |
| S1         | C2        | I2           | Bob             | B     |
| S2         | C1        | I1           | Alice           | C     |
| S2         | C3        | I3           | Charlie         | A     |

The functional dependencies in this table are:

- Student ID, Course ID -> Instructor ID, Grade
- Instructor ID -> Instructor Name

The candidate keys are:

- Student ID, Course ID
- Student ID, Instructor ID
- Course ID, Instructor ID

This table is not in BCNF because the functional dependency Instructor ID -> Instructor Name violates the BCNF condition. The left-hand side, Instructor ID, is not a superkey of the table. This causes redundancy and inconsistency in the data, as the same instructor name is repeated for different courses.

To convert this table into BCNF, we need to decompose it into two tables:

- Student_Course: Student ID, Course ID, Instructor ID, Grade
- Instructor: Instructor ID, Instructor Name

The Student_Course table has the functional dependency Student ID, Course ID -> Instructor ID, Grade, and the candidate key Student ID, Course ID. This table is in BCNF because the left-hand side of the functional dependency is a superkey.

The Instructor table has the functional dependency Instructor ID -> Instructor Name, and the candidate key Instructor ID. This table is also in BCNF because the left-hand side of the functional dependency is a superkey.

The two tables are linked by the Instructor ID attribute, which is a foreign key in the Student_Course table and a primary key in the Instructor table. This way, we can avoid the redundancy and inconsistency in the original table, and still retrieve the information we need by joining the two tables.

## Advantages of BCNF

Some of the advantages of BCNF are:

- It reduces data redundancy and duplication, which saves storage space and improves data quality.
- It eliminates update anomalies, which occur when the same data is updated in one place but not in another, leading to inconsistency and errors.
- It simplifies the queries and operations on the data, as the tables are smaller and more normalized.



# Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that states that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency is less prevalent than functional dependency, join dependency and multivalued dependency .
- Inclusion dependency can be represented by the notation R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ means "is contained in" .
- Inclusion dependency holds for a database if every tuple that is a member of the relation corresponding to the left-hand side is also in the relation corresponding to the right-hand side.
- Inclusion dependency can be checked by performing a natural join of the two relations and comparing the result with the left-hand side relation.
- Inclusion dependency can be enforced by using triggers or assertions in the database system.

: https://www.scaler.com/topics/dbms/inclusion-dependency-in-dbms/
: https://www.w3schools.blog/inclusion-dependency-in-dbms/
: https://link.springer.com/chapter/10.1007/978-3-663-12018-6_6



# Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of R1, R2, ... gives back the original relation R. 
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data.  
- Lossless join decomposition is also known as non-additive join decomposition. 
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the set of functional dependencies of R:  
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- The above condition can be checked using the chase algorithm, which is a method of applying the functional dependencies to a test relation until a fixed point is reached.  
- If the decomposition is lossless, the test relation will have the same number of tuples as the original relation R. Otherwise, the decomposition is lossy and some tuples will be added or deleted.  

## Examples

- Consider the relation R(A, B, C) with the functional dependencies A → B and B → C. A possible decomposition of R is R1(A, B) and R2(B, C). This decomposition is lossless because R1 ∩ R2 = B and B → R1.  
- Consider the relation R(A, B, C, D) with the functional dependencies A → B and C → D. A possible decomposition of R is R1(A, B) and R2(C, D). This decomposition is lossy because R1 ∩ R2 = ∅ and there is no functional dependency involving the empty set.



# Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Functional dependencies (FDs) are used to express the constraints between attributes in a relation. A functional dependency FD: X -> Y means that the values of Y are determined by the values of X. Two tuples sharing the same values of X will necessarily have the same values of Y.

Some of the common normal forms are:

- First normal form (1NF): A relation is in 1NF if every attribute is atomic, i.e., it cannot be further decomposed into smaller parts. For example, a relation with an attribute that stores a list of values is not in 1NF.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., it does not depend on a proper subset of the primary key. For example, a relation with a composite primary key (A, B) and a non-key attribute C that depends only on A is not in 2NF.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., it does not depend on another non-key attribute. For example, a relation with a primary key A and non-key attributes B and C, where B -> C, is not in 3NF.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there is no non-trivial FD where the left-hand side is not a candidate key. For example, a relation with a candidate key A and a non-key attribute B, where A -> B and B -> A, is not in BCNF.

The process of normalization using FDs involves the following steps:

- Identify all the FDs that hold in the relation.
- Check if the relation satisfies the desired normal form. If not, proceed to the next step.
- Decompose the relation into smaller relations that preserve the FDs and satisfy the desired normal form. This may involve finding a minimal cover of the FDs, i.e., a set of FDs that is equivalent to the original set but has no redundant FDs.
- Repeat the process for each of the smaller relations until all of them are in the desired normal form.

Normalization using FDs can help to achieve a better database design that avoids redundancy and anomalies, such as insertion, deletion, and update anomalies. However, normalization may also have some drawbacks, such as loss of performance, increased complexity, and loss of semantic information. Therefore, normalization should be balanced with other design considerations, such as user requirements, query efficiency, and data integrity.



# MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for **Multivalued Dependency**, which is a type of constraint between two sets of attributes in a relation.
- MVD means that for a single value of attribute `a`, multiple values of attribute `b` exist. For example, if a person named Geeks is working on two projects Microsoft and Oracle and has two hobbies Reading and Music, then the relation has MVD as follows:

| Name | Project | Hobby |
|------|---------|-------|
| Geeks | Microsoft | Reading |
| Geeks | Microsoft | Music |
| Geeks | Oracle | Reading |
| Geeks | Oracle | Music |

- We write MVD as `a --> --> b`, which is read as `a` is multivalued dependent on `b`.
- MVD plays a role in the **Fourth Normal Form (4NF)** of database normalization. Normalization is a process of organizing the data in a database to avoid redundancy, inconsistency, and anomalies.
- A relation is in 4NF if it is in **Boyce-Codd Normal Form (BCNF)** and has no MVD. BCNF is a stricter version of **Third Normal Form (3NF)**, which requires that every determinant in a relation is a candidate key.
- To remove MVD from a relation, we can use the following steps:
  - Identify the MVD in the relation, such as `a --> --> b`.
  - Decompose the relation into two relations, one with attributes `a` and `b`, and the other with attributes `a` and the rest of the attributes.
  - Check if the resulting relations are in 4NF, and repeat the process if necessary.
- For example, to remove the MVD from the relation above, we can decompose it into two relations as follows:

| Name | Project |
|------|---------|
| Geeks | Microsoft |
| Geeks | Oracle |

| Name | Hobby |
|------|-------|
| Geeks | Reading |
| Geeks | Music |

- These two relations are in 4NF, as they have no MVD and are in BCNF.



# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database system.
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and mapping them to tables and columns in a relational schema.
- Database design also involves choosing appropriate data types, indexes, keys, and integrity rules to ensure data quality, consistency, and performance.

## Normalization
- Normalization is a database design technique, which is used to design a relational database table up to higher normal form.
- The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization aims to reduce data redundancy, eliminate data anomalies, and improve data integrity by organizing the data into tables and columns that are related and independent.
- Normalization also simplifies the database design and makes it easier to query, update, and maintain the data.

## Normal Forms
- Normal forms are the levels of normalization that a database table can achieve based on certain rules and criteria.
- The most common normal forms are the first normal form (1NF), the second normal form (2NF), the third normal form (3NF), and the Boyce-Codd normal form (BCNF).
- Each normal form has a set of requirements that a table must satisfy to be in that normal form. For example, to be in 1NF, a table must have no repeating groups, no multivalued attributes, and a primary key. To be in 2NF, a table must be in 1NF and have no partial dependencies. To be in 3NF, a table must be in 2NF and have no transitive dependencies. To be in BCNF, a table must be in 3NF and have no non-trivial functional dependencies that are not determined by a candidate key  .
- Higher normal forms, such as the fourth normal form (4NF) and the fifth normal form (5NF), exist but are less commonly used in practice. They deal with more complex types of dependencies and relationships, such as multivalued dependencies and join dependencies.

## Normalization Example
- To illustrate the normalization process, let us consider a simple example of a database that stores information about students, courses, and grades. The database has one table called Student_Course_Grade, which has the following columns and sample data:

| Student_ID | Student_Name | Course_ID | Course_Name | Grade |
|------------|--------------|-----------|-------------|-------|
| 101        | Alice        | C101      | Math        | A     |
| 101        | Alice        | C102      | English     | B     |
| 102        | Bob          | C101      | Math        | C     |
| 102        | Bob          | C103      | Science     | A     |
| 103        | Charlie      | C102      | English     | A     |
| 103        | Charlie      | C103      | Science     | B     |

- This table is not in 1NF, because it has repeating groups of Course_ID, Course_Name, and Grade for each student. To convert it to 1NF, we need to remove the repeating groups and create a separate row for each combination of Student_ID and Course_ID. The resulting table is:

| Student_ID | Student_Name | Course_ID | Course_Name | Grade |
|------------|--------------|-----------|-------------|-------|
| 101        | Alice        | C101      | Math        | A     |
| 101        | Alice        | C102      | English     | B     |
| 102        | Bob          | C101      | Math        | C     |
| 102        | Bob          | C103      | Science     | A     |
| 103        | Charlie      | C102      | English     | A     |
| 103        | Charlie      | C103      | Science     | B     |

- This table is now in 1NF, but not in 2NF, because it has partial dependencies. For example, the Student_Name column depends only on the Student_ID column, and the Course_Name column depends only on the Course_ID column. These columns are not fully dependent on the primary key, which is the combination of Student_ID and Course_ID. To convert it to 2NF, we need to remove the partial dependencies and create separate tables for



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on alternative approaches to database design for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System.

# Alternative Approaches to Database Design

- Database design is the process of defining the structure, organization, and relationships of data in a database.
- Database design can be influenced by various factors, such as the requirements of the application, the characteristics of the data, the performance and scalability needs, and the preferences of the database designer.
- There are different approaches and techniques for database design, each with its own advantages and disadvantages. Some of the common ones are:

## Top-Down Design Method

- This approach starts with identifying the main entities and relationships of the data domain, and then refining them into smaller and more detailed components.
- This approach is also known as the **conceptual design** or the **entity-relationship (ER) model**.
- The advantages of this approach are:
  - It helps to capture the overall picture and the business rules of the data domain.
  - It facilitates communication and validation with the stakeholders and users of the database.
  - It provides a logical and consistent foundation for the physical design and implementation of the database.
- The disadvantages of this approach are:
  - It can be difficult and time-consuming to identify all the entities and relationships in a complex data domain.
  - It can be challenging to map the conceptual design to the physical design, especially when dealing with different database management systems (DBMS) and data types.
  - It can result in data redundancy and dependency if the normalization rules are not applied properly.

## Bottom-Up Design Method

- This approach starts with identifying the data elements and attributes that are needed for the application, and then grouping them into tables and columns.
- This approach is also known as the **physical design** or the **relational model**.
- The advantages of this approach are:
  - It helps to optimize the performance and storage of the database, by minimizing the data redundancy and dependency.
  - It facilitates the implementation and maintenance of the database, by using the features and functions of the DBMS and the data types.
  - It provides a flexible and adaptable design that can accommodate changes and additions to the data and the application.
- The disadvantages of this approach are:
  - It can lose the meaning and context of the data, by focusing on the technical aspects rather than the business aspects.
  - It can create difficulties in communication and validation with the stakeholders and users of the database, who may not understand the technical terms and details.
  - It can result in data inconsistency and integrity problems if the constraints and rules are not defined and enforced properly.

## Alternative Techniques for Database Design

- Besides the top-down and bottom-up methods, there are other techniques that can be used to design a database, such as:

### Normalization

- This technique is used to organize the data into tables and columns, by applying a set of rules and principles that reduce the data redundancy and dependency.
- The advantages of this technique are:
  - It improves the data quality and consistency, by avoiding the insertion, update, and deletion anomalies.
  - It simplifies the data manipulation and querying, by reducing the number of joins and calculations.
  - It enhances the data security and integrity, by enforcing the primary keys and foreign keys.
- The disadvantages of this technique are:
  - It can increase the complexity and overhead of the database, by creating more tables and columns.
  - It can degrade the performance and scalability of the database, by increasing the number of disk accesses and network transfers.
  - It can limit the flexibility and functionality of the database, by restricting the data types and operations.

### Denormalization

- This technique is used to combine the data from multiple tables and columns, by relaxing or violating some of the normalization rules and principles.
- The advantages of this technique are:
  - It improves the performance and scalability of the database, by reducing the number of disk accesses and network transfers.
  - It enhances the flexibility and functionality of the database, by allowing more data types and operations.
  - It simplifies the data manipulation and querying, by reducing the number of joins and calculations.
- The disadvantages of this technique are:
  - It reduces the data quality and consistency, by introducing the insertion, update, and deletion anomalies.
  - It complicates the data security and integrity, by weakening the primary keys and foreign keys.
  - It increases the complexity and overhead of the database, by creating more data redundancy and dependency.

### No



## Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- SQL statements are composed of keywords, clauses, expressions, operators, and identifiers that follow a specific syntax and semantics.
- SQL statements can be executed interactively through a command-line interface, or embedded in a host programming language, such as Java, C#, or Python.
- SQL supports various data types, such as numeric, character, date, time, interval, boolean, and binary.
- SQL allows users to define constraints, such as primary keys, foreign keys, unique, not null, and check, to enforce data integrity and consistency.
- SQL provides various functions, such as aggregate, string, numeric, date, and conversion functions, to perform calculations and transformations on data.
- SQL supports various operators, such as arithmetic, comparison, logical, bitwise, and set operators, to perform operations on data.
- SQL supports various clauses, such as select, from, where, group by, having, order by, and limit, to specify the data to be retrieved, filtered, grouped, aggregated, sorted, and limited.
- SQL supports various joins, such as inner join, left join, right join, full join, and cross join, to combine data from multiple tables based on a common condition.
- SQL supports various subqueries, such as scalar, correlated, and derived subqueries, to nest one query inside another query.
- SQL supports various views, such as base views and materialized views, to create virtual tables based on a query.
- SQL supports various indexes, such as clustered, non-clustered, and bitmap indexes, to speed up data retrieval and sorting.
- SQL supports various transactions, such as commit, rollback, and savepoint, to ensure the atomicity, consistency, isolation, and durability (ACID) properties of data changes.
- SQL supports various commands, such as grant, revoke, and audit, to control the access and privileges of users and roles on database objects.



# Basics of SQL

SQL stands for **Structured Query Language** and it is a language to operate databases . It is used to perform operations on the records stored in the database, such as updating records, inserting records, deleting records, creating and modifying database tables, views, etc.

SQL is not a database system, but it is a query language that can be used with various database systems, such as MySQL, SQL Server, MS Access, Oracle, Sybase, Informix, Postgres, and other database systems.

SQL is a standard language that became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987.

SQL can perform four basic operations on the data in the database, which are known as **CRUD** operations. CRUD stands for **Create, Read, Update and Delete**.

- You can create new data with **INSERT** statements.
- You can read data with **SELECT** statements.
- You can update data with **UPDATE** statements.
- You can delete data with **DELETE** statements.

SQL also has other features, such as:

- You can create and modify database tables with **CREATE** and **ALTER** statements.
- You can create and modify views with **CREATE VIEW** and **ALTER VIEW** statements.
- You can create and modify stored procedures and functions with **CREATE PROCEDURE**, **CREATE FUNCTION**, **ALTER PROCEDURE** and **ALTER FUNCTION** statements.
- You can create and modify triggers with **CREATE TRIGGER** and **ALTER TRIGGER** statements.
- You can create and modify indexes with **CREATE INDEX** and **ALTER INDEX** statements.
- You can create and modify constraints with **CREATE CONSTRAINT** and **ALTER CONSTRAINT** statements.
- You can control the access and permissions of the database objects with **GRANT** and **REVOKE** statements.
- You can join data from multiple tables with **JOIN** clauses.
- You can filter and sort data with **WHERE** and **ORDER BY** clauses.
- You can group and aggregate data with **GROUP BY** and **HAVING** clauses.
- You can use subqueries and common table expressions with **SELECT** statements.
- You can use various operators and functions to manipulate data, such as arithmetic, logical, comparison, string, date, aggregate, etc.

SQL is a powerful and versatile language that can help you to work with data in databases. You can learn more about SQL syntax and examples from various online resources, such as .



# DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that are used to create, modify, and delete database objects such as tables, views, indexes, schemas, etc.
- DDL commands do not affect the data stored in the database, but only the structure or schema of the database.
- Some of the common DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc. For example, the following statement creates a table named `students` with four columns: `id`, `name`, `age`, and `grade`.

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT CHECK (age > 0),
      grade CHAR(1) CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
    );
    ```

  - ALTER: This command is used to modify an existing database object, such as adding, dropping, or renaming columns, changing data types, adding or removing constraints, etc. For example, the following statement adds a new column named `email` to the `students` table.

    ```sql
    ALTER TABLE students
    ADD email VARCHAR(100) UNIQUE;
    ```

  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc. For example, the following statement drops the `students` table from the database.

    ```sql
    DROP TABLE students;
    ```

  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, etc. For example, the following statement renames the `students` table to `learners`.

    ```sql
    RENAME TABLE students TO learners;
    ```

  - TRUNCATE: This command is used to delete all the data from a table, but not the table itself. It is faster than using the `DELETE` command, which is a DML command. For example, the following statement deletes all the data from the `students` table.

    ```sql
    TRUNCATE TABLE students;
    ```

- DDL commands are normally executed by database administrators or developers, who have the necessary permissions to create or modify the database schema. They are not used by general users, who access the database through applications or queries.



# DML

Data Manipulation Language (DML) is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views  . The main DML statements are:

- **SELECT**: retrieve data from one or more tables or views .
- **INSERT**: add new rows of data to a table or view  .
- **UPDATE**: modify existing rows of data in a table or view  .
- **DELETE**: remove existing rows of data from a table or view  .

DML statements can be used with various clauses, such as WHERE, ORDER BY, GROUP BY, HAVING, JOIN, etc., to filter, sort, aggregate, and combine data from different sources.

DML statements can also be used with subqueries, which are nested queries that return a set of rows or a single value to be used by the outer query.

DML statements can be executed interactively or embedded in a program, such as a stored procedure, a function, or a trigger.

DML statements can affect the data in the database, so they need to be executed within a transaction, which is a logical unit of work that ensures data consistency and integrity.

Some examples of DML statements are:

- SELECT * FROM Customers; -- retrieve all the data from the Customers table
- INSERT INTO Customers (CustomerID, Name, City) VALUES (101, 'Alice', 'New York'); -- insert a new row into the Customers table
- UPDATE Customers SET City = 'Los Angeles' WHERE CustomerID = 101; -- update the city of the customer with ID 101
- DELETE FROM Customers WHERE CustomerID = 101; -- delete the customer with ID 101 from the Customers table



# DCL

Data Control Language (DCL) is a sublanguage of SQL that is used to control the access and permissions of data stored in a database. DCL allows the database owner or administrator to grant, revoke, or modify the privileges of different users or roles on the database objects, such as tables, views, procedures, etc. DCL is mainly used for enforcing data security and ensuring data integrity  .

The main DCL commands in SQL are:

- **GRANT**: This command is used to grant (give access to) specific privileges to a user or a role on a database object. For example, `GRANT SELECT ON employees TO user1;` grants the privilege of selecting data from the `employees` table to the user `user1` .
- **REVOKE**: This command is used to revoke (take away) specific privileges from a user or a role on a database object. For example, `REVOKE UPDATE ON employees FROM user1;` revokes the privilege of updating data in the `employees` table from the user `user1` .
- **DENY**: This command is used to deny (prevent) specific privileges to a user or a role on a database object. For example, `DENY INSERT ON employees TO user1;` denies the privilege of inserting data into the `employees` table to the user `user1` .

Some other DCL commands that are less commonly used are:

- **AUDIT**: This command is used to enable or disable the auditing of database activities by a user or a role. For example, `AUDIT SELECT ON employees BY user1;` enables the auditing of select statements on the `employees` table by the user `user1`.
- **COMMENT**: This command is used to add or modify a comment on a database object. For example, `COMMENT ON TABLE employees IS 'This table stores employee information';` adds a comment on the `employees` table.

DCL commands are important for managing the security and integrity of the database, as they allow the database owner or administrator to control who can access, modify, or manipulate the data and how. DCL commands also help to audit the database activities and document the database objects.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some advantages of SQL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

# Advantages of SQL

- **Faster and efficient query processing**: SQL can process a large amount of data in a very short amount of time. This high speed can boost the amount of data retrieval and manipulation  .
- **No coding skills required**: For data retrieval, large number of lines of code is not required. All basic keywords such as SELECT, INSERT, UPDATE, DELETE, etc. are easy to learn and use.
- **Standardized language**: SQL is a standardized language that is widely used and supported by many database management systems such as MySQL, Oracle, SQL Server, etc. This makes it easier to transfer data and skills across different platforms  .
- **Integration**: SQL is also beneficial for integrating data from multiple sources and applications. SQL can be used to query data from different databases, web services, APIs, etc. and combine them into a single result.
- **Data analysis and decision making**: SQL is also useful for performing data analysis and making better business decisions from data. SQL can be used to perform various operations such as filtering, sorting, grouping, aggregating, joining, etc. on data and generate insights and reports .



# SQL Data Types and Literals

## Data Types
- SQL data types are used to represent the nature of the data that can be stored in the database table  .
- Every field or column in a table is given a data type when a table is defined .
- Data types can be categorized into numeric, character, date and time, and binary types .
- Some common data types are:

| Data Type | Description | Example |
| --- | --- | --- |
| INT | Integer numbers | 42 |
| DECIMAL | Decimal numbers with a fixed precision and scale | 3.14 |
| FLOAT | Floating-point numbers with an approximate precision | 1.23E4 |
| CHAR | Fixed-length character strings | 'Hello' |
| VARCHAR | Variable-length character strings | 'World' |
| DATE | Dates in the format YYYY-MM-DD | '2021-12-15' |
| TIME | Times in the format HH:MM:SS | '22:11:27' |
| DATETIME | Dates and times in the format YYYY-MM-DD HH:MM:SS | '2021-12-15 22:11:27' |
| BIT | Binary values | 0 or 1 |
| BLOB | Binary large objects | Image files |

## Literals
- Literals are constant values that can be used in SQL statements .
- Literals can be of four kinds: character string, bit string, exact numeric, and approximate numeric.
- Character string literals are written as a sequence of characters enclosed in single quotes . For example, 'Hello'.
- Bit string literals are written as a sequence of 0s and 1s preceded by a B and enclosed in single quotes. For example, B'1010'.
- Exact numeric literals are written as a sequence of digits, optionally with a decimal point and a sign . For example, 42, -3.14, +100.
- Approximate numeric literals are written as a sequence of digits, with a decimal point, a sign, and an exponent . For example, 1.23E4, -6.78E-2, +9.0E+3.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of types of SQL commands:

# Types of SQL commands

SQL (Structured Query Language) is a standard language for manipulating and querying data in relational databases. SQL commands can be classified into four main categories:

- **Data Definition Language (DDL)**: These commands are used to create, alter, or drop database objects such as tables, views, indexes, schemas, etc. Some examples of DDL commands are:

  - `CREATE`: This command is used to create a new database object, such as a table or a view.
  - `ALTER`: This command is used to modify the structure or properties of an existing database object, such as adding or dropping a column or a constraint.
  - `DROP`: This command is used to delete an existing database object, such as a table or a view.
  - `RENAME`: This command is used to change the name of an existing database object, such as a table or a view.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - `INSERT`: This command is used to add one or more rows of data to a table.
  - `UPDATE`: This command is used to modify one or more rows of data in a table.
  - `DELETE`: This command is used to remove one or more rows of data from a table.
  - `SELECT`: This command is used to query data from one or more tables, optionally with filters, joins, aggregations, etc.

- **Data Control Language (DCL)**: These commands are used to grant or revoke permissions or access rights to database objects or users. Some examples of DCL commands are:

  - `GRANT`: This command is used to give a user or a role the privilege to perform certain actions on a database object, such as selecting, inserting, updating, or deleting data.
  - `REVOKE`: This command is used to take away a privilege that was previously granted to a user or a role on a database object.
  - `DENY`: This command is used to prevent a user or a role from performing certain actions on a database object, even if they have been granted the privilege by another user or role.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions that modify the data in the database. Transactions are a set of DML commands that are executed as a single unit, either all or none. Some examples of TCL commands are:

  - `BEGIN`: This command is used to start a new transaction.
  - `COMMIT`: This command is used to end a transaction and save the changes made by the DML commands in the transaction.
  - `ROLLBACK`: This command is used to undo the changes made by the DML commands in the transaction and restore the data to its previous state.
  - `SAVEPOINT`: This command is used to create a point in the transaction that can be used to rollback to in case of an error or a partial failure.



# SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They are used to specify conditions, filter results, compare values, perform calculations, concatenate strings, and more. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used to perform mathematical operations on numerical data, such as addition, subtraction, multiplication, division, modulus, and exponentiation. For example, `SELECT 10 + 5;` returns 15.
- Comparison operators: These operators are used to compare two values or expressions and return a Boolean value (true or false). For example, `SELECT 10 > 5;` returns true. Some common comparison operators are `=`, `<>`, `<`, `>`, `<=`, `>=`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`, and `EXISTS`.
- Logical operators: These operators are used to combine two or more conditions and return a Boolean value. For example, `SELECT * FROM customers WHERE age > 18 AND gender = 'F';` returns all female customers who are older than 18. Some common logical operators are `AND`, `OR`, `NOT`, and `ANY`.
- Bitwise operators: These operators are used to perform bit-level operations on binary data, such as bitwise AND, OR, XOR, NOT, and shift. For example, `SELECT 10 & 5;` returns 0, which is the result of performing bitwise AND on the binary representations of 10 and 5. Some common bitwise operators are `&`, `|`, `^`, `~`, `<<`, and `>>`.
- String operators: These operators are used to manipulate character data, such as concatenation, extraction, conversion, and trimming. For example, `SELECT 'Hello' + ' ' + 'World';` returns 'Hello World', which is the result of concatenating two strings. Some common string operators are `+`, `SUBSTRING`, `UPPER`, `LOWER`, `LTRIM`, and `RTRIM`.
- Set operators: These operators are used to combine the results of two or more queries into a single result set, such as union, intersection, and difference. For example, `SELECT name FROM customers UNION SELECT name FROM suppliers;` returns the names of both customers and suppliers, without any duplicates. Some common set operators are `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT`.



# Tables – Creation & Alteration

- A table is a collection of related data organized in rows and columns in a database.
- To create a table in SQL, use the `CREATE TABLE` statement, followed by the name of the table and the definition of its columns and constraints.
- For example, to create a table called `Students` with four columns: `id`, `name`, `age`, and `grade`, the syntax would be:

```sql
CREATE TABLE Students (
  id int,
  name varchar(50),
  age int,
  grade char(1)
);
```

- To modify the structure of an existing table, use the `ALTER TABLE` statement, followed by the name of the table and the changes to be made.
- The `ALTER TABLE` statement can be used to add, delete, or modify columns, as well as to add or delete constraints in a table.
- For example, to add a new column called `email` to the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
ADD email varchar(50);
```

- To delete a column from a table, use the `DROP COLUMN` clause with the `ALTER TABLE` statement. For example, to delete the `grade` column from the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
DROP COLUMN grade;
```

- To change the data type or size of a column, use the `ALTER COLUMN` clause with the `ALTER TABLE` statement. For example, to change the data type of the `age` column from `int` to `smallint`, the syntax would be:

```sql
ALTER TABLE Students
ALTER COLUMN age smallint;
```

- To add a constraint to a table, use the `ADD CONSTRAINT` clause with the `ALTER TABLE` statement. A constraint is a rule that restricts the values that can be stored in a column or a combination of columns. Some common types of constraints are: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and `CHECK`.
- For example, to add a primary key constraint to the `id` column of the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
ADD CONSTRAINT pk_students PRIMARY KEY (id);
```

- To delete a constraint from a table, use the `DROP CONSTRAINT` clause with the `ALTER TABLE` statement. For example, to delete the primary key constraint from the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
DROP CONSTRAINT pk_students;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` statement, followed by the name of the new table and a query that selects the data from the existing table.
- For example, to create a new table called `Students_backup` that is a copy of the `Students` table, the syntax would be:

```sql
CREATE TABLE Students_backup AS
SELECT * FROM Students;
```

- To delete a table from a database, use the `DROP TABLE` statement, followed by the name of the table to be deleted.
- For example, to delete the `Students_backup` table, the syntax would be:

```sql
DROP TABLE Students_backup;
```

- To delete all the data from a table, but keep the table structure, use the `TRUNCATE TABLE` statement, followed by the name of the table to be emptied.
- For example, to delete all the data from the `Students` table, the syntax would be:

```sql
TRUNCATE TABLE Students;
```

- Note: The `TRUNCATE TABLE` statement is faster and more efficient than the `DELETE` statement, but it cannot be rolled back.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of defining constraints for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System.

# Defining Constraints

- Constraints are rules that are applied to the data in a table to ensure its validity and integrity.
- Constraints can be defined at the column level or the table level, depending on the scope of the rule.
- Constraints can be specified when creating a table using the CREATE TABLE statement, or after creating a table using the ALTER TABLE statement.
- Some of the common types of constraints are:

  - **NOT NULL**: This constraint ensures that a column cannot have a null value. For example, `CREATE TABLE employee (emp_id INT NOT NULL, name VARCHAR(50) NOT NULL, salary DECIMAL(10,2));`
  - **UNIQUE**: This constraint ensures that a column or a combination of columns has a unique value for each row. For example, `CREATE TABLE employee (emp_id INT UNIQUE, name VARCHAR(50) NOT NULL, salary DECIMAL(10,2));`
  - **PRIMARY KEY**: This constraint combines the NOT NULL and UNIQUE constraints, and identifies a column or a combination of columns as the primary key of the table. For example, `CREATE TABLE employee (emp_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, salary DECIMAL(10,2));`
  - **FOREIGN KEY**: This constraint establishes a relationship between a column or a combination of columns in one table and the primary key of another table. For example, `CREATE TABLE department (dept_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL); CREATE TABLE employee (emp_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, salary DECIMAL(10,2), dept_id INT, FOREIGN KEY (dept_id) REFERENCES department(dept_id));`
  - **CHECK**: This constraint allows specifying a condition that the data in a column or a table must satisfy. For example, `CREATE TABLE employee (emp_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, salary DECIMAL(10,2), dept_id INT, FOREIGN KEY (dept_id) REFERENCES department(dept_id), CHECK (salary > 0));`
  - **DEFAULT**: This constraint allows specifying a default value for a column that is used when no value is provided for that column. For example, `CREATE TABLE employee (emp_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, salary DECIMAL(10,2) DEFAULT 10000, dept_id INT, FOREIGN KEY (dept_id) REFERENCES department(dept_id));`

- Constraints can be named or unnamed. If a constraint is unnamed, the system generates a name for it. For example, `CREATE TABLE employee (emp_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, salary DECIMAL(10,2), dept_id INT, FOREIGN KEY (dept_id) REFERENCES department(dept_id), CONSTRAINT salary_check CHECK (salary > 0));`
- Constraints can be enabled or disabled, depending on the need. For example, `ALTER TABLE employee DISABLE CONSTRAINT salary_check;`
- Constraints can be dropped or modified, using the ALTER TABLE statement. For example, `ALTER TABLE employee DROP CONSTRAINT salary_check; ALTER TABLE employee MODIFY CONSTRAINT salary_check CHECK (salary >= 5000);`



# Views and Indexes in SQL

## Views

- A view is a virtual table that contains data from one or more tables based on a SELECT query.
- A view does not store any data physically, but only shows the result of the query when it is referenced.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface for different users.
- A view can be created using the CREATE VIEW statement, and can be modified using the ALTER VIEW statement.
- A view can be dropped using the DROP VIEW statement, or renamed using the SP_RENAME stored procedure.
- A view can be queried, updated, inserted, or deleted from, as long as it follows certain rules.
- Some of the rules for modifying data through a view are:
  - The view must include the primary key of the underlying table.
  - The view must not contain any aggregate functions, DISTINCT, GROUP BY, HAVING, or SET operators.
  - The view must not contain any subqueries, joins, or derived tables.
  - The view must not contain any computed columns or non-deterministic functions.
  - The view must not contain any TOP or ORDER BY clauses.

## Indexes

- An index is a data structure that improves the speed of data retrieval from a table or a view.
- An index is created on one or more columns of a table or a view, and stores the values of those columns in a sorted order.
- An index can be used by the query optimizer to find the rows that match a search condition more efficiently, without scanning the entire table or view.
- An index can be created using the CREATE INDEX statement, and can be modified using the ALTER INDEX statement.
- An index can be dropped using the DROP INDEX statement, or disabled using the DISABLE INDEX statement.
- An index can be clustered or non-clustered, depending on how the data is physically stored.
- A clustered index determines the order of the data in the table or view, and can only be one per table or view.
- A non-clustered index does not affect the order of the data in the table or view, and can be multiple per table or view.
- A non-clustered index can also include additional columns that are not part of the index key, to avoid accessing the table or view for those columns.
- An indexed view is a view that has a unique clustered index on it, and is stored in the database like a table  .
- An indexed view can improve the performance of queries that join or aggregate data from multiple tables or views  .
- An indexed view has some limitations and requirements, such as:
  - The view must be created with the SCHEMABINDING option, which means it cannot reference any objects outside the current database or schema.
  - The view must not reference any tables or views that use temporary tables, table variables, or table-valued parameters.
  - The view must not reference any user-defined functions, or any system functions that are not deterministic or precise.
  - The view must not contain any outer or self joins, or any APPLY operators.
  - The view must not contain any UNION, INTERSECT, or EXCEPT operators, or any subqueries or derived tables.
  - The view must not contain any DISTINCT, TOP, or ORDER BY clauses, or any aggregate functions that are not COUNT_BIG.
  - The view must not contain any full-text predicates, or any expressions that involve collation changes or implicit conversions.
  - The view must not contain any modifications of data, such as INSERT, UPDATE, DELETE, or MERGE statements.
  - The view must not reference any views that are not indexed themselves.
  - The view must be referenced by the query optimizer using the NOEXPAND hint, or the database compatibility level must be 90 or higher.



# Queries and Subqueries in SQL

## Queries
- A query is a request for data or information from a database table or combination of tables.
- A query can be written in SQL, which is a standard language for accessing and manipulating databases.
- A query can perform various operations on the data, such as selecting, filtering, sorting, grouping, aggregating, joining, etc.
- A query can return a result set, which is a collection of rows that match the criteria specified in the query.
- A query can also modify the data in the database, such as inserting, updating, or deleting records.
- A query can be executed by a database management system (DBMS), which is a software that manages the storage and retrieval of data in a database.

## Subqueries
- A subquery is a query within another query, also known as a nested query or an inner query.
- A subquery can be used to return data that will be used in the main query as a condition to further restrict the data to be retrieved.
- A subquery can also be used to return data that will be used in the main query as a value or an expression.
- A subquery can be placed in various clauses of the main query, such as the WHERE clause, the HAVING clause, the FROM clause, or the SELECT clause.
- A subquery can return a single value, a single row, a single column, or a table of values or rows.
- A subquery can be correlated or non-correlated. A correlated subquery is a subquery that depends on the outer query for its values, and is executed once for each row of the outer query. A non-correlated subquery is a subquery that does not depend on the outer query for its values, and is executed only once for the entire outer query.



# Aggregate Functions

Aggregate functions are special functions in SQL that perform calculations on a set of values and return a single value. They are often used with the GROUP BY clause to summarize data into groups, and with the HAVING clause to filter groups based on a condition.

Some of the common aggregate functions in SQL are:

- **AVG**: Returns the average of the values in a column.
- **COUNT**: Returns the number of rows in a table or the number of non-null values in a column.
- **MAX**: Returns the maximum value in a column.
- **MIN**: Returns the minimum value in a column.
- **SUM**: Returns the sum of the values in a column.

To use an aggregate function, you need to specify the column name as an argument inside parentheses. For example, to find the average salary of employees in a table called `employees`, you can write:

```sql
SELECT AVG(salary) FROM employees;
```

You can also use aggregate functions with the `DISTINCT` keyword to eliminate duplicate values before performing the calculation. For example, to find the number of distinct departments in the `employees` table, you can write:

```sql
SELECT COUNT(DISTINCT department) FROM employees;
```

You can also use aggregate functions with the `GROUP BY` clause to divide the rows into groups based on one or more columns, and then apply the aggregate function to each group. For example, to find the average salary of each department in the `employees` table, you can write:

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;
```

You can also use aggregate functions with the `HAVING` clause to filter the groups based on a condition that involves an aggregate function. For example, to find the departments that have more than 10 employees in the `employees` table, you can write:

```sql
SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 10;
```

Some of the other aggregate functions in SQL are:

- **APPROX_COUNT_DISTINCT**: Returns an approximate count of the distinct values in a column.
- **CHECKSUM_AGG**: Returns the checksum of the values in a column.
- **COUNT_BIG**: Returns the number of rows in a table or the number of non-null values in a column as a bigint data type.
- **GROUPING**: Returns a 1 or 0 to indicate whether a row belongs to a subtotal or a grand total of a GROUP BY query.
- **GROUPING_ID**: Returns a bit vector that indicates the grouping level of a row in a GROUP BY query.
- **STDEV**: Returns the standard deviation of the values in a column.
- **STDEVP**: Returns the population standard deviation of the values in a column.
- **STRING_AGG**: Returns a string that concatenates the values in a column with a specified separator.
- **VAR**: Returns the variance of the values in a column.
- **VARP**: Returns the population variance of the values in a column.

For more details and examples of these aggregate functions, you can refer to the search results   .



# Built-in functions

Built-in functions are expressions in which an SQL keyword or special operator executes some operation. They can be used in SQL SELECT expressions to calculate values and manipulate data. They can also be used in other SQL statements, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.

There are different types of built-in functions in SQL, such as:

- **String functions**: These functions perform operations on string values, such as concatenation, extraction, conversion, etc. Some examples of string functions are ASCII, CHAR, CHARINDEX, CONCAT, LEFT, RIGHT, etc.
- **Numeric functions**: These functions perform mathematical operations on numeric values, such as rounding, truncating, finding the absolute value, etc. Some examples of numeric functions are ABS, CEILING, FLOOR, POWER, ROUND, SQRT, etc.
- **Date and time functions**: These functions perform operations on date and time values, such as extracting parts of a date, adding or subtracting intervals, converting formats, etc. Some examples of date and time functions are DATEADD, DATEDIFF, DATEPART, GETDATE, YEAR, MONTH, DAY, etc.
- **Conversion functions**: These functions convert a value from one data type to another, such as from string to numeric, from numeric to date, etc. Some examples of conversion functions are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, etc.
- **Aggregate functions**: These functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause to summarize data. Some examples of aggregate functions are AVG, COUNT, MAX, MIN, SUM, etc.
- **Analytic functions**: These functions compute an aggregate value based on a group of rows. However, unlike aggregate functions, they do not reduce the number of rows returned by the query. They are often used with the OVER clause to partition the data and apply a window function. Some examples of analytic functions are ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD, etc.
- **Bit manipulation functions**: These functions perform bitwise operations on binary values, such as shifting, rotating, anding, oring, etc. Some examples of bit manipulation functions are BITAND, BITOR, BITXOR, BITNOT, BITLSHIFT, BITRSHIFT, etc.
- **System functions**: These functions return information about the system, such as the current user, the current database, the current session, etc. Some examples of system functions are USER, DATABASE, SESSION_USER, @@VERSION, @@ROWCOUNT, @@ERROR, etc.

: https://www.tutorialsteacher.com/sqlserver/builtin-functions



# Unit 5 - Structured Query Language (SQL)

- SQL is a short-form of the structured query language, and it is pronounced as S-Q-L or sometimes as See-Quell.
- SQL is a standardized programming language that is used to manage relational databases and perform various operations on the data in them.
- SQL is supported by many the database systems and languages that you will use including Access, Ingres, Oracle, dBase, FoxBase, and COBOL.
- SQL is not a database system, but it is a query language.
- SQL became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987.
- SQL lets you access and manipulate databases.
- SQL is used to perform operations on the records stored in the database, such as updating records, inserting records, deleting records, creating and modifying database tables, views, etc.
- SQL is a special tool used by data professionals for handling structured data (data which is stored in the form of tables).
- SQL is case insensitive. But it is a recommended practice to use keywords (like SELECT, UPDATE, CREATE, etc) in capital letters and use user defined things (liked table names, column names, etc) in lower case.
- SQL has many sub-languages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).



# Update and Delete Operations in SQL

SQL is a language that allows you to manipulate data in relational databases. SQL has several commands that can perform different operations on data, such as inserting, selecting, updating, and deleting records. These commands are part of the Data Manipulation Language (DML) subset of SQL.

## Update Operation

The update operation is used to modify the existing records in a database table. The syntax of the update command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

The update command requires the name of the table to be updated, the columns and values to be changed, and an optional condition to specify which records to update. If the condition is omitted, all the records in the table will be updated.

For example, to update the salary of an employee with id 101 to 5000, you can use the following command:

```sql
UPDATE employees
SET salary = 5000
WHERE id = 101;
```

You can also update multiple columns in one command, such as changing the name and department of an employee:

```sql
UPDATE employees
SET name = 'John Smith', department = 'Sales'
WHERE id = 101;
```

## Delete Operation

The delete operation is used to remove records from a database table. The syntax of the delete command is:

```sql
DELETE FROM table_name
WHERE condition;
```

The delete command requires the name of the table to be deleted from, and an optional condition to specify which records to delete. If the condition is omitted, all the records in the table will be deleted.

For example, to delete the record of an employee with id 101, you can use the following command:

```sql
DELETE FROM employees
WHERE id = 101;
```

You can also use more complex conditions to delete records, such as deleting all the employees who work in the IT department:

```sql
DELETE FROM employees
WHERE department = 'IT';
```

## Summary

- The update operation is used to modify the existing records in a database table. It requires the name of the table, the columns and values to be changed, and an optional condition to specify which records to update.
- The delete operation is used to remove records from a database table. It requires the name of the table and an optional condition to specify which records to delete.
- Both operations can use the WHERE clause to filter the records based on a condition. If the condition is omitted, all the records in the table will be affected.



# Joins

Joins are used to combine data from two or more tables based on a common column. Joins allow us to query data from multiple sources as if they were a single table.

There are different types of joins in SQL, each with a different way of handling non-matching rows. The most common types of joins are:

- **Inner join**: returns only the rows that match in both tables.
- **Left outer join**: returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right side will be NULL.
- **Right outer join**: returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left side will be NULL.
- **Full outer join**: returns all the rows from both tables, and matches them if possible. If there is no match, both sides will be NULL.
- **Cross join**: returns the Cartesian product of both tables, meaning every possible combination of rows.

The syntax for joining two tables is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

The join condition specifies how the tables are related, usually by comparing a column from each table. The join condition can also use other operators, such as `=`, `<>`, `<`, `>`, etc.

Here is an example of an inner join between two tables, Customers and Orders, based on the CustomerID column:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the customer ID, first name, and order amount for each order placed by a customer. If a customer has not placed any order, or if an order has no customer, they will not be included in the result.

Here is an example of a left outer join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the same columns as the previous one, but it will also include the customers who have not placed any order. In that case, the order amount will be NULL.

Here is an example of a right outer join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
RIGHT JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the same columns as the previous ones, but it will also include the orders that have no customer. In that case, the customer ID and first name will be NULL.

Here is an example of a full outer join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
FULL JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the same columns as the previous ones, but it will also include all the rows from both tables, regardless of whether they have a match or not. If there is no match, both sides will be NULL.

Here is an example of a cross join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
CROSS JOIN Orders;
```

This query will return the same columns as the previous ones, but it will also include every possible combination of rows from both tables. For example, if there are 10 customers and 5 orders, the result will have 50 rows. This type of join is rarely useful, unless you want to generate some test data.

Sources:

: Joins (SQL Server) - SQL Server | Microsoft Learn
: SQL JOIN (With Examples) - Programiz
: SQL Joins - W3Schools
: SQL JOIN - W3Schools



# Unions in SQL

- UNION is an SQL operator that combines the result of two or more SELECT queries and provides a single set in the output  .
- The UNION operator removes any duplicates present in the results being combined .
- Every SELECT statement within UNION must have the same number of columns, the same data types, and the same order .
- The syntax of UNION in SQL is:

```sql
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_1
UNION
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_2
UNION
...
UNION
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_m;
```

- A UNION operation is different from a JOIN operation: A UNION concatenates result sets from two queries, but a UNION does not create individual rows from columns gathered from two tables. A JOIN compares columns from two tables, to create result rows composed of columns from two tables.
- An example of UNION in SQL is:

```sql
-- Create two tables with some data
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE suppliers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'New York'),
(2, 'Bob', 'Los Angeles'),
(3, 'Charlie', 'Chicago');

INSERT INTO suppliers VALUES
(4, 'David', 'New York'),
(5, 'Eve', 'Los Angeles'),
(6, 'Frank', 'Boston');

-- Use UNION to get the names and cities of both customers and suppliers
SELECT name, city FROM customers
UNION
SELECT name, city FROM suppliers
ORDER BY name;

-- The output is:

name    | city
-----------------
Alice   | New York
Bob     | Los Angeles
Charlie | Chicago
David   | New York
Eve     | Los Angeles
Frank   | Boston
```

- Note that the output does not have any duplicates, even though both tables have entries with the same city. If you want to keep the duplicates, you can use UNION ALL instead of UNION  .



Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of intersection in SQL. Here is the content in markdown format:

# Intersection

- The intersection operation in SQL is used to combine two queries and return only the rows that are common to both result sets.
- The syntax of the intersection operation is:

```sql
SELECT column_list
FROM table1
WHERE condition
INTERSECT
SELECT column_list
FROM table2
WHERE condition;
```

- The column_list in both queries must have the same number and order of columns, and the data types must be compatible.
- The intersection operation eliminates any duplicate rows from the final result set.
- The intersection operation is equivalent to the logical AND operation on two sets of data.
- The intersection operation can be used to find the common values in two or more tables, such as customers who have ordered products from different categories, employees who work in multiple departments, or students who have enrolled in multiple courses.
- Here is an example of the intersection operation in SQL:

```sql
-- Find the customers who have ordered both books and electronics
SELECT customer_id, customer_name
FROM orders
WHERE product_category = 'Books'
INTERSECT
SELECT customer_id, customer_name
FROM orders
WHERE product_category = 'Electronics';
```

- The result set of the above query will show the customers who have ordered both books and electronics from the orders table.



# Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several types of statements, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL statements are used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and constraints.
- DML statements are used to insert, update, delete, and merge data in the database tables.
- DCL statements are used to grant and revoke permissions and roles to users and groups for accessing and modifying the database objects.
- DQL statements are used to retrieve and manipulate data from the database tables, such as selecting, joining, filtering, sorting, grouping, and aggregating data.
- SQL supports various data types, such as numeric, character, date, time, boolean, and binary.
- SQL supports various operators, such as arithmetic, comparison, logical, bitwise, and string operators, to perform calculations and comparisons on data values.
- SQL supports various functions, such as aggregate, scalar, conversion, and analytical functions, to perform operations and transformations on data values.
- SQL supports various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT, to specify the conditions and order of the data retrieval and manipulation.
- SQL supports various keywords, such as DISTINCT, AS, IN, BETWEEN, LIKE, NULL, IS, NOT, AND, OR, and CASE, to modify and control the behavior and output of the SQL statements.
- SQL supports various subqueries, such as correlated, uncorrelated, scalar, and table subqueries, to nest one query inside another query and use the result of the inner query in the outer query.
- SQL supports various joins, such as inner, outer, cross, and self joins, to combine data from two or more tables based on a common column or condition.
- SQL supports various constraints, such as primary key, foreign key, unique, not null, check, and default, to enforce the rules and integrity of the data in the database tables.
- SQL supports various indexes, such as clustered, non-clustered, unique, and composite indexes, to improve the performance and efficiency of the data retrieval and manipulation.
- SQL supports various views, such as simple, complex, materialized, and indexed views, to create a virtual table based on the result of a SQL query and provide a logical and abstracted view of the data in the database tables.
- SQL supports various transactions, such as commit, rollback, and savepoint, to ensure the atomicity, consistency, isolation, and durability (ACID) properties of the data manipulation operations.



# Transaction Control Commands

- Transaction control commands are used to manage the changes made by SQL statements in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the statements in a transaction are executed successfully or none of them are executed at all.
- Consistency means that the database remains in a valid state before and after a transaction.
- Isolation means that the changes made by one transaction are not visible to other transactions until the transaction is committed.
- Durability means that the changes made by a committed transaction are permanent and not lost due to system failures.
- The following commands are used to control transactions in SQL:
  - **COMMIT** - This command is used to make a transaction permanent in a database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK** - This command is used to undo the changes made by a transaction. It restores the database to its previous state before the transaction started and ends the current transaction.
  - **SAVEPOINT** - This command is used to create points within a transaction to which the transaction can be rolled back partially. It allows dividing a transaction into smaller subtransactions.
  - **SET TRANSACTION** - This command is used to specify the characteristics of a transaction, such as its isolation level, name, or read-only status.
- SQL Server operates in the following transaction modes:
  - **Autocommit transactions** - Each individual statement is a transaction. It is committed automatically when it completes successfully or rolled back automatically when it fails.
  - **Explicit transactions** - Each transaction is explicitly started with the **BEGIN TRANSACTION** statement and explicitly ended with a **COMMIT** or **ROLLBACK** statement.
  - **Implicit transactions** - A transaction is implicitly started when the first SQL statement is executed after the **SET IMPLICIT_TRANSACTIONS ON** statement. It is ended with a **COMMIT** or **ROLLBACK** statement or when another **SET IMPLICIT_TRANSACTIONS ON** statement is executed.
- A transaction can be explicitly executed as a distributed transaction by using **BEGIN DISTRIBUTED TRANSACTION**. A distributed transaction involves multiple servers or databases that are coordinated by the Microsoft Distributed Transaction Coordinator (MS DTC).



## Unit 6 - PL/SQL

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that allows users to write procedural code in Oracle database.
- PL/SQL supports variables, constants, data types, operators, expressions, control structures, loops, arrays, cursors, exceptions, subprograms, packages, triggers, and object-oriented features.
- PL/SQL code is compiled and stored in the database, and can be executed by using SQL statements such as `EXECUTE`, `CALL`, or `BEGIN`.
- PL/SQL code can also be embedded in SQL statements, such as `SELECT`, `INSERT`, `UPDATE`, or `DELETE`, by using the `PL/SQL` keyword.
- PL/SQL code can interact with SQL data by using the `INTO`, `FROM`, and `RETURNING` clauses, and can use SQL functions, such as `SYSDATE`, `COUNT`, or `MAX`, in expressions.
- PL/SQL code can also use SQL cursors, which are pointers to the result sets of SQL queries, and can fetch, process, and close them using the `OPEN`, `FETCH`, `LOOP`, and `CLOSE` statements.
- PL/SQL code can handle errors and exceptions by using the `EXCEPTION` section, which contains handlers for predefined or user-defined exceptions, and can use the `RAISE` statement to raise an exception explicitly.
- PL/SQL code can modularize and reuse code by using subprograms, which are named blocks of code that can be invoked from other PL/SQL blocks or SQL statements. Subprograms can be either procedures or functions, depending on whether they return a value or not.
- PL/SQL code can also use packages, which are collections of related subprograms, variables, constants, cursors, and exceptions, that can be compiled and stored in the database as a unit. Packages can have a specification and a body, which can be created separately or together.
- PL/SQL code can also use triggers, which are special subprograms that are executed automatically when a certain event occurs on a table or view, such as `INSERT`, `UPDATE`, or `DELETE`. Triggers can be either row-level or statement-level, depending on whether they are executed for each affected row or once per statement.
- PL/SQL code can also use object-oriented features, such as object types, methods, inheritance, polymorphism, and collections, to model complex data structures and behaviors in the database. Object types can have attributes and methods, and can be used as data types for columns, variables, parameters, or return values. Object types can also inherit from other object types, and can be overridden or overloaded by using the `OVERRIDING` and `OVERLOADING` keywords. Collections are data structures that can store multiple values of the same or different data types, and can be either nested tables, varrays, or associative arrays.



# Introduction for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that allows users to write procedural code in a database environment.
- PL/SQL is a block-structured language that consists of statements, expressions, variables, constants, data types, operators, control structures, exceptions, cursors, and subprograms.
- PL/SQL supports features such as modularity, reusability, error handling, and object orientation. It also provides access to SQL commands and data manipulation functions.
- PL/SQL is mainly used for creating stored procedures, functions, triggers, and packages in a database. These are reusable units of code that can be invoked from other PL/SQL blocks or applications.
- PL/SQL can also be used for creating dynamic SQL statements, which are SQL statements that are constructed and executed at run time based on user input or program logic.
- PL/SQL can interact with other languages and environments, such as Java, C, C++, .NET, and Oracle Forms. It can also use external libraries and web services.



# Features of PL/SQL

PL/SQL is a procedural extension of SQL that allows developers to write efficient and compact code for manipulating data in a database. Some of the features of PL/SQL are:

- **Tight integration with SQL**: PL/SQL can use any SQL statement, such as SELECT, INSERT, UPDATE, DELETE, MERGE, etc., within its code. PL/SQL also supports SQL data types, operators, functions, and expressions.
- **Extensive error checking**: PL/SQL can handle errors and exceptions using predefined and user-defined handlers. PL/SQL also provides debugging tools and features, such as breakpoints, watches, and tracebacks.
- **Numerous data types**: PL/SQL supports scalar, composite, reference, and large object (LOB) data types. Scalar data types include numbers, characters, booleans, dates, intervals, etc. Composite data types include records, collections, and object types. Reference data types include pointers, cursors, and REFs. LOB data types include BLOB, CLOB, NCLOB, and BFILE.
- **Variety of programming structures**: PL/SQL supports conditional, iterative, and sequential control structures, such as IF-THEN-ELSE, CASE, LOOP, FOR, WHILE, EXIT, CONTINUE, GOTO, etc. PL/SQL also supports subprograms, such as procedures, functions, packages, triggers, and types.
- **Structured programming**: PL/SQL supports modular and reusable code through subprograms, packages, and types. Subprograms are blocks of code that can be invoked from other subprograms or SQL statements. Packages are collections of related subprograms and variables. Types are user-defined data types that can have attributes and methods.
- **Object-oriented programming**: PL/SQL supports object-oriented features, such as inheritance, polymorphism, encapsulation, and abstraction. Types can be defined as subtypes of other types, and can override or overload methods. Types can also have constructors, destructors, and static methods.
- **Web application development**: PL/SQL can be used to create dynamic web pages and server pages using PL/SQL Server Pages (PSP) and PL/SQL Web Toolkit. PSP allows embedding PL/SQL code within HTML tags, and PL/SQL Web Toolkit provides APIs for generating HTML, XML, JSON, etc. PL/SQL can also interact with web services using SOAP and REST protocols.



# Syntax and Constructs for the Notes of the Unit 6 - PL/SQL

PL/SQL is a procedural extension of SQL that allows you to write complex and modular programs that interact with Oracle databases. PL/SQL programs are composed of blocks, which are the basic units of execution. A block can be nested inside another block, creating a hierarchical structure. A block has the following syntax:

```sql
[DECLARE
  --optional declarations of variables, constants, cursors, exceptions, etc.
]
BEGIN
  --mandatory executable statements. At least one statement is required.
[EXCEPTION
  --optional handlers for errors or exceptions that occur during execution
]
END;
--mandatory end of the block
[/] --optional slash to execute the block
```

Some of the main constructs and features of PL/SQL are:

- **Variables and constants**: You can declare and use scalar, composite, or reference variables and constants in PL/SQL. You can also use bind variables and host variables to pass data between PL/SQL and other environments. Variables and constants have a name, a data type, and an optional initial value. You can use the `%TYPE` and `%ROWTYPE` attributes to declare variables that match the data types of existing database objects.
- **Data types**: PL/SQL supports many data types, including SQL data types (such as `NUMBER`, `VARCHAR2`, `DATE`, etc.), PL/SQL-specific data types (such as `BOOLEAN`, `PLS_INTEGER`, `BINARY_INTEGER`, etc.), user-defined data types (such as `OBJECT`, `VARRAY`, `TABLE`, etc.), and collection data types (such as `ASSOCIATIVE ARRAY`, `NESTED TABLE`, `VARRAY`, etc.).
- **Operators and expressions**: PL/SQL supports various operators and expressions to manipulate data and perform calculations. Operators include arithmetic, comparison, logical, bitwise, string, and set operators. Expressions are combinations of operators, operands, literals, and function calls that evaluate to a single value.
- **Control structures**: PL/SQL provides control structures to alter the flow of execution based on conditions, loops, or branches. Control structures include `IF-THEN-ELSE`, `CASE`, `LOOP`, `EXIT`, `CONTINUE`, `GOTO`, `NULL`, and `RETURN` statements.
- **Cursors**: A cursor is a pointer to a result set of a SQL query. PL/SQL provides two types of cursors: implicit and explicit. An implicit cursor is automatically created and managed by PL/SQL for every SQL statement that returns a single row. An explicit cursor is declared and controlled by the programmer for SQL statements that return multiple rows. You can use cursor attributes, such as `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN`, to check the status of a cursor. You can also use cursor variables, which are pointers to cursors, to pass cursors as parameters to subprograms or to work with multiple result sets.
- **Exceptions**: An exception is an error or an abnormal condition that occurs during the execution of a PL/SQL block. PL/SQL provides predefined exceptions, such as `NO_DATA_FOUND`, `TOO_MANY_ROWS`, `ZERO_DIVIDE`, etc., that are raised automatically by the PL/SQL runtime engine. You can also define your own user-defined exceptions and raise them explicitly with the `RAISE` statement. You can handle exceptions with the `EXCEPTION` section of a block, where you can use the `WHEN` clause to specify the actions to take for each exception.
- **Subprograms**: A subprogram is a named block of code that can be invoked from other blocks of code. PL/SQL provides two types of subprograms: procedures and functions. A procedure is a subprogram that performs a specific action and can have zero or more parameters. A function is a subprogram that returns a single value and can have zero or more parameters. You can declare subprograms in the `DECLARE` section of a block, or create them as standalone objects in the database schema. You can also use packages to group related subprograms and variables into a single unit.



# SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is a procedural extension of SQL designed for Oracle Database.
- PL/SQL allows developers to embed SQL statements within its syntax, and to create and execute complex programs that interact with the database.
- PL/SQL programs are composed of blocks, which are the basic units of execution. A block can contain declarations, executable statements, and exception handlers.
- PL/SQL blocks can be nested within each other, and can be stored inside the database as procedures, functions, triggers, or packages.
- PL/SQL blocks can also be executed dynamically using the EXECUTE IMMEDIATE statement or the DBMS_SQL package.
- PL/SQL offers many advantages over SQL, such as:
  - Better performance, as PL/SQL can process multiple SQL statements in a single block, reducing network traffic and context switches.
  - Better error handling, as PL/SQL can catch and handle exceptions using the RAISE, EXCEPTION_INIT, and PRAGMA EXCEPTION_INIT statements.
  - Better modularity, as PL/SQL can encapsulate business logic and data manipulation in reusable and maintainable units.
  - Better security, as PL/SQL can enforce access control and data validation using the AUTHID and INVOKER RIGHTS clauses.
  - Better integration, as PL/SQL can interact with other languages and technologies using the UTL_HTTP, UTL_SMTP, UTL_FILE, and UTL_TCP packages.



# DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity on the data stored in the database tables or views  .
- DML statements can be executed from within any PL/SQL block of code, such as procedures, functions, triggers, packages, etc.
- There are four types of DML statements: INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert new rows into a table or a view  .
- UPDATE statement is used to modify the existing rows in a table or a view  .
- DELETE statement is used to remove the existing rows from a table or a view  .
- MERGE statement is used to combine the data from two tables into one, based on a matching condition .
- DML statements can be executed either individually or in bulk, using the FORALL statement .
- DML statements can also use variables, expressions, and conditions to manipulate the data dynamically  .
- DML statements can be followed by the RETURNING clause, which returns the values of the affected rows into PL/SQL variables or collections .
- DML statements can be controlled by the transaction management commands, such as COMMIT, ROLLBACK, and SAVEPOINT, to ensure the data consistency and integrity  .
- DML statements can also use the hints, such as /*+ APPEND */, /*+ PARALLEL */, etc, to optimize the performance and execution plan of the statements  .



# Cursors

- A cursor is a pointer to a context area that contains information about the execution of a SQL statement .
- A cursor can hold one or more rows returned by a SQL statement.
- A cursor can be implicit or explicit .
  - An implicit cursor is automatically created by Oracle whenever a SQL statement is executed .
  - An explicit cursor is explicitly declared by the programmer to perform complex queries or to process multiple rows .
- A cursor has four attributes: `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN`.
  - `%FOUND` returns `TRUE` if the cursor fetched at least one row, otherwise `FALSE`.
  - `%NOTFOUND` returns `TRUE` if the cursor fetched no rows, otherwise `FALSE`.
  - `%ROWCOUNT` returns the number of rows fetched by the cursor so far.
  - `%ISOPEN` returns `TRUE` if the cursor is open, otherwise `FALSE`.
- A cursor can be manipulated using the following steps :
  - Declare the cursor using the `CURSOR` keyword and specify the query .
  - Open the cursor using the `OPEN` statement to allocate the context area and execute the query .
  - Fetch the cursor using the `FETCH` statement to retrieve one or more rows from the result set .
  - Close the cursor using the `CLOSE` statement to release the context area and free the resources .
- A cursor can be declared and opened in a single statement using the `CURSOR FOR` loop.
- A cursor can be dynamic, meaning that the query can be constructed and executed at run time using the `EXECUTE IMMEDIATE` statement.



# Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database catalog  .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc  .
- A stored procedure has a header and a body   .
- The header contains the name of the procedure and the parameters passed to the procedure  .
- The body contains the declarative, executable, and exception-handling parts of the procedure .
- The syntax of a stored procedure is as follows  :

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter_name [IN | OUT | IN OUT] type [, ...])]
IS
  [declaration_section]
BEGIN
  executable_section
[EXCEPTION
  exception_section]
END [procedure_name];
```

- The CREATE OR REPLACE option allows to modify an existing procedure .
- The parameter_name is the name of the parameter, which can be of three modes: IN, OUT, or IN OUT  .
- The IN mode is the default and indicates that the parameter is an input value that cannot be changed by the procedure  .
- The OUT mode indicates that the parameter is an output value that can be changed by the procedure and returned to the caller  .
- The IN OUT mode indicates that the parameter is both an input and an output value  .
- The type is the data type of the parameter, which can be any PL/SQL data type  .
- The declaration_section is optional and declares the variables, constants, cursors, and user-defined exceptions used in the procedure .
- The executable_section is mandatory and contains the PL/SQL statements that implement the logic of the procedure .
- The exception_section is optional and handles the errors that occur during the execution of the procedure .
- The procedure_name at the end of the block is optional and can be used to improve the readability of the code .
- To execute a stored procedure, we can use the EXECUTE or EXEC command followed by the procedure name and the arguments if any .
- To drop a stored procedure, we can use the DROP PROCEDURE command followed by the procedure name.
- Alternatively, we can use a graphical user interface such as SQL Developer to create, modify, execute, or drop a stored procedure.



# Stored Function in PL/SQL

- A stored function is a reusable program unit that can be invoked from SQL or PL/SQL code.
- A stored function returns a single value of a specified data type.
- A stored function can be created using the `CREATE FUNCTION` statement, which has the following syntax:

```
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
  [declarative section]
BEGIN
  [executable section]
  RETURN expression;
END [function_name];
```

- The `parameter_list` consists of zero or more parameters, each with a name, a mode (`IN`, `OUT`, or `IN OUT`), and a data type.
- The `return_type` specifies the data type of the value that the function returns.
- The `declarative section` is optional and contains the declarations of variables, constants, cursors, exceptions, and other local objects.
- The `executable section` is mandatory and contains the statements that perform the logic of the function.
- The `RETURN` statement specifies the expression that evaluates to the value that the function returns.
- The `function_name` at the end of the function is optional and can be used to improve readability.

- A stored function can be invoked from SQL statements, such as `SELECT`, `INSERT`, `UPDATE`, or `DELETE`, as long as the function does not modify any database tables or have any side effects.
- A stored function can also be invoked from PL/SQL blocks, procedures, packages, triggers, or other functions, using the syntax `function_name (argument_list)`, where the `argument_list` matches the `parameter_list` of the function.
- A stored function can be dropped using the `DROP FUNCTION` statement, which has the following syntax:

```
DROP FUNCTION function_name;
```

- A stored function can be modified using the `CREATE OR REPLACE FUNCTION` statement, which replaces the existing function definition with the new one.
- A stored function can be compiled using the `ALTER FUNCTION` statement, which has the following syntax:

```
ALTER FUNCTION function_name COMPILE;
```

- A stored function can be debugged using the `DBMS_DEBUG` package, which provides an API for debugging PL/SQL code.



# Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP  .
- Triggers can be used for maintaining the integrity of the information on the database, implementing complex data interactions, auditing data changes, enforcing business rules, and performing custom actions.
- Triggers are defined on a table, stored in the associated database, and executed as a result of an event on that table or view.
- Triggers can be created, modified, and dropped using SQL statements  .
- Triggers can be classified into different types based on the timing and scope of their execution  :
  - Row-level triggers: These triggers are executed for each row affected by the triggering event.
  - Statement-level triggers: These triggers are executed once for the whole statement that caused the triggering event.
  - Before triggers: These triggers are executed before the triggering event occurs.
  - After triggers: These triggers are executed after the triggering event occurs.
  - Instead of triggers: These triggers are executed instead of the triggering event, and can be used to override the default behavior of the event .
  - DML triggers: These triggers are executed in response to DML actions on a table or view.
  - DDL triggers: These triggers are executed in response to DDL actions on a database or server .
  - Logon triggers: These triggers are executed in response to logon events on a server.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some indices for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System:

# Unit 6 - PL/SQL

- Introduction to PL/SQL
  - What is PL/SQL and why use it?
  - Features and advantages of PL/SQL
  - PL/SQL architecture and environment
  - PL/SQL data types and variables
  - PL/SQL operators and expressions
- PL/SQL Control Structures
  - Conditional statements (IF, CASE)
  - Looping statements (FOR, WHILE, LOOP, EXIT, CONTINUE)
  - Sequential statements (GOTO, NULL)
  - Exception handling (RAISE, EXCEPTION, PRAGMA EXCEPTION_INIT, SQLCODE, SQLERRM)
- PL/SQL Cursors and Records
  - What are cursors and why use them?
  - Types of cursors (implicit, explicit, parameterized, ref cursors)
  - Cursor attributes (%FOUND, %NOTFOUND, %ROWCOUNT, %ISOPEN)
  - Cursor FOR loop
  - What are records and why use them?
  - Types of records (table-based, cursor-based, user-defined)
  - Record operations (assignment, comparison, copying)
- PL/SQL Subprograms
  - What are subprograms and why use them?
  - Types of subprograms (procedures, functions, packages)
  - Subprogram parameters (IN, OUT, IN OUT, NOCOPY)
  - Subprogram overloading and resolution
  - Subprogram invocation and execution
  - Subprogram scope and visibility
- PL/SQL Triggers
  - What are triggers and why use them?
  - Types of triggers (row-level, statement-level, DML, DDL, database, schema, instead-of)
  - Trigger components (timing, event, condition, action)
  - Trigger restrictions and guidelines
  - Trigger examples and applications
- PL/SQL Collections and Dynamic SQL
  - What are collections and why use them?
  - Types of collections (associative arrays, nested tables, varrays)
  - Collection methods (COUNT, EXISTS, EXTEND, TRIM, DELETE, PRIOR, NEXT, FIRST, LAST, LIMIT)
  - Collection examples and applications
  - What is dynamic SQL and why use it?
  - Types of dynamic SQL (EXECUTE IMMEDIATE, OPEN-FOR, DBMS_SQL)
  - Dynamic SQL examples and applications



# Unit 7 - Transaction Processing Concepts

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has the following properties :
  - **Atomicity**: A transaction must either complete all of its operations or none of them. If a transaction fails, the database state is restored to the state before the transaction started.
  - **Consistency**: A transaction must preserve the integrity constraints of the database. If the database is consistent before the transaction, it must be consistent after the transaction.
  - **Isolation**: A transaction must not be affected by the concurrent execution of other transactions. Each transaction must execute as if it were the only one in the system.
  - **Durability**: The effects of a successful transaction must be permanent and survive any system failures.
- A **transaction processing system** is a system that supports the execution of transactions on a large database with many concurrent users.
- A transaction processing system has the following components :
  - **Transaction manager**: The component that coordinates the execution of transactions and ensures their ACID properties. It also handles transaction failures and recovery.
  - **Scheduler**: The component that controls the order of execution of operations from different transactions. It also resolves conflicts and ensures serializability of transactions.
  - **Buffer manager**: The component that manages the movement of data between the main memory and the disk. It also implements caching and buffering techniques to improve performance.
  - **Recovery manager**: The component that ensures the durability of transactions and recovers the database from failures. It also implements logging and checkpointing techniques to facilitate recovery.
  - **Lock manager**: The component that implements locking protocols to ensure the isolation of transactions. It also handles deadlock detection and resolution.
  - **Query processor**: The component that parses, optimizes, and executes queries from transactions. It also implements query evaluation and optimization techniques to improve performance.



# Transaction Concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction has the following properties :

- **Atomicity**: A transaction is either performed in its entirety or not performed at all. If any error occurs during the execution of a transaction, the database is restored to its original state as if the transaction never happened.
- **Consistency**: A transaction must preserve the integrity constraints and business rules of the database. A transaction can only bring the database from one consistent state to another consistent state.
- **Isolation**: A transaction must not interfere with other concurrent transactions. The intermediate results of a transaction are not visible to other transactions until the transaction is committed.
- **Durability**: The effects of a committed transaction are permanent and must not be lost due to system failures or power outages.

A transaction can be executed using a simple pattern like the following:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

A transaction can be classified into different types based on its characteristics, such as:

- **Read-only transaction**: A transaction that only reads data from the database and does not modify it.
- **Read-write transaction**: A transaction that reads and writes data to the database.
- **Flat transaction**: A transaction that has a single entry and exit point and does not contain any nested transactions.
- **Nested transaction**: A transaction that contains one or more sub-transactions within it, each with its own commit and rollback operations.
- **Distributed transaction**: A transaction that spans multiple database systems or network nodes and requires coordination among them.



# Properties of Transaction in DBMS

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four main properties, also known as ACID properties, that ensure the reliability and correctness of the database.
- The four properties are:

  - **Atomicity**: This means that a transaction is either executed completely or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state before the transaction started. This ensures that the database is not left in an inconsistent state due to partial execution of a transaction.   
  - **Consistency**: This means that a transaction must preserve the integrity constraints and business rules of the database. A transaction must not violate any of the conditions that define a consistent state of the database. If a transaction starts with a consistent state of the database, it must end with a consistent state of the database. This ensures that the database is always valid and accurate.    
  - **Isolation**: This means that a transaction must not interfere with other concurrent transactions. A transaction must execute as if it is the only transaction in the system. The intermediate results and effects of a transaction must not be visible to other transactions until the transaction commits. This ensures that the concurrent execution of transactions does not lead to any anomalies or conflicts.     
  - **Durability**: This means that the effects of a committed transaction must be permanent and persistent in the database. The changes made by a transaction must not be lost due to any system failure or error. The database must be able to recover the committed state of the database after any failure. This ensures that the database is reliable and stable.    

- These properties are essential for ensuring the correctness and efficiency of transaction processing in a database management system.



# Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of a database.
- A schedule is serializable if it is equivalent to some serial schedule, where transactions are executed one after the other without any overlap.
- Serializability can be tested using two techniques: serialization graph and precedence graph.
- A serialization graph is a directed graph where the nodes represent transactions and the edges represent conflicts between transactions. A conflict occurs when two transactions access the same data item and at least one of them is a write operation.
- A schedule is serializable if and only if its serialization graph is acyclic, meaning that it has no cycles. A cycle in the graph indicates that there is a circular dependency between transactions, which violates serial order.
- A precedence graph is a special case of a serialization graph, where the edges are labeled with the type of conflict: read-write (RW), write-read (WR), or write-write (WW). A schedule is serializable if and only if its precedence graph is acyclic.
- To construct a precedence graph for a given schedule, we follow these steps:
  - Create a node for each transaction in the schedule.
  - Scan the schedule from left to right and identify the conflicts between transactions.
  - For each conflict, draw an edge from the transaction that executed earlier to the transaction that executed later, and label it with the type of conflict.
  - Check if the graph has any cycles. If yes, the schedule is not serializable. If no, the schedule is serializable.



# Serializability of schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- Serializability is a desirable property of schedules because it ensures the consistency and correctness of the database state after the execution of concurrent transactions.
- There are two types of serializability: conflict serializability and view serializability.

## Conflict serializability

- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations, which are operations that access different data items or are both read operations.
- Conflict serializability can be checked by constructing a precedence graph, which is a directed graph where the nodes are transactions and the edges are conflicts between operations. A conflict is a pair of operations from different transactions that access the same data item and at least one of them is a write operation.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.

## View serializability

- A schedule is view serializable if it is equivalent to a serial schedule in terms of the following three conditions:
  - The initial read operations of each data item are the same in both schedules.
  - The final write operations of each data item are the same in both schedules.
  - The read operations of each data item see the same value written by the same transaction in both schedules.
- View serializability is a more general concept than conflict serializability, as it allows some schedules that are not conflict serializable to be view serializable.
- View serializability can be checked by constructing a polygraph, which is a directed graph where the nodes are operations and the edges are dependencies between operations. A dependency is a relation between two operations that access the same data item and at least one of them is a write operation.
- A schedule is view serializable if and only if its polygraph is acyclic.



# Conflict and View Serializable Schedule

## Introduction

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

## Conflict Serializability

- Conflict serializability is a property of a schedule that ensures the same order of conflicting operations as a serial schedule.
- Two operations are said to be conflicting if they satisfy all the following conditions:
  - They belong to different transactions.
  - They operate on the same data item.
  - At least one of them is a write operation.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- A schedule is conflict equivalent to another schedule if they have the same order of conflicting operations.
- Conflict serializability can be checked by constructing a precedence graph of the transactions in the schedule and checking if it is acyclic.

## View Serializability

- View serializability is a property of a schedule that ensures the same effect on the database as a serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item.
  - They have the same final write operations on each data item.
  - They have the same update operations on each data item.
- A schedule is view serializable if it is view equivalent to some serial schedule.
- A schedule is view equivalent to another schedule if they have the same view on the database.
- View serializability can be checked by comparing the initial read, final write and update operations of the schedules.



# Recoverability in Transaction Processing

- Recoverability is the property of a schedule that ensures that the database state is consistent after a transaction failure or system crash.
- A schedule is recoverable if it does not contain any dirty read, which is when a transaction reads a data item that is updated by another uncommitted transaction.
- A schedule is irrecoverable if it contains a dirty read and the transaction that performs the dirty read commits before the transaction that updates the data item.
- Irrecoverable schedules can lead to inconsistent database states if the transaction that updates the data item aborts after the other transaction commits.
- Example of an irrecoverable schedule:

| T1 | T2 |
|----|----|
| W(A) |    |
|     | R(A) |
|     | C |
| A | |

- In this schedule, T2 reads the value of A that is written by T1, but T1 aborts later. T2 has already committed, so it cannot undo its changes. The database state is inconsistent because it reflects the changes of an aborted transaction.
- A schedule is cascadingly recoverable if it is recoverable and the transactions that read the data items updated by an aborted transaction also abort.
- Cascadingly recoverable schedules can avoid inconsistent database states, but they can cause a lot of wasted work and delays due to cascading aborts.
- Example of a cascadingly recoverable schedule:

| T1 | T2 | T3 |
|----|----|----|
| W(A) |    |    |
|     | R(A) |    |
|     | W(B) |    |
|     |    | R(B) |
|     |    | W(C) |
| A |    |    |
|     | A |    |
|     |    | A |

- In this schedule, T1 aborts and causes T2 to abort, which in turn causes T3 to abort. All the transactions that read the data items updated by T1 have to abort and undo their changes. The database state is consistent, but a lot of work is lost and the transactions have to restart.
- A schedule is strictly recoverable if it is recoverable and the transactions that update the data items commit only after all the transactions that read those data items commit.
- Strictly recoverable schedules can avoid inconsistent database states and cascading aborts, but they can reduce the concurrency and performance of the system.
- Example of a strictly recoverable schedule:

| T1 | T2 | T3 |
|----|----|----|
| W(A) |    |    |
|     | R(A) |    |
|     | W(B) |    |
|     |    | R(B) |
|     |    | W(C) |
|     |    | C |
|     | C |    |
| C |    |    |

- In this schedule, T1 commits only after T2 and T3 commit, and T2 commits only after T3 commits. All the transactions that update the data items commit after all the transactions that read those data items commit. The database state is consistent and no cascading aborts occur. However, the transactions have to wait for each other to commit, which can reduce the concurrency and performance of the system.



# Recovery from transaction failures

- A transaction failure is an event that causes a transaction to abort or terminate before it can commit its changes to the database.
- Transaction failures can occur due to various reasons, such as network failures, deadlock, or errors in application logic.
- Recovery from transaction failures is the process of restoring the database to a consistent state after such failures.
- Recovery from transaction failures is essential to ensure data consistency, integrity, and durability in a database system.
- Recovery from transaction failures can be achieved by using different techniques, such as deferred updates, immediate updates, undoing, redoing, or checkpointing.
- Deferred updates: This technique does not physically update the database on disk until a transaction has reached its commit point. Instead, it records the changes in a log file in main memory. If a transaction fails, no changes need to be undone, as the database on disk is unaffected. If the system crashes, the log file can be used to redo the committed transactions after restart.
- Immediate updates: This technique allows the database to be updated on disk before a transaction reaches its commit point. However, it also records the changes in a log file in main memory. If a transaction fails, the recovery manager may undo the changes by reversing the operations of the failed transaction using the log file. If the system crashes, the log file can be used to redo the committed transactions and undo the uncommitted transactions after restart.
- Undoing: This is the process of reversing the effects of a failed transaction by applying the inverse operations of the transaction using the log file. For example, if a transaction added 100 to an account balance, undoing would subtract 100 from the same account balance. Undoing is necessary when immediate updates are used, or when a transaction aborts after updating the database on disk.
- Redoing: This is the process of reapplying the effects of a committed transaction by applying the same operations of the transaction using the log file. For example, if a transaction added 100 to an account balance, redoing would add 100 to the same account balance again. Redoing is necessary when deferred updates are used, or when a system crash occurs after a transaction has committed but before its changes are reflected on disk.
- Checkpointing: This is the process of periodically writing the contents of the log file and the database buffers to disk, and marking a point in the log file as a checkpoint. Checkpointing reduces the amount of work that needs to be done during recovery, as only the transactions that occurred after the last checkpoint need to be considered. Checkpointing can be done in different ways, such as fuzzy checkpointing, incremental checkpointing, or concurrent checkpointing.



# Two-phase commit protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort (roll back) the transaction. It ensures that either all the changes are committed or none of them are, even in the case of site failures and message losses.

The protocol involves two phases:

- **Phase 1: Prepare phase**. In this phase, the coordinator (the process that initiates the transaction) sends a prepare message to all the participants (the processes that execute the transaction) and waits for their replies. Each participant executes the transaction up to the point where it is ready to commit, writes a prepare record to its log, and sends a prepared message to the coordinator. If any participant encounters an error or decides to abort, it sends an abort message to the coordinator and undoes the transaction.
- **Phase 2: Commit phase**. In this phase, the coordinator decides the outcome of the transaction based on the replies from the participants. If all the participants replied with prepared messages, the coordinator commits the transaction and sends a commit message to all the participants. If any participant replied with an abort message, the coordinator aborts the transaction and sends an abort message to all the participants. Each participant then follows the coordinator's decision and either commits or aborts the transaction, and writes a commit or abort record to its log.

The two-phase commit protocol is a blocking protocol; the failure of a single node blocks progress until the node recovers. Moreover, if the coordinator fails, then the database is left in an inconsistent state and only recovers once the coordinator recovers. This leads to another drawback as the protocol’s latency depends on the slowest node.

The two-phase commit protocol is used for distributed transaction management in databases, computer networking, and transaction processing systems . It ensures the ACID (atomicity, consistency, isolation, and durability) properties of transactions in a distributed system.



# Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique used to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A transaction log contains the following information  :
  - The transaction identifier (Tn)
  - The type of operation (read, write, delete, etc.)
  - The data item affected by the operation
  - The old value and the new value of the data item
  - The start and the end of the transaction
- For example, a transaction log for a transaction T1 that updates the city of a customer from Chennai to NCR can be written as follows:
  - <T1, Start>
  - <T1, City, 'Chennai', 'NCR'>
  - <T1, Commit>
- The log is maintained in some stable storage device, such as a disk, so that it can be accessed even after a failure   .
- The log is used to restore the database to a consistent state by applying one of the following methods    :
  - Undo: This method undoes the effects of the transactions that were not committed before the failure. It restores the old values of the data items from the log.
  - Redo: This method redoes the effects of the transactions that were committed before the failure. It applies the new values of the data items from the log.
  - Undo/Redo: This method combines both undo and redo methods. It undoes the effects of the transactions that were not committed and redoes the effects of the transactions that were committed before the failure.
- The choice of the recovery method depends on the type of failure and the checkpoint mechanism used by the DBMS    .
- A checkpoint is a point in time when the DBMS writes all the modified pages of the database to the disk and records the information about the active transactions in the log    .
- A checkpoint helps to reduce the amount of work needed for recovery by limiting the scope of the transactions that need to be undone or redone    .
- The following table summarizes the recovery methods and the conditions for applying them    :

| Recovery Method | Condition |
| --------------- | --------- |
| Undo | The transaction has not committed and has not reached the checkpoint |
| Redo | The transaction has committed and has reached the checkpoint |
| Undo/Redo | The transaction has committed but has not reached the checkpoint |

- Log based recovery in DBMS ensures the atomicity and durability properties of transactions    .
- Atomicity means that either all the operations of a transaction are executed or none of them are executed    .
- Durability means that the effects of a committed transaction are permanent and do not get lost due to a failure    .



# Checkpoints for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

- Define what is a **transaction** and how it is used to represent a logical unit of database processing that must be completed in its entirety to ensure correctness.
- Explain the **ACID** properties of transactions, which are **Atomicity**, **Consistency**, **Isolation**, and **Durability**, and why they are important for maintaining the integrity of the database .
- Describe the **states** of a transaction, which are **active**, **partially committed**, **committed**, **failed**, and **aborted**, and how they are affected by the **commit** and **rollback** operations .
- Discuss the **concurrency control** techniques that are used to ensure the serializability and recoverability of concurrent transactions, such as **locking**, **timestamping**, and **validation** .
- Compare the **advantages and disadvantages** of different concurrency control techniques, such as **strict two-phase locking**, **optimistic concurrency control**, and **multiversion concurrency control** .
- Explain the **recovery management** techniques that are used to restore the database to a consistent state after a failure, such as **log-based recovery**, **shadow paging**, and **checkpoints** .
- Compare the **advantages and disadvantages** of different recovery management techniques, such as **undo logging**, **redo logging**, and **undo/redo logging** .
- Understand the **challenges and solutions** for transaction processing in **distributed databases**, such as **distributed commit protocols**, **distributed locking protocols**, and **deadlock detection and resolution** .



# Deadlock Handling

A deadlock is a situation in which two or more transactions are waiting indefinitely for one another to release locks on data items that they need to proceed. Deadlocks can cause performance degradation and system unavailability in a database system. Therefore, deadlock handling is an important aspect of transaction processing.

There are three main strategies for handling deadlocks in a database system:

- **Deadlock prevention**: This strategy aims to prevent deadlocks from occurring in the first place by imposing some constraints on how transactions can acquire locks. For example, a transaction may be required to lock all the data items it needs before it starts, or to follow a predefined order of locking data items. This way, no circular wait can occur among transactions. However, deadlock prevention may also reduce concurrency and increase locking overhead, as transactions may have to lock more data items than they actually need or wait longer to acquire locks.
- **Deadlock avoidance**: This strategy allows transactions to acquire locks dynamically, but uses some information about the transactions' resource requirements and the current state of the system to decide whether granting a lock request may lead to a potential deadlock. For example, a transaction may have to declare in advance the maximum number of data items it will need, or the system may maintain a wait-for graph that shows the dependencies among transactions based on their lock requests. If granting a lock request may create a cycle in the wait-for graph, the request is denied and the transaction is made to wait. This way, no deadlock can occur in the system. However, deadlock avoidance may also require additional information and computation, as transactions may have to provide their resource requirements or the system may have to maintain and update the wait-for graph.
- **Deadlock detection and resolution**: This strategy allows transactions to acquire locks freely, but periodically checks for the existence of deadlocks in the system using some detection algorithm. For example, the system may periodically run a cycle detection algorithm on the wait-for graph, or use a timeout mechanism to identify transactions that have been waiting for too long. If a deadlock is detected, the system takes some action to resolve it, such as aborting one or more transactions involved in the deadlock and releasing their locks. This way, deadlocks are eliminated from the system. However, deadlock detection and resolution may also incur some cost and delay, as transactions may have to be restarted and their work may be wasted.

The choice of the deadlock handling strategy depends on various factors, such as the frequency and severity of deadlocks, the performance and availability requirements, the complexity and overhead of the strategy, and the characteristics of the transactions and the data. Different strategies may have different advantages and disadvantages in different scenarios. Therefore, there is no single best strategy for handling deadlocks in a database system.



## Unit 8 - Concurrency Control Techniques

Concurrency control techniques are methods of managing the simultaneous execution of transactions in a shared database. They aim to preserve the database consistency, enforce the isolation of different transactions, and resolve the conflicts that occur due to the read-write operations of transactions .

The need for concurrency control arises because multiple transactions may access and modify the same data items concurrently, which may lead to inconsistency, lost updates, uncommitted dependencies, or incorrect summary. Concurrency control ensures that the transactions are concurrent, accurate, and give correct results without violating data integrity. It also ensures serializability, which means that the concurrent execution of transactions produces the same effect as some serial execution of the same transactions.

Some of the common concurrency control techniques are :

- **Two-phase locking protocol**: This technique uses locks to secure the permission to read or write a data item. A transaction goes through two phases: a locking phase, where it acquires locks on the data items it needs, and an unlocking phase, where it releases the locks. The locking phase precedes the unlocking phase, and no new locks can be acquired after releasing any lock. This protocol ensures serializability, but may cause deadlocks or starvation.
- **Timestamp ordering protocol**: This technique assigns a unique timestamp to each transaction, and uses the timestamps to order the transactions. A transaction can read or write a data item only if its timestamp is compatible with the read and write timestamps of the data item. This protocol ensures serializability and avoids deadlocks, but may cause aborts or cascading aborts.
- **Multi-version concurrency control**: This technique maintains multiple versions of each data item, and assigns a read timestamp and a write timestamp to each version. A transaction can read the latest version of a data item that is older than its timestamp, and can write a new version of a data item only if its timestamp is greater than the write timestamp of the current version. This protocol ensures serializability and avoids aborts, but requires more storage space and overhead for version management.
- **Validation concurrency control**: This technique divides the execution of a transaction into three phases: a read phase, where it reads the data items from the database, a validation phase, where it checks for conflicts with other transactions, and a write phase, where it writes the updated data items to the database. A transaction can commit only if it passes the validation phase. This protocol ensures serializability and avoids deadlocks, but may cause aborts or delays.



# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

Some of the objectives of concurrency control are:

- To ensure the consistency and correctness of the database state after the execution of concurrent transactions.
- To prevent data loss or corruption due to concurrent access or modification of the same data item by different transactions.
- To improve the performance and throughput of the DBMS by allowing a high degree of concurrency among transactions.
- To avoid deadlock or starvation situations where transactions are waiting indefinitely for resources held by other transactions.

Some of the techniques of concurrency control are:

- Locking: This technique involves granting exclusive or shared access to a data item or a set of data items to a transaction based on the type of operation (read or write) it performs. A transaction must acquire a lock before accessing a data item and release it after completing the operation. Locking can ensure serializability, which is a correctness criterion for concurrent transactions, but it can also cause deadlock or blocking problems .
- Timestamping: This technique involves assigning a unique timestamp to each transaction based on its start time or priority. A transaction can access a data item only if its timestamp is compatible with the read and write timestamps of the data item, which are updated after each operation. Timestamping can ensure serializability without causing deadlock, but it can cause aborts or restarts of transactions due to timestamp conflicts .
- Optimistic: This technique involves allowing transactions to execute without any concurrency control until they are ready to commit. Then, a validation phase checks if the transactions have violated any serializability constraints based on their read and write sets. If no violation is detected, the transactions are committed; otherwise, they are aborted and restarted. Optimistic concurrency control can improve performance and avoid deadlock in low-conflict scenarios, but it can cause high overhead and aborts in high-conflict scenarios .



# Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the integrity of the database is maintained. Concurrency control also prevents conflicts and anomalies that may arise due to concurrent access, such as lost updates, dirty reads, unrepeatable reads, and phantom reads.

One of the most common concurrency control techniques is locking. Locking is a mechanism that grants or denies permission to access a data item based on the type and mode of the lock. Locking can be implemented at different levels of granularity, such as database, table, page, or record. Locking can also be classified into different types, such as binary, shared, exclusive, or intention locks.

The main idea behind locking is to enforce serializability, which is the property that the concurrent execution of transactions is equivalent to some serial execution of the same transactions. Serializability ensures that the outcome of concurrent transactions is the same as if they were executed one after the other, without any interference.

To achieve serializability, a locking protocol must follow some rules or principles. One of the most widely used locking protocols is the two-phase locking (2PL) protocol, which divides the execution of a transaction into two phases: the growing phase and the shrinking phase. In the growing phase, a transaction can acquire locks on data items, but cannot release any lock. In the shrinking phase, a transaction can release locks on data items, but cannot acquire any new lock. The point where the transaction switches from the growing phase to the shrinking phase is called the lock point.

The 2PL protocol ensures serializability, but it may cause some problems, such as deadlocks, starvation, or cascading aborts. Deadlocks occur when two or more transactions are waiting for each other to release locks on data items that they need. Starvation occurs when a transaction is repeatedly denied access to a data item due to the presence of other conflicting locks. Cascading aborts occur when a transaction aborts and causes other transactions that have read its uncommitted data to abort as well.

To overcome these problems, some variations or extensions of the 2PL protocol have been proposed, such as:

- Strict 2PL: A transaction must hold all its locks until it commits or aborts. This prevents cascading aborts, but may increase the lock holding time and reduce concurrency.
- Rigorous 2PL: A transaction must hold all its exclusive locks until it commits or aborts, and all its shared locks until it reads the corresponding data items. This is a stronger version of strict 2PL that also prevents dirty reads, but may further reduce concurrency.
- Conservative 2PL: A transaction must request all its locks before it starts its execution. This prevents deadlocks, but may cause unnecessary blocking and waste of resources.
- Timestamp-based 2PL: A transaction is assigned a unique timestamp when it starts, and uses this timestamp to order its lock requests. This avoids deadlocks and starvation, but may cause more aborts due to conflicts.
- Multi-version 2PL: A transaction can access multiple versions of a data item, each with a different timestamp. This increases concurrency and reduces conflicts, but requires more storage space and complexity.

These are some of the main locking techniques for concurrency control. There are other techniques as well, such as validation, optimistic, or snapshot isolation, that do not rely on locking, but use other methods to ensure serializability and consistency. Each technique has its own advantages and disadvantages, and the choice of the best technique depends on the characteristics and requirements of the database system and the application.



# Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use either system time or logical counters as timestamps to order the transactions and ensure serializability  .
- Timestamps are assigned to each transaction when it is created, and to each read or write operation when it is issued  .
- The timestamps determine the precedence order of the transactions, and any conflicting read and write operations are executed according to the timestamp order   .
- Timestamps can be either generated by a centralized authority, or by a distributed algorithm that guarantees the uniqueness and accuracy of the timestamps.
- Timestamps can be either global or local. Global timestamps are assigned by a single authority and are consistent across the system. Local timestamps are assigned by each site and may differ across the system.
- Timestamp ordering protocols can be either optimistic or pessimistic. Optimistic protocols assume that conflicts are rare and allow transactions to execute without checking for conflicts until they commit. Pessimistic protocols check for conflicts before each operation and abort or delay transactions that violate the timestamp order.
- Timestamp ordering protocols can be either conservative or strict. Conservative protocols ensure that a transaction reads the latest committed value of a data item, and that a transaction does not overwrite a data item that has been read by a later transaction. Strict protocols ensure that a transaction does not read or overwrite a data item that has been written by a later transaction.
- Timestamp ordering protocols can be either basic or multiversion. Basic protocols use a single version of each data item and maintain a read timestamp (RTS) and a write timestamp (WTS) for each data item. Multiversion protocols use multiple versions of each data item and maintain a version list (VL) for each data item.
- Timestamp ordering protocols can be either centralized or decentralized. Centralized protocols use a single site to assign timestamps and enforce the timestamp order. Decentralized protocols use multiple sites to assign timestamps and enforce the timestamp order locally or globally.
- Timestamp ordering protocols can be either wait-die or wound-wait. Wait-die protocols allow an older transaction to wait for a younger transaction to release a data item, but abort a younger transaction that conflicts with an older transaction. Wound-wait protocols abort an older transaction that conflicts with a younger transaction, but allow a younger transaction to wait for an older transaction to release a data item.

: https://www.geeksforgeeks.org/timestamp-based-concurrency-control/
: https://www.tutorialspoint.com/dbms/dbms_concurrency_control.htm
: https://www.guru99.com/dbms-concurrency-control.html
: https://en.wikipedia.org/wiki/Timestamp-based_concurrency_control



# Validation Based Protocol

- Validation Based Protocol is a type of concurrency control technique that works on the validation rules and timestamps .
- It is also called Optimistic Concurrency Control Technique because it assumes that very few conflicts occur among transactions .
- It does not check for conflicts while the transaction is executing, but only at the end of the transaction .
- It consists of three phases for each transaction: read phase, validation phase, and write phase  .
- In the read phase, the transaction can read data values from the database, but it can only write or update the local copies of the data, not the actual database .
- In the validation phase, the transaction is checked for conflicts with other transactions that have already committed  .
- The validation phase uses timestamps to determine the order of transactions and to detect conflicts  .
- A timestamp is a unique identifier assigned to each transaction when it starts  .
- The validation phase uses two types of timestamps for each transaction: start timestamp (ST) and end timestamp (ET)  .
- ST is the timestamp when the transaction starts its read phase, and ET is the timestamp when the transaction finishes its read phase  .
- The validation phase compares the timestamps of the current transaction with the timestamps of the other transactions that have committed or are in the validation phase  .
- The validation phase follows three rules to check for conflicts  :
  - If the current transaction Ti has read a data item X that was written by another transaction Tj, and STi < ETj, then Ti is aborted and restarted with a new timestamp  .
  - If the current transaction Ti has written a data item X that was read by another transaction Tj, and STi < STj < ETi, then Ti is aborted and restarted with a new timestamp  .
  - If the current transaction Ti has written a data item X that was written by another transaction Tj, and STi < STj < ETi, then Ti is aborted and restarted with a new timestamp  .
- If the current transaction Ti passes the validation phase without any conflicts, then it proceeds to the write phase  .
- In the write phase, the transaction writes or updates the actual database with the local copies of the data .
- The transaction then commits and releases all the resources .
- The advantages of validation based protocol are :
  - It does not require locking or unlocking of data items, which reduces the overhead and the possibility of deadlock .
  - It allows more concurrency among transactions, as they can execute without interference until the validation phase .
- The disadvantages of validation based protocol are :
  - It may cause more aborts and restarts of transactions, which increases the cost and the response time .
  - It may not be suitable for applications that have high conflict rates among transactions .



# Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- There are three types of lock granularity:
  - Fine granularity: It locks the smallest data items, such as records or fields. It provides high concurrency but also high locking overhead and high risk of deadlock.
  - Coarse granularity: It locks the largest data items, such as files or tables. It provides low concurrency but also low locking overhead and low risk of deadlock.
  - Medium granularity: It locks the intermediate data items, such as pages or blocks. It provides a balance between concurrency and overhead, but also requires a more complex locking mechanism.
- Multiple granularity locking protocol is a locking protocol that allows transactions to lock data items at different levels of granularity, depending on their access patterns and concurrency requirements.
- Multiple granularity locking protocol follows these rules :
  - Follow multi-granularity compatibility function: This function defines which lock modes are compatible with each other at different levels of granularity. For example, an S lock on a file is compatible with an IS lock on a record, but not with an X lock on a record.
  - Lock root of tree first, any mode: This rule ensures that every transaction locks the root node of the hierarchy, which represents the entire database, before locking any other node. The lock mode can be any of the six modes: S, X, IS, IX, SIX, or NL.
  - Node Q can be locked by T i in S or IS only if parent(Q) locked by T i in IX or IS: This rule ensures that a transaction can lock a node in shared or intention-shared mode only if it has locked its parent node in intention-exclusive or intention-shared mode. This prevents conflicts between transactions that lock different levels of granularity.
  - Node Q can be locked by T i in X, SIX, IX only if parent(Q) locked by T i in IX, SIX: This rule ensures that a transaction can lock a node in exclusive, shared-intent-exclusive, or intention-exclusive mode only if it has locked its parent node in intention-exclusive or shared-intent-exclusive mode. This prevents conflicts between transactions that lock different levels of granularity.
  - T i is two-phase: This rule ensures that every transaction follows the two-phase locking protocol, which means that it acquires all the locks before releasing any lock. This guarantees serializability of transactions.
  - T i can unlock node Q only if none of Q’s descendants are locked by T i: This rule ensures that a transaction can unlock a node only if it has unlocked all its descendant nodes. This prevents the violation of the lock hierarchy and the compatibility function.



# Multi-version Schemes for Concurrency Control

- Multi-version concurrency control (MVCC) is a technique that allows concurrent access to the database without locking the data.
- MVCC creates multiple versions of each data item and assigns them timestamps to indicate their validity periods.
- MVCC ensures that each transaction reads the most recent committed version of the data that is consistent with its snapshot.
- MVCC avoids the problems of locking-based concurrency control, such as deadlocks, starvation, and blocking.
- MVCC improves the performance and scalability of database applications in a multiuser environment.

## How MVCC Works

- While different database systems may implement MVCC in their own ways, the general idea is as follows:
  - Every database record has a version number that is incremented whenever the record is updated.
  - Concurrent reads happen against the record with the highest version number that is lower than or equal to the transaction's snapshot.
  - Write operations operate on a copy of the record, not the record itself.
  - Users continue to read the older version while the copy is updated.
  - After the write operation is successful, the version number is incremented and the copy becomes the new version.
  - Subsequent concurrent reads use the updated version.
  - Old versions of the records are eventually garbage collected when they are no longer needed.

## Example of MVCC

- Suppose we have a table called `products` with the following schema and data:

| id | name | price | version |
| -- | ---- | ----- | ------- |
| 1  | A    | 10    | 1       |
| 2  | B    | 20    | 1       |
| 3  | C    | 30    | 1       |

- Now suppose we have two transactions, T1 and T2, that execute concurrently as follows:

| T1                          | T2                          |
| --------------------------- | --------------------------- |
| begin                       | begin                       |
| read products where id = 1  | read products where id = 2  |
| update products set price = 15 where id = 1 | update products set price = 25 where id = 2 |
| commit                      | commit                      |

- With MVCC, the transactions will execute without any conflict or locking as follows:
  - T1 and T2 start with their own snapshots of the database, which are the same as the initial state of the table.
  - T1 reads the product with id = 1, which has version 1 and price 10.
  - T2 reads the product with id = 2, which has version 1 and price 20.
  - T1 updates the product with id = 1 by creating a copy of the record with version 2 and price 15.
  - T2 updates the product with id = 2 by creating a copy of the record with version 2 and price 25.
  - T1 commits and the copy of the product with id = 1 becomes the new version.
  - T2 commits and the copy of the product with id = 2 becomes the new version.
  - The final state of the table is as follows:

| id | name | price | version |
| -- | ---- | ----- | ------- |
| 1  | A    | 15    | 2       |
| 2  | B    | 25    | 2       |
| 3  | C    | 30    | 1       |

- Note that T1 and T2 did not interfere with each other, as they read and wrote different versions of the data.
- Note also that the old versions of the products with id = 1 and 2 are still present in the database, but they are marked as invalid and will be deleted later.



# Recovery with Concurrent Transaction

Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions. Recovery with concurrent transaction is important to ensure the ACID properties of transactions, especially atomicity and durability.

Recovery with concurrent transaction can be done in the following four ways:

- Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if strict two-phase locking is used, then no transaction can commit until all its locks are released. This ensures that no transaction can be affected by the rollback of another transaction. If timestamp ordering is used, then no transaction can read or write a data item that has been written by a younger transaction. This ensures that no transaction can be affected by the abort of another transaction.
- Transaction rollback: In this scheme, the recovery system can undo the effects of a transaction by using the log records. For example, if a transaction T writes a new value V to a data item X, then the log record will contain the old value W of X. The recovery system can use this log record to restore X to W and undo the write operation of T. Transaction rollback can be done for a single transaction or for a group of transactions that are dependent on each other.
- Checkpoints: In this scheme, the recovery system periodically performs a checkpoint operation, which is a special log record that marks a point in time when the database is in a consistent state. A checkpoint operation involves the following steps  :

  - The DBMS stops accepting new transactions and waits for the active transactions to finish their current operations.
  - The DBMS forces all the modified buffers in the main memory to be written to the disk.
  - The DBMS writes a checkpoint record to the log file and forces the log file to be written to the disk.
  - The DBMS resumes accepting new transactions.

  A checkpoint operation reduces the amount of work that the recovery system has to do in case of a failure. The recovery system only has to consider the transactions that were active after the last checkpoint.
- Restart recovery: In this scheme, the recovery system uses the log records and the checkpoint records to restore the database to a consistent state after a failure. Restart recovery involves the following steps  :

  - The recovery system scans the log file backwards from the end until it reaches the most recent checkpoint record. This is called the analysis phase, where the recovery system identifies the transactions that were active, committed, or aborted at the time of the failure.
  - The recovery system scans the log file forwards from the most recent checkpoint record until the end. This is called the redo phase, where the recovery system redoes all the operations of the committed transactions to ensure that their effects are reflected in the database.
  - The recovery system scans the log file backwards from the end until the most recent checkpoint record. This is called the undo phase, where the recovery system undoes all the operations of the active or aborted transactions to ensure that their effects are removed from the database.

  Restart recovery ensures that the database is restored to the most recent consistent state before the failure.



## Unit 9 - Database Security

- Database security is the use of a broad range of information security controls to protect databases and their components (data, applications, systems, servers, and network links) against compromises of their confidentiality, integrity, and availability  .
- Database security must address and protect the following aspects:
  - Data: the information stored in the database, such as personal data, financial data, health records, etc.
  - Database applications: the software programs that access and manipulate the data, such as queries, stored procedures, triggers, etc.
  - Database systems: the software that manages the database, such as MySQL, Oracle, SQL Server, etc.
  - Database servers: the hardware that hosts the database systems and applications, such as computers, storage devices, etc.
  - Network links: the communication channels that connect the database servers and applications with other systems and users, such as the internet, intranet, VPN, etc.
- Database security can be achieved by implementing a combination of the following measures  :
  - Authentication: verifying the identity of the users or systems that access the database, such as using passwords, tokens, biometrics, etc.
  - Authorization: granting or denying permissions to the users or systems that access the database, such as using roles, privileges, access control lists, etc.
  - Encryption: transforming the data into an unreadable form that can only be decrypted by authorized parties, such as using symmetric or asymmetric keys, certificates, etc.
  - Auditing: recording and monitoring the activities and events that occur in the database, such as using logs, alerts, reports, etc.
  - Backup and recovery: creating and restoring copies of the data in case of loss or corruption, such as using snapshots, replication, archiving, etc.
  - Patching and updating: applying the latest security fixes and enhancements to the database systems and applications, such as using automatic or manual updates, etc.
  - Firewall and antivirus: blocking or detecting unauthorized or malicious traffic or software that may compromise the database, such as using network or host-based firewalls, antivirus software, etc.
- Database security is especially important in the context of cloud computing, where data is stored and processed in remote servers that may be shared by multiple users or organizations. Securing cloud-based databases requires a different approach than the traditional model of situating defenses at the network’s perimeter. It demands comprehensive cloud data discovery and classification tools, plus ongoing activity monitoring and risk management.



# Types of security for the notes of the Unit 9 - Database Security in the subject of Basics of Data Base Management System

Database security refers to the process of protecting and safeguarding the database from unauthorized access or cyber-attacks. There are different types of database security that should be implemented in your business, such as:

- **Authentication**: Database authentication is the type of database security that verifies the user's login credentials which are stored in the database. If the user's login credentials match in the database, then the user can access the database. Authentication can be done using passwords, biometrics, tokens, or certificates.
- **Database Encryption**: Database encryption is the type of database security that encrypts the data stored in the database using a secret key. Encryption ensures that only authorized users can read or modify the data, even if the database is stolen or hacked. Encryption can be applied to the whole database, specific tables, columns, or rows, or individual data items.
- **Backup Database**: Backup database is the type of database security that creates a copy of the database and stores it in a safe location. Backup database ensures that the data can be restored in case of data loss, corruption, or disaster. Backup database can be done manually or automatically, using full, incremental, or differential methods.
- **Physical Security**: Physical security is the type of database security that protects the database server from physical damage, theft, or sabotage. Physical security involves locking the server room, installing security cameras, alarms, fire extinguishers, and power backup systems. Physical security also includes disposing of old or damaged storage media properly.
- **Application Security**: Application security is the type of database security that protects the database from malicious or erroneous applications that access the database. Application security involves validating the input data, sanitizing the output data, using parameterized queries, and implementing secure coding practices. Application security also includes testing and auditing the applications for vulnerabilities and bugs.
- **Access Control**: Access control is the type of database security that regulates who can access what data in the database. Access control involves assigning roles and privileges to the users, granting or revoking permissions, and enforcing policies and rules. Access control also includes logging and monitoring the user activities and database transactions.
- **Web Application Firewall**: Web application firewall is the type of database security that protects the database from web-based attacks, such as SQL/NoSQL injection, cross-site scripting, or denial-of-service. Web application firewall filters and blocks the malicious requests that try to exploit the database vulnerabilities or overload the database resources. Web application firewall can be deployed as a hardware, software, or cloud-based solution.



# System Failure

- A system failure is an event that causes the database to stop functioning normally and may result in data loss or corruption.
- System failures can be caused by various factors, such as hardware malfunctions, power outages, network disruptions, software bugs, human errors, malicious attacks, natural disasters, etc.
- System failures can affect the database security in terms of confidentiality, integrity, and availability of the data.
- Confidentiality is the protection of data from unauthorized access or disclosure. A system failure may compromise confidentiality if the data is exposed to unauthorized users or leaked to external sources.
- Integrity is the preservation of data from unauthorized modification or deletion. A system failure may compromise integrity if the data is corrupted, altered, or erased by the failure or by the recovery process.
- Availability is the assurance of data access and service delivery to authorized users and applications. A system failure may compromise availability if the database is inaccessible, slow, or unreliable due to the failure or the recovery process.
- To prevent or mitigate the impact of system failures on database security, some best practices are   :
  - Implementing backup and recovery mechanisms to restore the database to a consistent state after a failure.
  - Applying encryption and authentication techniques to protect the data from unauthorized access or disclosure.
  - Using auditing and monitoring tools to detect and respond to any abnormal or suspicious activities on the database.
  - Updating and patching the database software and hardware to fix any vulnerabilities or bugs that may cause failures.
  - Educating and training the database users and administrators on the security policies and procedures and the proper use of the database.

