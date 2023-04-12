

## Unit 1 - Introduction

- This unit provides an overview of the course, its objectives, and its scope.
- The course aims to teach the basic concepts and principles of artificial intelligence (AI), its applications and limitations, and its ethical and social implications.
- The course covers the following topics:

  - What is AI and how is it different from other fields of computer science and engineering?
  - What are the main subfields and techniques of AI, such as search, knowledge representation, reasoning, planning, learning, natural language processing, computer vision, robotics, and machine ethics?
  - What are some of the current and future challenges and opportunities for AI research and development?
  - What are some of the ethical and social issues raised by AI, such as privacy, fairness, accountability, transparency, human dignity, and human-AI collaboration?

- The course requires basic knowledge of mathematics, logic, and programming, as well as curiosity and critical thinking skills.
- The course consists of lectures, readings, assignments, quizzes, and a final project. The course is graded based on the following criteria:

  - Assignments: 40%
  - Quizzes: 20%
  - Final project: 40%

- The course follows the textbook "Artificial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig, 4th edition, 2020. The textbook is available online at https://aima.cs.berkeley.edu/.
- The course website is https://www.example.com/ai-course. The website contains the syllabus, schedule, lecture slides, assignments, quizzes, and other resources. The website also has a discussion forum where students can ask questions and interact with each other and the instructor.
- The instructor of the course is Dr. John Smith, a professor of computer science at Example University. The instructor can be contacted by email at john.smith@example.edu or by office hours at Room 101, Building A, on Mondays and Wednesdays from 10:00 to 11:00. The instructor is assisted by two teaching assistants, Alice and Bob, who can also answer questions and provide feedback on the assignments and quizzes. Alice and Bob can be contacted by email at alice@example.edu and bob@example.edu, respectively.



### An overview of database management system

- A database management system (DBMS) is a software system that manages databases, which are collections of data organized in a structured way.
- A DBMS provides an interface for users and applications to perform various operations on the data, such as creating, reading, updating, deleting, querying, and analyzing.
- A DBMS also provides functions for data security, integrity, backup, recovery, concurrency, and performance optimization.
- A DBMS consists of several components, such as a storage engine, a query processor, a data dictionary, a transaction manager, and a user interface.
- A DBMS can be classified into different types based on the data model, the level of abstraction, the distribution, and the usage. Some common types of DBMS are relational, hierarchical, network, object-oriented, document, graph, and NoSQL.



### Database System vs File System

- A **file system** is a software that organizes and manages files on a storage media, such as a hard disk or a flash drive. A file system provides basic operations such as creating, deleting, renaming, copying, and moving files and folders. A file system does not have any built-in mechanism for ensuring data consistency, security, integrity, or recovery. A file system does not support complex queries or transactions on the data stored in the files. A file system is suitable for storing simple and static data that does not require frequent updates or manipulations. Examples of file systems are FAT, NTFS, ext4, etc.    
- A **database management system (DBMS)** is a software that allows you to access, create, and administer databases. A database is a collection of structured and organized data that can be manipulated using a query language, such as SQL. A DBMS provides various features for ensuring data consistency, security, integrity, and recovery. A DBMS also supports complex queries and transactions on the data stored in the databases. A DBMS is suitable for storing dynamic and complex data that requires frequent updates or manipulations. Examples of DBMS are MySQL, Oracle, MongoDB, etc.      
- The main differences between a database system and a file system are:

  - A database system is designed for handling data objects, whereas a file system is designed for handling files and folders. 
  - A database system provides a query language for accessing and manipulating data, whereas a file system does not.  
  - A database system ensures data consistency, security, integrity, and recovery, whereas a file system does not.   
  - A database system supports concurrent access to data efficiently, whereas a file system does not. 
  - A database system can handle large and complex data, whereas a file system can handle only simple and static data.  

- The advantages of using a database system over a file system are:

  - A database system reduces data redundancy and inconsistency, as data is stored in a normalized and structured way. 
  - A database system improves data accessibility and usability, as data can be queried and manipulated using a query language. 
  - A database system enhances data security and integrity, as data can be protected from unauthorized access and modification. 
  - A database system facilitates data recovery and backup, as data can be restored from logs and snapshots in case of failures. 
  - A database system increases data performance and scalability, as data can be accessed and manipulated concurrently and efficiently. 

- The disadvantages of using a database system over a file system are:

  - A database system requires more hardware and software resources, such as memory, disk space, CPU, and network. 
  - A database system requires more maintenance and administration, such as installation, configuration, tuning, and updating. 
  - A database system requires more skills and knowledge, such as learning a query language and a database design methodology. 
  - A database system may have compatibility and portability issues, as different DBMS have different standards and formats.



### Database System Concepts and Architecture

- A database system is a software system that manages and manipulates data stored in a database, which is a collection of related data organized in a structured way.
- A database system consists of several components, such as the database, the database management system (DBMS), the database applications, and the users.
- The database is the actual data stored on a physical medium, such as disk or memory.
- The DBMS is the software that provides the functionality to create, maintain, query, and update the database.
- The database applications are the programs that use the DBMS to access and manipulate the database for specific purposes, such as online shopping, banking, or social networking.
- The users are the people or entities that interact with the database system, either directly or through the database applications.
- A database system can have different architectures, depending on how the components are distributed and connected across a network of computers.
- The most common architectures are centralized, client-server, and distributed.

#### Centralized Architecture
- In a centralized architecture, all the components of the database system are located on a single computer or server.
- The users access the database system through a terminal or a web browser that communicates with the server.
- The advantages of a centralized architecture are simplicity, efficiency, and security, as the data and the DBMS are under the control of a single system.
- The disadvantages of a centralized architecture are scalability, availability, and performance, as the server can become a bottleneck or a single point of failure for the entire system.

#### Client-Server Architecture
- In a client-server architecture, the components of the database system are divided into two types: clients and servers.
- The clients are the computers or devices that run the database applications and request services from the servers.
- The servers are the computers that run the DBMS and provide services to the clients, such as processing queries and updates on the database.
- The clients and the servers communicate over a network using a standard protocol, such as TCP/IP.
- The advantages of a client-server architecture are scalability, availability, and performance, as the workload can be distributed among multiple servers and clients can access the database system from different locations.
- The disadvantages of a client-server architecture are complexity, overhead, and security, as the data and the DBMS are exposed to multiple systems and the network.

#### Distributed Architecture
- In a distributed architecture, the components of the database system are distributed across multiple computers or servers that are connected by a network.
- The database is partitioned or replicated among the servers, and each server runs a local DBMS that manages a portion of the database.
- The database applications and the users can access the database system from any server, and the servers coordinate with each other to ensure the consistency and integrity of the database.
- The advantages of a distributed architecture are scalability, availability, and performance, as the database system can grow and handle failures by adding or removing servers.
- The disadvantages of a distributed architecture are complexity, overhead, and security, as the data and the DBMS are exposed to multiple systems and the network, and the coordination among the servers can be challenging.



### Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data abstraction also supports data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in the ANSI/SPARC database architecture :
  - Physical level: This is the lowest level of data abstraction. It describes how the data is physically stored in the storage devices and the access methods used to retrieve and update the data. It also reveals the data structures and file organizations used to store the data. For example, the physical level may specify that the data is stored in a B+ tree or a hash table, and that it is accessed by sequential or random access methods.
  - Logical level: This is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data. It also defines the constraints and integrity rules that apply to the data. It does not specify how the data is stored or accessed. The logical level is usually represented by a conceptual schema, such as an entity-relationship (ER) model or a relational model.
  - View level: This is the highest level of data abstraction. It describes how the data is seen by the users and applications. It may show only a part of the database that is relevant to a specific user or application. It may also hide some details of the data types and structures. The view level is usually represented by a set of external schemas, such as SQL queries or forms .
- The three levels of data abstraction provide a clear separation of concerns and responsibilities among the database users, designers, and administrators. They also allow for different levels of security and privacy for the data.



### Data Models

A data model is a type of data model that determines the logical structure of a database. It fundamentally determines in which manner data can be stored, organized and manipulated. Data models are fundamental entities to introduce abstraction in a DBMS. Data models ensure consistency in naming conventions, default values, semantics, security while ensuring quality of the data.

There are different types of data models used for understanding the structure of the database, such as:

- **Relational data model**: This type of model designs the data in the form of rows and columns within a table. Each row represents a record and each column represents an attribute. The tables are also called relations and they are linked by common attributes called keys. Relational data models were initially proposed by IBM researcher E.F. Codd in 1970. They are still implemented today in most relational database management systems (RDBMS).
- **Entity-relationship data model**: An ER model is the logical representation of data as objects and relationships among them. An object is called an entity and a relationship is a connection between two or more entities. An entity has a set of attributes and a relationship has a set of roles. An ER model can be represented graphically using an ER diagram. ER models are useful for conceptual design of databases and can be mapped to relational models.
- **Object-based data model**: An extension of the ER model with notions of functions, encapsulation, and object identity, as well. An object is a collection of data and methods that operate on the data. An object can inherit the properties and behaviors of another object. An object can also be part of a class, which is a collection of similar objects. Object-based data models are suitable for complex data structures and applications.
- **Hierarchical data model**: This type of model represents one-to-many relationships in a treelike format. In this type of model, each record has a parent record and zero or more child records. A record can have only one parent but can have multiple children. The root record is the one that has no parent. Hierarchical data models are simple and efficient for accessing data, but they are rigid and do not support many-to-many relationships.
- **Dimensional data model**: This type of model is used for data analysis and reporting. It consists of two types of tables: fact tables and dimension tables. A fact table contains the measures or metrics of interest, such as sales, revenue, profit, etc. A dimension table contains the attributes or characteristics of the facts, such as time, location, product, customer, etc. A dimensional model can be represented as a cube, where each side of the cube represents a dimension and the cells of the cube represent the facts. Dimensional data models are easy to understand and query, but they require a lot of storage space and processing power.



### Schema and Instances for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- A database is a collection of organized data that can be stored, accessed, and manipulated by a software program called a database management system (DBMS)  .
- A database schema is an abstract design that represents the storage of data in a database. It describes both the organization of data and the relationships between tables in a given database  .
- A database schema is considered the "blueprint" of a database, which defines the structure, constraints, and operations of the database  .
- A database schema is usually specified in a formal language called a data definition language (DDL), which is used to create and modify the schema  .
- A database schema can have different levels of abstraction, such as the conceptual schema, the logical schema, and the physical schema  .
- A database instance is a sample of data from a database at a single moment in time. It is the data stored in a database at a particular state  .
- A database instance can change over time as data is inserted, updated, deleted, or queried by the DBMS or other applications  .
- A database instance can be represented by a set of tables, each containing a set of rows and columns, where each row represents a record and each column represents an attribute  .
- A database instance can also be represented by a set of relations, each containing a set of tuples and attributes, where each tuple represents a record and each attribute represents a property  .
- A database instance can be viewed as a snapshot of the database schema, which shows the actual values of the data elements  .

: https://pediaa.com/what-is-the-difference-between-schema-and-instance/
: https://techdifferences.com/difference-between-schema-and-instance.html
: https://www.ibm.com/topics/database-schema
: https://www.geeksforgeeks.org/difference-between-schema-and-instance-in-dbms/
: https://www.educative.io/blog/what-are-database-schemas-examples



### Data Independence for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- Data independence is the property of a database system that allows the schema of the database to be changed without affecting the applications that use the database.
- Schema is the structure or design of the database that defines the tables, fields, relationships, constraints, etc.
- There are three levels of schema in a database system: external, conceptual, and physical .
- External schema is the view of the database that is seen by the users or applications. It defines what data and operations are available to them.
- Conceptual schema is the logical representation of the database that is independent of the physical implementation. It defines what data and relationships exist in the database.
- Physical schema is the actual storage and organization of the data on the disk. It defines how the data is stored, indexed, compressed, encrypted, etc.
- Data independence is of two types: logical and physical  .
- Logical data independence is the ability to change the conceptual schema without affecting the external schema. It allows the database administrator to modify the logical structure of the database, such as adding, deleting, or renaming tables, columns, or relationships, without requiring the users or applications to change their queries or programs.
- Physical data independence is the ability to change the physical schema without affecting the conceptual schema. It allows the database administrator to modify the physical storage and organization of the data, such as changing the file format, location, size, compression, encryption, etc., without requiring the users or applications to change their queries or programs.
- Data independence is important for the following reasons:
  - It enhances the flexibility and adaptability of the database system to changing requirements and technologies.
  - It reduces the maintenance and development costs of the database system by minimizing the impact of schema changes on the users and applications.
  - It improves the performance and efficiency of the database system by allowing the database administrator to optimize the physical storage and organization of the data according to the workload and usage patterns.
  - It increases the security and integrity of the database system by allowing the database administrator to control the access and manipulation of the data at different levels of abstraction.



### Database Languages and Interfaces

- Database languages are the means of communication between the users and the database management system (DBMS).
- Database interfaces are the tools or applications that allow the users to access and manipulate the data stored in the database.
- The DBMS must provide appropriate languages and interfaces for each category of users, such as database administrators, programmers, application developers, end-users, etc.
- The types of languages and interfaces provided by a DBMS may include the following:

  - Data definition language (DDL): This is the language used to define the structure and schema of the database, such as the tables, columns, constraints, indexes, etc. DDL statements are usually executed by the database administrator or the programmer. Examples of DDL statements are CREATE, ALTER, DROP, etc.
  - Data manipulation language (DML): This is the language used to insert, update, delete, and query the data stored in the database. DML statements are usually executed by the application developer or the end-user. Examples of DML statements are SELECT, INSERT, UPDATE, DELETE, etc.
  - Data control language (DCL): This is the language used to control the access and security of the database, such as granting or revoking permissions, roles, privileges, etc. DCL statements are usually executed by the database administrator or the programmer. Examples of DCL statements are GRANT, REVOKE, etc.
  - Transaction control language (TCL): This is the language used to manage the transactions in the database, such as committing or rolling back the changes, setting the isolation level, etc. TCL statements are usually executed by the application developer or the programmer. Examples of TCL statements are COMMIT, ROLLBACK, SET, etc.
  - Menu-based interfaces: These are the interfaces that present the user with lists of options (called menus) that lead the user through the database operations. These interfaces are suitable for web clients or browsers, as they are easy to use and navigate. Examples of menu-based interfaces are web pages, hyperlinks, buttons, etc.
  - Forms-based interfaces: These are the interfaces that display the data or allow the user to enter the data in predefined formats (called forms). These interfaces are suitable for data entry or data display applications, as they are convenient and efficient. Examples of forms-based interfaces are text boxes, drop-down lists, radio buttons, etc.
  - Graphical user interfaces (GUI): These are the interfaces that use graphical elements (such as icons, images, windows, etc.) to interact with the user and the database. These interfaces are suitable for complex or interactive applications, as they are user-friendly and intuitive. Examples of GUI elements are menus, toolbars, dialog boxes, etc.
  - Natural language interfaces: These are the interfaces that allow the user to communicate with the database using natural language (such as English, Hindi, etc.). These interfaces are suitable for casual or novice users, as they are natural and flexible. Examples of natural language interfaces are chatbots, voice assistants, etc.



### Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects in a database.
- Database objects include tables, indexes, views, schemas, sequences, locations, aliases, and others.
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas.
- DDL commands are predefined and have a specific syntax that must be followed.
- Some common DDL commands are:
  - CREATE: to create a new database object
  - ALTER: to modify an existing database object
  - DROP: to delete a database object
  - RENAME: to rename a database object
  - TRUNCATE: to remove all data from a table
  - COMMENT: to add a comment to a database object
- DDL is also known as data description language in some contexts, as it describes the fields and records in a database table.
- DDL is different from Data Manipulation Language (DML) and Data Control Language (DCL), which are used to manipulate and control the data in a database, respectively.
- DDL is an essential component of SQL, the standard language for relational database management systems.



### DML

- DML stands for Data Manipulation Language, which is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views  .
- The main DML statements are SELECT, INSERT, DELETE, and UPDATE  .
- SELECT statement is used to retrieve data from one or more tables or views.
- INSERT statement is used to add new rows of data to a table or view.
- DELETE statement is used to remove existing rows of data from a table or view.
- UPDATE statement is used to modify existing rows of data in a table or view.
- DML statements can be used with other SQL clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT, to filter, aggregate, sort, and limit the data manipulation results.
- DML statements can also be used with DML triggers, which are special types of stored procedures that automatically take effect when a DML event occurs on a table or view.
- DML triggers can be used to enforce business rules, audit data changes, replicate data, or perform other actions based on the data manipulation.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the overall database structure for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System:

### Overall database structure

- A **database** is a collection of related data that represents some aspect of the real world.
- A **data model** is a set of concepts and rules that define how data is structured, manipulated, and constrained in a database.
- A **database management system (DBMS)** is a software system that enables users to define, create, maintain, and control access to the database.
- A **database system** is the combination of the database and the DBMS.
- A **database schema** is the description of the database structure and constraints, specified in a data definition language (DDL) supported by the DBMS.
- A **database instance** is the collection of data stored in the database at a given point in time.
- A **database state** is the snapshot of the database instance at a particular moment.
- A **database application** is a software program that interacts with the database system to perform some tasks, such as querying, updating, or generating reports.
- A **database user** is a person or a software agent that accesses the database system through a database application or a query language.
- A **database administrator (DBA)** is a person who is responsible for the overall design, implementation, maintenance, and security of the database system.



### Transaction Management

Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations. It is a transaction is a program unit whose execution may or may not change the contents of a database. Transaction management ensures data integrity and consistency in the face of concurrent access, system failures, and malicious attacks.

Some of the topics covered in this unit are:

- Transaction states: A transaction can be in one of the following states: active, partially committed, committed, failed, or aborted. The state transition diagram shows how a transaction moves from one state to another based on the events that occur during its execution.
- Transaction properties: A transaction must satisfy four properties, known as ACID properties, to ensure data integrity and consistency. These are: atomicity, consistency, isolation, and durability . Atomicity means that a transaction is either executed completely or not at all. Consistency means that a transaction preserves the database rules and constraints. Isolation means that a transaction does not interfere with other concurrent transactions. Durability means that the effects of a committed transaction are permanent and survive system failures.
- Transaction log: A transaction log is a file that records all transactions and the database modifications made by each transaction. The transaction log is a critical component of the database, as it is used to recover the database to a consistent state in case of a system failure. The transaction log also supports concurrency control and backup operations.
- Concurrency control: Concurrency control is the process of managing simultaneous access to the database by multiple transactions. Concurrency control ensures that the transactions do not conflict with each other and maintain data integrity and consistency. Concurrency control techniques include locking, timestamping, validation, and multiversioning.
- Recovery management: Recovery management is the process of restoring the database to a consistent state after a system failure. Recovery management uses the transaction log and the backup files to undo or redo the effects of the transactions that were affected by the failure. Recovery management techniques include checkpointing, shadow paging, and deferred and immediate update.



### Storage Management

- Storage management is the process of managing the physical storage of data in a database system.
- Storage management involves the following tasks:
  - Allocating space for data files and indexes on disk or other storage devices.
  - Organizing data into logical structures such as tables, views, and indexes.
  - Maintaining data integrity and consistency by enforcing constraints, triggers, and transactions.
  - Providing efficient access to data by optimizing query execution plans and caching frequently used data in memory.
  - Ensuring data availability and durability by implementing backup and recovery strategies, replication, and fault tolerance.
  - Securing data from unauthorized access by implementing encryption, authentication, and authorization mechanisms.
- Storage management can be performed at different levels of abstraction, such as:
  - Physical level: This deals with the low-level details of how data is stored on disk or other devices, such as sectors, blocks, pages, and records.
  - Logical level: This deals with the high-level representation of data as entities, attributes, and relationships, such as tables, columns, and foreign keys.
  - Conceptual level: This deals with the meaning and semantics of data, such as entities, attributes, and constraints.
  - External level: This deals with the user's view of data, such as queries, views, and reports.
- Storage management can also be classified into two types, depending on the degree of control and automation:
  - Manual storage management: This requires the database administrator (DBA) to manually perform all the tasks of storage management, such as creating, resizing, and deleting data files, creating and dropping tables and indexes, and tuning query performance.
  - Automatic storage management: This allows the database system to automatically perform some or all of the tasks of storage management, such as allocating and freeing space, creating and dropping tables and indexes, and optimizing query performance.



### Database Users and Administrators

- Database users are the people who access or work with the database for various purposes. They can interact with the database directly or through an application program. They can have different levels of privileges and responsibilities depending on their roles and tasks  .
- Database administrators are the people who define, maintain, and control the database. They have full authority over the database and can perform various operations such as creating, modifying, deleting, and granting access to the database objects. They also ensure the security, performance, backup, and recovery of the database    .
- Some of the common types of database users and administrators are  :
  - Native users: These are the database users who communicate with the database through an already written program. They do not need to know the details of the database structure or the query language. For example, when a student registers for a course online, they are using a native user interface.
  - Application programmers: These are the software developers and programming professionals who write the application programs that access the database. They use a programming language such as Java, C#, or Python and a query language such as SQL to manipulate the database. They need to know the logical schema and the query language of the database .
  - Sophisticated users: These are the database users who have a good knowledge of the database system and the query language. They can interact with the database directly using a query tool or a report generator. They can perform complex queries and analysis on the database. For example, a business analyst or a data scientist can be a sophisticated user .
  - Specialized users: These are the database users who have a specific need or interest in the database. They use a specialized software or interface to access the database. They may not be aware of the database structure or the query language. For example, a web developer or a graphic designer can be a specialized user .
  - Casual users: These are the database users who access the database occasionally or for a short period of time. They may not have a consistent or well-defined need for the database. They use a general-purpose software or interface to access the database. They may not be familiar with the database system or the query language. For example, a customer or a visitor can be a casual user .
  - Database administrator (DBA): This is the person or team who is responsible for the overall management and administration of the database. They define the logical and physical schemas and manage all three levels of the database. They also monitor and optimize the database performance, security, backup, and recovery. They can create, modify, delete, and grant access to the database objects and users. They have a superuser account that can perform any operation on the database    .
  - System administrator: This is the person or team who is responsible for the hardware and software environment of the database system. They install, configure, update, and maintain the database server, the operating system, the network, and the storage devices. They also ensure the availability, reliability, and scalability of the database system. They may work closely with the DBA to coordinate the system resources and requirements  .



## Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is the process of designing a conceptual representation of the data that will be stored in a database.
- The Entity Relationship Model (ER Model) is a widely used data modeling technique that uses graphical symbols to represent the entities, attributes, and relationships in a database.
- An entity is a real-world object or concept that can be identified uniquely and has some properties of interest. For example, a student, a course, or a department are entities.
- An attribute is a property or characteristic of an entity that describes some aspect of it. For example, a student entity may have attributes such as name, ID, major, or GPA.
- A relationship is an association or link between two or more entities that expresses some meaningful connection or dependency among them. For example, a student entity may have a relationship with a course entity that indicates that the student is enrolled in the course.
- The ER Model uses the following symbols to represent the entities, attributes, and relationships in a database:

  - A rectangle represents an entity type, which is a collection of entities that share the same attributes. The name of the entity type is written inside the rectangle. For example, Student is an entity type that contains all the student entities in the database.
  - An oval represents an attribute of an entity type. The name of the attribute is written inside the oval. An attribute can be connected to only one entity type by a line. For example, Name is an attribute of the Student entity type.
  - A diamond represents a relationship type, which is a collection of relationships that share the same meaning and involve the same entity types. The name of the relationship type is written inside the diamond. A relationship type can be connected to one or more entity types by a line. For example, Enrolled is a relationship type that connects the Student and Course entity types.
  - A line represents a participation constraint, which specifies the minimum and maximum number of times an entity can participate in a relationship. The participation constraint is indicated by a cardinality ratio, which is a pair of numbers written on either side of the line. For example, a 1:N cardinality ratio means that one entity of the first entity type can participate in the relationship with many entities of the second entity type, but each entity of the second entity type can participate in the relationship with only one entity of the first entity type. A participation constraint can also be indicated by an existence dependency, which is a double line that means that an entity must participate in the relationship. For example, a double line between Student and Enrolled means that every student must be enrolled in at least one course.
  - A dashed oval represents a derived attribute, which is an attribute whose value can be computed from other attributes. The name of the derived attribute is written inside the dashed oval. A derived attribute can be connected to only one entity type by a dashed line. For example, Average is a derived attribute of the Course entity type that can be computed from the grades of the students enrolled in the course.
  - A double rectangle represents a weak entity type, which is an entity type that does not have a key attribute and depends on another entity type for its existence. The name of the weak entity type is written inside the double rectangle. A weak entity type can be connected to only one strong entity type (an entity type that has a key attribute) by a double line. For example, Section is a weak entity type that depends on the Course entity type for its existence.
  - A double oval represents a multivalued attribute, which is an attribute that can have more than one value for a given entity. The name of the multivalued attribute is written inside the double oval. A multivalued attribute can be connected to only one entity type by a line. For example, Phone is a multivalued attribute of the Student entity type that can store multiple phone numbers for a student.
  - A key attribute is an attribute that can uniquely identify an entity within an entity type. A key attribute is underlined in the ER diagram. For example, ID is a key attribute of the Student entity type that can uniquely identify a student.

- An example of an ER diagram for a university database is shown below:

```mermaid
erDiagram
  STUDENT ||--|{ ENROLLED : "1:N"
  ENROLLED ||--|| COURSE : "N:1"
  STUDENT {
    double ID
    string Name
    string Major
    double GPA
    double Phone
  }
  COURSE {
    string Code
    string Title
    double Credits
    double Average
  }
  SECTION ||--||| COURSE : "N:1"
  SECTION {
    double Number

```




### ER model concepts

- ER model stands for Entity Relationship model, which is a high-level conceptual data model that describes the data requirements and relationships of a system  .
- An entity is a real-world object or thing of interest that can be identified uniquely and has some attributes associated with it  . For example, a student, a course, a book, etc.
- An entity type is a collection of entities that share the same properties or characteristics  . For example, STUDENT, COURSE, BOOK, etc.
- An entity set is a set of entities of the same entity type  . For example, {S1, S2, S3, ...} is an entity set of STUDENT type.
- An attribute is a property or characteristic of an entity that describes some aspect of it  . For example, name, age, roll number, etc. are attributes of a student entity.
- An attribute can be classified into different types based on its structure, domain, and dependency . For example, simple vs. composite, single-valued vs. multi-valued, stored vs. derived, etc.
- A relationship is an association or link between two or more entities that expresses some meaningful connection or dependency among them   . For example, enrolls, teaches, borrows, etc. are relationships between student, teacher, and book entities.
- A relationship type is a collection of relationships that share the same meaning or semantics   . For example, ENROLLS, TEACHES, BORROWS, etc.
- A relationship set is a set of relationships of the same relationship type   . For example, {(S1, C2), (S2, C1), (S3, C3), ...} is a relationship set of ENROLLS type.
- A relationship can have some attributes associated with it that describe some property or condition of the relationship  . For example, date, grade, duration, etc. are attributes of a relationship.
- A relationship can also have a degree or cardinality, which specifies the number of entities that participate in the relationship   . For example, unary, binary, ternary, etc.
- A relationship can also have a cardinality ratio or multiplicity, which specifies the number of instances of one entity that can be associated with one instance of another entity in the relationship   . For example, one-to-one, one-to-many, many-to-one, many-to-many, etc.
- A relationship can also have a participation constraint or optionality, which specifies whether the participation of an entity in the relationship is mandatory or optional   . For example, total vs. partial participation.
- An ER diagram is a graphical representation of the ER model that uses symbols and notations to depict the entities, attributes, relationships, and constraints of a system    .
- An ER diagram can be converted into a relational schema or a set of tables that can be implemented in a relational database management system    .
- An ER model can be extended or enhanced with additional concepts and features to capture more complex and realistic scenarios of a system  . For example, weak entity, strong entity, generalization, specialization, aggregation, composition, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query.

### Notation for ER diagram

- ER diagram stands for Entity Relationship Diagram, also known as ERD, is a diagram that displays the relationship of entity sets stored in a database .
- ER diagrams help to explain the logical structure of databases .
- ER diagrams are created based on three basic concepts: entities, attributes and relationships .
- Entities are the objects or things that are represented in the database, such as students, courses, employees, etc .
- Attributes are the properties or characteristics of the entities, such as name, age, salary, etc .
- Relationships are the associations or connections between the entities, such as enrolled, works for, manages, etc .
- There are different notations or symbols that are used to represent the entities, attributes and relationships in ER diagrams, such as crow's foot notation, arrow notation, Barker's notation, UML notation, etc  .
- The most common and intuitive notation is the crow's foot notation, also known as the information engineering notation or the IE notation .
- In crow's foot notation, the following symbols are used :

  - Entities are represented by rectangles with the entity name inside.
  - Attributes are represented by ovals with the attribute name inside, and are connected to the entity by a line.
  - Relationships are represented by diamonds with the relationship name inside, and are connected to the entities by lines.
  - The cardinality or the number of instances of one entity that are associated with one instance of another entity are represented by symbols at the ends of the lines, such as crow's foot, dash, circle, etc.
  - The crow's foot symbol indicates one or many, the dash symbol indicates one and only one, and the circle symbol indicates zero or one.
  - The participation or the optionality of an entity in a relationship is represented by placing the symbols either on the line or above the line, such as mandatory or optional.
  - The mandatory participation means that every instance of an entity must participate in the relationship, and is indicated by placing the symbol on the line.
  - The optional participation means that some instances of an entity may not participate in the relationship, and is indicated by placing the symbol above the line.

- Here is an example of an ER diagram using the crow's foot notation for a university database, where the entities are student, course, instructor and department, and the relationships are enrolled, teaches and belongs to:

ER diagram example

- The diagram shows that a student can enroll in zero or many courses, a course can have zero or one instructor, an instructor can teach one or many courses, an instructor belongs to one and only one department, and a department can have one or many instructors.
- The diagram also shows that the attributes of student are student_id, name, major and phone, the attributes of course are course_id, title and credits, the attributes of instructor are instructor_id, name, rank and salary, and the attribute of department is dept_name.
- The diagram also shows that student_id, course_id, instructor_id and dept_name are the primary keys of the entities, which are underlined to indicate their uniqueness.



### Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are also known as the cardinality ratio. They express the number of entities to which another entity can be related via a relationship set.
- Mapping constraints are most useful in describing the relationship sets that involve more than two entity sets. For binary relationship sets, there are four possible mapping cardinalities:
  - One-to-one: An entity in A is related to at most one entity in B, and an entity in B is related to at most one entity in A.
  - One-to-many: An entity in A is related to any number of entities in B, but an entity in B is related to at most one entity in A.
  - Many-to-one: An entity in A is related to at most one entity in B, but an entity in B is related to any number of entities in A.
  - Many-to-many: An entity in A is related to any number of entities in B, and an entity in B is related to any number of entities in A.
- Mapping constraints can be represented by placing appropriate symbols on the relationship lines in an ER diagram. For example, a one-to-one relationship can be shown by placing a single line on both ends of the relationship line, a one-to-many relationship can be shown by placing a single line on the one side and a crow's foot on the many side, and a many-to-many relationship can be shown by placing a crow's foot on both ends of the relationship line.
- Another type of mapping constraint is the participation constraint, which specifies whether the existence of an entity depends on its being related to another entity via the relationship set. There are two types of participation constraints:
  - Total participation: Every entity in the entity set must participate in at least one relationship in the relationship set. This can be shown by placing a double line on the relationship line in an ER diagram.
  - Partial participation: Some entities in the entity set may not participate in any relationship in the relationship set. This can be shown by placing a single line on the relationship line in an ER diagram.
- Mapping constraints are important for data modeling because they help to define the semantics and integrity of the data in a database. They also help to avoid redundancy and inconsistency in the data.



### Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical and conceptual tool for data modeling using entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified and distinguished from others. Examples of entities are students, courses, books, etc.
- An attribute is a property or characteristic of an entity that describes some aspect of it. Examples of attributes are name, age, address, etc.
- A relationship is an association or connection between two or more entities that expresses some business rule or logic. Examples of relationships are enrolls, teaches, borrows, etc.
- An Entity Relationship Diagram (ERD) is a diagram that shows the entities, attributes, and relationships in a database using symbols and connectors.
- The symbols and connectors used in an ERD are:

  - A rectangle represents an entity. The name of the entity is written inside the rectangle.
  - An oval represents an attribute. The name of the attribute is written inside the oval. An attribute is connected to the entity it belongs to by a line.
  - A diamond represents a relationship. The name of the relationship is written inside the diamond. A relationship is connected to the entities it involves by a line.
  - A line represents a connection between an entity and an attribute or between an entity and a relationship. The line may have a cardinality symbol at one or both ends to indicate the number of occurrences of an entity in a relationship.
  - A cardinality symbol is a number or a letter that indicates the minimum and maximum number of occurrences of an entity in a relationship. The most common cardinality symbols are:

    - 1: one and only one
    - N: zero or more
    - M: one or more
    - C: zero or one

- An example of an ERD is:

ERD example

- The ERD above shows the entities Student, Course, and Instructor, their attributes, and their relationships. The cardinality symbols indicate the following:

  - A student can enroll in zero or more courses, and a course can have zero or more students enrolled in it.
  - A course can have one and only one instructor, and an instructor can teach one or more courses.
  - A student can have zero or one advisor, and an instructor can advise zero or more students.

- The ER Model can be converted into a relational model, which is a more formal and logical representation of data using tables, columns, and keys.
- A table is a collection of rows and columns that store data about a specific entity or relationship. A table has a name and a set of columns.
- A column is a vertical component of a table that stores data of a specific type and has a name and a domain.
- A domain is a set of values that a column can take. A domain can be a predefined data type (such as integer, string, date, etc.) or a user-defined data type (such as enumeration, range, etc.).
- A key is a column or a set of columns that uniquely identifies a row in a table. A key can be a primary key, a foreign key, or a candidate key.
- A primary key is a key that uniquely identifies a row in a table and cannot be null. A table can have only one primary key, which is usually underlined in the table schema.
- A foreign key is a key that references a primary key of another table and establishes a relationship between the two tables. A foreign key can be null and can appear more than once in a table. A foreign key is usually marked with an asterisk (*) in the table schema.
- A candidate key is a key that can uniquely identify a row in a table but is not chosen as the primary key. A table can have more than one candidate key, which are usually marked with a hash (#) in the table schema.
- An example of a relational model is:

Relational model example

- The relational model above shows the tables Student, Course, Instructor, Enrolls, and Advises, their columns, and their keys. The tables are derived from the



### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table.  
- A super key may have additional attributes that are not needed for unique identification.  
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table. 
- There can be more than one super key in a table, and it can also be NULL. 
- For example, in a table of students, the attributes {Student_ID}, {Student_Name, Phone_Number}, and {Student_ID, Student_Name, Phone_Number} are all super keys, but only {Student_ID} is a candidate key.



### Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a database  .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and removing any attribute from it would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier for the relation .
- The other candidate keys that are not chosen as the primary key are called alternate keys or unique keys, and they can also enforce uniqueness constraints on the relation.
- To find the candidate keys of a relation, one can use the following steps:
  - Identify all the attributes that are unique by themselves, and mark them as candidate keys.
  - Identify all the attributes that are part of a functional dependency, where they determine the values of other attributes, and mark them as candidate keys.
  - Identify all the combinations of two or more attributes that are unique together, and mark them as candidate keys.
  - Eliminate any candidate keys that have redundant attributes, i.e., attributes that can be derived from other candidate keys or functional dependencies.
  - The remaining candidate keys are the minimal superkeys of the relation.



### Primary key for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- An entity-relationship model (ER model) is a graphical representation of the data and the relationships among the data in a database system.
- An entity is an object or concept that can be identified and distinguished from others, such as a person, a product, or an event.
- An attribute is a property or characteristic of an entity, such as a name, a color, or a date.
- A key is a set of one or more attributes that uniquely identify an entity instance  .
- A primary key is a key that is chosen as the main way of identifying an entity instance  .
- A primary key must have the following properties:
  - It must be unique, meaning that no two entity instances can have the same primary key value.
  - It must be non-null, meaning that every entity instance must have a primary key value.
  - It must be minimal, meaning that it cannot contain any attribute that is not necessary for uniqueness.
- A primary key can be composed of a single attribute or a combination of attributes .
- A primary key can be represented in an ER diagram by underlining the attribute(s) that form the primary key.
- A primary key can be used to establish relationships between entities by referencing the primary key of another entity, which is called a foreign key .
- A primary key can also be used to enforce data integrity and consistency by preventing duplicate or missing data .



### Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Generalization is a bottom-up approach in which two or more lower level entities combine to form a higher level entity  .
- In generalization, the higher level entity inherits the properties of all the lower level entities that participate in the generalization  .
- Generalization is used to represent a group of entities that share some common characteristics as a single entity  .
- For example, consider the entities Student, Teacher and Staff. They all have some common attributes, such as name, id, address, salary, etc. We can generalize these entities into a higher level entity called Employee, which has all the common attributes. Employee is a generalized entity, and Student, Teacher and Staff are specialized entities .
- Generalization is represented by a triangle with a line connecting the generalized entity and the specialized entities. The triangle is labeled with the word "is-a" to indicate the inheritance relationship .
- For example, the following diagram shows the generalization of Student, Teacher and Staff into Employee:

```
    /\
   /  \
  /is-a\
 /      \
/        \
|        |
|        |
Student  Teacher
|        |
|        |
\        /
 \      /
  \    /
   \  /
    \/
    |
    |
  Employee
    |
    |
    |
  Staff
```
- Generalization can also be applied recursively, meaning that a generalized entity can further combine with other entities to form a more generalized entity .
- For example, consider the entities Person, Animal and Plant. They all have some common attributes, such as name, age, height, weight, etc. We can generalize these entities into a higher level entity called Living_Thing, which has all the common attributes. Living_Thing is a generalized entity, and Person, Animal and Plant are specialized entities. Living_Thing can further generalize with other entities, such as Machine, to form a more generalized entity called Thing .
- For example, the following diagram shows the generalization of Person, Animal and Plant into Living_Thing, and the generalization of Living_Thing and Machine into Thing:

```
    /\
   /  \
  /is-a\
 /      \
/        \
|        |
|        |
Person  Animal
|        |
|        |
\        /
 \      /
  \    /
   \  /
    \/
    |
    |
 Living_Thing
    |
    |
    |
  Plant
    |
    |
    |
    /\
   /  \
  /is-a\
 /      \
/        \
|        |
|        |
Living_Thing  Machine
|        |
|        |
\        /
 \      /
  \    /
   \  /
    \/
    |
    |
  Thing
```
- Generalization is a useful technique for data abstraction, as it allows us to hide the details of a set of entities and focus on their common features.
- Generalization also helps to reduce redundancy and complexity in the data model, as it avoids repeating the same attributes and relationships for different entities.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of aggregation for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System.

### Aggregation
- Aggregation is a process of abstraction in which composite or complex objects are represented as simple entities.
- Aggregation is used to model a relationship between a whole object and its component parts.
- Aggregation is a special case of the has-a relationship.
- Aggregation can be used to avoid redundancy and express the semantics more clearly.
- Aggregation can be nested, that is, an aggregate object can be part of another aggregate object.

#### Example of Aggregation
- Consider a university database that has entities such as Student, Course, Department, and Instructor.
- A Student can enroll in many Courses, and a Course can have many Students. This is a many-to-many relationship between Student and Course.
- A Course can belong to only one Department, and a Department can offer many Courses. This is a many-to-one relationship between Course and Department.
- An Instructor can teach many Courses, and a Course can be taught by many Instructors. This is a many-to-many relationship between Instructor and Course.
- A Student can have only one Instructor as an advisor, and an Instructor can advise many Students. This is a one-to-many relationship between Instructor and Student.

- To model these relationships, we can use the following entity sets and relationship sets:

ER diagram without aggregation

- However, this ER diagram has some problems:
  - The relationship between Student and Instructor is ambiguous. It is not clear whether it represents the advisor relationship or the teaching relationship.
  - The relationship between Course and Department is redundant. It can be derived from the relationship between Course and Instructor, and the relationship between Instructor and Department.
  - The relationship between Course and Instructor does not capture the semantics of the teaching assignment. It does not show which Instructor teaches which Course in which semester.

- To solve these problems, we can use aggregation as follows:

ER diagram with aggregation

- In this ER diagram, we have used aggregation to create a new entity set called Section, which represents a specific offering of a Course in a given semester.
- A Section is composed of a Course and an Instructor, and has an attribute called Semester.
- A Section is related to a Department by a many-to-one relationship called Belongs_to.
- A Section is related to a Student by a many-to-many relationship called Enrolls_in.
- A Student is related to an Instructor by a one-to-many relationship called Advised_by, which is distinct from the teaching relationship.

- By using aggregation, we have avoided redundancy and expressed the semantics more clearly. We have also created a new level of abstraction that can be used for further modeling.



### Reduction of an ER diagram to tables

- An ER diagram is a graphical representation of the entities and relationships in a database.
- A table is a collection of rows and columns that store data in a database.
- The process of converting an ER diagram to tables is called reduction or mapping.
- The reduction of an ER diagram to tables involves the following steps:

  - For each entity type in the ER diagram, create a table with the same name and include all the attributes as columns. The primary key of the table is the same as the key attribute of the entity type.
  - For each one-to-one or one-to-many relationship type in the ER diagram, identify the table that corresponds to the entity type on the many side of the relationship. Add a foreign key column to this table that references the primary key of the table on the one side of the relationship. The foreign key column can have the same name as the primary key column or a different name. If the relationship type has any attributes, include them as columns in the table on the many side of the relationship.
  - For each many-to-many relationship type in the ER diagram, create a new table with the same name as the relationship type. Include the primary keys of the tables that correspond to the entity types on both sides of the relationship as foreign key columns in the new table. The primary key of the new table is the combination of the foreign key columns. If the relationship type has any attributes, include them as columns in the new table.
  - For each weak entity type in the ER diagram, create a table with the same name and include all the attributes as columns. Include the primary key of the table that corresponds to the strong entity type that owns the weak entity type as a foreign key column in the weak entity table. Declare the combination of the foreign key column and the partial key attribute of the weak entity type as the primary key of the weak entity table.
  - For each multivalued attribute in the ER diagram, create a new table with the same name as the attribute. Include the primary key of the table that corresponds to the entity type that has the multivalued attribute as a foreign key column in the new table. Include the multivalued attribute as another column in the new table. The primary key of the new table is the combination of the foreign key column and the multivalued attribute column.

- Here is an example of an ER diagram and its corresponding tables:

ER diagram

| LECTURE | | STUDENT | | SUBJECT | | COURSE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LECTURE_ID | LECTURE_NAME | STUDENT_ID | STUDENT_NAME | SUBJECT_ID | SUBJECT_NAME | COURSE_ID | COURSE_NAME |
| PK | | PK | | PK | | PK | |

| LECTURE_STUDENT | | LECTURE_SUBJECT | | STUDENT_SUBJECT | | STUDENT_COURSE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LECTURE_ID | STUDENT_ID | LECTURE_ID | SUBJECT_ID | STUDENT_ID | SUBJECT_ID | STUDENT_ID | COURSE_ID |
| FK | FK | PK | PK | FK | FK | PK | PK |



### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. The EER model reflects more precisely the properties and constraints that are found in complex databases, such as inheritance, specialization, generalization, union, and aggregation.

The EER model includes the following concepts in addition to the ER model concepts:

- **Subclasses and Superclasses**: A subclass is a subset of entities that belong to a superclass, and inherits all the attributes and relationships of the superclass. A superclass is a superset of entities that share some common attributes or relationships. For example, a subclass STUDENT can be derived from a superclass PERSON, and inherit the attributes name, address, and phone from the superclass.
- **Specialization and Generalization**: Specialization is the process of defining one or more subclasses from a superclass based on some distinguishing characteristics of the entities in the subclass. Generalization is the reverse process of abstraction, where common attributes and relationships are combined from two or more subclasses to form a superclass. For example, a superclass VEHICLE can be generalized from the subclasses CAR and TRUCK, and have the common attribute license_plate.
- **Union or Category**: A union or category is a subclass that represents a collection of entities from different entity types. A union or category is also called a shared subclass, since it can be a subclass of more than one superclass. For example, a subclass EMPLOYEE can be a union of the subclasses FACULTY and STAFF, and be a subclass of both the superclasses PERSON and ORGANIZATION.
- **Aggregation**: Aggregation is the process of grouping together a set of entities and relationships into a single abstract entity type. Aggregation allows treating the group as a single unit without losing the individual identities of the entities. For example, an entity type PROJECT can be aggregated from the entity types TASK and RESOURCE, and the relationship type ALLOCATE. The aggregated entity type PROJECT can then participate in other relationships, such as MANAGE or EVALUATE.

The EER model can be represented graphically using the following symbols:

- A rectangle for an entity type, with the name of the entity type inside the rectangle.
- An ellipse for an attribute, with the name of the attribute inside the ellipse. A key attribute is underlined, and a multivalued attribute is double-lined. An attribute can be connected to an entity type or a relationship type by a line.
- A diamond for a relationship type, with the name of the relationship type inside the diamond. A relationship type can be connected to one or more entity types by a line, with a cardinality ratio and a participation constraint on each end of the line.
- A triangle for a superclass/subclass relationship, with the name of the relationship type above the triangle. A superclass/subclass relationship can be connected to one or more superclasses and one or more subclasses by a line, with a disjointness constraint and a completeness constraint on the line.
- A circle with a letter "d" for a union or category, with the name of the subclass below the circle. A union or category can be connected to one or more superclasses by a line, with a partial or total participation constraint on the line.
- A dashed rectangle for an aggregation, with the name of the aggregated entity type inside the rectangle. An aggregation can enclose a set of entity types and relationship types, and can be connected to other entity types or relationship types by a line.

Here is an example of an EER diagram for a university database:

EER diagram example



### Relationships of Higher Degree

- A relationship is an association between two or more entities in an ER model.
- The degree of a relationship is the number of entities that participate in it.
- A binary relationship has a degree of two, meaning it involves two entities.
- A ternary relationship has a degree of three, meaning it involves three entities.
- A higher degree relationship has a degree of more than three, meaning it involves more than three entities.
- Higher degree relationships are rare and complex, and they are usually avoided in ER modeling.
- Higher degree relationships can be converted into binary relationships by introducing new entity types or relationship types.
- For example, a quaternary relationship R between entities A, B, C, and D can be converted into two binary relationships R1 and R2, where R1 is between A and a new entity type E, and R2 is between E and B, C, and D.
- To read a higher degree relationship, one can isolate two out of the participating entities and see how they relate to the third one, and repeat this for all possible pairs.



## Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table consists of rows (records) and columns (attributes).
- A primary key is a column or a combination of columns that uniquely identifies each row in a table.
- A foreign key is a column or a combination of columns that references a primary key in another table, to establish a relationship between the tables.
- A relationship is a logical association between two or more tables, based on a common attribute or a foreign key.
- There are three types of relationships: one-to-one, one-to-many, and many-to-many.
- A one-to-one relationship occurs when each row in one table is related to exactly one row in another table.
- A one-to-many relationship occurs when each row in one table is related to zero or more rows in another table.
- A many-to-many relationship occurs when each row in one table is related to zero or more rows in another table, and vice versa.
- A many-to-many relationship cannot be directly represented in a relational database, and requires an intermediate table (also called a junction table or a linking table) to store the associations between the tables.
- A relational schema is a graphical representation of the tables, attributes, keys, and relationships in a relational database.
- A relational model is a set of rules and constraints that define how data is stored and manipulated in a relational database.
- Some of the rules and constraints are: entity integrity, referential integrity, domain integrity, and normalization.
- Entity integrity is the rule that states that no primary key value can be null or duplicated in a table.
- Referential integrity is the rule that states that if a foreign key value exists in a table, it must match a primary key value in the referenced table, or be null.
- Domain integrity is the rule that states that each attribute value must be valid and conform to the data type and range of the attribute domain.
- Normalization is the process of organizing the data in a relational database to reduce redundancy and improve data integrity.
- Normalization involves applying a series of normal forms, which are rules or criteria for designing a relational schema.
- The most common normal forms are: first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF).
- First normal form (1NF) requires that each attribute value in a table is atomic, meaning it cannot be further divided into smaller parts, and that each row in a table is unique.
- Second normal form (2NF) requires that a table is in 1NF, and that each non-key attribute in a table is fully functionally dependent on the primary key, meaning it cannot be determined by a subset of the primary key.
- Third normal form (3NF) requires that a table is in 2NF, and that each non-key attribute in a table is non-transitively dependent on the primary key, meaning it cannot be determined by another non-key attribute in the table.
- Boyce-Codd normal form (BCNF) requires that a table is in 3NF, and that every determinant in a table is a candidate key, meaning it can uniquely identify each row in the table.



