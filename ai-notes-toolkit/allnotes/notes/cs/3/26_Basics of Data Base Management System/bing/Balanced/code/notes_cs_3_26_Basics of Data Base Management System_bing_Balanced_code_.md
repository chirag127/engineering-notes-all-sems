

## Unit 1 - Introduction

This unit provides an overview of the course and the main concepts of artificial intelligence (AI). It covers the following topics:

- What is AI and why is it important?
- What are the main goals and challenges of AI?
- What are the main branches and applications of AI?
- What are the ethical and social implications of AI?

### What is AI and why is it important?

- AI is the study and design of intelligent agents that can perceive, learn, reason, and act in complex environments.
- AI is important because it can enhance human capabilities, solve difficult problems, and create new opportunities for innovation and progress.
- AI is also important because it raises fundamental questions about the nature of intelligence, knowledge, and morality.

### What are the main goals and challenges of AI?

- The main goals of AI are to create systems that can perform tasks that normally require human intelligence, such as understanding natural language, recognizing faces, playing games, and making decisions.
- The main challenges of AI are to deal with uncertainty, complexity, and diversity of real-world situations, and to ensure that AI systems are reliable, safe, fair, and beneficial for humans and society.

### What are the main branches and applications of AI?

- The main branches of AI are machine learning, natural language processing, computer vision, robotics, and knowledge representation and reasoning.
- Machine learning is the study of algorithms and models that can learn from data and improve their performance over time.
- Natural language processing is the study of methods and systems that can understand and generate natural language, such as speech and text.
- Computer vision is the study of methods and systems that can perceive and interpret visual information, such as images and videos.
- Robotics is the study of methods and systems that can control and interact with physical machines, such as robots and drones.
- Knowledge representation and reasoning is the study of methods and systems that can represent and manipulate knowledge, such as facts, rules, and concepts.
- The main applications of AI are diverse and span across various domains, such as health, education, entertainment, business, and security.

### What are the ethical and social implications of AI?

- AI has ethical and social implications because it can affect human values, rights, and responsibilities, such as privacy, autonomy, fairness, and accountability.
- AI can also have positive and negative impacts on human well-being, such as health, education, employment, and social cohesion.
- AI can also pose risks and challenges, such as bias, discrimination, manipulation, and misuse, that need to be addressed and regulated.
- AI can also create opportunities and benefits, such as innovation, efficiency, and empowerment, that need to be promoted and shared.



### An overview of database management system

A database management system (DBMS) is a software system that enables users to define, create, maintain, and control access to the data stored in a database. A database is a collection of related data that is organized so that it can be easily accessed, managed, and updated. A database can store data of various types, such as text, numbers, images, audio, video, etc.

Some of the main functions of a DBMS are:

- Data definition: A DBMS allows users to specify the structure and properties of the data to be stored in the database, such as data types, constraints, relationships, etc. This is done using a data definition language (DDL), which is a set of commands that define the schema of the database.
- Data manipulation: A DBMS allows users to perform various operations on the data in the database, such as inserting, updating, deleting, querying, sorting, filtering, etc. This is done using a data manipulation language (DML), which is a set of commands that manipulate the data in the database.
- Data security: A DBMS ensures that the data in the database is protected from unauthorized access, modification, or deletion. This is done by implementing various security mechanisms, such as authentication, authorization, encryption, auditing, etc.
- Data integrity: A DBMS ensures that the data in the database is consistent, accurate, and valid. This is done by enforcing various integrity rules, such as primary keys, foreign keys, referential integrity, etc.
- Data backup and recovery: A DBMS ensures that the data in the database is safe from accidental or intentional loss, damage, or corruption. This is done by performing regular backups of the database and providing methods to restore the database in case of a failure or disaster.
- Data concurrency: A DBMS allows multiple users to access and modify the data in the database simultaneously without compromising the data integrity or consistency. This is done by implementing various concurrency control techniques, such as locking, timestamping, serialization, etc.
- Data abstraction: A DBMS hides the low-level details of how the data is stored and accessed from the users and provides a high-level view of the data through a logical data model. This allows users to focus on the data and its meaning rather than the physical implementation of the database.



### Database System vs File System

- A database system is a software application that manages a collection of data and provides various operations to access, manipulate, and organize the data.
- A file system is a software component that manages the storage and retrieval of files on a disk or other storage device.
- Some of the differences between a database system and a file system are:

  - A database system provides a logical view of the data, whereas a file system provides a physical view of the data.
  - A database system supports complex queries and transactions, whereas a file system supports simple read and write operations.
  - A database system ensures data consistency, integrity, and security, whereas a file system does not provide these features.
  - A database system can handle concurrent access and recovery from failures, whereas a file system may not handle these situations well.
  - A database system can store different types of data, such as structured, semi-structured, or unstructured data, whereas a file system can only store files of a specific format.



### Database System Concepts and Architecture

- A database system is a software system that manages and manipulates data stored in a database.
- A database system consists of several components, such as:
  - Database: a collection of related data that represents some aspects of the real world.
  - Database management system (DBMS): a software package that provides the functionality to create, maintain, and manipulate databases.
  - Database application: a program that interacts with the database system to perform specific tasks, such as querying, updating, or reporting data.
  - Database users: the people or organizations that use the database system for various purposes, such as data entry, analysis, or decision making.
- A database system can have different architectures, depending on how the components are distributed and organized across different computers or devices.
  - Centralized architecture: a single computer hosts the database, the DBMS, and the database applications. All database users access the database system through the same computer.
  - Client-server architecture: the database and the DBMS are hosted on a server computer, while the database applications are hosted on client computers. The clients communicate with the server through a network to access the database system.
  - Distributed architecture: the database and the DBMS are partitioned and distributed across multiple computers, which may be geographically dispersed. The database applications can access the database system through a network, which may involve multiple hops or intermediaries.
- A database system can also have different levels of abstraction, depending on how the data is structured and represented.
  - External level: the view of the data that is presented to the database users, which may vary depending on their needs and preferences.
  - Conceptual level: the logical structure of the data that is independent of the physical storage and implementation details.
  - Internal level: the physical representation of the data that is dependent on the hardware and software characteristics of the database system.
- A database system can also have different models, depending on how the data is organized and manipulated.
  - Relational model: the data is organized as tables, which consist of rows and columns. The tables can be linked by common attributes, which form relationships. The data can be manipulated using a declarative query language, such as SQL.
  - Hierarchical model: the data is organized as a tree, which consists of nodes and edges. The nodes represent records, and the edges represent parent-child relationships. The data can be manipulated using a navigational query language, such as DL/I.
  - Network model: the data is organized as a graph, which consists of nodes and edges. The nodes represent records, and the edges represent arbitrary relationships. The data can be manipulated using a navigational query language, such as CODASYL.
  - Object-oriented model: the data is organized as objects, which consist of attributes and methods. The objects can be grouped into classes, which form inheritance hierarchies. The data can be manipulated using an object-oriented query language, such as OQL.



# Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data abstraction also supports data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in a database system: physical level, logical level, and view level.

## Physical Level

- The physical level is the lowest level of data abstraction. It describes how the data is physically stored in the storage devices and the access methods used to retrieve and update the data.
- The physical level is also called the internal level or the implementation level.
- The physical level is concerned with the data structures, file organizations, indexes, hashing, compression, encryption, and other techniques that optimize the performance and security of the database system.
- The physical level is usually hidden from the users and applications, and only the database administrator (DBA) can access and modify it.
- The physical level is defined by the internal schema, which is a description of the physical representation of the data and the access methods.

## Logical Level

- The logical level is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data.
- The logical level is also called the conceptual level or the data model level.
- The logical level is independent of the physical level, meaning that the logical structure of the data does not depend on how the data is stored or accessed.
- The logical level is the level that most users and applications interact with, as it provides a logical view of the data that is meaningful and understandable.
- The logical level is defined by the conceptual schema, which is a description of the data and the constraints on the data using a data model, such as the entity-relationship (ER) model or the relational model.

## View Level

- The view level is the highest level of data abstraction. It describes how the data is seen by different users and applications that access the database.
- The view level is also called the external level or the user level.
- The view level is independent of both the physical and the logical levels, meaning that the view of the data does not depend on how the data is stored or organized.
- The view level allows different users and applications to have different views of the same data, depending on their needs and preferences.
- The view level is defined by the external schema, which is a description of a subset of the data and the operations on the data using a query language, such as SQL or QBE.



### Data Models

A data model is a type of data abstraction that determines the logical structure of a database. It defines how data is connected to each other and how they are processed and stored inside the system. Data models are fundamental entities to introduce abstraction in a DBMS.

There are different types of data models used for understanding the structure of the database. Some of the common data models are:

- **Relational data model**: This type of model designs the data in the form of rows and columns within a table. Each row represents a record and each column represents an attribute. The tables are also called relations and they are linked by using primary and foreign keys. The relational model is the most popular and widely used data model in database systems .
- **Entity-relationship data model**: An ER model is the logical representation of data as objects and relationships among them. An object is called an entity and a relationship is an association between two or more entities. The ER model uses graphical symbols such as rectangles, diamonds and lines to depict the entities, relationships and attributes. The ER model is useful for designing and documenting the conceptual schema of a database .
- **Object-based data model**: An extension of the ER model with notions of functions, encapsulation, and object identity, as well. An object is a collection of data and methods that operate on the data. An object can inherit the properties and behaviors of another object. The object-based model supports complex data types and user-defined data types. Some examples of object-based models are object-oriented model, object-relational model and semantic data model .
- **Hierarchical data model**: This type of model represents one-to-many relationships in a treelike format. In this model, each record has only one parent record and zero or more child records. The records are also called nodes and the links between them are called branches. The hierarchical model is simple and efficient for accessing data, but it is rigid and does not support many-to-many relationships .
- **Network data model**: This type of model represents many-to-many relationships in a graph-like format. In this model, each record can have multiple parent and child records. The records are also called entities and the links between them are called sets. The network model is flexible and supports complex data structures, but it is difficult to maintain and query .
- **Dimensional data model**: This type of model is used for data analysis and reporting purposes. It organizes the data into facts and dimensions. A fact is a measure of interest, such as sales or revenue, and a dimension is an attribute that describes the fact, such as time, location or product. The dimensional model uses a star or snowflake schema to represent the data in a cube-like format. The dimensional model is easy to understand and query, but it may not capture all the details and relationships of the data .
- **Graph data model**: This type of model represents data as nodes and edges in a graph-like format. A node is an entity that has properties and an edge is a relationship that has a direction and a label. The graph model can capture complex and dynamic data structures, such as social networks, recommendation systems or fraud detection. The graph model is flexible and expressive, but it may not scale well for large and distributed data .



### Schema and Instances for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- A database is a collection of organized data that can be stored and accessed by a software program called a database management system (DBMS).
- A database schema is an abstract design that represents the storage of data in a database. It describes both the organization of data and the relationships between tables in a given database.
- A database instance is a sample of data from a database at a single moment in time. It is the data stored in a database at a particular state.
- A schema is the initial state of the database where the database is designed at first. An instance is a state when data is loaded into the database or when any change is acquired by the corresponding database.
- A schema is a structural view of the database, while the instance is the content of the database.
- A schema can be represented by a diagram or a text, while an instance can be represented by a table or a record.
- A schema is fixed and does not change frequently, while an instance is dynamic and changes constantly.
- A schema defines the constraints and rules for the data, while an instance follows the constraints and rules defined by the schema.
- A schema can have multiple instances, but an instance can have only one schema.
- A schema can be classified into different levels, such as physical schema, logical schema, and view schema, depending on the level of abstraction and the users' perspective. An instance can be classified into different types, such as full instance, partial instance, and empty instance, depending on the amount of data and the completeness of the data.



### Data Independence in DBMS

Data independence in DBMS is the ability to change the schema of the database at one level without affecting the schema at the next higher level. Schema is the logical structure of the database, such as tables, columns, views, etc. Data independence helps to improve the maintainability and flexibility of the database system.

There are two types of data independence in DBMS:

- **Physical data independence**: This is the ability to modify the physical schema of the database without affecting the logical schema or the external schema. For example, changing the storage structure, file organization, indexing strategy, etc. Physical data independence is usually provided by most database systems and file environments.
- **Logical data independence**: This is the ability to modify the logical schema of the database without affecting the external schema or the user applications. For example, changing the tables, columns, views, constraints, etc. Logical data independence is more difficult to achieve than physical data independence, as it requires the DBMS to provide a mapping mechanism between the logical schema and the external schema.

Some benefits of data independence are:

- It allows the database administrator to change the database structure as per the requirements without affecting the existing applications.
- It allows the application developers to focus on the functionality and presentation of the data without worrying about the physical or logical details of the data storage.
- It allows the users to access the data in a consistent and abstract manner without knowing the underlying implementation of the data.



### Database Languages and Interfaces

