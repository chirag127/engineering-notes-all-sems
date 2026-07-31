

## Unit 1 - Introduction

- In this unit, you will learn about the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be divided into two main branches: symbolic AI and sub-symbolic AI.
  - Symbolic AI is based on the idea of using symbols and rules to represent and manipulate knowledge. Examples of symbolic AI include expert systems, logic programming, and knowledge representation and reasoning.
  - Sub-symbolic AI is based on the idea of using numerical and statistical methods to model and simulate complex phenomena. Examples of sub-symbolic AI include neural networks, evolutionary algorithms, and fuzzy logic.
- AI can also be classified according to the level of intelligence and the type of task it can perform. Some common categories are:
  - Artificial narrow intelligence (ANI): AI that can perform a specific task or domain, such as playing chess, recognizing faces, or translating languages.
  - Artificial general intelligence (AGI): AI that can perform any intellectual task that a human can, such as understanding and reasoning about the world, learning from experience, and communicating with natural language.
  - Artificial superintelligence (ASI): AI that can surpass human intelligence and capabilities, such as creating new knowledge, solving any problem, and controlling other machines and systems.
  - Reactive AI: AI that can respond to stimuli and situations without any memory or learning. Examples include simple reflex agents, such as thermostats or traffic lights.
  - Limited memory AI: AI that can store and use some information from the past to improve its performance. Examples include learning agents, such as self-driving cars or chatbots.
  - Theory of mind AI: AI that can understand and model the mental states, emotions, and intentions of other agents, such as humans or animals. Examples include social robots, such as Sophia or Kismet.
  - Self-aware AI: AI that can have a sense of self, consciousness, and self-improvement. Examples include hypothetical agents, such as HAL 9000 or Skynet.
- AI can have various applications and impacts on different domains and aspects of society, such as education, health, entertainment, security, economy, and ethics. Some examples are:
  - Education: AI can enhance the learning experience and outcomes of students and teachers, such as by providing personalized feedback, adaptive content, intelligent tutoring systems, and automated grading.
  - Health: AI can improve the diagnosis, treatment, and prevention of diseases and disorders, such as by analyzing medical images, discovering new drugs, monitoring vital signs, and providing telemedicine and robotic surgery.
  - Entertainment: AI can create and enrich various forms of entertainment and art, such as by generating music, movies, games, and stories, and by interacting with users and audiences.
  - Security: AI can enhance the protection and defense of individuals, organizations, and nations, such as by detecting and preventing cyberattacks, fraud, and terrorism, and by providing surveillance and military systems.
  - Economy: AI can increase the productivity and efficiency of various industries and sectors, such as by automating and optimizing tasks, processes, and decisions, and by creating new products and services.
  - Ethics: AI can raise various ethical, social, and legal issues and challenges, such as by affecting human dignity, rights, and values, and by creating risks of bias, discrimination, and harm.



# An overview of database management system

- A database management system (DBMS) is a software system that manages the creation, storage, retrieval, modification, and protection of data in a database  .
- A database is a collection of related data that is organized in a way that facilitates data access, manipulation, and analysis.
- A DBMS serves as an interface between the end users or applications and the database, allowing them to perform various operations on the data, such as creating, reading, updating, and deleting records   .
- A DBMS also provides features such as data security, data integrity, data backup and recovery, data concurrency, data abstraction, and data independence .
- A DBMS can support different types of databases, such as relational, hierarchical, network, object-oriented, document, graph, and NoSQL databases, depending on the data model and structure .
- A DBMS can be classified into different categories based on the number of users, the location of the database, the degree of data consistency, and the type of user interface . Some examples of these categories are:

  - Single-user vs multi-user DBMS: A single-user DBMS supports only one user at a time, while a multi-user DBMS supports multiple users concurrently .
  - Centralized vs distributed DBMS: A centralized DBMS stores the database at a single location, while a distributed DBMS stores the database across multiple locations and synchronizes the data using a communication network .
  - Homogeneous vs heterogeneous DBMS: A homogeneous DBMS uses the same DBMS software and data model at all the locations, while a heterogeneous DBMS uses different DBMS software and data models at different locations .
  - Operational vs analytical DBMS: An operational DBMS supports the day-to-day transactions and operations of an organization, while an analytical DBMS supports the analysis and decision making of an organization using data from various sources .
  - Textual vs graphical DBMS: A textual DBMS uses a text-based user interface, such as a command-line or a query language, while a graphical DBMS uses a graphical user interface, such as a menu, a form, or a report .

- Some examples of popular DBMS software are Oracle, MySQL, Microsoft SQL Server, MongoDB, PostgreSQL, and SQLite .



# Database System vs File System

- A database system is a software that manages the storage, retrieval, and manipulation of data in a structured and organized way.
- A file system is a software that manages the storage, retrieval, and manipulation of data in a hierarchical and unstructured way.
- Some of the differences between database system and file system are:

| Database System | File System |
| --------------- | ----------- |
| Data is stored in tables, which consist of rows and columns. | Data is stored in files, which consist of records and fields. |
| Data is accessed using a query language, such as SQL, which allows complex and flexible operations. | Data is accessed using a file name and a record number, which allows simple and limited operations. |
| Data is organized according to a logical schema, which defines the structure and relationships of data. | Data is organized according to a physical schema, which defines the location and format of data. |
| Data is consistent and reliable, as the database system enforces integrity constraints and transaction properties. | Data is prone to inconsistency and errors, as the file system does not provide any mechanism to ensure data quality. |
| Data is shared and protected, as the database system supports concurrency control and security policies. | Data is isolated and vulnerable, as the file system does not support multiple users and access control. |



# Database System Concepts and Architecture

- A database system is a software system that manages and manipulates data stored in a database.
- A database system consists of the following components:
  - Database: a collection of related data that represents some aspect of the real world.
  - Database Management System (DBMS): a software package that provides the functionality to create, maintain, and manipulate databases.
  - Database Application: a program that interacts with the database system to perform specific tasks, such as querying, updating, or reporting data.
  - Database Users: the people or organizations that use the database system for various purposes, such as data entry, analysis, or decision making.
- A database system can be classified according to its architecture, which defines how the components are organized and communicate with each other.
- The main types of database system architectures are:
  - Centralized: a single computer system hosts the database, the DBMS, and the database applications. All database users access the database system through the same computer system.
  - Client-Server: the database system is divided into two parts: a server that hosts the database and the DBMS, and one or more clients that host the database applications. The clients communicate with the server through a network to request and receive data services.
  - Distributed: the database system is composed of multiple database systems, each of which hosts a portion of the database and the DBMS. The database systems are connected by a network and cooperate to provide data services to the database users.



# Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how the data is stored and manipulated from the users and applications.
- Data abstraction also enables data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in a database system: physical, logical, and view level.

## Physical Level

- The physical level is the lowest level of data abstraction. It describes how the data is physically stored in the storage devices and the access methods used to retrieve and update the data.
- The physical level is also called the internal level or the implementation level.
- The physical level is concerned with the data structures, file organizations, indexing techniques, and compression methods that optimize the performance and storage efficiency of the database system.
- The physical level is usually hidden from the users and applications, and only the database administrator (DBA) can access and modify it.
- The physical level is also the most difficult and complex level to design and maintain.

## Logical Level

- The logical level is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data.
- The logical level is also called the conceptual level or the data model level.
- The logical level is independent of the physical level, which means that the logical structure of the data does not depend on how the data is stored or accessed physically.
- The logical level is usually represented by a data model, such as the entity-relationship (ER) model, the relational model, or the object-oriented model.
- The logical level is the level that the users and applications interact with, and it provides a logical view of the entire database.

## View Level

- The view level is the highest level of data abstraction. It describes how the data is seen by different users and applications according to their needs and preferences.
- The view level is also called the external level or the user level.
- The view level is derived from the logical level, which means that the view level is a subset or a projection of the logical level.
- The view level can have multiple views, each of which represents a different aspect or perspective of the database.
- The view level is the level that provides the most flexibility and security to the users and applications, as they can access only the data that they are authorized to see and manipulate.



# Data Models

A data model is a type of data model that determines the logical structure of a database. It fundamentally determines in which manner data can be stored, organized and manipulated. Data models are fundamental entities to introduce abstraction in a DBMS. Data models ensure consistency in naming conventions, default values, semantics, security while ensuring quality of the data.

There are different types of data models, such as:

- **Relational data model**: This type of model designs the data in the form of rows and columns within a table. Each row represents a record and each column represents an attribute. The tables are related to each other by using primary and foreign keys. This model is based on the mathematical concept of relation and set theory . Relational data models were initially proposed by IBM researcher E.F. Codd in 1970.
- **Entity-relationship data model**: An ER model is the logical representation of data as objects and relationships among them. An object can be an entity, which is a real-world thing with a distinct identity, or an attribute, which is a property of an entity. A relationship is an association between two or more entities. ER models use symbols and diagrams to represent the data and their relationships .
- **Object-based data model**: An extension of the ER model with notions of functions, encapsulation, and object identity, as well. An object is a combination of data and methods that operate on the data. Objects can be grouped into classes, which define the common properties and behaviors of the objects. Objects can also inherit from other classes, which means they can share and modify the properties and behaviors of their parent classes .
- **Hierarchical data model**: This type of model represents one-to-many relationships in a treelike format. In this type of model, each record has a single parent record and zero or more child records. The records are organized in a hierarchy, where the root record is the topmost record and the leaf records are the bottommost records. This model is suitable for representing data that has a natural hierarchical structure, such as a file system or an organization chart .
- **Network data model**: This type of model represents many-to-many relationships in a graph-like format. In this type of model, each record can have multiple parent and child records. The records are connected by links, which are pointers that indicate the location of the related records. This model is suitable for representing data that has complex relationships, such as a social network or a transportation network .
- **Dimensional data model**: This type of model is used for data analysis and reporting purposes. It organizes the data into facts and dimensions. A fact is a numerical measure of a business event, such as a sale or a transaction. A dimension is a descriptive attribute of a fact, such as a product, a customer, or a date. Dimensions can have hierarchies, which are levels of detail within a dimension. For example, a date dimension can have a hierarchy of year, quarter, month, and day. Dimensional data models use a cube-like structure, where each side of the cube represents a dimension and the cells of the cube represent the facts .
- **Graph data model**: This type of model is used for data that has complex and dynamic relationships, such as social networks, recommendation systems, or fraud detection. It represents the data as nodes and edges. A node is an entity that has a unique identifier and a set of properties. An edge is a relationship that connects two nodes and has a type and a direction. Graph data models use graph algorithms and queries to traverse and analyze the data.



# Schema and Instances for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- A database is a collection of organized data that can be stored and managed in multiple databases using a software program called a database management system (DBMS)  .
- A database schema is an abstract design that represents the storage of data in a database. It describes both the organization of data and the relationships between tables in a given database  .
- A database schema is considered the "blueprint" of a database, which defines the structure, constraints, and operations that can be performed on the data  .
- A database schema is usually specified using a data definition language (DDL), which is a set of commands that can create, modify, or delete the schema elements  .
- A database instance is a sample of data from a database at a single moment in time. It is the data stored in a database that conforms to the schema  .
- A database instance can change over time as new data is inserted, updated, or deleted from the database. A database instance reflects the current state of the database  .
- A database instance can be represented by a set of tables, each containing a set of rows and columns that store the data values  .
- A database schema and a database instance are related, but not the same. A schema is the initial state of the database where the database is designed at first, while an instance is a state when data is loaded into the database or when any change is acquired by the corresponding database  .
- A database schema and a database instance can be illustrated by an example of a library database. The schema defines the tables, such as books, authors, and publishers, and the relationships between them, such as a book has an author and a publisher. The instance is the actual data stored in the tables, such as the title, author, and publisher of each book in the library .



# Data Independence

Data independence is the property of a database management system (DBMS) that allows the database schema to be changed without affecting the user applications that access the data. Data independence is important for maintaining data consistency, security, and integrity, as well as for facilitating data abstraction and modularity.

Data independence is of two types:

- **Physical data independence**: This is the ability to modify the physical schema of the database without affecting the logical schema or the external schema. The physical schema defines how the data is stored, organized, and accessed at the lowest level of abstraction. For example, changing the file structure, indexing method, or storage device of the data does not affect the user queries or programs that use the data.

- **Logical data independence**: This is the ability to modify the logical schema of the database without affecting the external schema or the user views. The logical schema defines the structure and relationships of the data at the conceptual level of abstraction. For example, adding, deleting, or modifying a table, attribute, or relationship does not affect the user queries or programs that use the data, as long as the external schema remains unchanged.

Some examples of data independence are:

- If the DBMS supports physical data independence, then the database administrator can change the storage structure or access method of the data without affecting the user applications. For instance, the DBA can compress the data, partition the data, or use a different hashing function to improve the performance or storage efficiency of the database.

- If the DBMS supports logical data independence, then the database designer can change the logical schema of the data without affecting the user applications. For instance, the designer can add a new attribute to a table, merge two tables into one, or split a table into two, to improve the data quality or functionality of the database.



# Database Languages and Interfaces

## Database Languages
- Database languages are the languages that allow users to define, manipulate, query, and control the access to the data stored in a database.
- There are four main types of database languages:
  - Data definition language (DDL): It creates the framework of the database by specifying the database schema, which is the structure and organization of the data. It also defines the constraints and relationships among the data. Examples of DDL commands are CREATE, ALTER, DROP, and RENAME.
  - Data manipulation language (DML): It allows users to insert, update, delete, and retrieve data from the database. It also supports queries and calculations on the data. Examples of DML commands are SELECT, INSERT, UPDATE, DELETE, and JOIN.
  - Data control language (DCL): It regulates the access and security of the data in the database. It also manages the transactions and concurrency control of the data. Examples of DCL commands are GRANT, REVOKE, COMMIT, and ROLLBACK.
  - Transaction control language (TCL): It is a subset of DCL that deals with the management of transactions, which are units of work that must be executed atomically, consistently, isolated, and durably. Examples of TCL commands are COMMIT, ROLLBACK, and SAVEPOINT.

## Database Interfaces
- Database interfaces are the ways that users can interact with the database and use the database languages.
- There are different types of database interfaces for different categories of users :
  - Menu-based interfaces for web clients or browsing: These interfaces present the user with lists of options (called menus) that lead the user through the database operations. They are suitable for novice or casual users who do not need to know the details of the database languages or structure. They are also commonly used for web applications and mobile devices.
  - Forms-based interfaces: These interfaces display the data or query results in predefined formats (called forms) that are easy to read and fill out. They are also suitable for novice or casual users who need to enter or view data in a simple and convenient way. They are often used for data entry, registration, or online shopping applications.
  - Graphical user interface (GUI): These interfaces use graphical elements (such as icons, buttons, menus, windows, etc.) to represent the data and operations in the database. They allow the user to interact with the database by using a mouse, keyboard, or touch screen. They are suitable for intermediate or advanced users who need more flexibility and functionality in the database operations. They are widely used for desktop or web-based applications that involve complex queries, data analysis, or data visualization.
  - Natural language interface: These interfaces allow the user to communicate with the database using natural language (such as English, Spanish, etc.) instead of formal database languages. They use natural language processing techniques to translate the user's input into database commands and vice versa. They are suitable for users who are not familiar with the database languages or structure, but they may not be very accurate or efficient in handling complex or ambiguous queries. They are often used for voice-based or chat-based applications that provide information or assistance to the user.
  - Application program interface (API): These interfaces allow the user to access the database through a set of predefined functions or procedures that are written in a programming language (such as Java, Python, etc.). They hide the details of the database languages and structure from the user and provide a high-level abstraction of the database operations. They are suitable for programmers or developers who need to integrate the database functionality into their own applications or systems. They are widely used for developing software applications that use the database as a backend or a data source.



# Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects in a database.
- Database objects include tables, indexes, views, schemas, sequences, aliases, locations, and users .
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas.
- DDL commands are predefined and have a specific syntax that must be followed.
- Some common DDL commands are CREATE, ALTER, DROP, RENAME, and TRUNCATE.
- DDL commands are executed by the database management system (DBMS) that manages the database.
- DDL commands can affect the data stored in the database, the metadata of the database, or the permissions of the database users.
- DDL commands are part of the Structured Query Language (SQL), which is a standard language for interacting with relational databases.
- DDL commands can be used to define the logical and physical structure of the database, such as the data types, constraints, keys, and indexes of the tables.
- DDL commands can also be used to modify the existing structure of the database, such as adding, deleting, or changing columns, tables, views, or indexes.
- DDL commands can be executed interactively or in batches, depending on the DBMS and the user interface.
- DDL commands can be stored in files or scripts that can be executed later or transferred to other databases.
- DDL commands can be used to create or delete databases, schemas, or users, as well as grant or revoke privileges to them.
- DDL commands can be used to create or delete views, which are virtual tables that show a subset or a combination of data from one or more tables.
- DDL commands can be used to create or delete indexes, which are data structures that improve the performance of queries on the tables.
- DDL commands can be used to create or delete sequences, which are objects that generate sequential numbers for primary keys or other purposes.
- DDL commands can be used to create or delete aliases, which are alternative names for tables, views, or columns.
- DDL commands can be used to create or delete locations, which are objects that specify the physical location of the data files on the disk.



# DML

DML stands for Data Manipulation Language. It is a family of computer languages that are used to manipulate data in a database. DML includes commands that allow users to:

- Insert data into database tables
- Retrieve data from database tables
- Delete data from database tables
- Update data in database tables

Some of the main DML statements are:

- SELECT: This statement is used to query data from one or more tables or views. It can specify the columns, conditions, order, and grouping of the data to be retrieved.
- INSERT: This statement is used to add new rows of data to a table. It can specify the values for each column or use a subquery to get the values from another table.
- DELETE: This statement is used to remove existing rows of data from a table. It can specify the conditions for the rows to be deleted or use a subquery to get the rows from another table.
- UPDATE: This statement is used to modify existing rows of data in a table. It can specify the new values for each column or use a subquery to get the values from another table. It can also specify the conditions for the rows to be updated.

DML is mostly incorporated in SQL databases, which are relational databases that use the Structured Query Language (SQL) as the standard language for accessing and manipulating data. SQL is a declarative language, which means that it specifies what data to get or change, but not how to do it. The database system is responsible for executing the DML statements and returning the results to the user or application.

DML is different from DDL (Data Definition Language), which is used to define the structure and schema of the database, such as tables, columns, constraints, indexes, etc. DML is also different from DCL (Data Control Language), which is used to control the access and permissions of the database, such as granting or revoking privileges, roles, etc.

DML triggers are a special type of stored procedure that automatically takes effect when a DML event occurs on a table or view. DML triggers can be used to enforce business rules, audit data changes, perform cascading actions, etc. DML triggers can be defined for INSERT, UPDATE, or DELETE statements, and can be executed before or after the statement. DML triggers can also access the inserted and deleted tables, which contain the rows affected by the DML statement. DML triggers are written in Transact-SQL, which is an extension of SQL that adds procedural features and database-specific functions.



# Overall database structure for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

- A database is a collection of related data that is organized and stored in a structured way.
- A database management system (DBMS) is a software system that allows users to create, manipulate, and access databases.
- A DBMS consists of three components: data, data dictionary, and database engine.
- Data is the actual information stored in the database, such as tables, records, and fields.
- Data dictionary is a set of metadata that describes the structure, format, and constraints of the data in the database.
- Database engine is the core component that performs the operations on the data, such as querying, updating, and enforcing integrity rules.
- A DBMS can be classified into different types based on the data model, the level of abstraction, and the degree of distribution.
- A data model is a logical representation of the data and the relationships among them. Some common data models are relational, hierarchical, network, and object-oriented.
- The level of abstraction refers to the degree of detail that is hidden from the users. There are three levels of abstraction: physical, logical, and view.
- The physical level describes how the data is physically stored and accessed in the database.
- The logical level describes the structure and meaning of the data, independent of the physical implementation.
- The view level describes how the data is presented to different users or applications, depending on their needs and preferences.
- The degree of distribution refers to how the data is distributed across multiple locations or systems. There are three types of distribution: centralized, decentralized, and distributed.
- A centralized database is stored and managed by a single system, and accessed by multiple users or applications over a network.
- A decentralized database is divided into multiple independent databases, each stored and managed by a different system, and accessed by local users or applications.
- A distributed database is composed of multiple interconnected databases, each stored and managed by a different system, and accessed by global users or applications as a single logical database.



# Transaction Management

Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations. It is a transaction is a program unit whose execution may or may not change the contents of a database. Not managing concurrent access may create issues like hardware failure and system crashes.

## Transaction States

There are various database transaction states as follows:

- Active state - this is the state in which the transaction is being executed. It involves reading and writing operations on the database.
- Partially committed state - this is the state in which the transaction has executed its final statement, but the changes are not yet permanent in the database.
- Committed state - this is the state in which the transaction has completed successfully and the changes are permanent in the database.
- Failed state - this is the state in which the transaction has encountered an error or an abort command and cannot continue execution.
- Aborted state - this is the state in which the transaction has been rolled back and the database is restored to its previous state before the transaction started.

## Transaction Properties

A transaction must satisfy four properties, known as ACID properties, to ensure data integrity and consistency :

- Atomicity - this means that the transaction is either executed in its entirety or not executed at all. If any part of the transaction fails, the whole transaction is aborted and the database is left unchanged.
- Consistency - this means that the transaction must preserve the integrity constraints and business rules of the database. The database must remain in a consistent state before and after the transaction.
- Isolation - this means that the transaction must not interfere with other concurrent transactions. The intermediate results of the transaction must not be visible to other transactions until the transaction is committed.
- Durability - this means that the changes made by the transaction must persist even in the event of system failures or power outages. The committed data must be stored in a non-volatile memory.

## Transaction Management Techniques

There are various techniques used by the DBMS to manage transactions and ensure ACID properties, such as:

- Locking - this is a mechanism that prevents concurrent access to the same data item by different transactions. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. There are different types of locks, such as shared locks, exclusive locks, and deadlock prevention and detection methods.
- Timestamping - this is a mechanism that assigns a unique timestamp to each transaction and each data item. The timestamp indicates the order of execution of the transactions and the data items. A transaction can read or write a data item only if its timestamp is compatible with the timestamp of the data item, otherwise it is aborted or delayed.
- Logging - this is a mechanism that records the changes made by the transactions in a log file. The log file contains information such as the transaction id, the data item, the old value, and the new value. The log file is used to recover the database in case of system failures or transaction aborts. There are different types of logging, such as undo logging, redo logging, and undo/redo logging.
- Checkpointing - this is a mechanism that periodically writes the contents of the main memory to the disk. This reduces the amount of data that needs to be recovered in case of system failures or transaction aborts. A checkpoint is a point in time when the database is in a consistent state and all the transactions have either committed or aborted.



# Storage Management for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- Storage management is the method by which organizations ensure data integrity, access, policy/regulation compliance, and effective storage resource use.
- Storage management involves developing a plan to provision, configure, back up, and monitor data storage infrastructure to prevent data loss, performance slowdowns, and access problems.
- Storage management also provides better visibility into the data, enabling organizations to more easily extract value from the data.
- A DBMS must store data persistently in files or datasets of some sort. Depending on the DBMS, table spaces and index spaces each may require one, or possibly more, files to store the actual data.
- Data storage system can be explained as the capacity secured by the database management system in the memory of the server allocated for the database and the related operations.
- A few of the commonly used primary devices for data storage in the database management systems are the CPU’s main memory, the CPU’s registers and otherwise known as the internal memory and the cache memory of the server that is accessible to the CPU for an uninterrupted data flow.
- Here are some general methods and services for data storage management:
  - storage resource management software
  - consolidation of systems
  - multiprotocol storage arrays
  - storage tiers
  - strategic SSD deployment
  - hybrid cloud
  - scale-out systems
  - archive storage of infrequently accessed data
  - elimination of duplicate data



# Database Users and Administrator

Database users and administrator are the people who are accessing or working with the database. The primary aim of the database management system (DBMS) is to store the data or information and retrieve it whenever it is needed by the database users. There are different types of database users and administrator, depending on their roles and responsibilities. Some of the common types are:

- **Native Users**: These are the database users who are communicating with the database through an already written program. For example, when a student uses an online portal to check their grades, they are native users. They do not need to know the details of the database or the query language. They just interact with the user interface of the program.
- **Application Programmers**: These are the software developers and programming professionals who write the programs that access the database. They use a programming language such as Java, Python, C#, etc. and a query language such as SQL to manipulate the data in the database. They need to know the logical structure and schema of the database, as well as the rules and constraints that apply to the data.
- **Sophisticated Users**: These are the database users who have a good knowledge of the query language and the database system. They can directly interact with the database using a query tool or a command-line interface. They can write complex queries to perform various operations on the data. They may also use the database for analytical purposes, such as data mining, data warehousing, etc.
- **Casual Users**: These are the database users who occasionally access the database for some specific purpose. They may not have a regular or well-defined need for the database. They may use a menu-driven or form-based interface to query the database. They do not need to know the query language or the database system. They just need to know the basic functionality of the interface.
- **Database Administrator (DBA)**: Database administrator (DBA) is a person or a team who defines the schema and also controls the three levels of the database. They have full control and authority over the database. They are responsible for creating, maintaining, securing, and optimizing the database. They perform tasks such as:

  - Defining the logical and physical schemas of the database
  - Creating and managing the database objects, such as tables, views, indexes, etc.
  - Granting and revoking the permissions and privileges to the database users and roles
  - Monitoring and tuning the performance of the database
  - Backing up and restoring the database
  - Implementing the policies and procedures for the database
  - Troubleshooting and resolving the database issues