### Introduction to relational database

- A relational database is a type of database that stores and organizes data in tables, where each table consists of rows and columns.
- Each row in a table represents a record or an entity, and each column represents an attribute or a property of the entity.
- A table can have a primary key, which is a column or a combination of columns that uniquely identifies each row in the table.
- A table can also have foreign keys, which are columns that reference the primary key of another table, to establish relationships between tables.
- A relational database follows a set of rules and constraints, such as entity integrity, referential integrity, domain integrity, and normalization, to ensure the validity and consistency of the data.
- A relational database can be manipulated and queried using a standard language called SQL (Structured Query Language), which allows users to perform various operations, such as creating, updating, deleting, and retrieving data from the database.
- A relational database can also support transactions, which are a sequence of operations that are executed as a single unit, to ensure the atomicity, consistency, isolation, and durability (ACID) properties of the database.
- A relational database can be implemented using various software systems, such as MySQL, Oracle, PostgreSQL, SQLite, etc.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of relational database structure for the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System.

### Relational Database Structure

- A relational database is a collection of data organized into tables, where each table consists of rows and columns.
- Each row in a table represents a record or a tuple, and each column represents an attribute or a field of the record.
- Each table has a primary key, which is a column or a combination of columns that uniquely identifies each record in the table.
- A table can also have foreign keys, which are columns that refer to the primary key of another table, establishing a relationship between the tables.
- A relational database can have multiple tables, which can be linked by using foreign keys and join operations.
- A relational database follows a set of rules, called the relational model, which defines how the data is stored, manipulated, and queried.
- The relational model is based on the concept of mathematical relations, which are sets of ordered pairs of values that satisfy certain properties.
- The relational model also defines a set of operations, called relational algebra, which can be used to manipulate and query the data in a relational database.
- Some of the common relational algebra operations are selection, projection, union, intersection, difference, product, join, and division.
- A relational database can also be accessed by using a query language, such as SQL, which allows users to specify what data they want to retrieve or modify, without specifying how to do it.
- A query language can also support features such as aggregation, grouping, sorting, filtering, and subqueries, which can enhance the functionality and efficiency of the queries.
- A relational database can also have constraints, which are rules that enforce the integrity and validity of the data in the database.
- Some of the common constraints are domain constraints, which specify the range of values that an attribute can take, key constraints, which ensure the uniqueness of the primary and foreign keys, entity integrity constraints, which ensure that no primary key value is null, referential integrity constraints, which ensure that the foreign key values match the primary key values of the referenced table, and general constraints, which can be defined by using logical expressions or triggers.



### Relational Model Terminology – Domains

- A domain is the set of all possible values that an attribute can have in a relation  .
- A domain is defined by a name, a data type, and a set of constraints .
- A domain is atomic, meaning that each value in the domain is indivisible as far as the relational model is concerned  .
- A domain can be shared by multiple attributes in different relations, as long as they have the same name, data type, and constraints .
- A domain can be simple or composite, depending on whether it is composed of one or more subdomains.
- A domain can be scalar or nonscalar, depending on whether it can be decomposed into smaller components.

Some examples of domains are:

- The domain of Marital Status has a set of possibilities: Married, Single, Divorced .
- The domain of Shift has the set of all possible days: {Mon, Tue, Wed, Thu, Fri, Sat, Sun}.
- The domain of Phone Number has a data type of string and a constraint of 10 digits.
- The domain of Address has a composite structure of subdomains: Street, City, State, Zip Code.
- The domain of Image has a nonscalar structure of pixels and colors.



### Attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- An attribute is a property or characteristic of an entity or a relationship in a relational database.
- An attribute can have a name, a data type, a domain, and a value for each entity or relationship instance.
- An attribute can be classified into different types based on its role and function in the database schema, such as:
  - **Key attribute**: An attribute that uniquely identifies an entity or a relationship instance in a relation. A key attribute can be a single attribute or a combination of attributes. A key attribute can be a primary key, a foreign key, or a candidate key.
  - **Primary key attribute**: A key attribute that is chosen as the main identifier of an entity or a relationship in a relation. A primary key attribute cannot have null or duplicate values. A primary key attribute can be a single attribute or a combination of attributes. A primary key attribute can be underlined in the relation schema to indicate its status.
  - **Foreign key attribute**: A key attribute that references the primary key attribute of another entity or relationship in a different relation. A foreign key attribute can have null or duplicate values. A foreign key attribute can be a single attribute or a combination of attributes. A foreign key attribute can be marked with an asterisk (*) in the relation schema to indicate its status.
  - **Candidate key attribute**: A key attribute that can potentially serve as the primary key attribute of an entity or a relationship in a relation. A candidate key attribute cannot have null or duplicate values. A candidate key attribute can be a single attribute or a combination of attributes. A candidate key attribute can be marked with a hash (#) in the relation schema to indicate its status.
  - **Non-key attribute**: An attribute that is not a key attribute of an entity or a relationship in a relation. A non-key attribute can have null or duplicate values. A non-key attribute can be a single attribute or a combination of attributes. A non-key attribute can be marked with a dash (-) in the relation schema to indicate its status.
  - **Simple attribute**: An attribute that cannot be further subdivided into smaller attributes. A simple attribute can have a single value for each entity or relationship instance. A simple attribute can be a key attribute or a non-key attribute. A simple attribute can be marked with a circle (o) in the relation schema to indicate its status.
  - **Composite attribute**: An attribute that can be further subdivided into smaller attributes. A composite attribute can have multiple values for each entity or relationship instance. A composite attribute can be a key attribute or a non-key attribute. A composite attribute can be marked with a square ([ ]) in the relation schema to indicate its status.
  - **Single-valued attribute**: An attribute that can have only one value for each entity or relationship instance. A single-valued attribute can be a simple attribute or a composite attribute. A single-valued attribute can be a key attribute or a non-key attribute. A single-valued attribute can be marked with a dot (.) in the relation schema to indicate its status.
  - **Multi-valued attribute**: An attribute that can have more than one value for each entity or relationship instance. A multi-valued attribute can be a simple attribute or a composite attribute. A multi-valued attribute can be a non-key attribute only. A multi-valued attribute can be marked with a double circle (oo) in the relation schema to indicate its status.
  - **Derived attribute**: An attribute that can be derived or calculated from other attributes in the database. A derived attribute can be a simple attribute or a composite attribute. A derived attribute can be a non-key attribute only. A derived attribute can be marked with a dashed circle (o-o) in the relation schema to indicate its status.
  - **Stored attribute**: An attribute that is stored in the database. A stored attribute can be a simple attribute or a composite attribute. A stored attribute can be a key attribute or a non-key attribute. A stored attribute can be marked with a solid circle (●) in the relation schema to indicate its status.



### Tuples

- A tuple is a row of a table that represents an entity or a relationship instance in a relational database.
- A tuple consists of one or more attributes, each of which has a name and a value.
- The value of an attribute can be atomic (single-valued) or composite (multi-valued).
- The order of the attributes in a tuple is irrelevant, as they are identified by their names.
- The number of attributes in a tuple is called its degree or arity.
- A tuple can be uniquely identified by a primary key, which is a subset of attributes that can distinguish it from other tuples in the same table.
- A tuple can also have foreign keys, which are attributes that reference the primary keys of other tables, to represent relationships between entities.
- A tuple can be inserted, updated, deleted, or queried using SQL commands or other relational algebra operations.



### Relations and Relational Database Schema

- A **relation** is a set of tuples that have the same attributes. A tuple is a single row of data in a table. An attribute is a column or field name of a table. A relation can also be called a table or a relation variable.
- A **relational schema** is a collection of relation schemas for a whole database. A relation schema is a description of a relation, which specifies the name of the relation and the name and type of each attribute. A relational schema can also be called a database schema or a schema diagram.
- A relational schema is a collection of **metadata**, which is data about data. It describes the structure and constraints of data representing in a particular domain  .
- A relational schema acts as a blueprint or design of the datasets within the database. It also highlights the connections between the database's datasets, which are called **relationships**. Relationships can be one-to-one, one-to-many, many-to-one, or many-to-many .
- A relational schema can be represented using various notations, such as **Entity-Relationship (ER) diagrams**, **Unified Modeling Language (UML) diagrams**, or **Structured Query Language (SQL) statements**. These notations help to visualize and document the schema in a clear and concise way  .
- A relational schema has many benefits, such as:
  - It helps to ensure the **integrity** and **consistency** of the data within the database, by enforcing rules and constraints on the data values and relationships .
  - It helps to improve the **performance** and **efficiency** of the database, by optimizing the storage and retrieval of data, and avoiding data redundancy and anomalies .
  - It helps to facilitate the **communication** and **collaboration** among the database developers, users, and administrators, by providing a common language and understanding of the data and its meaning .
  - It helps to support the **evolution** and **maintenance** of the database, by allowing changes and updates to the schema without affecting the existing data or applications .



### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of data in a relational database.
- Integrity constraints can be defined at the schema level (when the database is created) or at the instance level (when the data is inserted or updated).
- Integrity constraints can be classified into four types: domain constraints, key constraints, referential integrity constraints, and general constraints.

#### Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- Domain constraints ensure that the data stored in a relation is of the correct type and format.

#### Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by defining primary keys and candidate keys for the relations.
- Primary keys are the minimal set of attributes that can uniquely identify each tuple in a relation. There can be only one primary key for each relation.
- Candidate keys are the alternative sets of attributes that can also uniquely identify each tuple in a relation. There can be more than one candidate key for each relation.
- Key constraints ensure that the data stored in a relation is unique and non-redundant.

#### Referential Integrity Constraints

- Referential integrity constraints specify the relationships between tuples in different relations.
- Referential integrity constraints can be enforced by defining foreign keys and referential actions for the relations.
- Foreign keys are the attributes or combinations of attributes in a relation that refer to the primary key or a candidate key of another relation. The relation that contains the foreign key is called the referencing relation, and the relation that is referred to by the foreign key is called the referenced relation.
- Referential actions are the actions that are taken when the data in the referenced relation is inserted, updated, or deleted. The referential actions can be: cascade, restrict, set null, set default, or no action.
- Referential integrity constraints ensure that the data stored in a relation is consistent and coherent with the data in other relations.

#### General Constraints

- General constraints are the constraints that cannot be expressed by the other types of integrity constraints.
- General constraints can be enforced by defining triggers, assertions, or check clauses for the relations.
- Triggers are the procedures that are executed automatically when a certain event (such as insert, update, or delete) occurs on a relation.
- Assertions are the conditions that must hold true for the database at all times.
- Check clauses are the conditions that must hold true for each tuple in a relation.
- General constraints ensure that the data stored in a relation satisfies some specific business rules or logic.



### Entity Integrity

- Entity integrity is a rule that ensures that each row or record in a relational table is uniquely identified by a primary key.
- A primary key is a column or a combination of columns that can uniquely distinguish each row in a table.
- Entity integrity prevents duplicate rows or records from being inserted into a table, and ensures that every row can be uniquely identified and referenced by other tables.
- Entity integrity also ensures that no part of a primary key can be null, because null values are unknown and cannot be compared or matched.
- Entity integrity is enforced by the database system by creating a unique index on the primary key column(s) and checking for null values before inserting or updating data.



### Referential integrity

- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- It requires that if a value of one attribute (column) of a table references a value of another attribute (either in the same or a different table), then the referenced value must exist.
- It prevents the insertion, update, or deletion of data that would violate the consistency of the relationships .
- It is enforced by using primary keys and foreign keys.
- A primary key is a column or a set of columns that uniquely identifies a row in a table.
- A foreign key is a column or a set of columns that references a primary key in another table.
- For example, consider the following two tables:

| StudentID | Name | Major |
|-----------|------|-------|
| 1001      | Alice| CS    |
| 1002      | Bob  | Math  |
| 1003      | Carol| CS    |

| CourseID | CourseName | Instructor | StudentID |
|----------|------------|------------|-----------|
| CS101    | Programming| Smith      | 1001      |
| CS102    | Data Struct| Jones      | 1001      |
| CS102    | Data Struct| Jones      | 1003      |
| Math101  | Calculus   | Lee        | 1002      |

- In this example, StudentID is the primary key of the first table and a foreign key of the second table.
- Referential integrity ensures that every value of StudentID in the second table matches a value of StudentID in the first table.
- This means that we cannot insert a row in the second table with a StudentID that does not exist in the first table.
- Similarly, we cannot update or delete a row in the first table if it is referenced by a row in the second table.
- Referential integrity helps to maintain the accuracy and consistency of data in a relational database.



### Key Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple in a relation.
- A key constraint is a rule that specifies the properties and restrictions of a key.
- There are different types of key constraints, such as:
  - Superkey: a set of attributes that contains a key.
  - Candidate key: a minimal superkey, i.e., a superkey that has no proper subset that is also a superkey.
  - Primary key: a candidate key that is chosen to be the main identifier of a relation.
  - Foreign key: a set of attributes in a relation that references the primary key of another relation.
  - Alternate key: a candidate key that is not chosen as the primary key.
  - Composite key: a key that consists of two or more attributes.
- Key constraints are important for ensuring the integrity, consistency, and uniqueness of data in a relational database. They also facilitate the operations of querying, joining, and modifying data.



### Domain Constraints for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Domain constraints are a type of user-defined column that helps us to arrange the data we have entered according to the datatype.
- Domain constraints specify the domain or set of values that are allowed for an attribute or a column in a relation.
- Domain constraints ensure that the data stored in a column is valid, consistent and meaningful.
- Domain constraints can be enforced by using the following methods:
  - Not Null: This constraint prevents the insertion of null values in a column. Null values are the values that are unassigned or unknown. For example, if we have a column named `name` in a table named `student`, we can use the not null constraint to ensure that every student has a name.
  - Check: This constraint defines a condition that each row must satisfy. For example, if we have a column named `age` in a table named `student`, we can use the check constraint to ensure that the age of every student is between 18 and 25.
  - Default: This constraint specifies a default value for a column when no value is provided by the user. For example, if we have a column named `gender` in a table named `student`, we can use the default constraint to assign `M` or `F` as the default value for the gender of every student.
  - Unique: This constraint ensures that the values in a column are distinct and no two rows have the same value. For example, if we have a column named `roll_no` in a table named `student`, we can use the unique constraint to ensure that every student has a unique roll number.
  - Primary Key: This constraint combines the not null and unique constraints and identifies each row uniquely in a table. For example, if we have a column named `roll_no` in a table named `student`, we can use the primary key constraint to ensure that every student has a unique and non-null roll number.
  - Foreign Key: This constraint establishes a relationship between two tables by referencing a column in one table to a primary key column in another table. For example, if we have a table named `course` with a column named `course_id` as the primary key, and a table named `enrollment` with a column named `course_id` as the foreign key, we can use the foreign key constraint to ensure that every course enrolled by a student exists in the course table.
- Domain constraints are important for maintaining the integrity, accuracy and quality of the data in a relational database .



### Relational algebra - relational calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a **procedural** language that specifies **how** to construct a new relation from one or more existing relations.
- Relational calculus is a **declarative** language that specifies **what** information is required from the relations, without specifying how to obtain it.
- Relational algebra and relational calculus are **logically equivalent**, meaning that any query expressed in one language can be translated into an equivalent query in the other language. This is known as **Codd's theorem**  .
- Relational algebra consists of a set of basic operations, such as selection, projection, union, set difference, Cartesian product, and renaming, and a set of additional operations, such as join, division, natural join, and assignment, that can be derived from the basic ones.
- Relational calculus can be classified into two types: **tuple relational calculus** (TRC) and **domain relational calculus** (DRC). Both types use a notation of **quantified variables** and **logical predicates** to express queries over relations.
- Tuple relational calculus uses variables that range over **tuples** of a relation. A query in TRC is of the form `{T | P(T)}`, where `T` is a tuple variable and `P(T)` is a predicate involving `T` and other constants or variables. The result of the query is the set of all tuples `T` that satisfy the predicate `P(T)`.
- Domain relational calculus uses variables that range over **domains** or **attributes** of a relation. A query in DRC is of the form `{x1, x2, ..., xn | P(x1, x2, ..., xn)}`, where `x1, x2, ..., xn` are domain variables and `P(x1, x2, ..., xn)` is a predicate involving the variables and other constants. The result of the query is the set of all tuples `(x1, x2, ..., xn)` that satisfy the predicate `P(x1, x2, ..., xn)`.
- An example of a query in TRC is: `{T.name | Book(T) AND T.author = 'J.K. Rowling'}`, which returns the names of all books written by J.K. Rowling.
- An example of a query in DRC is: `{x | Book(y) AND y.name = x AND y.author = 'J.K. Rowling'}`, which returns the same result as the previous query.



### Tuple and Domain Calculus for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases .
- Relational calculus is a non-procedural language, which means it specifies what data to retrieve, not how to retrieve it .
- Tuple relational calculus (TRC) uses tuple variables that range over the rows of a relation and a predicate that specifies the condition for selecting tuples  .
- Domain relational calculus (DRC) uses domain variables that range over the values of a domain and a predicate that specifies the condition for selecting values  .
- Both TRC and DRC are equivalent in expressive power, which means they can express the same set of queries.
- The syntax of TRC is {t | P(t)}, where t is a tuple variable and P(t) is a predicate involving t and other constants.
- The syntax of DRC is {<x1, x2, ..., xn> | P(x1, x2, ..., xn)}, where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a predicate involving them and other constants.
- An example of a TRC query is {t | t ∈ Student ∧ t.age > 18}, which returns all the tuples from the Student relation whose age is greater than 18.
- An example of a DRC query is {<x, y> | ∃z(Student(x, y, z) ∧ z > 18)}, which returns all the pairs of values from the Student relation whose third attribute is greater than 18.
- TRC and DRC are safe if they only return finite sets of values, otherwise they are unsafe.



### Basic operations – selection and projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database  .
- Selection operation targets records (rows) or specific entities in a relational database. It filters the rows that satisfy a given condition or predicate .
- Projection operation targets attributes (columns) or specific properties in a relational database. It selects the columns that are specified in the query  .
- In SQL, the SELECT statement combines both selection and projection operations in a single statement.
- The syntax of the SELECT statement is as follows:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- The SELECT clause specifies the projection operation, i.e., the columns to be retrieved from the table.
- The FROM clause specifies the table name from which the data is to be retrieved.
- The WHERE clause specifies the selection operation, i.e., the condition or predicate to filter the rows.
- The SELECT * statement is a special case of the projection operation that returns all the columns in the table. It can also be used as a selection operation if no condition is specified.
- Examples of selection and projection operations in SQL are:

```sql
-- Selection operation: returns the rows where the salary is greater than 50000
SELECT * FROM employee WHERE salary > 50000;

-- Projection operation: returns the name and department columns of the employee table
SELECT name, department FROM employee;

-- Selection and projection operation: returns the name and department columns of the employee table where the salary is greater than 50000
SELECT name, department FROM employee WHERE salary > 50000;
```



### Set-theoretic operations for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- Set-theoretic operations are the standard mathematical operations on sets that can be applied to relations in a database.
- Set-theoretic operations are binary operations, meaning they operate on two relations unlike unary operations like project, select and rename.
- The two relations involved in a set-theoretic operation must be union compatible, meaning they have the same number and type of attributes .
- The major set-theoretic operations are union, intersection and set difference.
- Union operation combines the tuples of two relations and eliminates any duplicates . The symbol for union is ∪.
- Intersection operation returns the tuples that are common to both relations . The symbol for intersection is ∩.
- Set difference operation returns the tuples that are in one relation but not in the other . The symbol for set difference is -.
- An example of set-theoretic operations using two relations R and S is shown below:

| R | A | B |
|---|---|---|
|   | 1 | 2 |
|   | 3 | 4 |
|   | 5 | 6 |

| S | A | B |
|---|---|---|
|   | 3 | 4 |
|   | 7 | 8 |
|   | 9 | 10 |

R ∪ S = 

| A | B |
|---|---|
| 1 | 2 |
| 3 | 4 |
| 5 | 6 |
| 7 | 8 |
| 9 | 10 |

R ∩ S = 

| A | B |
|---|---|
| 3 | 4 |

R - S = 

| A | B |
|---|---|
| 1 | 2 |
| 5 | 6 |

S - R = 

| A | B |
|---|---|
| 7 | 8 |
| 9 | 10 |



### Join Operations

- A join operation is a way of combining data from two or more tables based on a common attribute or a logical relationship.
- A join operation allows queries across multiple tables and produces a result set that contains the relevant data from each table.
- A join operation is based on the relational algebra operation of the same name, which is a combination of Cartesian product and selection.
- A join operation requires a join condition, which specifies how the tables are related and what values to compare from each table.
- A join condition typically involves a foreign key from one table and its associated primary key in the other table, and a logical operator such as =, <>, <, >, etc.
- There are different types of join operations, such as inner join, outer join, cross join, self join, etc. Each type of join has a different way of handling the rows that do not match the join condition.
- The most common type of join is the inner join, which returns only the rows that match the join condition from both tables.
- An outer join returns all the rows that match the join condition, as well as the rows that do not match from one or both tables, depending on the type of outer join (left, right, or full).
- A cross join returns the Cartesian product of the two tables, which is all the possible combinations of rows from both tables. A cross join does not require a join condition, but it can be filtered by a WHERE clause.
- A self join is a special type of join that involves joining a table to itself, using different aliases for the same table. A self join can be useful for finding hierarchical or recursive relationships within a table.



## Unit 4 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that organizes the data into tables and columns to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design by creating atomic elements, i.e., elements that cannot be broken down into smaller parts.
- Normalization is based on a series of normal forms, which are rules that define the level of data organization and quality.
- The most common normal forms are:
  - First normal form (1NF): Each column in a table contains only one value, and each row is unique. There are no repeating groups or arrays in a table.
  - Second normal form (2NF): Each column in a table that is not part of the primary key depends on the whole primary key. There are no partial dependencies in a table.
  - Third normal form (3NF): Each column in a table that is not part of the primary key depends only on the primary key. There are no transitive dependencies in a table.
  - Boyce-Codd normal form (BCNF): Each determinant in a table is a candidate key. A determinant is a column or a set of columns that determines the value of another column.
  - Fourth normal form (4NF): Each column in a table contains only one value from a single domain, and each row is unique. There are no multi-valued dependencies in a table.
  - Fifth normal form (5NF): Each column in a table is part of a candidate key or a join dependency. A join dependency is a condition that specifies how a table can be reconstructed from its projections.
- Normalization is a progressive process, and a higher level of normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization has many benefits, such as:
  - Eliminating data anomalies, such as insertion, deletion, and update anomalies, that can cause data inconsistency and corruption.
  - Reducing data redundancy and storage space, which can improve performance and efficiency.
  - Enhancing data integrity and security, which can prevent unauthorized access and modification.
  - Facilitating data manipulation and querying, which can improve usability and functionality.
- Normalization also has some drawbacks, such as:
  - Increasing the number of tables and joins, which can complicate the database design and maintenance.
  - Decreasing the query performance and speed, which can affect the user experience and satisfaction.
  - Losing some information or context, which can reduce the data quality and completeness.



### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database  .
- A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X determines the value of Y  .
- A functional dependency is used to establish relationships between attributes and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A FD is trivial if Y is a subset of X, i.e., X -> Y is trivial if Y ⊆ X. For example, A -> A or A, B -> A are trivial FDs .
  - Non-trivial functional dependency: A FD is non-trivial if Y is not a subset of X, i.e., X -> Y is non-trivial if Y ⊄ X. For example, A -> B or A, B -> C are non-trivial FDs .
  - Multivalued functional dependency: A FD is multivalued if for a given value of X, there are multiple values of Y that are independent of each other, i.e., X ->> Y. For example, A ->> B, C means that for a given value of A, there are multiple values of B and C that are unrelated .
  - Transitive functional dependency: A FD is transitive if X -> Y and Y -> Z, then X -> Z. For example, A -> B and B -> C, then A -> C is a transitive FD .
- A relation is said to be in a certain normal form if it satisfies certain functional dependencies and other constraints. There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF)  .
- The process of normalization is to decompose a relation into smaller relations that are in higher normal forms and that preserve the original information and functional dependencies  .



### Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Normal forms are a set of rules or guidelines for designing relational databases in a way that reduces data redundancy and improves data integrity .
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes in a relation such that the values of one set determine the values of the other set .
- There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF)   .
- A relation is said to be in a certain normal form if it satisfies the conditions of that normal form and all the lower normal forms. For example, a relation in 3NF is also in 2NF and 1NF .
- The main benefits of normalizing a database are:
  - It eliminates or reduces data duplication, which saves storage space and improves performance .
  - It ensures data consistency and accuracy, which prevents data anomalies and errors .
  - It facilitates data manipulation and querying, which makes it easier to retrieve and update data .
- The main drawbacks of normalizing a database are:
  - It may increase the number of tables and joins, which can complicate the database design and query processing .
  - It may reduce the efficiency of some queries that require denormalized data, which can affect performance and usability .
  - It may not capture all the business rules and constraints, which can lead to data integrity violations .
- The process of normalizing a database involves the following steps:
  - Identify all the candidate keys and functional dependencies in the relation .
  - Decompose the relation into smaller relations that satisfy the conditions of the desired normal form .
  - Check for any data anomalies or integrity violations in the normalized relations .
  - Refine the normalized relations if necessary to improve the database design .



### Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design by eliminating or minimizing the anomalies and inconsistencies that may arise from data manipulation operations such as insertion, deletion, and update.
- There are several levels of normalization, each with a specific set of criteria that a database must satisfy to be in that normal form. The most common normal forms are:
  - First normal form (1NF): A database is in 1NF if every table has a primary key and every column contains atomic values (i.e., values that cannot be further decomposed).
  - Second normal form (2NF): A database is in 2NF if it is in 1NF and every non-key column depends on the whole primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): A database is in 3NF if it is in 2NF and every non-key column depends only on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): A database is in BCNF if it is in 3NF and every determinant (i.e., a column or a set of columns that determines another column) is a candidate key (i.e., a minimal set of columns that uniquely identifies a row).
  - Fourth normal form (4NF): A database is in 4NF if it is in BCNF and every multi-valued dependency (i.e., a dependency where a column or a set of columns can have more than one value for a given primary key value) is trivial (i.e., it involves only the primary key) or is implied by a candidate key.
  - Fifth normal form (5NF): A database is in 5NF if it is in 4NF and every join dependency (i.e., a dependency where a table can be decomposed into two or more tables and then reconstructed by joining them on a common set of columns) is trivial (i.e., it involves only the primary key) or is implied by a candidate key.
- The higher the normal form, the less redundancy and more consistency the database has, but also the more tables and joins it may require, which can affect the performance and complexity of the database. Therefore, the optimal level of normalization depends on the nature and purpose of the database and the trade-off between data quality and data efficiency.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of second for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System.

### Second

- Second is a unit of time that is equal to one sixtieth of a minute or 1000 milliseconds.
- Second is also a unit of angular measurement that is equal to one sixtieth of a degree or 3600th of a circle.
- Second is also a term used in database design and normalization to refer to the second normal form (2NF), which is a level of data integrity that ensures that every non-key attribute in a table is fully functionally dependent on the primary key.
- Second normal form (2NF) is achieved by eliminating partial dependencies, which are dependencies between a non-key attribute and a proper subset of the primary key.
- For example, if a table has a composite primary key of (student_id, course_id) and a non-key attribute of student_name, then student_name is partially dependent on student_id, which is a subset of the primary key. To achieve 2NF, student_name should be moved to a separate table with student_id as the primary key.
- Second normal form (2NF) is a prerequisite for achieving the third normal form (3NF), which is a higher level of data integrity that eliminates transitive dependencies, which are dependencies between a non-key attribute and another non-key attribute that is transitively dependent on the primary key.



### Third Normal Form for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if it is in second normal form (2NF) and every non-key attribute is non-transitively dependent on the primary key. That is, there is no functional dependency between two non-key attributes.
- A functional dependency is a relationship between two sets of attributes such that for a given value of one set, there is only one possible value of the other set.
- A transitive dependency is a functional dependency between two non-key attributes that are both functionally dependent on the primary key.
- For example, consider a table with the attributes Student ID, Student Name, Course ID, Course Name, and Instructor Name. The primary key is Student ID and Course ID. The table is not in 3NF because there is a transitive dependency between Course Name and Instructor Name. That is, Course Name determines Instructor Name and both are non-key attributes. To make the table in 3NF, we need to split it into two tables: one with Student ID, Student Name, and Course ID, and another with Course ID, Course Name, and Instructor Name.
- The benefits of 3NF are that it eliminates data redundancy, improves data consistency, avoids data anomalies, and preserves data integrity.
- The drawbacks of 3NF are that it may increase the number of tables and joins, reduce query performance, and complicate data manipulation.
- The Third Normal Form is also considered to be the ample requirement to build a database as the tables in the Third Normal Form are devoid of insert, update or delete anomalies.
- The Third Normal Form removes the redundancy effectively so the data becomes consistent as well as maintains the data integrity.
- The Third Normal Form always ensures functional dependency preserving and lossless.



### BCNF

- BCNF stands for Boyce-Codd Normal Form     .
- It is an advanced version of 3NF (Third Normal Form)   .
- It is also sometimes referred to as 3.5NF or 3.5 Normal Form.
- It is based on functional dependencies that take into account all candidate keys in a relation .
- A relation is in BCNF if and only if for every functional dependency X -> Y, X is a superkey    .
- A superkey is a set of attributes that uniquely identifies a tuple in a relation.
- A candidate key is a minimal superkey, that is, a superkey that has no proper subset that is also a superkey.
- A prime attribute is an attribute that belongs to any candidate key.
- BCNF eliminates the possibility of having non-trivial functional dependencies of attributes on anything other than a superset of a candidate key .
- BCNF ensures that every determinant is a candidate key.
- BCNF helps to reduce redundancy and anomalies in a relation.

#### Example of BCNF

- Consider a relation R with attributes A, B, C, D, E and the following functional dependencies:

  - A -> BC
  - C -> DE

- The candidate keys are {A} and {C}.
- The relation R is in 3NF, but not in BCNF, because the functional dependency A -> BC violates the BCNF condition, as A is not a superkey.
- To convert R into BCNF, we need to decompose it into two relations:

  - R1(A, B, C) with the functional dependency A -> BC
  - R2(C, D, E) with the functional dependency C -> DE

- Both R1 and R2 are in BCNF, as the left-hand side of each functional dependency is a superkey.
- The decomposition preserves the functional dependencies and reduces redundancy and anomalies.



### Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that specifies that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency can be expressed as R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ denotes the subset relation  .
- The inclusion dependency holds for a database if each tuple that is a member of the relation corresponding to the left-hand side is also in the relation corresponding to the right-hand side.
- Inclusion dependency can be checked by performing a natural join of the two relations and comparing the result with the left-hand side relation.
- Inclusion dependency can be enforced by creating foreign key constraints or triggers in the database.



### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R   .
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data .
- Lossless join decomposition is based on the concept of functional dependencies, which are constraints that specify how one set of attributes determines another set of attributes in a relation.
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the set of functional dependencies F for R   :
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
  - where R1 ∩ R2 is the set of common attributes between R1 and R2, and → denotes functional dependency.
- A decomposition of R into R1, R2, ... Rn is lossless if and only if the decomposition of R into R1 and R2 is lossless, and the decomposition of R2 into R3 and R4 is lossless, and so on.
- Lossless join decomposition can be achieved by using decomposition algorithms such as BCNF and 3NF, which are based on the concepts of normal forms and minimal covers.



### Normalization using FD

- Normalization is the process of designing a relational database schema to minimize redundancy and anomalies.
- Functional dependency (FD) is a constraint that describes the relationship between attributes in a relation.
- A FD X -> Y means that the values of Y are determined by the values of X. Two tuples sharing the same values of X will necessarily have the same values of Y.
- A FD is trivial if Y is a subset of X, or full if Y is not a subset of X.
- A FD is called a superkey if X is a superkey of the relation, or a candidate key if X is a candidate key of the relation.
- A FD is called a partial dependency if there is a proper subset of X that determines Y, or a transitive dependency if there is an attribute Z that is not part of any candidate key and X -> Z and Z -> Y.
- Normalization using FD involves applying a series of normal forms to a relation, each with a specific condition that must be satisfied.
- The normal forms are:

  - First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. All attributes must be atomic.
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and has no partial dependencies. All non-key attributes must depend on the whole candidate key.
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and has no transitive dependencies. All non-key attributes must depend only on the candidate keys.
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and has no FDs that violate the candidate keys. All FDs must have a candidate key on the left hand side.
  - Fourth normal form (4NF): A relation is in 4NF if it is in BCNF and has no multivalued dependencies. A multivalued dependency X ->> Y means that for each value of X, there is a set of values of Y that are associated with it.
  - Fifth normal form (5NF): A relation is in 5NF if it is in 4NF and has no join dependencies. A join dependency means that the relation can be decomposed into two or more relations that can be joined back to get the original relation.

- Normalization using FD can be done by following these steps:

  - Identify all the FDs that hold in the relation.
  - Check if the relation is in 1NF. If not, decompose it into 1NF relations.
  - Check if the relation is in 2NF. If not, decompose it into 2NF relations by eliminating partial dependencies.
  - Check if the relation is in 3NF. If not, decompose it into 3NF relations by eliminating transitive dependencies.
  - Check if the relation is in BCNF. If not, decompose it into BCNF relations by eliminating FDs that violate the candidate keys.
  - Check if the relation is in 4NF. If not, decompose it into 4NF relations by eliminating multivalued dependencies.
  - Check if the relation is in 5NF. If not, decompose it into 5NF relations by eliminating join dependencies.
  - Check if the decomposition is lossless and dependency-preserving. If not, try to find a better decomposition or use other techniques to ensure data integrity.



### MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for multivalued dependency, which is a type of constraint between two sets of attributes in a relation.
- A multivalued dependency occurs when one attribute determines multiple values of another attribute, independently of the other attributes in the relation.
- For example, if a relation has attributes employee, project, and hobby, and an employee can work on multiple projects and have multiple hobbies, then there is a multivalued dependency between employee and project, and between employee and hobby.
- MVDs can cause redundancy and inconsistency in a relation, as the same information may be repeated for different combinations of attributes.
- To avoid MVDs, a relation should be normalized to the fourth normal form (4NF), which requires that a relation be in the boyce-codd normal form (BCNF) and have no MVDs.
- To normalize a relation to 4NF, we can use the following algorithm:
  - Identify all the MVDs in the relation
  - For each MVD X --> --> Y, decompose the relation into two relations: one with attributes X and Y, and one with attributes X and the remaining attributes
  - Repeat the process until there are no more MVDs in any relation
- Normalization reduces programming effort, as rules are enforced in one place, one way, one time. It also helps maintain consistency and saves space by eliminating redundancy.



Hello, I am Sydney, your AI assistant. I can help you with your topic of Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System. Here are some notes that you can use for your study material:

# Unit 4 - Data Base Design & Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for the data in a database system.
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and the user requirements.
- Database design also involves choosing the appropriate data types, keys, indexes, and storage options for the data.
- Database design aims to achieve the following objectives:
  - Ensure data integrity, consistency, and accuracy
  - Avoid data redundancy and anomalies
  - Optimize data access and performance
  - Facilitate data security and privacy
  - Support data maintenance and evolution

## Normalization
- Normalization is an important process in database design that helps in improving the efficiency, consistency, and accuracy of the database.
- Normalization makes it easier to manage and maintain the data and ensures that the database is adaptable to changing business needs.
- Normalization is based on the concept of normal forms, which are rules or criteria that define the degree of organization of the data in a table.
- Normal forms are numbered from 1 to 5, with higher normal forms being more normalized and having fewer anomalies and redundancies.
- The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or arrays of data, and every attribute is atomic, meaning it cannot be further subdivided.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be derived from any other attribute or subset of attributes in the table.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be derived from any other non-key attribute in the table.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies on any non-key attribute.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, meaning there are no attributes that depend on more than one independent attribute in the table.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, meaning it cannot be decomposed into two or more tables without losing information.

## Normalization Process
- The normalization process involves the following steps:
  - Determine the purpose and scope of the database
  - Identify the entities and attributes that represent the problem domain and the user requirements
  - Define the functional dependencies and the candidate keys for each entity
  - Check if the entities are in 1NF and eliminate any repeating groups or arrays of data
  - Check if the entities are in 2NF and eliminate any partial dependencies on the primary key
  - Check if the entities are in 3NF and eliminate any transitive dependencies on the primary key
  - Check if the entities are in BCNF and eliminate any non-key dependencies on the candidate keys
  - Check if the entities are in 4NF and eliminate any multi-valued dependencies
  - Check if the entities are in 5NF and eliminate any join dependencies
  - Review and refine the database design and ensure that it meets the user requirements and the business rules
  - Implement the database design using the appropriate data types, keys, indexes, and storage options

## References
-  Introduction of Database Normalization - GeeksforGeeks
-  Db2 11 - Introduction - Normalization in database design - IBM
-  A Step-By-Step Guide to Normalization in DBMS With Examples - Database Star
-  Database design basics - Microsoft Support



### Alternative Approaches to Database Design

- Database design is the process of defining the structure, organization, and relationships of data in a database.
- Database design can be influenced by various factors, such as the application requirements, the data characteristics, the performance goals, and the available technologies.
- There are different approaches and techniques that can be used to design a database, depending on the context and the objectives of the project.
- Some of the alternative approaches and advanced techniques for database design are:

  - **Application Development Tools**: These are software tools that allow users to create, manage, and analyze data without requiring extensive technical skills or knowledge of database design. Some examples of these tools are Office Reports, Second Prism, Databoard, DataMarket, and Q Research Software. These tools can facilitate the data analysis process, provide interactive and visual data exploration, and enable data sharing and collaboration. However, these tools may also have some limitations, such as data quality issues, security risks, and lack of customization and flexibility.
  - **Domain Model from Use Cases**: This is an approach that uses Agile methodologies to design a database based on the business processes and user interactions. Instead of using Entity Relationship Diagrams (ERDs), this approach uses Domain Models, which are graphical representations of the concepts and relationships in a domain. A domain model can be derived from use cases, which are descriptions of how users interact with a system to achieve a goal. This approach can help to capture the user requirements, ensure alignment with the business objectives, and facilitate communication and feedback. However, this approach may also require more iterations, revisions, and validations, as well as more coordination and collaboration among the stakeholders.
  - **Normalization**: This is a technique that organizes the data in a database into tables that minimize data redundancy and dependency. Normalization involves dividing larger tables into smaller tables and linking them together using relationships. Normalization can improve the data integrity, consistency, and efficiency of a database. However, normalization may also increase the complexity and the number of joins required to query the data, which can affect the performance and usability of a database.
  - **NoSQL Databases**: These are databases that do not follow the relational model and do not use SQL as the query language. NoSQL databases can store and process large and typically unstructured data sets, such as JSON documents, key-value pairs, graphs, or columns. NoSQL databases can offer rapid scalability, flexibility, and performance, as they do not require a predefined schema, support horizontal partitioning, and allow parallel processing. However, NoSQL databases may also have some drawbacks, such as lack of standardization, consistency, and security, as well as difficulty in querying and analyzing the data.



## Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several types of statements, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL statements are used to define the structure and schema of the database, such as CREATE, ALTER, and DROP.
- DML statements are used to insert, update, delete, and modify data in the database, such as INSERT, UPDATE, DELETE, and MERGE.
- DCL statements are used to control the access and privileges of users and roles in the database, such as GRANT, REVOKE, and DENY.
- DQL statements are used to retrieve and manipulate data from the database, such as SELECT, JOIN, GROUP BY, and ORDER BY.
- SQL also supports various functions, operators, clauses, and keywords to perform complex operations and calculations on the data, such as aggregate functions, logical operators, subqueries, and CASE expressions.
- SQL is a declarative language, which means that it specifies what data to retrieve or manipulate, rather than how to do it. The database management system (DBMS) is responsible for executing and optimizing the SQL statements.
- SQL is a standardized language, but different DBMSs may have different implementations, extensions, and variations of SQL, such as MySQL, Oracle, SQL Server, and PostgreSQL. Therefore, some SQL statements may not work or behave differently across different DBMSs.



### Basics of SQL

- SQL stands for **Structured Query Language**   , which is a computer language for storing, manipulating and retrieving data stored in a **relational database**   .
- SQL is a **standard language** for accessing and manipulating databases, and it became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987.
- SQL can be used in different database systems, such as MySQL, SQL Server, MS Access, Oracle, Sybase, Informix, Postgres, and others.
- SQL can perform four basic operations in any database, which are known as **CRUD** operations. CRUD stands for **Create, Read, Update and Delete**.
  - **Create** new data with **INSERT** statements.
  - **Read** data with **SELECT** statements.
  - **Update** data with **UPDATE** statements.
  - **Delete** data with **DELETE** statements.
- SQL can also perform other tasks, such as creating, modifying and deleting tables, views, indexes, constraints, triggers, functions, procedures, etc.
- SQL has a simple and easy to learn syntax, which consists of **keywords**, **clauses**, **expressions**, **operators**, **functions**, **comments**, etc.
- SQL follows some basic rules, such as:
  - SQL keywords are not case sensitive, but it is a good practice to write them in uppercase.
  - SQL statements end with a semicolon (;).
  - SQL comments start with -- or /* and end with */.
  - SQL identifiers, such as table names, column names, etc., can be written in any case, but they must be enclosed in double quotes (") if they contain spaces or special characters.
  - SQL values, such as strings, dates, numbers, etc., must be enclosed in single quotes (') if they are not numeric.
  - SQL expressions can be used to calculate values, compare values, combine values, etc.
  - SQL operators can be used to perform arithmetic, logical, comparison, bitwise, etc., operations on values.
  - SQL functions can be used to perform various tasks, such as formatting, converting, aggregating, etc., on values.
  - SQL clauses can be used to specify different parts of a SQL statement, such as SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, etc.
- SQL is a powerful and versatile language that can handle complex and large amounts of data in a relational database. SQL is widely used by data professionals and users for various purposes, such as data analysis, data reporting, data mining, data warehousing, etc .



### DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that can be used to create, modify, and delete the structure of database objects, such as tables, views, indexes, etc.
- DDL commands do not affect the data stored in the database, but only the schema or the definition of the database objects.
- Some of the common DDL commands are:
  - CREATE: This command is used to create a new database object, such as a table, a view, an index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table named students with three columns: id, name, and age.
  - ALTER: This command is used to modify an existing database object, such as adding, dropping, or renaming a column, changing the data type of a column, adding or dropping a constraint, etc. For example, `ALTER TABLE students ADD email VARCHAR(50);` adds a new column named email to the students table.
  - DROP: This command is used to delete an existing database object, such as a table, a view, an index, etc. For example, `DROP TABLE students;` deletes the students table and all the data stored in it.
  - RENAME: This command is used to change the name of an existing database object, such as a table, a view, an index, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table, but keeps the table structure intact.
- DDL commands are normally executed by the database administrator or the developer, who should have the appropriate permissions to create, alter, or delete the database objects.



### DML

- Data Manipulation Language (DML) is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views .
- The main DML statements are SELECT, INSERT, DELETE, and UPDATE  .
- SELECT statement is used to retrieve data from one or more tables or views .
- INSERT statement is used to add new rows to a table .
- DELETE statement is used to remove existing rows from a table .
- UPDATE statement is used to modify existing rows in a table .
- DML statements can be used with various clauses, such as WHERE, ORDER BY, GROUP BY, HAVING, etc. to filter, sort, aggregate, and manipulate the data.
- DML statements can also be used with subqueries, joins, and set operators to combine data from multiple tables or sources.
- DML statements can be executed interactively or embedded in a program or script.



### DCL

- Data Control Language (DCL) is a sublanguage of SQL that deals with the commands used to control access to data stored in a database (authorization).
- DCL allows the database owner to grant, revoke, or change the permissions for different users or roles on the database objects, such as tables, views, procedures, etc. .
- DCL is used to enforce data security and prevent unauthorized access or modification of data.
- The main DCL commands in SQL are:
  - **GRANT**: This command is used to grant (give access to) specific privileges to a user or a role on a database object. For example, `GRANT SELECT ON employees TO user1;` grants the privilege to select data from the employees table to user1 .
  - **REVOKE**: This command is used to revoke (take away) specific privileges from a user or a role on a database object. For example, `REVOKE UPDATE ON employees FROM user1;` revokes the privilege to update data in the employees table from user1 .
  - **DENY**: This command is used to deny (block) specific privileges to a user or a role on a database object. For example, `DENY INSERT ON employees TO user1;` denies the privilege to insert data into the employees table to user1.
- DCL commands can also be used to grant or revoke system-level privileges, such as creating or dropping tables, views, procedures, etc. For example, `GRANT CREATE TABLE TO user1;` grants the privilege to create tables to user1.
- DCL commands can also be used with the `WITH GRANT OPTION` clause to allow a user or a role to grant or revoke the same privileges to or from other users or roles. For example, `GRANT SELECT ON employees TO user1 WITH GRANT OPTION;` grants the privilege to select data from the employees table to user1 and also allows user1 to grant the same privilege to other users or roles.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some advantages of SQL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### Advantages of SQL

- **Faster and efficient query processing**: SQL can process a large amount of data in a very short amount of time. This high speed can boost the amount of data retrieval and manipulation  .
- **No coding skills required**: SQL uses simple English phrases and keywords to perform data operations. For data retrieval, large number of lines of code is not required. All basic keywords such as SELECT, INSERT, UPDATE, DELETE, etc. are easy to learn and use.
- **Standardized language**: SQL is a standardized language that is widely used and supported by many database management systems. SQL can work with different types of databases, such as relational, hierarchical, network, etc. SQL also follows the ANSI (American National Standards Institute) and ISO (International Organization for Standardization) standards .
- **Integration**: SQL can be integrated with other programming languages, such as Java, C#, Python, etc. to perform complex tasks and applications. SQL can also be embedded in web pages and applications to access and manipulate data from the web.
- **Business intelligence**: SQL can help businesses to analyze and understand their data better. SQL can perform various functions, such as data aggregation, data transformation, data visualization, data mining, etc. to generate insights and reports from the data. SQL can also help businesses to make better decisions and improve their performance.



### SQL Data Type and Literals

- SQL data types are used to represent the nature of the data that can be stored in the database table. Every field or column in a table is given a data type when a table is defined .
- SQL data types can be categorized into three main groups: string, numeric, and date and time.
- String data types are used to store text or character data, such as names, addresses, descriptions, etc. Some examples of string data types are char, varchar, text, nchar, nvarchar, etc.
- Numeric data types are used to store numbers, such as integers, decimals, fractions, etc. Some examples of numeric data types are int, bigint, smallint, tinyint, decimal, numeric, float, real, etc.
- Date and time data types are used to store date and time values, such as year, month, day, hour, minute, second, etc. Some examples of date and time data types are date, time, datetime, datetime2, smalldatetime, etc.
- SQL also supports some other data types, such as binary, varbinary, image, xml, bit, money, uniqueidentifier, etc .

- SQL literals are constants that represent fixed values in SQL statements. They can be used to assign values to variables, columns, or parameters .
- There are four kinds of literal values supported in SQL. They are: character string, bit string, exact numeric, and approximate numeric.
- Character string literals are enclosed in single quotes ('), such as 'Hello', 'SQL', '2021-03-15', etc .
- Bit string literals are prefixed with 0x, such as 0x0A, 0xFF, 0x1234, etc .
- Exact numeric literals are composed of digits, an optional decimal point, and an optional sign, such as 123, -45.67, 0.0, etc .
- Approximate numeric literals are composed of digits, an optional decimal point, an optional sign, and an exponent, such as 1.23E4, -6.78E-9, 0.0E0, etc .
- SQL also supports some other literals, such as date and time literals, money literals, uniqueidentifier literals, etc.



### Types of SQL Commands

SQL stands for Structured Query Language and it is a standard language for storing, manipulating and retrieving data in databases. SQL commands can be grouped into five broad categories based on their functionality  . These are:

- **Data Definition Language (DDL)**: This category consists of SQL commands that can be used to define the database structure, such as creating, altering, dropping or renaming tables, views, indexes, schemas, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new table, view, index, schema, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table called students with three columns: id, name and age.
  - ALTER: This command is used to modify the structure of an existing table, view, index, schema, etc. For example, `ALTER TABLE students ADD COLUMN email VARCHAR(50);` adds a new column called email to the students table.
  - DROP: This command is used to delete an existing table, view, index, schema, etc. For example, `DROP TABLE students;` deletes the students table and all its data.
  - RENAME: This command is used to change the name of an existing table, view, index, schema, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.

- **Data Manipulation Language (DML)**: This category consists of SQL commands that can be used to manipulate the data in the database, such as inserting, updating, deleting or selecting data from tables, views, etc. Some examples of DML commands are:

  - INSERT: This command is used to insert new data into a table or view. For example, `INSERT INTO students (id, name, age, email) VALUES (1, 'Alice', 20, 'alice@example.com');` inserts a new row into the students table with the specified values.
  - UPDATE: This command is used to modify the existing data in a table or view. For example, `UPDATE students SET age = 21 WHERE id = 1;` updates the age of the student with id 1 to 21.
  - DELETE: This command is used to delete the existing data from a table or view. For example, `DELETE FROM students WHERE age > 25;` deletes all the rows from the students table where the age is greater than 25.
  - SELECT: This command is used to query or retrieve data from a table or view. For example, `SELECT name, email FROM students WHERE age < 22;` selects the name and email of the students whose age is less than 22.

- **Data Query Language (DQL)**: This category consists of SQL commands that can be used to query or retrieve data from the database, such as selecting, filtering, sorting, grouping, aggregating or joining data from tables, views, etc. Some examples of DQL commands are:

  - SELECT: This command is used to query or retrieve data from a table or view. For example, `SELECT name, email FROM students WHERE age < 22;` selects the name and email of the students whose age is less than 22.
  - WHERE: This clause is used to filter the data based on some condition. For example, `SELECT name, email FROM students WHERE age < 22;` selects the name and email of the students whose age is less than 22.
  - ORDER BY: This clause is used to sort the data in ascending or descending order. For example, `SELECT name, email FROM students ORDER BY name ASC;` selects the name and email of the students and sorts them by name in ascending order.
  - GROUP BY: This clause is used to group the data based on some column or expression. For example, `SELECT age, COUNT(*) FROM students GROUP BY age;` selects the age and the number of students for each age group.
  - HAVING: This clause is used to filter the data after grouping. For example, `SELECT age, COUNT(*) FROM students GROUP BY age HAVING COUNT(*) > 1;` selects the age and the number of students for each age group where the number of students is more than 1.
  - JOIN: This clause is used to combine data from two or more tables or views based on some common column or condition. For example, `SELECT s.name, s.email, c.name FROM students s



### SQL operators and their procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They are used to specify conditions, filter results, compare values, perform calculations, concatenate strings, and more. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used for mathematical operations on numerical data, such as adding, subtracting, multiplying, dividing, and finding the remainder. The arithmetic operators in SQL are:

  - `+` (Addition): This operator adds two numbers together. For example, `SELECT 10 + 10;` returns 20.
  - `-` (Subtraction): This operator subtracts one number from another. For example, `SELECT 20 - 10;` returns 10.
  - `*` (Multiplication): This operator multiplies two numbers together. For example, `SELECT 10 * 10;` returns 100.
  - `/` (Division): This operator divides one number by another. For example, `SELECT 20 / 10;` returns 2.
  - `%` (Modulus): This operator returns the remainder of one number divided by another. For example, `SELECT 20 % 10;` returns 0.

- Bitwise operators: These operators are used for manipulating bits in binary data, such as performing logical operations, shifting bits, and inverting bits. The bitwise operators in SQL are:

  - `&` (Bitwise AND): This operator performs a logical AND operation on each pair of bits in two binary values and returns a new binary value. For example, `SELECT 5 & 3;` returns 1, because 5 in binary is 0101 and 3 in binary is 0011, and 0101 & 0011 = 0001.
  - `|` (Bitwise OR): This operator performs a logical OR operation on each pair of bits in two binary values and returns a new binary value. For example, `SELECT 5 | 3;` returns 7, because 5 in binary is 0101 and 3 in binary is 0011, and 0101 | 0011 = 0111.
  - `^` (Bitwise XOR): This operator performs a logical XOR operation on each pair of bits in two binary values and returns a new binary value. For example, `SELECT 5 ^ 3;` returns 6, because 5 in binary is 0101 and 3 in binary is 0011, and 0101 ^ 0011 = 0110.
  - `~` (Bitwise NOT): This operator performs a logical NOT operation on each bit in a binary value and returns a new binary value. For example, `SELECT ~5;` returns -6, because 5 in binary is 0101 and ~0101 = 1010, which is -6 in two's complement notation.
  - `<<` (Left Shift): This operator shifts the bits in a binary value to the left by a specified number of positions and returns a new binary value. For example, `SELECT 5 << 2;` returns 20, because 5 in binary is 0101 and 0101 << 2 = 010100, which is 20 in decimal.
  - `>>` (Right Shift): This operator shifts the bits in a binary value to the right by a specified number of positions and returns a new binary value. For example, `SELECT 20 >> 2;` returns 5, because 20 in binary is 010100 and 010100 >> 2 = 0101, which is 5 in decimal.

- Comparison operators: These operators are used for comparing two values or expressions and returning a boolean value (true or false) based on the result of the comparison. The comparison operators in SQL are:

  - `=` (Equal): This operator returns true if the two values or expressions are equal, and false otherwise. For example, `SELECT 10 = 10;` returns true, and `SELECT 10 = 20;` returns false.
  - `<>` or `!=` (Not Equal): This operator returns true if the two values or expressions are not equal, and false otherwise. For example, `SELECT 10 <> 10;` or `SELECT 10 != 10;` returns false, and `SELECT 10 <> 20;` or `SELECT 10 != 20;` returns true.
  - `>` (Greater Than):



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write some notes on the topic of tables – creation and alteration for the unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here are some points that you can use for your study material:

### Tables – creation and alteration

- A table is a collection of data organized in rows and columns in a relational database.
- A table has a name, a set of attributes (columns), and a set of tuples (rows) that store the data values.
- A table can be created using the CREATE TABLE statement in SQL, which specifies the name of the table, the attributes and their data types, and any constraints on the attributes or the table.
- For example, the following statement creates a table called STUDENT with four attributes: ID, NAME, AGE, and MAJOR.

```sql
CREATE TABLE STUDENT (
  ID INT PRIMARY KEY,
  NAME VARCHAR(50) NOT NULL,
  AGE INT CHECK (AGE > 0),
  MAJOR VARCHAR(20)
);
```

- A table can be modified using the ALTER TABLE statement in SQL, which allows adding, deleting, or changing the attributes or the constraints of the table.
- For example, the following statement adds a new attribute called GPA to the STUDENT table.

```sql
ALTER TABLE STUDENT
ADD GPA DECIMAL(3,2) CHECK (GPA BETWEEN 0 AND 4);
```

- The following statement deletes the attribute MAJOR from the STUDENT table.

```sql
ALTER TABLE STUDENT
DROP COLUMN MAJOR;
```

- The following statement changes the data type of the attribute NAME from VARCHAR(50) to VARCHAR(100) in the STUDENT table.

```sql
ALTER TABLE STUDENT
ALTER COLUMN NAME VARCHAR(100);
```

- A table can be deleted using the DROP TABLE statement in SQL, which removes the table and all its data from the database.
- For example, the following statement deletes the STUDENT table.

```sql
DROP TABLE STUDENT;
```



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of defining constraints for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System.

### Defining Constraints

- Constraints are rules that restrict the values or formats of the data in a table or a column.
- Constraints can be defined at the column level or the table level.
- Constraints can be used to enforce data integrity, ensure data consistency, and prevent data anomalies.
- Some common types of constraints are:

  - **Primary key constraint**: A primary key constraint defines a column or a set of columns that uniquely identify each row in a table. A table can have only one primary key constraint. A primary key constraint also implies a not null constraint and a unique constraint on the column or columns involved.
  - **Foreign key constraint**: A foreign key constraint defines a column or a set of columns that refer to the primary key or a unique key of another table. A foreign key constraint establishes a relationship between two tables and ensures referential integrity. A table can have multiple foreign key constraints.
  - **Unique constraint**: A unique constraint defines a column or a set of columns that have unique values in a table. A table can have multiple unique constraints. A unique constraint also implies a not null constraint on the column or columns involved.
  - **Not null constraint**: A not null constraint defines a column that cannot have null values. A table can have multiple not null constraints. A not null constraint can be combined with other constraints such as primary key, foreign key, or unique.
  - **Check constraint**: A check constraint defines a condition that must be satisfied by the values in a column or a table. A table can have multiple check constraints. A check constraint can be used to validate data ranges, formats, or patterns.

- Constraints can be defined using the `CONSTRAINT` keyword in the `CREATE TABLE` or `ALTER TABLE` statements.
- Constraints can be named or unnamed. If a constraint is unnamed, the system will generate a default name for it.
- Constraints can be enabled or disabled. An enabled constraint is enforced by the system and prevents any violation of the rule. A disabled constraint is not enforced by the system and allows any violation of the rule. Constraints can be enabled or disabled using the `ENABLE` or `DISABLE` keywords in the `ALTER TABLE` statement.
- Constraints can be validated or not validated. A validated constraint is checked by the system for any existing violation of the rule in the table. A not validated constraint is not checked by the system for any existing violation of the rule in the table. Constraints can be validated or not validated using the `VALIDATE` or `NOVALIDATE` keywords in the `ALTER TABLE` statement.



### Views and Indexes in SQL

- A **view** is a named query that is stored in the database and can be used like a table. A view can simplify complex queries, hide sensitive data, or provide a consistent interface for different tables. 
- A view can be created using the `CREATE VIEW` statement, followed by the view name and the query definition. For example:

```sql
CREATE VIEW employee_view AS
SELECT employee_id, first_name, last_name, department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;
```

- A view can be queried, updated, inserted, or deleted from, as long as it follows certain rules. For example, a view cannot be updated if it contains aggregate functions, joins, or subqueries. 
- An **index** is a data structure that improves the speed of data retrieval from a table. An index can be created on one or more columns of a table, and it allows the database to quickly find the rows that match a given condition. 
- An index can be created using the `CREATE INDEX` statement, followed by the index name and the table and column names. For example:

```sql
CREATE INDEX idx_last_name ON employees (last_name);
```

- An index can be either **clustered** or **nonclustered**. A clustered index defines the physical order of the rows in the table, and there can be only one clustered index per table. A nonclustered index does not affect the physical order of the rows, but it creates a separate data structure that points to the rows. A table can have multiple nonclustered indexes. 
- An **indexed view** is a view that has a clustered index on it. An indexed view can improve the performance of queries that use the view, because the view is stored as a table in the database and the query optimizer can use the index to find the data faster.  
- An indexed view can be created using the `CREATE VIEW` statement with the `WITH SCHEMABINDING` option, followed by the `CREATE UNIQUE CLUSTERED INDEX` statement on the view. For example:

```sql
CREATE VIEW employee_view WITH SCHEMABINDING AS
SELECT employee_id, first_name, last_name, department_name
FROM dbo.employees
JOIN dbo.departments ON employees.department_id = departments.department_id;
GO
CREATE UNIQUE CLUSTERED INDEX idx_employee_view ON employee_view (employee_id);
```

- An indexed view has some limitations and requirements, such as the view must be schema-bound, the view must have a unique clustered index, and the view definition must follow certain rules. For more details, see  and .



### Queries and Subqueries in SQL

- A query is a request for data from a database that follows the syntax and rules of the Structured Query Language (SQL).
- A subquery, also known as a nested query or an inner query, is a query within another query that provides data for the outer query.
- A subquery can be used in different clauses of an SQL statement, such as the SELECT, FROM, WHERE, HAVING, or JOIN clause.
- A subquery can return a single value, a single row, a single column, or a table of values or rows.
- A subquery can be correlated or uncorrelated. A correlated subquery depends on the outer query for its values, while an uncorrelated subquery can be executed independently of the outer query.
- A subquery can be used for various purposes, such as filtering, aggregation, comparison, or existence testing.

Some examples of subqueries are:

- A subquery in the SELECT clause that returns a single value:

```sql
SELECT name, salary, (SELECT AVG(salary) FROM employees) AS average_salary
FROM employees;
```

- A subquery in the FROM clause that returns a table:

```sql
SELECT name, department, salary
FROM (SELECT * FROM employees WHERE salary > 5000) AS high_paid;
```

- A subquery in the WHERE clause that returns a single row:

```sql
SELECT name, address, phone
FROM customers
WHERE customer_id = (SELECT customer_id FROM orders WHERE order_id = 1001);
```

- A subquery in the WHERE clause that returns a single column:

```sql
SELECT name, product, quantity, price
FROM orders
WHERE product IN (SELECT product FROM products WHERE category = 'Electronics');
```

- A subquery in the WHERE clause that returns a table:

```sql
SELECT name, product, quantity, price
FROM orders
WHERE (product, quantity) IN (SELECT product, MAX(quantity) FROM orders GROUP BY product);
```

- A subquery in the HAVING clause that returns a single value:

```sql
SELECT product, SUM(quantity) AS total_quantity
FROM orders
GROUP BY product
HAVING SUM(quantity) > (SELECT AVG(quantity) FROM orders);
```

- A subquery in the JOIN clause that returns a table:

```sql
SELECT e.name, e.department, m.name AS manager
FROM employees e
JOIN (SELECT name, employee_id FROM employees WHERE position = 'Manager') m
ON e.manager_id = m.employee_id;
```

- A correlated subquery in the WHERE clause that returns a single value:

```sql
SELECT name, salary
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);
```

- A subquery with the EXISTS operator that returns a boolean value:

```sql
SELECT name, address, phone
FROM customers c
WHERE EXISTS (SELECT * FROM orders WHERE customer_id = c.customer_id);
```



### Aggregate Functions
- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used with the GROUP BY clause to calculate summary statistics for each group of rows.
- Some common aggregate functions are:
  - COUNT: returns the number of values in a set or the number of rows that satisfy a condition.
  - SUM: returns the sum of all values in a set.
  - AVG: returns the average of all values in a set.
  - MIN: returns the minimum value in a set.
  - MAX: returns the maximum value in a set.
- Aggregate functions can be used in the SELECT, HAVING, and ORDER BY clauses of a SQL query.
- Aggregate functions ignore NULL values in the set, except for COUNT(*), which counts all rows regardless of NULL values.
- Example: The following query calculates the total number of employees, the average salary, the minimum salary, and the maximum salary for each department in the employees table.

```sql
SELECT department, COUNT(*), AVG(salary), MIN(salary), MAX(salary)
FROM employees
GROUP BY department;
```



### Built-in functions for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- A built-in function is an expression in which an SQL keyword or special operator executes some operation.
- Built-in functions use keywords that are case-insensitive and can be used anywhere expressions are allowed.
- Built-in functions can be categorized into different types based on their functionality and input/output data types   .
- Some of the common types of built-in functions are:

  - **String functions**: These functions perform operations on string values, such as concatenation, extraction, conversion, searching, etc. Some examples are ASCII, CHAR, CHARINDEX, CONCAT, LEFT, RIGHT, REPLACE, etc .
  - **Numeric functions**: These functions perform calculations on numeric values, such as rounding, truncating, finding absolute value, etc. Some examples are ABS, CEILING, FLOOR, POWER, ROUND, SQRT, etc .
  - **Date and time functions**: These functions manipulate or extract information from date and time values, such as finding the current date, adding or subtracting intervals, formatting, etc. Some examples are DATEADD, DATEDIFF, DATEPART, GETDATE, YEAR, MONTH, DAY, etc .
  - **Conversion functions**: These functions convert values from one data type to another, such as converting a string to a number, a date to a string, etc. Some examples are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, etc .
  - **Logical functions**: These functions evaluate logical expressions and return a Boolean value (TRUE, FALSE, or UNKNOWN), such as checking for null values, comparing values, etc. Some examples are COALESCE, IIF, ISNULL, NULLIF, etc .
  - **Aggregate functions**: These functions perform a calculation on a set of values and return a single value, such as finding the sum, average, count, minimum, maximum, etc. Some examples are AVG, COUNT, MAX, MIN, SUM, etc  .
  - **Analytic functions**: These functions compute an aggregate value based on a group of rows, but unlike aggregate functions, they do not reduce the number of rows returned. They can also perform ranking, windowing, and other complex calculations. Some examples are CUME_DIST, DENSE_RANK, LAG, LEAD, NTILE, PERCENT_RANK, RANK, ROW_NUMBER, etc .
  - **Bit manipulation functions**: These functions perform bitwise operations on binary values, such as shifting, rotating, anding, oring, etc. Some examples are BITAND, BITOR, BITXOR, BITNOT, etc.
  - **System functions**: These functions return information about the system, such as the current user, the current database, the current session, etc. Some examples are CURRENT_USER, DB_NAME, HOST_NAME, SESSION_USER, etc .

- To use a built-in function, you need to specify the function name followed by parentheses, and optionally provide arguments inside the parentheses, depending on the function.
- For example, to use the CONCAT function to concatenate two strings, you can write:

  ```sql
  SELECT CONCAT('Hello', 'World');
  ```

- To use the AVG function to find the average salary of employees, you can write:

  ```sql
  SELECT AVG(salary) FROM employees;
  ```

- To use the RANK function to rank the employees by their salary, you can write:

  ```sql
  SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS rank FROM employees;
  ```



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here are some notes for you:

### Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying relational databases.
- SQL consists of several commands, such as `CREATE`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `DROP`, that can be used to perform different operations on database objects, such as tables, views, indexes, and constraints.
- SQL also supports various clauses, such as `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `JOIN`, and `UNION`, that can be used to filter, aggregate, sort, and combine data from one or more tables.
- SQL also supports various functions, such as `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`, and `SUBSTRING`, that can be used to perform calculations and transformations on data values.
- SQL also supports various data types, such as `INTEGER`, `VARCHAR`, `DATE`, `TIME`, and `BOOLEAN`, that can be used to define the format and range of data values stored in database columns.
- SQL also supports various constraints, such as `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and `CHECK`, that can be used to enforce the integrity and consistency of data in database tables.
- SQL also supports various keywords, such as `DISTINCT`, `ALL`, `AS`, `IN`, `BETWEEN`, and `LIKE`, that can be used to modify the behavior and output of SQL commands and clauses.

Here is an example of a SQL statement that creates a table called `students` with four columns: `id`, `name`, `age`, and `grade`:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INTEGER CHECK (age > 0),
  grade VARCHAR(2) CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
);
```

Here is an example of a SQL statement that inserts a new row into the `students` table with the values `1`, `Alice`, `20`, and `A`:

```sql
INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 20, 'A');
```

Here is an example of a SQL statement that selects all the columns and rows from the `students` table:

```sql
SELECT * FROM students;
```

Here is an example of a SQL statement that updates the `grade` column of the `students` table to `B` where the `id` column is `1`:

```sql
UPDATE students SET grade = 'B' WHERE id = 1;
```

Here is an example of a SQL statement that deletes the row from the `students` table where the `id` column is `1`:

```sql
DELETE FROM students WHERE id = 1;
```

Here is an example of a SQL statement that drops the `students` table from the database:

```sql
DROP TABLE students;
```



### Update and Delete Operations in SQL

- SQL stands for Structured Query Language, which is a standard language for manipulating data in relational databases.
- SQL has several commands for performing different operations on data, such as creating, retrieving, updating, and deleting data.
- SQL commands can be divided into two categories: Data Definition Language (DDL) and Data Manipulation Language (DML).
- DDL commands are used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, etc.
- DML commands are used to manipulate the data in the database, such as inserting, selecting, updating, and deleting data from tables and views.
- In this unit, we will focus on the update and delete operations in SQL, which are two of the most common DML commands.

#### Update Operation in SQL

- The update operation in SQL is used to modify the existing records in the database.
- The syntax of the update command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The table_name is the name of the table that contains the records to be updated.
- The SET clause specifies the columns and the new values to be assigned to them.
- The WHERE clause specifies the condition that identifies which records to be updated. If the WHERE clause is omitted, all the records in the table will be updated.
- The update command can modify one or more columns and one or more records at a time, depending on the SET and WHERE clauses.
- For example, the following update command will change the salary of the employee with id 101 to 5000 in the employees table:

```sql
UPDATE employees
SET salary = 5000
WHERE id = 101;
```

- The following update command will increase the salary of all the employees by 10% in the employees table:

```sql
UPDATE employees
SET salary = salary * 1.1;
```

#### Delete Operation in SQL

- The delete operation in SQL is used to delete the records in the database that are no longer required.
- The syntax of the delete command is:

```sql
DELETE FROM table_name
WHERE condition;
```

- The table_name is the name of the table that contains the records to be deleted.
- The WHERE clause specifies the condition that identifies which records to be deleted. If the WHERE clause is omitted, all the records in the table will be deleted.
- The delete command can delete one or more records at a time, depending on the WHERE clause.
- For example, the following delete command will delete the record of the employee with id 101 from the employees table:

```sql
DELETE FROM employees
WHERE id = 101;
```

- The following delete command will delete all the records from the employees table:

```sql
DELETE FROM employees;
```

- Note that the delete command only removes the data from the table, not the table itself. To delete the table, you need to use the drop command, which is a DDL command.



### Joins

- A join is a way of combining data from two or more tables based on a common column or condition.
- A join condition specifies how the tables are related, usually by matching values in one or more columns.
- A join can be either an inner join or an outer join, depending on whether it returns only matching rows or also includes non-matching rows.
- An inner join returns only the rows that have matching values in both tables.
- An outer join returns all the rows from one table, and the matching rows from the other table. If there is no match, the missing values are filled with NULL.
- There are three types of outer joins: left outer join, right outer join, and full outer join.
- A left outer join returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right side is filled with NULL.
- A right outer join returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left side is filled with NULL.
- A full outer join returns all the rows from both tables, and fills the missing values with NULL if there is no match.
- A join can also be a cross join, which returns the Cartesian product of the two tables, meaning every possible combination of rows from both tables.
- A join can also be a self join, which is a join of a table with itself, using different aliases to distinguish the two instances of the table.
- A join can also be a natural join, which is a join based on all the columns that have the same name and data type in both tables.
- A join can also be an equi join, which is a join that uses only the equality operator (=) in the join condition.
- A join can also be a non-equi join, which is a join that uses other operators (such as <, >, !=, etc.) in the join condition.
- A join can also be a theta join, which is a join that uses any condition in the join condition.
- A join can also be an anti join, which is a join that returns the rows from one table that do not have a match in the other table.



### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union can be used to merge data from different tables that have the same number and type of columns.
- A union can also be used to remove duplicate rows from the combined result set, or to include them by using the ALL keyword.
- The syntax of a union is:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION [ALL]
SELECT column1, column2, ..., columnN FROM table2
UNION [ALL]
...
SELECT column1, column2, ..., columnN FROM tableN;
```

- The columns in each SELECT statement must have the same name, data type, and order.
- The UNION operator applies a distinct operation to the combined result set, which means that it eliminates duplicate rows. To keep the duplicate rows, use the UNION ALL operator instead.
- The UNION operator can be combined with other SQL clauses, such as ORDER BY, LIMIT, OFFSET, etc. However, these clauses must be applied to the final result set, not to each individual SELECT statement.
- The UNION operator can be used to perform set operations, such as union, intersection, and difference, on two or more tables. For example, to find the intersection of two tables, use the following query:

```sql
SELECT column1, column2, ..., columnN FROM table1
INTERSECT
SELECT column1, column2, ..., columnN FROM table2;
```

- The INTERSECT operator is equivalent to the UNION operator with a WHERE clause that filters out the rows that are not in both tables. Similarly, to find the difference of two tables, use the following query:

```sql
SELECT column1, column2, ..., columnN FROM table1
EXCEPT
SELECT column1, column2, ..., columnN FROM table2;
```

- The EXCEPT operator is equivalent to the UNION operator with a WHERE clause that filters out the rows that are in both tables.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of intersection in SQL.

### Intersection
- The intersection operation in SQL is used to combine two queries and return only the rows that are common to both result sets.
- The syntax for the intersection operation is:

```sql
SELECT column_list
FROM table1
WHERE condition
INTERSECT
SELECT column_list
FROM table2
WHERE condition;
```

- The column_list must be the same in both queries, and the data types must be compatible.
- The intersection operation eliminates any duplicate rows from the final result set.
- The order of the rows in the final result set is not guaranteed, unless an ORDER BY clause is used.
- The intersection operation can be used to find the common elements between two tables, such as customers who bought products from both categories, employees who work in both departments, etc.

- Here are some examples of the intersection operation in SQL:

```sql
-- Find the customers who bought both books and DVDs
SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE product_category = 'Books')
INTERSECT
SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE product_category = 'DVDs');