- Database languages are the means of communication between the users and the database management system (DBMS).
- Database interfaces are the tools or applications that allow the users to interact with the database using the database languages.
- There are four main types of database languages: data definition language (DDL), data manipulation language (DML), data control language (DCL), and transaction control language (TCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, etc.
- DML is used to manipulate the data stored in the database, such as inserting, updating, deleting, or querying data.
- DCL is used to control the access and security of the database, such as granting or revoking permissions, roles, or privileges to users or groups.
- TCL is used to manage the transactions that affect the database, such as committing, rolling back, or saving changes.
- There are different types of database interfaces for different categories of users, such as:
  - Menu-based interfaces for web clients or browsing: These interfaces present the user with lists of options (called menus) that lead the user through the database operations. They are suitable for novice or casual users who do not need to know the database languages or commands.
  - Forms-based interfaces: These interfaces allow the user to fill out forms with fields that correspond to the attributes of the database tables or views. They are useful for data entry or retrieval tasks that involve a single record or a small set of records.
  - Graphical user interface (GUI): These interfaces use graphical elements such as icons, buttons, menus, windows, etc. to represent the database objects and operations. They are user-friendly and intuitive for most users, and can support complex queries and operations.
  - Natural language interface: These interfaces allow the user to interact with the database using natural language sentences or queries. They are convenient and easy to use, but they may not be precise or accurate enough for some applications.



### Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects in a database.
- Database objects include tables, indexes, views, schemas, sequences, aliases, locations, and users .
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas.
- DDL commands are predefined and have a specific syntax that must be followed.
- Some common DDL commands are CREATE, ALTER, DROP, RENAME, and TRUNCATE.
- DDL commands can be executed interactively or through a script file.
- DDL commands are not transactional, meaning they cannot be rolled back or committed.
- DDL commands affect the metadata of the database, which is the data about the data.
- DDL commands are used to define the logical structure of the data and the relationships among the data.
- DDL commands are independent of the data manipulation language (DML), which is used to insert, update, delete, and query the data in the database.



### DML for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

- DML stands for Data Manipulation Language, which is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views  .
- The main DML statements are SELECT, INSERT, DELETE, and UPDATE  .
- SELECT statement is used to retrieve data from one or more tables or views based on certain criteria .
- INSERT statement is used to add new rows of data into a table or view .
- DELETE statement is used to remove existing rows of data from a table or view .
- UPDATE statement is used to modify existing rows of data in a table or view .
- DML statements can be executed interactively or embedded in a program.
- DML statements can also be affected by DML triggers, which are special types of stored procedures that automatically take effect when a DML event occurs on a table or view.
- DML triggers can be used to enforce business rules, audit data changes, or perform other actions based on the data manipulation.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of overall database structure for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System. Here is the content I have generated:

```markdown
# Unit 1 - Introduction

## What is a Database?

- A database is a collection of related data that is organized and stored in a structured way.
- A database can store various types of data, such as text, numbers, images, audio, video, etc.
- A database can be accessed and manipulated by using a software application called a database management system (DBMS).

## What is a Database Management System (DBMS)?

- A DBMS is a software system that provides the functionality to create, maintain, and manipulate databases.
- A DBMS can perform various operations on the data, such as insertion, deletion, update, retrieval, sorting, filtering, etc.
- A DBMS can also provide security, concurrency, backup, recovery, and integrity features for the databases.
- A DBMS can support different types of databases, such as relational, hierarchical, network, object-oriented, etc.

## What is a Database Model?

- A database model is a logical representation of the structure and organization of the data in a database.
- A database model defines the rules and constraints for the data, such as the data types, the relationships, the keys, the integrity, etc.
- A database model can be represented by using a diagram or a notation, such as the entity-relationship (ER) model, the relational model, the object model, etc.

## What is a Database Schema?

- A database schema is a description of the structure and organization of the data in a database, based on a specific database model.
- A database schema specifies the names and attributes of the entities, the relationships and constraints among them, and the operations that can be performed on them.
- A database schema can be expressed by using a formal language, such as the structured query language (SQL), the object definition language (ODL), etc.

## What is a Database Instance?

- A database instance is a snapshot of the data in a database at a given point in time.
- A database instance reflects the current state and content of the data in a database.
- A database instance can change over time as the data is inserted, deleted, updated, or retrieved by the DBMS or the users.
```



### Transaction Management

Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations. It is a transaction is a program unit whose execution may or may not change the contents of a database. Not managing concurrent access may create issues like hardware failure and system crashes.

A transaction symbolizes a unit of work, performed within a database management system (or similar system) against a database, that is treated in a coherent and reliable way independent of other transactions. A transaction generally represents any change in a database.

Some of the topics covered in this unit are:

- Transaction states
- Transaction properties
- Transaction log
- Concurrency control
- Locking mechanisms
- Deadlocks
- Serializability
- Recovery techniques

#### Transaction States

There are various database transaction states as follows:

- Active state - this is the state in which the transaction is being executed and database modifications are being made.
- Partially committed state - this is the state in which the transaction has executed its final statement but the changes are not yet permanent in the database.
- Committed state - this is the state in which the transaction has completed successfully and the changes are permanent in the database.
- Failed state - this is the state in which the transaction has encountered an error and cannot continue execution.
- Aborted state - this is the state in which the transaction has been rolled back and the database is restored to its previous state before the transaction started.

#### Transaction Properties

A transaction must satisfy four properties, known as ACID properties, to ensure data integrity and consistency:

- Atomicity - this means that either all the operations in a transaction are executed or none of them are. A transaction is an indivisible unit of work.
- Consistency - this means that a transaction must preserve the consistency rules of the database, such as referential integrity, domain constraints, etc. A transaction must not leave the database in an inconsistent state.
- Isolation - this means that a transaction must not interfere with other concurrent transactions. A transaction must execute as if it is the only one in the system.
- Durability - this means that the changes made by a transaction must persist even in the event of system failures. A transaction must not lose its effects due to power outages, crashes, etc.

#### Transaction Log

Every SQL Server database has a transaction log that records all transactions and the database modifications made by each transaction. The transaction log is a critical component of the database. If there is a system failure, you will need that log to bring your database back to a consistent state.

The transaction log contains the following information:

- The start and end of each transaction
- The names of the data items that are accessed and modified by each transaction
- The old and new values of the data items that are updated by each transaction
- The commit or rollback operations of each transaction

The transaction log is used for two main purposes:

- Recovery - the transaction log is used to undo the effects of incomplete transactions and redo the effects of committed transactions in case of a system failure. This ensures that the ACID properties of transactions are maintained.
- Auditing - the transaction log is used to track the history of transactions and the changes they made to the database. This can help in detecting unauthorized access, fraud, or errors.

#### Concurrency Control

Concurrency control is the process of managing simultaneous access to the database by multiple transactions. Concurrency control is necessary to ensure the isolation and consistency properties of transactions. Without concurrency control, concurrent transactions may cause the following problems:

- Lost update - this occurs when two transactions update the same data item and one of them overwrites the changes of the other without knowing it.
- Dirty read - this occurs when one transaction reads a data item that has been modified by another transaction but not yet committed. The read value may be incorrect or inconsistent.
- Unrepeatable read - this occurs when one transaction reads the same data item twice and gets different values because another transaction has updated it in between.
- Phantom read - this occurs when one transaction reads a set of data items that satisfy some condition and another transaction inserts or deletes some data items that affect the condition. The read set may change unexpectedly.

There are various techniques for concurrency control, such as:

- Locking - this is the most common technique, which involves granting exclusive or shared access to data items based on the operations performed by transactions. Locking can prevent lost updates, dirty reads, and unrepeatable reads, but may cause deadlocks or reduced concurrency.
- Timestamping - this is a technique that assigns a unique timestamp



### Storage Management for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

- Storage management is the method by which organizations ensure data integrity, access, policy/regulation compliance, and effective storage resource use.
- Storage management involves developing a plan to provision, configure, back up, and monitor data storage infrastructure to prevent data loss, performance slowdowns, and access problems.
- Storage management can offer numerous advantages, such as reducing costs, improving performance, enhancing security, and enabling data analysis.
- Storage management can also pose some challenges, such as complexity, scalability, compatibility, and compliance.
- A DBMS must store data persistently in files or datasets of some sort. Depending on the DBMS, table spaces and index spaces each may require one, or possibly more, files to store the actual data.
- A DBMS can use different types of data storage devices, such as primary, secondary, and tertiary devices.
- Primary devices are the fastest and most expensive devices, such as the CPU's main memory, registers, and cache memory.
- Secondary devices are slower and cheaper devices, such as hard disks, optical disks, and flash drives.
- Tertiary devices are the slowest and cheapest devices, such as magnetic tapes, CDs, and DVDs.
- A DBMS can use different methods and services for data storage management, such as storage resource management software, consolidation of systems, multiprotocol storage arrays, storage tiers, strategic SSD deployment, hybrid cloud, scale-out systems, archive storage of infrequently accessed data, and elimination of redundant data.
- A DBMS can also use different techniques and algorithms for data storage management, such as hashing, indexing, compression, encryption, replication, and deduplication.



### Database Users and Administrator

Database users and administrator are the people who are accessing or working with the database. The primary aim of the database management system (DBMS) is to store the data or information and retrieve it whenever it is needed by the database users. There are different types of database users and administrator, depending on their interaction with the database and their roles and responsibilities. Here are some of the common types of database users and administrator:

- **Native Users**: These are the database users who are communicating with the database through an already written program. For example, when a student logs in to an online learning platform, the program will query the database to retrieve the student's profile, courses, and grades. The student is a native user who does not directly interact with the database, but uses the program as an interface.
- **Application Programmers**: These are the software developers and programming professionals who write the programs that access the database. They use a programming language such as SQL, Java, Python, or C# to create, update, delete, and query the data in the database. They also design and implement the user interface, the business logic, and the security features of the application.
- **Casual Users**: These are the database users who occasionally access the database, but do not have a fixed or regular pattern of queries. They use a general-purpose query language such as SQL to retrieve the data they need. For example, a manager may want to generate a report on the sales performance of a product or a region, and use a query tool to extract the relevant data from the database.
- **Sophisticated Users**: These are the database users who have a deep knowledge of the database structure and content, and can formulate complex queries to access the data. They may use a specialized query language or a programming language to manipulate the data in the database. For example, a data analyst may use a statistical software or a machine learning framework to perform data analysis and visualization on the database.
- **Database Administrator (DBA)**: This is a person or a team who defines the schema and also controls the three levels of the database: the physical level, the logical level, and the view level. The DBA is responsible for creating, maintaining, and securing the database. The DBA also monitors the performance, backup, recovery, and availability of the database. The DBA has full control of the database and can grant or revoke access privileges to other database users. The DBA's account is called a superuser account.



## Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is the process of designing and documenting the structure and relationships of data in a database.
- The Entity Relationship Model (ER Model) is a graphical notation for representing data models using entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified uniquely and has some properties of interest.
- An attribute is a property or characteristic of an entity that describes some aspect of the entity.
- A relationship is an association or link between two or more entities that expresses some semantic meaning or constraint.
- The ER Model consists of three basic components: entity sets, relationship sets, and attributes.
- An entity set is a collection of entities of the same type that share the same attributes.
- A relationship set is a collection of relationships of the same type that involve the same entity sets.
- An attribute can be associated with either an entity set or a relationship set, depending on whether it describes the entity or the relationship.
- The ER Model can be represented using a diagram called an Entity Relationship Diagram (ERD), which uses symbols and labels to depict the entity sets, relationship sets, and attributes.
- The ERD can also show additional information such as cardinality ratios, participation constraints, and keys, which specify the constraints and rules that govern the data model.
- A cardinality ratio is the number of entities that can be associated with another entity in a relationship set.
- A participation constraint is the degree to which an entity set is involved in a relationship set, either total (mandatory) or partial (optional).
- A key is a set of one or more attributes that can uniquely identify an entity in an entity set.
- The ER Model can be used to design and validate the data model of a database before implementing it in a specific database management system (DBMS).
- The ER Model can also be used to communicate and document the data model to various stakeholders, such as developers, users, and managers.



### ER model concepts

The ER model is a conceptual data model that describes the entities, attributes, and relationships in a database. It is used to design and represent the logical structure of a database. The ER model consists of the following basic concepts  :

- **Entity**: An entity is a real-world object or thing that can be identified uniquely. For example, a student, a course, a book, etc. An entity has a set of properties or attributes that describe its characteristics. For example, a student entity may have attributes like name, roll number, age, etc.
- **Entity type**: An entity type is a collection or set of entities that share the same attributes. For example, student is an entity type that contains all the student entities in a database. An entity type has an independent existence within a database.
- **Entity set**: An entity set is a subset of an entity type that contains the entities that participate in a particular relationship. For example, enrolled is an entity set that contains the student entities that are enrolled in a course.
- **Attribute**: An attribute is a property or characteristic of an entity or a relationship. For example, name, age, roll number, etc. are attributes of a student entity. An attribute can have a single value or multiple values for an entity. For example, a student can have one or more phone numbers.
- **Attribute domain**: An attribute domain is a set of possible values for an attribute. For example, the domain of the age attribute can be the set of positive integers. An attribute domain defines the data type and constraints of an attribute.
- **Key attribute**: A key attribute is an attribute that uniquely identifies an entity in an entity set. For example, roll number is a key attribute of a student entity. A key attribute can be a single attribute or a combination of attributes. For example, a book entity can have a key attribute composed of ISBN and edition.
- **Relationship**: A relationship is an association or link between two or more entities. For example, a student entity and a course entity can have a relationship called enrolled. A relationship can have attributes that describe its properties. For example, the enrolled relationship can have an attribute called grade that stores the grade of a student in a course.
- **Relationship type**: A relationship type is a collection or set of relationships that share the same attributes and entities. For example, enrolled is a relationship type that contains all the enrolled relationships in a database. A relationship type is represented by a diamond and connecting the entities with lines.
- **Relationship set**: A relationship set is a subset of a relationship type that contains the relationships that participate in a particular entity set. For example, the following relationship set depicts S1 as enrolled in C2, S2 is enrolled in C1, and S3 is enrolled in C3:

relationship set

- **Degree of a relationship**: The degree of a relationship is the number of entities that participate in a relationship. For example, the enrolled relationship has a degree of two, as it involves two entities: student and course. A relationship can have a degree of one (unary), two (binary), three (ternary), or more (n-ary).
- **Cardinality of a relationship**: The cardinality of a relationship is the number of occurrences of one entity that are associated with one occurrence of another entity. For example, the cardinality of the enrolled relationship can be one-to-many, as one student can enroll in many courses, but one course can have only one student. A relationship can have a cardinality of one-to-one, one-to-many, many-to-one, or many-to-many.
- **Participation of an entity in a relationship**: The participation of an entity in a relationship is the extent to which the entity is involved in the relationship. For example, the participation of a student entity in the enrolled relationship can be total or partial, depending on whether every student must enroll in at least one course or not. A participation can be total (mandatory) or partial (optional).
- **Weak entity**: A weak entity is an entity that does not have a key attribute of its own, but depends on another entity (called the identifying or owner entity) for its identification. For example, a section entity can be a weak entity, as it does not have a key attribute, but depends on the course entity for its identification. A weak entity is represented by a double rectangle.
- **Identifying relationship**:



# Notation for ER Diagram

An ER diagram is a graphical representation of the entities and their relationships in a database. It helps to design and understand the logical structure of the data. There are different notations and symbols used to create an ER diagram, depending on the preference and purpose of the modeler. Some of the common notations and symbols are:

- **Crow's foot notation**: This is the most intuitive and widely used notation for ER diagrams. It uses different shapes and lines to indicate the entities, attributes, and relationships. The main symbols are:

  - **Entity**: A rectangle represents an entity, which is a real-world object or concept that can be identified and stored in the database. For example, a student, a course, or a department can be entities. The name of the entity is written inside the rectangle.

  - **Attribute**: An oval represents an attribute, which is a property or characteristic of an entity. For example, a student entity can have attributes such as name, ID, or major. The name of the attribute is written inside the oval. There are different types of attributes, such as:

    - **Simple attribute**: An attribute that cannot be divided into smaller parts. For example, name or ID.

    - **Composite attribute**: An attribute that can be divided into smaller parts. For example, address can be composed of street, city, and state.

    - **Single-valued attribute**: An attribute that has only one value for each entity. For example, ID or major.

    - **Multi-valued attribute**: An attribute that can have more than one value for each entity. For example, phone number or email. A multi-valued attribute is shown by a double oval.

    - **Derived attribute**: An attribute that can be derived from other attributes. For example, age can be derived from date of birth. A derived attribute is shown by a dashed oval.

  - **Relationship**: A diamond represents a relationship, which is an association or interaction between two or more entities. For example, a student can enroll in a course, or a department can offer a course. The name of the relationship is written inside the diamond. There are different types of relationships, such as:

    - **One-to-one relationship**: A relationship where each entity in one set is associated with only one entity in another set. For example, a student can have only one advisor, and an advisor can advise only one student. A one-to-one relationship is shown by a single line connecting the entities.

    - **One-to-many relationship**: A relationship where each entity in one set is associated with many entities in another set. For example, a department can offer many courses, but a course can belong to only one department. A one-to-many relationship is shown by a single line connecting the entity in the one side, and a crow's foot (three prongs) connecting the entity in the many side.

    - **Many-to-many relationship**: A relationship where each entity in one set is associated with many entities in another set. For example, a student can enroll in many courses, and a course can have many students. A many-to-many relationship is shown by a crow's foot connecting both entities.

  - **Cardinality**: The cardinality of a relationship specifies the number of instances of one entity that can be associated with each instance of another entity. For example, a student can enroll in zero or more courses, and a course can have zero or more students. The cardinality of a relationship is shown by placing a number or a symbol next to the line connecting the entities. Some of the common symbols are:

    - **0**: Zero or optional. For example, a student may or may not enroll in a course.

    - **1**: One or mandatory. For example, a course must belong to one department.

    - **N**: Many or unspecified. For example, a student can enroll in many courses.

    - **M**: A specific number. For example, a student can enroll in at most four courses.

- **Other notations**: There are some other notations that are used for ER diagrams, such as arrow notation, Barker's notation, UML notation, etc. They have different symbols and conventions to represent the entities, attributes, and relationships. However, they all convey the same information and can be converted to each other. The choice of notation depends on the preference and purpose of the modeler.



### Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are also known as the cardinality ratio. They express the number of entities to which another entity can be related via a relationship set.
- Mapping constraints are most useful in describing the relationship sets that involve more than two entity sets.
- There are two types of mapping constraints in the entity relationship model:
  - Mapping cardinality or cardinality ratio: It specifies the maximum number of relationship instances that an entity can participate in. There are four possible mapping cardinalities for binary relationship sets :
    - One to one: Each entity in the relationship set can be related to at most one entity of the other set. For example, a person can have at most one passport, and a passport belongs to at most one person.
    - One to many: An entity in one set can be related to many entities of the other set, but not vice versa. For example, a department can have many employees, but an employee belongs to at most one department.
    - Many to one: An entity in one set can be related to at most one entity of the other set, but not vice versa. For example, a course can have at most one instructor, but an instructor can teach many courses.
    - Many to many: An entity in one set can be related to many entities of the other set, and vice versa. For example, a student can enroll in many courses, and a course can have many students.
  - Participation constraints: They specify whether the existence of an entity depends on its being related to another entity via the relationship set. There are two types of participation constraints:
    - Total participation: Every entity in the entity set must participate in at least one relationship in the relationship set. For example, every employee must work for a department.
    - Partial participation: Some entities in the entity set may not participate in any relationship in the relationship set. For example, some instructors may not teach any course.



### Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical and conceptual tool for data modeling using entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified and distinguished from others. Examples of entities are students, courses, employees, products, etc.
- An attribute is a property or characteristic of an entity that describes some aspect of it. Examples of attributes are name, age, address, salary, etc.
- A relationship is an association or connection between two or more entities that expresses some business rule or logic. Examples of relationships are enrolls, teaches, works for, buys, etc.
- An Entity Relationship Diagram (ERD) is a diagram that shows the entities, attributes, and relationships in a database using symbols and connectors.
- The symbols and connectors used in an ERD are:

  - A rectangle represents an entity. The name of the entity is written inside the rectangle.
  - An oval represents an attribute. The name of the attribute is written inside the oval. An attribute is connected to the entity it belongs to by a line.
  - A diamond represents a relationship. The name of the relationship is written inside the diamond. A relationship is connected to the entities it involves by a line.
  - A line represents a connection between an entity and an attribute, or between an entity and a relationship. The line can have different cardinalities and participation constraints to indicate the degree and optionality of the connection.
  - A cardinality is a number or a symbol that shows how many instances of one entity can be associated with one instance of another entity in a relationship. The cardinalities are:

    - One-to-one (1:1): One instance of entity A can be associated with at most one instance of entity B, and vice versa. A single line is used to represent this cardinality.
    - One-to-many (1:N): One instance of entity A can be associated with zero or more instances of entity B, but one instance of entity B can be associated with at most one instance of entity A. A single line with a crow's foot at the end is used to represent this cardinality.
    - Many-to-one (N:1): One instance of entity B can be associated with zero or more instances of entity A, but one instance of entity A can be associated with at most one instance of entity B. A single line with a crow's foot at the start is used to represent this cardinality.
    - Many-to-many (N:M): One instance of entity A can be associated with zero or more instances of entity B, and vice versa. A double line with a crow's foot at both ends is used to represent this cardinality.

  - A participation constraint is a symbol that shows whether the participation of an entity in a relationship is mandatory or optional. The participation constraints are:

    - Total participation: Every instance of an entity must participate in the relationship. A double line is used to represent this constraint.
    - Partial participation: Some instances of an entity may or may not participate in the relationship. A single line is used to represent this constraint.

- An example of an ERD is:

ERD example

- The ERD above shows the entities Student, Course, and Instructor, and their attributes and relationships. The relationship Enrolls has a many-to-many cardinality between Student and Course, and a total participation of Student and a partial participation of Course. The relationship Teaches has a one-to-many cardinality between Instructor and Course, and a total participation of both entities. The attribute ID is underlined for each entity, which means it is a key attribute that uniquely identifies each instance of the entity.



### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- A super key can also be NULL, meaning that it does not have any value.
- A table can have more than one super key, but only one primary key, which is a candidate key chosen by the database designer .
- A super key can be used to enforce referential integrity, which means that the values of a foreign key in one table must match the values of a primary key in another table.

Some examples of super keys are:

- In a table of students, the attributes {student_id, name, email} form a super key, because they can uniquely identify each student. However, this super key is not minimal, because {student_id} alone can also uniquely identify each student. Therefore, {student_id} is a candidate key, and {student_id, name, email} is a super key that contains the candidate key.
- In a table of employees, the attributes {employee_id, name, department, salary} form a super key, because they can uniquely identify each employee. However, this super key is not minimal, because {employee_id} alone can also uniquely identify each employee. Therefore, {employee_id} is a candidate key, and {employee_id, name, department, salary} is a super key that contains the candidate key.
- In a table of books, the attributes {ISBN, title, author, publisher, year} form a super key, because they can uniquely identify each book. However, this super key is not minimal, because {ISBN} alone can also uniquely identify each book. Therefore, {ISBN} is a candidate key, and {ISBN, title, author, publisher, year} is a super key that contains the candidate key.



### Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a database  .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and removing any attribute from it would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier of the relation .
- The other candidate keys that are not chosen as the primary key are called alternate keys or unique keys, and they can also enforce uniqueness constraints on the relation.
- To find the candidate keys of a relation, one can use the following steps:
  - Identify all the attributes that are unique by themselves, and mark them as candidate keys.
  - Identify all the attributes that are part of a functional dependency, where they determine the values of other attributes, and mark them as candidate keys.
  - Identify all the combinations of two or more attributes that are unique together, and mark them as candidate keys.
  - Eliminate any candidate key that is a proper subset of another candidate key, as it is not minimal.
  - Choose one of the remaining candidate keys as the primary key, and label the others as alternate keys.



### Primary Key

- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key must satisfy the following properties:
  - It must not contain null values.
  - It must be unique for each row in the table.
  - It must be minimal, meaning that no subset of the columns can also uniquely identify each row.
- A primary key can be chosen from the attributes of the entity type that the table represents, or it can be generated by the database system as a surrogate key.
- A primary key can be used to reference the table from other tables or queries, using a foreign key.
- A primary key can be specified using the `PRIMARY KEY` constraint in the `CREATE TABLE` or `ALTER TABLE` statement.



# Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model

- Generalization is a bottom-up approach in which two or more lower level entities (subclasses) combine to form a higher level entity (superclass)   .
- In generalization, the superclass inherits the common properties and relationships of the subclasses   .
- Generalization is used to represent a hierarchy of entities that share some attributes or operations  .
- Generalization is depicted by a triangle with a horizontal line connecting the subclasses to the superclass   .
- An example of generalization is the entity Person, which can be generalized from the entities Student and Employee, as shown below:

```
    Person
    /    \
Student  Employee
```

- In this example, Person is the superclass and Student and Employee are the subclasses. Person has some attributes that are common to both Student and Employee, such as name, address, and phone number. Student and Employee have some attributes that are specific to them, such as student_id and salary, respectively. Person also has some relationships that are common to both Student and Employee, such as lives_in and works_for. Student and Employee have some relationships that are specific to them, such as enrolled_in and manages, respectively   .
- Generalization can also be applied recursively to form further higher level entities from existing superclasses. For example, the entity Animal can be generalized from the entities Mammal and Bird, and Mammal can be further generalized from the entities Dog and Cat, as shown below:

```
       Animal
       /    \
   Mammal  Bird
   /    \
 Dog    Cat
```

- In this example, Animal is the highest level superclass and Dog and Cat are the lowest level subclasses. Animal has some attributes that are common to all its subclasses, such as name, color, and weight. Mammal has some attributes that are common to its subclasses, such as fur and milk. Bird has some attributes that are specific to it, such as feathers and wings. Dog and Cat have some attributes that are specific to them, such as breed and tail. Animal also has some relationships that are common to all its subclasses, such as belongs_to and eats. Mammal has some relationships that are common to its subclasses, such as mates_with and gives_birth_to. Bird has some relationships that are specific to it, such as flies and lays_eggs. Dog and Cat have some relationships that are specific to them, such as barks and scratches, respectively   .



### Aggregation in Entity Relationship Model

- Aggregation is a technique to model a relationship involving a relationship set and one or more entity sets .
- Aggregation allows us to treat a relationship set as an entity set for purposes of participation in other relationships .
- Aggregation is an abstraction through which we can represent relationships as higher level entity sets.
- Aggregation protects the integrity of an assembly of objects by defining a single point of control.
- Aggregation is useful when we need to express a relationship among relationships, or when we need to attach attributes to relationships .

- Example of aggregation:

  - Consider a scenario where an employee works for a project and requires some machinery. We can model this as follows:

    - Employee and Project are entity sets, and Works_For is a relationship set between them.
    - Machinery is another entity set, and Requires is a relationship set between Works_For and Machinery.
    - To simplify the diagram, we can use aggregation to treat Works_For as an entity set and connect it to Machinery with Requires.
    - We can also attach an attribute to Requires, such as Quantity, to indicate how many machines are needed for each work assignment.

  - The following diagram shows the aggregation:

    ```
    +----------+       +----------+       +----------+
    | Employee |       | Project  |       | Machinery|
    +----------+       +----------+       +----------+
         |                |                    |
         | Works_For      |                    |
         +----------------+                    |
         |                                    |
         |                                    |
         | Requires                           |
         +------------------------------------+
         | Quantity                           |
    ```



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content in markdown format:

### Reduction of an ER diagram to tables

- An ER diagram is a graphical representation of the entities and relationships in a database.
- A table is a collection of rows and columns that store data in a database.
- To convert an ER diagram to tables, we need to follow some rules and steps:

  - For each entity type in the ER diagram, create a table with the same name and include all the attributes as columns.
  - Choose a primary key for each table, which is a column or a combination of columns that uniquely identifies each row in the table.
  - For each one-to-one or one-to-many relationship type in the ER diagram, identify the table that represents the entity type on the many side of the relationship and add a foreign key to that table, which is a column or a combination of columns that references the primary key of the table that represents the entity type on the one side of the relationship.
  - For each many-to-many relationship type in the ER diagram, create a new table with the same name and include the primary keys of the tables that represent the entity types participating in the relationship as columns. Declare the combination of these columns as the primary key of the new table. Optionally, include any attributes of the relationship type as columns in the new table.
  - For each weak entity type in the ER diagram, create a table with the same name and include all the attributes as columns. Also, include the primary key of the table that represents the strong entity type that owns the weak entity type as a foreign key. Declare the combination of the foreign key and the partial key (the attribute or attributes that uniquely identify the weak entity type within the owner entity type) as the primary key of the table.

- Here is an example of converting an ER diagram to tables:

ER diagram

- The tables corresponding to the ER diagram are:

| LECTURE | | | | |
| --- | --- | --- | --- | --- |
| **Lecture_ID** | Lecture_Name | Lecture_Salary | Lecture_Age | Lecture_Gender |
| PK | | | | |

| STUDENT | | | | |
| --- | --- | --- | --- | --- |
| **Student_ID** | Student_Name | Student_Age | Student_Gender | Lecture_ID |
| PK | | | | FK |

| SUBJECT | | | |
| --- | --- | --- | --- |
| **Subject_ID** | Subject_Name | Subject_Credit | Lecture_ID |
| PK | | | FK |

| COURSE | | | |
| --- | --- | --- | --- |
| **Course_ID** | Course_Name | Course_Fee | Course_Duration |
| PK | | | |

| STUDENT_COURSE | | |
| --- | --- | --- |
| **Student_ID** | **Course_ID** | Grade |
| PK, FK | PK, FK | |

- Note: PK stands for primary key and FK stands for foreign key.



### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts in addition to the ER model concepts :

- Subclasses and superclasses: A subclass is a subset of entities of a superclass that share some common attributes or relationships distinct from other entities of the superclass. A superclass is a set of entities that includes all its subclasses. For example, a superclass PERSON can have subclasses STUDENT and EMPLOYEE, each with their own attributes and relationships.
- Specialization and generalization: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics of the entities in the superclass. Generalization is the reverse process of abstraction, where common properties of lower-level entities are grouped together to form a higher-level entity. For example, a specialization of PERSON can be based on the attribute occupation, and a generalization of STUDENT and EMPLOYEE can be PERSON.
- Category or union type: A category or union type is a subclass that represents a collection of entities from different entity types that share a common relationship with another entity type. For example, a category DEPENDENT can include entities from subclasses SPOUSE and CHILDREN, which are related to the superclass EMPLOYEE.
- Aggregation: Aggregation is the process of treating a relationship as an entity type, which allows relationships between relationships or between entities and relationships. For example, an aggregation PROJECT_ASSIGNMENT can represent the relationship between the entity types EMPLOYEE and PROJECT, and have its own attributes and relationships.

The extended ER model can be represented graphically using the following symbols :

- A rectangle for an entity type, with the name inside.
- An ellipse for an attribute, with the name inside. A key attribute is underlined, a multivalued attribute is double-lined, and a derived attribute is dashed.
- A diamond for a relationship type, with the name inside. A total participation is indicated by a double line, and a partial participation by a single line. A cardinality ratio is shown by placing numbers or symbols near the ends of a relationship line.
- A triangle for an ISA relationship, which connects a superclass to its subclasses. The subclasses are written below the triangle, separated by commas. A disjoint constraint is indicated by placing a D inside the triangle, and an overlap constraint by placing an O. A total specialization is indicated by a double line, and a partial specialization by a single line.
- A circle with a T inside for a category or union type, which connects a category to its member entity types. The category is written below the circle, and the member entity types are written above the circle, separated by commas.
- A dashed rectangle for an aggregation, which encloses the relationship type that is being aggregated and the entity types that participate in that relationship. The aggregation is treated as an entity type and can have its own attributes and relationships.

Here is an example of an extended ER diagram for a university database:

EER diagram example



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on relationships of higher degree for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System.

# Relationships of Higher Degree

- A relationship is an association among two or more entity sets.
- The degree of a relationship is the number of entity sets that participate in it .
- A binary relationship has a degree of two, meaning that it involves two entity sets . For example, a Works_For relationship between Employees and Departments entity sets.
- A unary relationship has a degree of one, meaning that it involves only one entity set. For example, a Represents relationship between Agents entity set.
- A ternary relationship has a degree of three, meaning that it involves three entity sets . For example, a Supplies relationship between Suppliers, Parts and Projects entity sets.
- A relationship of higher degree than three is called an n-ary relationship, where n is the number of entity sets involved. For example, a Sells relationship between Customers, Products, Stores and Salespersons entity sets.
- Relationships of higher degree than two are less common and more complex than binary relationships .
- They can sometimes be replaced by a combination of binary relationships and associative entities . For example, a Sells relationship can be replaced by a Sale entity that relates Customers, Products, Stores and Salespersons entity sets.
- However, some relationships of higher degree cannot be easily replaced by binary relationships, as they may lose some information or introduce redundancy . For example, a Supplies relationship cannot be replaced by binary relationships without losing the information about which supplier supplies which part to which project.
- Therefore, it is important to choose the appropriate degree of relationship based on the semantics and constraints of the real-world situation .
- The notation for relationships of higher degree is similar to that of binary relationships, except that more than two entity sets are connected by a diamond-shaped symbol . The cardinality ratios and participation constraints can also be specified for each entity set .
- Here is an example of a ternary relationship diagram:

Ternary relationship diagram

: Relationships in ER Models and Types - CSVeda
: What is the degree of relation in DBMS? - AfterAcademy
: What is degree of relationship in ER modeling in dbms
: Relationships in ER model - GeeksforGeeks
: CPS352 Lecture -The Entity-Relationship Model
: THE ENTITY- RELATIONSHIP (ER) MODEL - Cheriton School of Computer Science



```
## Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table has a fixed number of columns (attributes) and a variable number of rows (records or tuples).
- A relational database follows a set of rules, called the relational model, that ensure the data is consistent, accurate, and accessible.
- The relational model was proposed by Edgar F. Codd in 1970, and is based on the concept of mathematical relations and set theory.
- The main components of the relational model are:

  - Relation: A table with a unique name, where each row represents a fact or an entity, and each column represents an attribute or a property of the entity. A relation can also be called a relation schema or a relation variable.
  - Attribute: A column in a table, where each attribute has a unique name and a domain (a set of possible values). An attribute can also be called a relation attribute or a relation column.
  - Tuple: A row in a table, where each tuple contains a value for each attribute in the relation. A tuple can also be called a relation tuple or a relation record.
  - Degree: The number of attributes in a relation.
  - Cardinality: The number of tuples in a relation.
  - Domain: The set of possible values for an attribute.
  - Primary key: A set of one or more attributes that uniquely identify each tuple in a relation. A primary key can also be called a relation key or a candidate key.
  - Foreign key: A set of one or more attributes in a relation that refer to the primary key of another relation. A foreign key can also be called a relation foreign key or a referential attribute.
  - Referential integrity: A rule that ensures that the values of a foreign key in a relation match the values of the primary key in the referenced relation, or are null.
  - Null: A special value that indicates the absence of a value for an attribute. Null is not the same as zero or blank.
  - Relational algebra: A set of operators that can be applied to one or more relations to produce a new relation. Relational algebra operators include selection, projection, join, union, intersection, difference, and division.
  - Relational calculus: A declarative language that can be used to specify queries on relations. Relational calculus expressions consist of variables, constants, logical operators, and quantifiers.
  - SQL: A standard language for defining, manipulating, and querying data in relational databases. SQL stands for Structured Query Language, and is based on relational algebra and relational calculus.
  - Normalization: A process of decomposing a relation into smaller relations that have less redundancy and anomalies. Normalization is based on the concept of functional dependencies and normal forms.
  - Functional dependency: A constraint that specifies that the value of one or more attributes in a relation depends on the value of another attribute or a set of attributes in the same relation.
  - Normal form: A condition that a relation satisfies if it has a certain level of normalization. The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
```



### Introduction to relational database

- A relational database is a type of database that stores and provides access to data points that are related to one another   .
- A relational database organizes data into rows and columns, which collectively form a table . Each row in the table is a record with a unique ID called the key. Each column in the table is an attribute that describes some property of the record.
- Data is typically structured across multiple tables, which can be joined together via a primary key or a foreign key. A primary key is a column or a set of columns that uniquely identifies each row in a table. A foreign key is a column or a set of columns that references a primary key in another table. The relationship between two tables is established by matching the foreign key with the corresponding primary key.
- Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables . The relational model was proposed by Edgar F. Codd in 1970 as a way of overcoming the limitations of the hierarchical and network models of data organization.
- Relational databases are also typically associated with transactional databases, which execute commands, or transactions, collectively. A transaction is a logical unit of work that ensures the consistency and integrity of the data. A transaction must follow the ACID properties: atomicity, consistency, isolation, and durability. Atomicity means that a transaction either completes entirely or not at all. Consistency means that a transaction does not violate any rules or constraints defined on the data. Isolation means that a transaction does not interfere with other concurrent transactions. Durability means that a transaction's effects are permanent and survive any system failures.
- Relational databases are widely used in various domains and applications, such as banking, e-commerce, inventory management, social media, etc. Some examples of popular relational database management systems (RDBMS) are Oracle, MySQL, PostgreSQL, Microsoft SQL Server, etc. An RDBMS is a software system that provides tools and interfaces for creating, querying, updating, and managing relational databases.



### Relational Database Structure

- A relational database is a collection of data organized into tables, also known as relations, that are linked by common attributes or keys.
- A table consists of rows, also known as tuples or records, that store data about an entity or an object, and columns, also known as attributes or fields, that store data about a property or a characteristic of the entity.
- A primary key is a column or a combination of columns that uniquely identifies each row in a table. A primary key cannot contain null values or duplicate values.
- A foreign key is a column or a combination of columns that references the primary key of another table. A foreign key establishes a relationship between two tables and enforces referential integrity, which means that the values in the foreign key column must match the values in the referenced primary key column or be null.
- A relational database can have many types of relationships between tables, such as one-to-one, one-to-many, many-to-one, or many-to-many. A relationship is represented by a line that connects the foreign key of one table to the primary key of another table.
- A relational database can be normalized to reduce data redundancy and improve data integrity. Normalization is the process of organizing the data into tables that follow certain rules or normal forms. The most common normal forms are first normal form (1NF), second normal form (2NF), and third normal form (3NF).
- A relational database can be queried using a structured query language (SQL), which is a standard language for manipulating and retrieving data from relational databases. SQL consists of commands, clauses, operators, functions, and expressions that specify the data to be retrieved or modified. SQL can also be used to create, alter, or delete tables and other database objects.



### Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relational database .
- A domain defines the **data type**, **format**, and **constraints** of an attribute .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- For example, the domain of Marital Status can be a set of values: {Married, Single, Divorced}. The domain of Shift can be a set of values: {Mon, Tue, Wed, Thu, Fri, Sat, Sun}.
- A domain can be **simple** or **composite**. A simple domain consists of a single data type, such as integer or string. A composite domain consists of multiple data types, such as date or address.
- A domain can be **scalar** or **nonscalar**. A scalar domain has only one value for each attribute, such as age or name. A nonscalar domain has multiple values for each attribute, such as hobbies or skills.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System:

### Attributes for the notes of the Unit 3 - Relational Database Concepts

- Define the terms relation, tuple, attribute, domain, degree, cardinality, and primary key.
- Explain the concept of relational integrity and the types of constraints that enforce it: domain, entity, referential, and user-defined.
- Describe the properties of relations: uniqueness of tuples, ordering of tuples and attributes, and atomic values.
- Illustrate the use of relational algebra operators: select, project, union, set difference, Cartesian product, rename, and join.
- Demonstrate how to formulate relational algebra expressions for various queries and how to simplify them using algebraic laws and rules.
- Compare and contrast the relational algebra and the relational calculus as query languages for relational databases.
- Define the terms functional dependency, determinant, candidate key, superkey, and foreign key.
- Apply the rules of inference and the Armstrong's axioms to derive functional dependencies from a given set of dependencies.
- Explain the concept of normalization and the normal forms: first, second, and third normal forms (1NF, 2NF, and 3NF).
- Perform the normalization process on a given relation using the functional dependencies and the normal forms.
- Discuss the advantages and disadvantages of normalization and denormalization in relational database design.



### Tuples

- A tuple is a row of a table that represents an entity or a relationship instance.
- A tuple consists of a set of attribute values, one for each attribute of the table.
- A tuple can also be seen as a function that maps each attribute name to a value.
- The order of the attribute values in a tuple does not matter, as long as they correspond to the attribute names in the table schema.
- A tuple is uniquely identified by its primary key, which is a subset of its attribute values that can distinguish it from other tuples in the same table.
- A tuple can be inserted, deleted, or updated in a table using SQL commands.
- A tuple can be selected, projected, joined, or aggregated using SQL queries.
- A tuple can be represented as a comma-separated list of attribute values enclosed in parentheses, such as `(1, 'Alice', 25)`.
- A tuple can also be represented as a record or a structure in some programming languages, such as C or Python.



# Relations and Relational Database Schema

- A **relation** is a set of tuples that have the same attributes. A tuple is a single row of data in a table. An attribute is a column or field name of a table. A relation can also be called a table or a relation variable.
- A **relational schema** is a collection of relation schemas for a whole database. A relation schema is a description of a relation, which specifies the name of the relation and the name and type of each attribute. A relational schema can also be called a database schema or a schema diagram.
- A relational schema is a collection of **metadata**, which is data about data. It describes the structure and constraints of data representing in a particular domain. It does not contain the actual data values, but only the names and types of the attributes.
- A relational schema acts as a **blueprint** or a design of the datasets within the database. It shows the **connections** between different tables, which contain related data. These connections are called **foreign keys**, which are attributes that refer to the primary key of another table.
- A relational schema can be represented using a **graphical notation** or a **textual notation**. A graphical notation uses symbols and lines to show the tables and their attributes, and the foreign keys and their references. A textual notation uses a list of relation names and their attributes, and the constraints on the attributes.
- A relational schema can have **benefits** such as:
  - It helps to **organize** and **structure** the data in a logical and consistent way.
  - It helps to **avoid** data **redundancy** and **inconsistency**, by ensuring that each data item is stored only once and in one place.
  - It helps to **enforce** data **integrity** and **security**, by defining the rules and restrictions on the data values and operations.
  - It helps to **facilitate** data **manipulation** and **querying**, by providing a common language and interface for accessing and modifying the data.
  - It helps to **document** and **communicate** the data model and design to the users and developers of the database.



### Integrity Constraints for the Notes of the Unit 3 - Relational Database Concepts

- Integrity constraints are the set of rules that can be used to maintain the data integrity during an insert, delete and update operations into a table.
- Data integrity means that the data in the database is valid, consistent and accurate.
- There are four types of integrity constraints in relational database:
  - Domain constraints
  - Key constraints
  - Entity integrity constraints
  - Referential integrity constraints

#### Domain Constraints
- Domain constraints specify the valid values for a column or an attribute.
- They are defined by the data type, size, range, format and default value of the column.
- For example, a column named AGE can have a domain constraint that only allows integer values between 1 and 120.

#### Key Constraints
- Key constraints identify the unique rows in a table or a relation.
- They are defined by the primary key and the candidate keys of the table.
- A primary key is a column or a combination of columns that uniquely identifies a row in a table.
- A candidate key is a column or a combination of columns that can also uniquely identify a row in a table, but is not chosen as the primary key.
- For example, a table named STUDENT can have a primary key of STUDENT_ID and a candidate key of EMAIL.

#### Entity Integrity Constraints
- Entity integrity constraints ensure that every table has a primary key and that the primary key does not contain null values.
- Null values are used to represent missing or unknown data in a database.
- A primary key with null values cannot uniquely identify a row in a table.
- For example, a table named COURSE can have a primary key of COURSE_ID and an entity integrity constraint that does not allow null values in the COURSE_ID column.

#### Referential Integrity Constraints
- Referential integrity constraints ensure that the foreign key values in a table match the primary key values in another table.
- A foreign key is a column or a combination of columns that references the primary key of another table.
- Referential integrity constraints prevent the insertion of invalid data or the deletion of referenced data in the database.
- For example, a table named ENROLLMENT can have a foreign key of STUDENT_ID that references the primary key of the STUDENT table, and a referential integrity constraint that does not allow the insertion of a STUDENT_ID that does not exist in the STUDENT table, or the deletion of a STUDENT_ID that is referenced by the ENROLLMENT table.



### Entity Integrity in Relational Database

- Entity integrity is a form of data integrity that ensures that each row in a table has a unique and non-null identifier, called a primary key  .
- A primary key is a column or a combination of columns that can uniquely identify a row in a table .
- Entity integrity prevents duplicate records, missing values, and inconsistent data in a table  .
- Entity integrity is enforced by the database system by checking the primary key values before inserting or updating data in a table.
- Entity integrity is important for maintaining the accuracy, consistency, and reliability of the data in a relational database .



### Referential Integrity

- Referential integrity is a property of data stating that all its references are valid .
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist .
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key.
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table.
- Referential integrity ensures that relationships between tables remain consistent .
- Referential integrity prevents the following problems:
  - Inserting a record in a child table that does not have a corresponding record in the parent table (orphaned record).
  - Updating a primary key value in the parent table that is referenced by a foreign key value in the child table (dangling reference).
  - Deleting a record in the parent table that is referenced by a foreign key value in the child table (lost child).
- Referential integrity can be enforced by using constraints, triggers, or application logic .
- Referential integrity is a type of data integrity, which is a broader concept that encompasses the accuracy, consistency, and validity of data in a database.



### Key Constraints in Relational Database

- Key constraints are rules that are defined for primary keys in a relational database. A primary key is a column or a set of columns that uniquely identifies each row in a table. 
- Key constraints ensure that the data in the primary key column(s) is unique and not null, and that each row can be referenced by other tables using foreign keys. 
- Key constraints can be classified into two types: single-attribute and composite. A single-attribute key constraint is applied on a single column, while a composite key constraint is applied on a combination of two or more columns. 
- Key constraints can be specified using the PRIMARY KEY keyword in the CREATE TABLE or ALTER TABLE statements. For example, to create a table named Student with a single-attribute primary key on the column StudentID, the following SQL statement can be used:

```sql
CREATE TABLE Student (
  StudentID INT PRIMARY KEY,
  Name VARCHAR(50),
  Age INT
);
```

- To create a table named Course with a composite primary key on the columns CourseID and Semester, the following SQL statement can be used:

```sql
CREATE TABLE Course (
  CourseID VARCHAR(10),
  Semester VARCHAR(10),
  Title VARCHAR(50),
  Instructor VARCHAR(50),
  PRIMARY KEY (CourseID, Semester)
);
```

- Key constraints can also be defined using the CONSTRAINT keyword and a constraint name. For example, to create a table named Enrollment with a composite primary key on the columns StudentID and CourseID, and a foreign key constraint on the column StudentID that references the Student table, the following SQL statement can be used:

```sql
CREATE TABLE Enrollment (
  StudentID INT,
  CourseID VARCHAR(10),
  Grade CHAR(1),
  CONSTRAINT PK_Enrollment PRIMARY KEY (StudentID, CourseID),
  CONSTRAINT FK_Student FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);
```

- Key constraints have some limitations and rules that must be followed. For example, a table can have only one primary key constraint, a primary key cannot exceed 16 columns and a total key length of 900 bytes, and a foreign key must reference a primary key or a unique key in another table.  
- Key constraints are important for maintaining the integrity, consistency, and accuracy of the data in a relational database. They prevent duplicate, null, or invalid values in the primary key columns, and ensure that the relationships between tables are enforced and consistent.



### Domain Constraints

- A domain is a set of atomic values that a column or attribute can take in a table or relation.
- A domain constraint specifies the valid values for a column or attribute in a table or relation.
- A domain constraint can be enforced by using data types, ranges, formats, patterns, or lists of values.
- A domain constraint can help to ensure data integrity, consistency, and accuracy in a database.
- A domain constraint can be defined at the schema level or the instance level.
- A schema-level domain constraint is specified when the table or relation is created or modified, and applies to all the rows in the table or relation.
- An instance-level domain constraint is specified when a row is inserted or updated, and applies to only that row.
- A domain constraint can be violated if a value that does not belong to the domain is inserted or updated in the column or attribute.
- A domain constraint violation can result in an error, a warning, a rejection, or a substitution of the value, depending on the database system and the user's preference.
- A domain constraint can be checked by using the CHECK clause in the CREATE TABLE or ALTER TABLE statement, or by using a trigger or a stored procedure.



### Relational algebra - relational calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a **procedural** language that specifies **how** to construct a new relation from one or more existing relations.
- Relational calculus is a **declarative** language that specifies **what** information is required from the relations, without specifying how to obtain it.
- Relational algebra and relational calculus are **logically equivalent**, meaning that any query that can be expressed in one language can also be expressed in the other language. This is known as **Codd's theorem** .
- Relational algebra consists of a set of basic operations, such as selection, projection, union, set difference, Cartesian product, and renaming, and a set of additional operations, such as join, division, natural join, and assignment, that can be derived from the basic ones.
- Relational calculus can be divided into two variants: **tuple relational calculus** (TRC) and **domain relational calculus** (DRC). Both variants use a notation of **quantified variables** and **logical predicates** to define the result of a query.
- Tuple relational calculus uses variables that range over **tuples** of a relation. A query in TRC consists of a formula that specifies the attributes and conditions for the tuples in the result. For example, the query "Find the names of all customers who have a loan at the bank" can be written in TRC as:

```{x | Customer(x) ∧ ∃y (Loan(y) ∧ x.customer_name = y.customer_name)}```

- Domain relational calculus uses variables that range over **values** of the attributes in a relation. A query in DRC consists of a formula that specifies the values and conditions for the attributes in the result. For example, the same query as above can be written in DRC as:

```{<n> | ∃c, l, b, a (Customer(c, n, a) ∧ Loan(l, c, b)}```

- Both TRC and DRC are **safe** languages, meaning that they can only express queries that are guaranteed to return a finite number of tuples. A query is safe if all the variables in the query are either bound by a quantifier or appear in the output. A query is unsafe if it contains a free variable that can take infinitely many values. For example, the query "Find all customers who have a loan with a branch that is located in the same city as the customer" is safe, but the query "Find all customers who have a loan with a branch that is located in a different city than the customer" is unsafe.



### Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases.
- Relational calculus is based on the concept of mathematical logic and allows users to specify what data they want to retrieve from the database, without specifying how to do it.
- Tuple and domain calculus differ in the way they use variables to represent data.

#### Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables range over tuples, which are ordered sets of attribute values that represent a single row or record in a database table.
- A tuple variable (t) goes to each row of the table and checks if the predicate is true or false for the given row.
- A query in tuple relational calculus is of the form `{t | P(t)}`, where t is a tuple variable and P(t) is a formula involving t and other constants, comparison operators, logical connectives and quantifiers.
- The result of the query is the set of all tuples t that satisfy the formula P(t).
- For example, the query `{t | t[dept] = 'CS' and t[salary] > 50000}` returns the set of all tuples t from the employee table such that the department is CS and the salary is greater than 50000.

#### Domain Relational Calculus (DRC)

- In domain relational calculus, variables range over domain elements, which are field values of the attributes in the database tables.
- A query in domain relational calculus is of the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a formula involving the variables and other constants, comparison operators, logical connectives and quantifiers.
- The result of the query is the set of all n-tuples <x1, x2, ..., xn> that satisfy the formula P(x1, x2, ..., xn).
- For example, the query `{<name, salary> | exists e (e[name] = name and e[dept] = 'CS' and e[salary] = salary and salary > 50000)}` returns the set of all pairs <name, salary> such that there exists an employee e with the same name and salary, and the department is CS and the salary is greater than 50000.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of basic operations – selection and projection in relational database.

### Basic operations – selection and projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database.
- Selection operation targets records (rows) or specific entities in a relational database. It filters the rows that satisfy a given condition or predicate.
- Projection operation targets attributes (columns) or specific properties of entities in a relational database. It selects the columns that are specified in the query.
- In SQL, the SELECT statement combines both selection and projection operations in a single statement. The WHERE clause is used for selection and the list of attributes after the SELECT keyword is used for projection.
- For example, consider the following table of employees:

| EmpID | Name | Dept | Salary |
| ----- | ---- | ---- | ------ |
| 101   | John | IT   | 5000   |
| 102   | Mary | HR   | 4000   |
| 103   | Bob  | IT   | 6000   |
| 104   | Alice| HR   | 4500   |

- To select all the employees who work in the IT department, we can use the following SQL query:

```sql
SELECT * FROM employees WHERE Dept = 'IT';
```

- This query performs a selection operation on the table and returns the following result:

| EmpID | Name | Dept | Salary |
| ----- | ---- | ---- | ------ |
| 101   | John | IT   | 5000   |
| 103   | Bob  | IT   | 6000   |

- To project only the names and salaries of the employees, we can use the following SQL query:

```sql
SELECT Name, Salary FROM employees;
```

- This query performs a projection operation on the table and returns the following result:

| Name | Salary |
| ---- | ------ |
| John | 5000   |
| Mary | 4000   |
| Bob  | 6000   |
| Alice| 4500   |

- We can also combine both selection and projection operations in a single query. For example, to project only the names and salaries of the employees who work in the HR department, we can use the following SQL query:

```sql
SELECT Name, Salary FROM employees WHERE Dept = 'HR';
```

- This query performs both selection and projection operations on the table and returns the following result:

| Name | Salary |
| ---- | ------ |
| Mary | 4000   |
| Alice| 4500   |

- Selection and projection operations are useful for retrieving specific data from a relational database based on certain criteria or preferences. They are also the basis for other relational algebra operations such as join, union, intersection, and difference.



### Set-theoretic operations for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- Set-theoretic operations are operations that are based on the mathematical concept of sets. Sets are collections of distinct elements that have some common property or relation.
- In relational database, set-theoretic operations are used to combine or compare two or more relations (tables) that have the same attributes (columns) and domains (data types).
- The main set-theoretic operations in relational database are union, intersection, and difference. These operations are also called relational set operators.
- Union: The union operation combines two relations and returns a new relation that contains all the tuples (rows) that are either in the first relation or in the second relation or in both. The union operation is denoted by the symbol ∪.
- Intersection: The intersection operation returns a new relation that contains only the tuples that are common to both the relations. The intersection operation is denoted by the symbol ∩.
- Difference: The difference operation returns a new relation that contains only the tuples that are in the first relation but not in the second relation. The difference operation is denoted by the symbol -.
- The condition for using set-theoretic operations is that the relations must be union compatible, which means that they must have the same number of attributes, the same attribute names, and the same attribute domains.
- Example: Consider the following two relations Student and Teacher, which have the same attributes Name, Age, and Subject.

| Name | Age | Subject |
| --- | --- | --- |
| Alice | 20 | Math |
| Bob | 21 | Physics |
| Carol | 22 | Chemistry |
| David | 23 | Biology |

Student

| Name | Age | Subject |
| --- | --- | --- |
| Eve | 24 | Math |
| Frank | 25 | Physics |
| Carol | 22 | Chemistry |
| George | 26 | History |

Teacher

- The union of Student and Teacher is:

| Name | Age | Subject |
| --- | --- | --- |
| Alice | 20 | Math |
| Bob | 21 | Physics |
| Carol | 22 | Chemistry |
| David | 23 | Biology |
| Eve | 24 | Math |
| Frank | 25 | Physics |
| George | 26 | History |

Student ∪ Teacher

- The intersection of Student and Teacher is:

| Name | Age | Subject |
| --- | --- | --- |
| Carol | 22 | Chemistry |

Student ∩ Teacher

- The difference of Student and Teacher is:

| Name | Age | Subject |
| --- | --- | --- |
| Alice | 20 | Math |
| Bob | 21 | Physics |
| David | 23 | Biology |

Student - Teacher

- The difference of Teacher and Student is:

| Name | Age | Subject |
| --- | --- | --- |
| Eve | 24 | Math |
| Frank | 25 | Physics |
| George | 26 | History |

Teacher - Student

- Set-theoretic operations can be implemented in DBMS using different queries, such as SQL (Structured Query Language). For example, the union operation can be performed using the keyword UNION, the intersection operation can be performed using the keyword INTERSECT, and the difference operation can be performed using the keyword EXCEPT or MINUS.



# Join Operations

Join operations are used to combine data from two or more tables in a relational database based on some common attributes or conditions. Join operations are essential for querying data across multiple tables and for implementing the relational algebra operations of selection, projection, and Cartesian product.

There are different types of join operations, each with its own syntax and semantics. Some of the most common join types are:

- **Inner join**: This join returns only the rows that match the join condition in both tables. For example, an inner join of the tables `Customer` and `Order` on the attribute `CustomerID` will return only the rows where the same `CustomerID` value exists in both tables. This is the default join type in SQL.

- **Left outer join**: This join returns all the rows from the left table, and the matched rows from the right table. If there is no match for a row in the left table, the columns of the right table will have null values. For example, a left outer join of the tables `Customer` and `Order` on the attribute `CustomerID` will return all the rows from the `Customer` table, and the corresponding rows from the `Order` table if they exist, or null values otherwise.

- **Right outer join**: This join returns all the rows from the right table, and the matched rows from the left table. If there is no match for a row in the right table, the columns of the left table will have null values. For example, a right outer join of the tables `Customer` and `Order` on the attribute `CustomerID` will return all the rows from the `Order` table, and the corresponding rows from the `Customer` table if they exist, or null values otherwise.

- **Full outer join**: This join returns all the rows from both tables, and the matched rows from both tables. If there is no match for a row in either table, the columns of the other table will have null values. For example, a full outer join of the tables `Customer` and `Order` on the attribute `CustomerID` will return all the rows from both tables, and the corresponding rows from both tables if they exist, or null values otherwise.

- **Cross join**: This join returns the Cartesian product of the two tables, which means every possible combination of rows from both tables. For example, a cross join of the tables `Customer` and `Order` will return every possible pair of rows from both tables, regardless of the `CustomerID` value. This join type does not require a join condition, but it can result in a very large result set.

- **Self join**: This join is used to join a table with itself, which means the same table is used as both the left and the right table. This can be useful for finding relationships within the same table. For example, a self join of the table `Employee` on the attribute `ManagerID` can be used to find the employees who work under the same manager. A self join requires an alias for the table name to distinguish the two instances of the same table.

The syntax for join operations in SQL is as follows:

```sql
SELECT column_list
FROM table1 [JOIN_TYPE] JOIN table2
ON join_condition;
```

where `JOIN_TYPE` is one of the join types mentioned above, and `join_condition` is the expression that defines how the two tables are related, usually by comparing the values of some common attributes using a logical operator.

For example, the following query uses an inner join to find the names of the customers who have placed orders and the dates of their orders:

```sql
SELECT Customer.Name, Order.OrderDate
FROM Customer INNER JOIN Order
ON Customer.CustomerID = Order.CustomerID;
```

The following query uses a left outer join to find the names of the customers who have not placed any orders:

```sql
SELECT Customer.Name
FROM Customer LEFT OUTER JOIN Order
ON Customer.CustomerID = Order.CustomerID
WHERE Order.OrderID IS NULL;
```

The following query uses a cross join to find the total price of each possible combination of products:

```sql
SELECT Product.Name, Product.Price * Quantity.Quantity AS TotalPrice
FROM Product CROSS JOIN Quantity;
```

The following query uses a self join to find the names of the employees who work under the same manager as John Smith:

```sql
SELECT E1.Name
FROM Employee AS E1 INNER JOIN Employee AS E2
ON E1.ManagerID = E2.ManagerID
WHERE E2.Name = 'John Smith';
```



## Unit 4 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that organizes data into tables and columns to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design by creating atomic elements (i.e., elements that cannot be broken down into smaller parts) and defining relationships among them.
- Normalization is based on a series of normal forms (NF) that specify the conditions for a table to be well-structured and normalized. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or arrays of data. Each column should contain only one value for each row, and each row should have a unique identifier (primary key).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key. There should be no partial dependencies, where a column depends on only a part of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key. There should be no transitive dependencies, where a column depends on another non-key column that depends on the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (a column or a set of columns that determines another column) is a candidate key (a minimal set of columns that uniquely identifies a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, where a column or a set of columns depends on another column or a set of columns, and both are independent of the primary key.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, where a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys without losing any information.
- Normalization is not always desirable or feasible, as it may result in too many tables, increased complexity, reduced performance, or loss of business meaning. Therefore, database designers should balance the benefits and costs of normalization and consider the requirements and constraints of the application and the users.



### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency is denoted by an arrow, such as X -> Y, which means that the value of Y is determined by the value of X.
- There are four primary types of functional dependencies: multivalued, trivial, non-trivial and transitive .
- Multivalued dependency: A multivalued dependency occurs when there are two or more independent attributes in a relation that depend on a third attribute. For example, in a relation R(A, B, C), if A ->> B and A ->> C, then B and C are multivalued dependent on A.
- Trivial dependency: A trivial dependency occurs when the dependent attribute is a subset of the determinant attribute. For example, in a relation R(A, B, C), if A -> A or A -> AB, then these are trivial dependencies.
- Non-trivial dependency: A non-trivial dependency occurs when the dependent attribute is not a subset of the determinant attribute. For example, in a relation R(A, B, C), if A -> C, then this is a non-trivial dependency.
- Transitive dependency: A transitive dependency occurs when there is an indirect dependency between two attributes through a third attribute. For example, in a relation R(A, B, C), if A -> B and B -> C, then C is transitively dependent on A.
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization .
- Normalization is the process of organizing the data in a database to minimize data redundancy and improve data integrity .
- There are several normal forms that a database can follow, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF) and fifth normal form (5NF) .
- Each normal form has a set of rules or conditions that the database must satisfy to be in that normal form .
- The higher the normal form, the more normalized the database is, and the less data redundancy and anomalies it has .
- However, higher normal forms may also result in more tables and joins, which may affect the performance and complexity of the database .
- Therefore, the choice of the normal form depends on the requirements and trade-offs of the database design .



### Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

Normal forms are a set of rules or guidelines for designing relational databases in a way that reduces data redundancy and improves data integrity. Normalization is the process of applying these rules to a database schema or table. There are different levels of normalization, called normal forms, that indicate how well a database is normalized. The higher the normal form, the less redundancy and more consistency the database has.

The most common normal forms are:

- **First Normal Form (1NF)**: A table is in 1NF if it does not contain any composite or multi-valued attributes. This means that each column should have a single value and each row should have a unique identifier (primary key).
- **Second Normal Form (2NF)**: A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there should be no partial dependencies, where a non-key attribute depends on only a part of the primary key.
- **Third Normal Form (3NF)**: A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there should be no transitive dependencies, where a non-key attribute depends on another non-key attribute that depends on the primary key.
- **Boyce-Codd Normal Form (BCNF)**: A table is in BCNF if it is in 3NF and every determinant is a candidate key. This means that there should be no non-trivial functional dependencies, where a non-key attribute determines another non-key attribute.

There are other higher normal forms, such as 4NF, 5NF, and 6NF, but they are less commonly used in practice. The goal of normalization is to achieve the highest normal form possible without losing any information or compromising the performance of the database. Normalization can help avoid problems such as data anomalies, data inconsistency, data duplication, and data loss. However, normalization can also introduce some drawbacks, such as increased complexity, reduced efficiency, and more joins. Therefore, normalization should be balanced with other factors, such as the requirements of the application, the nature of the data, and the expected queries.



# Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database management system (DBMS) .
- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies .
- Normalization rules divide larger tables into smaller tables and link them using relationships .
- Normalization is based on the concept of normal forms, which are sets of conditions that a table must satisfy to be considered well-structured .
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if every attribute is atomic, meaning it cannot be further subdivided, and every row has a unique identifier .
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be derived from any other attribute or combination of attributes .
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be derived from any other non-key attribute or combination of non-key attributes .
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies .
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, meaning there are no attributes that depend on a set of attributes rather than a single attribute .
- A good rule to follow when doing logical database design is to arrange all the data in entities that are in fourth normal form. Then decide whether the result gives you an acceptable level of performance. If the performance is not acceptable, denormalizing your design is a good option .
- Denormalization is the process of introducing redundancy into a database design to improve query performance or simplify application logic .
- Denormalization should be done carefully and only after analyzing the trade-offs between normalization and denormalization, such as data consistency, storage space, and maintenance costs .



### Second

- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies.
- Normalization rules divide larger tables into smaller tables and link them using relationships.
- Normalization helps produce database systems that are cost-effective and have better security models.
- Normalization is based on the concept of normal forms, which are sets of rules that define the level of data integrity and efficiency in a table.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if every attribute is atomic (cannot be further subdivided) and every row has a unique identifier (primary key).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (a set of attributes that determines another attribute) is a candidate key (a minimal set of attributes that uniquely identifies a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies (a situation where one attribute determines a set of values for another attribute).
- To perform the normalization process, you start with a rough idea of the data you want to store, and apply certain rules to it in order to get it to a more efficient form.
- A good rule to follow when doing logical database design is to arrange all the data in entities that are in 4NF. Then decide whether the result gives you an acceptable level of performance. If the performance is not acceptable, denormalizing your design is a good option.
- Denormalization is the process of reversing the normalization steps to improve the query performance or simplify the application logic. Denormalization can introduce data redundancy and inconsistency, so it should be done carefully and selectively.
- Database design is critical to the successful implementation of a database management system that meets the data requirements of an enterprise system.



### Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two or more non-prime attributes that are indirectly determined by the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name.
- The primary key is (Student ID, Course ID), and the candidate keys are (Student ID, Course ID) and (Student ID, Course Name).
- The non-prime attributes are Student Name, Course Name, Instructor ID, and Instructor Name.
- There is a transitive dependency between Instructor ID and Instructor Name, since Instructor ID -> Instructor Name, and Instructor ID is determined by Course ID, which is part of the primary key.
- To convert this table to 3NF, we need to remove the transitive dependency by creating a separate table for instructors, with Instructor ID as the primary key and Instructor Name as the non-prime attribute.
- The original table will then have a foreign key reference to the instructor table, and the transitive dependency will be eliminated.
- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the Third Normal Form.
  - The Third Normal Form ensures functional dependency preserving and lossless decomposition, which means that the original data can be reconstructed from the normalized tables without any loss of information or inconsistency.
  - The Third Normal Form reduces the storage space and improves the performance of the database queries.



### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form)   .
- A relation is in BCNF if it is already in 3NF and for every functional dependency X -> Y, X is a super key or a candidate key  .
- A super key is a set of attributes that can uniquely identify a tuple in a relation. A candidate key is a minimal super key, meaning that no proper subset of it is a super key .
- BCNF is stricter than 3NF, as it eliminates the possibility of having a non-prime attribute (an attribute that is not part of any candidate key) on the right-hand side of a functional dependency  .
- BCNF ensures that there are no anomalies (such as redundancy, inconsistency, or update anomalies) in the relation, and that every attribute is fully dependent on the key  .

#### Example

- Consider a relation R with attributes A, B, C, D, and E, and the following functional dependencies:

  - A -> BC
  - C -> DE

- The candidate key for this relation is A, as it can uniquely determine all other attributes .
- This relation is in 3NF, as for every functional dependency, the left-hand side is a super key or the right-hand side is a prime attribute .
- However, this relation is not in BCNF, as C -> DE violates the condition that the left-hand side must be a super key .
- To convert this relation into BCNF, we need to decompose it into two relations, R1 and R2, as follows:

  - R1 (A, B, C)
  - R2 (C, D, E)

- Now, both R1 and R2 are in BCNF, as the only functional dependencies are A -> BC and C -> DE, and in both cases, the left-hand side is a candidate key .



### Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a statement in which some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency is a generalized form of referential constraints, which specify that a foreign key of one relation must be a subset of the primary key of another relation  .
- The syntax of inclusion dependency is `R1[A1, A2, ..., An] ⊆ R2[B1, B2, ..., Bn]`, where `R1` and `R2` are relations, `A1, A2, ..., An` and `B1, B2, ..., Bn` are attributes, and `⊆` denotes the subset relation  .
- The semantics of inclusion dependency is that for every tuple `t1` in `R1`, there exists a tuple `t2` in `R2` such that `t1[A1] = t2[B1]`, `t1[A2] = t2[B2]`, ..., and `t1[An] = t2[Bn]`  .
- An example of inclusion dependency is `Student[StudentID, Name, Major] ⊆ Person[PersonID, Name, Address]`, which means that every student is a person and has the same ID and name in both relations .
- Inclusion dependency can be checked by using the SQL query `SELECT * FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE R1.A1 = R2.B1 AND R1.A2 = R2.B2 AND ... AND R1.An = R2.Bn)`, which returns an empty result if the inclusion dependency holds  .
- Inclusion dependency can be enforced by using foreign key constraints, which are a special case of inclusion dependency where the right-hand side is a primary key  .
- Inclusion dependency can also be expressed by using universal relation assumption, which states that there is a single relation that contains all the attributes of the database and every other relation is a projection of this universal relation .
- Inclusion dependency can be used to normalize a database by decomposing a relation into smaller relations that satisfy inclusion dependency and other dependencies .



### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations yields back the original relation R. 
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data.  
- Lossless join decomposition is based on the concept of functional dependencies, which are constraints that specify how one set of attributes determines another set of attributes in a relation. 
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the given set of functional dependencies F:  
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- The above condition ensures that the common attributes of R1 and R2 are a superkey for either R1 or R2, which means that they can uniquely identify each tuple in the smaller relation. 
- If the decomposition is not lossless, then the natural join of R1 and R2 may produce spurious tuples that do not exist in the original relation R, resulting in loss of information and inconsistency. 
- There are algorithms that can decompose a relation into smaller relations that are in a certain normal form and also satisfy the lossless join property. Some of these algorithms are: 
  - Boyce-Codd Normal Form (BCNF) decomposition algorithm
  - Third Normal Form (3NF) decomposition algorithm
- These algorithms use the concept of minimal cover, which is a minimal set of functional dependencies that is equivalent to the given set of functional dependencies. 
- The steps of the BCNF decomposition algorithm are: 
  - Find a minimal cover G for the given set of functional dependencies F.
  - Initialize the set of relations D to {R}, where R is the original relation.
  - For each relation Ri in D, do the following:
    - Find a functional dependency X → Y in G that violates BCNF, i.e., X is not a superkey for Ri.
    - If such a dependency exists, then replace Ri by two relations: (Ri - Y) and (X U Y).
    - Repeat this step until Ri is in BCNF or no more dependencies in G can be applied.
  - Return the set of relations D as the final decomposition.
- The steps of the 3NF decomposition algorithm are: 
  - Find a minimal cover G for the given set of functional dependencies F.
  - Find a canonical cover H for G, i.e., a set of functional dependencies that preserves the dependency and has a singleton right-hand side.
  - For each functional dependency X → A in H, create a relation with the schema XA and add it to the set of relations D.
  - If none of the relations in D contains a key of R, then create a relation with the schema of any key of R and add it to D.
  - Return the set of relations D as the final decomposition.



Hello, I am Sydney, your AI assistant. I can help you with your topic of normalization using FD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System. Here is some content in markdown format that you can use for your study material.

### Normalization using FD

- Normalization is a process of organizing the data in a database to avoid data redundancy, insertion anomaly, update anomaly and deletion anomaly.
- Normalization is based on the concept of normal forms, which are sets of rules or constraints that a relation (table) should satisfy to be considered well-structured.
- Functional dependency (FD) is a constraint that describes the relationship between attributes (columns) in a relation. An FD of the form X -> Y means that the value of Y is determined by the value of X. X is called the determinant and Y is called the dependent.
- There are different types of FDs, such as trivial FD, non-trivial FD, partial FD, transitive FD, multivalued FD, join FD, etc. Each type of FD has a different impact on the normalization process.
- The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF) and fifth normal form (5NF). Each normal form has a set of conditions that a relation should satisfy to be in that normal form.
- To normalize a relation using FDs, we need to follow these steps:
  - Identify all the FDs that hold in the relation.
  - Check if the relation is in 1NF. If not, decompose it into 1NF relations by eliminating repeating groups and composite attributes.
  - Check if the relation is in 2NF. If not, decompose it into 2NF relations by eliminating partial dependencies, i.e., dependencies of non-prime attributes on proper subsets of candidate keys.
  - Check if the relation is in 3NF. If not, decompose it into 3NF relations by eliminating transitive dependencies, i.e., dependencies of non-prime attributes on non-prime attributes.
  - Check if the relation is in BCNF. If not, decompose it into BCNF relations by eliminating FDs that violate the condition that every determinant is a candidate key.
  - Check if the relation is in 4NF. If not, decompose it into 4NF relations by eliminating multivalued dependencies, i.e., dependencies of non-prime attributes on subsets of candidate keys that are not functionally dependent on them.
  - Check if the relation is in 5NF. If not, decompose it into 5NF relations by eliminating join dependencies, i.e., dependencies that imply that the relation can be losslessly joined from its projections on subsets of attributes.
- Normalization using FDs can improve the data integrity, consistency, and efficiency of the database, but it can also introduce some drawbacks, such as increased number of relations, complexity of queries, and loss of performance. Therefore, normalization should be balanced with other design considerations, such as user requirements, application needs, and system constraints.



### MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for **Multivalued Dependency**, which is a type of constraint between two sets of attributes in a relation.
- MVD means that for a single value of attribute `A`, multiple values of attribute `B` exist. For example, a person can work on multiple projects and have multiple hobbies.
- MVD is written as `A --> --> B`, which means `A` is multivalued dependent on `B` . For example, `Person --> --> Project` and `Person --> --> Hobby`.
- MVD plays a role in the **4NF** (Fourth Normal Form) database normalization, which is a process of reducing redundancy and inconsistency in a database.
- 4NF rule states that a relation should not contain any MVD in a single table to satisfy its conditions. Otherwise, it may lead to unnecessary repetition of data and other anomalies.
- To achieve 4NF, we need to decompose the relation into smaller relations that do not have any MVD. For example, if we have a relation `R(Person, Project, Hobby)`, we can decompose it into `R1(Person, Project)` and `R2(Person, Hobby)`.
- The decomposition should preserve the original MVDs and the functional dependencies (FDs) in the relation. For example, if we have `Person --> --> Project` and `Person --> Name` in `R`, we should have them in `R1` and `R2` as well.
- The decomposition should also be lossless, which means we can reconstruct the original relation from the decomposed relations without losing any information. For example, we can join `R1` and `R2` on `Person` to get `R` back.
- The algorithm for 4NF decomposition is similar to the BCNF (Boyce-Codd Normal Form) decomposition, except we replace the MVD as a FD in the BCNF algorithm. For example, we can treat `A --> --> B` as `A --> B` in the BCNF algorithm.



# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accuracy: The data stored in the database should reflect the real-world facts and events as accurately as possible.
  - Efficiency: The database should allow fast and easy access, retrieval, and modification of data, while minimizing the storage space and processing time.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Flexibility: The database should be able to accommodate changing data requirements and business needs, and support new functionalities and features.

## Normalization
- Normalization is a database schema design technique that reduces data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- Normalization helps to improve the database design by:
  - Eliminating data anomalies: Data anomalies are inconsistencies or errors that occur when data is inserted, updated, or deleted in a database. Normalization prevents data anomalies by ensuring that each piece of data is stored only once and in one place.
  - Reducing data duplication: Data duplication is the storage of the same data in multiple places, which wastes storage space and increases the risk of data inconsistency. Normalization reduces data duplication by separating the data into different tables based on their logical categories and dependencies.
  - Enhancing data integrity: Data integrity is the quality and reliability of the data in a database. Normalization enhances data integrity by enforcing the rules and constraints that govern the data and their relationships, such as primary keys, foreign keys, and referential integrity.
  - Simplifying data maintenance: Data maintenance is the process of updating, modifying, or deleting data in a database. Normalization simplifies data maintenance by reducing the number of places where data changes need to be made, and by making the data structure more understandable and manageable.

## Normal Forms
- Normal forms are the standards or rules that define the level of normalization of a database schema. There are several normal forms, each with a specific criterion that must be satisfied to achieve that level of normalization. The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, that is, values that cannot be further divided into smaller parts. This means that each column should store only one value of a single data type, and there should be no repeating groups or arrays of values in a table.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, that is, the value of a non-key attribute is determined by the value of the primary key and nothing else. This means that there should be no partial dependencies or subsets of the primary key that can determine the value of a non-key attribute.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, that is, the value of a non-key attribute is determined by the value of the primary key and not by the value of any other non-key attribute. This means that there should be no transitive dependencies or indirect relationships between the non-key attributes.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, that is, every attribute or set of attributes that can uniquely identify a row in a table is a potential primary key. This means that there should be no non-trivial functional dependencies or dependencies that do not involve a candidate key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, that is, dependencies where a single attribute or set of attributes can have more than one value for a given primary key. This means that there should be no repeating groups or arrays of values in a table.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, that is, dependencies where a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys. This means that there should be no



### Alternative Approaches to Database Design

- Database design is the process of defining the structure, organization, and relationships of data in a database.
- Database design can be influenced by various factors, such as the requirements of the application, the characteristics of the data, the performance and scalability needs, and the preferences of the developers and users.
- There are different approaches and techniques that can be used to design a database, depending on the context and the goals of the project. Some of the alternative approaches and advanced techniques are:

  - **Domain Model from Use Cases**: This is an agile approach that focuses on identifying the main entities and relationships of the domain from the user stories and use cases, rather than using formal entity-relationship diagrams. This approach can help to capture the essential features and behaviors of the system, and to avoid over-engineering or under-engineering the database.

  - **Normalization**: This is a technique that aims to reduce data redundancy and dependency by organizing the data into tables with well-defined attributes and keys. Normalization can help to improve data integrity, consistency, and efficiency, as well as to facilitate data manipulation and querying. Normalization involves applying a series of rules or normal forms to the tables, such as eliminating repeating groups, partial dependencies, and transitive dependencies.

  - **NoSQL Databases**: These are databases that do not follow the relational model or use SQL as the query language. NoSQL databases can store data in different formats and structures, such as JSON documents, key-value pairs, graphs, or columns. NoSQL databases can offer advantages such as flexibility, scalability, and performance, especially for handling large and unstructured data sets. However, they may also have drawbacks such as lack of standardization, consistency, and security.

  - **Application Development Tools**: These are tools that can help to create and manage databases without requiring extensive coding or technical skills. Application development tools can provide features such as data collection, analysis, visualization, and reporting, as well as user interface design, workflow automation, and collaboration. Some examples of application development tools are Office Reports, Second Prism, Databoard, DataMarket, and Q Research Software.



## Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for accessing and manipulating data in relational databases.
- SQL stands for Structured Query Language and is pronounced as "sequel" or "S-Q-L".
- SQL can perform various tasks on data, such as creating, querying, updating, deleting, and managing tables, views, indexes, and other database objects.
- SQL is divided into several sublanguages, each with a specific purpose and syntax. The main sublanguages are:
  - Data Definition Language (DDL): used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and constraints.
  - Data Manipulation Language (DML): used to insert, update, delete, and query data in the database, such as selecting, inserting, updating, and deleting rows from tables.
  - Data Control Language (DCL): used to control the access and permissions of the database, such as granting, revoking, and auditing privileges and roles.
  - Transaction Control Language (TCL): used to manage the transactions and concurrency of the database, such as committing, rolling back, and saving changes to the data.
- SQL is a declarative language, which means that it specifies what data to retrieve or manipulate, rather than how to do it. The database management system (DBMS) is responsible for executing the SQL statements and returning the results.
- SQL is a case-insensitive language, which means that it does not matter whether the keywords, identifiers, or literals are written in uppercase or lowercase. However, some DBMS may have specific rules or conventions for naming and quoting identifiers, such as table and column names.
- SQL is a semi-colon terminated language, which means that each SQL statement should end with a semi-colon (;) to indicate the end of the statement. However, some DBMS may not require or allow the semi-colon, depending on the context and mode of execution.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the basics of SQL for the unit 5 of the subject of Basics of Data Base Management System.

### Basics of SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- SQL can perform various tasks on data, such as creating, querying, updating, deleting, and modifying tables, views, indexes, and other database objects.
- SQL is composed of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL is used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and constraints.
- DML is used to manipulate the data in the database, such as inserting, updating, deleting, and merging records.
- DCL is used to control the access and privileges of the database, such as granting, revoking, and auditing permissions and roles.
- DQL is used to query and retrieve data from the database, such as selecting, joining, filtering, sorting, and grouping records.
- SQL follows a set of syntax rules and keywords that must be followed to write valid and executable statements. SQL is case-insensitive, but some database systems may require certain keywords or identifiers to be written in a specific case.
- SQL statements are composed of clauses, expressions, operators, functions, and literals. Clauses are the main components of a statement that specify the action and the data involved. Expressions are combinations of operators, functions, and literals that produce a value. Operators are symbols that perform arithmetic, logical, or comparison operations on operands. Functions are predefined or user-defined routines that perform calculations or transformations on arguments. Literals are constants that represent values of different data types, such as strings, numbers, dates, or booleans.
- SQL supports various data types that define the nature and format of the data stored in the database, such as char, varchar, int, float, date, time, etc. Different database systems may have different names or specifications for the data types, so it is important to check the documentation of the specific database system before using them.
- SQL also supports various constraints that enforce the rules and integrity of the data in the database, such as primary key, foreign key, unique, not null, check, default, etc. Constraints can be defined at the column level or the table level, and can be added, modified, or dropped using the DDL commands.
- SQL allows the use of comments to add explanatory or descriptive notes to the statements. Comments can be written in two ways: using two hyphens (--) to start a single-line comment, or using a slash and an asterisk (/* */) to enclose a multi-line comment. Comments are ignored by the database system and do not affect the execution of the statements.



### DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that can be used to create, modify, and delete the structure of database objects, such as tables, views, indexes, etc.
- DDL commands do not affect the data stored in the database, but only the schema or the definition of the database objects.
- Some of the common DDL commands are:
  - CREATE: This command is used to create a new database object, such as a table, a view, an index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table named students with three columns: id, name, and age.
  - ALTER: This command is used to modify an existing database object, such as adding, dropping, or renaming columns, changing data types, adding constraints, etc. For example, `ALTER TABLE students ADD email VARCHAR(100);` adds a new column named email to the students table.
  - DROP: This command is used to delete an existing database object, such as a table, a view, an index, etc. For example, `DROP TABLE students;` deletes the students table and all the data stored in it.
  - RENAME: This command is used to change the name of an existing database object, such as a table, a view, an index, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table, but keeps the table structure intact.
- DDL commands are normally executed by the database administrator or the developer, who have the required permissions to create and modify the database schema. DDL commands are not used by the general user, who should access the database via an application.



### DML

Data Manipulation Language (DML) is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views  . The main DML statements are:

- **SELECT**: retrieve data from one or more tables or views .
- **INSERT**: add new rows of data to a table or view  .
- **UPDATE**: modify existing rows of data in a table or view  .
- **DELETE**: remove existing rows of data from a table or view  .

DML statements can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, etc., to filter, aggregate, sort, or limit the data that is returned or affected.

DML statements can also be used with subqueries, joins, functions, expressions, and operators to perform complex operations on the data.

DML statements are executed by the database engine, which checks the syntax, semantics, and permissions of the statements, and then performs the requested actions on the data.

DML statements can be used in various contexts, such as interactive SQL sessions, stored procedures, triggers, functions, or applications that connect to the database.

DML statements can be classified into two types: read-only and write-only.

- Read-only DML statements are those that only retrieve data from the database, such as SELECT.
- Write-only DML statements are those that modify the data in the database, such as INSERT, UPDATE, and DELETE.

Write-only DML statements can affect the integrity, consistency, and concurrency of the data, and therefore they are subject to various constraints, rules, and mechanisms, such as primary keys, foreign keys, check constraints, default values, triggers, transactions, locks, etc., to ensure the data quality and prevent data anomalies.



### DCL

- Data Control Language (DCL) is a sublanguage of SQL that deals with the commands used to control the access and privileges of users on the database  .
- DCL is used for enforcing data security and ensuring that only authorized users can perform certain operations on the database .
- The main DCL commands in SQL are:
  - **GRANT**: This command is used to grant (give access to) security privileges to specific database users or roles  . It can be used to restrict or allow user access to INSERT, DELETE, SELECT, UPDATE, EXECUTE, ALTER or other operations on the database objects . For example, `GRANT SELECT ON employees TO user1;` grants the privilege to select data from the employees table to user1.
  - **REVOKE**: This command is used to revoke (take away) security privileges from specific database users or roles  . It can be used to remove or reduce user access to the database objects or operations . For example, `REVOKE SELECT ON employees FROM user1;` revokes the privilege to select data from the employees table from user1.
  - **DENY**: This command is used to deny (block) security privileges to specific database users or roles. It can be used to override the privileges granted by the GRANT command or inherited from the role membership. For example, `DENY SELECT ON employees TO user1;` denies the privilege to select data from the employees table to user1, even if user1 has been granted the SELECT privilege by another command or role.



# Advantages of SQL

SQL is a widely used language for managing and manipulating data in relational database management systems (RDBMS). Some of the advantages of using SQL are:

- **Faster and efficient query processing.** SQL can process large amounts of data in a very short amount of time. SQL uses set-based operations and optimized algorithms to perform operations like insertion, deletion, updating, and retrieval of data  .
- **No coding skills required.** SQL is a declarative language, which means that the user only needs to specify what data they want, not how to get it. SQL uses simple English phrases and keywords, such as SELECT, FROM, WHERE, GROUP BY, etc., to express queries .
- **Standardized language.** SQL is a standardized language that follows the ANSI (American National Standards Institute) and ISO (International Organization for Standardization) standards. This means that SQL is compatible with different RDBMS, such as MySQL, Oracle, SQL Server, etc., with minor variations .
- **Integration with other languages.** SQL can be easily integrated with other programming languages, such as Java, Python, C#, etc., to perform complex tasks and applications. SQL can also be embedded in HTML pages to create dynamic web pages that interact with databases .
- **Data security and integrity.** SQL provides various features and mechanisms to ensure the security and integrity of the data stored in the databases. SQL allows the user to define access privileges and permissions for different users and roles, to prevent unauthorized access or modification of data. SQL also supports constraints, such as primary keys, foreign keys, unique keys, etc., to enforce the relationships and rules among the data .



### SQL data type and literals

- SQL data types are the attributes that define the kind of value that can be stored in a column of a table or a variable in a program.
- SQL data types can be categorized into numeric, character, date and time, Boolean, and special types.
- Numeric data types can store integer, decimal, or floating-point numbers. Examples are INT, DECIMAL, FLOAT, etc.
- Character data types can store strings of characters, such as names, addresses, or descriptions. Examples are CHAR, VARCHAR, TEXT, etc.
- Date and time data types can store values that represent dates, times, or intervals. Examples are DATE, TIME, DATETIME, etc.
- Boolean data types can store values that are either true or false. Examples are BIT, BOOLEAN, etc.
- Special data types can store values that are not easily classified into the other categories, such as binary data, spatial data, or XML data. Examples are BLOB, GEOMETRY, XML, etc.
- SQL literals are the constant values that can be used in SQL statements or expressions. They are also called constants or scalars.
- SQL literals can be classified into four types: numeric, character, date and time, and Boolean literals.
- Numeric literals are the values that represent numbers, such as 42, 3.14, or -0.5. They can be written with or without a decimal point, and can have an optional sign (+ or -) at the beginning.
- Character literals are the values that represent strings of characters, such as 'Hello', 'SQL', or '2023'. They are enclosed in single quotes (' '), and can contain any character except the single quote itself. To include a single quote in a character literal, it must be doubled (''').
- Date and time literals are the values that represent dates, times, or intervals, such as '2023-03-15', '22:11:26', or '1 YEAR'. They are enclosed in single quotes (' '), and must follow a specific format depending on the data type they are assigned to.
- Boolean literals are the values that represent true or false, such as TRUE, FALSE, or NULL. They are not enclosed in quotes, and are case-insensitive. NULL means unknown or missing value.



### Types of SQL Commands

SQL commands are instructions that are used to communicate with the database and perform various tasks. SQL commands can be classified into five main categories, based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of the database objects, such as tables, views, indexes, etc. Some examples of DDL commands are:

  - `CREATE`: This command is used to create a new database object, such as a table, view, index, etc.
  - `ALTER`: This command is used to modify the structure or attributes of an existing database object, such as adding, dropping, or renaming columns, constraints, etc.
  - `DROP`: This command is used to delete an existing database object, such as a table, view, index, etc.
  - `RENAME`: This command is used to change the name of an existing database object, such as a table, view, index, etc.
  - `TRUNCATE`: This command is used to delete all the data from a table, but not the table structure.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from the database tables. Some examples of DML commands are:

  - `INSERT`: This command is used to insert new data into a table.
  - `UPDATE`: This command is used to modify the existing data in a table.
  - `DELETE`: This command is used to delete the existing data from a table.
  - `SELECT`: This command is used to query data from one or more tables, based on certain criteria.

- **Data Query Language (DQL)**: This is a subset of DML commands that are used to query data from the database tables. The main DQL command is:

  - `SELECT`: This command is used to query data from one or more tables, based on certain criteria. It can also be used to perform various operations on the data, such as sorting, filtering, grouping, aggregating, joining, etc.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of the database users and roles. Some examples of DCL commands are:

  - `GRANT`: This command is used to grant privileges or permissions to a user or role, such as the ability to select, insert, update, or delete data from a table, view, etc.
  - `REVOKE`: This command is used to revoke or remove the privileges or permissions that were previously granted to a user or role.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, such as committing, rolling back, or saving the changes made by the DML commands. Some examples of TCL commands are:

  - `COMMIT`: This command is used to save the changes made by the DML commands in the database permanently.
  - `ROLLBACK`: This command is used to undo the changes made by the DML commands in the database and restore the previous state.
  - `SAVEPOINT`: This command is used to create a point in the transaction where the changes can be rolled back to, in case of any error or failure.



### SQL operators and their procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They are used to specify conditions, filter results, compare values, perform calculations, concatenate strings, and more. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used for mathematical operations on numerical data, such as adding, subtracting, multiplying, dividing, and finding the remainder. The arithmetic operators in SQL are `+`, `-`, `*`, `/`, and `%`. For example, `SELECT 10 + 10;` returns 20.
- Comparison operators: These operators are used to compare two values or expressions and return a boolean value (true or false). The comparison operators in SQL are `=`, `<>`, `<`, `>`, `<=`, `>=`, `!=`, `!<`, `!>`, `IS NULL`, `IS NOT NULL`, `LIKE`, `NOT LIKE`, `IN`, `NOT IN`, `BETWEEN`, `NOT BETWEEN`, `EXISTS`, and `NOT EXISTS`. For example, `SELECT * FROM customers WHERE age > 30;` returns all the customers whose age is greater than 30.
- Logical operators: These operators are used to combine two or more conditions or expressions and return a boolean value. The logical operators in SQL are `AND`, `OR`, and `NOT`. For example, `SELECT * FROM products WHERE price > 100 AND category = 'Electronics';` returns all the products whose price is greater than 100 and category is 'Electronics'.
- Bitwise operators: These operators are used to perform bitwise operations on binary data, such as shifting, rotating, and masking. The bitwise operators in SQL are `&`, `|`, `^`, `~`, `<<`, and `>>`. For example, `SELECT 10 & 5;` returns 0, which is the result of bitwise AND operation on 10 and 5.
- String operators: These operators are used to manipulate string data, such as concatenating, extracting, replacing, and trimming. The string operators in SQL are `+`, `||`, `SUBSTRING`, `REPLACE`, `LTRIM`, `RTRIM`, and `TRIM`. For example, `SELECT 'Hello' + ' ' + 'World';` returns 'Hello World', which is the result of concatenating two strings with a space.
- Set operators: These operators are used to combine the results of two or more queries into a single result set. The set operators in SQL are `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT`. For example, `SELECT name FROM customers UNION SELECT name FROM suppliers;` returns the names of both customers and suppliers, without any duplicates.



### Tables – Creation & Alteration

- A table is a collection of data organized in rows and columns in a relational database.
- To create a table in SQL, use the `CREATE TABLE` statement, followed by the table name and the column definitions.
- For example, to create a table called `Students` with four columns: `id`, `name`, `age`, and `grade`, the syntax would be:

```sql
CREATE TABLE Students (
  id int,
  name varchar(50),
  age int,
  grade char(1)
);
```

- To add data to a table, use the `INSERT INTO` statement, followed by the table name, the column names, and the values to insert.
- For example, to insert a row into the `Students` table, the syntax would be:

```sql
INSERT INTO Students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
```

- To modify the structure of a table, use the `ALTER TABLE` statement, followed by the table name and the changes to make.
- For example, to add a new column called `email` to the `Students` table, the syntax would be:

```sql
ALTER TABLE Students ADD email varchar(50);
```

- To delete a table, use the `DROP TABLE` statement, followed by the table name.
- For example, to delete the `Students` table, the syntax would be:

```sql
DROP TABLE Students;
```

- To delete all the data from a table, but keep the table structure, use the `TRUNCATE TABLE` statement, followed by the table name.
- For example, to delete all the data from the `Students` table, the syntax would be:

```sql
TRUNCATE TABLE Students;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` statement, followed by the new table name and a `SELECT` query that specifies the columns and data to copy.
- For example, to create a new table called `Graduates` that is a copy of the `Students` table with only the students who have grade 'A', the syntax would be:

```sql
CREATE TABLE Graduates AS
SELECT id, name, age, grade
FROM Students
WHERE grade = 'A';
```

- To rename a table, use the `ALTER TABLE` statement, followed by the old table name, the `RENAME TO` keyword, and the new table name.
- For example, to rename the `Graduates` table to `Alumni`, the syntax would be:

```sql
ALTER TABLE Graduates RENAME TO Alumni;
```

- To change the data type or size of a column, use the `ALTER TABLE` statement, followed by the table name, the `ALTER COLUMN` keyword, the column name, and the new data type or size.
- For example, to change the data type of the `age` column in the `Students` table from `int` to `smallint`, the syntax would be:

```sql
ALTER TABLE Students ALTER COLUMN age smallint;
```

- To add a constraint to a table or a column, use the `ALTER TABLE` statement, followed by the table name, the `ADD` keyword, and the constraint definition.
- For example, to add a primary key constraint to the `id` column in the `Students` table, the syntax would be:

```sql
ALTER TABLE Students ADD PRIMARY KEY (id);
```

- To remove a constraint from a table or a column, use the `ALTER TABLE` statement, followed by the table name, the `DROP` keyword, and the constraint name.
- For example, to remove the primary key constraint from the `id` column in the `Students` table, the syntax would be:

```sql
ALTER TABLE Students DROP PRIMARY KEY;
```

- To view the structure and data of a table, use the `DESCRIBE` or `DESC` statement, followed by the table name, or the `SELECT` statement, followed by the columns and the table name.
- For example, to view the structure of the `Students` table, the syntax would be:

```sql
DESCRIBE Students;
```

- To view the data of the `Students` table, the syntax would be:

```sql
SELECT * FROM Students;
```



Hello, I am Sydney, your AI assistant. I can help you with your topic.

### Defining Constraints for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- Constraints are rules that are applied to the columns or tables in a database to ensure the validity and integrity of the data.
- Constraints can be defined at the column level or the table level, depending on the scope of the rule.
- Constraints can be specified when creating or altering a table using the CREATE TABLE or ALTER TABLE statements in SQL.
- Some of the common types of constraints are:

  - **NOT NULL**: This constraint ensures that a column cannot have a null value, which means it must have a value in every row of the table.
  - **UNIQUE**: This constraint ensures that a column or a combination of columns has a unique value in every row of the table, which means no two rows can have the same value for that column or combination of columns.
  - **PRIMARY KEY**: This constraint identifies a column or a combination of columns as the primary key of the table, which means it uniquely identifies each row of the table. A primary key also implies a NOT NULL and a UNIQUE constraint on the column or combination of columns.
  - **FOREIGN KEY**: This constraint establishes a relationship between a column or a combination of columns in one table and a primary key or a unique key in another table, which means the value of the column or combination of columns in the first table must match the value of the primary key or unique key in the second table. This ensures the referential integrity of the data across tables.
  - **CHECK**: This constraint allows specifying a condition that must be satisfied by the value of a column or a combination of columns in every row of the table, which means the value of the column or combination of columns must meet the criteria defined by the condition.
  - **DEFAULT**: This constraint allows specifying a default value for a column, which means if a value is not provided for the column when inserting a new row, the default value will be used instead.

- Constraints can be named or unnamed. If a constraint is named, the name must be unique within the schema. If a constraint is unnamed, the system will generate a name for it automatically.
- Constraints can be enabled or disabled. If a constraint is enabled, it will be enforced by the system and any violation will result in an error. If a constraint is disabled, it will not be enforced by the system and any violation will be ignored. Constraints can be enabled or disabled using the ENABLE or DISABLE keywords in the CREATE TABLE or ALTER TABLE statements.
- Constraints can be validated or not validated. If a constraint is validated, it will be checked by the system for all the existing rows in the table and any violation will result in an error. If a constraint is not validated, it will not be checked by the system for the existing rows in the table, but it will be enforced for any new or modified rows. Constraints can be validated or not validated using the VALIDATE or NOVALIDATE keywords in the CREATE TABLE or ALTER TABLE statements.



# Views and Indexes in SQL

## Views

- A view is a named query that is stored in the database and can be used to access or manipulate data from one or more tables.
- A view does not contain any data or exist in physical storage, but it acts like a virtual table that can be queried or updated.
- A view can be used to:
  - Limit a user's access to specific rows and columns of a table.
  - Manipulate data from multiple tables as if all the data were contained in a single table.
  - Simplify complex queries and hide their details.
  - Provide a consistent interface to the underlying data, even if the data structure changes.
- A view can be created using the CREATE VIEW statement, followed by the name of the view and the SELECT query that defines the view.
- A view can be queried or updated using the same syntax as a table, as long as the view is updatable.
- A view can be dropped using the DROP VIEW statement, followed by the name of the view.

## Indexes

- An index is a data structure that improves the speed of data retrieval operations on a table by creating a pointer to the data in a specific column or a set of columns.
- An index can be used to:
  - Reduce the amount of data that needs to be scanned by the query optimizer.
  - Sort and group data more efficiently.
  - Enforce uniqueness and referential integrity constraints on the table.
- An index can be created using the CREATE INDEX statement, followed by the name of the index, the name of the table, and the name of the column or columns to be indexed.
- An index can be dropped using the DROP INDEX statement, followed by the name of the index and the name of the table.

## Indexed Views

- An indexed view is a view that has a unique clustered index on it, which physically stores the view data in the database and makes the view act like a table.
- An indexed view can be used to:
  - Improve the performance of queries that join and aggregate data from multiple tables.
  - Write fewer pages to disk than the underlying tables, meaning fewer pages queries need to read fewer pages to return results.
  - Create statistics for the view that optimize cardinality estimations.
- An indexed view can be created using the CREATE VIEW statement with the WITH SCHEMABINDING option, followed by the name of the view and the SELECT query that defines the view, and then using the CREATE UNIQUE CLUSTERED INDEX statement, followed by the name of the index and the name of the view.
- An indexed view can be dropped using the DROP VIEW statement, followed by the name of the view, or using the DROP INDEX statement, followed by the name of the index and the name of the view.
- An indexed view has some limitations and requirements, such as:
  - The view must be schema-bound to the base tables, meaning the view definition cannot be changed and the base tables cannot be modified in a way that affects the view.
  - The view must not contain any non-deterministic expressions, such as GETDATE(), NEWID(), or RAND().
  - The view must not contain any outer or self joins, subqueries, or derived tables.
  - The view must contain a COUNT_BIG(*) expression in the SELECT list.
  - The view must be referenced by the query optimizer to produce the query plan, which depends on the SET options of the session.
  - Any insert, update, or delete operation performed on any table that participates in the indexed view must also update the indexed view, which may incur some overhead .

: Database Design - Views & indexes - California State University, Long Beach
: SQL Server Indexed Views: The Basics - Simple Talk
: Create Indexed Views - SQL Server | Microsoft Learn
: sql - How do indexes work on views? - Stack Overflow
: Tables, Views and Indexes in SQL - theintactone



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on queries and subqueries in SQL.

### Queries and Subqueries in SQL

- A query is a request for data or information from a database table or combination of tables. A query can be written using the SQL language, which stands for Structured Query Language. SQL is a standard language for accessing and manipulating data in databases.
- A subquery is a query within another query. The outer query is called the main query, and the inner query is called the subquery. A subquery can be nested inside the SELECT, FROM, WHERE, HAVING, or JOIN clause of the main query.
- A subquery can return a single value, a single row, a single column, or a table. Depending on the type of subquery, it can be used with different operators or clauses in the main query. For example, a subquery that returns a single value can be used with comparison operators like =, <, >, etc. A subquery that returns a table can be used with the IN, EXISTS, or ANY/ALL operators or as a derived table in the FROM clause.
- A subquery can be used for various purposes, such as filtering, aggregation, calculation, or joining data from different tables. Some examples of subqueries are:

  - Finding the customers who have the same name as the employees:

    ```sql
    SELECT customer_name, customer_id
    FROM customers
    WHERE customer_name IN
      (SELECT employee_name FROM employees);
    ```

  - Finding the average salary of the employees in each department:

    ```sql
    SELECT department_id, department_name, 
      (SELECT AVG(salary) FROM employees
       WHERE employees.department_id = departments.department_id) AS avg_salary
    FROM departments;
    ```

  - Finding the products that have a higher price than the average price of all products:

    ```sql
    SELECT product_id, product_name, product_price
    FROM products
    WHERE product_price >
      (SELECT AVG(product_price) FROM products);
    ```

  - Finding the orders that have a total amount greater than 1000:

    ```sql
    SELECT order_id, order_date, customer_id, 
      (SELECT SUM(quantity * unit_price) FROM order_details
       WHERE order_details.order_id = orders.order_id) AS total_amount
    FROM orders
    WHERE total_amount > 1000;
    ```

  - Joining the customers and orders tables using a subquery:

    ```sql
    SELECT customer_name, order_id, order_date
    FROM customers
    JOIN
      (SELECT order_id, order_date, customer_id FROM orders
       WHERE order_date BETWEEN '2022-01-01' AND '2022-01-31') AS recent_orders
    ON customers.customer_id = recent_orders.customer_id;
    ```

- A subquery can also be correlated or uncorrelated. A correlated subquery is a subquery that depends on the main query for its values. A correlated subquery is executed once for each row of the main query. An uncorrelated subquery is a subquery that does not depend on the main query for its values. An uncorrelated subquery is executed only once and its result is used for the main query. For example, the subquery in the second example above is correlated, while the subquery in the third example above is uncorrelated.



### Aggregate Functions for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- Aggregate functions are SQL functions that perform calculations on a set of values and return a single value  .
- Aggregate functions can be used in the select list of a SELECT statement, or in a HAVING clause to filter the grouped rows.
- Some of the common aggregate functions are:
  - AVG: returns the average of the values in a column   .
  - COUNT: returns the number of rows in a table or the number of non-null values in a column   .
  - MAX: returns the maximum value in a column   .
  - MIN: returns the minimum value in a column   .
  - SUM: returns the sum of the values in a column   .
- Aggregate functions can be combined with the GROUP BY clause to calculate the aggregate values for each group of rows that share the same values in the specified columns   .
- Aggregate functions can also be combined with the HAVING clause to filter the groups based on a condition that involves the aggregate values  .
- Aggregate functions ignore null values in the columns, except for the COUNT function, which counts null values as well   .
- Aggregate functions can be nested inside other aggregate functions, as long as they operate on different columns.
- Some examples of using aggregate functions are:

```sql
-- Find the average salary of all employees
SELECT AVG(salary) FROM employees;

-- Find the number of employees in each department
SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;

-- Find the highest salary in each department
SELECT department_id, MAX(salary) FROM employees GROUP BY department_id;

-- Find the total salary of each department that is more than 100000
SELECT department_id, SUM(salary) FROM employees GROUP BY department_id HAVING SUM(salary) > 100000;

-- Find the number of distinct job titles in the company
SELECT COUNT(DISTINCT job_title) FROM employees;
```



### Built-in functions

Built-in functions are expressions that perform some operation using SQL keywords or special operators. They can be used in SQL SELECT statements to calculate values and manipulate data. They can also be used in other SQL clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.

There are different types of built-in functions in SQL, depending on the purpose and the data type they operate on. Some of the common types are:

- **Aggregate functions**: These functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause to summarize data. Examples of aggregate functions are SUM, AVG, MIN, MAX, COUNT, etc.
- **Analytic functions**: These functions compute an aggregate value based on a group of rows, but unlike aggregate functions, they do not reduce the number of rows in the result. They are often used with the OVER clause to partition the data and apply a window function. Examples of analytic functions are RANK, ROW_NUMBER, LAG, LEAD, etc.
- **String functions**: These functions perform various operations on string values, such as concatenation, extraction, replacement, conversion, etc. Examples of string functions are CONCAT, SUBSTRING, REPLACE, UPPER, LOWER, etc.
- **Numeric functions**: These functions perform various operations on numeric values, such as arithmetic, rounding, truncation, conversion, etc. Examples of numeric functions are ABS, CEILING, FLOOR, POWER, SQRT, CAST, etc.
- **Date and time functions**: These functions perform various operations on date and time values, such as extraction, addition, subtraction, conversion, formatting, etc. Examples of date and time functions are GETDATE, DATEADD, DATEDIFF, DATEPART, FORMAT, etc.
- **Logical functions**: These functions perform various operations on logical values, such as comparison, negation, conjunction, disjunction, etc. Examples of logical functions are AND, OR, NOT, IF, CASE, etc.
- **Bit manipulation functions**: These functions perform various operations on bit values, such as shifting, rotating, masking, etc. Examples of bit manipulation functions are BITAND, BITOR, BITNOT, BITXOR, etc.

The syntax and usage of each built-in function may vary depending on the SQL dialect and the database system. Therefore, it is important to consult the documentation of the specific SQL server or database management system for more details and examples.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes for the topic of Structured Query Language (SQL) in the subject of Basics of Data Base Management System.

### Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several keywords, clauses, expressions, and operators that specify what operations to perform on the data.
- SQL is divided into four sublanguages: Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL is used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and constraints.
- DML is used to insert, update, delete, and merge data in the database tables.
- DCL is used to grant and revoke permissions and roles to users and groups for accessing and modifying the database.
- DQL is used to retrieve and analyze data from the database tables, using various clauses such as SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, and JOIN.
- SQL also supports various functions, such as aggregate functions, string functions, date functions, and mathematical functions, that can be applied to the data in the queries.
- SQL also supports various commands, such as COMMIT, ROLLBACK, SAVEPOINT, and SET TRANSACTION, that can be used to control the transactions and ensure the consistency and integrity of the data.
- SQL is a declarative language, which means that it specifies what result to obtain, not how to obtain it. The database management system (DBMS) is responsible for executing the SQL queries and returning the results.



### Update and Delete Operations for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- SQL is a language that allows users to view and manage data in a relational database system.
- Data Manipulation Language (DML) is a subset of SQL that deals with inserting, updating, deleting, and selecting data from tables and views.
- The UPDATE command is used to modify the existing records in the database. It has the following syntax:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The SET clause specifies which columns to update and what values to assign to them.
- The WHERE clause is optional and filters the records that match the condition. If the WHERE clause is omitted, all the records in the table will be updated.
- The UPDATE command can also use expressions, subqueries, and joins to update data from multiple tables or sources.
- The DELETE command is used to remove the records from the table that are no longer required. It has the following syntax:

```sql
DELETE FROM table_name
WHERE condition;
```

- The WHERE clause is optional and filters the records that match the condition. If the WHERE clause is omitted, all the records in the table will be deleted.
- The DELETE command can also use subqueries and joins to delete data from multiple tables or sources.
- Both the UPDATE and DELETE commands can use the TOP keyword to limit the number of rows affected by the operation. For example:

```sql
UPDATE TOP (10) table_name
SET column1 = value1
WHERE condition;

DELETE TOP (10) FROM table_name
WHERE condition;
```

- The above commands will update or delete only the first 10 rows that match the condition.
- Both the UPDATE and DELETE commands can use the OUTPUT clause to return the modified or deleted rows as a result set. For example:

```sql
UPDATE table_name
SET column1 = value1
OUTPUT inserted.column1, deleted.column1
WHERE condition;

DELETE FROM table_name
OUTPUT deleted.*
WHERE condition;
```

- The above commands will return the new and old values of column1 for the updated rows, and the entire deleted rows, respectively.
- Both the UPDATE and DELETE commands can be customized by using stored procedures, triggers, or user-defined functions to implement business logic or validation rules. For example, a trigger can be defined to audit the changes made by the UPDATE or DELETE commands, or a stored procedure can be used to perform complex calculations or validations before updating or deleting data.
- Both the UPDATE and DELETE commands should be used with caution, as they can cause data loss or inconsistency if not performed correctly. Some of the best practices for using these commands are:

  - Always use a WHERE clause to limit the scope of the operation, unless you want to affect all the rows in the table.
  - Always test the WHERE clause with a SELECT statement before executing the UPDATE or DELETE command, to verify that the correct rows are selected.
  - Always use transactions to ensure the atomicity and consistency of the operation, and to be able to roll back the changes in case of errors or exceptions.
  - Always use appropriate locking or isolation levels to prevent concurrency issues or data corruption, especially when updating or deleting data from multiple tables or sources.
  - Always backup the database or the table before performing the UPDATE or DELETE operation, to be able to restore the data in case of accidental or unwanted changes.



### Joins

- Joins are commands that combine rows from two or more tables, based on a related column between those tables  .
- Joins are useful when a user wants to extract data from tables that have one-to-many or many-to-many relationships .
- There are four main types of joins: inner join, left join, right join, and full join   .
- An inner join returns only the rows that match in both tables   .
- A left join returns all the rows from the left table, and the matching rows from the right table, or null if there is no match   .
- A right join returns all the rows from the right table, and the matching rows from the left table, or null if there is no match   .
- A full join returns all the rows from both tables, and null values for the columns that do not match    .
- The syntax for joins is as follows:

```sql
SELECT column_name(s)
FROM table1
JOIN table2
ON table1.column_name = table2.column_name;
```

- The JOIN keyword can be replaced by INNER JOIN, LEFT JOIN, RIGHT JOIN, or FULL JOIN to specify the type of join .
- The ON clause specifies the join condition, which is the column or columns that are used to relate the tables  .
- The ORDER BY clause can be used to sort the result set by one or more columns .
- Here is an example of an inner join between two tables, Customers and Orders, based on the CustomerID column:

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;
```

- This query returns the customer name and order ID for each order that has a matching customer ID in both tables.



### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union removes any duplicate rows from the combined result set, unless the UNION ALL option is used, which preserves all rows.
- A union can be used to combine data from different tables or views that have the same or compatible column names and data types.
- A union can also be used to combine data from different databases or servers, as long as they support the same SQL dialect and have a common connection.
- The syntax of a union is:

```sql
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_1
UNION [ALL]
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_2
UNION [ALL]
...
UNION [ALL]
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_m;
```

- The number, order, and data type of the columns in each SELECT query must be the same or convertible.
- The column names in the result set are taken from the first SELECT query, unless aliases are used.
- The result set can be sorted by using the ORDER BY clause after the last SELECT query, but not within each individual query.
- The result set can be filtered by using the WHERE clause before the first SELECT query, but not after the UNION operator.
- The result set can be limited by using the LIMIT or TOP clause after the ORDER BY clause, but not within each individual query.
- The result set can be grouped by using the GROUP BY and HAVING clauses before the first SELECT query, but not after the UNION operator.
- The result set can be joined with other tables or views by using the JOIN clause before the first SELECT query, but not after the UNION operator.

- Some examples of using unions are:

  - To combine data from two tables that have the same columns:

  ```sql
  SELECT name, age, gender
  FROM students
  UNION
  SELECT name, age, gender
  FROM teachers;
  ```

  - To combine data from two tables that have different columns, but compatible data types:

  ```sql
  SELECT name, salary, NULL AS department
  FROM employees
  UNION
  SELECT name, NULL AS salary, department
  FROM managers;
  ```

  - To combine data from two tables that have different columns, and use aliases to rename them:

  ```sql
  SELECT name AS person_name, email AS contact_info
  FROM customers
  UNION
  SELECT company_name AS person_name, phone AS contact_info
  FROM suppliers;
  ```

  - To combine data from two tables and sort the result set by a column:

  ```sql
  SELECT name, price
  FROM products
  UNION
  SELECT name, price
  FROM services
  ORDER BY price DESC;
  ```

  - To combine data from two tables and limit the result set to 10 rows:

  ```sql
  SELECT name, price
  FROM products
  UNION
  SELECT name, price
  FROM services
  ORDER BY price DESC
  LIMIT 10;
  ```

  - To combine data from two tables and filter the result set by a condition:

  ```sql
  SELECT name, price
  FROM products
  WHERE price > 100
  UNION
  SELECT name, price
  FROM services
  WHERE price > 100;
  ```

  - To combine data from two tables and group the result set by a column:

  ```sql
  SELECT name, SUM(price) AS total_price
  FROM (
    SELECT name, price
    FROM products
    UNION
    SELECT name, price
    FROM services
  ) AS subquery
  GROUP BY name;
  ```

  - To combine data from two tables and join the result set with another table:

  ```sql
  SELECT subquery.name, subquery.price, categories.category
  FROM (
    SELECT name, price, category_id
    FROM products
    UNION
    SELECT name, price, category_id
    FROM services
  ) AS subquery
  JOIN categories
  ON subquery.category_id = categories.id;
  ```

  - To combine data from two databases or servers that have the same table structure:

  ```sql
  SELECT name, price
  FROM db1.products
  UNION
  SELECT name, price
  FROM db2.products;
  ```



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of intersection for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here is the content I have written in markdown format:

### Intersection
- The intersection operation in SQL is used to combine two queries and return only the records that are common to both the queries.
- The syntax of the intersection operation is:

```sql
SELECT column_list
FROM table1
WHERE condition1
INTERSECT
SELECT column_list
FROM table2
WHERE condition2;
```

- The column_list in both the queries must have the same number and order of columns, and the data types must be compatible.
- The intersection operation eliminates any duplicate rows from the result set.
- The intersection operation is equivalent to the logical AND operation between two queries.
- For example, suppose we have two tables, `students` and `employees`, with the following data:

| id | name | age | department |
|----|------|-----|------------|
| 1  | Alice| 22  | CS         |
| 2  | Bob  | 23  | EE         |
| 3  | Carol| 24  | CS         |
| 4  | David| 25  | ME         |

| id | name | salary | department |
|----|------|--------|------------|
| 1  | Alice| 50000  | CS         |
| 2  | Bob  | 60000  | EE         |
| 5  | Eve  | 70000  | CS         |
| 6  | Frank| 80000  | ME         |

- To find the records that are common to both the tables, we can use the intersection operation as follows:

```sql
SELECT id, name, department
FROM students
INTERSECT
SELECT id, name, department
FROM employees;
```

- The result of this query will be:

| id | name | department |
|----|------|------------|
| 1  | Alice| CS         |
| 2  | Bob  | EE         |



### Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL is used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and constraints.
- DML is used to insert, update, delete, and merge data in the database tables.
- DCL is used to grant and revoke permissions and privileges to users and roles on the database objects.
- DQL is used to retrieve and manipulate data from the database tables using various clauses, operators, functions, and expressions.
- SQL follows a set of rules and syntax for writing statements and commands, which can vary slightly depending on the database system and vendor.
- SQL statements are composed of keywords, identifiers, literals, symbols, and comments.
- SQL keywords are reserved words that have a specific meaning and function in SQL, such as SELECT, FROM, WHERE, GROUP BY, etc.
- SQL identifiers are user-defined names for database objects, such as tables, columns, views, etc. They must follow certain naming conventions and rules, such as starting with a letter, not containing spaces or special characters, etc.
- SQL literals are constant values that represent data, such as strings, numbers, dates, etc. They must be enclosed in single or double quotes, depending on the data type and the database system.
- SQL symbols are punctuation marks and operators that separate and combine SQL elements, such as commas, parentheses, asterisks, plus signs, etc.
- SQL comments are remarks or explanations that are ignored by the SQL interpreter, but can help document and understand the SQL code. They can be either single-line or multi-line, depending on the database system and the comment delimiter.



### Transaction Control Commands

Transaction control commands are used to manage the changes made by SQL statements in a database. A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a whole. Transactions ensure the consistency and integrity of the data in the database by following the ACID properties: atomicity, consistency, isolation, and durability.

The main transaction control commands in SQL are:

- **COMMIT**: This command is used to make the changes made by a transaction permanent in the database. It ends the current transaction and saves the work done. It also releases any locks held by the transaction on the data.
- **ROLLBACK**: This command is used to undo the changes made by a transaction and restore the database to its previous state. It ends the current transaction and discards the work done. It also releases any locks held by the transaction on the data.
- **SAVEPOINT**: This command is used to create points within a transaction that can be used to roll back to a specific state in case of an error or failure. A savepoint is a name given to a point in the transaction. Multiple savepoints can be created within a transaction. To roll back to a savepoint, the ROLLBACK TO SAVEPOINT command is used.
- **SET TRANSACTION**: This command is used to specify the characteristics of the current transaction, such as its isolation level, read-only or read-write mode, and name. It must be the first statement of a transaction and can only be executed once per transaction.

Some examples of transaction control commands are:

```sql
-- Start a transaction
BEGIN TRANSACTION;

-- Insert a record into a table
INSERT INTO customers (id, name, email) VALUES (1, 'Alice', 'alice@example.com');

-- Create a savepoint
SAVEPOINT sp1;

-- Update a record in the table
UPDATE customers SET email = 'alice@gmail.com' WHERE id = 1;

-- Roll back to the savepoint
ROLLBACK TO SAVEPOINT sp1;

-- Commit the transaction
COMMIT;
```

```sql
-- Start a transaction with a name and isolation level
SET TRANSACTION NAME 'tran1' ISOLATION LEVEL SERIALIZABLE;

-- Delete a record from a table
DELETE FROM customers WHERE id = 1;

-- Roll back the transaction
ROLLBACK;
```



## Unit 6 - PL/SQL

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that allows users to write procedural code in Oracle database.
- PL/SQL supports variables, constants, data types, operators, expressions, control structures, loops, exceptions, cursors, subprograms, packages, triggers, and object-oriented features.
- PL/SQL code is stored in the database as compiled units, which can be executed by other programs or triggers.
- PL/SQL code can also be embedded in SQL statements, such as SELECT, INSERT, UPDATE, and DELETE, to perform complex calculations or validations.
- PL/SQL code can interact with the database using SQL statements, such as SELECT INTO, INSERT INTO, UPDATE, and DELETE, or using cursor variables, which can hold the result sets of queries.
- PL/SQL code can also use built-in functions, such as TO_CHAR, TO_DATE, TO_NUMBER, SUBSTR, LENGTH, etc., or user-defined functions, which can be created using the CREATE FUNCTION statement.
- PL/SQL code can handle errors and exceptions using the EXCEPTION block, which can catch predefined or user-defined exceptions, and use the RAISE statement to raise an exception explicitly.
- PL/SQL code can modularize and reuse code using subprograms, which are either procedures or functions. Procedures are subprograms that perform a specific task and do not return a value. Functions are subprograms that return a single value and can be used in expressions. Subprograms can be created using the CREATE PROCEDURE or CREATE FUNCTION statements, and can be invoked using the CALL statement or the subprogram name.
- PL/SQL code can organize and manage subprograms using packages, which are collections of related subprograms, variables, constants, cursors, and exceptions. Packages can be created using the CREATE PACKAGE and CREATE PACKAGE BODY statements, and can be invoked using the package name and the subprogram name.
- PL/SQL code can automate actions on database events using triggers, which are subprograms that are executed when a specific event occurs on a table, view, or schema. Triggers can be created using the CREATE TRIGGER statement, and can use the :NEW and :OLD pseudo-records to access the values of the affected row before and after the event. Triggers can be classified into row-level triggers, which are executed for each affected row, or statement-level triggers, which are executed once for the whole statement.
- PL/SQL code can also support object-oriented features, such as abstract data types, inheritance, polymorphism, and encapsulation. Abstract data types are user-defined data types that can have attributes and methods. They can be created using the CREATE TYPE statement, and can be used to define table columns or variables. Inheritance is the ability of a subtype to inherit the attributes and methods of a supertype. Polymorphism is the ability of a subprogram to behave differently depending on the type of the argument. Encapsulation is the ability to hide the implementation details of an abstract data type from the outside world.



### Introduction for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is a programming language that extends SQL, the standard language for accessing and manipulating data in relational databases.
- PL/SQL allows users to create stored procedures, functions, triggers, packages, and other program units that can be executed on the database server. PL/SQL also supports features such as variables, constants, data types, operators, expressions, control structures, loops, arrays, cursors, exceptions, and records.
- PL/SQL is designed to integrate seamlessly with SQL. Users can embed SQL statements in PL/SQL blocks, and use PL/SQL variables and parameters in SQL statements. PL/SQL also provides built-in functions and packages that can be used to manipulate data, handle errors, perform calculations, and interact with the database.
- PL/SQL is a compiled language. The PL/SQL compiler checks the syntax and semantics of the PL/SQL code, and generates an intermediate form that can be executed by the database server. The compiler also optimizes the code and performs error checking and debugging.
- PL/SQL is portable and platform-independent. Users can write PL/SQL code once and run it on any Oracle database server, regardless of the operating system or hardware. PL/SQL also supports interoperability with other programming languages, such as Java, C, and C++.
- PL/SQL is a powerful and flexible language that can enhance the functionality and performance of database applications. By using PL/SQL, users can reduce network traffic, improve security, enforce business rules, and encapsulate complex logic. PL/SQL also enables users to create reusable and modular code that can be maintained and modified easily.



# Features of PL/SQL

PL/SQL is a procedural extension of SQL that allows developers to write efficient and compact code for manipulating data in a database. Some of the features of PL/SQL are:

- **Tight integration with SQL**: PL/SQL can use SQL statements directly in its code, without any need for translation or interface. This allows PL/SQL to access and manipulate data in tables, views, and other database objects easily and efficiently   .
- **Extensive error checking**: PL/SQL can detect and handle errors at compile time and run time, using predefined and user-defined exceptions. PL/SQL also provides debugging tools and facilities to trace and monitor the execution of PL/SQL code   .
- **Numerous data types**: PL/SQL supports a variety of data types, including scalar, composite, reference, and large object (LOB) types. PL/SQL also allows the creation of user-defined types and subtypes, as well as the use of SQL data types and collection types   .
- **A variety of programming structures**: PL/SQL provides various programming structures, such as variables, constants, cursors, loops, conditional statements, and exception handlers, to help developers write clear and modular code. PL/SQL also supports the use of labels and GOTO statements for controlling the flow of execution   .
- **Structured programming through functions and procedures**: PL/SQL allows the creation and invocation of functions and procedures, which are subprograms that can be stored and executed in the database. Functions and procedures can be grouped into packages, which are collections of related subprograms and variables. PL/SQL also supports the use of triggers, which are subprograms that are automatically executed when certain events occur in the database   .
- **Object-oriented programming**: PL/SQL supports the creation and manipulation of objects, which are instances of user-defined types that can have attributes and methods. PL/SQL also supports the concepts of inheritance, polymorphism, and encapsulation, which are essential for object-oriented programming   .
- **Development of web applications and server pages**: PL/SQL can be used to create dynamic web pages and web services, using the PL/SQL Web Toolkit and the PL/SQL Gateway. PL/SQL can also generate HTML, XML, JSON, and other formats for web applications. PL/SQL can also interact with web servers, browsers, and other web components    .



# PL/SQL Syntax and Constructs

PL/SQL is a procedural extension of SQL that allows you to write complex and modular programs that interact with Oracle databases. PL/SQL programs are composed of blocks, which are the basic units of execution. A block can contain declarations, executable statements, and exception handlers. A block can also be nested inside another block, forming a hierarchical structure.

## PL/SQL Block Structure

The general syntax of a PL/SQL block is as follows:

```
DECLARE
  -- optional section for declaring variables, constants, cursors, exceptions, etc.
BEGIN
  -- mandatory section for executable statements
  -- at least one statement is required
EXCEPTION
  -- optional section for handling errors and exceptions
END;
-- mandatory terminator
/
-- optional symbol to execute the block
```

The DECLARE section is where you can declare identifiers such as variables, constants, cursors, exceptions, etc. that are local to the block. You can also initialize them with values or expressions. The declarations must follow the rules of PL/SQL identifiers, which are:

- They must begin with a letter.
- They can contain letters, digits, underscores, dollar signs, and number signs.
- They cannot exceed 30 characters in length.
- They cannot be reserved words or keywords.

The BEGIN section is where you can write executable statements that perform actions such as assigning values, calling procedures, looping, branching, etc. You must have at least one executable statement in this section. The statements must end with a semicolon (;).

The EXCEPTION section is where you can handle errors and exceptions that may occur during the execution of the block. You can use predefined or user-defined exceptions, and specify the actions to take when they are raised. You can also use the SQLCODE and SQLERRM functions to get the error code and message of the last exception.

The END keyword marks the end of the block. It must be followed by a semicolon (;). Optionally, you can also add a label to the END keyword to match the label of the block, if any.

The / symbol is used to execute the block in SQL*Plus or SQL Developer. It is not part of the PL/SQL syntax, but a command of the interactive tool. You can also use the EXECUTE or EXEC command to run a block.

## PL/SQL Block Types

There are three types of PL/SQL blocks: anonymous, subprogram, and trigger.

- An anonymous block is a block that has no name and is not stored in the database. It is used for one-time execution of a PL/SQL code. You can write an anonymous block in SQL*Plus or SQL Developer, or embed it in a host language such as Java or C#.
- A subprogram is a named block that is stored in the database and can be invoked repeatedly. There are two types of subprograms: procedures and functions. A procedure is a subprogram that performs a specific action, and may or may not return a value. A function is a subprogram that always returns a single value, and can be used in SQL statements or expressions.
- A trigger is a named block that is stored in the database and is executed automatically when a certain event occurs on a table or view. A trigger can be used to enforce business rules, audit changes, or perform other actions related to the data manipulation.

## PL/SQL Language Elements

PL/SQL supports many language elements that are common to other procedural languages, such as:

- Data types: PL/SQL supports scalar, composite, reference, and large object (LOB) data types. Scalar data types include numeric, character, boolean, date, and interval types. Composite data types include record, collection, and table types. Reference data types include cursor and REF CURSOR types. LOB data types include BLOB, CLOB, NCLOB, and BFILE types.
- Operators: PL/SQL supports arithmetic, relational, logical, bitwise, and string operators. You can use operators to manipulate values and expressions in PL/SQL statements.
- Expressions: PL/SQL supports various types of expressions, such as arithmetic, boolean, character, date, and null expressions. You can use expressions to assign values, compare values, or perform calculations in PL/SQL statements.
- Control structures: PL/SQL supports conditional, iterative, and sequential control structures. You can use control structures to control the flow of execution in PL/SQL blocks. Conditional control structures include IF-THEN-ELSE, CASE, and NULL statements. Iterative control structures include LOOP, WHILE, FOR, and EXIT statements. Sequential control structures include GOTO and NULL statements



### SQL within PL/SQL

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



### DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity on the data stored in the database tables or views .
- DML statements can be executed from within any PL/SQL block of code, such as procedures, functions, triggers, packages, etc.
- The four types of DML statements are: INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert new rows into a table or a view .
- UPDATE statement is used to modify the values of existing rows in a table or a view .
- DELETE statement is used to remove existing rows from a table or a view .
- MERGE statement is used to combine the data from two tables into one, based on a matching condition .
- DML statements can be executed either implicitly or explicitly in PL/SQL.
- Implicit execution means that the DML statement is executed automatically by the PL/SQL engine, without using the EXECUTE IMMEDIATE statement.
- Explicit execution means that the DML statement is executed by using the EXECUTE IMMEDIATE statement, which allows dynamic SQL execution.
- DML statements can also use bind variables, which are placeholders for actual values that are supplied at run time.
- Bind variables can improve the performance and security of DML statements, as they reduce the parsing overhead and prevent SQL injection attacks.
- DML statements can be followed by the RETURNING clause, which returns the values of the affected rows after the execution.
- The RETURNING clause can be used with bulk operations, such as FORALL, to return multiple rows at once.
- DML statements can also use the RETURNING BULK COLLECT INTO clause, which returns the values of the affected rows into a collection variable.
- DML statements can be combined with transaction control statements, such as COMMIT, ROLLBACK, and SAVEPOINT, to manage the changes made to the database.
- DML statements can also use the AUTONOMOUS_TRANSACTION pragma, which allows a subprogram to execute its own independent transaction, regardless of the main transaction.
- DML statements can raise exceptions, such as DUP_VAL_ON_INDEX, NO_DATA_FOUND, TOO_MANY_ROWS, etc, which can be handled by using the EXCEPTION section of the PL/SQL block.



### Cursors

A cursor is a pointer to a result set, or the data that results from a query. Cursors let you fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.

There are two types of cursors in PL/SQL: implicit cursors and explicit cursors.

- Implicit cursors are automatically created by Oracle whenever an SQL statement is executed. You can access the attributes of an implicit cursor using the SQL prefix. For example, SQL%ROWCOUNT returns the number of rows affected by the last SQL statement.
- Explicit cursors are user-defined cursors that allow you to name and control the result set of a query. You can declare, open, fetch, and close an explicit cursor using PL/SQL statements. You can also define parameters for an explicit cursor and use them in the query.

Some advantages of using cursors are:

- You can process each row individually and perform complex logic on it.
- You can avoid errors such as too many rows or no data found by handling exceptions.
- You can improve the performance of your queries by using cursor attributes and bulk operations.

Some disadvantages of using cursors are:

- You need to write more code to declare and manipulate cursors.
- You may consume more memory and CPU resources by fetching and processing large result sets.
- You may encounter locking issues if you update the data in the cursor and other sessions try to access the same data.



### Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database for reuse .
- A stored procedure can be invoked by other procedures, triggers, or applications written in Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to it. The body contains the executable statements and optional exception handlers .
- A stored procedure can have three types of parameters: IN, OUT, and IN OUT. IN parameters are used to pass values to the procedure. OUT parameters are used to return values from the procedure. IN OUT parameters are used to do both .
- A stored procedure can be created using the CREATE PROCEDURE statement. The syntax is as follows:

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
[(parameter_name [IN | OUT | IN OUT] parameter_type, ...)]
IS
  -- declare local variables
BEGIN
  -- executable statements
EXCEPTION
  -- exception handlers
END [procedure_name];
```

- A stored procedure can be executed using the EXECUTE or EXEC statement, or by calling it from another block of code. The syntax is as follows:

```sql
EXECUTE schema.procedure_name[(parameter_value, ...)];
EXEC schema.procedure_name[(parameter_value, ...)];
BEGIN
  schema.procedure_name[(parameter_value, ...)];
END;
```

- A stored procedure can be dropped using the DROP PROCEDURE statement. The syntax is as follows:

```sql
DROP PROCEDURE schema.procedure_name;
```

- A stored procedure can be modified using the CREATE OR REPLACE PROCEDURE statement, which replaces the existing procedure with the new one.
- A stored procedure can be viewed using the USER_PROCEDURES, ALL_PROCEDURES, or DBA_PROCEDURES data dictionary views.



### Stored function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement, another PL/SQL block, or a Java program .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must do so in a read-only manner .
- A stored function cannot contain DML statements that modify database data, such as INSERT, UPDATE, or DELETE .
- A stored function cannot contain transaction control statements, such as COMMIT or ROLLBACK .
- A stored function cannot return a result set, such as a cursor or a collection .

The syntax for creating a stored function is as follows :

```sql
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
-- declarative section
BEGIN
-- executable section
END;
```

- The CREATE OR REPLACE clause allows you to modify an existing function or create a new one if it does not exist .
- The function_name is the name of the function that must be unique within the schema .
- The parameter_list is a comma-separated list of parameters that can be of three modes: IN, OUT, or IN OUT .
- The IN mode indicates that the parameter is an input value that cannot be modified by the function .
- The OUT mode indicates that the parameter is an output value that can be modified by the function .
- The IN OUT mode indicates that the parameter is both an input and an output value that can be modified by the function .
- The return_type is the data type of the value that the function returns .
- The IS keyword marks the beginning of the function body .
- The declarative section is optional and can contain declarations of variables, constants, cursors, exceptions, or other local objects that are used by the function .
- The BEGIN keyword marks the beginning of the executable section that contains the logic of the function .
- The END keyword marks the end of the function body .

An example of a stored function that calculates the factorial of a given number is as follows:

```sql
CREATE OR REPLACE FUNCTION factorial (n IN NUMBER)
RETURN NUMBER
IS
  result NUMBER := 1;
BEGIN
  FOR i IN 1..n LOOP
    result := result * i;
  END LOOP;
  RETURN result;
END;
```

To execute a stored function, you can use one of the following methods:

- Use the function in a SQL statement, such as SELECT, INSERT, UPDATE, or DELETE.
- Use the function in a PL/SQL expression, such as an assignment, a conditional, or a loop.
- Use the function in a PL/SQL procedure or another function.
- Use the function in a Java program by using the CallableStatement interface.

An example of using the factorial function in a SQL statement is as follows:

```sql
SELECT factorial(5) FROM dual;
```

The output is:

```sql
FACTORIAL(5)
------------
120
```



### Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data.
- Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- Triggers can also be defined to run in response to DDL (Data Definition Language) actions such as CREATE, ALTER, and DROP  .
- Triggers can be used to implement complex data interactions, maintain the integrity of the information on the database, enforce business rules, audit data changes, and perform other tasks  .
- Triggers are defined on a table, stored in the associated database, and executed as a result of an event on that table or view.
- Triggers can be recursive, meaning that they can invoke themselves or other triggers, and nested, meaning that they can be called by other triggers.
- Triggers can be disabled or enabled, and their order of execution can be specified.
- Triggers can return results to the calling application or user, but this feature will be removed in a future version of SQL Server.
- Triggers can be created in the master database and behave just like those created in user-designed databases.
- Triggers can be queried by using the sys.triggers catalog view.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System. Here are the indices for the notes of the unit:

### Indices for the notes of the Unit 6 - PL/SQL

- Introduction to PL/SQL
  - What is PL/SQL and why use it?
  - Features and advantages of PL/SQL
  - PL/SQL architecture and environment
  - PL/SQL block structure and syntax
  - PL/SQL data types and variables
  - PL/SQL operators and expressions
- PL/SQL Control Structures
  - Conditional statements (IF, CASE)
  - Looping statements (FOR, WHILE, LOOP, EXIT, CONTINUE)
  - Sequential control statements (GOTO, NULL)
  - Exception handling (RAISE, EXCEPTION, PRAGMA EXCEPTION_INIT, SQLCODE, SQLERRM)
- PL/SQL Cursors and Records
  - What are cursors and why use them?
  - Types of cursors (implicit, explicit, parameterized, ref, bulk)
  - Cursor attributes (%FOUND, %NOTFOUND, %ROWCOUNT, %ISOPEN)
  - Cursor FOR loop
  - What are records and why use them?
  - Types of records (table-based, cursor-based, user-defined)
  - Record operations (assignment, comparison, INSERT, UPDATE, DELETE)
- PL/SQL Subprograms
  - What are subprograms and why use them?
  - Types of subprograms (procedures, functions, packages)
  - Subprogram parameters (IN, OUT, IN OUT, NOCOPY)
  - Subprogram overloading and resolution
  - Subprogram scope and visibility
  - Subprogram invocation and return
- PL/SQL Triggers
  - What are triggers and why use them?
  - Types of triggers (row, statement, DML, DDL, database, instead-of)
  - Trigger attributes (OLD, NEW, INSERTING, UPDATING, DELETING)
  - Trigger restrictions and guidelines
  - Trigger examples and applications
- PL/SQL Collections and Dynamic SQL
  - What are collections and why use them?
  - Types of collections (associative arrays, nested tables, varrays)
  - Collection methods (COUNT, EXISTS, EXTEND, TRIM, DELETE, PRIOR, NEXT, FIRST, LAST, LIMIT)
  - Collection examples and applications
  - What is dynamic SQL and why use it?
  - Types of dynamic SQL (EXECUTE IMMEDIATE, OPEN-FOR, OPEN-FOR-USING, DBMS_SQL)
  - Dynamic SQL examples and applications




```markdown
## Unit 7 - Transaction Processing Concepts

- A transaction is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either executes all or none of its operations.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it were the only one running on the database.
- Durability means that the effects of a transaction persist even if the system fails.
- A transaction processing system is a system that supports the execution of transactions on a large database with many concurrent users.
- A transaction processing system has three components: a transaction manager, a scheduler, and a recovery manager.
- A transaction manager is responsible for starting, committing, or aborting transactions.
- A scheduler is responsible for controlling the order of execution of operations from different transactions.
- A recovery manager is responsible for restoring the database to a consistent state in case of failures.
- A transaction processing system can use different techniques to ensure the ACID properties of transactions, such as locking, timestamping, logging, and checkpointing.
- A locking protocol is a set of rules that determines when a transaction can acquire or release locks on data items.
- A timestamping protocol is a set of rules that determines the order of execution of transactions based on their assigned timestamps.
- A logging protocol is a set of rules that determines what information is recorded in a log file for each transaction.
- A checkpointing protocol is a set of rules that determines when and how the database and the log file are synchronized.
```



### Transaction concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. Transactions are executed by users or applications to perform some tasks on the database. Transactions have the following characteristics:

- A transaction is a **single unit of logic** or work, that is either performed in its entirety or not at all .
- A transaction is **independent** of other transactions, meaning that its execution does not interfere with or depend on other transactions.
- A transaction is **coherent** and **reliable**, meaning that it preserves the consistency and integrity of the database.
- A transaction can be **committed** or **rolled back**, meaning that its effects are either made permanent or undone in the database .

Transactions in a database environment have two main purposes:

- To provide a **correct and consistent** view of the data to each user or application, regardless of concurrent access or system failures.
- To provide a **mechanism** for recovering from failures and maintaining the database in a consistent state.

Transactions are governed by the **ACID** properties, which are:

- **Atomicity**: The 'all or nothing' property. A transaction is an indivisible entity that is either performed in its entirety or not at all. If any part of the transaction fails, the whole transaction is aborted and the database is restored to its previous state.
- **Consistency**: A transaction must alter the database from one steady-state to another steady state. This means that the transaction must obey all the integrity constraints and business rules of the database, and not leave the database in an inconsistent or invalid state.
- **Isolation**: Transactions are executed in isolation from each other, meaning that their intermediate results are not visible to other transactions. This ensures that concurrent transactions do not interfere with each other and produce incorrect results.
- **Durability**: The 'once and for all' property. Once a transaction is committed, its effects are permanent and cannot be lost, even in the event of a system failure or power outage. The database system must ensure that the committed data is written to a non-volatile storage and can be recovered if needed.



### Properties of Transaction

A transaction is a logical unit of work that represents a real-world event in a database system. A transaction must satisfy four properties, known as ACID properties, to ensure the consistency and reliability of the database. These properties are:

- **Atomicity**: This property ensures that either all the operations of a transaction are executed successfully, or none of them are executed at all. If a transaction fails at any point, the database is restored to its original state before the transaction started. This property is also called the all-or-nothing property.

- **Consistency**: This property ensures that a transaction transforms the database from one consistent state to another consistent state. A consistent state is one that satisfies all the integrity constraints and business rules of the database. A transaction must not violate any of these rules during its execution.

- **Isolation**: This property ensures that a transaction is executed independently of other concurrent transactions. The intermediate results of a transaction are not visible to other transactions, and the effects of other transactions are not visible to the current transaction. This property is also called the serializability property.

- **Durability**: This property ensures that once a transaction commits, its effects are permanent in the database. The changes made by a transaction are not lost even in the case of system failures, such as power outages, crashes, or restarts. This property is also called the persistence property.



### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the same outcome as if the transactions were executed serially, one after the other.
- Serializability is important for maintaining the consistency and correctness of a database in a concurrent environment.
- There are two main techniques for testing the serializability of a schedule: serialization graph and precedence graph.
- A serialization graph is a directed graph where the nodes represent the transactions and the edges represent the conflicts between the transactions. A conflict occurs when two transactions access the same data item and at least one of them is a write operation.
- A schedule is serializable if and only if its serialization graph is acyclic, meaning that there is no cycle in the graph. A cycle in the graph implies that there is a circular dependency among the transactions, which violates the serial order.
- A precedence graph is a special case of a serialization graph where the edges are drawn only from the earlier transaction to the later transaction in the schedule. A precedence graph preserves the order of conflicting operations in the schedule.
- A schedule is serializable if and only if its precedence graph is acyclic, meaning that there is no cycle in the graph. A cycle in the graph implies that there is a contradiction in the order of conflicting operations, which violates the serial order.
- An example of a schedule and its precedence graph is shown below:

| T1 | T2 | T3 |
|----|----|----|
| R(A) |    |    |
|    | R(A) |    |
| W(A) |    |    |
|    |    | R(A) |
|    | W(A) |    |
|    |    | W(A) |

Precedence graph

- The schedule is not serializable because its precedence graph has a cycle: T1 -> T2 -> T3 -> T1. This means that there is no serial order that is equivalent to the concurrent execution of the transactions.



### Serializability of schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- Serializability is a property of a schedule that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it produces the same effect on the database as some serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- There are different types of serializability, such as conflict serializability, view serializability, and cursor stability serializability, which have different criteria for determining the equivalence of schedules.
- Conflict serializability is the most common type of serializability, which is based on the notion of conflict between operations. Two operations conflict if they access the same data item and at least one of them is a write operation. A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- View serializability is a weaker type of serializability, which is based on the notion of view of the database. A view of the database is the set of values read and written by the transactions. A schedule is view serializable if it produces the same view of the database as some serial schedule.
- Cursor stability serializability is a type of serializability that is specific to cursor-based transactions, which are transactions that use cursors to access records in the database. A cursor is a pointer that identifies the current record being accessed by a transaction. A schedule is cursor stability serializable if it preserves the cursor positions of the transactions in some serial schedule.

- Serializability is important for ensuring the isolation and atomicity of transactions, which are two of the ACID properties of database systems. Isolation means that transactions do not interfere with each other's effects on the database, and atomicity means that transactions either commit or abort as a whole.
- Serializability can be enforced by using concurrency control mechanisms, such as locking, timestamping, or validation, which prevent or resolve conflicts between transactions. Concurrency control mechanisms can also improve the performance and throughput of the database system by allowing more parallelism and less blocking of transactions.



### Conflict and View Serializable Schedule

A schedule is a sequence of operations performed by concurrent transactions on a shared database. A schedule is said to be serializable if it is equivalent to a serial schedule, which means that the transactions are executed one after another without any overlap. Serializability ensures the consistency and correctness of the database.

There are two types of serializability: conflict serializability and view serializability.

- Conflict serializability: A schedule is called conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. Two operations are said to be conflicting if they belong to different transactions, operate on the same data item, and at least one of them is a write operation. For example, R1(X) and W2(X) are conflicting, but R1(X) and R2(X) are not. A schedule is conflict serializable if its precedence graph (a directed graph that shows the order of conflicting operations) is acyclic.

- View serializability: A schedule is called view serializable if it is view equivalent to a serial schedule, which means that the initial read, final write, and update operations on each data item are the same in both schedules. For example, R1(X)W1(X)R2(X)W2(X) is view equivalent to R2(X)W2(X)R1(X)W1(X), but not to R1(X)R2(X)W1(X)W2(X). A schedule is view serializable if it is conflict serializable or it contains blind writes (write operations that do not depend on previous read operations).



### Recoverability
- Recoverability is the ability of a database system to restore the database to a consistent state after a failure or an abort of a transaction.
- A transaction is a logical unit of work that consists of a sequence of operations on the database, such as read, write, insert, delete, etc.
- A transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints and business rules of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failure.
- A failure or an abort of a transaction may leave the database in an inconsistent state, violating the ACID properties.
- To ensure recoverability, the database system must keep track of the changes made by each transaction and be able to undo or redo them if necessary.
- The database system uses a recovery manager to perform the recovery operations.
- The recovery manager uses two main techniques: logging and checkpointing.
- Logging is the process of recording the changes made by each transaction in a log file, which is stored on a stable storage device.
- A log record contains information such as the transaction id, the operation performed, the data item affected, the old value, and the new value.
- The log file is used to undo or redo the changes made by a transaction in case of a failure or an abort.
- Undoing a change means restoring the old value of a data item, while redoing a change means applying the new value of a data item.
- Checkpointing is the process of periodically writing the modified pages of the database from the main memory to the disk, and recording the checkpoint in the log file.
- A checkpoint marks a point in time when the database is consistent and all the transactions that have committed before the checkpoint have their effects reflected on the disk.
- Checkpointing reduces the amount of work that the recovery manager has to do in case of a failure, as it only has to consider the transactions that have started after the checkpoint.
- The recovery manager uses two main algorithms to perform the recovery operations: undo and redo.
- The undo algorithm is used to roll back the transactions that have not committed at the time of the failure, and restore the database to a consistent state.
- The undo algorithm scans the log file backwards from the end to the most recent checkpoint, and undoes the changes made by each transaction in reverse order of their occurrence.
- The redo algorithm is used to reapply the changes made by the transactions that have committed but have not written their effects to the disk at the time of the failure, and ensure the durability of the transactions.
- The redo algorithm scans the log file forward from the most recent checkpoint to the end, and redoes the changes made by each transaction in the same order of their occurrence.



### Recovery from transaction failures in DBMS

- A transaction failure is an event that causes a transaction to abort or terminate before it can commit its changes to the database.
- A transaction failure can be caused by various reasons, such as system errors, user errors, concurrency conflicts, or integrity violations.
- A transaction failure can affect the consistency and integrity of the database, as it may leave the database in an inconsistent state or violate some constraints or rules.
- To recover from a transaction failure, the DBMS must ensure that the effects of the failed transaction are undone or rolled back, and that the database is restored to a consistent state.
- There are mainly two types of recovery techniques used in DBMS: rollback/undo recovery and compensation/redo recovery.
- Rollback/undo recovery technique is based on the principle of backing out or undoing the effects of a transaction that has not completed successfully due to a system failure or error.
- Rollback/undo recovery technique requires the DBMS to keep a log of all the operations performed by each transaction, along with the old and new values of the data items affected by the operations.
- Rollback/undo recovery technique uses the log to undo the operations of the failed transaction in the reverse order, restoring the old values of the data items and releasing any locks held by the transaction.
- Compensation/redo recovery technique is based on the principle of repeating or redoing the effects of a transaction that has committed successfully but whose changes have not been written to the disk due to a system failure or error.
- Compensation/redo recovery technique requires the DBMS to keep a log of all the operations performed by each transaction, along with the new values of the data items affected by the operations.
- Compensation/redo recovery technique uses the log to redo the operations of the committed transaction in the same order, applying the new values of the data items and acquiring any locks needed by the transaction.
- In a partitioned database environment, where the database is distributed across multiple servers or partitions, a transaction failure can affect more than one partition.
- In this case, the DBMS must perform crash recovery on the failed partition, and transaction recovery on the other partitions involved in the transaction.
- Crash recovery is the process of restarting the database manager on the failed partition and restoring the database to a consistent state.
- Transaction recovery is the process of ensuring the atomicity and durability of the transactions that were executing on the other partitions when the failure occurred.
- Transaction recovery can involve either rollback/undo or compensation/redo techniques, depending on the state of the transaction at the time of the failure.
- If the transaction was not committed, the DBMS must roll back the transaction on all the partitions.
- If the transaction was committed, the DBMS must redo the transaction on the failed partition and ensure that the changes are written to the disk.



### Two-phase commit protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort (roll back) the transaction. It ensures that either all the changes are committed or none of them are, even in the case of site failures and message losses.

The protocol consists of two phases:

- **Phase 1: Prepare phase**. The coordinator (Ci) of the transaction (T) sends a Prepare T message to all the sites where T executed and waits for their replies. Each site that receives the message writes a <Prepare T> record on its log and forces it to disk. Then, it replies with either Yes or No, depending on whether it is ready to commit or not. If the site replies Yes, it locks all the data items updated by T and waits for the final decision from the coordinator. If the site replies No, it aborts T and releases all the locks.

- **Phase 2: Commit/Abort phase**. The coordinator collects the replies from all the sites and decides the outcome of the transaction. If all the sites replied Yes, the coordinator decides to commit T and writes a <Commit T> record on its log. Then, it sends a Commit T message to all the sites. If any site replied No, the coordinator decides to abort T and writes an <Abort T> record on its log. Then, it sends an Abort T message to all the sites. Each site that receives the message executes the decision and writes a <Commit T> or <Abort T> record on its log. Then, it sends an Acknowledgment message to the coordinator and releases all the locks.

The two-phase commit protocol is a blocking protocol; the failure of a single node blocks progress until the node recovers. Moreover, if the coordinator fails, then the database is left in an inconsistent state and only recovers once the coordinator recovers. This leads to another drawback as the protocol’s latency depends on the slowest node.

: https://www.educative.io/answers/what-is-the-two-phase-commit-protocol
: https://en.wikipedia.org/wiki/Two-phase_commit_protocol
: https://courses.cs.vt.edu/~cs5204/fall00/distributedDBMS/duckett/tpcp.html
: https://www.geeksforgeeks.org/two-phase-commit-protocol-distributed-transaction-management/



### Log Based Recovery in DBMS

- Log based recovery is a technique used in DBMS to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: a unique identifier for each transaction
  - Operation: the type of operation performed by the transaction, such as read, write, commit, or abort
  - Data item: the name of the data item affected by the operation
  - Old value: the value of the data item before the operation
  - New value: the value of the data item after the operation
- A log record can also have a start or end marker to indicate the beginning or the end of a transaction  .
- For example, a log record for a transaction T1 that updates the city of a customer from Chennai to NCR can be written as:

  <T1, Start>
  <T1, City, Chennai, NCR>
  <T1, Commit>

- Log based recovery can be classified into two types  :
  - Undo logging: also known as rollback or backward recovery, it restores the database to its state before the failure by undoing the effects of the transactions that did not commit
  - Redo logging: also known as rollforward or forward recovery, it restores the database to its state after the failure by redoing the effects of the transactions that did commit
- The choice of undo or redo logging depends on the recovery point objective (RPO) and the recovery time objective (RTO) of the database.
  - RPO is the maximum amount of data loss that can be tolerated in the event of a failure
  - RTO is the maximum amount of time that can be taken to restore the database to a consistent state after a failure
- Undo logging requires less RPO but more RTO, while redo logging requires more RPO but less RTO.
- Log based recovery can be implemented in SQL Server using the following steps:
  - Enable the full recovery model for the database, which ensures that all the transactions are logged
  - Perform regular backups of the database and the transaction log
  - In case of a failure, restore the database from the most recent backup
  - Apply the transaction log backups to the restored database, either in undo or redo mode, depending on the RPO and RTO requirements
  - Verify the consistency and integrity of the database



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some checkpoints for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System:

### Checkpoints for the notes of the Unit 7 - Transaction Processing Concepts

- Define what is a transaction and its properties (ACID).
- Explain the concept of concurrency control and why it is needed in a database system.
- Describe the locking protocols for concurrency control, such as two-phase locking, timestamp ordering, and optimistic concurrency control.
- Discuss the problems of deadlock and starvation in locking protocols and how to prevent or resolve them.
- Explain the concept of serializability and how to test for it using precedence graphs.
- Describe the recovery techniques for ensuring atomicity and durability of transactions, such as log-based recovery, shadow paging, and checkpointing.
- Discuss the trade-offs between performance and reliability in transaction processing systems.



### Deadlock Handling

A deadlock is a situation in which two or more transactions are waiting indefinitely for one another to release locks on data items that they need to proceed. Deadlocks can cause the system to halt and waste resources. Therefore, deadlock handling is an important aspect of transaction processing in a database system.

There are three main methods of deadlock handling:

- **Deadlock prevention**: This method aims to prevent deadlocks from occurring in the first place by imposing some constraints on how transactions can acquire and release locks. For example, a transaction may be required to lock all the data items it needs before it starts, or to release all the locks it holds before it requests a new one. This way, no transaction can hold a lock that another transaction needs while waiting for another lock. However, deadlock prevention can also reduce concurrency and performance, as transactions may have to wait longer to acquire locks or may lock unnecessary data items.
- **Deadlock avoidance**: This method allows transactions to acquire and release locks dynamically, but uses some information about the transactions' future requests to determine whether granting a lock request will lead to a deadlock or not. For example, a transaction may have to declare in advance the set of data items it will need during its execution, or the system may maintain a wait-for graph that shows the dependencies among transactions based on their lock requests. If granting a lock request will create a cycle in the wait-for graph, indicating a deadlock, the request is denied and the transaction is delayed until it is safe to proceed. Deadlock avoidance can achieve better concurrency and performance than deadlock prevention, but it also requires more overhead and complexity, as the system has to keep track of the transactions' future requests and analyze the wait-for graph.
- **Deadlock detection and resolution**: This method does not try to prevent or avoid deadlocks, but rather detects them after they have occurred and resolves them by aborting and rolling back some of the transactions involved in the deadlock. For example, the system may periodically run a deadlock detection algorithm that scans the wait-for graph for cycles, or it may use some timeout mechanism that aborts a transaction if it has been waiting for a lock for too long. Deadlock detection and resolution can achieve the highest concurrency and performance among the three methods, as transactions can acquire and release locks freely without any constraints or analysis. However, it also has the highest cost and risk, as the system has to run the deadlock detection algorithm frequently and abort and restart transactions, which may result in wasted work and inconsistent states.



## Unit 8 - Concurrency Control Techniques

Concurrency control techniques are methods to ensure the correctness and consistency of data in a database system when multiple transactions are executed concurrently. Concurrency control techniques can be classified into two categories: pessimistic and optimistic.

- Pessimistic concurrency control techniques assume that conflicts are likely to occur and prevent them by locking the data items that are accessed by the transactions. Locking can be done at different levels of granularity, such as records, pages, tables, or the entire database. Locking can also be done in different modes, such as shared, exclusive, or update. Locking protocols are rules that govern how transactions acquire and release locks on data items. Some examples of locking protocols are two-phase locking, timestamp ordering, and strict two-phase locking.

- Optimistic concurrency control techniques assume that conflicts are rare and allow transactions to execute without locking. However, before committing, each transaction has to validate its read and write sets against the database state to ensure that no conflicts have occurred. If a conflict is detected, the transaction is aborted and restarted. Some examples of optimistic concurrency control techniques are validation-based, multiversion, and snapshot isolation.



### Concurrency control

- Concurrency control is the process of managing simultaneous operations on a database without compromising its integrity or consistency.
- Concurrency control is needed to ensure that concurrent transactions do not interfere with each other and violate the ACID properties of transactions (atomicity, consistency, isolation, and durability).
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and snapshot isolation.
- The choice of concurrency control technique depends on the characteristics of the application, the workload, and the performance requirements. Some factors to consider are the degree of concurrency, the conflict rate, the overhead of locking and validation, and the response time.



# Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the integrity of the database is maintained.

One of the most common concurrency control techniques is locking, which involves applying locks on data items that are accessed by transactions. Locks can be either shared or exclusive, depending on the type of access required by the transaction. A shared lock allows multiple transactions to read the same data item, while an exclusive lock allows only one transaction to write to the data item. Locks prevent conflicts between transactions that may arise due to concurrent read and write operations on the same data item.

There are different types of locking techniques that can be used for concurrency control, such as:

- Two-phase locking protocol: This protocol ensures that a transaction acquires all the locks it needs before releasing any of them. The protocol has two phases: a growing phase, where the transaction can only obtain new locks, and a shrinking phase, where the transaction can only release locks. This protocol guarantees serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.

- Timestamp ordering protocol: This protocol assigns a unique timestamp to each transaction, and uses the timestamps to order the access requests to the data items. The protocol ensures that a transaction can access a data item only if its timestamp is greater than the timestamp of the last transaction that accessed the same data item. This protocol also guarantees serializability, but avoids the overhead of locking and unlocking data items.

- Multi-version concurrency control: This technique allows multiple versions of the same data item to exist in the database, and assigns a timestamp to each version. The technique allows transactions to read the most recent committed version of a data item, and to write to a new version of the data item. The technique uses a certify lock to ensure that the new version does not conflict with any other transaction that has read or written to the same data item. This technique improves the concurrency and performance of the system, as transactions do not have to wait for locks or roll back due to conflicts.

- Validation concurrency control: This technique allows transactions to execute without any locking or timestamping, but validates them before committing. The technique divides the execution of a transaction into three phases: a read phase, where the transaction reads the data items it needs, a validation phase, where the transaction checks if it has any conflicts with other transactions, and a write phase, where the transaction writes the data items it has modified. The technique ensures that only serializable schedules are allowed, and that no transaction is aborted unnecessarily.



### Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability.
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be based on the system clock or a logical counter.
- The basic idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamp to determine the precedence and compatibility of conflicting operations.
- There are two main types of time stamping protocols: basic timestamp ordering and optimistic concurrency control.

#### Basic timestamp ordering

- In this protocol, each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item, and WTS is the largest timestamp of any transaction that has successfully written the data item.
- When a transaction Ti requests to read or write a data item X, the protocol compares the timestamp of Ti (TS(Ti)) with the timestamps of X (RTS(X) and WTS(X)) and decides whether to grant or reject the request based on the following rules:

  - If Ti requests to read X:
    - If TS(Ti) < WTS(X), then Ti is trying to read a value of X that has been overwritten by a later transaction. The request is rejected and Ti is aborted.
    - If TS(Ti) >= WTS(X), then Ti can read X without violating serializability. The request is granted and RTS(X) is updated to max(RTS(X), TS(Ti)).
  - If Ti requests to write X:
    - If TS(Ti) < RTS(X), then Ti is trying to write a value of X that has been read by a later transaction. The request is rejected and Ti is aborted.
    - If TS(Ti) < WTS(X), then Ti is trying to write a value of X that has been overwritten by a later transaction. The request is rejected and Ti is aborted.
    - If TS(Ti) >= RTS(X) and TS(Ti) >= WTS(X), then Ti can write X without violating serializability. The request is granted and WTS(X) is updated to TS(Ti).

- The basic timestamp ordering protocol ensures that the transactions are executed in the order of their timestamps, which is equivalent to a serial schedule. However, it has some drawbacks, such as:

  - It may cause unnecessary aborts of transactions that do not actually conflict with each other.
  - It may cause starvation of transactions that have low timestamps and are repeatedly aborted by later transactions.
  - It may cause cascading aborts of transactions that depend on the values read or written by aborted transactions.

#### Optimistic concurrency control

- In this protocol, each transaction is divided into three phases: read phase, validation phase, and write phase. The protocol assumes that conflicts among transactions are rare and allows transactions to execute concurrently without locking or checking for conflicts in the read phase. However, before committing, each transaction has to pass the validation phase, where the protocol checks for conflicts and serializability using timestamps.
- In the read phase, a transaction Ti reads the values of data items from the database and stores them in a local buffer. Ti also records the timestamps of the data items in the read set (RS(Ti)) and the write set (WS(Ti)).
- In the validation phase, Ti obtains a unique commit timestamp (CTS(Ti)) and compares it with the timestamps of other transactions that have already committed or are in the validation phase. Ti passes the validation if and only if the following conditions are satisfied for every data item X in RS(Ti) or WS(Ti):

  - Ti is the only transaction that has accessed X in its read phase, or
  - Ti has accessed X in its read phase and no other transaction has written X in its write phase, or
  - Ti has accessed X in its write phase and no other transaction has accessed X in its read or write phase, or
  - Ti has accessed X in its read phase and some other transaction Tj has accessed X in its write phase, but CTS(Ti) < CTS(Tj).

- If Ti passes the validation, it proceeds to the write phase, where it writes the values of the data items in WS(Ti) to the database and commits. If Ti fails the validation, it is aborted and restarted with a new timestamp.
- The optimistic concurrency control protocol ensures that the transactions are executed in a serializable order based



### Validation Based Protocol in DBMS

- Validation based protocol is a type of concurrency control technique that works on the assumption that very few transactions interfere with each other, and therefore there is no need to check for conflicts while the transaction is executing  .
- It is also called optimistic concurrency control technique because it optimistically allows transactions to execute without locking any data items, and only validates them at the end to ensure serializability  .
- The protocol consists of three phases for each transaction: read phase, validation phase, and write phase  .
- In the read phase, the transaction reads the data items from the database and stores them in a local buffer. It also records the timestamps of the data items it reads  .
- In the validation phase, the transaction checks whether it can commit without violating serializability. It does so by comparing its timestamps with those of other transactions that have already committed or are in the validation phase. The validation rules are as follows  :
  - If the transaction Ti reads a data item X that was written by another transaction Tj, then Ti must start after Tj commits. This ensures that Ti does not read a dirty value of X.
  - If the transaction Ti writes a data item X that was read by another transaction Tj, then Ti must start before Tj starts. This ensures that Ti does not overwrite a value of X that Tj has already read.
  - If the transaction Ti writes a data item X that was written by another transaction Tj, then Ti must start after Tj commits. This ensures that Ti does not cause a lost update of X.
- If the transaction passes the validation phase, it moves to the write phase, where it writes the updated data items from its local buffer to the database. It also commits and releases any resources it holds  .
- If the transaction fails the validation phase, it aborts and restarts from the beginning  .
- The advantages of validation based protocol are that it avoids locking and deadlock, and it allows more concurrency and parallelism among transactions  .
- The disadvantages of validation based protocol are that it may cause more aborts and restarts, and it requires more memory and processing power to store and validate timestamps  .



### Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows a tree structure to represent the hierarchy of data items, where each node corresponds to a data item and each edge corresponds to a containment relationship.
- Multiple granularity locking protocol uses six types of locks: shared (S), exclusive (X), intention shared (IS), intention exclusive (IX), shared intention exclusive (SIX), and no lock (NL).
- Multiple granularity locking protocol follows six rules to ensure serializability and avoid deadlock:
  1. Follow multi-granularity compatibility function, which defines which lock modes are compatible with each other at the same node.
  2. Lock the root of the tree first, in any mode.
  3. Node Q can be locked by transaction Ti in S or IS only if parent(Q) is locked by Ti in IX or IS.
  4. Node Q can be locked by transaction Ti in X, SIX, IX only if parent(Q) is locked by Ti in IX or SIX.
  5. Ti is two-phase, meaning it acquires all the locks before releasing any lock.
  6. Ti can unlock node Q only if none of Q's descendants are locked by Ti.



# Multi-version Schemes for Concurrency Control

- Multi-version schemes are a type of concurrency control method that allow concurrent access to the database without locking the data.
- Multi-version schemes create and maintain different versions of data items for each write operation performed by a transaction.
- Multi-version schemes allow read operations to access the most recent committed version of a data item, without waiting for the write operations to finish.
- Multi-version schemes improve the performance and concurrency of database applications in a multiuser environment, by reducing the conflicts and delays between read and write operations.
- Multi-version schemes can be implemented in different ways, such as timestamp ordering, multiversion two-phase locking, or snapshot isolation.

## Timestamp Ordering

- Timestamp ordering is a multi-version scheme that assigns a unique timestamp to each transaction and each version of a data item.
- Timestamp ordering ensures that the transactions and the versions of data items are executed in a serializable order, based on their timestamps.
- Timestamp ordering uses two rules to enforce serializability:
  - Write Rule: A transaction T can write a new version of a data item X only if the timestamp of T is greater than the timestamp of the latest committed version of X.
  - Read Rule: A transaction T can read a version of a data item X only if the timestamp of T is greater than or equal to the timestamp of that version of X, and less than the timestamp of any uncommitted version of X.
- Timestamp ordering prevents write-write conflicts and write-read conflicts, but allows read-write conflicts.

## Multiversion Two-Phase Locking

- Multiversion two-phase locking is a multi-version scheme that combines the two-phase locking protocol with the creation of multiple versions of data items.
- Multiversion two-phase locking allows read operations to access the latest committed version of a data item, without acquiring any lock on it.
- Multiversion two-phase locking requires write operations to acquire exclusive locks on the data items they want to update, and to create new versions of them.
- Multiversion two-phase locking ensures that the transactions and the versions of data items are executed in a serializable order, based on the lock points of the transactions.
- Multiversion two-phase locking prevents write-write conflicts and read-write conflicts, but allows write-read conflicts.

## Snapshot Isolation

- Snapshot isolation is a multi-version scheme that provides each transaction with a consistent snapshot of the database at the start of the transaction.
- Snapshot isolation allows read operations to access the data items as they were in the snapshot, without acquiring any lock on them.
- Snapshot isolation requires write operations to check for conflicts with other concurrent transactions before committing, and to abort if any conflict is detected.
- Snapshot isolation ensures that the transactions and the versions of data items are executed in a serializable order, based on the commit order of the transactions.
- Snapshot isolation prevents write-write conflicts and write-read conflicts, but allows read-write conflicts.



### Recovery with Concurrent Transaction

Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions. Recovery with concurrent transaction is important to ensure the ACID properties of transactions, especially atomicity and durability.

Recovery with concurrent transaction can be done in the following four ways:

- Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if locking is used, then the recovery scheme can use the lock table to determine which transactions need to be rolled back or committed. If timestamp ordering is used, then the recovery scheme can use the timestamps to order the transactions and their operations.
- Transaction rollback: In this scheme, the recovery scheme can undo the effects of a transaction that has failed or aborted by using the log records. The log records contain the information about the operations performed by the transaction, such as the old and new values of the data items. The recovery scheme can use the log records to restore the old values of the data items and make the database consistent.
- Checkpoints: In this scheme, the recovery scheme can reduce the amount of work needed to recover the database by periodically taking a snapshot of the database and the log records. A checkpoint is a point in time when the database and the log records are synchronized and consistent. The recovery scheme can use the checkpoint to start the recovery process from the most recent checkpoint instead of from the beginning of the log.
- Restart recovery: In this scheme, the recovery scheme can handle the failure of the system itself, such as a power outage or a crash. The recovery scheme can use the log records and the checkpoints to determine which transactions were committed, which transactions were aborted, and which transactions were in progress at the time of the failure. The recovery scheme can then redo the effects of the committed transactions, undo the effects of the aborted transactions, and either abort or restart the in-progress transactions.



## Unit 9 - Database Security

Database security is the protection of data stored in a database from unauthorized access, modification, or deletion. Database security involves the following aspects:

- **Data confidentiality**: ensuring that only authorized users can access the data in the database.
- **Data integrity**: ensuring that the data in the database is accurate, consistent, and reliable.
- **Data availability**: ensuring that the data in the database is accessible to authorized users whenever they need it.
- **Data authentication**: ensuring that the identity of the users and the sources of the data are verified.
- **Data authorization**: ensuring that the users and the sources of the data have the appropriate permissions to access, modify, or delete the data in the database.

Some of the common threats to database security are:

- **Malicious insiders**: users who have legitimate access to the database but misuse their privileges to harm the data or the system.
- **External attackers**: users who do not have legitimate access to the database but try to exploit the vulnerabilities of the system or the network to gain unauthorized access to the data or the system.
- **Data leakage**: unauthorized disclosure of sensitive or confidential data to unauthorized parties, either intentionally or unintentionally.
- **Data corruption**: unauthorized alteration or deletion of data in the database, either intentionally or unintentionally.
- **Data loss**: accidental or intentional destruction of data in the database, either due to hardware failure, software error, natural disaster, or human error.

Some of the common techniques to ensure database security are:

- **Encryption**: transforming the data into an unreadable form using a secret key, so that only authorized users who have the key can decrypt and access the data.
- **Hashing**: generating a fixed-length value from the data using a mathematical function, so that the data can be verified for integrity and authenticity.
- **Digital signature**: attaching a value to the data that is generated using the private key of the sender, so that the receiver can verify the identity of the sender and the integrity of the data using the public key of the sender.
- **Access control**: defining and enforcing the rules and policies that specify who can access what data and what operations they can perform on the data in the database.
- **Auditing**: recording and monitoring the activities and events that occur in the database, such as who accessed what data, when, and how, so that any suspicious or malicious behavior can be detected and prevented.
- **Backup and recovery**: creating and maintaining copies of the data in the database, so that the data can be restored in case of data loss or corruption.



### Types of security for the notes of the Unit 9 - Database Security in the subject of Basics of Data Base Management System

Database security refers to the process of protecting and safeguarding the database from unauthorized access or cyber-attacks. There are different types of database security that should be implemented in any business or organization that uses a database system. Some of the common types of database security are:

- **Authentication**: This is the process of verifying the user's login credentials, such as username and password, which are stored in the database. If the user's login credentials match the ones in the database, then the user can access the database. Authentication helps to prevent unauthorized users from accessing the database. Authentication can be done using various methods, such as passwords, biometrics, tokens, certificates, etc.
- **Database Encryption**: This is the process of transforming the data in the database into an unreadable form using a secret key or algorithm. Database encryption helps to protect the data from being stolen or tampered with by unauthorized users or hackers. Database encryption can be done at different levels, such as column-level, table-level, file-level, or database-level. Database encryption can use various algorithms, such as symmetric, asymmetric, or hybrid encryption.
- **Backup Database**: This is the process of creating a copy of the database and storing it in a secure location. Backup database helps to restore the data in case of any loss or damage due to natural disasters, hardware failures, human errors, cyber-attacks, etc. Backup database should be done regularly and frequently, and should be tested for validity and integrity. Backup database should also be encrypted and protected from unauthorized access.
- **Physical Security**: This is the process of securing the physical location and environment of the database servers and storage devices. Physical security helps to prevent any damage or theft of the database hardware by unauthorized users or intruders. Physical security can include various measures, such as locks, alarms, cameras, guards, firewalls, etc.
- **Application Security**: This is the process of securing the applications that interact with the database. Application security helps to prevent any malicious or erroneous actions by the application users or developers that can compromise the database. Application security can include various measures, such as input validation, output sanitization, error handling, logging, auditing, etc.
- **Access Control**: This is the process of defining and enforcing the rules and permissions for the database users and roles. Access control helps to limit the access and actions of the database users and roles based on their needs and responsibilities. Access control can include various measures, such as granting, revoking, or modifying privileges, roles, or permissions, creating or deleting users or roles, auditing or monitoring user activities, etc.
- **Web Application Firewall**: This is a type of firewall that monitors and filters the web traffic between the database and the web applications. Web application firewall helps to prevent any web-based attacks, such as SQL/NoSQL injection, cross-site scripting, buffer overflow, etc. that can exploit the database vulnerabilities. Web application firewall can use various techniques, such as signature-based, anomaly-based, or behavior-based detection, to identify and block malicious web requests.



### System Failure

- A system failure is an event that causes the database to stop functioning normally and may result in data loss, corruption, or unauthorized access.
- System failures can be caused by various factors, such as hardware malfunctions, power outages, network disruptions, software bugs, human errors, malicious attacks, or natural disasters.
- System failures can affect the database security in terms of confidentiality, integrity, and availability of the data.
- Confidentiality is the protection of data from unauthorized disclosure or access. A system failure may compromise confidentiality if it exposes sensitive data to unauthorized users or allows unauthorized modifications to the data.
- Integrity is the protection of data from unauthorized or accidental changes. A system failure may compromise integrity if it causes data corruption, inconsistency, or loss.
- Availability is the protection of data from unauthorized or accidental denial of access. A system failure may compromise availability if it prevents authorized users from accessing or using the data.
- To prevent or mitigate the impact of system failures, database systems should implement various security measures, such as:
  - Backup and recovery: Backup is the process of making copies of the database and log files at regular intervals and storing them in a secure location. Recovery is the process of restoring the database to a consistent state after a failure using the backup and log files.
  - Encryption: Encryption is the process of transforming data into an unreadable form using a secret key. Encryption can protect data from unauthorized access or modification in case of a system failure.
  - Authentication and authorization: Authentication is the process of verifying the identity of a user or a system. Authorization is the process of granting or denying access rights to a user or a system. Authentication and authorization can prevent unauthorized users or systems from accessing or modifying the data in case of a system failure.
  - Auditing and monitoring: Auditing is the process of recording the activities and events that occur in the database system. Monitoring is the process of analyzing the audit records and detecting any anomalies or violations. Auditing and monitoring can help identify the cause and extent of a system failure and prevent or respond to any security breaches.