A database administrator can use a superuser account to access the database. A superuser account is a special type of login that has full administrative permissions on all databases as a server-level principal. A database administrator can also create and manage other logins and user accounts for the database. A login is an individual account for logging in to the database server. A user account is the identity of the login when it is connected to a database. A user account can use the same name as the login, but that is not required. A user account can have different permissions and roles in different databases.



## Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is the process of designing and documenting the structure and semantics of data for a specific application domain.
- The Entity Relationship (ER) model is a widely used conceptual data model that represents data as entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified uniquely and has some properties of interest.
- An attribute is a property or characteristic of an entity that describes some aspect of it.
- A relationship is an association or link between two or more entities that expresses some meaningful connection or dependency among them.
- The ER model can be represented graphically using an ER diagram, which consists of the following symbols:
  - Rectangles for entities
  - Ellipses for attributes
  - Diamonds for relationships
  - Lines for connecting entities and relationships
  - Cardinality ratios and participation constraints for specifying the degree and optionality of relationships
- The ER model can be used to design a database schema, which is a formal description of the data and its constraints in a database management system.
- The ER model can also be used to perform data analysis, which is the process of understanding the data requirements and characteristics of a problem domain.
- The ER model can be extended with additional features, such as:
  - Subclasses and superclasses for representing specialization and generalization of entities
  - Aggregation and composition for representing part-of relationships among entities
  - Weak entities and identifying relationships for representing entities that depend on other entities for their existence and identification
  - Multi-valued and derived attributes for representing attributes that can have more than one value or are computed from other attributes
  - Complex and composite attributes for representing attributes that are structured or composed of other attributes
- The ER model can be mapped to a relational model, which is another widely used data model that represents data as tables, columns, and rows.
- The mapping rules depend on the features and constraints of the ER model and the relational model, and may involve the following steps:
  - Mapping entities to tables
  - Mapping attributes to columns
  - Mapping relationships to tables or columns
  - Mapping cardinality ratios and participation constraints to primary keys and foreign keys
  - Mapping subclasses and superclasses to tables or columns
  - Mapping aggregation and composition to tables or columns
  - Mapping weak entities and identifying relationships to tables or columns
  - Mapping multi-valued and derived attributes to tables or columns
  - Mapping complex and composite attributes to tables or columns
- The mapping process may result in some redundancy or inconsistency in the data, which can be reduced or eliminated by applying normalization techniques, such as:
  - First normal form (1NF) for eliminating multi-valued and composite attributes
  - Second normal form (2NF) for eliminating partial functional dependencies
  - Third normal form (3NF) for eliminating transitive functional dependencies
  - Boyce-Codd normal form (BCNF) for eliminating non-trivial functional dependencies that are not determined by candidate keys
  - Fourth normal form (4NF) for eliminating multi-valued dependencies
  - Fifth normal form (5NF) for eliminating join dependencies
- The ER model and the relational model are not the only data models available, and there are other alternatives, such as:
  - Object-oriented data model for representing data as objects, classes, and methods
  - XML data model for representing data as hierarchical and semi-structured documents
  - NoSQL data model for representing data as key-value pairs, documents, graphs, or columns
- The choice of data model depends on the characteristics and requirements of the data and the application domain, and may involve trade-offs between performance, scalability, flexibility, and consistency.



# ER Model Concepts

The ER model is a conceptual data model that describes the entities, attributes, and relationships in a database. It is used to design and represent the logical structure of a database. The ER model consists of the following concepts:

- **Entity**: An entity is a real-world object or thing that can be identified uniquely. For example, a student, a course, a book, etc. An entity type is a collection of entities that share the same properties or characteristics. For example, the entity type Student represents all the students in a database. An entity occurrence or instance is a specific entity of an entity type. For example, John is an entity occurrence of the entity type Student.

- **Attribute**: An attribute is a property or characteristic of an entity that describes some aspect of it. For example, name, age, address, etc. are attributes of the entity type Student. An attribute can have a single value or multiple values for an entity. For example, name is a single-valued attribute, while phone number is a multi-valued attribute. An attribute can also have a domain, which is the set of possible values for that attribute. For example, the domain of age is the set of positive integers.

- **Relationship**: A relationship is an association or connection between two or more entities. For example, a student enrolls in a course, a book belongs to a library, etc. A relationship type is a collection of relationships that share the same meaning or semantics. For example, the relationship type Enrolls represents all the enrollments of students in courses in a database. A relationship occurrence or instance is a specific relationship of a relationship type. For example, John enrolls in DBMS is a relationship occurrence of the relationship type Enrolls.

- **Cardinality**: Cardinality is the number of occurrences of one entity that can be associated with a single occurrence of another entity in a relationship. For example, the cardinality of the relationship type Enrolls can be one-to-many, meaning that one student can enroll in many courses, but one course can have only one student enrolled. Cardinality can also be many-to-many, meaning that one student can enroll in many courses, and one course can have many students enrolled.

- **ER Diagram**: An ER diagram is a graphical representation of the ER model using symbols and notation. It shows the entity types, attributes, relationships, and cardinalities in a database. An ER diagram can be used to communicate the design and structure of a database to the users and developers. An ER diagram consists of the following symbols:

  - A rectangle represents an entity type.
  - An oval represents an attribute of an entity type.
  - A diamond represents a relationship type.
  - A line connects an entity type to a relationship type or an attribute to an entity type.
  - A double line indicates a total participation of an entity type in a relationship type, meaning that every entity occurrence must participate in at least one relationship occurrence.
  - A single line indicates a partial participation of an entity type in a relationship type, meaning that some entity occurrences may not participate in any relationship occurrence.
  - A double oval indicates a derived attribute, meaning that its value can be derived from other attributes or relationships.
  - A dashed oval indicates a multi-valued attribute, meaning that it can have more than one value for an entity occurrence.
  - A small circle on a line indicates an optional attribute, meaning that it can have a null value for an entity occurrence.
  - A small oval with a letter inside indicates a key attribute, meaning that it can uniquely identify an entity occurrence.

  Here is an example of an ER diagram for a university database:

  ER diagram example



# Notation for ER diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw ER diagrams, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entities**: Entities are the basic objects or concepts in the database, such as customers, products, orders, etc. They are represented by rectangles with the entity name inside. For example:

entity

- **Attributes**: Attributes are the properties or characteristics of the entities, such as name, age, price, quantity, etc. They are represented by ovals with the attribute name inside, connected to the entity by a line. For example:

attribute

- **Relationships**: Relationships are the associations or interactions between the entities, such as buys, sells, owns, etc. They are represented by diamonds with the relationship name inside, connected to the entities by lines. For example:

relationship

- **Cardinality**: Cardinality is the number of occurrences or instances of one entity that can be related to another entity in a relationship. It is usually expressed by the minimum and maximum number of entities that can participate in the relationship. For example, one customer can buy many products, but one product can be bought by only one customer. This is a one-to-many relationship. Cardinality can be represented by different notations, such as arrow notation, crow's foot notation, Chen notation, etc. For example:

cardinality

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. They are used to enforce the integrity and consistency of the data. There are different types of keys, such as primary key, foreign key, candidate key, etc. For example, a primary key is an attribute that uniquely identifies each entity in an entity set, such as customer ID, product ID, etc. A foreign key is an attribute that references the primary key of another entity or relationship, such as product ID in the order entity. Keys are usually represented by underlining the attribute name or adding a key symbol next to it. For example:

key

- **Types**: Types are the data types or domains of the attributes, such as integer, string, date, etc. They specify the format and range of values that an attribute can take. Types are usually represented by adding the type name next to the attribute name or inside parentheses. For example:

type

These are some of the basic notations and symbols used to draw ER diagrams. Depending on the modeling methodology and the level of abstraction, there may be more notations and symbols to represent other concepts, such as generalization, specialization, aggregation, composition, etc. For more details and examples, you can refer to the following sources:

: Entity Relationship (ER) Diagram Model with DBMS Example - Guru99
: Guide to entity-relationship diagram notations & symbols - Gleek
: E-R NOTATION - Computer Notes
: Entity-Relationship Diagram Symbols and Notation | Lucidchart



# Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are data constraints that express the number of entities to which another entity can be related via a relationship set .
- Mapping constraints are also known as the cardinality ratio, which corresponds to the number of relationship occurrences an entity can be involved in an entity-relationship model.
- Mapping constraints are most useful in describing the relationship sets that involve more than two entity sets, such as ternary or n-ary relationships.
- Mapping constraints can be classified into two types: participation constraints and cardinality constraints.

## Participation Constraints
- Participation constraints specify whether the existence of an entity depends on its being related to another entity via the relationship set.
- Participation constraints can be either total or partial.
- Total participation means that every entity in the entity set must participate in at least one relationship in the relationship set.
- Partial participation means that some entities in the entity set may not participate in any relationship in the relationship set.
- Participation constraints are shown by a double line connecting the entity set and the relationship set in an ER diagram.

## Cardinality Constraints
- Cardinality constraints specify the maximum number of relationship instances that an entity can participate in.
- Cardinality constraints can be one-to-one, one-to-many, many-to-one, or many-to-many.
- One-to-one means that an entity in one entity set can be related to at most one entity in another entity set, and vice versa.
- One-to-many means that an entity in one entity set can be related to many entities in another entity set, but an entity in the other entity set can be related to at most one entity in the first entity set.
- Many-to-one means that an entity in one entity set can be related to at most one entity in another entity set, but an entity in the other entity set can be related to many entities in the first entity set.
- Many-to-many means that an entity in one entity set can be related to many entities in another entity set, and an entity in the other entity set can be related to many entities in the first entity set.
- Cardinality constraints are shown by placing numbers or symbols on the relationship lines in an ER diagram.

## Example of Mapping Constraints
- Consider the following ER diagram of a university database, where the entity sets are Student, Course, and Instructor, and the relationship sets are Enroll, Teach, and Advise.

ER diagram of a university database

- The participation constraints are as follows:
  - Every student must enroll in at least one course, so the participation of Student in Enroll is total.
  - Every course must have at least one student enrolled, so the participation of Course in Enroll is total.
  - Every instructor must teach at least one course, so the participation of Instructor in Teach is total.
  - Every course must have at least one instructor teaching it, so the participation of Course in Teach is total.
  - Every student must have exactly one instructor as an advisor, so the participation of Student in Advise is total.
  - Not every instructor must advise a student, so the participation of Instructor in Advise is partial.
- The cardinality constraints are as follows:
  - A student can enroll in many courses, but a course can have at most one student enrolled, so the cardinality of Enroll is one-to-many from Course to Student.
  - An instructor can teach many courses, but a course can have at most one instructor teaching it, so the cardinality of Teach is one-to-many from Course to Instructor.
  - A student can have only one instructor as an advisor, but an instructor can advise many students, so the cardinality of Advise is many-to-one from Student to Instructor.



# Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical and conceptual tool for data modeling using entities, attributes, and relationships.
- Entities are the basic objects or things that exist in the database, such as people, places, events, or concepts. They are represented by rectangles in an ER diagram.
- Attributes are the properties or characteristics of entities that describe them. They are represented by ovals in an ER diagram. Attributes can be classified into different types, such as simple, composite, single-valued, multi-valued, derived, or key attributes.
- Relationships are the associations or connections between entities that indicate how they are related to each other. They are represented by diamonds in an ER diagram. Relationships can have different types, such as one-to-one, one-to-many, many-to-one, or many-to-many. Relationships can also have attributes, such as name, role, or cardinality.
- An ER diagram is a graphical representation of the ER model that shows the entities, attributes, and relationships in a database. An ER diagram can be used to communicate the database design to the developers, users, and stakeholders. An ER diagram can also be used to check the consistency and completeness of the database design.
- An ER diagram can be converted into a relational schema, which is a set of tables and columns that store the data in a relational database. The conversion process involves mapping the entities, attributes, and relationships in the ER diagram to the tables, columns, and constraints in the relational schema. The conversion rules may vary depending on the type and level of the ER model.



# Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- There can be more than one super key for a table, but only one candidate key .
- A super key can also be NULL, unless the table has a primary key constraint.
- A super key can be used to enforce referential integrity, which means that the values of a super key in one table must match the values of a corresponding super key in another table.

## Example of Super Key

- Consider a table STUDENT with the following attributes: ID, Name, Age, Address, Phone, Email.
- A possible super key for this table is {ID, Name, Age, Address, Phone, Email}, which contains all the attributes of the table and can uniquely identify each student.
- Another possible super key for this table is {ID, Phone}, which contains only two attributes and can also uniquely identify each student.
- A candidate key for this table is {ID}, which is the minimal set of attributes that can uniquely identify each student.
- A primary key for this table can be {ID}, which is a candidate key that is chosen to be the main identifier for the table.



# Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a database  .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and removing any attribute from it would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier of the relation.
- The other candidate keys that are not chosen as the primary key are called alternate keys or secondary keys.
- A candidate key can be a single attribute or a combination of attributes, depending on the data requirements and constraints.
- A candidate key should satisfy the following properties:
  - Uniqueness: No two tuples in the relation should have the same values for the candidate key attributes.
  - Irreducibility: No subset of the candidate key attributes should have the uniqueness property.
  - Non-nullability: The candidate key attributes should not have null values in any tuple.



# Primary Key

- A primary key is a column or a combination of columns in a relational database table that uniquely identifies each record in the table .
- A primary key is a choice of candidate key, which is a minimal superkey, meaning that it has the smallest possible number of columns that can uniquely identify each record .
- A primary key can be either natural or surrogate. A natural key is based on real-world observables, such as a social security number or an email address. A surrogate key is created to function as a key and not used for identification outside the database, such as an auto-incremented ID or a UUID .
- A primary key must be entered when a record is created, and it should never be changed. It must not contain null values .
- A primary key is used as a unique identifier to quickly parse data within the table and to link to related information in other tables through foreign keys  .
- A primary key can be simple or composite. A simple primary key consists of a single column, while a composite primary key consists of two or more columns.



# Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model

- An entity-relationship model (or ER model) describes interrelated things of interest in a specific domain of knowledge.
- A basic ER model is composed of entity types (which classify the things of interest) and specifies relationships that can exist between entities (instances of those entity types).
- Generalization is a bottom-up approach in which two lower level entities combine to form a higher level entity .
- In generalization, the higher level entity can also combine with other lower level entities to make further higher level entity.
- In generalization, the higher level entity inherits the properties of all the lower level entities .
- Generalization is used to hide the details of a set of objects and create a generalized entity from them.
- Generalization is represented by a triangle with a line connecting the higher level entity to the lower level entities  .
- An example of generalization is shown below:

generalization example

- In this example, the entities Student and Teacher are generalized into a higher level entity Person, which inherits the attributes name, age and gender from them.
- The entity Person can also be generalized with other entities, such as Employee or Customer, to form a further higher level entity, such as Human.



# Aggregation in Entity Relationship Model

- Aggregation is a technique to model a relationship involving a relationship set and one or more entity sets .
- Aggregation allows us to treat a relationship set as an entity set for purposes of participation in other relationships .
- Aggregation is an abstraction through which we can represent relationships as higher level entity sets.
- Aggregation protects the integrity of an assembly of objects by defining a single point of control.
- Aggregation is useful when we need to express a relationship among relationships .

## Example of Aggregation

- Consider a scenario where an employee works for a project and requires some machinery.
- We can model the relationship between employee and project as WORKS_FOR, and the relationship between employee and machinery as REQUIRES.
- However, this does not capture the fact that the employee requires the machinery for a specific project, not in general.
- To express this constraint, we can use aggregation to treat the WORKS_FOR relationship as an entity set, and relate it to the machinery entity set with a new relationship called NEEDS.
- The diagram below shows the aggregation of WORKS_FOR and NEEDS.

Aggregation Example



# Reduction of an ER Diagram to Tables

- An ER diagram is a graphical representation of the entities and relationships in a database.
- A table is a collection of rows and columns that store data in a database.
- The process of converting an ER diagram to tables is called reduction or mapping.
- The reduction of an ER diagram to tables involves the following steps:

  - Convert all the entities in the diagram to tables. All the entities represented in the rectangular box in the ER diagram become independent tables in the database. Each table should have a primary key that uniquely identifies each row. The attributes of the entity become the columns of the table.
  - Convert all the relationships in the diagram to tables or foreign keys. All the relationships represented by diamonds in the ER diagram can be mapped to tables or foreign keys depending on the cardinality and participation of the entities involved. A foreign key is a column or a set of columns that references the primary key of another table. The foreign key establishes a link between the tables and ensures referential integrity.
  - For one-to-one relationships, choose one of the entities to be the parent and the other to be the child. Add the primary key of the parent entity as a foreign key in the child entity table. Alternatively, you can create a separate table for the relationship and include the primary keys of both entities as foreign keys in the relationship table.
  - For one-to-many relationships, choose the entity on the one side to be the parent and the entity on the many side to be the child. Add the primary key of the parent entity as a foreign key in the child entity table.
  - For many-to-many relationships, create a separate table for the relationship and include the primary keys of both entities as foreign keys in the relationship table. This table is also called a junction table or an associative table. If the relationship has any attributes, include them as columns in the relationship table.
  - For weak entities, create a separate table for the weak entity and include all its attributes. Also, include the primary key of the strong entity that identifies the weak entity as a foreign key in the weak entity table. Declare the combination of the foreign key and the partial key (or discriminator) of the weak entity as the primary key of the weak entity table. A weak entity is an entity that does not have a key attribute of its own and depends on another entity for its existence. A partial key is an attribute that can uniquely identify a weak entity within the scope of its strong entity. A discriminator is an attribute that distinguishes the weak entities that are related to the same strong entity.
  - For composite attributes, include each component attribute as a separate column in the table. A composite attribute is an attribute that can be divided into sub-attributes. For example, an address attribute can be divided into street, city, state, and zip code sub-attributes.
  - For multivalued attributes, create a separate table for the attribute and include the primary key of the entity and the attribute value as columns in the table. Declare the combination of the primary key and the attribute value as the primary key of the attribute table. A multivalued attribute is an attribute that can have more than one value for a given entity. For example, a person can have more than one phone number.
  - For derived attributes, do not include them in the table as they can be computed from other attributes. A derived attribute is an attribute that can be derived from other attributes using a formula or a function. For example, the age of a person can be derived from the date of birth attribute.



# Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts   :

- **Subclasses and Superclasses**: A subclass is a subset of entities of a superclass that share some common attributes or relationships distinct from other entities in the superclass. A superclass is a set of entities that have some common attributes or relationships. For example, a superclass PERSON can have subclasses STUDENT and EMPLOYEE, each with their own attributes and relationships.
- **Specialization and Generalization**: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics of the entities in the superclass. Generalization is the reverse process of abstraction, where common properties of subclasses are grouped together to form a superclass. For example, a specialization of PERSON can be based on the attribute occupation, and a generalization of STUDENT and EMPLOYEE can be PERSON.
- **Category or Union Type**: A category or union type is a subclass that represents a collection of entities from different superclasses that share some common attributes or relationships. A category or union type is also called a shared subclass. For example, a category or union type PART-TIME-EMPLOYEE can include entities from subclasses STUDENT and EMPLOYEE that work part-time.
- **Aggregation**: Aggregation is the process of grouping together a set of entities and relationships into a single abstract entity type. An aggregation can be seen as a relationship between a whole entity and its component entities. For example, an aggregation of COURSE, STUDENT and INSTRUCTOR can form a CLASS entity type, which represents the relationship of a course being taught by an instructor to a set of students.

The extended ER model can be represented graphically using the following symbols:

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type, or between an attribute and an entity type or a relationship type
- A triangle for a superclass-subclass relationship, with the superclass above the triangle and the subclasses below the triangle
- A circle with d for a disjoint constraint, which means that an entity can belong to only one subclass of a superclass
- A circle with o for an overlap constraint, which means that an entity can belong to more than one subclass of a superclass
- A circle with c for a completeness constraint, which means that every entity in the superclass must belong to at least one subclass
- A dashed rectangle for an aggregation, with the component entity types and relationship types inside the rectangle and the aggregate entity type outside the rectangle

Here is an example of an extended ER diagram for a university database:

EER diagram



# Relationships of Higher Degree

- A relationship in an ER model is an association between two or more entity sets.
- The degree of a relationship is the number of entity sets involved in the relationship .
- A relationship of degree two is called a binary relationship, and it is the most common type of relationship in ER models.
- A relationship of degree three is called a ternary relationship, and it involves three entity sets.
- A relationship of degree n is called an n-ary relationship, and it involves n entity sets.
- Higher degree relationships (n > 2) are more complex and less common than binary relationships, and they may be difficult to convert to relational tables.
- Higher degree relationships can sometimes be replaced by a combination of binary relationships using an associative entity set  .
- An associative entity set is an entity set that represents the association between two or more other entity sets, and it may have its own attributes and relationships .
- For example, a ternary relationship between entity sets Student, Course, and Instructor can be replaced by an associative entity set Enrollment that has relationships with Student, Course, and Instructor, and has an attribute Grade .
- The advantage of using an associative entity set is that it simplifies the ER model and makes it easier to convert to a relational model .
- The disadvantage of using an associative entity set is that it may introduce redundancy and inconsistency in the data, and it may lose some information about the original higher degree relationship .



## Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table consists of rows (records) and columns (attributes).
- A primary key is a column or a combination of columns that uniquely identifies each row in a table.
- A foreign key is a column or a combination of columns that references a primary key in another table, to establish a relationship between the tables.
- A relationship is a logical association between two or more tables, based on a common attribute or a foreign key.
- There are three types of relationships: one-to-one, one-to-many, and many-to-many.
- A one-to-one relationship occurs when each row in one table is related to exactly one row in another table.
- A one-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to exactly one row in the first table.
- A many-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and each row in the other table is related to zero or more rows in the first table.
- A many-to-many relationship requires a third table, called a junction table or an associative table, to store the combinations of primary keys from the two related tables.
- A relational schema is a graphical representation of the structure and relationships of a relational database, using symbols and notation to indicate the tables, columns, keys, and relationships.
- A relational model is a set of rules and constraints that define how data is stored and manipulated in a relational database, such as the entity integrity rule, the referential integrity rule, and the normalization rules.
- The entity integrity rule states that no primary key column can have null (missing or unknown) values, and that each table must have a primary key.
- The referential integrity rule states that if a foreign key exists in a table, it must either match a primary key value in another table or be null.
- Normalization is a process of organizing the data in a relational database to reduce redundancy and improve data integrity, by applying a series of normal forms or rules.
- The first normal form (1NF) states that each column in a table must have atomic values, meaning that they cannot be divided into smaller parts, and that there must be no repeating groups of columns.
- The second normal form (2NF) states that each table must be in 1NF, and that each non-key column in a table must depend on the whole primary key, not just a part of it.
- The third normal form (3NF) states that each table must be in 2NF, and that each non-key column in a table must depend only on the primary key, not on any other non-key column.



# Introduction to Relational Database

- A relational database is a type of database that stores and provides access to data points that are related to one another.
- A relational database is based on the relational model, an intuitive, straightforward way of representing data in tables .
- In a relational database, each row in the table is a record with a unique ID called the key, and each column in the table is an attribute that describes some aspect of the data.
- A relational database can have multiple tables, and each table can have a different schema (the structure and definition of the data in the table).
- A relational database can establish relationships between the tables using foreign keys, which are references to the primary keys of other tables.
- A relational database can be manipulated using a query language, such as SQL, which allows users to create, read, update, and delete data in the database.
- A relational database can also support transactions, which are sequences of operations that must be executed atomically, consistently, isolated, and durably (ACID properties).
- A relational database is managed by a relational database management system (RDBMS), which is a software system that provides tools and interfaces for creating, maintaining, and querying relational databases.
- Some examples of popular RDBMS are Oracle, MySQL, PostgreSQL, Microsoft SQL Server, and SQLite.



# Relational Database Structure

- A relational database is a collection of data organized into tables, where each table consists of rows and columns.
- Each row in a table represents a record or a tuple, and each column represents an attribute or a field of the record.
- Each table has a primary key, which is a column or a combination of columns that uniquely identifies each record in the table.
- Tables can be related to each other through foreign keys, which are columns that refer to the primary key of another table.
- The relationship between tables can be one-to-one, one-to-many, or many-to-many, depending on how many records in one table can be associated with records in another table.
- A relational database schema is a set of tables and their relationships, along with constraints and rules that define the integrity and validity of the data.
- A relational database can be manipulated using a query language, such as SQL, which allows users to create, update, delete, and retrieve data from the tables.
- A relational database can also be modeled using an entity-relationship diagram, which is a graphical representation of the entities, attributes, and relationships in the database.



# Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relational database .
- A domain defines the **data type**, **format**, and **constraints** of an attribute .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- For example, the domain of Marital Status can have the values {Married, Single, Divorced}, and the domain of Shift can have the values {Mon, Tue, Wed, Thu, Fri, Sat, Sun}.
- A domain can be **simple** or **composite**, depending on whether it is composed of one or more subdomains.
- For example, the domain of Address can be a composite domain consisting of subdomains for Street, City, State, and Zip Code.
- A domain can be **scalar** or **nonscalar**, depending on whether it can hold only one value or a collection of values.
- For example, the domain of Phone Number can be a nonscalar domain that can hold multiple phone numbers for a person.
- A domain can be **user-defined** or **system-defined**, depending on whether it is created by the user or the database system.
- For example, the domain of Date can be a system-defined domain that has a predefined format and range.
- A domain can be **named** or **unnamed**, depending on whether it has a specific name or not.
- For example, the domain of Marital Status can be a named domain, while the domain of {1, 2, 3} can be an unnamed domain.
- A domain can be **shared** or **local**, depending on whether it is used by more than one attribute or not.
- For example, the domain of Employee ID can be a shared domain that is used by multiple attributes in different relations, while the domain of Salary can be a local domain that is used by only one attribute in one relation.



# Attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- A relational database is a collection of data organized into tables with rows and columns. Each row represents an entity and each column represents an attribute of the entity.   
- A relation is a set of tuples (rows) that have the same attributes (columns). A relation can also be called a table or a file. A relation has a name and a degree (the number of attributes). 
- An attribute is a property or characteristic of an entity or a relation. An attribute has a name and a domain (the set of possible values). An attribute can also be called a field or a column.  
- A primary key is an attribute or a combination of attributes that uniquely identifies each tuple in a relation. A primary key cannot have null values and must be unique for each tuple. A relation can have only one primary key. 
- A foreign key is an attribute or a combination of attributes in one relation that refers to the primary key of another relation. A foreign key establishes a relationship between two relations. A foreign key can have null values and can be duplicated. A relation can have more than one foreign key. 
- A relational database management system (RDBMS) is a software that allows users to create, manipulate, and query relational databases. An RDBMS provides a set of operations to perform on relations, such as insertion, deletion, modification, selection, projection, join, union, intersection, difference, etc. An RDBMS also ensures the integrity, security, and consistency of the data.   
- A relational database schema is a collection of relation schemas, where each relation schema defines the name, attributes, and constraints of a relation. A relational database schema also defines the primary keys and foreign keys of the relations. A relational database schema represents the logical structure of a relational database.  
- A relational database design is a process of creating a relational database schema that satisfies the requirements of the users and avoids data redundancy, inconsistency, and anomalies. The design process consists of the following steps: 
  - Determine the purpose of the database
  - Find and organize the information required
  - Divide the information into tables
  - Turn information items into columns
  - Specify primary keys
  - Set up the table relationships
  - Refine the design
  - Apply the normalization rules



# Tuples for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- A tuple is a row of values in a table that represents an entity or a relationship instance.
- A tuple can also be called a record or a fact.
- A tuple consists of one or more attributes, which are the columns of the table that describe the properties of the entity or the relationship.
- A tuple can be identified by a primary key, which is a unique combination of one or more attributes that distinguishes it from other tuples in the same table.
- A tuple can also have foreign keys, which are attributes that reference the primary keys of other tables to establish relationships between them.
- A tuple can have null values, which indicate the absence of information or unknown values for some attributes.
- A tuple can be inserted, updated, deleted, or queried using SQL commands or other database operations.
- A tuple can be represented by a horizontal line with the attribute values separated by commas, or by a vertical list with the attribute names and values. For example, the tuple (Alice, 25, Female, Engineer) can be written as:

| Name | Age | Gender | Occupation |
| --- | --- | --- | --- |
| Alice | 25 | Female | Engineer |

or

Name: Alice
Age: 25
Gender: Female
Occupation: Engineer



# Relations and Relational Database Schema

- A **relation** is a set of tuples that have the same attributes. A tuple is a single row of data in a table. An attribute is a column or field name of a table. A relation can also be called a table or a file.
- A **relational database** is a collection of relations that store data in a structured and organized way. A relational database follows the principles of the relational data model, which is based on mathematical concepts of sets and relations.
- A **relational database schema** is a blueprint or plan that a database uses to store and organize information. It describes the structure of the data within the database and shows the connections between different tables, which contain related data.
- A **relation schema** is a part of the relational database schema that defines the name, attributes, and constraints of a relation. A relation schema can be written as R(A1, A2, ..., An), where R is the name of the relation and A1, A2, ..., An are the attributes of the relation.
- A **database schema** is the collection of relation schemas for a whole database. A database schema is a collection of metadata, which means data about data. A database schema describes the structure and constraints of data representing in a particular domain.
- A **database instance** is a snapshot of the data in a database at a given point in time. A database instance can change as the data in the database is inserted, updated, deleted, or queried. A database instance is also called a database state.

Some benefits of using a relational database schema are:

- It helps to ensure data integrity and consistency by enforcing rules and constraints on the data.
- It helps to avoid data redundancy and duplication by eliminating unnecessary or repeated data.
- It helps to improve data security and access control by defining user privileges and permissions on the data.
- It helps to facilitate data manipulation and analysis by providing a logical and clear view of the data.
- It helps to simplify data maintenance and management by allowing changes to the schema without affecting the data.

Some uses of a relational database schema are:

- It is used to design and implement a relational database system that meets the requirements and specifications of a particular application or domain.
- It is used to document and communicate the structure and meaning of the data in a relational database to other users or developers.
- It is used to query and retrieve data from a relational database using a standard language such as SQL (Structured Query Language).
- It is used to optimize and enhance the performance and efficiency of a relational database by applying techniques such as normalization, indexing, and partitioning.



# Integrity Constraints for the Notes of the Unit 3 - Relational Database Concepts

- Integrity constraints are the set of rules that can be used to maintain the data integrity during an insert, delete and update operations into a table.
- Data integrity refers to the overall validity, integrity, and consistency of the data present in the database table.
- There are four main types of integrity constraints in relational database:
  - Domain constraints
  - Key constraints
  - Entity integrity constraints
  - Referential integrity constraints
- Domain constraints specify the valid values for a column or an attribute. They can be defined by data type, range, format, or a set of permissible values .
- Key constraints specify that a column or a combination of columns can uniquely identify a row in a table. They can be primary key or candidate key .
- Entity integrity constraints ensure that every table has a primary key and that the primary key has no null values.
- Referential integrity constraints ensure that the foreign key values in one table match the primary key values in another table. They also define the actions to be taken when the primary key or the foreign key is modified or deleted .
- Integrity constraints can be enforced by the database management system (DBMS) or by the application program. The DBMS can check the constraints before performing any operation on the tables and reject any operation that violates the constraints .
- Integrity constraints can help to prevent data anomalies, such as insertion, deletion, and update anomalies, that can compromise the quality and consistency of the data .



# Entity Integrity in Relational Database

- Entity integrity is a form of data integrity that ensures that each record in a table has a unique and non-null identifier, called the primary key .
- The primary key is a column or a combination of columns that can uniquely identify a row in a table .
- Entity integrity prevents duplicate records, missing values, and inconsistent data in a table .
- Entity integrity is one of the three types of integrity constraints in the relational data model, along with referential integrity and domain integrity.
- Entity integrity can be enforced by the database system by checking the primary key values before inserting or updating data in a table .
- Entity integrity is important for maintaining the accuracy, consistency, and reliability of the data in a relational database.



# Referential Integrity

- Referential integrity is a property of relational database that ensures the consistency and validity of the data across different tables.
- Referential integrity is enforced by using foreign keys, which are columns in one table that reference the primary key of another table.
- A foreign key can either have a matching value in the referenced table, or be null (meaning no value).
- Referential integrity rules prevent the following actions that would violate the consistency of the data:
  - Inserting a record in a table with a foreign key that does not exist in the referenced table.
  - Updating a record in a table with a foreign key that would make it not match any value in the referenced table.
  - Deleting a record in a table that is referenced by a foreign key in another table, unless the foreign key is set to null or cascaded.
- Referential integrity can be enforced by the database system using constraints, triggers, or stored procedures.
- Referential integrity can also be implemented by the application logic using transactions, validations, or error handling.



# Keys Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple or a row in a relation or a table.
- A constraint is a rule or a condition that is imposed on the data in a relation or a table to ensure its validity and integrity.
- There are different types of keys and constraints in a relational database, such as:

  - **Primary key**: A primary key is a key that uniquely identifies each tuple or row in a relation or table. A primary key cannot have null values or duplicate values. A relation or table can have only one primary key. For example, in a Student relation, the student_id attribute can be a primary key.

  - **Foreign key**: A foreign key is a key that refers to the primary key of another relation or table. A foreign key establishes a relationship between two relations or tables. A foreign key can have null values or duplicate values, but it must match the value of the primary key in the referenced relation or table, or be null. For example, in a Course relation, the student_id attribute can be a foreign key that references the Student relation.

  - **Candidate key**: A candidate key is a key that can uniquely identify each tuple or row in a relation or table. A candidate key can be a single attribute or a combination of attributes. A relation or table can have more than one candidate key, but only one of them can be chosen as the primary key. For example, in a Student relation, the student_id and the email attributes can be candidate keys, but only one of them can be the primary key.

  - **Alternate key**: An alternate key is a candidate key that is not chosen as the primary key. An alternate key can be used as a backup or a secondary key to identify the tuples or rows in a relation or table. For example, in a Student relation, if the student_id attribute is chosen as the primary key, then the email attribute can be an alternate key.

  - **Composite key**: A composite key is a key that consists of two or more attributes. A composite key can be a primary key, a foreign key, a candidate key, or an alternate key. A composite key can uniquely identify the tuples or rows in a relation or table based on the combination of values of the attributes. For example, in a Course relation, the course_id and the semester attributes can form a composite key.

  - **Super key**: A super key is a key that consists of one or more attributes that can uniquely identify each tuple or row in a relation or table. A super key can be a single attribute or a combination of attributes. A super key can have additional attributes that are not necessary for the uniqueness of the tuples or rows. A super key can be a primary key, a foreign key, a candidate key, an alternate key, or a composite key. For example, in a Student relation, the student_id, the email, and the name attributes can form a super key.

  - **Unique key**: A unique key is a key that can uniquely identify each tuple or row in a relation or table, but it is not a primary key. A unique key can have null values, but it cannot have duplicate values. A relation or table can have more than one unique key. A unique key can be a single attribute or a combination of attributes. A unique key can be a foreign key, a candidate key, an alternate key, or a composite key. For example, in a Student relation, the email attribute can be a unique key.



# Domain Constraints for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Domain constraints are a type of user-defined column that helps us to arrange the data we have entered according to the datatype.
- A domain integrity constraint is a set of rules that restricts the kind of attributes or values a column or relation can hold in the database table.
- The domain means a range of values. In mathematics, the concept of Domain means the allowed values for a function. Similarly, in DBMS, the Domain Constraint specifies the domain or set of values.
- There are two types of constraints that come under domain constraint and they are:
  - Domain Constraints – Not Null: Null values are the values that are unassigned or we can also say that which are unknown. The not null constraint is used to specify that the column must not accept null values.
  - Domain Constraints – Check: It defines a condition that each row must satisfy which means it checks the validity of the data entered into a column.
- Domain constraints can be defined using the CREATE TABLE or ALTER TABLE statements in SQL.
- Domain constraints are a part of the integrity constraints in DBMS, which are rules that ensure the accuracy and consistency of the data in the database.
- Domain constraints are important because they prevent the insertion of invalid data into the database, which can lead to errors and inconsistencies. They also help to maintain the data quality and integrity.



# Relational Algebra and Relational Calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a procedural language that specifies how to construct a new relation from one or more existing relations in the database.
- Relational calculus is a declarative language that specifies what data to retrieve from the database without specifying how to do it.
- Both languages are equivalent in expressive power, meaning that any query that can be expressed in one language can also be expressed in the other language. This is known as Codd's theorem.
- Relational algebra and relational calculus are the basis for the SQL language, which is the most widely used language for querying and manipulating relational databases.

## Relational Algebra

- Relational algebra consists of a set of basic operations that can be applied to relations, such as selection, projection, union, set difference, Cartesian product, rename, join, division, and assignment.
- Selection (σ) is an operation that selects a subset of tuples from a relation that satisfy a given condition.
- Projection (π) is an operation that extracts a subset of attributes from a relation and eliminates duplicates.
- Union (∪) is an operation that combines two relations with the same set of attributes and eliminates duplicates.
- Set difference (-) is an operation that returns the tuples that are in one relation but not in another relation with the same set of attributes.
- Cartesian product (×) is an operation that combines two relations by forming all possible pairs of tuples from the two relations.
- Rename (ρ) is an operation that changes the name of a relation or its attributes.
- Join (⋈) is an operation that combines two relations by matching tuples based on a join condition.
- Division (÷) is an operation that returns the tuples from one relation that are associated with all tuples from another relation.
- Assignment (←) is an operation that assigns a relation to a temporary relation variable.

## Relational Calculus

- Relational calculus consists of two variants: tuple relational calculus and domain relational calculus.
- Tuple relational calculus (TRC) is a language that uses variables that range over tuples of a relation and a formula that defines the conditions for selecting tuples.
- Domain relational calculus (DRC) is a language that uses variables that range over the domains of attributes of a relation and a formula that defines the conditions for selecting values.
- Both TRC and DRC use quantifiers (∀ and ∃) to express universal and existential conditions, and logical connectives (∧, ∨, ¬) to combine conditions.
- A query in TRC or DRC is a formula that evaluates to true for the tuples or values that should be in the result of the query.



# Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases .
- Relational calculus is a declarative language, which means it specifies what data to retrieve, not how to retrieve it .
- Tuple and domain calculus differ in the way they use variables to represent data from a relation.

## Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables range over tuples, which are ordered sets of attribute values that represent a single row or record in a database table .
- A tuple variable (t) goes to each row of the table and checks if a predicate (a logical condition) is true or false for the given row .
- Depending on the predicate, it returns the whole row or part of the row that satisfies the condition .
- The syntax of tuple relational calculus is:

  `{t | P(t)}`

  where t is a tuple variable and P(t) is a predicate involving t .

- For example, the query to find the names of all employees who work in the department 10 is:

  `{t.name | EMPLOYEE(t) AND t.deptno = 10}`

  where EMPLOYEE(t) is a predicate that checks if t is a tuple from the EMPLOYEE relation .

## Domain Relational Calculus (DRC)

- In domain relational calculus, variables range over domain elements, which are field values of a relation .
- A domain variable (x) goes to each value of an attribute and checks if a predicate is true or false for the given value .
- Depending on the predicate, it returns the value or a combination of values that satisfies the condition .
- The syntax of domain relational calculus is:

  `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`

  where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a predicate involving them .

- For example, the query to find the names of all employees who work in the department 10 is:

  `{<x> | EMPLOYEE(x, y, z, w) AND w = 10}`

  where EMPLOYEE(x, y, z, w) is a predicate that checks if x, y, z, w are values of the attributes name, empno, job, deptno of the EMPLOYEE relation .

## Comparison of TRC and DRC

- Both TRC and DRC are equivalent in expressive power, which means they can express the same queries .
- However, TRC is more intuitive and natural for humans, while DRC is more concise and abstract .
- TRC is closer to the relational algebra, which is a procedural query language, while DRC is closer to the first-order logic, which is a formal system of reasoning .



# Basic Operations – Selection and Projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database.
- Selection operation targets records (rows) or specific entities in a relational database. It filters the rows that satisfy a given condition or predicate.
- Projection operation targets attributes (columns) or specific properties in a relational database. It selects the columns that are specified in the query.
- In SQL, the SELECT statement combines both selection and projection operations in a single statement. The WHERE clause is used for selection and the column names are used for projection.
- Examples of selection and projection operations in SQL:

  - Select all the rows and columns from a table named Employees:

    ```sql
    SELECT * FROM Employees;
    ```

  - Select only the rows where the salary is greater than 5000 from a table named Employees:

    ```sql
    SELECT * FROM Employees WHERE salary > 5000;
    ```

  - Select only the columns name and department from a table named Employees:

    ```sql
    SELECT name, department FROM Employees;
    ```

  - Select only the rows where the department is 'Sales' and only the columns name and salary from a table named Employees:

    ```sql
    SELECT name, salary FROM Employees WHERE department = 'Sales';
    ```



# Set-theoretic operations in relational database

- Set-theoretic operations are based on the mathematical concept of sets, which are collections of distinct elements.
- Set-theoretic operations can be applied to relations in a relational database to combine or compare them in various ways.
- The main set-theoretic operations are union, intersection, difference, and Cartesian product.
- To apply set-theoretic operations to relations, the relations must be **union-compatible**, which means they have the same number and type of attributes, and the corresponding attributes have the same domain.
- The result of a set-theoretic operation is also a relation, which may or may not be stored in the database.

## Union

- The union operation, denoted by ∪, returns a relation that contains all the tuples that are either in the first relation or in the second relation, or in both.
- The union operation eliminates any duplicate tuples from the result.
- The union operation is **commutative**, which means that R ∪ S is equivalent to S ∪ R.
- The union operation is also **associative**, which means that (R ∪ S) ∪ T is equivalent to R ∪ (S ∪ T).
- The union operation can be implemented in SQL using the **UNION** keyword.

## Intersection

- The intersection operation, denoted by ∩, returns a relation that contains only the tuples that are common to both the first and the second relation.
- The intersection operation does not produce any duplicate tuples, since they are already eliminated by the union-compatibility condition.
- The intersection operation is **commutative**, which means that R ∩ S is equivalent to S ∩ R.
- The intersection operation is also **associative**, which means that (R ∩ S) ∩ T is equivalent to R ∩ (S ∩ T).
- The intersection operation can be implemented in SQL using the **INTERSECT** keyword.

## Difference

- The difference operation, denoted by -, returns a relation that contains only the tuples that are in the first relation but not in the second relation.
- The difference operation does not produce any duplicate tuples, since they are already eliminated by the union-compatibility condition.
- The difference operation is **not commutative**, which means that R - S is not equivalent to S - R.
- The difference operation is **not associative**, which means that (R - S) - T is not equivalent to R - (S - T).
- The difference operation can be implemented in SQL using the **EXCEPT** or **MINUS** keyword, depending on the database system.

## Cartesian product

- The Cartesian product operation, denoted by ×, returns a relation that contains all possible combinations of tuples from the first and the second relation.
- The Cartesian product operation does not require the relations to be union-compatible, since it combines the attributes of both relations.
- The Cartesian product operation may produce duplicate tuples, if the relations have common attributes with the same values.
- The Cartesian product operation is **commutative**, which means that R × S is equivalent to S × R.
- The Cartesian product operation is also **associative**, which means that (R × S) × T is equivalent to R × (S × T).
- The Cartesian product operation can be implemented in SQL using the **CROSS JOIN** keyword.



# Join Operations

Join operations are used to combine data from two or more tables in a relational database based on some common attribute or condition. Join operations are essential for querying data across multiple tables and for implementing relationships between entities.

## Types of Join Operations

There are different types of join operations that can be performed in SQL, depending on the desired result. Some of the most common types are:

- **Inner join**: This type of join returns only the rows that match the join condition in both tables. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, an inner join will return only the rows where the same `CustomerID` exists in both tables.
- **Left outer join**: This type of join returns all the rows from the left table, and the matching rows from the right table. If there is no match for a row in the left table, the columns from the right table will be null. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, a left outer join will return all the rows from the `Customers` table, and the corresponding rows from the `Orders` table if they exist, or null values otherwise.
- **Right outer join**: This type of join returns all the rows from the right table, and the matching rows from the left table. If there is no match for a row in the right table, the columns from the left table will be null. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, a right outer join will return all the rows from the `Orders` table, and the corresponding rows from the `Customers` table if they exist, or null values otherwise.
- **Full outer join**: This type of join returns all the rows from both tables, and the matching rows from the other table. If there is no match for a row in either table, the columns from the other table will be null. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, a full outer join will return all the rows from both tables, and the corresponding rows from the other table if they exist, or null values otherwise.
- **Cross join**: This type of join returns the Cartesian product of the two tables, which means every possible combination of rows from both tables. For example, if we want to join the tables `Customers` and `Orders` without any condition, a cross join will return every row from the `Customers` table paired with every row from the `Orders` table.

## Syntax of Join Operations

The general syntax of join operations in SQL is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

The `JOIN` keyword can be replaced by the specific type of join, such as `INNER JOIN`, `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`, `FULL OUTER JOIN`, or `CROSS JOIN`. The `ON` clause specifies the join condition, which is usually a comparison of columns from both tables using a logical operator, such as `=` or `<>`. The `SELECT` clause specifies the columns to be retrieved from the joined tables.

For example, the following query performs an inner join between the tables `Customers` and `Orders` based on the `CustomerID` column, and returns the `CustomerName`, `OrderID`, and `OrderDate` columns:

```sql
SELECT Customers.CustomerName, Orders.OrderID, Orders.OrderDate
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;
```

## References

: Joins (SQL Server) - SQL Server | Microsoft Learn. https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver16
: SQL JOIN | How to link Relational Databases - IONOS. https://www.ionos.com/digitalguide/hosting/technical-matters/sql-join/
: JOIN OPERATOR - University of Delaware. https://www1.udel.edu/evelyn/SQL-Class2/SQLclass2_Join.html
: How To Use Joins in SQL | DigitalOcean. https://www.digitalocean.com/community/tutorials/how-to-use-joins-in-sql



## Unit 4 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that organizes the data into tables and columns to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design by creating atomic elements (i.e., elements that cannot be broken down into smaller parts) and representing the relationships among them.
- Normalization is based on a series of normal forms (NF) that define the criteria for a well-designed database. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values and no repeating groups of attributes.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies.
- The process of normalization involves decomposing a table into smaller tables that satisfy a higher normal form, while preserving the information and relationships in the original table.
- The benefits of normalization include:
  - Eliminating data anomalies, such as insertion, deletion, and update anomalies, that can cause data inconsistency and corruption.
  - Reducing data redundancy and storage space, by avoiding duplicate or unnecessary data.
  - Improving data integrity and quality, by enforcing data constraints and rules at the table level.
  - Enhancing data security and access control, by restricting the access to specific tables and columns based on user roles and privileges.
  - Facilitating data manipulation and querying, by simplifying the structure and logic of the database.
- The drawbacks of normalization include:
  - Increasing the number of tables and joins, which can affect the performance and complexity of the database.
  - Losing some information or relationships, if the normalization is not done properly or completely.
  - Requiring more maintenance and administration, as the database grows and changes over time.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on functional dependencies for the unit 4 of the subject of basics of database management system:

# Functional dependencies

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database .
- A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X is called the determinant and Y is called the dependent .
- A functional dependency X -> Y means that for every valid instance of X, that value of X uniquely determines the value of Y.
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity.

## Types of functional dependencies

- There are four primary types of functional dependencies: trivial, non-trivial, multivalued and transitive .

### Trivial functional dependency

- A trivial functional dependency is a functional dependency where the dependent is always a subset of the determinant.
- For example, A -> A or A -> AB are trivial functional dependencies, because A is a subset of A and AB.
- A trivial functional dependency does not impose any constraint on the relation, because it is always satisfied by any relation.

### Non-trivial functional dependency

- A non-trivial functional dependency is a functional dependency where the dependent is strictly not a subset of the determinant.
- For example, A -> B or AB -> C are non-trivial functional dependencies, because B and C are not subsets of A and AB respectively.
- A non-trivial functional dependency imposes a constraint on the relation, because it restricts the possible values of the dependent based on the value of the determinant.

### Multivalued functional dependency

- A multivalued functional dependency is a functional dependency where the determinant determines more than one attribute, and the attributes are independent of each other.
- For example, A -> BC is a multivalued functional dependency, because A determines both B and C, and B and C are independent of each other.
- A multivalued functional dependency implies that for a given value of A, there can be multiple values of B and C, and the values of B and C do not depend on each other.

### Transitive functional dependency

- A transitive functional dependency is a functional dependency where the determinant determines another attribute, which in turn determines another attribute.
- For example, A -> B and B -> C are transitive functional dependencies, because A determines B, and B determines C.
- A transitive functional dependency implies that the value of C depends on the value of A indirectly, through the value of B.




# Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Normal forms are a set of rules or guidelines for designing relational databases in a way that reduces data redundancy and improves data integrity  .
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes in a relation such that the values of one set determine the values of the other set .
- There are several normal forms, each with a higher degree of normalization than the previous one. The most common normal forms are: first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF)   .
- A relation is said to be in a certain normal form if it satisfies the conditions or requirements of that normal form. A relation can be converted from a lower normal form to a higher normal form by applying certain normalization techniques  .
- The main benefits of normalization are: avoiding data anomalies, such as insertion, deletion, and update anomalies; ensuring data consistency and accuracy; and facilitating efficient data retrieval and manipulation  .
- The main drawbacks of normalization are: increased complexity and overhead of database design and maintenance; possible loss of performance due to more joins and queries; and possible loss of information due to decomposition of relations .