-- Find the employees who work in both sales and marketing departments
SELECT employee_id, employee_name
FROM employees
WHERE employee_id IN (SELECT employee_id FROM department_employees WHERE department_id = 1)
INTERSECT
SELECT employee_id, employee_name
FROM employees
WHERE employee_id IN (SELECT employee_id FROM department_employees WHERE department_id = 2);
```



### Notes for Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL is used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and constraints.
- DML is used to insert, update, delete, and merge data in the database tables.
- DCL is used to grant and revoke permissions and privileges to users and roles on the database objects.
- DQL is used to retrieve and manipulate data from the database tables using various clauses, operators, functions, and expressions.
- SQL statements are composed of keywords, identifiers, literals, symbols, and comments. Keywords are reserved words that have a specific meaning and syntax in SQL. Identifiers are names of database objects, such as tables, columns, views, etc. Literals are constants, such as strings, numbers, dates, etc. Symbols are punctuation marks, such as commas, parentheses, semicolons, etc. Comments are optional texts that explain or document the SQL code, and are ignored by the SQL interpreter.
- SQL statements can be executed interactively using a command-line interface (CLI) or a graphical user interface (GUI) tool, or embedded in a host programming language, such as Java, C#, Python, etc.
- SQL statements can be classified into two categories: single-row and multiple-row statements. Single-row statements affect or return only one row at a time, such as INSERT, UPDATE, DELETE, and SELECT with a WHERE clause. Multiple-row statements affect or return more than one row at a time, such as SELECT without a WHERE clause, JOIN, GROUP BY, HAVING, and ORDER BY.
- SQL supports various data types, such as numeric, character, date and time, Boolean, binary, etc. Each data type has a range of values and a storage size. SQL also supports user-defined data types, such as domains, enums, arrays, etc.
- SQL supports various constraints, such as primary key, foreign key, unique, not null, check, default, etc. Constraints are rules that enforce the integrity and validity of the data in the database tables.
- SQL supports various operators, such as arithmetic, comparison, logical, bitwise, set, etc. Operators are symbols that perform calculations or comparisons on the operands. Operators have a precedence order that determines the order of evaluation in an expression.
- SQL supports various functions, such as aggregate, scalar, string, numeric, date and time, conversion, etc. Functions are predefined or user-defined routines that perform a specific task and return a value. Functions can be used in various clauses and expressions in SQL statements.
- SQL supports various clauses, such as SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, OFFSET, etc. Clauses are keywords that specify the structure and logic of the SQL statements. Clauses have a specific order and syntax in SQL statements.
- SQL supports various expressions, such as arithmetic, conditional, case, null, etc. Expressions are combinations of literals, identifiers, operators, and functions that produce a value. Expressions can be used in various clauses and statements in SQL.
- SQL supports various statements, such as CREATE, ALTER, DROP, TRUNCATE, INSERT, UPDATE, DELETE, SELECT, JOIN, UNION, INTERSECT, EXCEPT, etc. Statements are keywords that perform a specific action on the database objects or data. Statements have a specific syntax and semantics in SQL.



### Transaction Control Commands

- Transaction control commands are used to manage the changes made by SQL statements in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a whole.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the statements in a transaction are executed successfully or none of them are executed at all.
- Consistency means that the database remains in a valid state before and after a transaction.
- Isolation means that the changes made by one transaction are not visible to other transactions until the transaction is committed.
- Durability means that the changes made by a committed transaction are permanent and not lost due to system failures.
- The following commands are used to control transactions in SQL:
  - **COMMIT** - This command is used to make a transaction permanent in a database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK** - This command is used to undo the changes made by a transaction. It restores the database to its state before the transaction started and ends the current transaction.
  - **SAVEPOINT** - This command is used to create points within a transaction to which the transaction can be rolled back partially. It allows dividing a transaction into smaller parts and undoing some changes without affecting the whole transaction.
  - **SET TRANSACTION** - This command is used to specify the characteristics of a transaction, such as its isolation level, name, or read-only status. It must be executed before any SQL statements in a transaction.
- SQL Server operates in the following transaction modes:
  - **Autocommit transactions** - Each individual statement is a transaction. It is committed automatically after it is executed. This is the default mode for SQL Server.
  - **Explicit transactions** - Each transaction is explicitly started with the **BEGIN TRANSACTION** statement and explicitly ended with a **COMMIT** or **ROLLBACK** statement. This mode gives more control over the transactions and their boundaries.
  - **Implicit transactions** - A transaction is implicitly started when the first SQL statement is executed after the **SET IMPLICIT_TRANSACTIONS ON** statement. The transaction is implicitly committed when the next **COMMIT**, **ROLLBACK**, or **SET IMPLICIT_TRANSACTIONS OFF** statement is executed. This mode is similar to explicit transactions, but it does not require the **BEGIN TRANSACTION** statement.
- A transaction can be explicitly executed as a distributed transaction by using **BEGIN DISTRIBUTED TRANSACTION**. A distributed transaction involves multiple servers or databases that are coordinated by the Microsoft Distributed Transaction Coordinator (MS DTC). This mode allows performing transactions across different systems or platforms.



## Unit 6 - PL/SQL

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that allows users to write procedural code in Oracle database.
- PL/SQL supports variables, constants, data types, operators, expressions, control structures, loops, arrays, cursors, exceptions, subprograms, packages, triggers, and object-oriented features.
- PL/SQL code is compiled and stored in the database as named objects, such as procedures, functions, packages, and triggers. These objects can be invoked from SQL statements or other PL/SQL blocks.
- PL/SQL code can also be embedded in SQL*Plus scripts, SQL Developer tools, or external applications that connect to Oracle database using APIs such as JDBC or ODBC.
- PL/SQL code can interact with SQL statements by using bind variables, placeholders, and dynamic SQL. PL/SQL code can also use SQL functions, operators, and pseudocolumns in expressions and conditions.
- PL/SQL code can improve the performance and security of database applications by reducing network traffic, enforcing business rules, and implementing access control.
- PL/SQL code can handle errors and exceptions by using predefined or user-defined exception handlers, RAISE statements, and PRAGMA directives.
- PL/SQL code can be debugged and tested by using tools such as PL/SQL Developer, SQL Developer, DBMS_DEBUG, DBMS_OUTPUT, and DBMS_TRACE packages.



### Introduction for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is a programming language that extends SQL (Structured Query Language) by adding procedural features such as variables, loops, conditional statements, and functions.
- PL/SQL is designed to work with Oracle Database, which is a relational database management system (RDBMS) that stores and manipulates data in tables and views.
- PL/SQL allows users to create and execute stored procedures, functions, triggers, and packages, which are collections of PL/SQL code that can be reused and shared by multiple applications.
- PL/SQL also supports object-oriented features such as object types, methods, inheritance, and polymorphism, which allow users to model complex data structures and behaviors in the database.
- PL/SQL can improve the performance and security of database applications by reducing the network traffic between the application and the database server, and by enforcing data integrity and business rules in the database layer.
- PL/SQL can also interact with other programming languages such as Java, C, and C++, and can use external libraries and web services to extend its functionality.



### Features of PL/SQL

PL/SQL is a procedural extension of SQL that allows developers to write efficient and compact code for manipulating data in a database. Some of the features of PL/SQL are:

- **Integration with SQL**: PL/SQL is tightly integrated with SQL, which means that it can use all the SQL data types, operators, functions, and commands. PL/SQL can also embed SQL statements within its code and use SQL cursors to process multiple rows of data.
- **Error checking**: PL/SQL offers extensive error checking, which means that it can detect and handle errors at compile time and run time. PL/SQL also provides predefined exceptions and user-defined exceptions to handle different types of errors.
- **Data types**: PL/SQL offers numerous data types, such as scalar, composite, reference, and large object (LOB) data types. Scalar data types include basic types like numbers, characters, booleans, and dates. Composite data types include collections, records, and tables. Reference data types include pointers to other data types. LOB data types include binary large objects (BLOBs) and character large objects (CLOBs).
- **Programming structures**: PL/SQL offers a variety of programming structures, such as variables, constants, operators, expressions, assignments, conditional statements, loops, cursors, exceptions, subprograms, and triggers. These structures allow developers to write modular and structured code that is easy to read and maintain.
- **Structured programming**: PL/SQL supports structured programming through functions and procedures, which are subprograms that can be reused and invoked from other subprograms or SQL statements. Functions and procedures can have parameters, local variables, and return values. They can also be grouped into packages, which are collections of related subprograms and variables.
- **Object-oriented programming**: PL/SQL supports object-oriented programming, which means that it can define and manipulate user-defined data types, called objects. Objects can have attributes, methods, constructors, and destructors. They can also inherit from other objects, called superclasses, and implement interfaces, which are contracts that specify the methods that an object must have.
- **Web development**: PL/SQL supports the development of web applications and server pages, which are dynamic web pages that can interact with a database. PL/SQL can be embedded in HTML, XML, or JSON documents, and can use the PL/SQL Web Toolkit to generate web content and handle HTTP requests and responses.



### Syntax and Constructs for the Notes of the Unit 6 - PL/SQL in the Subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that adds procedural features to the relational database language .
- PL/SQL is designed to work with Oracle Database, and allows users to create applications that manipulate data, handle errors, and perform complex calculations.
- PL/SQL is a block-structured language, which means that the basic unit of PL/SQL code is a block. A block consists of three sections: declaration, execution, and exception .
- The declaration section is optional and contains the definitions of constants, variables, cursors, exceptions, and other identifiers that can be used in the block .
- The execution section is mandatory and contains the executable statements that perform the logic of the block. At least one executable statement is required in this section .
- The exception section is optional and contains the handlers that deal with the errors or exceptions that may occur during the execution of the block .
- The end of the block is marked by the keyword END, followed by an optional block label and a semicolon. The block can be executed as a whole by using a slash (/) or the keyword EXECUTE .
- The syntax of a PL/SQL block is as follows:

```
[<<block_label>>]
DECLARE
   -- optional declarations
BEGIN
   -- mandatory executable statements
EXCEPTION
   -- optional exception handlers