## First Normal Form (1NF)

- A relation is in 1NF if it does not contain any composite or multi-valued attributes, i.e., each attribute has a single atomic value .
- To convert a relation to 1NF, we need to remove any composite or multi-valued attributes and create separate relations for them, with appropriate foreign keys to link them to the original relation .
- For example, consider the following relation that contains a composite attribute (Address) and a multi-valued attribute (Phone):

| Student_ID | Name | Address | Phone |
| --- | --- | --- | --- |
| 101 | Alice | 123 Main St, Seattle, WA | 555-1111, 555-2222 |
| 102 | Bob | 456 Elm St, Portland, OR | 555-3333 |
| 103 | Carol | 789 Pine St, San Francisco, CA | 555-4444, 555-5555 |

- To convert this relation to 1NF, we need to split the Address attribute into its components (Street, City, State) and create a separate relation for Phone, with Student_ID as a foreign key:

| Student_ID | Name | Street | City | State |
| --- | --- | --- | --- | --- |
| 101 | Alice | 123 Main St | Seattle | WA |
| 102 | Bob | 456 Elm St | Portland | OR |
| 103 | Carol | 789 Pine St | San Francisco | CA |

| Student_ID | Phone |
| --- | --- |
| 101 | 555-1111 |
| 101 | 555-2222 |
| 102 | 555-3333 |
| 103 | 555-4444 |
| 103 | 555-5555 |

## Second Normal Form (2NF)

- A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there is no partial dependency .
- To convert a relation to 2NF, we need to identify any partial dependencies and remove them by creating separate relations for them, with appropriate foreign keys to link them to the original relation .
- For example, consider the following relation that contains a composite primary key (Student_ID, Course_ID) and a partial dependency (Course_Name -> Course_Credit):

| Student_ID | Course_ID | Course_Name | Course_Credit | Grade |
| --- | --- | --- | --- | --- |
| 101 | CS101 | Introduction to Computer Science | 3 | A |
| 101 | CS102 | Data Structures and Algorithms | 4 | B |
| 102 | CS101 | Introduction to Computer Science | 3 |



# Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database management system (DBMS) .
- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies .
- Normalization rules divide larger tables into smaller tables and link them using relationships .
- Normalization is based on the concept of normal forms, which are sets of conditions that a table must satisfy to be considered well-structured .
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if every attribute is atomic, meaning it cannot be further subdivided, and every row has a unique identifier .
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be determined by a subset of the key .
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be determined by another non-key attribute .
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies .
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, meaning there are no attributes that depend on a set of values rather than a single value .
- To perform the normalization process, you start with a rough idea of the data you want to store, and apply certain rules to it in order to get it to a more efficient form .
- The benefits of normalization are:
  - It reduces data duplication and storage space .
  - It improves data integrity and consistency .
  - It simplifies data manipulation and querying .
  - It facilitates data security and access control .
- The drawbacks of normalization are:
  - It may increase the number of tables and joins, which can affect performance .
  - It may require denormalization to optimize some queries or operations .
  - It may not capture all the semantics and constraints of the real-world data .



# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, insertion, update, and deletion of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Flexibility: The database should be able to accommodate changing data requirements and business needs, without requiring major modifications or redesigns.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity and organization of data.
- Normalization also helps to avoid data anomalies, such as insertion, update, and deletion anomalies, that may arise due to redundant or dependent data.
- Normalization is based on a set of rules or normal forms, that define the criteria for a well-structured database schema. The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic (cannot be further subdivided).
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key (i.e., the non-key attribute depends on the whole key and not on a part of it).
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e., the non-key attribute depends only on the key and not on another non-key attribute).
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant (a set of attributes that determines another attribute) is a candidate key (a minimal set of attributes that uniquely identifies a tuple).
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies (a dependency where one attribute determines a set of values for another attribute).
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (a dependency where a table can be decomposed into two or more tables and then reconstructed by joining them without losing any information).

## Example of Database Normalization
- Consider the following table that stores the information about the courses offered by a college, the instructors who teach them, and the students who enroll in them.

| Course_ID | Course_Name | Instructor_ID | Instructor_Name | Student_ID | Student_Name |
|-----------|-------------|---------------|-----------------|------------|--------------|
| CSE101    | Programming | I001          | Alice           | S001       | Bob          |
| CSE101    | Programming | I001          | Alice           | S002       | Carol        |
| CSE101    | Programming | I001          | Alice           | S003       | Dave         |
| CSE102    | Database    | I002          | Eve             | S002       | Carol        |
| CSE102    | Database    | I002          | Eve             | S004       | Frank        |
| CSE103    | Web Design  | I003          | Grace           | S001       | Bob          |
| CSE103    | Web Design  | I003          | Grace           | S003       | Dave         |
| CSE103    | Web Design  | I003          | Grace           | S005       | Helen        |

- This table is not in 1NF, because it has repeating groups of attributes (Course_Name, Instructor_ID, Instructor_Name, Student_ID, Student_Name) for each Course_ID. To convert it to 1NF, we need to remove the repeating groups and create a separate table for each group, with a foreign key referencing the Course_ID. For example:

| Course_ID | Course



# Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two or more non-prime attributes that are indirectly determined by the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name.
  - The primary key is (Student ID, Course ID).
  - The non-prime attributes are Student Name, Course Name, Instructor ID, Instructor Name.
  - There is a transitive dependency between Course Name and Instructor Name, since they are both functionally dependent on Course ID, which is part of the primary key.
  - To convert this table to 3NF, we need to remove the transitive dependency by creating a separate table for Course ID, Course Name, and Instructor ID, and referencing it from the original table using a foreign key.
- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the Third Normal Form.
  - The Third Normal Form ensures functional dependency preserving and lossless decomposition, which means that the original data can be reconstructed from the normalized tables without any loss or inconsistency.
  - The Third Normal Form reduces the storage space and improves the performance of the database queries.



# BCNF

BCNF stands for Boyce-Codd Normal Form. It is a form of database normalization that ensures that there are no anomalies or redundancies in the data. BCNF is a stricter version of 3NF (Third Normal Form), which requires that every non-prime attribute is fully functionally dependent on the primary key, and that there are no transitive dependencies.

A table is in BCNF if and only if for every functional dependency X -> Y, X is a superkey of the table. A superkey is a set of attributes that uniquely identifies a tuple in the table. A candidate key is a minimal superkey, meaning that no subset of the candidate key is a superkey.

To check if a table is in BCNF, we need to find all the functional dependencies and candidate keys in the table, and then verify that the left-hand side of every functional dependency is a superkey. If not, we need to decompose the table into smaller tables that satisfy the BCNF condition.

## Example

Consider the following table that stores information about students, courses, and instructors.

| Student ID | Course ID | Instructor ID | Instructor Name | Grade |
|------------|-----------|---------------|-----------------|-------|
| S1         | C1        | I1            | Alice           | A     |
| S1         | C2        | I2            | Bob             | B     |
| S2         | C1        | I1            | Alice           | C     |
| S2         | C3        | I3            | Charlie         | A     |

The functional dependencies in this table are:

- Student ID, Course ID -> Instructor ID, Grade
- Instructor ID -> Instructor Name

The candidate keys are:

- Student ID, Course ID
- Student ID, Instructor ID
- Course ID, Instructor ID

This table is not in BCNF, because the functional dependency Instructor ID -> Instructor Name violates the condition. The left-hand side, Instructor ID, is not a superkey, because it is not unique in the table. This dependency also causes redundancy, because the same instructor name is repeated for different courses.

To convert this table into BCNF, we need to decompose it into two tables:

| Student ID | Course ID | Instructor ID | Grade |
|------------|-----------|---------------|-------|
| S1         | C1        | I1            | A     |
| S1         | C2        | I2            | B     |
| S2         | C1        | I1            | C     |
| S2         | C3        | I3            | A     |

| Instructor ID | Instructor Name |
|---------------|-----------------|
| I1            | Alice           |
| I2            | Bob             |
| I3            | Charlie         |

The first table has the same candidate keys as before, and the only functional dependency is Student ID, Course ID -> Instructor ID, Grade, which satisfies the BCNF condition. The second table has Instructor ID as the primary key, and the only functional dependency is Instructor ID -> Instructor Name, which also satisfies the BCNF condition. The redundancy is eliminated, and the tables are in BCNF.



# Inclusion Dependency in DBMS

- Inclusion dependency is a statement in which some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential constraints, such as foreign keys  .
- Inclusion dependency can be used to guide the design of the database, but it usually has little influence on how the database is actually designed .
- Inclusion dependency can be represented as R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ means "is contained in" .
- Inclusion dependency holds for a database if every tuple that is a member of the relation R is also a member of the relation S.
- Inclusion dependency can be checked by performing a natural join of R and S on the corresponding columns and comparing the result with R.
- Inclusion dependency can be violated if a tuple is inserted into R that does not have a matching tuple in S, or if a tuple is deleted from S that has a matching tuple in R.
- Inclusion dependency can be enforced by using triggers, assertions, or cascading updates and deletes.



# Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of R1, R2, ... gives back the original relation R. 
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data.  
- Lossless join decomposition is also known as non-additive join decomposition. 
- A decomposition of R into R1 and R2 is lossless if at least one of the following functional dependencies holds in the closure of the set of functional dependencies F of R:  
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- A decomposition of R into R1, R2, ... Rn is lossless if there exists a sequence of binary lossless decompositions from R to R1, R2, ... Rn. 
- A decomposition of R is lossless if and only if the common attributes of any two relations in the decomposition form a superkey for at least one of the relations. 
- A decomposition of R is lossless if and only if for every legal instance r of R, the projection of r on R1, R2, ... Rn is a join dependency. 

: Lossless join decomposition - Wikipedia
: What is lossless join decomposition in DBMS - tutorialspoint.com
: Lossless Decomposition in DBMS - GeeksforGeeks
: relational database - Lossless Join Property - Stack Overflow



# Normalization using FD

- Normalization is a process of organizing the data in a database to avoid data redundancy, insertion anomaly, update anomaly and deletion anomaly.
- Normalization is done by applying some rules or constraints called normal forms on the database schema.
- Normal forms are based on the concept of functional dependencies (FDs), which capture the relationships between the attributes of a relation.
- A functional dependency X -> Y means that the value of Y is determined by the value of X. In other words, if two tuples have the same value for X, they must also have the same value for Y.
- A relation is in a certain normal form if it satisfies the corresponding set of conditions or constraints based on the FDs.
- The most common normal forms are:

  - First normal form (1NF): A relation is in 1NF if it has no repeating groups or multivalued attributes. That is, each attribute must have a single atomic value.
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there is no partial dependency of any attribute on a subset of the primary key.
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there is no transitive dependency of any attribute on a non-key attribute that is functionally dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there is no dependency of any attribute on a non-key attribute that is not a candidate key.
  - Fourth normal form (4NF): A relation is in 4NF if it is in BCNF and has no multivalued dependencies. That is, there is no dependency of one set of attributes on another set of attributes that is not functionally dependent on the primary key.
  - Fifth normal form (5NF): A relation is in 5NF if it is in 4NF and has no join dependencies. That is, the relation cannot be decomposed into two or more relations that can be joined together to produce the original relation.

- To normalize a relation using FDs, we can follow these steps:

  - Identify all the FDs that hold in the relation and find the candidate keys.
  - Check if the relation is in 1NF and eliminate any repeating groups or multivalued attributes by creating new relations.
  - Check if the relation is in 2NF and eliminate any partial dependencies by creating new relations.
  - Check if the relation is in 3NF and eliminate any transitive dependencies by creating new relations.
  - Check if the relation is in BCNF and eliminate any dependencies that violate the BCNF condition by creating new relations.
  - Check if the relation is in 4NF and eliminate any multivalued dependencies by creating new relations.
  - Check if the relation is in 5NF and eliminate any join dependencies by creating new relations.



# MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for multivalued dependency, which is a type of constraint between two sets of attributes in a relation.
- A multivalued dependency occurs when a single value of one attribute is associated with multiple values of another attribute, and vice versa.
- For example, if a relation R has attributes A, B, and C, and A --> --> B means that for each value of A, there are multiple values of B, and A --> --> C means that for each value of A, there are multiple values of C, then R has a multivalued dependency A --> --> B, C.
- A multivalued dependency is a special case of a join dependency, which is a constraint that requires a relation to be equal to the join of its projections.
- A join dependency is denoted by JD(R1, R2, ..., Rn), where R is a relation and R1, R2, ..., Rn are its projections.
- A multivalued dependency is a binary join dependency, which means it involves only two projections.
- For example, A --> --> B, C is equivalent to JD(R1, R2), where R1 has attributes A and B, and R2 has attributes A and C.
- A relation is in fourth normal form (4NF) if it has no multivalued dependencies.
- 4NF is a refinement of the third normal form (3NF), which requires a relation to have no transitive dependencies.
- A transitive dependency is a functional dependency of the form A --> B and B --> C, which implies A --> C.
- A functional dependency is a constraint that for each value of one attribute, there is exactly one value of another attribute.
- For example, if a relation R has attributes A, B, and C, and A --> B and B --> C, then R has a transitive dependency A --> C.
- To achieve 4NF, a relation with multivalued dependencies should be decomposed into smaller relations that preserve the dependencies and the information.
- For example, if a relation R has attributes A, B, and C, and A --> --> B, C, then R can be decomposed into R1(A, B) and R2(A, C), which are both in 4NF.
- Normalization is the process of designing a database schema that reduces redundancy and anomalies, and ensures data integrity and consistency.
- Normalization helps to avoid problems such as update, insertion, and deletion anomalies, which can cause data inconsistency and loss.
- Normalization also helps to improve query performance and maintainability, by reducing the size and complexity of the relations.
- Normalization is based on a series of normal forms, such as 1NF, 2NF, 3NF, 4NF, and 5NF, each of which has a set of rules and criteria to check and enforce.
- The higher the normal form, the more normalized the relation is, and the less redundancy and anomalies it has.
- However, normalization also has some drawbacks, such as increased number of relations and joins, loss of semantic information, and possible performance degradation.
- Therefore, normalization should be balanced with other design considerations, such as user requirements, application needs, and system constraints.



# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its rules.
  - Ensure data integrity, consistency, and quality.
  - Support efficient and secure data access and manipulation.
  - Facilitate data maintenance and evolution.
  - Minimize data redundancy and anomalies.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization helps in improving the overall design of the database, making it easier to maintain, query, and update.
- Normalization also makes the database more flexible and adaptable to changing business needs.
- Normalization is based on a set of rules or forms, each of which is a refinement of the previous one. The most common forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values and no repeating groups of attributes.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies.

## Database Design and Normalization Example
- Suppose we have a table called Student_Course that stores the information of students and the courses they enroll in:

| Student_ID | Student_Name | Course_ID | Course_Name | Instructor_ID | Instructor_Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| 101        | Alice        | CS101     | Programming | 1001          | Bob             |
| 101        | Alice        | CS102     | Database    | 1002          | Carol           |
| 102        | David        | CS101     | Programming | 1001          | Bob             |
| 103        | Eve          | CS102     | Database    | 1002          | Carol           |

- This table is not in 1NF, because it has repeating groups of attributes (Course_ID, Course_Name, Instructor_ID, Instructor_Name) for each student.
- To convert it to 1NF, we can create a new table called Enrollment that stores the relationship between students and courses, and remove the repeating attributes from the Student_Course table:

| Student_ID | Student_Name |
|------------|--------------|
| 101        | Alice        |
| 102        | David        |
| 103        | Eve          |

| Course_ID | Course_Name | Instructor_ID | Instructor_Name |
|-----------|-------------|---------------|-----------------|
| CS101     | Programming | 1001          | Bob             |
| CS102     | Database    | 1002          | Carol           |

| Student_ID | Course_ID |
|------------|-----------|
| 101        | CS101     |
| 101        | CS102     |
| 102        | CS101     |
| 103        | CS102     |

- The Student_Course table is now in 1NF, but not in 2NF, because the non-key attributes (Student_Name, Course_Name, Instructor_Name) are not fully dependent on the primary key (Student_ID, Course_ID), but only on part of it.
- To convert it to 2NF, we can create separate tables for Student, Course, and Instructor, and use foreign keys to reference them in the Enrollment table:

| Student_ID | Student_Name |
|------------|--------------|
| 101        | Alice        |
| 102        |



# Alternative Approaches to Database Design

Database design is the process of creating a logical and physical structure for storing and manipulating data. Database design can have a significant impact on the performance, functionality, and maintainability of a database system. There are different approaches and techniques for database design, depending on the requirements and preferences of the database developers and users.

Some of the alternative approaches to database design are:

- **Domain Model from Use Cases**: This is an agile approach that focuses on identifying the entities and relationships from the user stories and scenarios. The domain model is a conceptual representation of the problem domain, and it can be used as a basis for creating the database schema. The advantage of this approach is that it aligns the database design with the user needs and expectations, and it allows for iterative and incremental development. The disadvantage is that it may not capture all the details and constraints of the data, and it may require frequent changes as the user requirements evolve.

- **Normalization**: This is a technique that aims to reduce data redundancy and dependency by organizing the data into tables with minimal attributes and clear relationships. Normalization involves applying a series of rules or normal forms to the data, such as eliminating repeating groups, partial dependencies, and transitive dependencies. The advantage of normalization is that it improves data integrity, consistency, and efficiency. The disadvantage is that it may result in a large number of tables and joins, which can affect the performance and complexity of the database.

- **NoSQL Databases**: This is a category of database systems that do not follow the relational model and do not use SQL as the query language. NoSQL databases are designed to handle large and unstructured data sets, such as documents, graphs, key-value pairs, and columns. NoSQL databases offer more flexibility, scalability, and performance than relational databases, especially for big data and web applications. The disadvantage is that they may not support ACID (atomicity, consistency, isolation, durability) properties, which guarantee the reliability and correctness of the data.

- **Data Visualization Tools**: These are tools that enable users to create and explore data visualizations, such as charts, graphs, maps, and dashboards. Data visualization tools can help users to understand and communicate the patterns, trends, and insights from the data. Some of the data visualization tools that can be used for database design are:

  - **Office Reports**: This is a tool that integrates with Microsoft Office and allows users to create data visualizations from Excel, PowerPoint, and Word. Users can import data from various sources, such as databases, CSV files, and web services, and create charts, tables, and infographics.

  - **Second Prism**: This is a tool that allows users to create interactive data visualizations from their mobile devices. Users can upload data from various sources, such as Google Sheets, Dropbox, and email, and create charts, maps, and gauges. Users can also share and collaborate on their data visualizations with others.

  - **Databoard**: This is a tool that allows users to create and publish data visualizations on the web. Users can connect to various data sources, such as Google Analytics, Facebook, and Twitter, and create charts, tables, and widgets. Users can also customize the look and feel of their data visualizations and embed them on their websites or blogs.

  - **DataMarket**: This is a tool that allows users to find, explore, and visualize data from various sources, such as government, business, and social media. Users can browse and search for data sets, and create charts, maps, and tables. Users can also download and export the data and the visualizations.

  - **Q Research Software**: This is a tool that allows users to analyze and visualize data from surveys, market research, and customer feedback. Users can import data from various sources, such as Excel, SPSS, and SurveyMonkey, and create charts, tables, and dashboards. Users can also apply statistical methods, such as regression, cluster analysis, and factor analysis, to the data.



## Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several keywords, clauses, operators, and functions that can be combined to form statements.
- SQL statements can be categorized into four types: data definition language (DDL), data manipulation language (DML), data query language (DQL), and data control language (DCL).
- DDL statements are used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, or constraints.
- DML statements are used to insert, update, delete, or merge data in the database tables or views.
- DQL statements are used to retrieve data from the database tables or views, using various filtering, sorting, grouping, and aggregation options.
- DCL statements are used to grant or revoke permissions and roles to users or groups, to control the access and security of the database.
- SQL statements are executed by a database management system (DBMS), which interprets and processes the statements, and returns the results or errors.
- SQL is a declarative language, which means that it specifies what data to retrieve or manipulate, rather than how to do it. The DBMS decides the best way to execute the statements, using an optimizer and a query plan.
- SQL is a case-insensitive language, which means that the keywords, clauses, operators, and functions can be written in any combination of upper or lower case letters. However, some DBMS may have case-sensitive rules for identifiers, such as table names, column names, or aliases.
- SQL follows a set of syntax and semantic rules, which must be followed to write valid and correct statements. Some of these rules are:

  - Every SQL statement must end with a semicolon (;).
  - Every SQL statement must have at least one keyword, such as SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, GRANT, or REVOKE.
  - Every SQL statement must follow the order of clauses, such as SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT.
  - Every SQL statement must have matching parentheses, quotes, and brackets, where applicable.
  - Every SQL statement must have valid expressions, operators, and functions, where applicable.
  - Every SQL statement must have consistent data types, where applicable.
  - Every SQL statement must refer to existing tables, columns, views, indexes, or constraints, where applicable.
  - Every SQL statement must comply with the integrity and security constraints of the database, where applicable.



# Basics of SQL

SQL is a language to operate databases; it includes Database Creation, Database Deletion, Fetching Data Rows, Modifying & Deleting Data rows, etc. SQL stands for Structured Query Language which is a computer language for storing, manipulating and retrieving data stored in a relational database.

Some of the basic concepts of SQL are:

- **Relational Database Management System (RDBMS):** A RDBMS is a computer program that manages the data stored in tables, which are collections of related data entries consisting of columns and rows. A RDBMS can configure a database as well as add, delete, and display data. Some popular RDBMS programs are Oracle, PostgreSQL, MySQL, Microsoft SQL Server, and SQLite .
- **SQL Statements:** SQL statements are commands that perform various operations on the data in the database. SQL statements can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
  - **DDL:** DDL statements are used to define the structure of the database, such as creating, altering, or dropping tables, views, indexes, etc. Some examples of DDL statements are CREATE, ALTER, DROP, RENAME, etc.
  - **DML:** DML statements are used to manipulate the data in the database, such as inserting, updating, or deleting data rows. Some examples of DML statements are INSERT, UPDATE, DELETE, MERGE, etc.
  - **DQL:** DQL statements are used to query the data in the database, such as selecting, sorting, filtering, or joining data rows. Some examples of DQL statements are SELECT, ORDER BY, WHERE, JOIN, etc.
  - **DCL:** DCL statements are used to control the access and security of the database, such as granting or revoking permissions, roles, or privileges. Some examples of DCL statements are GRANT, REVOKE, DENY, etc.
- **SQL Syntax:** SQL syntax is the set of rules that govern how SQL statements are written and executed. SQL syntax is case-insensitive, meaning that keywords can be written in either upper or lower case. However, it is a common convention to write keywords in upper case and identifiers (such as table names, column names, etc.) in lower case. SQL syntax also requires that statements end with a semicolon (;) and that string values are enclosed in single quotes ('').
- **SQL Operators:** SQL operators are symbols or keywords that perform various operations on the data in the database, such as arithmetic, comparison, logical, or bitwise operations. Some examples of SQL operators are +, -, *, /, =, <, >, AND, OR, NOT, etc.
- **SQL Functions:** SQL functions are predefined or user-defined routines that perform specific tasks on the data in the database, such as calculations, conversions, aggregations, or validations. Some examples of SQL functions are SUM, AVG, COUNT, MIN, MAX, LEN, UPPER, LOWER, etc.

These are some of the basic concepts of SQL that you should know before getting started with SQL. SQL is a powerful and versatile language that allows you to interact with various types of databases and perform various tasks on the data. SQL is also easy to learn and widely used in the industry. To learn more about SQL, you can refer to the following sources:

: https://www.tutorialspoint.com/sql/sql-overview.htm
: https://www.javatpoint.com/sql-tutorial
: https://bootcamp.berkeley.edu/resources/coding/learn-sql/
: https://www.w3schools.com/sql/
: https://www.w3schools.com/sql/sql_intro.asp
: https://learnsql.com/blog/complete-beginners-guide-sql-fundamentals/



# DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that can be used to create, modify, and delete the structure of database objects, such as tables, views, indexes, etc.
- DDL commands do not affect the data stored in the database, but only the schema or the definition of the database objects.
- Some of the common DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, a view, an index, etc. For example, the following statement creates a table named `students` with four columns: `id`, `name`, `age`, and `grade`.

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

  - DROP: This command is used to delete an existing database object, such as a table, a view, an index, etc. For example, the following statement drops the `students` table from the database.

    ```sql
    DROP TABLE students;
    ```

  - RENAME: This command is used to change the name of an existing database object, such as a table, a view, an index, etc. For example, the following statement renames the `students` table to `learners`.

    ```sql
    RENAME TABLE students TO learners;
    ```

  - TRUNCATE: This command is used to delete all the data from a table, but not the table itself. It is faster than using the `DELETE` command, which is a DML command. For example, the following statement deletes all the rows from the `students` table.

    ```sql
    TRUNCATE TABLE students;
    ```

- DDL commands are normally executed by database administrators or developers, who have the necessary permissions to create and modify the database schema. They are not used by general users, who should access the database via an application.



# DML

DML stands for Data Manipulation Language. It is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views   . The main DML statements are:

- SELECT: retrieve data from one or more tables or views .
- INSERT: add new rows to a table or view   .
- UPDATE: modify existing rows in a table or view   .
- DELETE: remove existing rows from a table or view   .

DML statements can be used to store, modify, retrieve, delete and update data in a database. They can also be used with other SQL clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT, to filter, aggregate, sort, and limit the data returned by the query.

Some examples of DML statements are:

- SELECT * FROM customers; -- returns all the rows and columns from the customers table
- INSERT INTO orders (order_id, customer_id, order_date) VALUES (1, 101, '2022-01-01'); -- adds a new row to the orders table with the specified values
- UPDATE products SET price = price * 1.1 WHERE category = 'Electronics'; -- increases the price of all the products in the Electronics category by 10%
- DELETE FROM employees WHERE department = 'Sales'; -- removes all the employees who work in the Sales department

DML statements are different from DDL (Data Definition Language) statements, which are used to create, alter, or drop database objects and their structure, such as tables, views, indexes, constraints, etc. DML statements are also different from DCL (Data Control Language) statements, which are used to grant or revoke permissions and roles to users and groups in a database.



# DCL

- Data Control Language (DCL) is a sublanguage of SQL that deals with the commands used to control the access and privileges of users on the database .
- DCL is used for enforcing data security and ensuring that only authorized users can perform certain operations on the database .
- The main DCL commands in SQL are:
  - GRANT: This command is used to grant (give access to) security privileges to specific database users or roles . It can be used to allow users to perform operations such as INSERT, DELETE, SELECT, UPDATE, EXECUTE, ALTER, etc. on the database objects.
  - REVOKE: This command is used to revoke (take away) security privileges from specific database users or roles . It can be used to deny users from performing operations that they were previously granted.
  - DENY: This command is used to explicitly deny security privileges to specific database users or roles. It can be used to override any permissions that are granted or inherited by the users or roles.
- The syntax of the DCL commands is as follows :
  - GRANT privilege(s) ON object TO user(s) [WITH GRANT OPTION];
  - REVOKE [GRANT OPTION FOR] privilege(s) ON object FROM user(s) [CASCADE];
  - DENY privilege(s) ON object TO user(s);
- Some examples of the DCL commands are :
  - GRANT SELECT, UPDATE ON employees TO john, mary;
  - REVOKE UPDATE ON employees FROM john;
  - DENY DELETE ON employees TO mary;



# Advantages of SQL

SQL is a widely used language for managing and manipulating data in relational database management systems (RDBMS). Some of the advantages of using SQL are:

- **Faster and efficient query processing.** SQL can process large amounts of data in a very short time, using simple and intuitive commands. SQL also supports various functions and operators that can perform complex calculations and transformations on the data.  
- **Standardized language.** SQL is a standardized language that follows the ANSI (American National Standards Institute) and ISO (International Organization for Standardization) standards. This means that SQL is compatible with different RDBMS and platforms, and can be easily learned and used by different users. 
- **No coding skills required.** SQL does not require extensive programming skills or knowledge to retrieve data from a database. SQL uses simple English phrases and keywords, such as SELECT, FROM, WHERE, GROUP BY, etc., that can be easily understood and written by anyone. 
- **Integration with other languages and tools.** SQL can be integrated with various programming languages, such as Java, Python, C#, etc., and tools, such as Excel, Power BI, Tableau, etc., that can enhance the functionality and usability of SQL. SQL can also be embedded in applications and web pages to interact with databases. 
- **Data security and integrity.** SQL can enforce data security and integrity rules on the database, such as granting or revoking permissions, creating views, defining constraints, etc. SQL can also ensure data consistency and accuracy by using transactions, triggers, and stored procedures.



# SQL data type and literals

- SQL data types are the attributes that define the kind of value that can be stored in a column of a table or a variable in a program.
- SQL data types can be categorized into numeric, character, date and time, interval, boolean, and large object types.
- SQL literals are the constant values that can be assigned to a column or a variable, or used in expressions or conditions.
- SQL literals can be classified into numeric, character, date and time, interval, and boolean literals.
- SQL literals are written in a specific format depending on the data type they represent.

## Numeric data types and literals

- Numeric data types are used to store numbers, such as integers, decimals, fractions, and real numbers.
- Numeric data types can be further divided into exact and approximate numeric types.
- Exact numeric types are used to store numbers with a fixed precision and scale, such as integers, decimals, and numeric.
- Approximate numeric types are used to store numbers with a floating-point representation, such as floats, doubles, and reals.
- Numeric literals are written as a sequence of digits, optionally with a decimal point, a sign, and an exponent.
- Examples of numeric literals are: 42, -3.14, 6.02E23, +0.5.

## Character data types and literals

- Character data types are used to store strings of characters, such as letters, symbols, and spaces.
- Character data types can be further divided into fixed-length and variable-length character types.
- Fixed-length character types are used to store strings of a fixed size, such as char and nchar.
- Variable-length character types are used to store strings of a variable size, such as varchar, nvarchar, text, and clob.
- Character literals are written as a sequence of characters enclosed in single quotes, optionally with escape sequences for special characters.
- Examples of character literals are: 'Hello', 'SQL', 'It''s a sunny day', 'This is a newline\n'.

## Date and time data types and literals

- Date and time data types are used to store values that represent dates, times, or both.
- Date and time data types can be further divided into date, time, timestamp, and interval types.
- Date types are used to store values that represent calendar dates, such as date and year.
- Time types are used to store values that represent clock times, such as time and time with time zone.
- Timestamp types are used to store values that represent both date and time, such as timestamp and timestamp with time zone.
- Interval types are used to store values that represent a duration of time, such as interval year to month and interval day to second.
- Date and time literals are written in a specific format depending on the data type they represent, using keywords, separators, and delimiters.
- Examples of date and time literals are: DATE '2021-03-15', TIME '22:11:25', TIMESTAMP '2021-03-15 22:11:25', INTERVAL '1' YEAR, INTERVAL '10:30:00' HOUR TO SECOND.

## Boolean data types and literals

- Boolean data types are used to store values that represent logical truth values, such as boolean and bit.
- Boolean literals are written as the keywords TRUE, FALSE, or UNKNOWN, or as the digits 1, 0, or NULL for bit data types.
- Examples of boolean literals are: TRUE, FALSE, UNKNOWN, 1, 0, NULL.



# Types of SQL Commands

SQL stands for Structured Query Language and it is a standard language for storing, manipulating and retrieving data in databases. SQL commands can be grouped into five broad categories based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify or delete the database structure, such as tables, views, indexes, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new table, view, index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table called students with three columns: id, name and age.
  - ALTER: This command is used to modify the existing database structure, such as adding, deleting or renaming columns, changing data types, etc. For example, `ALTER TABLE students ADD email VARCHAR(50);` adds a new column called email to the students table.
  - DROP: This command is used to delete an existing table, view, index, etc. For example, `DROP TABLE students;` deletes the students table and all its data.
  - RENAME: This command is used to rename an existing table, view, index, etc. For example, `RENAME TABLE students TO learners;` renames the students table to learners.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table, but keeps the table structure.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete or retrieve data from the database tables. Some examples of DML commands are:

  - INSERT: This command is used to insert new data into a table. For example, `INSERT INTO students (id, name, age, email) VALUES (1, 'Alice', 20, 'alice@example.com');` inserts a new row into the students table with the specified values.
  - UPDATE: This command is used to modify existing data in a table. For example, `UPDATE students SET age = 21 WHERE id = 1;` updates the age of the student with id 1 to 21.
  - DELETE: This command is used to delete existing data from a table. For example, `DELETE FROM students WHERE id = 1;` deletes the row with id 1 from the students table.
  - SELECT: This command is used to retrieve data from one or more tables. For example, `SELECT name, email FROM students WHERE age > 18;` retrieves the name and email of the students who are older than 18.

- **Data Query Language (DQL)**: This is another name for the SELECT command, which is used to query data from the database. DQL can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, etc. to filter, aggregate, sort or limit the data. For example, `SELECT name, COUNT(*) AS count FROM students GROUP BY name HAVING count > 1 ORDER BY count DESC LIMIT 10;` retrieves the name and number of students who have the same name, only for those who have more than one occurrence, sorted by the number of occurrences in descending order, and limited to the top 10 results.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of the database users and roles. Some examples of DCL commands are:

  - GRANT: This command is used to grant privileges or permissions to a user or role to perform certain actions on the database objects, such as tables, views, etc. For example, `GRANT SELECT, UPDATE ON students TO alice;` grants the SELECT and UPDATE privileges on the students table to the user alice.
  - REVOKE: This command is used to revoke or remove the privileges or permissions that were previously granted to a user or role. For example, `REVOKE UPDATE ON students FROM alice;` revokes the UPDATE privilege on the students table from the user alice.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, which are a set of logical operations that are performed as a single unit. Transactions ensure the consistency and integrity of the data by following the ACID properties (Atomicity, Consistency, Isolation, Durability). Some examples of TCL commands are:

  - BEGIN: This command is used to start a new transaction. For example, `



# SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They can be used to specify conditions, filter results, compare values, perform calculations, concatenate strings, and more. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used to perform mathematical operations on numerical data, such as addition, subtraction, multiplication, division, and modulus. For example, `SELECT 10 + 5;` returns 15.
- Comparison operators: These operators are used to compare two values or expressions and return a Boolean value (true or false). For example, `SELECT 10 > 5;` returns true.
- Logical operators: These operators are used to combine two or more conditions and return a Boolean value. They can be used to implement logical operations such as AND, OR, and NOT. For example, `SELECT 10 > 5 AND 10 < 15;` returns true.
- Bitwise operators: These operators are used to perform bit-level operations on binary data, such as AND, OR, XOR, NOT, and shift. For example, `SELECT 10 & 5;` returns 0, which is the result of performing a bitwise AND operation on the binary representations of 10 and 5.
- String operators: These operators are used to manipulate character data, such as concatenation, extraction, conversion, and pattern matching. For example, `SELECT 'Hello' + 'World';` returns HelloWorld, which is the result of concatenating two strings.
- Set operators: These operators are used to combine the results of two or more queries into a single result set, based on set theory. They can be used to implement operations such as union, intersection, difference, and symmetric difference. For example, `SELECT name FROM table1 UNION SELECT name FROM table2;` returns the names that are present in either table1 or table2, or both.

The procedure for using SQL operators depends on the type of operator and the context of the SQL statement. Generally, operators are used in conjunction with SQL clauses such as SELECT, WHERE, ON, HAVING, GROUP BY, and ORDER BY. The syntax and semantics of each operator may vary depending on the database system and the data types involved. Therefore, it is important to consult the documentation of the specific database system for more details and examples.



# Tables – Creation & Alteration

- A table is a collection of data organized in rows and columns in a relational database.
- To create a table in SQL, we use the **CREATE TABLE** statement, followed by the name of the table and the definition of the columns and their data types   .
- For example, the following SQL statement creates a table called **Customers** with four columns: **id**, **name**, **address**, and **phone**.

```sql
CREATE TABLE Customers (
  id int,
  name varchar(50),
  address text,
  phone varchar(10)
);
```

- To add data to a table, we use the **INSERT INTO** statement, followed by the name of the table, the columns to insert, and the values to insert .
- For example, the following SQL statement inserts a row into the **Customers** table with the values 1, 'Alice', '123 Main Street', and '555-1111'.

```sql
INSERT INTO Customers (id, name, address, phone)
VALUES (1, 'Alice', '123 Main Street', '555-1111');
```

- To modify the structure of a table, we use the **ALTER TABLE** statement, followed by the name of the table and the changes to apply   .
- For example, the following SQL statement adds a new column called **email** to the **Customers** table.

```sql
ALTER TABLE Customers
ADD email varchar(50);
```

- To delete a table, we use the **DROP TABLE** statement, followed by the name of the table .
- For example, the following SQL statement deletes the **Customers** table.

```sql
DROP TABLE Customers;
```

- To delete all the data from a table, but keep the table structure, we use the **TRUNCATE TABLE** statement, followed by the name of the table.
- For example, the following SQL statement deletes all the rows from the **Customers** table, but keeps the columns.

```sql
TRUNCATE TABLE Customers;
```

- To create a copy of an existing table, we use the **CREATE TABLE AS** statement, followed by the name of the new table and a query to select the data from the existing table.
- For example, the following SQL statement creates a new table called **TestTable** that is a copy of the **Customers** table.

```sql
CREATE TABLE TestTable AS
SELECT * FROM Customers;
```



# Defining Constraints for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- Constraints are rules or restrictions that are applied to the data in a table to ensure its validity and integrity.
- Constraints can be defined at the column level or the table level, depending on the scope of the rule.
- Constraints can be specified when creating a table using the CREATE TABLE statement, or after the table is created using the ALTER TABLE statement.
- Some of the common types of constraints are:

  - NOT NULL: This constraint ensures that a column cannot have a null value, which means it must have a value in every row.
  - UNIQUE: This constraint ensures that a column or a combination of columns has a unique value in every row, which means no two rows can have the same value.
  - PRIMARY KEY: This constraint identifies the column or the combination of columns that uniquely identifies each row in the table. A primary key is a special type of unique constraint that also implies a not null constraint.
  - FOREIGN KEY: This constraint establishes a relationship between a column or a combination of columns in one table and a primary key or a unique key in another table. A foreign key ensures that the value in the referencing column or columns must exist in the referenced column or columns.
  - CHECK: This constraint allows defining a condition that must be satisfied by the value in a column or a combination of columns. A check constraint can be used to enforce domain integrity, such as limiting the range of values or the format of values.
  - DEFAULT: This constraint specifies a default value for a column that is used when no value is provided for that column in an insert or update operation. A default constraint can be used to assign a constant value, a system function, or a user-defined function.



# Views and Indexes in SQL

## Views

- A view is a named query that is stored in the database and can be used like a table.
- A view can be created from one or more tables or other views, and can have a subset of columns and rows from the source tables.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface to changing data structures.
- A view can be created using the CREATE VIEW statement, followed by the view name and the SELECT query that defines the view.
- A view can be queried, updated, inserted into, or deleted from, as long as it meets certain conditions, such as not having aggregate functions, DISTINCT, or GROUP BY clauses.
- A view can be dropped using the DROP VIEW statement, followed by the view name.

## Indexes

- An index is a data structure that improves the speed of data retrieval from a table or a view.
- An index can be created on one or more columns of a table or a view, and can be used to quickly locate rows that match a search condition.
- An index can be created using the CREATE INDEX statement, followed by the index name, the table or view name, and the list of columns to be indexed.
- An index can be clustered or non-clustered, depending on whether it physically sorts the data rows or not.
- An index can be unique or non-unique, depending on whether it allows duplicate values or not.
- An index can be dropped using the DROP INDEX statement, followed by the index name and the table or view name.



# Queries and Subqueries in SQL

## What is a query?

- A query is a request for data or information from a database table or combination of tables.
- A query can be written in SQL (Structured Query Language), which is a standard language for accessing and manipulating databases.
- A query can perform various operations on the data, such as selecting, inserting, updating, deleting, sorting, filtering, grouping, aggregating, joining, etc.
- A query can return a result set, which is a collection of rows that match the criteria specified in the query.
- A query can be executed by a database management system (DBMS), which is a software that manages the storage and retrieval of data in a database.

## What is a subquery?

- A subquery is a query that is nested inside another query, also known as the outer query or the main query.
- A subquery can be used to return data that will be used in the outer query as a condition, a value, or a table.
- A subquery can be placed in various clauses of the outer query, such as the WHERE clause, the HAVING clause, the FROM clause, or the SELECT clause.
- A subquery can be classified into two types: correlated and non-correlated.
- A correlated subquery is a subquery that depends on the outer query for its values. It is executed once for each row of the outer query.
- A non-correlated subquery is a subquery that does not depend on the outer query for its values. It is executed only once and returns a single value or a set of values.

## Examples of subqueries

- A subquery in the WHERE clause can be used to filter the rows of the outer query based on the result of the subquery. For example, the following query returns the customers who have ordered more than the average order amount:

```sql
SELECT customer_id, customer_name, order_amount
FROM customers
WHERE order_amount > (SELECT AVG(order_amount) FROM customers);
```

- A subquery in the HAVING clause can be used to filter the groups of the outer query based on the result of the subquery. For example, the following query returns the products that have been ordered more than 10 times in the last month:

```sql
SELECT product_id, product_name, COUNT(order_id) AS order_count
FROM products
JOIN orders ON products.product_id = orders.product_id
WHERE order_date BETWEEN '2023-02-01' AND '2023-02-28'
GROUP BY product_id, product_name
HAVING COUNT(order_id) > (SELECT 10);
```

- A subquery in the FROM clause can be used to create a temporary table that can be joined with other tables in the outer query. For example, the following query returns the products that have the highest price in each category:

```sql
SELECT p.product_id, p.product_name, p.product_price, p.category_id, c.category_name
FROM products p
JOIN (SELECT category_id, MAX(product_price) AS max_price
      FROM products
      GROUP BY category_id) m
ON p.category_id = m.category_id AND p.product_price = m.max_price
JOIN categories c
ON p.category_id = c.category_id;
```

- A subquery in the SELECT clause can be used to return a single value or a set of values as a column in the outer query. For example, the following query returns the total number of orders and the average order amount for each customer:

```sql
SELECT customer_id, customer_name, 
       (SELECT COUNT(order_id) FROM orders WHERE customer_id = c.customer_id) AS order_count,
       (SELECT AVG(order_amount) FROM orders WHERE customer_id = c.customer_id) AS order_average
FROM customers c;
```



# Aggregate Functions

- Aggregate functions are SQL functions that perform calculations on a set of values and return a single value.
- Aggregate functions can be used in the select list or the having clause of a select statement.
- Aggregate functions ignore null values in the input set, except for the count function, which counts all rows.
- Aggregate functions can be used with the group by clause to group the input set by one or more columns and apply the function to each group.
- Some common aggregate functions are:

  - **avg**: returns the average of the numeric values in the input set.
  - **count**: returns the number of rows in the input set, or the number of rows with non-null values in a specific column.
  - **max**: returns the maximum value in the input set, or the maximum value of a specific column.
  - **min**: returns the minimum value in the input set, or the minimum value of a specific column.
  - **sum**: returns the sum of the numeric values in the input set, or the sum of the numeric values of a specific column.
  - **string_agg**: returns a string that concatenates the values of a string column in the input set, separated by a specified delimiter.

- Example of using aggregate functions:

  - To find the average, minimum, and maximum salary of all employees in the employees table, use the following query:

    ```sql
    select avg(salary) as average_salary, min(salary) as minimum_salary, max(salary) as maximum_salary
    from employees;
    ```

  - To find the number of employees in each department, use the following query:

    ```sql
    select department_id, count(*) as employee_count
    from employees
    group by department_id;
    ```

  - To find the total salary of each department, use the following query:

    ```sql
    select department_id, sum(salary) as total_salary
    from employees
    group by department_id;
    ```

  - To find the names of the employees who have the highest salary in each department, use the following query:

    ```sql
    select e.name, e.department_id, e.salary
    from employees e
    join (
      select department_id, max(salary) as max_salary
      from employees
      group by department_id
    ) m
    on e.department_id = m.department_id and e.salary = m.max_salary;
    ```



# Built-in functions

Built-in functions are expressions in which an SQL keyword or special operator executes some operation. They can be used in SQL SELECT expressions to calculate values and manipulate data. They can also be used in other SQL statements, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.

There are different types of built-in functions in SQL, such as:

- **String functions**: These functions perform operations on string values, such as concatenation, extraction, conversion, etc. Some examples are ASCII, CHAR, CHARINDEX, CONCAT, LEFT, RIGHT, etc.
- **Numeric functions**: These functions perform calculations on numeric values, such as arithmetic, rounding, trigonometry, etc. Some examples are ABS, CEILING, FLOOR, POWER, SQRT, SIN, COS, etc.
- **Date and time functions**: These functions perform operations on date and time values, such as extraction, conversion, addition, subtraction, etc. Some examples are DATEADD, DATEDIFF, DATEPART, GETDATE, YEAR, MONTH, DAY, etc.
- **Conversion functions**: These functions convert values from one data type to another, such as numeric, string, date, etc. Some examples are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, etc.
- **Aggregate functions**: These functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause to group rows into categories and apply a summary function to each group. Some examples are AVG, COUNT, MAX, MIN, SUM, etc.
- **Analytic functions**: These functions compute an aggregate value based on a group of rows. However, unlike aggregate functions, they do not reduce the number of rows returned by the query. They are often used with the OVER clause to specify the partitioning and ordering of the rows. Some examples are ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD, etc.
- **Bit manipulation functions**: These functions perform bitwise operations on binary values, such as AND, OR, XOR, NOT, etc. Some examples are BITAND, BITOR, BITXOR, BITNOT, etc.
- **System functions**: These functions return information about the system, such as the current user, database, session, etc. Some examples are CURRENT_USER, DB_NAME, HOST_NAME, SESSION_USER, etc.



# Unit 5 - Structured Query Language (SQL)

## Introduction

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- SQL can perform various tasks, such as creating, querying, updating, deleting, and modifying data and database objects.
- SQL is divided into several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- SQL follows a set of rules and syntax, which may vary slightly depending on the database management system (DBMS) used, such as Oracle, MySQL, SQL Server, etc.

## Data Definition Language (DDL)

- DDL is used to define and modify the structure of database objects, such as tables, views, indexes, constraints, etc.
- DDL commands include CREATE, ALTER, DROP, RENAME, and TRUNCATE.
- CREATE is used to create a new database object, such as a table or a view.
- ALTER is used to modify the structure or attributes of an existing database object, such as adding, deleting, or renaming columns or constraints in a table.
- DROP is used to delete an existing database object, such as a table or a view, and all its data and dependencies.
- RENAME is used to change the name of an existing database object, such as a table or a view.
- TRUNCATE is used to delete all the data from an existing table, but not the table structure or its dependencies.

## Data Manipulation Language (DML)

- DML is used to insert, update, delete, and retrieve data from database tables.
- DML commands include INSERT, UPDATE, DELETE, and SELECT.
- INSERT is used to add one or more rows of data to a table.
- UPDATE is used to modify one or more rows of data in a table based on a condition.
- DELETE is used to remove one or more rows of data from a table based on a condition.
- SELECT is used to query data from one or more tables based on a condition, and optionally sort, group, or aggregate the results.

## Data Control Language (DCL)

- DCL is used to control the access and permissions of users and roles on database objects and data.
- DCL commands include GRANT, REVOKE, and DENY.
- GRANT is used to give a user or a role a specific privilege or permission on a database object or data, such as SELECT, INSERT, UPDATE, DELETE, etc.
- REVOKE is used to take back a previously granted privilege or permission from a user or a role on a database object or data.
- DENY is used to explicitly prevent a user or a role from having a specific privilege or permission on a database object or data.

## Data Query Language (DQL)

- DQL is a subset of DML that is used to query data from database tables using the SELECT command.
- DQL can use various clauses, operators, functions, and keywords to specify the data to be retrieved, such as WHERE, ORDER BY, GROUP BY, HAVING, JOIN, UNION, DISTINCT, etc.
- WHERE is used to filter the rows of data based on a condition.
- ORDER BY is used to sort the rows of data based on one or more columns in ascending or descending order.
- GROUP BY is used to group the rows of data based on one or more columns and apply an aggregate function, such as SUM, AVG, COUNT, MIN, MAX, etc.
- HAVING is used to filter the groups of data based on a condition involving an aggregate function.
- JOIN is used to combine the data from two or more tables based on a common column or condition, such as INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, CROSS JOIN, etc.
- UNION is used to combine the results of two or more SELECT queries into a single result set, eliminating any duplicate rows.
- DISTINCT is used to eliminate any duplicate rows from the result set of a SELECT query.



# Update and Delete Operations for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- SQL is a language that allows users to view and manage data in a relational database system.
- Data Manipulation Language (DML) is a subset of SQL that deals with inserting, updating, deleting, and selecting data from tables and views.
- The UPDATE command is used to modify the existing records in the database. The syntax is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The SET clause specifies which columns to update and what values to assign to them.
- The WHERE clause specifies which rows to update based on a condition. If the WHERE clause is omitted, all rows in the table will be updated.
- The DELETE command is used to delete the records in the database that are no longer required. The syntax is:

```sql
DELETE FROM table_name
WHERE condition;
```

- The WHERE clause specifies which rows to delete based on a condition. If the WHERE clause is omitted, all rows in the table will be deleted.
- The SELECT command is used to retrieve data from the database. The syntax is:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- The SELECT clause specifies which columns to return from the table or view.
- The FROM clause specifies which table or view to query from.
- The WHERE clause specifies which rows to return based on a condition. If the WHERE clause is omitted, all rows in the table or view will be returned.
- The INSERT command is used to add new records to the database. The syntax is:

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

- The INSERT INTO clause specifies which table to insert the data into and which columns to fill.
- The VALUES clause specifies the values to assign to each column. The number and order of values must match the number and order of columns.
- SQL best practices for deleting and updating data include:
  - Using transactions to ensure data integrity and consistency. Transactions are a set of SQL statements that are executed as a single unit. If any statement fails, the whole transaction is rolled back and the database is restored to its previous state. Transactions can be started and ended with the BEGIN TRANSACTION and COMMIT TRANSACTION commands, respectively.
  - Using backup and restore mechanisms to prevent data loss. Backup and restore are processes that allow users to save and recover the data in the database in case of a failure or a mistake. Backup and restore can be performed using the BACKUP and RESTORE commands, respectively.
  - Using primary keys and foreign keys to enforce data relationships and constraints. Primary keys are columns that uniquely identify each row in a table. Foreign keys are columns that reference the primary keys of another table. Primary keys and foreign keys can be defined using the PRIMARY KEY and FOREIGN KEY constraints, respectively.
  - Using indexes to improve the performance of queries. Indexes are data structures that store the values of one or more columns in a sorted order, allowing faster access to the data. Indexes can be created using the CREATE INDEX command.



# Joins

- A join is a way of combining data from two or more tables based on a common column or condition.
- A join condition specifies how the tables are related, usually by matching values in one or more columns.
- A join can be classified into different types, such as inner join, outer join, cross join, self join, etc.
- A join can improve the performance and efficiency of queries by reducing the amount of data that needs to be scanned and processed.
- A join can also enhance the readability and maintainability of queries by avoiding subqueries and duplication of code.

## Inner Join

- An inner join returns only the rows that match the join condition in both tables.
- An inner join can be written using the keyword JOIN or the operator =.
- An inner join can be used to retrieve data from multiple tables that have a one-to-one, one-to-many, or many-to-many relationship.
- An inner join can be written as:

```sql
SELECT column_list
FROM table1
JOIN table2
ON table1.column = table2.column;
```

- Or as:

```sql
SELECT column_list
FROM table1, table2
WHERE table1.column = table2.column;
```

- For example, to join the Customers and Orders tables based on the CustomerID column, we can write:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

- This query will return the customer ID, first name, and order amount for all customers who have placed at least one order.

## Outer Join

- An outer join returns all the rows that match the join condition in either table, and also the rows that do not match in one or both tables.
- An outer join can be written using the keywords LEFT JOIN, RIGHT JOIN, or FULL JOIN.
- An outer join can be used to retrieve data from multiple tables that have a one-to-one, one-to-many, or many-to-many relationship, and also to find the missing or unmatched data in either table.
- An outer join can be written as:

```sql
SELECT column_list
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