END [block_label];
/
```

- PL/SQL blocks can be nested within each other, meaning that a block can contain another block as a part of its execution section. The inner block can access the identifiers declared in the outer block, but not vice versa .
- PL/SQL supports many constructs that are common in procedural languages, such as variables, constants, data types, operators, expressions, assignments, control structures, loops, cursors, subprograms, packages, triggers, and object types  .
- PL/SQL also integrates with SQL, allowing users to embed SQL statements within PL/SQL blocks, and use PL/SQL variables and expressions in SQL statements  .
- PL/SQL is a powerful and flexible language that can be used to create complex and robust applications that work with Oracle Database. It is also a highly structured and readable language that expresses the intent of the code clearly .



### SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is an extension of SQL that allows developers to write procedural code using SQL statements within its syntax .
- PL/SQL blocks are the basic units of PL/SQL programs, which can be nested within each other. A PL/SQL block consists of three sections: declaration, executable, and exception .
- Declaration section: This section is optional and declares variables, constants, cursors, and user-defined types that are used in the block.
- Executable section: This section is mandatory and contains the logic of the block, which can include SQL statements, assignments, loops, conditional statements, and calls to other PL/SQL blocks or subprograms.
- Exception section: This section is optional and handles any errors or exceptions that occur during the execution of the block.
- PL/SQL blocks can be anonymous or named. Anonymous blocks are not stored in the database and are executed once. Named blocks are stored in the database as subprograms, such as procedures, functions, triggers, or packages, and can be invoked multiple times .
- PL/SQL supports two types of dynamic SQL, which are SQL statements that are constructed and executed at run time. Dynamic SQL is useful when the SQL statement is not known in advance or depends on user input or other variables.
- Execute Immediate: This is a simple way of executing a single dynamic SQL statement, such as INSERT, UPDATE, DELETE, or CREATE. The syntax is:

```sql
EXECUTE IMMEDIATE dynamic_string [INTO {define_variable | record}] [USING [IN | OUT | IN OUT] bind_argument]...
```

- DBMS_SQL: This is a package that provides more control and flexibility over executing dynamic SQL statements, such as SELECT, that return multiple rows or columns. The process of using DBMS_SQL involves the following steps:

  - Open a cursor: A cursor is a pointer to a memory area that holds the result set of a SQL statement. The syntax is:

  ```sql
  cursor_variable := DBMS_SQL.OPEN_CURSOR;
  ```

  - Parse the SQL statement: This step checks the syntax and validity of the SQL statement and associates it with the cursor. The syntax is:

  ```sql
  DBMS_SQL.PARSE(cursor_variable, dynamic_string, DBMS_SQL.NATIVE);
  ```

  - Bind the variables: This step binds the values of the variables to the placeholders in the SQL statement. The syntax is:

  ```sql
  DBMS_SQL.BIND_VARIABLE(cursor_variable, placeholder, bind_variable);
  ```

  - Execute the SQL statement: This step executes the SQL statement and stores the result set in the cursor. The syntax is:

  ```sql
  rows_processed := DBMS_SQL.EXECUTE(cursor_variable);
  ```

  - Fetch the result set: This step retrieves the rows and columns from the cursor and assigns them to the variables. The syntax is:

  ```sql
  DBMS_SQL.DEFINE_COLUMN(cursor_variable, column_position, define_variable);
  DBMS_SQL.FETCH_ROWS(cursor_variable);
  DBMS_SQL.COLUMN_VALUE(cursor_variable, column_position, define_variable);
  ```

  - Close the cursor: This step releases the memory and resources associated with the cursor. The syntax is:

  ```sql
  DBMS_SQL.CLOSE_CURSOR(cursor_variable);
  ```



### DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity on the data stored in the database tables or views .
- DML statements can be executed from within any PL/SQL block of code, such as procedures, functions, triggers, packages, etc.
- The most common DML statements are INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert new rows into a table or a view.
- UPDATE statement is used to modify the values of existing rows in a table or a view.
- DELETE statement is used to remove existing rows from a table or a view.
- MERGE statement is used to combine the data from two tables into one, based on a matching condition.
- DML statements can be executed using the EXECUTE IMMEDIATE statement, which allows dynamic SQL execution in PL/SQL.
- DML statements can also be executed using the cursor FOR loop, which allows iterating over the result set of a query and performing DML operations on each row.
- DML statements can be combined with transaction control statements, such as COMMIT, ROLLBACK, and SAVEPOINT, to manage the changes made to the database.
- DML statements can be affected by the integrity constraints, triggers, and exceptions defined on the database objects.
- DML statements can return the number of rows affected by using the SQL%ROWCOUNT attribute of the implicit cursor.
- DML statements can also return the values of the columns of the affected rows by using the RETURNING clause.



### Cursors

- A cursor is a pointer to a result set, or the data that results from a query .
- Cursors let you fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.
- Cursors are useful when you need to perform row-by-row operations on the data, such as calculations, validations, or transformations.
- PL/SQL has two types of cursors: implicit cursors and explicit cursors.
- Implicit cursors are automatically created and managed by Oracle whenever an SQL statement such as SELECT INTO, INSERT, UPDATE, or DELETE is executed .
- Implicit cursors have attributes such as %FOUND, %ISOPEN, %NOTFOUND, and %ROWCOUNT that can be used to check the status and outcome of the SQL statement.
- Explicit cursors are defined and controlled by the programmer using the CURSOR keyword .
- Explicit cursors have four steps: declaration, opening, fetching, and closing .
- Declaration: The cursor is defined with a name and a query .
- Opening: The cursor is executed and the result set is populated .
- Fetching: The cursor is moved to the next row and the data is retrieved into variables or records .
- Closing: The cursor is closed and the memory is freed .
- Explicit cursors can have parameters that can be passed at the time of opening .
- Explicit cursors can also use the FOR loop to simplify the fetching process .
- Explicit cursors can be declared in the declaration section of a block, a subprogram, or a package.
- Explicit cursors can also be declared as REF CURSORs, which are cursor variables that can point to different queries at run time.



### Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database catalog .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to the procedure. The body contains the declarative, executable, and exception-handling parts of the procedure .
- A stored procedure can be created using the CREATE PROCEDURE statement, which has the following syntax :

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
[(parameter1 [mode] datatype [DEFAULT value], ...)]
IS
  --declarative part
BEGIN
  --executable part
EXCEPTION
  --exception-handling part
END [procedure_name];
```

- The OR REPLACE option allows to modify an existing procedure. The schema is the optional name of the schema that the procedure belongs to. The mode can be IN, OUT, or IN OUT, which specifies the parameter passing mechanism. The DEFAULT value is the optional default value for the parameter  .
- A stored procedure can be executed using the EXECUTE or EXEC command, which has the following syntax :

```sql
EXECUTE [schema.]procedure_name[(parameter1, ...)];
```

- A stored procedure can be dropped using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE [schema.]procedure_name;
```

- A stored procedure can also be dropped using SQL Developer, by right-clicking on the procedure name and choosing the Drop menu option.
- A stored procedure can have advantages such as modularity, reusability, maintainability, security, and performance .



### Stored Function in PL/SQL

- A stored function is a reusable program unit that can be defined and stored in the database as a schema object .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement, another PL/SQL block, or a PL/SQL expression .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must not have any side effects such as committing or rolling back transactions .
- The syntax for creating a stored function is as follows :

```sql
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
[declarative section]
BEGIN
[executable section]
END [function_name];
```

- The `CREATE OR REPLACE` option allows to overwrite an existing function with the same name .
- The `parameter_list` consists of zero or more parameters, each with a name, a data type, and an optional mode (IN, OUT, or IN OUT) .
- The `return_type` specifies the data type of the value that the function returns .
- The `declarative section` is optional and can contain declarations of variables, constants, cursors, or exceptions that are used in the function .
- The `executable section` is mandatory and contains the PL/SQL statements that implement the function logic .
- The `END` clause marks the end of the function body and can optionally include the function name for clarity .

- An example of a stored function that calculates the factorial of a given number is as follows:

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
END factorial;
```

- To invoke a stored function, use the function name followed by the argument list in parentheses .
- For example, to call the factorial function from a SQL statement, use the following syntax:

```sql
SELECT factorial(5) FROM dual;
```

- The output of the above statement is 120.



### Database Triggers

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
  - Instead of triggers: These triggers are executed instead of the triggering event, and can be used to override the default behavior of the event.
  - DML triggers: These triggers are executed in response to DML actions on a table or view.
  - DDL triggers: These triggers are executed in response to DDL actions on a database or server .
  - Logon triggers: These triggers are executed in response to logon events on a server.
- Triggers can have advantages and disadvantages depending on the use case and design :
  - Advantages: Triggers can provide data consistency, security, and integrity across multiple tables and databases; Triggers can automate common tasks and reduce the need for coding in applications; Triggers can enable auditing and logging of data changes; Triggers can enforce business rules and policies.
  - Disadvantages: Triggers can increase the complexity and maintenance of the database; Triggers can affect the performance and scalability of the database; Triggers can cause unexpected side effects and errors if not designed and tested properly; Triggers can create recursive or nested executions that can be hard to control and debug.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some indices for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System:

### Unit 6 - PL/SQL

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
- PL/SQL Cursors and Exceptions
  - What are cursors and how to use them?
  - Types of cursors (implicit, explicit, parameterized, ref)
  - Cursor attributes and operations
  - What are exceptions and how to handle them?
  - Types of exceptions (predefined, user-defined, unnamed)
  - Exception propagation and scope
- PL/SQL Subprograms
  - What are subprograms and how to create them?
  - Types of subprograms (procedures, functions, packages)
  - Subprogram parameters and modes (IN, OUT, IN OUT)
  - Subprogram overloading and nesting
  - Subprogram invocation and execution
- PL/SQL Triggers
  - What are triggers and how to create them?
  - Types of triggers (row, statement, DML, DDL, database, instead-of)
  - Trigger attributes and events
  - Trigger restrictions and guidelines
  - Trigger applications and examples
- PL/SQL Collections and Records
  - What are collections and records and how to use them?
  - Types of collections (associative arrays, nested tables, varrays)
  - Collection methods and operations
  - What are records and how to define them?
  - Record attributes and operations



## Unit 7 - Transaction Processing Concepts

- A transaction is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either executes all or none of its operations.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a transaction are permanent even in the case of failures.
- Transaction processing is the execution of transactions in a database system, which typically involves concurrency control, recovery, and security mechanisms.
- Concurrency control is the technique of ensuring that concurrent transactions do not violate the consistency of the database.
- Recovery is the technique of restoring the database to a consistent state after a failure.
- Security is the technique of protecting the database from unauthorized access and modification.



### Transaction concepts

- A **transaction** is an action or series of actions that are performed by a single user or application program, which reads or updates the contents of the database.
- A transaction can be defined as a **logical unit of work** on the database.
- A transaction generally represents **any change** in a database.
- Transactions in a database environment have two main purposes:
  - To provide reliable units of work that allow correct recovery from failures and keep a database consistent even in cases of system failure.
  - To provide isolation between programs accessing a database concurrently.
- A transaction has four properties, known as **ACID**:
  - **Atomicity**: The 'all or nothing' property. A transaction is an indivisible entity that is either performed in its entirety or not performed at all.
  - **Consistency**: A transaction must alter the database from one steady-state to another steady state. This means that the database must satisfy all the integrity constraints before and after the transaction.
  - **Isolation**: Transactions must execute in isolation from each other, as if they were executed serially. This means that the intermediate results of a transaction are not visible to other transactions, and vice versa.
  - **Durability**: The effects of a committed transaction must persist in the database even in the event of system failures. This means that the changes made by a transaction are permanent and cannot be undone.



### Properties of Transaction for the Notes of the Unit 7 - Transaction Processing Concepts in the Subject of Basics of Data Base Management System

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction has a beginning and an end.
- A transaction must satisfy the ACID properties, which are Atomicity, Consistency, Isolation, and Durability. 
- Atomicity means that a transaction is either completed in its entirety or not executed at all. If a transaction fails, the database is restored to its original state before the transaction started.  
- Consistency means that a transaction must preserve the integrity constraints of the database. A transaction can only bring the database from one valid state to another valid state.  
- Isolation means that a transaction must not interfere with other concurrent transactions. Each transaction should execute as if it is the only transaction in the system.  
- Durability means that the effects of a committed transaction are permanent and persist even in the case of system failures. The database must not lose any data due to power outages, crashes, or errors.  
- A transaction can be in one of the following states: active, partially committed, committed, failed, or aborted. 
- Active is the initial state of a transaction when it is executed. 
- Partially committed is the state of a transaction after it has executed its final statement, but before it has committed. 
- Committed is the state of a transaction after it has successfully completed and made its changes permanent in the database. 
- Failed is the state of a transaction when it cannot continue due to some error or violation of integrity constraints. 
- Aborted is the state of a transaction when it has been rolled back and the database is restored to its state before the transaction started. 
- A schedule is a sequence of operations from a set of concurrent transactions. 
- A schedule is serial if it executes the transactions one after another, without interleaving their operations. 
- A schedule is serializable if it is equivalent to some serial schedule, meaning that it produces the same final state of the database as the serial schedule. 
- A schedule is recoverable if it ensures that a transaction can only commit after all the transactions whose changes it has read have committed. 
- A schedule is cascadeless if it ensures that a transaction can only read the changes made by a committed transaction. 
- A schedule is strict if it ensures that a transaction can only read and write the data items that have not been accessed by any other transaction. 
- A schedule is conflict-serializable if it can be transformed into a serial schedule by swapping the order of non-conflicting operations. 
- A schedule is view-serializable if it is equivalent to a serial schedule in terms of the read and write operations on each data item. 
- A transaction management system is responsible for ensuring the ACID properties of transactions, by using various techniques such as locking, timestamping, logging, recovery, and concurrency control.  

: https://www.educba.com/transaction-property-in-dbms/
: https://www.guru99.com/dbms-transaction-management.html
: https://byjus.com/gate/transaction-in-dbms-notes/
: https://www.javatpoint.com/dbms-transaction-property
: https://www.w3schools.in/dbms/transaction
: https://www.geeksforgeeks.org/acid-properties-in-dbms/



### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to some serial schedule, where the transactions are executed one after the other without any interleaving of operations.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read-write, write-read, or write-write) on the same data item in a schedule must be ordered in the same way as in a serial schedule.
- View serializability is a weaker form of serializability that requires that any two schedules have the same initial and final state of the database, and that any read operation on a data item in a schedule must read the same value as in a serial schedule.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph or a precedence graph is a directed graph of the transactions in a schedule, where an edge from Ti to Tj indicates that Ti must precede Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its serialization graph is acyclic, meaning that it does not contain any cycles or loops.
- A schedule is view serializable if and only if it is conflict serializable or it can be transformed into a conflict serializable schedule by swapping non-conflicting operations.
- Testing of serializability using serialization graph or precedence graph is a polynomial-time algorithm, meaning that it can be done in a reasonable amount of time for a given schedule.



### Serializability of schedules

- Serializability is a property of a transaction schedule (history) that relates to the isolation property of a database transaction .
- Serializability of a schedule means equivalence (in the outcome, the database state, data values) to a serial schedule (i.e., sequential with no transaction overlap in time) with the same transactions .
- Serializability of schedules ensures that a non-serial schedule is equivalent to a serial schedule. It helps in maintaining the transactions to execute simultaneously without interleaving one another.
- Serializability is a way to check if the execution of two or more transactions are maintaining the database consistency or not.
- There are two methods widely used to check serializability: conflict equivalent and view equivalent .
- Conflict equivalent: Two schedules are conflict equivalent if they have the same set of transactions and the order of any two conflicting operations is the same in both schedules .
- View equivalent: Two schedules are view equivalent if they have the same set of transactions and the following three conditions hold for each data item in the database :
  - The same transaction reads the initial value of the data item in both schedules.
  - The same transaction writes the final value of the data item in both schedules.
  - The set of transactions that read the value of the data item written by a transaction is the same in both schedules.



### Conflict and View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions, which may lead to inconsistency or anomalies in the database.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be conflicting if they satisfy all the following conditions:
  - They belong to different transactions.
  - They operate on the same data item.
  - At least one of them is a write operation.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- The schedule S is not serial, as it interleaves operations from T1 and T2.
- The schedule S is conflict serializable, as it can be transformed into a serial schedule S' by swapping non-conflicting operations:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- The schedule S' is serial and equivalent to S in terms of the final state of the database.
- A conflict serializable schedule preserves the order of conflicting operations in the serial schedule.

#### View Serializability

- A schedule is view serializable if it is view equivalent to some serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item.
  - They have the same final write operations on each data item.
  - They have the same update operations on each data item by the same transaction.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
|     | R(A) |
|     | W(A) |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- The schedule S is not serial, as it interleaves operations from T1 and T2.
- The schedule S is view serializable, as it is view equivalent to a serial schedule S' as follows:

| T1 | T2 |
|----|----|
| R(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(A) |
|     | W(A) |
|     | R(B) |
|     | W(B) |

- The schedule S' is serial and equivalent to S in terms of the initial and final views of the database.
- A view serializable schedule may not preserve the order of conflicting operations in the serial schedule.

#### Difference between Conflict and View Serializability

- Conflict serializability is a stricter criterion than view serializability, as every conflict serializable schedule is also view serializable, but not vice versa.
- Conflict serializability can be checked by constructing a precedence graph of the transactions and testing for cycles, whereas view serializability requires testing for view equivalence with all possible serial schedules, which is computationally expensive.
- Conflict serializability ensures that the concurrent execution of transactions is equivalent to some serial order of the transactions, whereas view serializability ensures that the concurrent execution of transactions produces the same view of the database as some serial order of the transactions.



### Recoverability in Transaction Processing
- Recoverability is the property of a schedule that ensures that the database state is consistent after a transaction failure or system crash .
- A schedule is recoverable if no transaction commits before all the transactions whose changes it has read commit .
- A schedule is irrecoverable if some transaction commits after reading the changes made by another transaction that has not committed yet .
- Irrecoverable schedules can lead to inconsistency in the database state if the transaction that has not committed yet aborts or fails .
- Example of a recoverable schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(A) |
| W(A) |    |
|    | W(A) |
| C |    |
|    | C |

- Example of an irrecoverable schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(A) |
|    | W(A) |
|    | C |
| W(A) |    |
| A |    |

- There are different types of recoverable schedules, such as cascadeless schedules and strict schedules.
- A cascadeless schedule is a recoverable schedule in which no transaction reads a data item unless the transaction that last wrote it has committed.
- A strict schedule is a recoverable schedule in which no transaction reads or writes a data item unless the transaction that last wrote it has committed.
- Cascadeless and strict schedules prevent cascading aborts, which are a chain of aborts caused by the failure of one transaction.
- Example of a cascadeless schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| C |    |
|    | R(A) |
|    | W(A) |
|    | C |

- Example of a strict schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|    | R(A) |
|    | W(A) |
| C |    |
|    | C |

- Recoverability is an important concept in transaction processing systems, as it ensures the consistency and durability of the database state .
- Recoverability can be achieved by using various techniques, such as logging, checkpoints, shadow paging, and locking .



### Recovery from transaction failures

- Transaction failures are situations where a transaction cannot complete its execution due to various reasons, such as network failures, deadlock, or errors in application logic.
- Transaction failures can compromise the consistency and integrity of the database, as they may leave the database in an intermediate or inconsistent state.
- Recovery from transaction failures is the process of restoring the database to a consistent state after such failures, by undoing or redoing the effects of the failed transactions.
- Recovery from transaction failures is based on the following concepts:
  - Atomicity: A transaction is either executed in its entirety or not at all.
  - Durability: The effects of a committed transaction are permanent and survive any system failure.
  - Logging: A transaction log is a record of all the changes made by a transaction to the database. It contains information such as transaction ID, operation type, data item, old value, and new value.
  - Checkpoints: A checkpoint is a point in time when the database and the transaction log are synchronized, i.e., all the changes made by the committed transactions are written to the database. Checkpoints reduce the amount of work needed for recovery.
- There are two major techniques for recovery from non-catastrophic transaction failures:
  - Deferred update: This technique does not physically update the database on disk until a transaction has reached its commit point. It only records the changes in the transaction log. If a transaction fails before its commit point, no recovery action is needed, as the database is not affected. If a transaction commits, the recovery manager reads the transaction log and applies the changes to the database (redoing).
  - Immediate update: This technique allows the database to be updated on disk before a transaction reaches its commit point. However, it also records the changes in the transaction log. If a transaction fails before its commit point, the recovery manager reads the transaction log and restores the original values of the data items that were modified by the transaction (undoing). If a transaction commits, the recovery manager ensures that all the changes made by the transaction are written to the database (redoing).
- Recovery from catastrophic transaction failures is the process of restoring the database from a backup copy after a system failure that causes the loss of the entire database or a significant part of it.
- Recovery from catastrophic transaction failures is based on the following steps:
  - Restore a previous copy of the database from archival backup.
  - Apply the transaction log to the copy to reconstruct a more current state of the database by redoing the committed transaction operations up to the failure point.
  - Undo the effects of any uncommitted transactions that were in progress at the time of the failure.



### Two-phase commit protocol

- The two-phase commit protocol (2PC) is a type of atomic commitment protocol (ACP) that ensures the atomicity and consistency of distributed transactions.
- A distributed transaction is a transaction that involves multiple sites (such as databases or servers) that need to agree on whether to commit or abort the transaction.
- The two-phase commit protocol consists of two phases: the prepare phase and the commit phase .
- In the prepare phase, a coordinator (a site that initiates the transaction) sends a prepare message to all the participants (the sites that execute the transaction) and asks them to vote on whether they are ready to commit or not .
- Each participant responds with a vote message: either prepared (meaning ready to commit) or aborted (meaning not ready to commit)  .
- The coordinator collects all the votes and decides the outcome of the transaction based on the majority rule: if all the participants vote prepared, the outcome is commit; otherwise, the outcome is abort .
- In the commit phase, the coordinator sends the outcome to all the participants and asks them to either commit or abort the transaction accordingly .
- Each participant follows the coordinator's decision and sends an acknowledgement message to the coordinator  .
- The coordinator waits for all the acknowledgements and then completes the transaction  .
- The two-phase commit protocol ensures that either all the participants commit the transaction or none of them do, thus preserving the atomicity and consistency of the distributed system .
- However, the two-phase commit protocol also has some drawbacks, such as:
  - It is a blocking protocol, meaning that the failure of a single site or a message loss can block the progress of the transaction until the site or the message recovers .
  - It has a high latency, meaning that it takes a long time to complete the transaction, as it depends on the slowest site or the longest message delay .
  - It is not resilient to network partitions, meaning that it cannot handle the situation when the sites are divided into two or more groups that cannot communicate with each other .



### Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique used to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: A unique identifier for each transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data Item: The name of the data item affected by the operation.
  - Old Value: The value of the data item before the operation.
  - New Value: The value of the data item after the operation.
- A log record can also have a start or end marker to indicate the beginning or the end of a transaction  .
- For example, a log record for a transaction T1 that updates the city of a customer from Chennai to NCR can be written as:

  `<T1, Start>`  
  `<T1, City, Chennai, NCR>`  
  `<T1, Commit>`

- Log based recovery in DBMS can be classified into two types  :
  - Undo Logging: This type of logging ensures that the database is restored to its state before the failure by undoing the effects of the transactions that did not commit.
  - Redo Logging: This type of logging ensures that the database is restored to its state after the failure by redoing the effects of the transactions that did commit.
- The choice of logging type depends on the recovery algorithm used by the DBMS, such as immediate update, deferred update, checkpointing, or shadow paging  .
- Log based recovery in DBMS provides the following advantages  :
  - It preserves the ACID properties of transactions, such as atomicity, consistency, isolation, and durability.
  - It minimizes the data loss and inconsistency caused by failures or crashes.
  - It reduces the need for frequent backups and restores of the database.
  - It improves the performance and availability of the database.



### Checkpoints for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

- Define the concept of a transaction as a logical unit of database processing that consists of a set of operations on data objects .
- Explain the properties of transactions, namely atomicity, consistency, isolation, and durability (ACID) and why they are important for ensuring database integrity .
- Describe the types of failures that can occur during transaction execution and how they affect the database state.
- Discuss the methods for handling failures and ensuring recovery, such as logging, checkpoints, undo and redo operations, and shadow paging.
- Understand the concept of concurrency control and why it is needed to prevent conflicts and anomalies among concurrent transactions.
- Compare the advantages and disadvantages of different concurrency control techniques, such as locking, timestamp ordering, validation, and multiversion concurrency control.
- Identify the types of locks and their compatibility, such as shared, exclusive, and intention locks.
- Explain the concept of serializability and how it can be used to determine the correctness of concurrent transaction execution.
- Apply the concepts of transaction processing to design and implement database applications that require high availability, reliability, and performance .



### Deadlock Handling

- A deadlock is a situation in which two or more transactions are waiting indefinitely for one another to release locks on database resources.
- A deadlock can be represented by a cycle in the wait-for graph, which is a directed graph where the vertices are transactions and the edges are waits for data items.
- Deadlocks are undesirable because they cause the system to waste resources and time, and may lead to inconsistent database states.
- Deadlocks can be handled by three main methods: deadlock prevention, deadlock avoidance, and deadlock detection and recovery.
- Deadlock prevention is a technique that ensures that deadlocks never occur by imposing some constraints on how transactions acquire and release locks. For example, a transaction may be required to lock all the data items it needs before it starts, or to release all the locks it holds before it requests a new lock. Deadlock prevention may reduce concurrency and performance, as transactions may have to wait longer for locks or hold locks longer than necessary.
- Deadlock avoidance is a technique that allows transactions to proceed without causing deadlocks, by using some information about the resources they need and the current state of the system. For example, a transaction may be assigned a timestamp and be allowed to lock a data item only if it does not conflict with the timestamp order of other transactions, or the system may use a wait-for graph to check if granting a lock request would create a cycle. Deadlock avoidance may incur some overhead in maintaining and checking the information needed to avoid deadlocks.
- Deadlock detection and recovery is a technique that allows the system to detect when deadlocks have occurred and take some actions to resolve them. For example, the system may periodically run a deadlock detection algorithm that examines the wait-for graph and identifies any cycles, or the system may use some event-driven mechanisms such as timeouts or alerts to trigger the detection. Once a deadlock is detected, the system may choose a victim transaction to abort and roll back, and release its locks, or the system may ask the user or the application to intervene and resolve the deadlock. Deadlock detection and recovery may cause some transactions to be wasted and restarted, and may affect the consistency and durability of the database.



## Unit 8 - Concurrency Control Techniques

Concurrency control techniques are methods of managing the simultaneous execution of transactions in a shared database. They aim to preserve the database consistency, enforce the isolation of different transactions, and resolve the conflicts that occur due to the read-write operations of transactions .

The need for concurrency control arises because multiple transactions may access and modify the same data items concurrently, which may lead to inconsistency, lost updates, uncommitted dependencies, or incorrect summary.

Some of the common concurrency control techniques are:

- **Two-phase locking protocol**: This technique uses locks to secure the permission to read or write a data item. A transaction goes through two phases: a locking or growing phase, where it acquires locks on data items, and an unlocking or shrinking phase, where it releases locks on data items. The transaction cannot request any new locks after it releases any lock. This protocol ensures serializability, but may cause deadlocks or starvation .
- **Timestamp ordering protocol**: This technique assigns a unique timestamp to each transaction based on its arrival time. The timestamp determines the order of execution of the transactions. A transaction can read or write a data item only if its timestamp is compatible with the read and write timestamps of the data item. This protocol avoids deadlocks, but may cause aborts or cascading aborts.
- **Multi-version concurrency control**: This technique maintains multiple versions of each data item, each with a different timestamp. A transaction can read the version of a data item that is compatible with its timestamp, without locking or waiting. A transaction can write a new version of a data item only if its timestamp is greater than the write timestamp of the data item. This protocol allows more concurrency and reduces aborts, but requires more storage space and overhead.
- **Validation concurrency control**: This technique divides the execution of a transaction into three phases: a read phase, where the transaction reads data items without locking, a validation phase, where the transaction checks for conflicts with other transactions, and a write phase, where the transaction writes the modified data items. This protocol avoids locking and deadlocks, but may cause aborts or delays.



### Concurrency control

- Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system.
- Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases .
- Concurrency control is a procedure in DBMS which helps us for the management of two simultaneous processes to execute without conflicts between each other, these conflicts occur in multi user systems.
- Concurrency control refers to the various techniques that are used to preserve the integrity of the database when multiple users are updating rows at the same time.
- Incorrect concurrency can lead to problems such as dirty reads, phantom reads, and non-repeatable reads.

### Concurrency control techniques

- There are two main types of concurrency control techniques: pessimistic and optimistic .
- Pessimistic concurrency control assumes that conflicts are likely to happen and uses locks to prevent them. Locks are mechanisms that restrict access to data items by concurrent transactions .
- Optimistic concurrency control assumes that conflicts are rare and uses timestamps or versions to detect them. Timestamps or versions are identifiers that indicate the order or state of data items by concurrent transactions .
- Some examples of pessimistic concurrency control techniques are two-phase locking (2PL), strict two-phase locking (S2PL), and tree locking .
- Some examples of optimistic concurrency control techniques are timestamp ordering (TO), multiversion concurrency control (MVCC), and validation .



### Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the integrity of the database is maintained. One of the main challenges of concurrency control is to prevent conflicts that may arise when multiple transactions try to read or write the same data item at the same time.

Locking is one of the most common techniques for concurrency control. Locking is the mechanism of granting or denying access to a data item based on the state of a lock variable associated with it. A lock can be either shared or exclusive, depending on the type of access required by a transaction. A shared lock allows multiple transactions to read the same data item, but prevents any transaction from writing it. An exclusive lock allows only one transaction to read or write the data item, and blocks any other transaction from accessing it.

There are different types of locking techniques that can be used for concurrency control, such as:

- Two-phase locking protocol: This is a protocol that ensures that a transaction acquires all the locks it needs before releasing any of them. The protocol consists of two phases: a growing phase, where the transaction can only obtain new locks, and a shrinking phase, where the transaction can only release locks. The protocol guarantees serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.

- Timestamp ordering protocol: This is a protocol that assigns a unique timestamp to each transaction, and uses the timestamps to order the access to data items. The protocol ensures that a transaction can only read or write a data item if its timestamp is greater than the timestamp of any previous transaction that accessed the same data item. The protocol also guarantees serializability, but avoids the overhead of locking and unlocking data items.

- Multi-version concurrency control: This is a technique that maintains multiple versions of each data item, and allows transactions to access the version that is appropriate for their timestamp. The technique avoids locking and ensures that transactions do not block each other, but requires more storage space and complexity to manage the versions.

- Validation concurrency control: This is a technique that allows transactions to execute without any locking or ordering, but validates them at the end to check if they are serializable. The technique divides the execution of a transaction into three phases: a read phase, where the transaction reads data items, a validation phase, where the transaction checks if it is serializable, and a write phase, where the transaction writes data items. The technique reduces the blocking and waiting of transactions, but may incur more aborts and restarts if the validation fails.

- Multiple granularity: This is a technique that allows transactions to lock data items at different levels of granularity, such as a record, a page, a file, or a table. The technique reduces the number of locks required by a transaction, and allows more concurrency among transactions that access different parts of the data. The technique requires a hierarchical locking scheme, where a transaction must lock a higher-level data item before locking a lower-level data item within it.



### Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability   .
- A timestamp is a unique identifier that represents the creation time of a transaction or a logical counter that increments after each transaction   .
- Each transaction has two timestamps: a start timestamp (TS) that indicates when the transaction started, and a commit timestamp (CT) that indicates when the transaction committed.
- Each data item also has two timestamps: a read timestamp (RT) that indicates the timestamp of the last transaction that read the data item, and a write timestamp (WT) that indicates the timestamp of the last transaction that wrote the data item.
- The basic rules of timestamp ordering protocol are   :
  - If a transaction T wants to read a data item X, it is allowed to do so only if TS(T) >= WT(X), meaning that T started after the last transaction that wrote X. Otherwise, T is aborted and restarted with a new timestamp.
  - If a transaction T wants to write a data item X, it is allowed to do so only if TS(T) >= RT(X) and TS(T) >= WT(X), meaning that T started after the last transaction that read or wrote X. Otherwise, T is aborted and restarted with a new timestamp.
- The advantages of timestamp ordering protocol are   :
  - It avoids deadlock, as no transaction ever waits for another transaction to release a lock.
  - It ensures serializability, as the transactions are executed in the order of their timestamps.
  - It is easy to implement, as no lock manager or deadlock detection is needed.
- The disadvantages of timestamp ordering protocol are   :
  - It may cause starvation, as a transaction may be repeatedly aborted and restarted if it conflicts with other transactions with higher timestamps.
  - It may cause cascading aborts, as an aborted transaction may invalidate the results of other transactions that depend on it.
  - It may not reflect the actual order of events, as the timestamps may not correspond to the real-time occurrence of the transactions.



### Validation Based Protocol for Concurrency Control

- Validation based protocol is also called optimistic concurrency control technique  .
- It is used to avoid concurrency problems in transactions by validating them before committing them to the database  .
- It works on the assumption that very few transactions interfere with each other, so there is no need to check for conflicts while the transaction is executing .
- It divides the transaction into three phases: read phase, validation phase, and write phase  .
- In the read phase, the transaction reads the data values from the database and makes updates to the local copies, not the actual database .
- In the validation phase, the transaction checks if it can be committed without violating the serializability order of the transactions  .
- In the write phase, the transaction writes the updated values to the database if it passes the validation, otherwise it is aborted and restarted  .
- The validation phase uses timestamps to determine the order of the transactions and to detect conflicts  .
- There are different types of timestamps associated with each transaction, such as start timestamp, validation timestamp, and finish timestamp.
- The start timestamp is the time when the transaction begins its execution.
- The validation timestamp is the time when the transaction enters the validation phase.
- The finish timestamp is the time when the transaction completes its execution.
- The validation phase applies different rules to check if the transaction can be committed, such as basic timestamp ordering, Thomas write rule, and multiversion timestamp ordering .
- Basic timestamp ordering ensures that the transactions are executed in the order of their start timestamps and rejects any conflicting operations .
- Thomas write rule allows some conflicting write operations to be ignored if they do not affect the final outcome of the transactions .
- Multiversion timestamp ordering maintains multiple versions of the data items and assigns them different timestamps to allow more concurrency among the transactions .
- Validation based protocol has the advantage of not requiring locking or blocking of the data items, which reduces the overhead and the possibility of deadlock .
- It also has the advantage of allowing more concurrency among the transactions, as they can execute without interference until the validation phase .
- However, it has the disadvantage of requiring more memory space to store the local copies and the timestamps of the transactions .
- It also has the disadvantage of wasting some computation time if the transactions are aborted and restarted after the validation phase .
- It is suitable for applications where the conflict rate is low and the transactions are short-lived .



### Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows the multi-granularity compatibility function, which defines the compatibility of different lock modes on different levels of the hierarchy .
- The lock modes are: Shared (S), Exclusive (X), Intention Shared (IS), Intention Exclusive (IX), and Shared with Intention Exclusive (SIX) .
- The compatibility function is shown in the following table :

|     | S  | X  | IS | IX | SIX |
|-----|----|----|----|----|-----|
| S   | Y  | N  | Y  | N  | N   |
| X   | N  | N  | N  | N  | N   |
| IS  | Y  | N  | Y  | Y  | Y   |
| IX  | N  | N  | Y  | Y  | N   |
| SIX | N  | N  | Y  | N  | N   |

- The multi-granularity locking protocol follows these rules :
  - Lock the root of the tree first, in any mode.
  - Node Q can be locked by Ti in S or IS only if parent(Q) is locked by Ti in IX or IS.
  - Node Q can be locked by Ti in X, SIX, IX only if parent(Q) is locked by Ti in IX or SIX.
  - Ti is two-phase, meaning it acquires all the locks before releasing any lock.
  - Ti can unlock node Q only if none of Q's descendants are locked by Ti.
- An example of a multi-granularity locking hierarchy is shown in the following figure:

Figure 1: An example of a multi-granularity locking hierarchy

- In this figure, the database is divided into four levels: database (D), file (F), page (P), and record (R). Each level has a different granularity and can be locked by different transactions in different modes. For example, T1 has locked the entire database in IS mode, meaning it intends to read some of the files. T2 has locked file F1 in IX mode, meaning it intends to update some of the pages in F1. T3 has locked page P1 in S mode, meaning it wants to read P1. T4 has locked record R1 in X mode, meaning it wants to update R1. T5 has locked record R2 in S mode, meaning it wants to read R2. These locks are compatible according to the compatibility function and the protocol rules.



### Multi-version schemes for concurrency control

- Multi-version schemes are a type of concurrency control method that allow concurrent access to the database without locking the data.
- Multi-version schemes create and maintain different versions of data items for each write operation performed by a transaction.
- Multi-version schemes allow read operations to access the most recent committed version of a data item, without waiting for the write operations to finish.
- Multi-version schemes improve the performance and concurrency of database applications in a multiuser environment, by reducing the conflicts and delays between read and write operations.
- Multi-version schemes can be implemented in different ways, such as timestamp ordering, multiversion two-phase locking, snapshot isolation, etc.
- Multi-version schemes have some advantages and disadvantages, such as:

  - Advantages:
    - No read locks are required, which reduces the locking overhead and the possibility of deadlocks.
    - Read operations are not blocked by write operations, which improves the response time and throughput of the system.
    - Write operations can be performed on a copy of the data item, which reduces the contention and interference with other transactions.
    - Data consistency and serializability are ensured by using appropriate validation or conflict resolution techniques.
  - Disadvantages:
    - Multiple versions of data items need to be stored and managed, which increases the storage space and the complexity of the system.
    - Write operations may need to abort and restart if they conflict with other transactions, which reduces the availability and efficiency of the system.
    - Concurrency anomalies, such as phantom reads, may occur if the isolation level is not set properly.
    - Garbage collection and version management may incur additional overhead and performance degradation.



### Recovery with Concurrent Transaction

- Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions executing simultaneously.
- Recovery with concurrent transaction is necessary to ensure the ACID properties of transactions, especially atomicity and durability.
- Recovery with concurrent transaction can be done in the following four ways:
  - Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if locking is used, then the recovery scheme can use the lock table to identify the transactions that were active at the time of failure and undo their effects. If timestamp ordering is used, then the recovery scheme can use the timestamps to order the transactions and redo their effects.
  - Transaction rollback: In this scheme, the recovery scheme can undo the effects of a transaction that has failed or aborted by using the log records. The recovery scheme can use the undo operation to restore the previous values of the data items that were modified by the transaction. The recovery scheme can also use the redo operation to reapply the changes of the transaction that were lost due to failure.
  - Checkpoints: In this scheme, the recovery scheme can reduce the amount of work that needs to be done after a failure by periodically taking a snapshot of the database and the log. A checkpoint is a point in time when the database and the log are synchronized and consistent. The recovery scheme can use the checkpoint to determine the starting point of the recovery process and ignore the log records that were written before the checkpoint.
  - Restart recovery: In this scheme, the recovery scheme can use a combination of undo and redo operations to restore the database to a consistent state after a failure. The recovery scheme can use the log records to identify the transactions that were committed, aborted, or active at the time of failure. The recovery scheme can then undo the effects of the aborted and active transactions and redo the effects of the committed transactions. The recovery scheme can also use the checkpoints to optimize the recovery process and avoid unnecessary undo and redo operations.



## Unit 9 - Database Security

- Database security is the processes, tools, and controls that secure and protect databases against accidental and intentional threats.
- The objective of database security is to secure sensitive data and maintain the confidentiality, integrity, and availability of the database.
- Database security must address and protect the following:
  - Data at rest: Data that is stored in the database or backup files.
  - Data in transit: Data that is transferred between the database and the application or between different databases.
  - Data in use: Data that is processed by the database or the application.
  - Database system: The software and hardware components that run the database, such as the database server, the operating system, the network, and the storage devices.
  - Database users: The people or applications that access the database, such as administrators, developers, analysts, or customers.
- Database security can be implemented using various methods, such as   :
  - Physical security: Ensuring that the database server and the storage devices are located in a secure and controlled environment, and that unauthorized access is prevented.
  - Administrative and network access controls: Restricting the access to the database system and the network using authentication, authorization, and encryption mechanisms, and enforcing the principle of least privilege and separation of duties.
  - Database encryption and key management: Encrypting the data at rest and in transit using strong encryption algorithms and keys, and managing the keys securely using a centralized key management system or a hardware security module.
  - Database auditing and monitoring: Tracking and recording the activities and events that occur in the database system, such as user logins, queries, changes, errors, or anomalies, and analyzing the audit logs for detecting and responding to suspicious or malicious behavior.
  - Database backup and recovery: Creating and maintaining copies of the database and the transaction logs, and restoring the database in case of data loss or corruption due to hardware failure, human error, or cyberattack.
  - Database patching and hardening: Applying the latest security updates and patches to the database system and the operating system, and removing or disabling any unnecessary or vulnerable features, services, or accounts.
  - Database firewall and intrusion prevention: Blocking or filtering the network traffic to and from the database system, and preventing or mitigating the impact of common attacks, such as SQL injection, denial-of-service, or ransomware.
  - Database masking and anonymization: Replacing or obfuscating the sensitive data in the database or the copies of the database, such as for testing or development purposes, using techniques such as substitution, shuffling, or generalization, and ensuring that the masked data cannot be re-identified or linked to the original data.



### Types of security for the notes of the Unit 9 - Database Security in the subject of Basics of Data Base Management System

Database security refers to the process of protecting and safeguarding the database from unauthorized access or cyber-attacks. There are different types of database security that should be implemented in your business, such as :

- **Authentication**: Database authentication is the type of database security that verifies the user's login credentials which are stored in the database. If the user's login credentials match in the database, then the user can access the database. Authentication can be done by using passwords, biometrics, tokens, or certificates.
- **Database Encryption**: Database encryption is the type of database security that encrypts the data stored in the database, so that only authorized users can decrypt and read the data. Encryption can be done at the column level, table level, or database level, using symmetric or asymmetric keys, or hashing algorithms.
- **Backup Database**: Backup database is the type of database security that creates a copy of the database and stores it in a safe location, so that it can be restored in case of data loss, corruption, or disaster. Backup database can be done by using full backup, incremental backup, or differential backup methods, and can be stored on-premises, off-premises, or in the cloud.
- **Physical Security**: Physical security is the type of database security that protects the database server from physical damage, theft, or sabotage. Physical security can be done by using locks, alarms, cameras, guards, or firewalls, and by placing the database server in a secure room, cabinet, or rack.
- **Application Security**: Application security is the type of database security that protects the database from malicious or erroneous applications that can compromise the data integrity, confidentiality, or availability. Application security can be done by using input validation, output sanitization, parameterized queries, stored procedures, or code reviews, and by following the principle of least privilege, separation of duties, and defense in depth.
- **Access Control**: Access control is the type of database security that controls who can access what data and how they can access it, based on their roles, permissions, and privileges. Access control can be done by using discretionary access control (DAC), mandatory access control (MAC), or role-based access control (RBAC) models, and by implementing audit trails, logging, or monitoring mechanisms.
- **Web Application Firewall**: Web application firewall is the type of database security that protects the database from web-based attacks, such as SQL/NoSQL injection, cross-site scripting, or buffer overflow. Web application firewall can be done by using signature-based, anomaly-based, or hybrid-based detection methods, and by blocking, alerting, or logging the malicious requests.



### System Failure

- A system failure is an event that causes the database to stop functioning normally and may result in data loss, corruption, or unauthorized access .
- System failures can be caused by various factors, such as hardware malfunctions, power outages, network disruptions, software bugs, human errors, malicious attacks, natural disasters, etc .
- System failures can affect the database security in terms of confidentiality, integrity, and availability of the data .
- Confidentiality is the protection of data from unauthorized disclosure or access . A system failure can compromise confidentiality if it exposes sensitive data to unauthorized users or allows unauthorized modifications to the data .
- Integrity is the protection of data from unauthorized or accidental modification or deletion . A system failure can compromise integrity if it causes data corruption, inconsistency, or loss .
- Availability is the protection of data from unauthorized or accidental denial of access or use . A system failure can compromise availability if it prevents authorized users from accessing or using the data or the database system .
- To prevent or mitigate the impact of system failures on database security, some best practices include   :
  - Implementing backup and recovery procedures to restore the database to a consistent state after a failure .
  - Applying encryption and authentication techniques to protect the data from unauthorized access or modification .
  - Applying patches and updates to fix software vulnerabilities and bugs .
  - Monitoring and auditing the database activity and performance to detect and respond to anomalies or threats .
  - Implementing redundancy and load balancing techniques to ensure the availability and reliability of the database system .