- Or as:

```sql
SELECT column_list
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

- Or as:

```sql
SELECT column_list
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

- For example, to join the Customers and Orders tables based on the CustomerID column, and also to find the customers who have not placed any order, we can write:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

- This query will return the customer ID, first name, and order amount for all customers, and NULL for the order amount for the customers who have not placed any order.

## Cross Join

- A cross join returns the Cartesian product of the rows from the joined tables, i.e., every possible combination of rows from both tables.
- A cross join can be written using the keyword CROSS JOIN or the operator *.
- A cross join can be used to generate test data or to combine data from different sources that have no common column or condition.
- A cross join can be written as:

```sql
SELECT column_list
FROM table1
CROSS JOIN table2;
```

- Or as:

```sql
SELECT column_list
FROM table1, table2;
```

- For example, to join the Customers and Products tables based on no condition, we can write:

```sql
SELECT Customers.customer_id, Customers.first_name, Products.product_id, Products.product_name
FROM Customers
CROSS JOIN Products;
```

- This query will return the customer ID, first name, product ID, and product name for every possible combination of customers and products.

## Self Join

- A self join is a way of joining a table to itself, i.e., using the same table as both the left and right tables in the join.
- A self join can be written using any type of join, such as inner join, outer join, cross join, etc.
- A self join can be used to compare or find the relationship between the rows within the same table.
- A self join can be written as:

```sql
SELECT column_list
FROM table1 AS alias1
JOIN table1 AS alias2
ON alias1.column

```




# Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union eliminates any duplicate rows from the result set, unless the ALL option is specified.
- A union requires that the number and data types of the columns in the SELECT queries must be the same or compatible.
- A union can be used to combine data from different tables that have a similar structure or meaning.
- A union can be useful for performing queries across multiple tables or databases, or for combining data from different sources.

## Syntax of union in SQL

The basic syntax of a union is as follows:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION [ALL]
SELECT column1, column2, ..., columnN FROM table2;
```

- The UNION keyword is used to combine the result sets of the two SELECT queries.
- The ALL option is optional and can be used to include duplicate rows in the result set.
- The columns in the SELECT queries must have the same number and data types, and they must be in the same order.
- The column names in the result set are taken from the first SELECT query.

## Example of union in SQL

Suppose we have two tables, customers and suppliers, that store the information of the customers and suppliers of a company, respectively. The tables have the following structure and data:

| id | name | city | phone |
|----|------|------|-------|
| 1  | Alice | New York | 111-1111 |
| 2  | Bob | Los Angeles | 222-2222 |
| 3  | Charlie | Chicago | 333-3333 |

| id | name | city | phone |
|----|------|------|-------|
| 1  | David | London | 444-4444 |
| 2  | Eva | Paris | 555-5555 |
| 3  | Frank | Berlin | 666-6666 |

If we want to get the names and cities of all the customers and suppliers, we can use the following union query:

```sql
SELECT name, city FROM customers
UNION
SELECT name, city FROM suppliers;
```

The result set of the union query is:

| name | city |
|------|------|
| Alice | New York |
| Bob | Los Angeles |
| Charlie | Chicago |
| David | London |
| Eva | Paris |
| Frank | Berlin |

Note that the union query has eliminated any duplicate rows from the result set. If we want to include duplicate rows, we can use the ALL option as follows:

```sql
SELECT name, city FROM customers
UNION ALL
SELECT name, city FROM suppliers;
```

The result set of the union all query is:

| name | city |
|------|------|
| Alice | New York |
| Bob | Los Angeles |
| Charlie | Chicago |
| David | London |
| Eva | Paris |
| Frank | Berlin |
| David | London |
| Eva | Paris |
| Frank | Berlin |

Note that the union all query has included the duplicate rows from the second SELECT query in the result set.



# Intersection

- The **INTERSECT** operator in SQL is used to combine two **SELECT** statements and return only the rows that are common in both the statements.
- The **INTERSECT** operator acts as a mathematical intersection, meaning it returns the elements that belong to both sets.
- The syntax of the **INTERSECT** operator is as follows:

```sql
SELECT column_list
FROM table1
INTERSECT
SELECT column_list
FROM table2;
```

- The column_list in both the **SELECT** statements must have the same number and order of columns, and the data types must be compatible.
- The **INTERSECT** operator eliminates duplicate rows from the result set, unless the **ALL** option is specified.
- The **INTERSECT** operator can be combined with other set operators, such as **UNION** and **EXCEPT**, using parentheses to specify the order of operations.
- The **INTERSECT** operator can be used to find common values in different tables, such as customers who ordered products from different categories, or employees who work in different departments.
- Some examples of using the **INTERSECT** operator are:

```sql
-- Find the customers who ordered both books and movies
SELECT customer_id
FROM orders
WHERE category = 'Books'
INTERSECT
SELECT customer_id
FROM orders
WHERE category = 'Movies';

-- Find the employees who work in both sales and marketing departments
SELECT employee_id
FROM employees
WHERE department = 'Sales'
INTERSECT
SELECT employee_id
FROM employees
WHERE department = 'Marketing';

-- Find the products that are sold in both USA and Canada
SELECT product_id
FROM sales
WHERE country = 'USA'
INTERSECT
SELECT product_id
FROM sales
WHERE country = 'Canada';
```



# Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- SQL commands can be classified into four categories: DDL, DML, DCL, and DQL.

## Data Definition Language (DDL)

- DDL is used to define the structure and schema of the database, such as tables, views, indexes, constraints, etc.
- DDL commands include CREATE, ALTER, DROP, RENAME, and TRUNCATE.
- Examples of DDL commands are:

```sql
-- Create a table named Student with four columns: id, name, age, and major
CREATE TABLE Student (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  major VARCHAR(20)
);

-- Add a column named email to the Student table
ALTER TABLE Student
ADD email VARCHAR(50) UNIQUE;

-- Delete the Student table and its data
DROP TABLE Student;

-- Rename the Student table to Students
RENAME TABLE Student TO Students;

-- Delete all the data from the Students table but keep the table structure
TRUNCATE TABLE Students;
```

## Data Manipulation Language (DML)

- DML is used to insert, update, delete, and merge data in the database tables.
- DML commands include INSERT, UPDATE, DELETE, and MERGE.
- Examples of DML commands are:

```sql
-- Insert a new record into the Students table
INSERT INTO Students (id, name, age, major, email)
VALUES (1, 'Alice', 19, 'Computer Science', 'alice@example.com');

-- Update the age and email of the student with id 1
UPDATE Students
SET age = 20, email = 'alice@new.com'
WHERE id = 1;

-- Delete the record of the student with id 1
DELETE FROM Students
WHERE id = 1;

-- Merge the data from the NewStudents table into the Students table
MERGE INTO Students AS S
USING NewStudents AS N
ON S.id = N.id
WHEN MATCHED THEN
  UPDATE SET S.name = N.name, S.age = N.age, S.major = N.major, S.email = N.email
WHEN NOT MATCHED THEN
  INSERT (id, name, age, major, email) VALUES (N.id, N.name, N.age, N.major, N.email);
```

## Data Control Language (DCL)

- DCL is used to control the access and permissions of the database users and roles.
- DCL commands include GRANT, REVOKE, and DENY.
- Examples of DCL commands are:

```sql
-- Grant the SELECT and UPDATE privileges on the Students table to the user Bob
GRANT SELECT, UPDATE ON Students TO Bob;

-- Revoke the UPDATE privilege on the Students table from the user Bob
REVOKE UPDATE ON Students FROM Bob;

-- Deny the DELETE privilege on the Students table to the user Bob
DENY DELETE ON Students TO Bob;
```

## Data Query Language (DQL)

- DQL is used to retrieve and manipulate data from the database tables and views.
- DQL commands include SELECT, JOIN, GROUP BY, HAVING, ORDER BY, and LIMIT.
- Examples of DQL commands are:

```sql
-- Select all the columns and records from the Students table
SELECT * FROM Students;

-- Select the name and email of the students who are majoring in Computer Science
SELECT name, email FROM Students
WHERE major = 'Computer Science';

-- Select the name and major of the students who are older than 18 and sort them by name in ascending order
SELECT name, major FROM Students
WHERE age > 18
ORDER BY name ASC;

-- Select the name and age of the students who are younger than 20 and group them by age
SELECT name, age FROM Students
WHERE age < 20
GROUP BY age;

-- Select the average age of the students who are majoring in Computer Science and having an email ending with '.com'
SELECT AVG(age) FROM Students
WHERE major = 'Computer Science' AND email LIKE '%.com';

-- Select the first 10 records from the Students table
SELECT * FROM Students
LIMIT 10;
```



# Transaction Control Commands

- Transaction Control Language (TCL) is a subset of SQL that is used to manage transactions in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- Transactions ensure the consistency and integrity of the database by following the ACID properties: Atomicity, Consistency, Isolation, and Durability.
- The following commands are used to control transactions in SQL:

  - **COMMIT**: This command is used to make a transaction permanent in a database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK**: This command is used to undo the changes made by the transaction and restore the database to its previous state. It aborts the current transaction and discards any changes made since the last commit or savepoint.
  - **SAVEPOINT**: This command is used to create points within a transaction in which to rollback. It allows partial rollback of a transaction by specifying a name for a savepoint. Multiple savepoints can be created within a transaction.
  - **SET TRANSACTION**: This command is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write access, and name.

- SQL Server operates in the following transaction modes:

  - **Autocommit transactions**: Each individual statement is a transaction. The changes made by the statement are committed or rolled back automatically depending on whether the statement succeeds or fails.
  - **Explicit transactions**: Each transaction is explicitly started with the `BEGIN TRANSACTION` statement and explicitly ended with a `COMMIT` or `ROLLBACK` statement. The changes made by the transaction are not permanent until a `COMMIT` statement is executed.
  - **Implicit transactions**: A new transaction is implicitly started when the previous transaction is completed. The `SET IMPLICIT_TRANSACTIONS ON` statement enables this mode. The changes made by the transaction are not permanent until a `COMMIT` statement is executed.

- Examples of transaction control commands in SQL:

  - To start an explicit transaction and commit it:

    ```sql
    BEGIN TRANSACTION;
    -- SQL statements
    COMMIT TRANSACTION;
    ```

  - To start an explicit transaction and rollback it:

    ```sql
    BEGIN TRANSACTION;
    -- SQL statements
    ROLLBACK TRANSACTION;
    ```

  - To create a savepoint within a transaction and rollback to it:

    ```sql
    BEGIN TRANSACTION;
    -- SQL statements
    SAVEPOINT savepoint_name;
    -- SQL statements
    ROLLBACK TRANSACTION savepoint_name;
    -- SQL statements
    COMMIT TRANSACTION;
    ```

  - To set the isolation level of a transaction to serializable:

    ```sql
    SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
    BEGIN TRANSACTION;
    -- SQL statements
    COMMIT TRANSACTION;
    ```



## Unit 6 - PL/SQL

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that allows users to write procedural code in Oracle database.
- PL/SQL supports variables, constants, data types, operators, expressions, control structures, loops, arrays, cursors, exceptions, subprograms, packages, triggers, and object-oriented features.
- PL/SQL code is stored in the database as compiled units, which can be executed by other applications or database objects.
- PL/SQL code can be embedded in SQL statements or run as standalone blocks or scripts.
- PL/SQL code can interact with SQL data and manipulate it using DML (Data Manipulation Language) statements such as INSERT, UPDATE, DELETE, and MERGE.
- PL/SQL code can also use DDL (Data Definition Language) statements such as CREATE, ALTER, DROP, and RENAME to create or modify database objects.
- PL/SQL code can use SQL functions and operators to perform calculations and transformations on data.
- PL/SQL code can use SQL queries to retrieve data from tables or views and store it in variables or collections.
- PL/SQL code can use cursors to process data row by row in a loop.
- PL/SQL code can use exceptions to handle errors and unexpected situations.
- PL/SQL code can use subprograms to modularize and reuse code. Subprograms can be procedures, functions, or anonymous blocks.
- PL/SQL code can use packages to group related subprograms, variables, constants, cursors, and exceptions into a single unit.
- PL/SQL code can use triggers to execute code automatically in response to database events such as INSERT, UPDATE, DELETE, or DDL statements.
- PL/SQL code can use object-oriented features to define and manipulate user-defined types, such as objects, collections, and references.



# Introduction for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is a programming language that extends SQL, the standard language for accessing and manipulating data in relational databases.
- PL/SQL allows users to create stored procedures, functions, triggers, packages, and other program units that can be executed by the database server. PL/SQL also supports features such as variables, constants, data types, operators, expressions, control structures, loops, arrays, collections, cursors, exceptions, and records.
- PL/SQL is designed to integrate seamlessly with SQL. Users can embed SQL statements in PL/SQL blocks, and use PL/SQL variables and parameters in SQL statements. PL/SQL also provides built-in functions and packages that can be used to manipulate data, perform calculations, handle errors, and interact with the database server.
- PL/SQL is a compiled language. The database server compiles and stores PL/SQL program units in the database, where they can be executed by other applications or users. The compilation process checks the syntax and semantics of the PL/SQL code, and generates an executable form that can run efficiently on the database server.
- PL/SQL is a portable language. It can run on any platform that supports Oracle Database, and it is compatible with different versions of Oracle Database. PL/SQL also follows the ANSI/ISO SQL standards, and can interoperate with other languages and technologies that use SQL.



# Features of PL/SQL

PL/SQL is a procedural extension of SQL that allows developers to write efficient and compact code for manipulating data in a database. Some of the features of PL/SQL are:

- **Tight integration with SQL**: PL/SQL can execute SQL statements directly, without any need for translation or interface. PL/SQL can also use SQL data types, operators, and functions .
- **Extensive error checking**: PL/SQL can detect and handle errors at compile time and run time, using predefined and user-defined exceptions. PL/SQL also provides debugging tools and facilities .
- **Numerous data types**: PL/SQL supports scalar, composite, reference, and large object (LOB) data types, as well as user-defined types and subtypes. PL/SQL also supports collections, such as arrays, nested tables, and varrays .
- **Variety of programming structures**: PL/SQL provides control structures, such as loops, conditional statements, and exception handlers, as well as modular structures, such as subprograms, packages, triggers, and object types. PL/SQL also supports cursors, which are pointers to the result sets of SQL queries .
- **Structured programming**: PL/SQL supports the development of reusable and maintainable code, using functions and procedures. Functions return a single value, while procedures perform a specific task. Both functions and procedures can accept parameters and can be nested, overloaded, and invoked from other subprograms .
- **Object-oriented programming**: PL/SQL supports the creation and manipulation of user-defined types, which are abstract data types that encapsulate attributes and methods. PL/SQL also supports inheritance, polymorphism, and encapsulation, which are the key features of object-oriented programming .
- **Web application development**: PL/SQL can be used to create dynamic web pages and server pages, using PL/SQL Server Pages (PSP) and PL/SQL Web Toolkit. PL/SQL can also interact with web servers, browsers, and other web technologies, such as XML, HTML, and Java  .



# PL/SQL Syntax and Constructs

- PL/SQL is a procedural extension of SQL that allows you to write complex and modular programs that interact with Oracle databases .
- The basic unit of PL/SQL is a block, which consists of three sections: declaration, execution, and exception .
- The declaration section is optional and contains the definitions of constants, variables, cursors, exceptions, and other identifiers .
- The execution section is mandatory and contains the executable statements that perform the logic of the program .
- The exception section is optional and contains the handlers for the errors that may occur during the execution of the program .
- The syntax of a PL/SQL block is as follows:

```sql
DECLARE --optional
  <declarations>
BEGIN --mandatory
  <executable statements>
EXCEPTION --optional
  <exception handlers>
END; --mandatory
/
```

- A PL/SQL block can be anonymous or named. An anonymous block is not stored in the database and is executed once. A named block is stored in the database and can be invoked repeatedly. A named block can be a procedure, a function, a package, or a trigger.
- PL/SQL supports many procedural constructs, such as variables, constants, data types, operators, expressions, assignments, conditional statements, loops, cursors, exceptions, subprograms, and packages  .
- PL/SQL also supports SQL statements, such as SELECT, INSERT, UPDATE, DELETE, and MERGE, which can be embedded in the execution section of a PL/SQL block .
- PL/SQL uses the compatibility collation USING_NLS_COMP for all data processed in PL/SQL expressions, which instructs collation-sensitive operators to behave in the same way as in previous Oracle Database releases.



# SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is an extension of SQL that allows developers to write procedural code using SQL statements within its syntax.
- PL/SQL program units are compiled by the Oracle Database server and stored inside the database. And at run-time, both PL/SQL and SQL run within the same server process, bringing optimal efficiency.
- PL/SQL offers a set of procedural commands (IF statements, loops, assignments), organized within blocks, that complement and extend the reach of SQL.
- A PL/SQL block is a basic unit of PL/SQL code that consists of three sections: declaration, executable, and exception-handling. A block can be nested inside another block, creating a hierarchical structure of code.
- PL/SQL supports two types of SQL statements: static and dynamic. Static SQL statements are known at compile time and can be embedded directly in the PL/SQL code. Dynamic SQL statements are constructed at run time and can be executed using the EXECUTE IMMEDIATE statement or the DBMS_SQL package.
- The EXECUTE IMMEDIATE statement allows you to execute a single SQL statement that is stored in a character string variable or a string literal. The syntax is:

```sql
EXECUTE IMMEDIATE dynamic_string
[INTO {define_variable[, define_variable]... | record}]
[USING [IN | OUT | IN OUT] bind_argument
[, [IN | OUT | IN OUT] bind_argument]...];
```

- The DBMS_SQL package allows you to execute multiple SQL statements that are stored in a cursor variable. The process of creating and executing the dynamic SQL using the DBMS_SQL package involves the following steps:

  - OPEN CURSOR: The dynamic SQL will execute in the same way as a cursor.
  - PARSE: The SQL statement is parsed and associated with the cursor.
  - BIND_VARIABLE: The bind variables are associated with the placeholders in the SQL statement.
  - DEFINE_COLUMN: The output columns are defined and associated with the variables.
  - EXECUTE: The SQL statement is executed.
  - FETCH_ROWS: The result set is fetched row by row.
  - CLOSE_CURSOR: The cursor is closed and released.

- The syntax for using the DBMS_SQL package is:

```sql
DECLARE
  c NUMBER; -- cursor variable
  n NUMBER; -- number of rows affected
  v VARCHAR2(20); -- output variable
BEGIN
  c := DBMS_SQL.OPEN_CURSOR; -- open cursor
  DBMS_SQL.PARSE(c, 'UPDATE emp SET sal = sal * 1.1 WHERE deptno = :x', DBMS_SQL.NATIVE); -- parse SQL statement with a bind variable :x
  DBMS_SQL.BIND_VARIABLE(c, ':x', 10); -- bind variable :x with value 10
  n := DBMS_SQL.EXECUTE(c); -- execute SQL statement and return number of rows affected
  DBMS_OUTPUT.PUT_LINE('Rows updated: ' || n); -- display number of rows affected
  DBMS_SQL.PARSE(c, 'SELECT ename FROM emp WHERE deptno = :x', DBMS_SQL.NATIVE); -- parse another SQL statement with the same bind variable :x
  DBMS_SQL.DEFINE_COLUMN(c, 1, v, 20); -- define output column 1 with variable v and size 20
  LOOP
    IF DBMS_SQL.FETCH_ROWS(c) > 0 THEN -- fetch rows until no more rows
      DBMS_SQL.COLUMN_VALUE(c, 1, v); -- get column value for column 1 into variable v
      DBMS_OUTPUT.PUT_LINE(v); -- display variable v
    ELSE
      EXIT; -- exit loop
    END IF;
  END LOOP;
  DBMS_SQL.CLOSE_CURSOR(c); -- close cursor
END;
```

- To output a SELECT statement from a PL/SQL block, you can use the DBMS_OUTPUT.PUT_LINE function to display the result on the screen. However, this requires that the server output is enabled and that the result set is small. Alternatively, you can use a cursor FOR loop or a PIPELINED function to return the result as a collection.



# DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity  .
- DML statements can be executed from within any PL/SQL block of code against any and all tables and views to which you have access.
- There are four types of DML statements: INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert data into a table or a view .
- UPDATE statement is used to modify data in a table or a view .
- DELETE statement is used to remove data from a table or a view .
- MERGE statement is used to combine data from two tables into one table based on a matching condition .
- DML statements can be used with variables, expressions, conditions, and subqueries in PL/SQL .
- DML statements can also return values into PL/SQL variables using the RETURNING clause .
- DML statements can be executed using the EXECUTE IMMEDIATE statement in PL/SQL, which allows dynamic SQL execution .
- DML statements can be grouped into transactions, which are logical units of work that either succeed or fail as a whole .
- Transactions can be committed or rolled back using the COMMIT or ROLLBACK statements in PL/SQL .
- Transactions can also be controlled using the SAVEPOINT, SET TRANSACTION, and LOCK TABLE statements in PL/SQL .



# Cursors

- A cursor is a pointer to a result set, or the data that results from a query .
- A cursor allows you to fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.
- A cursor also holds information about the context area, which is a memory area that contains the execution state of a SQL statement .
- PL/SQL has two types of cursors: implicit cursors and explicit cursors.

## Implicit Cursors

- Implicit cursors are automatically created by Oracle whenever an SQL statement such as SELECT INTO, INSERT, UPDATE, or DELETE is executed.
- Implicit cursors are also known as SQL cursors, and they have attributes such as %FOUND, %ISOPEN, %NOTFOUND, and %ROWCOUNT that can be used to check the status and outcome of the SQL statement.
- Implicit cursors are useful for simple queries that return only one row or perform a single data manipulation operation.

## Explicit Cursors

- Explicit cursors are user-defined cursors that are declared and controlled by the programmer .
- Explicit cursors are used for complex queries that return more than one row or require more processing logic.
- Explicit cursors have four steps: declaration, opening, fetching, and closing .
- Declaration: The cursor is declared using the CURSOR keyword, followed by a name and a query .
- Opening: The cursor is opened using the OPEN statement, which allocates the context area and executes the query .
- Fetching: The cursor is fetched using the FETCH statement, which retrieves one or more rows from the result set and assigns them to variables or records .
- Closing: The cursor is closed using the CLOSE statement, which frees the context area and releases the resources .
- Explicit cursors can also have parameters, which are variables that are passed to the query when the cursor is opened .
- Explicit cursors can also be used with cursor FOR loops, which simplify the fetching and processing of the rows in the result set .



# Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database for reuse .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to it. The body contains the declarative, executable, and exception-handling parts of the code .
- A stored procedure can be created using the CREATE PROCEDURE statement, which has the following syntax :

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
  (parameter1 [IN|OUT|IN OUT] datatype1 [DEFAULT value1],
   parameter2 [IN|OUT|IN OUT] datatype2 [DEFAULT value2],
   ...
   parameterN [IN|OUT|IN OUT] datatypeN [DEFAULT valueN])
IS
  -- declarative part
  variable1 datatype1;
  variable2 datatype2;
  ...
  variableN datatypeN;
BEGIN
  -- executable part
  statement1;
  statement2;
  ...
  statementN;
EXCEPTION
  -- exception-handling part
  WHEN exception1 THEN
    statement1;
    statement2;
    ...
    statementN;
  WHEN exception2 THEN
    statement1;
    statement2;
    ...
    statementN;
  ...
  WHEN exceptionN THEN
    statement1;
    statement2;
    ...
    statementN;
END procedure_name;
```

- A stored procedure can be executed using the EXECUTE or EXEC command, which has the following syntax :

```sql
EXECUTE schema.procedure_name(parameter1, parameter2, ..., parameterN);
```

- A stored procedure can be dropped using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE schema.procedure_name;
```

- A stored procedure can be modified using the ALTER PROCEDURE statement, which has the following syntax:

```sql
ALTER PROCEDURE schema.procedure_name COMPILE;
```

- A stored procedure can have advantages such as modularity, reusability, maintainability, security, and performance .



# Stored Function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement or another PL/SQL block .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must not have any side effects such as committing or rolling back transactions .

## Syntax of a Stored Function

The syntax for creating a stored function is as follows :

```sql
CREATE [ OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
[declarative section]
BEGIN
[executable section]
RETURN expression;
EXCEPTION
[exception handling section]
END [function_name];
```

- The `CREATE OR REPLACE` clause allows you to modify an existing function or create a new one if it does not exist .
- The `function_name` is the name of the function that must be unique within the schema .
- The `parameter_list` is a comma-separated list of parameters that can have different modes: `IN`, `OUT`, or `IN OUT` .
- The `return_type` is the data type of the value that the function returns .
- The `IS` keyword marks the beginning of the function body .
- The `declarative section` is optional and can contain declarations of variables, constants, cursors, or exceptions that are used in the function .
- The `BEGIN` keyword marks the beginning of the executable section that contains the logic of the function .
- The `RETURN` statement specifies the expression that evaluates to the value that the function returns .
- The `EXCEPTION` keyword marks the beginning of the exception handling section that can handle any errors or exceptions that occur in the function .
- The `END` keyword marks the end of the function body and can optionally include the function name for clarity .

## Example of a Stored Function

The following example shows how to create a stored function that calculates the factorial of a given number:

```sql
CREATE OR REPLACE FUNCTION factorial (n IN NUMBER)
RETURN NUMBER
IS
  result NUMBER := 1;
BEGIN
  IF n < 0 THEN
    RAISE VALUE_ERROR;
  END IF;
  FOR i IN 1..n LOOP
    result := result * i;
  END LOOP;
  RETURN result;
EXCEPTION
  WHEN VALUE_ERROR THEN
    DBMS_OUTPUT.PUT_LINE('Invalid input');
    RETURN NULL;
END factorial;
```

The function takes a parameter `n` of type `NUMBER` and returns a `NUMBER` as well. It declares a local variable `result` to store the intermediate values. It checks if the input is negative and raises a `VALUE_ERROR` exception if so. It uses a `FOR` loop to iterate from 1 to n and multiply the result by each value. It returns the final result or `NULL` if an exception occurs.

To invoke the function, you can use a `SELECT` statement or a PL/SQL block, for example:

```sql
SELECT factorial(5) FROM dual;
```

The output is:

```sql
FACTORIAL(5)
------------
120
```



# Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP.
- Triggers can be used for maintaining the integrity of the information on the database, implementing complex data interactions, auditing data changes, or enforcing business rules.
- Triggers are defined on a table, stored in the associated database, and executed as a result of an event on that table or view.
- Triggers can be created in the master database and behave just like those created in user-designed databases.
- Triggers can be recursive, meaning that they can fire themselves or other triggers, or nested, meaning that they can fire other triggers that fire them.
- Triggers can be disabled or enabled, modified or dropped, using SQL commands .
- Triggers can be queried using the sys.triggers catalog view.



# Unit 6 - PL/SQL

## Introduction

- PL/SQL stands for Procedural Language/Structured Query Language.
- It is an extension of SQL that allows users to write procedural code in a database environment.
- It supports variables, constants, data types, operators, expressions, control structures, loops, functions, procedures, triggers, packages, cursors, exceptions, and arrays.
- It can be used to create and execute stored procedures, functions, and triggers, which are reusable blocks of code that can perform complex tasks and improve performance.
- It can also be used to embed SQL statements in a procedural code, which can handle errors and manipulate data more efficiently.

## Advantages of PL/SQL

- PL/SQL allows users to combine the power of SQL with the flexibility of procedural programming.
- PL/SQL can reduce network traffic and improve performance by executing multiple SQL statements in a single block of code on the server side, rather than sending them one by one from the client side.
- PL/SQL can enhance the security and integrity of data by enforcing business rules and logic in the database layer, rather than relying on the application layer.
- PL/SQL can simplify the maintenance and debugging of complex applications by modularizing the code into reusable and self-contained units.
- PL/SQL can increase the portability and compatibility of applications by following the ANSI/ISO SQL standards and running on any Oracle platform.

## PL/SQL Architecture

- PL/SQL is a block-structured language, which means that the code is organized into logical units called blocks.
- A block consists of three sections: declaration, executable, and exception.
- The declaration section defines the variables, constants, cursors, and user-defined data types that are used in the block.
- The executable section contains the SQL statements and PL/SQL statements that perform the main logic of the block.
- The exception section handles the errors and exceptions that may occur during the execution of the block.
- A block can be nested inside another block, creating a hierarchical structure of blocks.
- A block can be named or anonymous, depending on whether it has an identifier or not.
- A named block can be a stored procedure, function, or trigger, which can be invoked by other blocks or applications.
- An anonymous block is a one-time block that is not stored in the database and is executed only once.



## Unit 7 - Transaction Processing Concepts

- A transaction is a logical unit of work that represents a real-world event of interest to a business or an organization.
- A transaction processing system (TPS) is a software system that supports the execution of transactions and ensures their correctness, consistency, durability, and availability.
- The main characteristics of a transaction are atomicity, consistency, isolation, and durability (ACID).
  - Atomicity means that a transaction either completes all its operations or none of them.
  - Consistency means that a transaction preserves the integrity and validity of the data.
  - Isolation means that a transaction does not interfere with other concurrent transactions.
  - Durability means that the effects of a transaction are permanent and survive any system failures.
- The main components of a TPS are the transaction manager, the scheduler, the recovery manager, and the data manager.
  - The transaction manager is responsible for initiating, coordinating, and terminating transactions.
  - The scheduler is responsible for controlling the order and concurrency of transactions.
  - The recovery manager is responsible for restoring the system to a consistent state in case of failures.
  - The data manager is responsible for accessing and manipulating the data stored in the database or other data sources.
- The main types of failures that can affect a TPS are transaction failures, system failures, media failures, and network failures.
  - Transaction failures are caused by logical errors, such as division by zero, or by user aborts.
  - System failures are caused by hardware or software malfunctions, such as power outages, memory errors, or bugs.
  - Media failures are caused by physical damage to the storage devices, such as disk crashes, fire, or flood.
  - Network failures are caused by communication problems, such as broken links, congestion, or security breaches.
- The main techniques for ensuring the reliability and availability of a TPS are logging, checkpointing, backup, and replication.
  - Logging is the process of recording the changes made by transactions to the data in a separate file called the log.
  - Checkpointing is the process of periodically saving the state of the system to a stable storage device.
  - Backup is the process of copying the data from the primary storage device to a secondary storage device for recovery purposes.
  - Replication is the process of maintaining multiple copies of the data on different storage devices or servers for fault tolerance and load balancing purposes.



# Transaction Concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. Transactions are executed by users or applications to perform some tasks on the database. Transactions have the following characteristics:

- A transaction is a **single unit of logic** or work, that is either performed in its entirety or not at all .
- A transaction is **independent** of other transactions, meaning that its execution does not interfere with or depend on the execution of other transactions.
- A transaction is **coherent and reliable**, meaning that it preserves the consistency and integrity of the database .
- A transaction can be **committed** or **aborted**. Committing a transaction means that the changes made by the transaction are permanently saved in the database. Aborting a transaction means that the changes made by the transaction are discarded and the database is restored to its previous state .

A transaction can be executed using a language like SQL wrapped in a transaction, using a pattern similar to the following:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

A transaction must satisfy the **ACID** properties, which are as follows:

- **Atomicity**: The 'all or nothing' property. A transaction is an indivisible entity that is either performed in its entirety or not at all. If any part of the transaction fails, the whole transaction is aborted and the database is left unchanged.
- **Consistency**: A transaction must alter the database from one steady-state to another steady state. This means that the transaction must obey the rules and constraints defined by the database schema, such as data types, primary keys, foreign keys, etc. The transaction must not leave the database in an inconsistent or invalid state.
- **Isolation**: Transactions must appear to execute in isolation from each other, meaning that the concurrent execution of multiple transactions does not affect their outcomes. Each transaction must operate on a consistent snapshot of the database, as if no other transactions were running at the same time.
- **Durability**: The changes made by a committed transaction must persist in the database, even in the event of system failures, power outages, crashes, etc. The database system must ensure that the committed data is safely stored and can be recovered when needed.

These properties are essential for ensuring the correctness and reliability of transactions and the database system.



# Properties of Transaction in DBMS

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four main properties, also known as ACID properties, that ensure the reliability and correctness of the database.
- The ACID properties are:

  - **Atomicity**: This means that a transaction is either executed completely or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state.
  - **Consistency**: This means that a transaction must preserve the integrity and validity of the database. A transaction must obey the predefined rules and constraints of the database, such as primary keys, foreign keys, triggers, etc. A transaction must not leave the database in an inconsistent state.
  - **Isolation**: This means that a transaction must not interfere with other concurrent transactions. A transaction must execute as if it is the only transaction in the system. The intermediate results of a transaction must not be visible to other transactions until the transaction is committed or aborted.
  - **Durability**: This means that the effects of a committed transaction must be permanent and persistent in the database. The changes made by a transaction must not be lost due to system failures, power outages, crashes, etc. The database must ensure the recovery of the committed transactions in case of any failure.

- These properties are essential for maintaining the accuracy and consistency of the data in a database. They also help in preventing data loss, corruption, and anomalies.



# Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of a database.
- A schedule is serializable if it is equivalent to some serial schedule, where transactions are executed one after the other without any overlap.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read-write, write-read, or write-write) on the same data item in a schedule must be ordered in the same way as in a serial schedule.
- View serializability is a weaker form of serializability that requires that any two schedules have the same initial and final state of the database, and that any read operation on a data item in a schedule must read the same value as in a serial schedule.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph is a directed graph of the entire transactions of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions.
- A precedence graph is a subset of a serialization graph that only contains the edges that indicate the order of conflicting operations on the same data item.
- A schedule is conflict serializable if and only if its serialization graph or precedence graph is acyclic, meaning that it does not contain any cycles.
- A schedule is view serializable if and only if it is view equivalent to some serial schedule, where two schedules are view equivalent if they have the same initial and final state of the database, and the same read operations on the same data items.
- Testing for view serializability is more complex than testing for conflict serializability, and it involves checking for potential cycles between transactions' precedence relationships.
- A precedence relationship exists when one transaction must precede another transaction for the schedule to be valid. For example, if transaction T1 reads a data item X that was written by transaction T2, then T2 must precede T1 in any serial schedule.
- A schedule is view serializable if and only if it has a legal serialization order, meaning that there is a way to order the transactions in a serial schedule such that no precedence relationship is violated.
- A legal serialization order can be found by using a topological sorting algorithm on the precedence graph, which produces an order of nodes such that no node appears before its predecessors. If the precedence graph is cyclic, then there is no legal serialization order and the schedule is not view serializable.



# Serializability of schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- Serializability is a property of a schedule that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it produces the same effect on the database as some serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read and write operations on the same data item) in a schedule must be ordered in the same way as in some serial schedule.
- View serializability is a weaker form of serializability that requires that any two transactions in a schedule must have the same view of the database as in some serial schedule. A view of a transaction consists of three components: the initial read set, the final write set, and the read-from relation.
- To check whether a schedule is conflict serializable, we can use a precedence graph, which is a directed graph where the nodes are transactions and the edges are conflicts. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- To check whether a schedule is view serializable, we can use a polygraph, which is a directed graph where the nodes are operations and the edges are view dependencies. A schedule is view serializable if and only if its polygraph is acyclic and has a unique sink node for each data item.
- Serializability is important for concurrency control, which is the mechanism to ensure the isolation and atomicity of transactions in a database system. Concurrency control techniques, such as locking, timestamping, and validation, can enforce serializability by preventing or resolving conflicts among transactions.



# Conflict and View Serializable Schedule

## Conflict Serializability

- A schedule is called **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be **conflicting** if all conditions satisfy:
  - They belong to different transactions
  - They operate on the same data item
  - At least one of them is a write operation
- A schedule is **conflict serializable** if it preserves the order of conflicting operations of every pair of transactions in a serial schedule.
- Conflict serializability can be checked by using a **precedence graph** or a **conflict graph**  .
  - A precedence graph is a directed graph where the nodes represent the transactions and the edges represent the conflicts between them.
  - An edge from Ti to Tj means that Ti must precede Tj in any serial schedule that is conflict equivalent to the given schedule.
  - A schedule is conflict serializable if and only if its precedence graph is **acyclic** .

## View Serializability

- A schedule is called **view serializable** if it is view equal to a serial schedule.
- Two schedules are said to be **view equal** if the order of initial read, final write and update operations is the same in both the schedules .
- A schedule is **view serializable** if it preserves the following three conditions for every data item in a serial schedule:
  - **Initial read condition**: If a transaction Ti reads the initial value of a data item X in S, then the same transaction must read the initial value of X in S'.
  - **Final write condition**: If a transaction Ti performs the final write on a data item X in S, then the same transaction must perform the final write on X in S'.
  - **Update read condition**: If a transaction Ti reads the value of a data item X written by another transaction Tj in S, then the same transaction must read the value of X written by the same transaction in S'.
- View serializability can be checked by using a **polygraph** or a **view graph**.
  - A polygraph is a directed graph where the nodes represent the read and write operations and the edges represent the dependencies between them.
  - An edge from Ri(X) to Wj(X) means that Ti must read the initial value of X before Tj writes the final value of X.
  - An edge from Wi(X) to Rj(X) means that Ti must write the value of X that is read by Tj.
  - An edge from Wi(X) to Wj(X) means that Ti must write the value of X before Tj overwrites it.
  - A schedule is view serializable if and only if its polygraph is **acyclic**.

## Difference between Conflict and View Serializability

- Conflict serializability is a **subset** of view serializability.
- Every conflict serializable schedule is also view serializable, but the converse is not true.
- A view serializable schedule may contain **blind writes**, which are write operations that do not depend on any previous read operations.
- A conflict serializable schedule does not contain any blind writes, as they are considered as conflicting operations.
- Conflict serializability is **easier** to check and implement than view serializability.
- View serializability is **more general** and allows more concurrency than conflict serializability.



# Recoverability

Recoverability is the ability of a database system to restore the database to a consistent state after a failure or an abort of a transaction. Recoverability is an important property for ensuring the integrity and consistency of the database.

Some key concepts related to recoverability are:

- **Transaction**: A transaction is a logical unit of work that consists of a sequence of operations on the database. A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- **Commit**: A commit is an operation that marks the successful completion of a transaction and makes its effects permanent in the database.
- **Abort**: An abort is an operation that marks the unsuccessful termination of a transaction and undoes its effects from the database.
- **Schedule**: A schedule is a sequence of operations from a set of transactions that reflects the chronological order of their execution.
- **Serial schedule**: A serial schedule is a schedule in which the operations of each transaction are executed consecutively without any interleaving with other transactions.
- **Concurrent schedule**: A concurrent schedule is a schedule in which the operations of different transactions are interleaved.
- **Conflict**: A conflict is a situation in which two operations from different transactions access the same data item and at least one of them is a write operation.
- **Conflict serializable schedule**: A conflict serializable schedule is a concurrent schedule that is equivalent to some serial schedule, where two schedules are equivalent if they produce the same final state of the database.
- **Recoverable schedule**: A recoverable schedule is a schedule in which, for each pair of transactions T<sub>i</sub> and T<sub>j</sub>, if T<sub>j</sub> reads a data item previously written by T<sub>i</sub>, then the commit operation of T<sub>i</sub> appears before the commit operation of T<sub>j</sub> in the schedule.
- **Cascading abort**: A cascading abort is a situation in which the abort of one transaction causes the abort of other transactions that have read data items written by the aborted transaction.
- **Cascadeless schedule**: A cascadeless schedule is a schedule in which, for each pair of transactions T<sub>i</sub> and T<sub>j</sub>, if T<sub>j</sub> reads a data item previously written by T<sub>i</sub>, then the commit operation of T<sub>i</sub> appears before the read operation of T<sub>j</sub> in the schedule.

Some examples of schedules and their recoverability are:

- Schedule 1: T<sub>1</sub>: R(A), W(A), C; T<sub>2</sub>: R(B), W(B), C
  - This is a serial schedule, and it is recoverable and cascadeless.
- Schedule 2: T<sub>1</sub>: R(A), W(A); T<sub>2</sub>: R(B), W(B), C; T<sub>1</sub>: C
  - This is a concurrent schedule, and it is conflict serializable, recoverable, and cascadeless.
- Schedule 3: T<sub>1</sub>: R(A), W(A); T<sub>2</sub>: R(A), W(A), C; T<sub>1</sub>: C
  - This is a concurrent schedule, and it is conflict serializable and recoverable, but not cascadeless, because T<sub>2</sub> reads A before T<sub>1</sub> commits.
- Schedule 4: T<sub>1</sub>: R(A), W(A); T<sub>2</sub>: R(A), W(A), C; T<sub>1</sub>: A
  - This is a concurrent schedule, and it is not conflict serializable, not recoverable, and not cascadeless, because T<sub>2</sub> commits before T<sub>1</sub>, and T<sub>1</sub> aborts, causing a cascading abort of T<sub>2</sub>.



# Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before it can commit its changes to the database.
- Transaction failures can occur due to various reasons, such as network failures, deadlock, or errors in application logic.
- Transaction failures can leave the database in an inconsistent state, violating the ACID properties of transactions.
- Recovery mechanisms are techniques that can help restore the database to a consistent state after transaction failures.
- Recovery mechanisms are based on the use of logs, which are records of the operations performed by transactions on the database.
- There are two major techniques for recovery from transaction failures: deferred updates and immediate updates.
  - Deferred update: This technique does not physically update the database on disk until a transaction has reached its commit point. Instead, it records the updates in the log and marks the transaction as committed. If a transaction fails before reaching its commit point, no recovery is needed. If a system failure occurs, the recovery manager can redo the committed transactions from the log to bring the database to a consistent state.
  - Immediate update: This technique allows the database to be updated on disk before a transaction reaches its commit point. However, it also records the updates in the log and maintains a before-image and an after-image of each updated data item. A before-image is the value of the data item before the update, and an after-image is the value of the data item after the update. If a transaction fails before reaching its commit point, the recovery manager can undo the effects of the transaction by restoring the before-images from the log. If a system failure occurs, the recovery manager can redo the committed transactions and undo the uncommitted transactions from the log to bring the database to a consistent state.



# Two-phase commit protocol

The two-phase commit protocol (2PC) is a type of atomic commitment protocol (ACP) that ensures the consistency of distributed transactions in a distributed system. A distributed transaction is a transaction that involves multiple processes or sites that may be geographically dispersed. The 2PC protocol coordinates all the processes or sites that participate in a distributed transaction on whether to commit or abort the transaction. The 2PC protocol has two phases: the prepare phase and the commit phase.

## Prepare phase

In the prepare phase, the following steps are performed:

- The coordinator (Ci) is the process or site that initiates the distributed transaction and acts as the leader of the protocol. The coordinator places a log record <Prepare T> on the log record at its site, where T is the transaction identifier.
- The coordinator sends a Prepare T message to all the participants (Pj), which are the processes or sites that execute some operations of the transaction T. The participants are also called cohorts or subordinates.
- Each participant (Pj) receives the Prepare T message and decides whether to vote for commit or abort. If the participant is ready to commit its part of the transaction, it writes a log record <Ready T> on its log and sends a Ready T message to the coordinator. If the participant decides to abort the transaction, it writes a log record <Abort T> on its log, undoes its part of the transaction, and sends an Abort T message to the coordinator.
- The coordinator waits for the votes from all the participants. If the coordinator does not receive a vote from a participant within a timeout period, it assumes that the participant has failed and votes for abort.

## Commit phase

In the commit phase, the following steps are performed:

- The coordinator decides the final outcome of the transaction based on the votes from the participants. If all the participants voted for commit, the coordinator decides to commit the transaction. If any participant voted for abort, or the coordinator itself decided to abort, the coordinator decides to abort the transaction.
- The coordinator writes a log record <Commit T> or <Abort T> on its log, depending on its decision, and sends a Commit T or Abort T message to all the participants.
- Each participant receives the Commit T or Abort T message from the coordinator and acts accordingly. If the participant receives a Commit T message, it writes a log record <Commit T> on its log and commits its part of the transaction. If the participant receives an Abort T message, it writes a log record <Abort T> on its log, undoes its part of the transaction, and releases any locks it may have acquired.
- Each participant sends an Ack T message to the coordinator to acknowledge the completion of the commit or abort operation.
- The coordinator waits for the acknowledgments from all the participants. If the coordinator does not receive an acknowledgment from a participant within a timeout period, it assumes that the participant has failed and resends the Commit T or Abort T message to the participant.
- The coordinator writes a log record <End T> on its log to indicate the end of the transaction.

## Advantages and disadvantages of 2PC

The main advantage of 2PC is that it guarantees the atomicity of distributed transactions, meaning that either all the participants commit or all the participants abort. This ensures the consistency and integrity of the distributed data.

The main disadvantages of 2PC are:

- It is a blocking protocol, meaning that the failure of a single participant or the coordinator blocks the progress of the transaction until the failed process recovers. Moreover, if the coordinator fails, the participants may be left in an uncertain state, waiting for the final decision from the coordinator. This leads to a loss of availability and concurrency in the system.
- It is a costly protocol, meaning that it requires a lot of messages and log writes to coordinate the distributed transaction. The number of messages and log writes is proportional to the number of participants involved in the transaction. This leads to a high latency and overhead in the system.
- It is a rigid protocol, meaning that it does not allow any flexibility or optimization in the execution of the distributed transaction. For example, it does not allow early commits or read-only transactions that do not need to participate in the protocol. This leads to a loss of performance and scalability in the system.



# Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique to restore the database to a consistent state after a failure or crash.
- It uses a log file, which is a sequence of records that store the details of every transaction performed on the database.
- The log file is maintained in a stable storage device, such as a disk or a tape, that can survive a system failure.
- The log file contains the following information for each transaction:
  - Transaction ID: A unique identifier for the transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data Item: The name of the data item affected by the operation.
  - Old Value: The value of the data item before the operation.
  - New Value: The value of the data item after the operation.
- The log file can be used to recover the database in two ways:
  - Undo: This method is used to undo the effects of incomplete or aborted transactions that may have left the database in an inconsistent state. It involves scanning the log file backwards from the end and restoring the old values of the data items that were modified by the transactions.
  - Redo: This method is used to redo the effects of committed transactions that may have not been reflected in the database due to a failure. It involves scanning the log file forwards from the beginning and applying the new values of the data items that were modified by the transactions.
- The log file can also be used to support concurrency control and recovery protocols, such as two-phase locking and two-phase commit, that ensure the atomicity and durability of transactions.



# Checkpoints for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

- A transaction is a logical unit of work that accesses and possibly modifies the contents of a database.
- Transactions access data using read and write operations.
- In order to maintain consistency of data, transactions must satisfy the ACID properties: Atomicity, Consistency, Isolation, and Durability.
- Atomicity ensures that either all the operations of a transaction are reflected in the database or none are.
- Consistency ensures that the database remains in a consistent state before and after the transaction.
- Isolation ensures that the concurrent execution of transactions does not result in a loss of data consistency.
- Durability ensures that the changes made by committed transactions persist in the database even in the event of failures.
- A schedule is a chronological sequence of operations performed by transactions on the database.
- A schedule is serial if the operations of each transaction are executed consecutively without any interleaving operations from other transactions.
- A schedule is serializable if it is equivalent to some serial schedule, meaning that it produces the same final state of the database as the serial schedule.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations, meaning that they access different data items or they are both read operations.
- A schedule is view serializable if it is view equivalent to some serial schedule, meaning that it preserves the same initial and final values of each data item and the same set of transactions that read the initial value of each data item.
- A schedule is recoverable if no transaction commits until all transactions whose changes it has read have committed.
- A schedule is cascadeless if no transaction reads a data item until the last transaction that has written it has committed.
- A schedule is strict if no transaction reads or writes a data item until the last transaction that has written it has committed.
- A concurrency control protocol is a set of rules that govern how transactions access and modify data in the database concurrently.
- The main goal of concurrency control is to ensure serializability and recoverability of schedules while maximizing the degree of concurrency.
- Some common concurrency control protocols are: locking protocols, timestamp-based protocols, validation-based protocols, and multiversion protocols.
- A locking protocol is a concurrency control protocol that uses locks to synchronize the access of transactions to data items in the database.
- A lock is a variable associated with a data item that describes the status of the item with respect to possible operations that can be applied to it.
- There are two types of locks: binary locks and shared/exclusive locks.
- A binary lock can have two states: locked or unlocked. A transaction can access a data item only if it is unlocked and it must lock it before accessing it. A transaction must also unlock the data item after it finishes accessing it.
- A shared/exclusive lock can have three states: unlocked, shared, or exclusive. A transaction can read a data item only if it is unlocked or shared and it must acquire a shared lock before reading it. A transaction can write a data item only if it is unlocked and it must acquire an exclusive lock before writing it. A transaction must also release the lock after it finishes accessing the data item.
- A locking protocol is deadlock-free if it prevents the occurrence of deadlocks, which are situations where two or more transactions are waiting for locks held by each other and none of them can proceed.
- A locking protocol is deadlock-preventable if it imposes some restrictions on how transactions can acquire locks so that at least one of the conditions for deadlock occurrence is violated.
- A locking protocol is deadlock-detectable if it allows deadlocks to occur but provides a mechanism to detect them and abort some transactions to break the deadlock cycle.
- A locking protocol is deadlock-avoidable if it uses some information about the future requests of transactions to decide whether granting a lock can potentially lead to a deadlock or not.
- A timestamp-based protocol is a concurrency control protocol that uses timestamps to order the transactions and ensure serializability.
- A timestamp is a unique identifier assigned to each transaction that reflects its start time or priority.
- There are two types of timestamps: commit-timestamps and logical-timestamps.
- A commit-timestamp is assigned to a transaction when it commits and reflects its actual commit time.
- A logical-timestamp is assigned to a transaction when it starts and reflects its relative priority.
- A timestamp-based protocol ensures that the conflicting operations of transactions are executed in the order of their timestamps.
- A timestamp-based protocol is optimistic if it assumes that conflicts are rare and validates the transactions at commit time to ensure serializability.
- A timestamp-based protocol is pessimistic if it checks for conflicts at the time of each operation and aborts the



# Deadlock Handling

- A deadlock is a situation where a set of transactions are blocked waiting for each other to release locks on the data items they need.
- Deadlocks can occur in a concurrent transaction processing system when transactions use locking for concurrency control.
- Deadlocks are undesirable because they waste system resources and reduce throughput.
- There are three main methods for handling deadlocks: prevention, avoidance, and detection and recovery.

## Deadlock Prevention

- Deadlock prevention is a method that ensures that at least one of the four necessary conditions for deadlock does not hold.
- The four necessary conditions for deadlock are: mutual exclusion, hold and wait, no preemption, and circular wait.
- Deadlock prevention can be achieved by imposing some constraints on how transactions acquire and release locks.
- Some examples of deadlock prevention techniques are:

  - Timestamp ordering: transactions are assigned timestamps when they start, and they must request locks in the order of their timestamps. This prevents circular wait.
  - Conservative locking: transactions must request all the locks they need before they start execution. This prevents hold and wait.
  - Two-phase locking with lock conversion: transactions must acquire all the locks they need in a growing phase, and then release them in a shrinking phase. They can also convert a shared lock to an exclusive lock, or vice versa, in the growing phase. This prevents hold and wait and circular wait.

## Deadlock Avoidance

- Deadlock avoidance is a method that allows transactions to acquire locks dynamically, but checks whether granting a lock request will lead to a potential deadlock.
- Deadlock avoidance requires the system to have some knowledge of the future requests of transactions, such as the set of data items they will access.
- Deadlock avoidance can be achieved by using a deadlock detection algorithm, such as the wait-for graph or the banker's algorithm, to determine whether granting a lock request is safe or unsafe.
- A lock request is safe if it does not create a circular wait among the transactions. A lock request is unsafe if it may create a circular wait in the future.
- If a lock request is safe, the system grants it. If a lock request is unsafe, the system delays it until it becomes safe.

## Deadlock Detection and Recovery

- Deadlock detection and recovery is a method that allows transactions to acquire locks without any constraints, but periodically checks whether a deadlock has occurred.
- Deadlock detection and recovery does not require the system to have any knowledge of the future requests of transactions.
- Deadlock detection and recovery can be achieved by using a deadlock detection algorithm, such as the wait-for graph or the wound-wait scheme, to identify the transactions involved in a deadlock.
- A wait-for graph is a directed graph where the nodes are transactions and the edges are wait-for relationships. An edge from Ti to Tj means that Ti is waiting for Tj to release a lock. A cycle in the wait-for graph indicates a deadlock.
- A wound-wait scheme is a priority-based scheme where transactions are assigned priorities based on their timestamps. A transaction with a higher priority can either wait for or wound a transaction with a lower priority. Wounding means aborting and restarting the transaction with the same timestamp. A deadlock occurs when two or more transactions are waiting for each other and none of them can wound the others.
- Once a deadlock is detected, the system must perform some recovery actions to resolve it. Some examples of recovery actions are:

  - Victim selection: the system chooses one or more transactions to abort and restart. The choice can be based on criteria such as the amount of work done, the number of locks held, the priority, or the estimated remaining time.
  - Rollback: the system restores the database to a consistent state by undoing the effects of the aborted transactions. The rollback can be total, where the transaction is restarted from the beginning, or partial, where the transaction is restarted from a savepoint.
  - Lock release: the system releases the locks held by the aborted transactions and grants them to the waiting transactions. The system must ensure that the lock release does not violate the serializability or the recoverability of the transactions.



## Unit 8 - Concurrency Control Techniques

Concurrency control techniques are methods of managing the simultaneous execution of transactions in a shared database. They aim to preserve the database consistency, enforce the isolation of different transactions, and resolve the conflicts that occur due to the read-write operations of transactions .

The need for concurrency control arises because multiple transactions may access and modify the same data items concurrently, which may lead to data inconsistency, lost updates, uncommitted dependencies, or inconsistent reads. Concurrency control ensures that the transactions are concurrent, accurate, and give correct results without violating data integrity. It also ensures serializability, which means that the effect of executing a set of concurrent transactions is equivalent to some serial execution of the same transactions.

Some of the common concurrency control techniques are :

- **Two-phase locking protocol**: This technique uses locks to secure the permission to read or write a data item. A transaction goes through two phases: a locking (growing) phase, where it acquires locks on desired data items one at a time, and an unlocking (shrinking) phase, where it releases locks on its locked data items one at a time. A transaction cannot acquire any new locks after it releases any lock. This protocol ensures serializability, but may cause deadlocks or starvation .
- **Timestamp ordering protocol**: This technique assigns a unique timestamp to each transaction based on its arrival time. A transaction can read or write a data item only if its timestamp is compatible with the read and write timestamps of the data item, which record the latest transactions that have read or written the data item. This protocol ensures serializability and avoids deadlocks, but may cause aborts or cascading aborts.
- **Multi-version concurrency control**: This technique maintains multiple versions of each data item, each with a different timestamp. A transaction can read the latest version of a data item that is older than its timestamp, and can write a new version of a data item with its timestamp. This protocol ensures serializability and avoids aborts, but may require more storage space and garbage collection.
- **Validation concurrency control**: This technique divides a transaction into three phases: a read phase, where it reads data items but does not write any, a validation phase, where it checks if the transaction can be serialized based on the read and write sets of other transactions, and a write phase, where it writes the data items if the validation succeeds. This protocol ensures serializability and avoids deadlocks, but may cause aborts or delays.

: https://quescol.com/dbms/concurrency-control-techniques
: https://www.geeksforgeeks.org/concurrency-control-techniques/
: https://quescol.com/dbms/need-for-concurrency-control
: https://en.wikipedia.org/wiki/Concurrency_control
: https://www.cs.purdue.edu/homes/bb/cs448_Spring2014/lecture-files/pdf/ch18-Concurrency%20Control%20Techniques.pdf



# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

Some of the problems that concurrency control aims to prevent are:

- Lost update: When two transactions update the same data item and one of them overwrites the other's update.
- Dirty read: When a transaction reads a data item that has been modified by another transaction that has not yet committed or aborted.
- Non-repeatable read: When a transaction reads the same data item twice and gets different values due to another transaction's update.
- Phantom read: When a transaction reads a set of data items that satisfies some condition and gets different results due to another transaction's insertion or deletion of data items that satisfy the same condition.

There are two main types of concurrency control techniques:

- Pessimistic concurrency control: This technique assumes that conflicts are likely to happen and uses locks to prevent them. A lock is a mechanism that grants exclusive access to a data item to a transaction. A transaction must acquire a lock before reading or writing a data item and release it after finishing. There are different types of locks, such as shared locks, exclusive locks, and intention locks, that allow different levels of concurrency.
- Optimistic concurrency control: This technique assumes that conflicts are rare and does not use locks to prevent them. Instead, it uses a validation mechanism to detect and resolve conflicts after they happen. A validation mechanism can be based on timestamps, versions, or validation queries, that allow a transaction to check if its operations are consistent with the current state of the database.

Some of the advantages and disadvantages of these techniques are:

- Pessimistic concurrency control can avoid the overhead of validation and rollback, but it can also cause deadlock, livelock, and reduced concurrency.
- Optimistic concurrency control can avoid the overhead of locking and deadlock, but it can also cause more aborts and retries, and increased complexity.



# Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the integrity of the database is maintained.

One of the most common concurrency control techniques is locking. Locking is an operation that grants a transaction permission to read or write a data item. A lock manager is a subsystem that manages the acquisition and release of locks on data items.

There are different types of locks, such as:

- Binary locks: These locks have two states, locked or unlocked. A transaction can either lock a data item exclusively for writing, or leave it unlocked for reading by any transaction.
- Shared/exclusive locks: These locks have three states, shared, exclusive, or unlocked. A transaction can either lock a data item exclusively for writing, lock it shared for reading, or leave it unlocked. Multiple transactions can lock the same data item shared, but only one transaction can lock it exclusive.
- Read/write locks: These locks are similar to shared/exclusive locks, but they distinguish between read and write operations. A transaction can either lock a data item for reading, lock it for writing, or leave it unlocked. Multiple transactions can lock the same data item for reading, but only one transaction can lock it for writing.
- Intention locks: These locks are used to indicate the intention of a transaction to lock a data item or a group of data items at a lower level of granularity. For example, a transaction can lock a table with an intention to lock a row, or lock a row with an intention to lock a column. Intention locks prevent other transactions from locking the same data item or group of data items at a higher level of granularity.
- Certify locks: These locks are used in multi-version concurrency control techniques, where each transaction works on a local version of the data item and certifies its updates before committing. A transaction must acquire a certify lock on all the data items it has written before committing, and check for any conflicts with other transactions.

Locking techniques can also be classified based on the timing and duration of locking, such as:

- Strict two-phase locking: This is a locking protocol that requires a transaction to acquire all the locks it needs before releasing any lock. A transaction goes through two phases: a growing phase, where it acquires locks, and a shrinking phase, where it releases locks. Strict two-phase locking ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.
- Rigorous two-phase locking: This is a locking protocol that requires a transaction to hold all the locks it has acquired until it commits or aborts. Rigorous two-phase locking is a stricter version of strict two-phase locking, and it also ensures recoverability, which means that a transaction does not read or overwrite the data written by another transaction that has not committed yet.
- Conservative two-phase locking: This is a locking protocol that requires a transaction to acquire all the locks it needs before it starts execution. Conservative two-phase locking avoids deadlock, which is a situation where two or more transactions are waiting for each other to release locks, and none of them can proceed.
- Timestamp-based locking: This is a locking protocol that assigns a unique timestamp to each transaction, and uses the timestamp to order the access to data items. A transaction can lock a data item only if its timestamp is greater than the timestamp of the last transaction that accessed the same data item. Timestamp-based locking avoids deadlock, but it may cause more aborts due to conflicts.



# Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability.
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be either system time or logical counter.
- The basic idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamp to determine the precedence and compatibility of conflicting operations.
- There are two types of time stamping protocols: optimistic and pessimistic.
- Optimistic time stamping protocols assume that conflicts are rare and allow transactions to execute without checking for conflicts until they commit. If a conflict is detected at commit time, the transaction is aborted and restarted with a new timestamp.
- Pessimistic time stamping protocols check for conflicts before executing each operation and abort the transaction immediately if a conflict is detected. The transaction is then restarted with a new timestamp.
- A common pessimistic time stamping protocol is the basic timestamp ordering protocol, which uses two timestamps for each data item: read timestamp (RTS) and write timestamp (WTS). The RTS is the largest timestamp of any transaction that has successfully read the data item, and the WTS is the largest timestamp of any transaction that has successfully written the data item.
- The basic timestamp ordering protocol works as follows:
  - When a transaction Ti issues a read operation on a data item X, the protocol checks if Ti's timestamp is smaller than or equal to the WTS of X. If yes, the read is allowed and the RTS of X is updated to the maximum of Ti's timestamp and the current RTS of X. If no, the read is rejected and Ti is aborted, as it is trying to read a stale value of X that was overwritten by a later transaction.
  - When a transaction Ti issues a write operation on a data item X, the protocol checks if Ti's timestamp is larger than both the RTS and the WTS of X. If yes, the write is allowed and the WTS of X is updated to Ti's timestamp. If no, the write is rejected and Ti is aborted, as it is trying to overwrite a value of X that was read or written by a later transaction.
- The basic timestamp ordering protocol ensures that the transactions are executed in timestamp order and no transaction can read or write a data item that has been modified by a later transaction. This guarantees serializability and avoids the problem of lost update, dirty read, and unrepeatable read. However, it may also cause some transactions to be aborted unnecessarily, such as when a transaction writes a data item that is never read by any other transaction. This is called the problem of cascading aborts, which can be solved by using a modified timestamp ordering protocol that allows some writes to be delayed until commit time.



# Validation Based Protocol in DBMS

- Validation Based Protocol is a concurrency control technique that works on the assumption that interference among transactions is rare and can be detected during validation  .
- It is also called Optimistic Concurrency Control Technique because it does not check for conflicts while the transaction is executing, but only at the end before committing  .
- The protocol consists of three phases for each transaction: read phase, validation phase, and write phase  .
- In the read phase, the transaction reads the data items from the database and stores them in a local buffer. It also records the timestamps of the data items it reads  .
- In the validation phase, the transaction checks whether it can commit without violating the serializability order. It compares its timestamps with those of other transactions that have committed or are in the validation phase  .
- If the transaction passes the validation test, it proceeds to the write phase, where it writes the updated data items from its buffer to the database and commits  .
- If the transaction fails the validation test, it aborts and restarts  .
- The validation test can be based on different criteria, such as start time, end time, or commit time of the transactions  .
- The advantages of validation based protocol are that it avoids locking and deadlock, it allows more concurrency, and it reduces the number of rollbacks  .
- The disadvantages of validation based protocol are that it requires more memory and processing power, it may delay the commit of some transactions, and it may not be suitable for applications that have high interference  .



# Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- There are three types of lock granularity:
  - Fine granularity: It locks the smallest data items, such as records or fields. It has high concurrency but also high locking overhead and high probability of deadlock.
  - Coarse granularity: It locks the largest data items, such as files or tables. It has low concurrency but also low locking overhead and low probability of deadlock.
  - Medium granularity: It locks the intermediate data items, such as pages or blocks. It has moderate concurrency and moderate locking overhead and deadlock probability.
- Multiple granularity locking protocol is a set of rules that governs how transactions can acquire and release locks on different levels of data granularity . It uses a compatibility matrix to determine which lock modes are compatible with each other. The lock modes are :
  - Shared (S): It allows a transaction to read a data item.
  - Exclusive (X): It allows a transaction to read and write a data item.
  - Intention Shared (IS): It indicates that a transaction intends to lock some of the lower level data items in shared mode.
  - Intention Exclusive (IX): It indicates that a transaction intends to lock some of the lower level data items in exclusive mode.
  - Shared and Intention Exclusive (SIX): It indicates that a transaction intends to lock some of the lower level data items in exclusive mode and also locks the current data item in shared mode.
- The compatibility matrix is as follows :

|     | S | X | IS | IX | SIX |
|-----|---|---|----|----|-----|
| S   | Y | N | Y  | N  | N   |
| X   | N | N | N  | N  | N   |
| IS  | Y | N | Y  | Y  | N   |
| IX  | N | N | Y  | Y  | N   |
| SIX | N | N | N  | N  | N   |

- Y means compatible and N means incompatible.
- Multiple granularity locking protocol follows these rules :
  - Follow the compatibility matrix for locking data items.
  - Lock the root of the tree first, in any mode.
  - Node Q can be locked by transaction T in S or IS mode only if the parent of Q is locked by T in IX or IS mode.
  - Node Q can be locked by transaction T in X, SIX, or IX mode only if the parent of Q is locked by T in IX or SIX mode.
  - Transaction T is two-phase, meaning it acquires all the locks before releasing any lock.
  - Transaction T can unlock node Q only if none of Q's descendants are locked by T.
- An example of multiple granularity locking protocol is shown below:

A tree representing the hierarchy of data granularity, with four levels of nodes: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P. A is the root node, B and C are its children, D, E, F, G are the children of B, and H, I, J, K, L, M, N, O, P are the children of C. The nodes represent different data items, such as files, pages, records, or fields.

- Suppose there are two transactions, T1 and T2, that want to access some of the data items in the tree. The sequence of locking and unlocking operations is as follows:

| Transaction | Operation | Lock Mode | Node |
|-------------|-----------|-----------|------|
| T1          | Lock      | IS        | A    |
|



# Multi-version Schemes for Concurrency Control

- Multi-version concurrency control (MVCC) is a technique that allows concurrent access to the database without locking the data.
- MVCC creates multiple versions of each data item and assigns them version numbers.
- Each transaction reads the most recent version of the data item that is compatible with its timestamp.
- Each transaction writes a new version of the data item with an incremented version number.
- MVCC avoids conflicts between read and write operations, as well as between write and write operations.
- MVCC improves the performance and scalability of database applications in a multi-user environment.

## Example of MVCC

- Suppose there are two transactions, T1 and T2, that operate on a data item X.
- Initially, X has a value of 10 and a version number of 1.
- T1 starts at time 1 and reads X. It gets the value 10 and the version number 1.
- T2 starts at time 2 and writes X. It creates a new version of X with a value of 20 and a version number of 2.
- T1 continues and writes X. It creates another new version of X with a value of 30 and a version number of 3.
- T2 reads X. It gets the value 20 and the version number 2, which is the most recent version compatible with its timestamp.
- T1 commits at time 3 and T2 commits at time 4.
- The final state of X is 30 with a version number of 3. The older versions of X are either deleted or archived.



# Recovery with Concurrent Transaction

- Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions executing simultaneously.
- Recovery with concurrent transaction is necessary to ensure the ACID properties of transactions, especially atomicity and durability.
- Recovery with concurrent transaction can be done in the following four ways:
  - Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if locking is used, then the recovery scheme can use the lock table to identify the transactions that were active at the time of failure and undo their effects. If timestamp ordering is used, then the recovery scheme can use the timestamps to order the transactions and redo their effects.
  - Transaction rollback: In this scheme, the recovery scheme can undo the effects of a transaction that has failed or aborted by using the log records. The log records contain the information about the operations performed by the transaction, such as the old and new values of the data items. The recovery scheme can use the log records to restore the old values of the data items and make the transaction appear as if it never executed.
  - Checkpoints: In this scheme, the recovery scheme can reduce the amount of work needed to recover from a failure by periodically taking a snapshot of the database and the log records. A checkpoint is a point in time when the database and the log records are synchronized and consistent. The recovery scheme can use the checkpoint as a starting point for recovery and only process the log records after the checkpoint.
  - Restart recovery: In this scheme, the recovery scheme can handle the case when the system crashes during the recovery process. The recovery scheme can use a special log record called restart to mark the point where the recovery process was interrupted. The recovery scheme can resume the recovery process from the restart point and avoid repeating the work that was already done.



## Unit 9 - Database Security

- Database security is the use of various methods and techniques to protect databases and their components from unauthorized access, modification, or destruction.
- Database security aims to ensure the confidentiality, integrity, and availability of the data and the database system.
- Database security involves the following aspects:
  - Authentication: verifying the identity of the users or applications that access the database.
  - Authorization: granting or denying permissions to perform certain actions on the database objects or data.
  - Encryption: transforming the data into an unreadable form to prevent unauthorized disclosure or tampering.
  - Auditing: recording and reviewing the activities and events that occur on the database system.
  - Backup and recovery: creating and restoring copies of the data and the database system in case of failure or disaster.
- Database security faces various challenges and threats, such as:
  - Data breaches: unauthorized or illegal access to the data by hackers, insiders, or third parties.
  - Data corruption: accidental or intentional modification or deletion of the data by human or system errors, viruses, or malware.
  - Data loss: permanent or temporary unavailability of the data due to hardware failure, natural disaster, or human intervention.
  - Data leakage: unauthorized or inadvertent disclosure of the data to unauthorized parties or channels, such as email, cloud, or social media.
- Database security requires a comprehensive and proactive approach that involves the following steps:
  - Assessing the risks and vulnerabilities of the database system and the data.
  - Implementing the appropriate security controls and policies based on the best practices and standards.
  - Monitoring and testing the effectiveness and performance of the security controls and policies.
  - Updating and improving the security controls and policies based on the changing needs and threats.



# Types of security for the notes of the Unit 9 - Database Security in the subject of Basics of Data Base Management System

- Database security refers to the protection of data and information stored in a database from unauthorized access, modification, or deletion.
- Database security can be classified into three types: physical security, logical security, and administrative security.
- Physical security: This type of security involves the protection of the hardware and software components of the database system from physical damage, theft, or sabotage. Physical security measures include locking the doors, windows, and cabinets where the database system is located, using firewalls, antivirus software, and encryption to prevent unauthorized access or tampering with the data, and having backup and recovery procedures in case of data loss or corruption.
- Logical security: This type of security involves the protection of the data and information stored in the database from unauthorized access, modification, or deletion by users or applications. Logical security measures include defining user roles and privileges, enforcing authentication and authorization mechanisms, implementing access control policies and rules, auditing and monitoring database activities and transactions, and using encryption and hashing techniques to ensure data confidentiality and integrity.
- Administrative security: This type of security involves the management and maintenance of the database system by the database administrator (DBA) or other authorized personnel. Administrative security measures include performing regular backups and restores, applying patches and updates, conducting security audits and assessments, detecting and resolving security breaches and incidents, and educating and training users and staff on database security best practices and policies.



# System Failure

- System failure is a situation where a database system cannot function properly due to some hardware or software malfunction, such as power outage, disk crash, network failure, or software bug.
- System failure can compromise the security of the database by causing data loss, data corruption, data inconsistency, or unauthorized access.
- To prevent or recover from system failure, database systems should implement the following techniques:
  - Backup and recovery: Backup is the process of making copies of the database and log files at regular intervals and storing them in a secure location. Recovery is the process of restoring the database to a consistent state after a failure using the backup and log files .
  - Transaction management: Transaction is a logical unit of work that consists of a sequence of operations on the database. Transaction management is the process of ensuring that transactions are executed in a reliable, consistent, and atomic manner, meaning that either all or none of the operations are performed. Transaction management involves the use of concurrency control and logging mechanisms to prevent or correct data inconsistency and data corruption caused by concurrent or failed transactions.
  - Access control: Access control is the process of granting or denying permissions to users or applications to access or modify data in the database. Access control is based on the principles of authentication, authorization, and encryption. Authentication is the process of verifying the identity of the user or application. Authorization is the process of checking the privileges of the user or application. Encryption is the process of transforming data into an unreadable form to prevent unauthorized access or modification  .
  - Auditing: Auditing is the process of recording and monitoring the activities and events that occur in the database system. Auditing helps to detect and prevent security breaches, such as insider threats, human errors, or exploitation of database software vulnerabilities. Auditing also helps to ensure compliance with security policies and regulations  .

