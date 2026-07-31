

## Unit 1 - Introduction

- In this unit, you will learn about the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be divided into two main branches: symbolic AI and sub-symbolic AI.
  - Symbolic AI uses symbols and rules to represent and manipulate knowledge, such as logic, ontologies, and expert systems.
  - Sub-symbolic AI uses numerical and statistical methods to model and learn from data, such as neural networks, evolutionary algorithms, and reinforcement learning.
- AI can also be classified into different types based on the level of intelligence and the domain of application, such as narrow AI, general AI, and super AI.
  - Narrow AI is the type of AI that can perform specific tasks well, but cannot generalize to other tasks or domains, such as face recognition, speech recognition, and chess playing.
  - General AI is the type of AI that can perform any intellectual task that a human can, and can transfer knowledge and skills across domains, such as natural language understanding, common sense reasoning, and creativity.
  - Super AI is the type of AI that can surpass human intelligence and capabilities in all domains, and can potentially create and control other AI systems, such as artificial superintelligence, artificial god, and artificial singularity.
- AI can have various impacts and implications on society, economy, ethics, and humanity, both positive and negative, such as automation, innovation, empowerment, enhancement, displacement, inequality, bias, responsibility, and existential risk.



### An overview of database management system

- A database management system (DBMS) is a software system that manages the creation, storage, manipulation, and retrieval of data in a database.
- A database is a collection of related data that is organized in a way that facilitates efficient access, modification, and analysis.
- A DBMS serves as an interface between the end users or applications and the database, allowing them to perform various operations on the data, such as insertion, deletion, update, query, and analysis .
- A DBMS also provides features such as data security, integrity, backup, recovery, concurrency, and performance tuning.
- A DBMS can be classified into different types based on the data model, such as relational, hierarchical, network, object-oriented, and document-oriented.
- A DBMS can also be classified into different types based on the architecture, such as centralized, distributed, client-server, and cloud-based.
- A DBMS can support different languages for defining, manipulating, and querying data, such as SQL, QBE, Datalog, and XQuery.
- A DBMS can be used for various applications, such as banking, e-commerce, social media, health care, education, and research.



### Database System vs File System

- A database system is a software that manages the storage, retrieval, and manipulation of data in a structured and organized way. A file system is a software that manages the storage, retrieval, and manipulation of data in a hierarchical and unstructured way.
- A database system supports multiple users, concurrency control, security, integrity, backup and recovery, and query languages. A file system supports single or limited users, basic file operations, access control, and file naming.
- A database system stores data in tables, which consist of rows and columns. Each table has a unique name and a set of attributes that define the properties of the data. A file system stores data in files, which consist of bytes and characters. Each file has a unique name and a path that defines its location in the directory structure.
- A database system provides data independence, which means that the logical and physical structure of the data can be changed without affecting the applications that use the data. A file system provides data dependence, which means that the logical and physical structure of the data are tightly coupled and any change in the data affects the applications that use the data.
- A database system reduces data redundancy, which means that the same data is not stored in multiple places. A file system increases data redundancy, which means that the same data may be stored in multiple places.
- A database system ensures data consistency, which means that the data is always in a valid and coherent state. A file system may cause data inconsistency, which means that the data may be in an invalid or incoherent state due to errors or conflicts.
- A database system facilitates data sharing, which means that the data can be accessed and modified by multiple users and applications. A file system limits data sharing, which means that the data can be accessed and modified by single or limited users and applications.



### Database System Concepts and Architecture

- A database system is a software package that allows users to store, manipulate, and access data in an organized and efficient way.
- A database system consists of several components, such as:
  - The database, which is a collection of data organized according to a logical schema or model.
  - The database management system (DBMS), which is the software that provides the functionality for creating, maintaining, and querying the database.
  - The database applications, which are the programs that use the DBMS to interact with the database and perform various tasks, such as data entry, analysis, reporting, etc.
  - The database users, who are the people or entities that use the database applications to access the database and perform their tasks.
- A database system can have different architectures, depending on how the components are distributed and communicated across different machines or networks.
  - A centralized database system is one where the database, the DBMS, and the database applications are all located on a single machine or server. This architecture is simple and easy to manage, but it has limitations in terms of scalability, performance, and reliability.
  - A client-server database system is one where the database and the DBMS are located on a server machine, and the database applications are located on client machines that communicate with the server through a network. This architecture allows for better scalability, performance, and reliability, but it also introduces more complexity and overhead in terms of network communication and security.
  - A distributed database system is one where the database is partitioned or replicated across multiple machines or servers, and the DBMS and the database applications are also distributed accordingly. This architecture allows for even higher scalability, performance, and reliability, but it also introduces more challenges in terms of data consistency, concurrency control, and fault tolerance.



### Views of Data – Levels of Abstraction

- Views of data are the different ways of representing the data in a database system.
- Views of data help to achieve data abstraction, which is the process of hiding the details of how data is stored and manipulated from the users and applications.
- Data abstraction also supports data independence, which is the ability to change the data at one level without affecting the data at higher levels.
- There are three levels of data abstraction in a database system: physical, logical, and view level.

#### Physical Level
- The physical level is the lowest level of data abstraction. It describes how the data is actually stored in the storage devices and the access methods used to retrieve and update the data.
- The physical level is also called the internal level or the implementation level.
- The physical level is concerned with the data structures, file organizations, indexes, hashing, compression, encryption, and other physical aspects of data storage and access.
- The physical level is usually hidden from the users and applications, and only the database administrator (DBA) can access and modify it.
- The physical level is defined by the physical schema, which is the description of the physical organization and access methods of the data.

#### Logical Level
- The logical level is the middle level of data abstraction. It describes what data is stored in the database and the relationships among the data.
- The logical level is also called the conceptual level or the data model level.
- The logical level is independent of the physical level, meaning that the logical structure and meaning of the data do not depend on how the data is physically stored and accessed.
- The logical level is the level that most users and applications interact with, as it provides a logical and meaningful view of the data.
- The logical level is defined by the logical schema, which is the description of the data and the data relationships in terms of a data model, such as the entity-relationship (ER) model, the relational model, or the object-oriented model.

#### View Level
- The view level is the highest level of data abstraction. It describes how the data is seen by different users and applications, according to their needs and preferences.
- The view level is also called the external level or the user level.
- The view level is derived from the logical level, meaning that the views are subsets or transformations of the data and the data relationships defined at the logical level.
- The view level can have multiple views, each tailored for a specific user group or application. For example, a view can show only a part of the data, hide some attributes, combine data from different tables, or perform some calculations on the data.
- The view level is defined by the view schema, which is the description of a view in terms of a data model, such as the relational model or the object-oriented model.



### Data Models for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- A data model is a type of data model that determines the logical structure of a database. It fundamentally determines in which manner data can be stored, organized and manipulated.
- Data models are fundamental entities to introduce abstraction in a DBMS. Data models define how data is connected to each other and how they are processed and stored inside the system.
- Data modeling is the process of developing data model for the data to be stored in a Database. Data Models ensure consistency in naming conventions, default values, semantics, security while ensuring quality of the data.
- There are different types of data models, such as:
  - Hierarchical data model: This type of model represents one-to-many relationships in a treelike format. In this type of model, each record has only one parent record and zero or more child records.
  - Relational data model: This type of model designs the data in the form of rows and columns within a table. It uses a set of tables to show the data and the relationships among those data. Each table has a unique primary key and each column has a unique name.
  - Entity-relationship data model: This type of model is the logical representation of data as objects and relationships among them. It uses entities, attributes and relationships to describe the data. An entity is a real-world object that can be identified by its attributes. A relationship is an association between two or more entities.
  - Object-based data model: This type of model is an extension of the ER model with notions of functions, encapsulation, and object identity, as well. It uses objects, classes, inheritance, polymorphism and methods to model the data. An object is an instance of a class that has attributes and methods. A class is a collection of objects that share the same structure and behavior.
  - Dimensional data model: This type of model is used for data analysis and reporting. It uses facts, dimensions and measures to model the data. A fact is a numerical value that represents a business event or transaction. A dimension is a descriptive attribute that provides context to the fact. A measure is a calculation or aggregation of facts.
  - Graph data model: This type of model is used for modeling complex and interconnected data. It uses nodes, edges and properties to model the data. A node is an entity that has a unique identifier and a set of properties. An edge is a relationship that connects two nodes and has a direction and a label. A property is a key-value pair that describes a node or an edge.



### Schema and Instances for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- A database is a collection of organized data that can be stored and managed in multiple databases using a software program called a database management system (DBMS)  .
- A database schema is an abstract design that represents the storage of data in a database. It describes both the organization of data and the relationships between tables in a given database  .
- A database schema is considered the "blueprint" of a database, which defines the structure, constraints, and operations that can be performed on the data  .
- A database schema is usually specified using a data definition language (DDL), which is a set of commands that define the tables, columns, data types, keys, indexes, and other elements of the schema  .
- A database instance is a sample of data from a database at a single moment in time. It is the data stored in a database that conforms to the schema  .
- A database instance can change over time as data is inserted, updated, deleted, or modified by the users or applications that access the database  .
- A database instance is usually specified using a data manipulation language (DML), which is a set of commands that manipulate the data in the database, such as SELECT, INSERT, UPDATE, and DELETE  .
- The main difference between schema and instance is that schema is a structural view of the database, while the instance is the data stored in a database at a particular moment of time  .
- The schema is the initial state of the database where the database is designed at first, while the instance is a state when data is loaded into the database or when any change is acquired by the corresponding database .
- The schema is fixed and does not change frequently, while the instance is dynamic and changes constantly  .
- The schema is independent of the physical storage of the data, while the instance is dependent on the physical storage of the data  .
- The schema can be represented by a diagram or a text, while the instance can be represented by a table or a record  .

: https://pediaa.com/what-is-the-difference-between-schema-and-instance/

: https://techdifferences.com/difference-between-schema-and-instance.html

: https://www.ibm.com/topics/database-schema

: https://www.geeksforgeeks.org/difference-between-schema-and-instance-in-dbms/

: https://www.educative.io/blog/what-are-database-schemas-examples



### Data Independence

Data independence is the property of a database management system (DBMS) that allows the database schema to be changed without affecting the user applications that access the data. Data independence helps to maintain the consistency and integrity of the data, and to reduce the complexity and cost of developing and maintaining the applications.

Data independence is of two types:

- **Physical data independence**: This is the ability to modify the physical schema of the database without affecting the logical schema or the external schema. The physical schema defines how the data is stored, organized, and accessed on the physical storage devices. Examples of physical schema changes are adding or removing indexes, changing the file structure or storage method, or altering the compression or encryption techniques. Physical data independence is present in most databases and file environments, as the hardware details and storage methods are hidden from the users.  

- **Logical data independence**: This is the ability to modify the logical schema of the database without affecting the external schema or the user applications. The logical schema defines the structure and relationships of the data, such as tables, columns, keys, and constraints. Examples of logical schema changes are adding or removing tables, columns, or constraints, changing the data type or domain of a column, or altering the primary key or foreign key of a table. Logical data independence is more difficult to achieve than physical data independence, as the user applications may depend on the logical structure and meaning of the data.  

- **View level data independence**: This is the ability to modify the external schema of the database without affecting the user applications. The external schema defines the views or subsets of the data that are available to different users or applications. Examples of external schema changes are adding or removing views, changing the attributes or conditions of a view, or altering the access rights or privileges of a view. View level data independence is also challenging to achieve, as the user applications may depend on the content and format of the views. 

Data independence is achieved by using a three-level architecture for the database, which separates the physical, logical, and external levels of abstraction. The data definition language (DDL) is used to define the schemas at each level, and the data manipulation language (DML) is used to access and manipulate the data. The DBMS provides a data dictionary or catalog that stores the metadata or information about the schemas, and a mapping mechanism that translates the requests and responses between different levels.



### Database Languages and Interfaces

- Database languages are the means of communication between the users and the database management system (DBMS).
- Database interfaces are the tools or applications that allow the users to interact with the database using the database languages.
- There are four main types of database languages: data definition language (DDL), data manipulation language (DML), data control language (DCL), and transaction control language (TCL).
- Data definition language (DDL) is used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, etc.
- Data manipulation language (DML) is used to manipulate the data stored in the database, such as inserting, updating, deleting, or querying data.
- Data control language (DCL) is used to control the access and security of the database, such as granting or revoking permissions, roles, or privileges to users or groups.
- Transaction control language (TCL) is used to manage the transactions in the database, such as committing, rolling back, or saving changes made by the users.
- There are different types of database interfaces for different categories of users, such as menu-based, forms-based, graphical, natural language, or application program interfaces.
- Menu-based interfaces present the user with lists of options or menus that guide the user through the database operations, such as browsing, searching, or updating data. They are suitable for web clients or novice users who do not need to write complex queries or commands.
- Forms-based interfaces allow the user to enter or view data using predefined forms or templates that are linked to the database. They are suitable for data entry or retrieval tasks that require specific input or output formats.
- Graphical user interfaces (GUI) use graphical elements such as icons, buttons, menus, or windows to represent the database objects and operations. They are suitable for users who prefer a visual and intuitive way of interacting with the database.
- Natural language interfaces allow the user to communicate with the database using natural language sentences or queries, such as English or Hindi. They are suitable for users who are not familiar with the syntax or semantics of the database languages.
- Application program interfaces (API) allow the user to access the database through a programming language or a software application, such as Java, Python, or Excel. They are suitable for users who need to perform complex or customized tasks that require programming skills or logic.



### Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects in a database.
- Database objects include tables, indexes, views, schemas, sequences, aliases, locations, and users .
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas.
- DDL uses predefined commands and a specific syntax to perform operations on database objects.
- Some common DDL commands are:
  - CREATE: to create a new database object
  - ALTER: to modify an existing database object
  - DROP: to delete a database object
  - RENAME: to rename a database object
  - TRUNCATE: to remove all data from a table
  - COMMENT: to add a comment to a database object
- DDL statements are executed by a database management system (DBMS) that interprets and validates the syntax and semantics of the commands.
- DDL statements are usually stored in a data dictionary, which is a collection of metadata that describes the structure and properties of database objects.
- DDL is different from Data Manipulation Language (DML), which is used to insert, update, delete, and query data in a database.



### DML for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

- DML stands for Data Manipulation Language, which is a type of SQL query that deals with data manipulation in a database   .
- DML commands are used to store, modify, retrieve, delete and update data in a database   .
- DML commands are not auto-committed, which means that the changes made by them are not permanent until they are committed by the user.
- The most common DML commands are:
  - SELECT: retrieve data from one or more tables  .
  - INSERT: insert data into a table  .
  - UPDATE: modify data in a table  .
  - DELETE: delete data from a table  .
- DML commands can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, etc., to filter, aggregate, sort and limit the data  .
- DML commands can also be used with subqueries, joins, functions, operators and expressions to perform complex data manipulation operations  .
- DML is different from DDL (Data Definition Language), which is used to create or modify the structure or schema of the database  .
- DML is also different from DCL (Data Control Language), which is used to grant or revoke permissions and roles to users or groups in the database .



### Overall database structure for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

- A database is a collection of related data that is organized and stored in a structured way.
- A database management system (DBMS) is a software system that allows users to create, manipulate, and access databases.
- A DBMS consists of three main components: data, data dictionary, and data manipulation language.
- Data is the actual information stored in the database, such as names, addresses, phone numbers, etc.
- Data dictionary is a set of metadata that describes the structure, format, and constraints of the data in the database.
- Data manipulation language (DML) is a set of commands that allows users to insert, update, delete, and query data in the database.
- A DBMS can also provide other features, such as data security, data integrity, data backup and recovery, data concurrency, and data independence.
- Data security is the protection of data from unauthorized access or modification.
- Data integrity is the maintenance of data consistency and accuracy.
- Data backup and recovery is the process of creating and restoring copies of data in case of data loss or corruption.
- Data concurrency is the ability of multiple users to access and modify data in the database simultaneously without interfering with each other.
- Data independence is the separation of data from the applications that use it, so that changes in data structure or format do not affect the applications.
- A DBMS can support different types of databases, such as relational, hierarchical, network, object-oriented, and NoSQL databases.
- A relational database is a database that organizes data into tables, where each table consists of rows and columns.
- A hierarchical database is a database that organizes data into a tree-like structure, where each node has one parent and zero or more children.
- A network database is a database that organizes data into a graph-like structure, where each node can have multiple parents and multiple children.
- An object-oriented database is a database that stores data as objects, which have attributes and methods.
- A NoSQL database is a database that does not follow the relational model, and can store data in various formats, such as key-value, document, column, or graph.



### Transaction Management in DBMS

- Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations.
- A transaction is a program unit whose execution may or may not change the contents of a database.
- Transactions are used to manage concurrency and ensure data integrity in a database.
- A transaction is a set of logically related operations, such as transferring money from one account to another, or booking a flight ticket.
- A transaction usually means that the data in the database has changed.
- A transaction has four properties, known as ACID properties, which are Atomicity, Consistency, Isolation, and Durability  .
- Atomicity means that either all the operations in a transaction are executed or none of them are  .
- Consistency means that a transaction preserves the integrity constraints of the database, such as primary keys, foreign keys, and domain constraints  .
- Isolation means that a transaction is executed as if it is the only one running on the database, and does not interfere with other concurrent transactions  .
- Durability means that the effects of a transaction are permanent and do not get lost due to system failures or crashes  .
- A transaction can have one of the following states: active, partially committed, committed, failed, or aborted .
- An active transaction is one that has started but not yet finished .
- A partially committed transaction is one that has executed its final statement but not yet committed .
- A committed transaction is one that has completed successfully and made its changes permanent in the database .
- A failed transaction is one that has encountered an error or violation and cannot continue .
- An aborted transaction is one that has been rolled back and its changes have been undone from the database .
- A DBMS is responsible for scheduling the access of data concurrently, and ensuring that the ACID properties of transactions are maintained  .
- A DBMS uses various techniques, such as locking, timestamping, validation, and serialization, to control the concurrency and prevent conflicts among transactions   .
- A DBMS also uses various methods, such as logging, checkpointing, and recovery, to protect the user's data from system failures and restore the database to a consistent state   .



### Storage Management for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- Storage management is the process of optimizing the use of storage resources for data storage in database systems.
- Storage management involves planning, allocating, monitoring, and maintaining the storage capacity and performance of the database system.
- Storage management is important for database administration because it affects the availability, reliability, security, and efficiency of the data and the database system.
- Storage management strategies include :
  - Understanding the data needs and value of the business
  - Choosing the appropriate storage devices and technologies
  - Using a tiered approach to store data based on its frequency of access, performance requirements, and cost
  - Mapping out disaster recovery plans and backup procedures
  - Using intelligent storage management software and tools to automate and simplify storage tasks
  - Consolidating and scaling storage systems to reduce complexity and overhead
  - Archiving and deleting infrequently accessed or obsolete data to free up space
- Storage devices and technologies for data storage in database systems include :
  - Primary storage devices, such as CPU registers, main memory, and cache memory, that store data temporarily and provide fast access to the CPU
  - Secondary storage devices, such as hard disks, solid state drives, and optical disks, that store data persistently and provide large capacity and durability
  - Tertiary storage devices, such as magnetic tapes, CDs, and DVDs, that store data for long-term archival and backup purposes
  - Storage area networks (SANs), that connect multiple storage devices and servers over a high-speed network
  - Network-attached storage (NAS), that provides file-level access to storage devices over a network
  - Cloud storage, that provides on-demand access to storage resources over the internet
- Storage management challenges include :
  - Managing the increasing volume and variety of data
  - Balancing the trade-offs between storage performance, capacity, and cost
  - Ensuring the security and integrity of the data
  - Complying with the regulatory and legal requirements for data retention and disposal
  - Adapting to the changing business and user needs and expectations



### Database Users and Administrator

Database users and administrator are the people who are accessing or working with the database. The primary aim of the database management system (DBMS) is to store the data or information and retrieve it whenever it is needed by the database users. There are different types of database users and administrator, depending on their interaction with the database and their roles and responsibilities. Some of the common types are:

- **Native Users**: These are the database users who are communicating with the database through an already written program. For example, when a student logs in to an online learning platform, the program will query the database to authenticate the student and display the relevant courses and materials. Native users do not need to know the details of the database or the query language. They just use the interface provided by the program.

- **Application Programmers**: These are the software developers and programming professionals who write the programs that interact with the database. They use a programming language such as Java, Python, C#, etc. and a query language such as SQL, NoSQL, etc. to manipulate the data in the database. They need to have a good understanding of the database schema, the query language, and the application logic.

- **Casual Users**: These are the database users who occasionally access the database for some specific purpose. They may use a query language or a graphical user interface (GUI) to retrieve the data they need. For example, a manager may want to generate a report on the sales performance of a product or a region. Casual users do not need to have a deep knowledge of the database, but they need to know how to formulate the queries or use the GUI.

- **Sophisticated Users**: These are the database users who have a high level of expertise and experience in working with the database. They may use a query language or a specialized tool to perform complex and advanced operations on the data. For example, a data analyst may use a tool such as R or Python to perform statistical analysis or data mining on the database. Sophisticated users need to have a thorough knowledge of the database, the query language, and the data analysis techniques.

- **Parametric Users**: These are the database users who access the database through a predefined set of parameters. They do not directly interact with the database, but they use an application that has a fixed set of queries or commands. For example, a bank teller may use an application that allows them to deposit, withdraw, or transfer money by entering the account number, the amount, and the transaction type. Parametric users do not need to know anything about the database or the query language. They just follow the instructions of the application.

- **Database Administrator (DBA)**: The database administrator is a person or a team who has the full control and responsibility of the database. The DBA defines the logical and physical schemas and manages all three levels of the database: the external level, the conceptual level, and the internal level. The DBA also performs tasks such as creating and maintaining user accounts, granting and revoking permissions, backing up and restoring the database, monitoring and optimizing the database performance, and ensuring the security and integrity of the database. The DBA needs to have a comprehensive knowledge of the database, the query language, the operating system, the hardware, and the network.



## Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is the process of designing and documenting the structure and semantics of data for a specific application domain.
- Data models are abstract representations of data and their relationships, constraints, and operations.
- Data models can be classified into three levels: conceptual, logical, and physical.
- Conceptual data models describe the data and their relationships at a high level of abstraction, without specifying implementation details.
- Logical data models refine the conceptual data models by adding more details, such as data types, keys, and integrity constraints.
- Physical data models specify how the data are stored and accessed in a specific database system or technology.
- The Entity Relationship (ER) model is a widely used conceptual data modeling technique that uses graphical notation to represent the data and their relationships as entities and relationships.
- An entity is an object or concept that can be identified and distinguished from others in the application domain. An entity has a set of attributes that describe its properties or characteristics.
- A relationship is an association or link between two or more entities that expresses some semantic meaning or business rule. A relationship has a name and a degree, which is the number of entities involved in the relationship.
- An entity set is a collection of entities of the same type. A relationship set is a collection of relationships of the same type.
- An entity type is a definition or template for an entity set. A relationship type is a definition or template for a relationship set.
- An entity type or a relationship type can have a key, which is a minimal set of attributes that uniquely identifies each entity or relationship in the corresponding set.
- An entity type or a relationship type can also have constraints, which are rules or conditions that restrict the possible values or combinations of values for the attributes or the relationships.
- The ER model can be extended with additional features, such as subclasses, superclasses, inheritance, specialization, generalization, aggregation, composition, and weak entities, to capture more complex and realistic data requirements.



### ER Model Concepts

- The ER model is a conceptual data model that describes the entities, attributes, and relationships in a database. It is used to design and analyze the data requirements of a system.   
- An entity is a real-world object or concept that can be identified uniquely and has some properties. For example, a student, a course, a book, etc.  
- An attribute is a property or characteristic of an entity that describes some aspect of it. For example, name, age, address, etc. Attributes can be simple or composite, single-valued or multi-valued, derived or stored, etc.  
- A relationship is an association or connection between two or more entities that expresses some meaningful dependency or interaction. For example, a student enrolls in a course, a book belongs to a library, etc. Relationships can have cardinality (one-to-one, one-to-many, many-to-many) and participation constraints (total or partial).   
- An ER diagram is a graphical representation of the ER model using symbols and notation. It shows the entities, attributes, and relationships in a database schema. It helps to visualize and communicate the data design.



### Notation for ER diagram

An ER diagram is a graphical representation of the entities and their relationships in a database. It helps to design and understand the logical structure of the data. There are different notations and symbols used to create an ER diagram, depending on the preference and convention of the modeler. Some of the common notations and symbols are:

- **Crow's foot notation**: This is the most intuitive and widely used notation for ER diagrams. It uses symbols like rectangles, ovals, diamonds, and lines to represent entities, attributes, relationships, and cardinalities. The name comes from the shape of the symbol for many-to-many relationships, which resembles a crow's foot.  

- **OMT notation**: This is a notation based on the object modeling technique (OMT), which is a method for object-oriented analysis and design. It uses symbols like boxes, circles, triangles, and lines to represent entities, attributes, relationships, and cardinalities. The name comes from the shape of the symbol for inheritance, which resembles a triangle. 

- **IDEF notation**: This is a notation based on the integrated definition (IDEF) method, which is a family of modeling languages for various domains. It uses symbols like boxes, ellipses, diamonds, and lines to represent entities, attributes, relationships, and cardinalities. The name comes from the acronym of the method. 

- **Bachman notation**: This is a notation based on the work of Charles Bachman, who is a pioneer of database management systems. It uses symbols like boxes, circles, diamonds, and lines to represent entities, attributes, relationships, and cardinalities. The name comes from the surname of the author. 

- **UML notation**: This is a notation based on the unified modeling language (UML), which is a standard for modeling software systems. It uses symbols like rectangles, ovals, diamonds, and lines to represent entities, attributes, relationships, and cardinalities. The name comes from the acronym of the language. 

- **Arrow notation**: This is a simple and easily recognizable notation for ER diagrams. It uses symbols like arrows, circles, and lines to represent entities, relationships, and cardinalities. The name comes from the shape of the symbol for relationships, which resembles an arrow. 

- **Barker's notation**: This is a notation based on the work of Richard Barker, who is a consultant and author of database design books. It uses symbols like boxes, ovals, diamonds, and lines to represent entities, attributes, relationships, and cardinalities. The name comes from the surname of the author. 

Each notation has its own advantages and disadvantages, and the choice of notation depends on the preference and convention of the modeler. However, some of the common elements and rules of ER diagrams are:

- **Entities**: Entities are the objects or concepts that are stored in the database. They are represented by rectangles or boxes with the name of the entity inside. For example, Student, Course, Department, etc. 

- **Attributes**: Attributes are the properties or characteristics of the entities. They are represented by ovals or circles with the name of the attribute inside. For example, Name, ID, Address, etc. 

- **Relationships**: Relationships are the associations or connections between the entities. They are represented by diamonds or lines with the name of the relationship above or below. For example, Enrolls, Teaches, Belongs, etc. 

- **Cardinalities**: Cardinalities are the numbers or ranges that specify how many instances of one entity can be related to another entity. They are represented by symbols or numbers on the lines that connect the entities and the relationships. For example, one-to-one, one-to-many, many-to-one, many-to-many, etc. 

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. They are represented by underlining the name of the attribute or by adding a (K) next to it. For example, ID, SSN, etc. 

- **Types**: Types are the categories or subgroups of entities or relationships. They are represented by adding a (T) next to the name of the entity or the relationship. For example, Student (T), Course (T), etc. 

- **Generalization**: Generalization is the process of grouping similar entities or relationships into a



### Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are also known as the cardinality ratio, which corresponds to the number of relationship occurrences an entity can be involved in an entity-relationship model.
- Mapping constraints are useful for describing the relationship sets that involve more than two entity sets.
- There are two types of mapping constraints on the entity-relationship model: mapping cardinality and participation constraints.
- Mapping cardinality can be one of the following four types for a binary relationship set R on entity sets A and B:
  - One-to-one: Each entity in A is associated with at most one entity in B, and each entity in B is associated with at most one entity in A.
  - One-to-many: Each entity in A is associated with any number of entities in B, but each entity in B is associated with at most one entity in A.
  - Many-to-one: Each entity in A is associated with at most one entity in B, but each entity in B is associated with any number of entities in A.
  - Many-to-many: Each entity in A is associated with any number of entities in B, and each entity in B is associated with any number of entities in A.
- Participation constraints specify whether the existence of an entity depends on its being related to another entity via the relationship set.
- Participation constraints can be either total or partial for each entity set participating in a relationship set:
  - Total: Every entity in the entity set must participate in at least one relationship in the relationship set.
  - Partial: Some entities in the entity set may not participate in any relationship in the relationship set.
- Mapping constraints can be represented by using different notations in the entity-relationship diagrams, such as crow's foot, Chen, or UML.
- Mapping constraints can help to enforce data integrity and avoid redundancy in the database design.



### Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Data modeling is a method for designing and representing complex data systems.
- Entity Relationship Model (ER Model) is a type of data modeling that uses diagrams to show the structure and relationships of entities in a database .
- An entity is an object or concept that can be identified and distinguished from others, such as a person, place, or thing .
- An attribute is a property or characteristic of an entity, such as a name, age, or address .
- A relationship is an association or connection between two or more entities, such as a student enrolls in a course, or a customer orders a product .
- An Entity Relationship Diagram (ER Diagram) is a graphical representation of the ER Model, using symbols and notation to show the entities, attributes, and relationships in a database  .
- An ER Diagram can be drawn at three different levels: conceptual, logical, or physical, depending on the level of detail and purpose of the design.
- A conceptual ER Diagram shows the high-level view of the database, without specifying the data types or constraints of the attributes or relationships.
- A logical ER Diagram shows the detailed view of the database, including the data types and constraints of the attributes and relationships, as well as the primary keys and foreign keys.
- A primary key is an attribute or a combination of attributes that uniquely identifies each entity in a relation .
- A foreign key is an attribute or a combination of attributes that references the primary key of another relation, to establish a relationship between them .
- A physical ER Diagram shows the implementation view of the database, including the specific names and formats of the tables, columns, and indexes.
- ER Diagrams use different symbols and notation to represent the entities, attributes, and relationships in a database, such as rectangles, ovals, diamonds, lines, and crow's feet   .
- A rectangle represents an entity, and the name of the entity is written inside the rectangle   .
- An oval represents an attribute, and the name of the attribute is written inside the oval   .
- A line connects an entity and an attribute, to show that the attribute belongs to the entity   .
- A diamond represents a relationship, and the name of the relationship is written inside the diamond   .
- A line connects two entities and a relationship, to show that the entities participate in the relationship   .
- A crow's foot at the end of a line indicates the cardinality of the relationship, which is the number of instances of one entity that can be associated with one instance of another entity   .
- A single line indicates a one-to-one relationship, which means that one instance of an entity can be associated with at most one instance of another entity   .
- A double line indicates a one-to-many relationship, which means that one instance of an entity can be associated with many instances of another entity   .
- A three-pronged line indicates a many-to-many relationship, which means that many instances of an entity can be associated with many instances of another entity   .
- An attribute can be classified as simple or composite, single-valued or multi-valued, derived or stored, or key or non-key  .
- A simple attribute is an attribute that cannot be divided into sub-attributes, such as a name or a phone number[^2



### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- There can be more than one super key for a table, but only one candidate key .
- A super key can also be NULL, unless the table has a primary key constraint.
- An example of a super key is the combination of student ID and student name in a table of students. This combination can uniquely identify each student, but student ID alone is enough to do so. Therefore, student ID is a candidate key and a subset of the super key .



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

- A primary key is a special column or combination of columns in a relational database table that uniquely identifies each row in the table   .
- A primary key is used as a unique identifier to quickly access and manipulate data within the table .
- A table can have only one primary key, and a primary key cannot have null values  .
- A primary key can be either a simple key (a single column) or a composite key (a combination of two or more columns) .
- A primary key can be defined at the time of table creation (using the PRIMARY KEY constraint) or after the table is created (using the ALTER TABLE statement) .
- A primary key can be referenced by other tables to establish relationships between tables. The columns in other tables that refer to the primary key are called foreign keys  .



### Generalization for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Generalization is a bottom-up approach in which two or more lower level entities are combined to form a higher level entity based on their common attributes  .
- Generalization is a process of data abstraction that hides the details of a set of objects and creates a generalized entity that can represent them all.
- Generalization can be represented in an entity-relationship diagram (ERD) by using an is-a relationship between the higher level entity and the lower level entities  .
- An example of generalization is the entity PERSON that can be generalized from the entities STUDENT and TEACHER based on their common attribute NAME  .

Generalization example

- Generalization can be used to reduce the complexity of the ER model by grouping entities with similar characteristics into a single entity  .
- Generalization can also be used to model inheritance hierarchies in object-oriented databases, where the higher level entity inherits the properties and methods of the lower level entities.
- Generalization can be combined with other concepts such as specialization and aggregation to create more complex and expressive ER models   .



### Aggregation in Entity Relationship Model

- Aggregation is a technique to model a relationship involving a relationship set and one or more entity sets .
- Aggregation allows us to treat a relationship set as an entity set for purposes of participation in other relationships .
- Aggregation is an abstraction through which we can represent relationships as higher level entity sets.
- Aggregation protects the integrity of an assembly of objects by defining a single point of control.
- Aggregation is useful when we need to express a relationship among relationships, or when we need to attach attributes to relationships.

#### Example of Aggregation

- Consider a scenario where an employee works for a project and requires some machinery. We can model this as follows:

Aggregation Example

- In this example, WORKS_FOR is a relationship between EMPLOYEE and PROJECT entity sets, and REQUIRE is a relationship between WORKS_FOR and MACHINERY entity sets .
- We can use aggregation to treat WORKS_FOR as a higher level entity set, and form a relationship set OFFERS between CENTER and WORKS_FOR .
- This way, we can express that a center offers a work opportunity for an employee on a project with some machinery .

Aggregation Example with OFFERS

- Aggregation vs. ternary relationship: In some cases, we can use a ternary relationship instead of aggregation to model a similar scenario. For example, we can use a ternary relationship MONITORS between CENTER, EMPLOYEE and PROJECT to express that a center monitors an employee working on a project.
- However, aggregation is preferred when we need to distinguish the relationship between EMPLOYEE and PROJECT from the relationship between CENTER and EMPLOYEE-PROJECT pair, or when we need to attach attributes to the relationship between EMPLOYEE and PROJECT.

Ternary Relationship Example



### Reduction of an ER diagram to tables

An ER diagram is a graphical representation of the entities and relationships in a database. It shows the structure and constraints of the data. To implement the database, we need to convert the ER diagram into a collection of tables. Each table represents an entity set or a relationship set in the ER diagram. The following are the general rules for converting an ER diagram to tables  :

- For each strong entity set, create a table with the same name and include all the attributes as columns. Declare the primary key attribute(s) of the entity set as the primary key of the table.
- For each weak entity set, create a table with the same name and include all the attributes as columns. Include the primary key attribute(s) of the owner entity set as foreign key(s) in the weak entity set table. Declare the combination of foreign key(s) and partial key attribute(s) of the weak entity set as the primary key of the table.
- For each one-to-one or one-to-many relationship set, identify the entity set that participates as the many side and include the primary key attribute(s) of the other entity set as foreign key(s) in the many side table. If the relationship set has any attributes, include them as columns in the many side table as well. If the relationship set is one-to-one and both entity sets are strong, choose either entity set to include the foreign key.
- For each many-to-many relationship set, create a table with the same name and include the primary key attribute(s) of both participating entity sets as foreign key(s) in the relationship set table. Declare the combination of foreign key(s) as the primary key of the table. If the relationship set has any attributes, include them as columns in the relationship set table as well.
- For each multivalued attribute, create a separate table with the same name and include the attribute as a column. Include the primary key attribute(s) of the entity set or relationship set that the multivalued attribute belongs to as foreign key(s) in the multivalued attribute table. Declare the combination of foreign key(s) and multivalued attribute as the primary key of the table.
- For each derived attribute, do not include it as a column in the table. Instead, use a function or a query to compute its value from the other attributes when needed.

Here is an example of an ER diagram and its corresponding tables:

ER diagram example

The tables are:

**LECTURE** (Lecture_ID, Lecture_Name, Lecture_Duration, Course_ID)  
Primary key: Lecture_ID  
Foreign key: Course_ID references COURSE(Course_ID)

**STUDENT** (Student_ID, Student_Name, Student_Address, Student_Phone)  
Primary key: Student_ID

**SUBJECT** (Subject_ID, Subject_Name, Subject_Credit)  
Primary key: Subject_ID

**COURSE** (Course_ID, Course_Name, Course_Fee)  
Primary key: Course_ID

**ENROLL** (Student_ID, Subject_ID, Marks)  
Primary key: (Student_ID, Subject_ID)  
Foreign key: Student_ID references STUDENT(Student_ID)  
Foreign key: Subject_ID references SUBJECT(Subject_ID)

**TEACH** (Lecture_ID, Subject_ID)  
Primary key: (Lecture_ID, Subject_ID)  
Foreign key: Lecture_ID references LECTURE(Lecture_ID)  
Foreign key: Subject_ID references SUBJECT(Subject_ID)

**PHONE** (Student_ID, Phone_Number)  
Primary key: (Student_ID, Phone_Number)  
Foreign key: Student_ID references STUDENT(Student_ID)



### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts in addition to the ER model concepts :

- **Subclasses and Superclasses**: A subclass is a subset of entities of a superclass that share some additional attributes or relationships. A superclass is a superset of entities that have some common attributes or relationships. For example, a STUDENT entity can be a subclass of a PERSON entity, and a PERSON entity can be a superclass of a STUDENT entity.
- **Specialization and Generalization**: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics of the entities in the superclass. Generalization is the reverse process of abstraction, where common properties of subclasses are grouped together to form a superclass. For example, a PERSON entity can be specialized into STUDENT and EMPLOYEE entities based on their roles, and STUDENT and EMPLOYEE entities can be generalized into a PERSON entity based on their common attributes.
- **Category or Union Type**: A category or union type is a subclass that represents a collection of entities from different entity types that share some common characteristics. For example, a VEHICLE entity can be a category of CAR, TRUCK, and BIKE entities, where each entity type has its own attributes and relationships, but they all share some common attributes such as color, model, and license number.
- **Aggregation**: Aggregation is the process of treating a relationship as an entity type, which allows relationships to have attributes and participate in other relationships. For example, a WORKS_ON relationship between an EMPLOYEE entity and a PROJECT entity can be aggregated into a WORK_ASSIGNMENT entity, which can have attributes such as hours, start date, and end date, and can participate in other relationships such as REPORTS_TO or SUPERVISES.

The extended ER model can be represented graphically using the following symbols :

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type, or between an attribute and an entity type or a relationship type
- A double line for a total participation constraint
- A single line for a partial participation constraint
- A dashed line for a weak entity type or a weak relationship type
- A double rectangle for a weak entity type
- A double diamond for a weak relationship type
- A circle with a d inside for a derived attribute
- A triangle with an ISA inside for a superclass/subclass relationship
- A circle with a c inside for a category or union type
- A dashed rectangle for an aggregation

Here is an example of an extended ER diagram for a university database:

EER diagram example



### Relationships of Higher Degree

- A relationship is an association between two or more entities in an ER model.
- The degree of a relationship is the number of entities that participate in it.
- A binary relationship has a degree of two, meaning it involves two entities.
- A ternary relationship has a degree of three, meaning it involves three entities.
- A higher degree relationship has a degree of more than three, meaning it involves more than three entities.
- Higher degree relationships are rare and complex, and they are usually avoided in ER model design.
- Higher degree relationships can be converted into binary relationships by introducing a new entity that represents the association of the original entities.
- For example, a quaternary relationship R between entities A, B, C, and D can be replaced by a new entity E that has binary relationships with A, B, C, and D.
- To read a higher degree relationship, one can isolate two out of the n participating entities and see how they relate to the third one, and repeat this for all possible pairs.



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
- A relational model is a set of rules and constraints that define how data is stored and manipulated in a relational database, based on the concepts of entities, attributes, domains, and relations.
- An entity is a real-world object or concept that can be identified and distinguished from other entities, and that has a set of properties or attributes that describe it.
- An attribute is a property or characteristic of an entity, that can have a value or a range of values.
- A domain is a set of possible values for an attribute, that defines the data type, format, and constraints of the attribute.
- A relation is a mathematical term for a table, that represents a set of entities of the same type, and that has a unique name and a set of attributes.



### Introduction to relational database

- A relational database is a type of database that stores and provides access to data points that are related to one another   .
- A relational database organizes data into rows and columns, which collectively form a table . Each row in the table is a record with a unique ID called the key. Each column in the table is an attribute that describes some property of the record.
- Data is typically structured across multiple tables, which can be joined together via a primary key or a foreign key. A primary key is a column or a set of columns that uniquely identifies each row in a table. A foreign key is a column or a set of columns that references a primary key in another table. The relationship between two tables is established by matching the foreign key with the corresponding primary key.
- Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables . The relational model was proposed by Edgar F. Codd in 1970 as a way of overcoming the limitations of the hierarchical and network models of data organization.
- Relational databases are also typically associated with transactional databases, which execute commands, or transactions, collectively. A transaction is a logical unit of work that ensures the consistency and integrity of the data. A transaction must follow the ACID properties: atomicity, consistency, isolation, and durability. Atomicity means that a transaction either completes entirely or not at all. Consistency means that a transaction does not violate any rules or constraints defined on the data. Isolation means that a transaction does not interfere with other concurrent transactions. Durability means that a transaction's effects are permanent and survive any system failures.
- Some of the advantages of relational databases are:
  - They allow for easy and flexible querying of data using a standard language called Structured Query Language (SQL).
  - They enforce data integrity and consistency by applying rules and constraints on the data.
  - They support data normalization, which is a process of organizing data into tables to avoid redundancy and anomalies.
  - They facilitate data security and authorization by allowing different levels of access and permissions to the data.
  - They enable data scalability and performance by allowing for data partitioning, indexing, caching, and replication.
- Some of the disadvantages of relational databases are:
  - They may have difficulty handling complex or unstructured data, such as images, videos, documents, or graphs.
  - They may suffer from performance issues when dealing with large volumes of data or high concurrency.
  - They may require more storage space and processing power than other types of databases.
  - They may not support some of the features or functionalities of other types of databases, such as real-time analytics, full-text search, or geospatial queries.



### Relational Database Structure

- A relational database is a collection of data organized into tables, where each table consists of rows and columns.
- Each row in a table represents a record or a tuple, and each column represents an attribute or a field of the record.
- Each table has a primary key, which is a column or a combination of columns that uniquely identifies each record in the table.
- Tables can be related to each other through foreign keys, which are columns that refer to the primary key of another table.
- The relationship between tables can be one-to-one, one-to-many, or many-to-many, depending on how many records in one table can be associated with records in another table.
- A relational database schema is a set of tables and their relationships, along with constraints and rules that define the integrity and validity of the data.
- A relational database can be manipulated using a query language, such as SQL, which allows users to create, retrieve, update, and delete data from the tables.
- A relational database can also be accessed through an application program, which uses an interface or a driver to communicate with the database management system (DBMS).
- A DBMS is a software system that manages the storage, retrieval, and manipulation of data in a relational database, and provides security, concurrency, backup, and recovery features.



### Relational Model Terminology – Domains

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



### Attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- An attribute is a describing characteristic or property that defines an item pertaining to a certain category  .
- Attributes map to database table columns, and each column should describe precisely one property of the entity.
- A relation is a set of tuples, or rows in a table, with each tuple sharing a set of attributes, or columns.
- Attributes can have different types, such as numeric, string, date, etc.
- Attributes can have different constraints, such as primary key, foreign key, unique, not null, etc.
- Attributes can have different operations, such as selection, projection, join, etc.
- Attributes can have different dependencies, such as functional, multivalued, transitive, etc.
- Attributes can have different normal forms, such as first, second, third, etc.



### Tuples

- A tuple is a **row** of a table in a relational database.
- A tuple represents a **single record** or an **instance** of the entity or relation that the table models.
- A tuple consists of **attributes** or **columns** that store the **values** or **data** for each record.
- A tuple can be identified by a **primary key**, which is a unique value or a combination of values that distinguishes it from other tuples in the same table.
- A tuple can also have **foreign keys**, which are values that reference the primary keys of other tuples in other tables, to establish **relationships** between them.
- A tuple can be **inserted**, **updated**, **deleted**, or **queried** using **SQL** commands or other database operations.
- A tuple can be **represented** by enclosing its attribute values in parentheses and separating them by commas, such as `(1, 'Alice', 'Smith', 25)`.
- A tuple can also be **accessed** by using its position or index in the table, such as `table[0]` for the first tuple, or by using its attribute names, such as `table['name']` for the name column.



### Relations and Relational Database Schema

- A **relation** is a set of tuples that have the same attributes. A tuple is a single row of data in a table. An attribute is a column or field name of a table. A relation can also be called a table or a relation variable.
- A **relational schema** is a collection of relation schemas for a whole database. A relation schema is a description of a relation, which specifies the name of the relation and the name and type of each attribute. A relational schema can also be called a database schema or a schema diagram.
- A relational schema is a **meta-data**, which means it describes the structure and constraints of data representing in a particular domain. A relational schema does not contain the actual data, but only the blueprint or design of the data.
- A relational schema can be represented by using a **notation** that shows the name of the relation, followed by the list of attributes in parentheses, separated by commas. For example, `Student (id, name, age, major)` is a relation schema for a relation named Student with four attributes: id, name, age, and major.
- A relational schema can also be represented by using a **diagram** that shows the name of the relation as a box, and the attributes as ovals connected to the box. The primary key attribute, which uniquely identifies each tuple in the relation, is underlined. For example, the following diagram shows the relation schema for Student:

Student relation schema diagram

- A relational schema can show the **connections** between different relations by using foreign key attributes, which refer to the primary key attribute of another relation. A foreign key attribute is marked with an asterisk (*). For example, the following diagram shows the relation schemas for Student and Course, and the connection between them by using the foreign key attribute sid, which refers to the id attribute of Student:

Student and Course relation schema diagram

- A relational schema can also show the **constraints** on the data, such as domain constraints, key constraints, entity integrity constraints, referential integrity constraints, and general constraints. Constraints are rules that ensure the validity and consistency of the data. For example, the following diagram shows the relation schemas for Student and Course, and some of the constraints on them:

Student and Course relation schema diagram with constraints

- The **benefits** of using a relational schema are:
  - It provides a clear and concise representation of the data and its structure.
  - It facilitates the design and implementation of the database and its applications.
  - It enables the verification and validation of the data and its constraints.
  - It supports the manipulation and querying of the data using a relational algebra or a relational calculus.
  - It allows the optimization and performance tuning of the database and its operations.



### Integrity Constraints for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Integrity constraints are the set of rules that can be used to maintain the data integrity during an insert, delete and update operations into a table.
- Data integrity refers to the overall validity, integrity, and consistency of the data present in the database table.
- There are four main types of integrity constraints in relational database:
  - Domain constraints: These are the rules that define the valid values for a column or attribute. For example, a column that stores the age of a person must have a positive integer value.
  - Key constraints: These are the rules that ensure the uniqueness of a row or record in a table. For example, a primary key is a column or a combination of columns that can uniquely identify a row in a table.
  - Entity integrity constraints: These are the rules that ensure that every table has a primary key and that the primary key or any part of it does not contain null values. For example, a table that stores the details of employees must have a primary key such as employee_id and it cannot be null.
  - Referential integrity constraints: These are the rules that ensure that the foreign key values in a table are consistent with the primary key values in the related table. For example, a table that stores the details of departments must have a foreign key such as manager_id that references the employee_id in the employee table.
- Integrity constraints are enforced by the database management system (DBMS) to ensure the quality and accuracy of the data in the database.
- Integrity constraints can be specified at the time of table creation or table modification using the SQL commands such as CREATE TABLE, ALTER TABLE, or ADD CONSTRAINT.



### Entity Integrity in Relational Database

- Entity integrity is a form of data integrity that ensures that every record in a table has a unique and non-null identifier, called a primary key  .
- A primary key is a column or a combination of columns that can uniquely identify a row in a table  .
- Entity integrity prevents duplicate records, missing values, and inconsistent data in a table  .
- Entity integrity is enforced by the database system by checking the values of the primary key before inserting, updating, or deleting data  .
- Entity integrity is important for maintaining the accuracy, consistency, and reliability of the data in a relational database  .
- Entity integrity is one of the three types of integrity constraints in the relational data model, along with referential integrity and domain integrity.



### Referential Integrity

- Referential integrity is a property of a relational database that ensures that the data in the tables is consistent and valid.
- Referential integrity is based on the concept of foreign keys, which are columns in one table that reference the primary key of another table.
- Referential integrity rules prevent the following actions:
  - Inserting a record in a child table that does not have a corresponding record in the parent table.
  - Updating a record in the parent table that would make it incompatible with the records in the child table.
  - Deleting a record in the parent table that has related records in the child table.
- Referential integrity can be enforced by using constraints, triggers, or application logic.
- Referential integrity helps to maintain the accuracy, integrity, and quality of the data in the database.



### Key Constraints for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- A key is a set of one or more attributes that uniquely identifies a tuple or a row in a relation or a table.
- A key constraint is a rule that enforces some restriction on the values of a key in a relation or a table.
- There are different types of key constraints, such as:
  - Primary key constraint: A primary key is a key that uniquely identifies each tuple in a relation. A relation can have only one primary key. A primary key cannot have null values. A primary key constraint enforces that the values of the primary key are unique and not null in a relation.
  - Foreign key constraint: A foreign key is a key that refers to the primary key of another relation. A foreign key can have null values. A foreign key constraint enforces that the values of the foreign key either match the values of the primary key of the referenced relation or are null.
  - Unique key constraint: A unique key is a key that uniquely identifies each tuple in a relation, but is not the primary key. A relation can have more than one unique key. A unique key can have null values, but only one null value per unique key. A unique key constraint enforces that the values of the unique key are unique or null in a relation.
  - Check constraint: A check constraint is a rule that enforces some condition on the values of one or more attributes in a relation. A check constraint can be used to restrict the range, format, or domain of the attribute values. For example, a check constraint can enforce that the values of an attribute are positive, or that they follow a certain pattern, or that they belong to a predefined set of values.



### Domain Constraints

- Domain constraints are the rules that define the valid values for an attribute or a column in a table.
- Domain constraints can be specified by the data type, the format, the range, or the set of permissible values for an attribute.
- Domain constraints help to ensure the data integrity and consistency in a relational database.
- Domain constraints can be enforced by the database system or by the application program that interacts with the database.
- Domain constraints can be defined at the time of creating a table or altering an existing table using the CREATE TABLE or ALTER TABLE commands in SQL.
- Domain constraints can also be defined using CHECK constraints, which allow the user to specify a condition that must be satisfied by every row in a table.
- Domain constraints can be violated if the user tries to insert, update, or delete a row that does not comply with the rules defined for the attribute or the column.
- Domain constraints can be modified or dropped using the ALTER TABLE or DROP CONSTRAINT commands in SQL.



### Relational algebra - relational calculus

- Relational algebra and relational calculus are two formal languages for manipulating data in relational databases.
- Relational algebra is a **procedural** language that specifies **how** to construct a new relation from one or more existing relations.
- Relational calculus is a **non-procedural** language that specifies **what** data to retrieve from the database without describing how to do it.
- Relational algebra and relational calculus are **logically equivalent**, meaning that any query expressed in one language can be translated into an equivalent query in the other language. This is known as **Codd's theorem**  .
- Relational algebra consists of a set of basic operations, such as selection, projection, join, union, difference, and renaming, that can be applied to relations or sets of tuples.
- Relational calculus consists of a set of formulas that use variables to represent relations or tuples, and logical connectives, such as and, or, not, and implies, to express conditions on the variables.
- There are two types of relational calculus: **tuple relational calculus** (TRC) and **domain relational calculus** (DRC).
- Tuple relational calculus uses tuple variables that range over a relation and specifies the tuples to be selected by a predicate (a logical expression) involving the tuple variables.
- Domain relational calculus uses domain variables that range over the attributes of a relation and specifies the tuples to be selected by a predicate involving the domain variables.
- Both tuple relational calculus and domain relational calculus are **safe**, meaning that they only express queries that are guaranteed to return a finite number of tuples .



### Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases .
- Relational calculus is a non-procedural language, which means it specifies what data to retrieve, not how to retrieve it .
- Tuple and domain calculus are based on the concept of predicates, which are logical expressions that evaluate to true or false for a given row or value in a database table  .
- Tuple and domain calculus differ in the type of variables they use and the way they express queries .

#### Tuple Relational Calculus (TRC)

- Tuple relational calculus uses tuple variables, which are denoted by lowercase letters (such as t, s, u) and range over tuples or rows of a table  .
- A tuple variable can be qualified by an attribute name to refer to a specific value in a tuple, such as t.name or s.age  .
- A query in tuple relational calculus is written as {t | P(t)}, where t is a tuple variable and P(t) is a predicate involving t and possibly other tuple variables or constants  .
- The result of a query in tuple relational calculus is a set of tuples that satisfy the predicate P(t)  .
- For example, the query {t | t ∈ Student ∧ t.age > 20} returns the set of tuples from the Student table whose age is greater than 20  .

#### Domain Relational Calculus (DRC)

- Domain relational calculus uses domain variables, which are denoted by uppercase letters (such as X, Y, Z) and range over domain elements or values of a table  .
- A query in domain relational calculus is written as {<X1, X2, ..., Xn> | P(X1, X2, ..., Xn)}, where X1, X2, ..., Xn are domain variables and P(X1, X2, ..., Xn) is a predicate involving X1, X2, ..., Xn and possibly other domain variables or constants  .
- The result of a query in domain relational calculus is a set of n-tuples that satisfy the predicate P(X1, X2, ..., Xn)  .
- For example, the query {<X, Y> | X ∈ Student.name ∧ Y ∈ Student.age ∧ Y > 20} returns the set of pairs of name and age from the Student table whose age is greater than 20  .

#### References

: https://en.wikipedia.org/wiki/Tuple_relational_calculus
: https://www.scaler.com/topics/dbms/relational-calculus-in-dbms/
: https://www.educba.com/relational-calculus-in-dbms/
: https://www.geeksforgeeks.org/difference-between-tuple-relational-calculus-trc-and-domain-relational-calculus-drc/
: https://www.geeksforgeeks.org/tuple-relational-calculus-trc-in-dbms/
: https://pages.cs.wisc.edu/~dbbook/openAccess/thirdEdition/slides/slides3ed-english/Ch4_Domain_Calculus.pdf



### Basic operations – selection and projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database.
- Selection is the operation of choosing a subset of rows (tuples) from a relation (table) that satisfy a given condition. The condition is specified by a predicate (a logical expression) that involves the attributes (columns) of the relation.
- Projection is the operation of choosing a subset of columns (attributes) from a relation (table) and eliminating the duplicates. The result is a new relation that contains only the specified attributes.
- In SQL, the SELECT statement combines both selection and projection operations in a single query. The WHERE clause is used to specify the selection condition, and the list of attributes after the SELECT keyword is used to specify the projection attributes.
- For example, the following SQL query performs both selection and projection on the relation Employee:

```sql
SELECT name, salary
FROM Employee
WHERE department = 'Sales';
```

- The query selects only the rows where the department attribute is 'Sales', and projects only the name and salary attributes of those rows. The result is a new relation with two columns and no duplicates.



### Set-theoretic operations in relational database

- Set-theoretic operations are based on the mathematical concept of sets, which are collections of distinct elements.
- Set-theoretic operations can be applied to relations in a relational database, which are also sets of tuples (rows) with the same attributes (columns).
- The main set-theoretic operations in relational database are union, intersection, and difference. These operations are also called relational set operators.
- Union: The union of two relations R and S is a relation that contains all the tuples that are either in R or in S or in both. The union operation is denoted by R ∪ S.
- Intersection: The intersection of two relations R and S is a relation that contains only the tuples that are common to both R and S. The intersection operation is denoted by R ∩ S.
- Difference: The difference of two relations R and S is a relation that contains only the tuples that are in R but not in S. The difference operation is denoted by R - S.
- For the set-theoretic operations to be valid, the two relations involved must be union-compatible, which means they must have the same number and type of attributes, and the attributes must be in the same order.
- Set-theoretic operations can be implemented in DBMS using different queries, such as SQL or relational algebra.
- Set-theoretic operations can be used to perform various tasks on the data, such as combining, comparing, or filtering the data from different relations.
- Set-theoretic operations can also be combined with other relational operations, such as selection, projection, join, or aggregation, to form more complex queries.



### Join Operations

Join operations are used to combine data from two or more tables in a relational database based on a common attribute or condition. Join operations are based on the relational algebra operation of the same name, which is a combination of Cartesian product and selection.

There are different types of join operations, such as:

- **Inner join**: This type of join returns only the rows that match the join condition in both tables. For example, if you want to join the tables `Customers` and `Orders` based on the `CustomerID` column, an inner join will return only the rows that have the same `CustomerID` value in both tables.
- **Outer join**: This type of join returns all the rows from one table and the matching rows from the other table. If there is no match, the missing values are filled with nulls. There are three types of outer joins: left outer join, right outer join, and full outer join. For example, if you want to join the tables `Customers` and `Orders` based on the `CustomerID` column, a left outer join will return all the rows from the `Customers` table and the matching rows from the `Orders` table. If a customer has no orders, the order details will be null.
- **Cross join**: This type of join returns the Cartesian product of the two tables, which means every row from one table is paired with every row from the other table. This type of join does not require a join condition, but it can result in a very large result set. For example, if you want to join the tables `Customers` and `Products` without any condition, a cross join will return every possible combination of customer and product.
- **Self join**: This type of join is used to join a table with itself, which means the same table is used as both the left and the right table. This type of join requires an alias for the table name to distinguish the two instances of the same table. This type of join is useful when you want to compare or relate data within the same table. For example, if you want to find the customers who live in the same city as another customer, you can use a self join on the `Customers` table based on the `City` column.

There are different ways to implement join operations in SQL, such as using the `JOIN` keyword, using the `WHERE` clause, or using subqueries. The syntax and performance of join operations may vary depending on the database system and the size and structure of the tables.




## Unit 4 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that organizes the data into tables and columns to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design by creating atomic elements (i.e. elements that cannot be broken down into smaller parts) and representing the relationships among them.
- There are several levels of normalization, each with a specific set of rules and objectives. The most common levels are:
  - First normal form (1NF): Each column in a table contains only one value and each row is unique. There are no repeating groups or arrays in a table.
  - Second normal form (2NF): Each column in a table that is not part of the primary key depends on the whole primary key. There are no partial dependencies in a table.
  - Third normal form (3NF): Each column in a table that is not part of the primary key depends only on the primary key. There are no transitive dependencies in a table.
  - Boyce-Codd normal form (BCNF): Each determinant in a table is a candidate key. A determinant is a column or a set of columns that determines the value of another column.
  - Fourth normal form (4NF): Each column in a table contains only one value from a single domain and each row is unique. There are no multi-valued dependencies in a table.
  - Fifth normal form (5NF): Each table represents a single fact and can be reconstructed from other tables using join operations. There are no join dependencies in a table.
- Normalization is a progressive process, and a higher level of normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization has many benefits, such as:
  - Eliminating data anomalies, such as insertion, deletion, and update anomalies, that can cause data inconsistency and corruption.
  - Reducing data redundancy and storage space, which can improve performance and efficiency.
  - Enhancing data integrity and security, which can prevent unauthorized access and modification.
  - Facilitating data analysis and querying, which can support decision making and business intelligence.
- Normalization also has some drawbacks, such as:
  - Increasing the number of tables and joins, which can complicate the database design and maintenance.
  - Decreasing the query performance and response time, which can affect the user experience and satisfaction.
  - Losing some information or context, which can make the data less meaningful or useful.



### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a **constraint** between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the **relation** between different values in a database management system (DBMS).
- A functional dependency is denoted by an **arrow** (→) that shows which attribute **relies** on the other.
- For example, if A and B are attributes of a relation R, then A → B means that the value of B is **determined** by the value of A.
- There are four primary types of functional dependencies: **trivial**, **non-trivial**, **multivalued**, and **transitive** .
- A trivial functional dependency is when the **dependent** is always a **subset** of the **determinant**. For example, A → A or A → AB are trivial FDs.
- A non-trivial functional dependency is when the dependent is **strictly not** a subset of the determinant. For example, A → B or AB → C are non-trivial FDs.
- A multivalued functional dependency is when the determinant can have **multiple** values for the dependent. For example, A →> B means that for a given value of A, there can be more than one value of B.
- A transitive functional dependency is when the dependent of one FD becomes the determinant of another FD. For example, A → B and B → C imply A → C.
- Functional dependencies are used to establish **relationships** between attributes in a database and to ensure that the database is in a state of **normalization**, which helps to minimize data **redundancy** and improve data **integrity** .



### Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Normal forms are used to eliminate or reduce redundancy in database tables.
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes in a relation.
- Normal forms are of four major forms: 1NF, 2NF, 3NF, and BCNF. A majority of the database systems have their databases normalized up to the 3NF in DBMS.
- 1NF: A relation is in first normal form if it does not contain any composite or multi-valued attribute. This means that each attribute should have a single atomic value and no repeating groups of attributes.
- 2NF: A relation is in second normal form if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there should be no partial dependency of any attribute on the primary key.
- 3NF: A relation is in third normal form if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there should be no transitive dependency of any attribute on the primary key.
- BCNF: A relation is in Boyce-Codd normal form if it is in 3NF and every determinant is a candidate key. This means that there should be no non-trivial functional dependency where the left-hand side is not a superkey.
- Normalization helps to avoid redundancy and maintain the integrity of the database. It also helps to eliminate undesirable characteristics associated with insertion, deletion, and updating.



### Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database management system (DBMS).
- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies.
- Normalization rules divide larger tables into smaller tables and link them using relationships.
- The main benefits of normalization are:
  - It improves data integrity and consistency by avoiding data duplication and inconsistency.
  - It reduces storage space and improves query performance by minimizing the number of columns and rows in a table.
  - It facilitates data maintenance and security by simplifying the enforcement of constraints and access control.
- The main drawbacks of normalization are:
  - It may increase the complexity and number of joins in a query, which can affect performance and readability.
  - It may require denormalization to achieve optimal performance for some applications or queries.
- Normalization is based on the concept of normal forms, which are levels of data organization that satisfy certain conditions or rules.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values and no repeating groups of attributes.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies.
- The process of normalization involves the following steps:
  - Identify the functional dependencies and candidate keys in a table.
  - Decompose the table into smaller tables based on the normal form criteria.
  - Preserve the original information and relationships by creating foreign keys and referential integrity constraints.
  - Evaluate the resulting tables for anomalies and performance issues.
  - Repeat the process until the desired level of normalization is achieved.



### Second

Database design and normalization are two important concepts in database management systems. Database design is the process of creating a logical and physical structure for the data and defining the relationships between the data entities. Normalization is a technique of database design that aims to reduce data redundancy and dependency by splitting a large table into smaller ones and establishing relationships among them.

Some of the benefits of database design and normalization are:

- Improved data integrity and consistency
- Reduced data anomalies and errors
- Enhanced query performance and efficiency
- Increased flexibility and scalability
- Easier maintenance and modification

Some of the steps involved in database design and normalization are:

- Identify the purpose and scope of the database
- Gather the data requirements and sources
- Define the data entities and attributes
- Determine the primary keys and foreign keys
- Draw the entity-relationship (ER) diagram
- Apply the normalization rules to eliminate data redundancy and dependency
- Create the data tables and indexes
- Implement the database schema and constraints
- Test and refine the database design

There are different levels or forms of normalization, each with a specific criterion to satisfy. The most common forms are:

- First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes. Each attribute should have a single value for each record.
- Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. There should be no partial dependencies or subsets of the primary key that determine other attributes.
- Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. There should be no transitive dependencies or attributes that depend on other non-key attributes.
- Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key. There should be no non-trivial functional dependencies that violate the key constraint.
- Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies. There should be no attributes that depend on a set of values rather than a single value.
- Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies. There should be no loss of information or redundancy when joining or decomposing the table.

The following is an example of database design and normalization for a student enrollment system:

- The data requirements are: student ID, student name, course ID, course name, instructor ID, instructor name, grade, and semester.
- The data entities are: student, course, instructor, and enrollment.
- The data attributes are:

| Entity | Attributes |
| --- | --- |
| Student | student ID, student name |
| Course | course ID, course name |
| Instructor | instructor ID, instructor name |
| Enrollment | student ID, course ID, instructor ID, grade, semester |

- The primary keys are: student ID, course ID, instructor ID, and a composite key of student ID and course ID for enrollment.
- The foreign keys are: student ID, course ID, and instructor ID in enrollment, referencing the respective entities.
- The ER diagram is:

ER diagram

- The normalization process is:

| Unnormalized table | Normalized tables |
| --- | --- |
| Unnormalized table | Normalized tables |

- The unnormalized table has the following problems:

  - It has repeating groups of course ID, course name, instructor ID, instructor name, grade, and semester for each student.
  - It has multivalued attributes of course ID, course name, instructor ID, instructor name, grade, and semester for each student.
  - It has partial dependencies of course name on course ID, and instructor name on instructor ID.
  - It has transitive dependencies of grade and semester on course ID and instructor ID.
  - It has redundancy and inconsistency of data, such as the same course name or instructor name appearing multiple times.
  - It has potential data anomalies and errors, such as inserting, updating, or deleting data in multiple places.

- The normalized tables are:

  - Student: This table is in 1NF, 2NF,



### Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that does not belong to any candidate key of the table.
- A transitive dependency is a functional dependency between two or more non-prime attributes that are indirectly determined by the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name.
  - The primary key is (Student ID, Course ID).
  - The non-prime attributes are Student Name, Course Name, Instructor ID, Instructor Name.
  - There is a transitive dependency between Course ID and Instructor ID, because Course ID determines Instructor ID, and Instructor ID determines Instructor Name.
  - To convert this table to 3NF, we need to remove the transitive dependency by creating a separate table for Course ID, Course Name, Instructor ID, Instructor Name, with Course ID as the primary key.
  - The original table will only have Student ID, Student Name, Course ID as the attributes, and it will reference the new table by Course ID as a foreign key.
- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the 3NF.
  - The 3NF always ensures functional dependency preserving and lossless decomposition.
  - The 3NF reduces the storage space and improves the performance of the queries.



### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form).
- A relation is in BCNF if it is in 3NF and for every functional dependency X -> Y, X is a superkey or a candidate key of the relation  .
- A superkey is a set of attributes that uniquely identifies a tuple in a relation. A candidate key is a minimal superkey, meaning that no proper subset of it is a superkey.
- BCNF is stricter than 3NF, as it eliminates the possibility of having a non-prime attribute (an attribute that is not part of any candidate key) on the right-hand side of a functional dependency.
- The purpose of BCNF is to reduce redundancy and anomalies in the data, such as insertion, deletion and update anomalies.
- To convert a relation into BCNF, we need to decompose it into smaller relations that satisfy the BCNF condition, while preserving the functional dependencies and the data.
- An example of BCNF decomposition is as follows:

  - Consider a relation R(ABCDE) with the following functional dependencies: FD = {A -> BC, C -> DE}.
  - The candidate key of R is A, as it determines all the other attributes.
  - The relation R is not in BCNF, as the functional dependency C -> DE violates the BCNF condition, since C is not a superkey or a candidate key.
  - To convert R into BCNF, we need to decompose it into two relations: R1(ABC) and R2(CDE), such that R1 has the functional dependency A -> BC and R2 has the functional dependency C -> DE.
  - The relations R1 and R2 are in BCNF, as the left-hand side of each functional dependency is a candidate key of the relation.
  - The decomposition preserves the functional dependencies and the data of R, as we can reconstruct R by joining R1 and R2 on the attribute C.



### Inclusion Dependency in DBMS

- An inclusion dependency (IND) is a statement that some columns of a relation are contained in other columns of the same or another relation  .
- An IND has the form R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are attributes, and n is a positive integer.
- An IND means that for every tuple t in R, there exists a tuple s in S such that t[A1] = s[B1], t[A2] = s[B2], ..., and t[An] = s[Bn].
- An IND is a generalization of a referential constraint (or foreign key constraint), which is a special case of an IND where n = 1   .
- An IND can be used to guide the design of the database, but they usually have little influence on how the database is actually designed  .
- An example of an IND is Employee[DeptNo] ⊆ Department[DeptNo], which means that every employee belongs to a valid department  .



### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R  .
- Lossless join decomposition is desirable because it eliminates redundancy and anomalies from the relation R without losing any information .
- Lossless join decomposition can be verified by using the following criteria:
  - Let F be the set of functional dependencies that hold on R, and F+ be the closure of F.
  - The decomposition of R into R1, R2, ... is lossless if and only if for every pair of relations Ri and Rj, one of the following functional dependencies is in F+:
    - Ri ∩ Rj → Ri
    - Ri ∩ Rj → Rj
    - Ri ∩ Rj → Ri ∪ Rj
- Lossless join decomposition can also be achieved by using decomposition algorithms based on normal forms, such as BCNF and 3NF. These algorithms ensure that the decomposed relations are free of redundancy and preserve the dependencies of the original relation.



### Normalization using FD

- Normalization is a process of organizing the data in a database to avoid data redundancy, insertion anomaly, update anomaly and deletion anomaly.
- Functional dependency (FD) is a constraint that describes the relationship between attributes in a relation.
- FDs are used to decompose relations into smaller relations that are in higher normal forms.
- Normal forms are the standards for evaluating the quality of a relation. The most common normal forms are 1NF, 2NF, 3NF and BCNF.
- 1NF: A relation is in 1NF if it has no repeating groups or multivalued attributes. Every attribute value must be atomic and unique within a tuple.
- 2NF: A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there is no partial dependency of any attribute on the primary key.
- 3NF: A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there is no transitive dependency of any attribute on the primary key.
- BCNF: A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there is no dependency of any attribute on a non-key attribute.
- The steps to normalize a relation using FDs are:
  - Identify all the candidate keys and the primary key of the relation.
  - Identify all the FDs that hold in the relation.
  - Check if the relation is in 1NF. If not, eliminate the repeating groups or multivalued attributes by creating new relations.
  - Check if the relation is in 2NF. If not, decompose the relation into smaller relations such that each relation is in 2NF.
  - Check if the relation is in 3NF. If not, decompose the relation into smaller relations such that each relation is in 3NF.
  - Check if the relation is in BCNF. If not, decompose the relation into smaller relations such that each relation is in BCNF.
  - Eliminate any redundant relations that may have been created during the decomposition process.



### MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for multivalued dependency, which is a type of constraint between two sets of attributes in a relation.
- A multivalued dependency occurs when one attribute determines multiple values of another attribute, independently of other attributes.
- For example, if a relation R has attributes A, B, and C, and A --> --> B means that for each value of A, there are multiple values of B, then R has a multivalued dependency A --> --> B.
- MVD plays a role in the 4NF database normalization, which is a process of reducing redundancy and anomalies in a relation.
- 4NF requires that a relation should be in BCNF and have no multivalued dependencies.
- To check if a relation is in 4NF, we can use the following steps:
  - Identify all the candidate keys of the relation.
  - Identify all the non-trivial multivalued dependencies in the relation.
  - For each multivalued dependency X --> --> Y, check if X is a superkey or not.
  - If X is not a superkey, then the relation is not in 4NF and needs to be decomposed into two relations: one with attributes XY and another with attributes XZ, where Z is the set of attributes other than X and Y.
  - Repeat the process until there are no multivalued dependencies in any relation.
- Normalization has several benefits, such as reducing redundancy, maintaining consistency, saving space, and simplifying queries. However, it also has some drawbacks, such as increased complexity, reduced performance, and possible loss of information. Therefore, it is important to balance the trade-offs between normalization and denormalization according to the requirements of the database system.



# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its information needs.
  - Ensure data integrity, consistency, and quality.
  - Minimize data redundancy and duplication.
  - Optimize data access and performance.
  - Facilitate data maintenance and evolution.
- Database design can be divided into three phases:
  - Conceptual design: The high-level description of the data and its relationships, using a conceptual data model such as the entity-relationship (ER) model or the unified modeling language (UML) class diagram.
  - Logical design: The translation of the conceptual design into a logical data model such as the relational model or the object-relational model, which defines the tables, columns, keys, and constraints.
  - Physical design: The implementation of the logical design in a specific database management system (DBMS), which defines the storage structures, indexes, views, and other physical aspects.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization also helps to avoid data anomalies, such as insertion, deletion, and update anomalies, which can cause data inconsistency and corruption.
- Normalization is based on the concept of normal forms, which are sets of rules or criteria that a table must satisfy to be considered well-structured and normalized.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values, i.e., each cell can hold only one value, and there are no repeating groups or arrays of values.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no non-trivial functional dependencies that violate the key constraint.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, i.e., there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, i.e., it cannot be decomposed into smaller tables without losing information.



### Alternative Approaches to Database Design

- Database design is the process of defining the structure, organization, and relationships of data in a database.
- Database design can be influenced by various factors, such as the purpose, scope, and requirements of the database, the type and volume of data, the performance and scalability needs, and the available tools and technologies.
- There are different approaches and techniques that can be used to design a database, depending on the context and the goals of the database project. Some of the alternative approaches to database design are:

  - **Top-down design**: This approach starts with a high-level conceptual model of the data and its relationships, and then refines it into a logical and physical model. This approach is suitable for complex and large-scale databases that require careful planning and analysis. The advantages of this approach are that it helps to ensure data integrity, consistency, and normalization. The disadvantages are that it can be time-consuming, rigid, and difficult to adapt to changing requirements. 
  - **Bottom-up design**: This approach starts with a low-level physical model of the data and its storage, and then builds a logical and conceptual model on top of it. This approach is suitable for simple and small-scale databases that do not require much planning and analysis. The advantages of this approach are that it is fast, flexible, and easy to implement. The disadvantages are that it can lead to data redundancy, inconsistency, and denormalization. 
  - **Domain-driven design**: This approach starts with a domain model of the business entities and their behaviors, and then maps it to a data model. This approach is suitable for agile and iterative development methodologies that focus on the business value and user needs. The advantages of this approach are that it helps to align the database design with the business logic and the user expectations. The disadvantages are that it can be challenging to translate the domain model into a data model, and that it can require frequent changes and refinements. 
  - **NoSQL design**: This approach uses non-relational databases that store data in different formats and structures, such as documents, graphs, key-value pairs, or columns. This approach is suitable for handling large and diverse data sets that do not fit well in the relational model. The advantages of this approach are that it offers high performance, scalability, and flexibility. The disadvantages are that it can compromise data consistency, integrity, and security.



## Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for accessing and manipulating data in relational databases.
- SQL stands for Structured Query Language and is pronounced as "sequel" or "ess-que-ell".
- SQL can perform various tasks on data, such as creating, querying, updating, deleting, and managing tables, views, indexes, and constraints.
- SQL is divided into several sublanguages, each with a specific purpose and syntax. The main sublanguages are:
  - Data Definition Language (DDL): used to define the structure and schema of the database objects, such as tables, views, indexes, and constraints.
  - Data Manipulation Language (DML): used to insert, update, delete, and query data in the database objects.
  - Data Control Language (DCL): used to grant and revoke permissions and roles to users and groups for accessing and modifying the database objects.
  - Transaction Control Language (TCL): used to manage the transactions that affect the data in the database objects, such as commit, rollback, and savepoint.
- SQL is a declarative language, which means that it specifies what data to retrieve or manipulate, rather than how to do it. The database management system (DBMS) is responsible for translating the SQL statements into low-level operations and executing them efficiently.
- SQL is a standardized language that is supported by most relational DBMSs, such as Oracle, MySQL, PostgreSQL, SQL Server, and SQLite. However, each DBMS may have some variations and extensions to the SQL syntax and features, which are called dialects or flavors of SQL. Therefore, it is important to check the documentation of the specific DBMS before using SQL.



### Basics of SQL

SQL stands for Structured Query Language, which is a computer language for storing, manipulating and retrieving data stored in a relational database . SQL is not a database system, but it is a query language that can be used with various database systems, such as MySQL, SQL Server, Oracle, etc .

Some of the basic concepts and operations of SQL are:

- **Database**: A database is a collection of organized data that can be accessed and manipulated by SQL commands. A database can have one or more tables, which store the data in rows and columns .
- **Table**: A table is a structure that holds the data in a database. A table has a name and a set of columns, each with a name and a data type. A table can have one or more rows, which are the records of the data .
- **Column**: A column is a vertical part of a table that stores a specific attribute of the data. For example, a table of customers can have columns such as customer_id, name, address, etc. A column has a name and a data type, such as integer, varchar, date, etc .
- **Row**: A row is a horizontal part of a table that stores a single record of the data. For example, a table of customers can have rows that represent each customer's information. A row has a set of values, one for each column in the table .
- **Primary Key**: A primary key is a column or a combination of columns that uniquely identifies each row in a table. A primary key ensures that there are no duplicate rows in a table and that each row can be referenced by other tables .
- **Foreign Key**: A foreign key is a column or a combination of columns that references the primary key of another table. A foreign key establishes a relationship between two tables and ensures that the data is consistent and valid .
- **Query**: A query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. A query can have various clauses, such as SELECT, FROM, WHERE, GROUP BY, ORDER BY, etc., that specify the details of the data retrieval .
- **Statement**: A statement is a complete SQL command that can be executed by the database system. A statement can be a query, such as SELECT, or a command, such as INSERT, UPDATE, DELETE, etc., that performs an operation on the data .
- **CRUD**: CRUD stands for Create, Read, Update and Delete, which are the four basic operations in any database. SQL can perform all of these operations with different statements, such as INSERT, SELECT, UPDATE and DELETE.

These are some of the basics of SQL that you should know for the subject of Basics of Data Base Management System. For more details and examples, you can refer to the web search results. I hope this helps you.



### DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that are used to create, modify, and delete database objects such as tables, views, indexes, schemas, etc.
- DDL commands do not affect the data stored in the database, but only the structure or schema of the database.
- Some of the common DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table named students with three columns: id, name, and age.
  - ALTER: This command is used to modify an existing database object, such as adding, dropping, or renaming columns, changing data types, adding constraints, etc. For example, `ALTER TABLE students ADD email VARCHAR(50);` adds a new column named email to the students table.
  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc. For example, `DROP TABLE students;` deletes the students table and all the data stored in it.
  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table, but the table structure remains intact.
- DDL commands are normally executed by database administrators or developers, who have the necessary permissions to create and modify the database schema. DDL commands are not used by general users, who should access the database through an application or a query interface.



### DML

- Data Manipulation Language (DML) is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views .
- The main DML statements are SELECT, INSERT, DELETE, and UPDATE  .
- SELECT statement is used to retrieve data from one or more tables .
- INSERT statement is used to add new rows to a table .
- DELETE statement is used to remove existing rows from a table .
- UPDATE statement is used to modify existing rows in a table .
- DML statements can be used with various clauses, such as WHERE, ORDER BY, GROUP BY, HAVING, etc., to filter, sort, aggregate, and manipulate the data.
- DML statements can also be used with subqueries, joins, and set operators to combine data from multiple tables or sources.



### DCL

- Data Control Language (DCL) is a sublanguage of SQL that deals with the commands used to control the access and privileges of users on the database .
- DCL allows the database owner or administrator to grant, revoke, or change the permissions of users to perform certain operations on the database, such as insert, delete, select, update, execute, or alter data  .
- DCL is used for enforcing data security and ensuring that only authorized users can access or modify the data .
- The main DCL commands in SQL are:
  - **GRANT**: This command is used to grant (give access to) security privileges to specific database users or roles . For example, `GRANT SELECT ON employees TO user1;` grants the permission to select data from the employees table to user1.
  - **REVOKE**: This command is used to revoke (take away) security privileges from specific database users or roles . For example, `REVOKE SELECT ON employees FROM user1;` revokes the permission to select data from the employees table from user1.
  - **DENY**: This command is used to deny (block) security privileges to specific database users or roles. For example, `DENY SELECT ON employees TO user1;` denies the permission to select data from the employees table to user1. This command is mainly used in Microsoft SQL Server and not in other SQL dialects.



### Advantages of SQL

SQL is a widely used language for managing and manipulating data in relational database management systems. Some of the advantages of SQL are:

- **Faster and efficient query processing.** SQL can process large amounts of data in a very short time, using simple and concise commands. This can improve the performance and scalability of the database system.   
- **Standardized language.** SQL is a standardized language that follows the ANSI and ISO standards. This means that SQL can be used across different database platforms and applications, without requiring much modification. SQL also has a common syntax and structure that is easy to learn and understand.  
- **No coding skills required.** SQL does not require complex programming skills or logic to retrieve data from the database. SQL uses natural English phrases and keywords, such as SELECT, FROM, WHERE, etc., to specify the data requirements. SQL also has built-in functions and operators that can perform various calculations and manipulations on the data.  
- **Integration with other languages.** SQL can be integrated with other programming languages, such as Java, Python, C#, etc., to create dynamic and interactive applications that use data from the database. SQL can also be embedded in HTML, XML, JSON, etc., to exchange data over the web.  
- **Data analysis and decision making.** SQL can be used to perform various data analysis tasks, such as filtering, sorting, grouping, aggregating, joining, etc., on the data stored in the database. SQL can also generate reports, charts, graphs, etc., to visualize and present the data in a meaningful way. SQL can help businesses to gain insights and make better decisions from their data.



### SQL data type and literals

- SQL data types are the attributes that define the kind of values that can be stored in a column of a table or a variable in a program.
- SQL data types can be categorized into numeric, character, date and time, Boolean, and special types.
- Numeric data types include integers, decimals, floats, and binary numbers.
- Character data types include fixed-length and variable-length strings of characters, such as char, varchar, text, etc.
- Date and time data types include date, time, timestamp, interval, etc. that store values related to calendar and clock.
- Boolean data types include boolean or bit that store true or false values.
- Special data types include blob, clob, xml, json, etc. that store large objects of binary or character data, or structured data in a specific format.

- SQL literals are the constant values that can be used in SQL statements or expressions.
- SQL literals can be classified into four types: string, numeric, date and time, and Boolean literals.
- String literals are enclosed in single quotes, such as 'Hello', '2021-03-15', etc.
- Numeric literals are not enclosed in quotes, such as 42, 3.14, 0b1010, etc.
- Date and time literals are enclosed in single quotes and follow a specific format, such as '2021-03-15', '22:11:26', '2021-03-15 22:11:26', etc.
- Boolean literals are not enclosed in quotes and can be either true or false.



### Types of SQL Commands

SQL commands are instructions that are used to communicate with the database and perform various tasks. SQL commands can be classified into five main categories, depending on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of the database objects, such as tables, views, indexes, etc. Some examples of DDL commands are CREATE, ALTER, DROP, RENAME, and TRUNCATE   .
- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from the database tables. Some examples of DML commands are INSERT, UPDATE, DELETE, and MERGE   .
- **Data Query Language (DQL)**: These commands are used to query or select data from the database tables. The most common DQL command is SELECT, which can be used with various clauses and functions to filter, sort, group, or aggregate data    .
- **Data Control Language (DCL)**: These commands are used to grant or revoke permissions or access rights to the database objects or users. Some examples of DCL commands are GRANT, REVOKE, and DENY   .
- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, such as committing, rolling back, or saving the changes made by the DML commands. Some examples of TCL commands are COMMIT, ROLLBACK, and SAVEPOINT   .

These are the main types of SQL commands that are used to interact with the database. Each command has its own syntax and options that can be learned from various sources, such as books, online tutorials, or documentation. SQL is a powerful and widely used language for data manipulation and analysis.



### SQL operators and their procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They are used to specify conditions, filter results, compare values, perform calculations, concatenate strings, and more. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used for mathematical operations on numerical data, such as adding, subtracting, multiplying, dividing, and finding the remainder. For example, `SELECT 10 + 10;` returns 20.
- Comparison operators: These operators are used to compare two values or expressions and return a boolean value (true or false). For example, `SELECT 10 > 10;` returns false.
- Logical operators: These operators are used to combine two or more conditions and return a boolean value. They are often used with the WHERE clause to filter the results based on multiple criteria. For example, `SELECT * FROM customers WHERE age > 18 AND gender = 'F';` returns all the female customers who are older than 18.
- Bitwise operators: These operators are used to perform bitwise operations on binary data, such as AND, OR, XOR, NOT, and SHIFT. They are often used to manipulate bits, flags, and masks. For example, `SELECT 10 & 2;` returns 2, which is the result of bitwise AND operation between 10 (1010 in binary) and 2 (0010 in binary).
- String operators: These operators are used to manipulate character data, such as concatenating, extracting, replacing, and converting. For example, `SELECT 'Hello' + ' ' + 'World';` returns 'Hello World', which is the result of concatenating two strings with a space in between.
- Set operators: These operators are used to combine the results of two or more queries and return a single result set. They are often used to perform set operations, such as union, intersection, difference, and symmetric difference. For example, `SELECT name FROM customers UNION SELECT name FROM suppliers;` returns the names of all the customers and suppliers, without any duplicates.



### Tables – Creation & Alteration

- A table is a collection of data organized in rows and columns in a relational database.
- To create a table in SQL, use the `CREATE TABLE` command, followed by the name of the table and the definition of its columns and constraints.
- For example, the following SQL statement creates a table called `Students` with four columns: `id`, `name`, `grade`, and `email`.

```sql
CREATE TABLE Students (
  id int PRIMARY KEY,
  name varchar(50) NOT NULL,
  grade char(1) CHECK (grade IN ('A', 'B', 'C', 'D', 'F')),
  email varchar(50) UNIQUE
);
```

- The `PRIMARY KEY` constraint defines a column that uniquely identifies each row in the table.
- The `NOT NULL` constraint ensures that a column cannot have a null value.
- The `CHECK` constraint validates that a column value satisfies a logical condition.
- The `UNIQUE` constraint ensures that a column value is not repeated in the table.
- To alter a table in SQL, use the `ALTER TABLE` command, followed by the name of the table and the changes to be made.
- For example, the following SQL statement adds a new column called `phone` to the `Students` table.

```sql
ALTER TABLE Students
ADD phone varchar(10);
```

- The `ADD` clause adds a new column or constraint to the table.
- To modify an existing column or constraint, use the `MODIFY` or `ALTER` clause.
- For example, the following SQL statement changes the data type of the `phone` column to `char(10)`.

```sql
ALTER TABLE Students
MODIFY phone char(10);
```

- To delete an existing column or constraint, use the `DROP` clause.
- For example, the following SQL statement removes the `email` column from the `Students` table.

```sql
ALTER TABLE Students
DROP COLUMN email;
```

- To rename a table or a column, use the `RENAME` clause.
- For example, the following SQL statement renames the `Students` table to `Learners`.

```sql
ALTER TABLE Students
RENAME TO Learners;
```

- To delete a table from the database, use the `DROP TABLE` command, followed by the name of the table.
- For example, the following SQL statement deletes the `Learners` table.

```sql
DROP TABLE Learners;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` command, followed by the name of the new table and a query that selects the data from the existing table.
- For example, the following SQL statement creates a new table called `Graduates` that contains the data from the `Students` table where the `grade` is `A`.

```sql
CREATE TABLE Graduates AS
SELECT * FROM Students
WHERE grade = 'A';
```

- To truncate a table, use the `TRUNCATE TABLE` command, followed by the name of the table.
- This command deletes all the data from the table, but preserves its structure and constraints.
- For example, the following SQL statement truncates the `Graduates` table.

```sql
TRUNCATE TABLE Graduates;
```

- To view the structure and constraints of a table, use the `DESCRIBE` or `DESC` command, followed by the name of the table.
- For example, the following SQL statement describes the `Students` table.

```sql
DESCRIBE Students;
```

- This command returns the following output:

| Field | Type        | Null | Key  | Default | Extra |
| ----- | ----------- | ---- | ---- | ------- | ----- |
| id    | int         | NO   | PRI  | NULL    |       |
| name  | varchar(50) | NO   |      | NULL    |       |
| grade | char(1)     | YES  |      | NULL    |       |
| email | varchar(50) | YES  | UNI  | NULL    |       |
| phone | char(10)    | YES  |      | NULL    |       |

- To view the data in a table, use the `SELECT` command, followed by the columns and the table name.
- For example, the following SQL statement selects all the columns and rows from the `Students` table.

```sql
SELECT * FROM Students;
```

- This command returns the following output:

| id | name       | grade



### Defining Constraints for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- Constraints are rules or restrictions that are applied to the columns or tables in a database to ensure data integrity and consistency.
- Constraints can be defined at the column level or the table level, depending on the scope of the constraint.
- Constraints can be specified when creating a table using the CREATE TABLE statement, or after the table is created using the ALTER TABLE statement.
- Some of the common types of constraints are:

  - NOT NULL: This constraint ensures that a column cannot have a NULL value. For example, `CREATE TABLE student (id INT NOT NULL, name VARCHAR(50) NOT NULL);` creates a table with two columns, id and name, that cannot be NULL.
  - UNIQUE: This constraint ensures that a column or a combination of columns has a unique value for each row in the table. For example, `CREATE TABLE student (id INT NOT NULL UNIQUE, name VARCHAR(50) NOT NULL);` creates a table with a unique id for each student.
  - PRIMARY KEY: This constraint combines the NOT NULL and UNIQUE constraints, and identifies a column or a combination of columns as the primary key of the table. The primary key is used to uniquely identify each row in the table and to establish relationships with other tables. For example, `CREATE TABLE student (id INT NOT NULL PRIMARY KEY, name VARCHAR(50) NOT NULL);` creates a table with id as the primary key.
  - FOREIGN KEY: This constraint establishes a relationship between a column or a combination of columns in one table and the primary key of another table. The foreign key references the primary key of the related table and ensures that the values in the foreign key column(s) exist in the primary key column(s) of the related table. For example, `CREATE TABLE course (code VARCHAR(10) NOT NULL PRIMARY KEY, title VARCHAR(100) NOT NULL);` creates a table with code as the primary key, and `CREATE TABLE enrollment (student_id INT NOT NULL, course_code VARCHAR(10) NOT NULL, grade CHAR(1), FOREIGN KEY (student_id) REFERENCES student(id), FOREIGN KEY (course_code) REFERENCES course(code));` creates a table with two foreign keys, student_id and course_code, that reference the primary keys of the student and course tables, respectively.
  - CHECK: This constraint allows to specify a condition that must be satisfied by the values in a column or a table. For example, `CREATE TABLE student (id INT NOT NULL PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT CHECK (age >= 18));` creates a table with a check constraint that ensures that the age of the students is at least 18.
  - DEFAULT: This constraint allows to specify a default value for a column when no value is provided for that column. For example, `CREATE TABLE student (id INT NOT NULL PRIMARY KEY, name VARCHAR(50) NOT NULL, gender CHAR(1) DEFAULT 'M');` creates a table with a default constraint that assigns 'M' as the gender of the students if no value is given for that column.



### Views and Indexes in SQL

- A **view** is a named query that is stored in the database and can be used like a table. A view can hide the complexity of the underlying tables and provide a simpler or more meaningful way of accessing the data. A view can also restrict the access to certain columns or rows of the underlying tables. 
- An **index** is a data structure that improves the speed of data retrieval from a table. An index can be created on one or more columns of a table, and it allows the database to quickly find the rows that match a given query condition. An index can also enforce uniqueness on the indexed columns, preventing duplicate values. 
- A **clustered index** is a special type of index that determines the physical order of the rows in a table. A table can have only one clustered index, and it is usually created on the primary key column. A clustered index can improve the performance of queries that access a range of rows or that join the table with another table. 
- An **indexed view** is a view that has a clustered index created on it. An indexed view is stored in the database like a table, and it is updated whenever the underlying tables are modified. An indexed view can improve the performance of queries that use the view, because the database can use the index to access the precomputed results of the view. An indexed view has some limitations and requirements, such as the SET options and the schema binding.



### Queries and Subqueries

- A query is a request for data from a database that follows the syntax and rules of a query language, such as SQL (Structured Query Language).
- A subquery, also known as a nested query or an inner query, is a query within another query that is embedded in a clause such as WHERE, HAVING, or FROM.
- A subquery is used to return data that will be used in the main query as a condition, a source, or a value to further restrict or manipulate the data to be retrieved.
- A subquery can return a single value, a single row, a single column, or a table of values or rows.
- A subquery can be correlated or uncorrelated. A correlated subquery depends on the outer query for its values, while an uncorrelated subquery can be executed independently of the outer query.
- A subquery can be placed in various clauses of the main query, such as:

  - SELECT: A subquery in the SELECT clause returns a single value or a single column that can be used as an expression or an alias in the main query.
  - FROM: A subquery in the FROM clause returns a table of values or rows that can be used as a source or a join partner in the main query. The subquery must have an alias in this case.
  - WHERE: A subquery in the WHERE clause returns a single value, a single row, a single column, or a table of values or rows that can be used as a condition or a comparison operator in the main query.
  - HAVING: A subquery in the HAVING clause returns a single value, a single row, a single column, or a table of values or rows that can be used as a condition or a comparison operator in the main query after the GROUP BY clause.
  - IN: A subquery in the IN operator returns a single column or a table of values that can be used to check if a value exists in the subquery result set.
  - EXISTS: A subquery in the EXISTS operator returns a boolean value that indicates whether the subquery has any rows or not.
  - ANY, ALL: A subquery in the ANY or ALL operator returns a single column or a table of values that can be used to compare with a value in the main query using a comparison operator such as =, <, >, etc. The ANY operator returns true if any value in the subquery satisfies the comparison, while the ALL operator returns true if all values in the subquery satisfy the comparison.

- Some examples of subqueries are:

  - SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees); -- This query returns the name and salary of employees who earn more than the average salary of all employees. The subquery in the WHERE clause returns a single value, the average salary, that is used as a condition in the main query.
  - SELECT * FROM (SELECT name, department, salary FROM employees) AS emp_dept; -- This query returns all the columns from a subquery that returns the name, department, and salary of employees. The subquery in the FROM clause returns a table of values that is used as a source in the main query. The subquery must have an alias, emp_dept, in this case.
  - SELECT name, department FROM employees WHERE department IN (SELECT department FROM departments WHERE location = 'New York'); -- This query returns the name and department of employees who work in departments that are located in New York. The subquery in the IN operator returns a single column, the department, that is used to check if the department of the employee exists in the subquery result set.
  - SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department HAVING SUM(salary) > (SELECT MAX(total_salary) FROM (SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department) AS dept_sal); -- This query returns the department and the total salary of employees who have the highest total salary among all departments. The subquery in the HAVING clause returns a single value, the maximum total salary, that is used as a condition in the main query after the GROUP BY clause. The subquery in the MAX function returns a table of values, the department and the total salary, that is used as a source in the subquery. The subquery must have an alias, dept_sal, in this case.
  - SELECT name, salary FROM employees WHERE salary > ANY (SELECT salary FROM employees WHERE department = 'Sales'); -- This query returns the name and salary of employees who



### Aggregate Functions

- Aggregate functions are special functions in SQL that perform calculations on a set of values and return a single value.
- Aggregate functions can be used to summarize numerical data, such as finding the average, minimum, maximum, sum, or count of a column.
- Aggregate functions can also be used to combine values from different rows into a single value, such as concatenating strings or calculating checksums.
- Aggregate functions can be used with the `GROUP BY` clause to group the rows by a certain column or expression and apply the aggregate function to each group.
- Aggregate functions can also be used with the `HAVING` clause to filter the groups based on a certain condition.
- Some of the common aggregate functions in SQL are:

  - `AVG(column_name)` returns the average value of a numeric column.
  - `COUNT(column_name)` returns the number of non-null values in a column.
  - `COUNT(*)` returns the number of rows in a table or group.
  - `MAX(column_name)` returns the maximum value in a column.
  - `MIN(column_name)` returns the minimum value in a column.
  - `SUM(column_name)` returns the sum of the values in a numeric column.
  - `STRING_AGG(column_name, separator)` returns a string that concatenates the values in a column with a specified separator.
  - `CHECKSUM_AGG(column_name)` returns a checksum value that can be used to verify the integrity of the data in a column.

- Here are some examples of using aggregate functions in SQL:

  - To find the average salary of all employees:

    ```sql
    SELECT AVG(salary) FROM employees;
    ```

  - To find the number of employees in each department:

    ```sql
    SELECT department, COUNT(*) FROM employees GROUP BY department;
    ```

  - To find the highest salary in each department:

    ```sql
    SELECT department, MAX(salary) FROM employees GROUP BY department;
    ```

  - To find the total sales amount for each product:

    ```sql
    SELECT product, SUM(amount) FROM sales GROUP BY product;
    ```

  - To find the names of the products that have more than 10 sales:

    ```sql
    SELECT product FROM sales GROUP BY product HAVING COUNT(*) > 10;
    ```

  - To find the list of customers and their orders separated by commas:

    ```sql
    SELECT customer, STRING_AGG(order_id, ',') FROM orders GROUP BY customer;
    ```

  - To find the checksum value of the order_id column:

    ```sql
    SELECT CHECKSUM_AGG(order_id) FROM orders;
    ```



### Built-in functions

- Built-in functions are expressions that perform some operation using SQL keywords or special operators.
- Built-in functions can be used anywhere expressions are allowed, such as in SELECT, WHERE, GROUP BY, HAVING, ORDER BY clauses.
- Built-in functions can be categorized into different types based on their functionality and input/output data types.
- Some of the common types of built-in functions are:

  - **Aggregate functions**: These functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause to summarize data. Examples of aggregate functions are SUM, AVG, MIN, MAX, COUNT, etc.
  - **Analytic functions**: These functions compute an aggregate value based on a group of rows, but unlike aggregate functions, they do not reduce the number of rows in the result. They are often used with the OVER clause to partition the data and apply ranking, windowing, or statistical operations. Examples of analytic functions are ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, etc.
  - **String functions**: These functions manipulate character data and return a string value. They can be used to perform operations such as concatenation, extraction, conversion, comparison, searching, trimming, etc. Examples of string functions are CONCAT, SUBSTRING, UPPER, LOWER, REPLACE, CHARINDEX, etc .
  - **Numeric functions**: These functions perform mathematical operations on numeric data and return a numeric value. They can be used to perform operations such as rounding, truncating, exponentiation, logarithm, absolute value, etc. Examples of numeric functions are ROUND, FLOOR, CEILING, POWER, LOG, ABS, etc.
  - **Date and time functions**: These functions manipulate date and time data and return a date or time value. They can be used to perform operations such as extraction, addition, subtraction, conversion, formatting, etc. Examples of date and time functions are GETDATE, DATEADD, DATEDIFF, CONVERT, FORMAT, etc.
  - **Conversion functions**: These functions convert data from one data type to another data type. They can be used to perform explicit or implicit conversions, depending on the compatibility of the data types. Examples of conversion functions are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, etc.
  - **Logical functions**: These functions perform logical operations on boolean data and return a boolean value. They can be used to evaluate conditions and return true or false values. Examples of logical functions are AND, OR, NOT, IF, CASE, IIF, CHOOSE, etc.
  - **System functions**: These functions return information about the system, such as the current user, database, session, server, etc. They can be used to perform operations such as security, configuration, metadata, etc. Examples of system functions are USER, DB_NAME, SESSION_ID, @@VERSION, @@ROWCOUNT, etc.



### Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL is used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and constraints.
- DML is used to insert, update, delete, and merge data in the database tables.
- DCL is used to grant and revoke permissions and roles to users and groups for accessing and modifying the database.
- DQL is used to retrieve and manipulate data from the database tables using various clauses, operators, functions, and expressions.
- SQL follows a set of rules and syntax for writing statements and commands, which can vary slightly depending on the database system and vendor.
- SQL supports various data types, such as numeric, character, date, time, boolean, and binary, to store different kinds of data in the database tables.
- SQL supports various constraints, such as primary key, foreign key, unique, not null, check, and default, to enforce the integrity and validity of the data in the database tables.
- SQL supports various operators, such as arithmetic, comparison, logical, bitwise, and set, to perform calculations and comparisons on the data in the database tables.
- SQL supports various functions, such as aggregate, string, numeric, date, time, conversion, and analytical, to perform various operations and transformations on the data in the database tables.
- SQL supports various clauses, such as select, from, where, group by, having, order by, and limit, to specify the data to be retrieved and manipulated from the database tables.
- SQL supports various expressions, such as case, alias, subquery, join, and union, to combine and manipulate the data from multiple tables and sources in the database.
- SQL supports various commands, such as create, alter, drop, truncate, insert, update, delete, merge, grant, revoke, select, and execute, to perform various actions and operations on the database objects and data.
- SQL supports various keywords, such as distinct, all, as, in, between, like, null, and exists, to modify and refine the behavior and output of the SQL statements and commands.



### Update and Delete Operations for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- SQL is a language that allows users to view and manage data in a relational database system.
- SQL has several commands that can manipulate data, such as INSERT, UPDATE, DELETE, SELECT and MERGE. These commands are known as Data Manipulation Language (DML) statements.
- The UPDATE command is used to modify the existing records in the database. It can be used with a WHERE clause to specify which records to update.
- The syntax of the UPDATE command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The DELETE command is used to delete the records in the database that are no longer required. It can also be used with a WHERE clause to specify which records to delete.
- The syntax of the DELETE command is:

```sql
DELETE FROM table_name
WHERE condition;
```

- Some SQL best practices for deleting and updating data are:
  - Always backup the data before performing any delete or update operations.
  - Use transactions to ensure the data integrity and consistency.
  - Use the WHERE clause carefully to avoid deleting or updating the wrong records.
  - Test the delete or update statements on a sample data set before applying them to the actual data.
  - Use the ROLLBACK command to undo the changes if something goes wrong.



### Joins

- A join is a way of combining data from two or more tables based on a common column or condition.
- A join condition specifies how the tables are related, usually by comparing the values of a column in each table.
- A join can be classified into different types, depending on how the data is matched and retrieved from the tables.
- The most common types of joins are:

  - **Inner join**: This join returns only the rows that have matching values in both tables. It is the default type of join in SQL.
  - **Left outer join**: This join returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right side will have NULL values.
  - **Right outer join**: This join returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left side will have NULL values.
  - **Full outer join**: This join returns all the rows from both tables, and matches them if possible. If there is no match, both sides will have NULL values.
  - **Cross join**: This join returns the Cartesian product of the two tables, which means every row in the first table is paired with every row in the second table.
  - **Self join**: This join is used to join a table with itself, as if it were two separate tables. It is useful for comparing values within the same table.

- The syntax for a join in SQL is:

  ```sql
  SELECT column_list
  FROM table1
  JOIN table2
  ON join_condition;
  ```

- The join condition can be any logical expression that evaluates to true or false. It is usually based on the equality of a column in each table, but it can also use other operators or functions.
- The join type can be specified using the keywords INNER, LEFT OUTER, RIGHT OUTER, FULL OUTER, or CROSS before the word JOIN. If no join type is specified, it is assumed to be an inner join.
- The column list can include columns from both tables, or use aliases to rename them. It can also use aggregate functions or expressions to perform calculations on the data.
- The order of the tables in the join does not affect the result, unless the join type is left or right. In that case, the first table is considered the left table, and the second table is considered the right table.
- The join can be combined with other clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, or LIMIT, to filter, group, or sort the data.



### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union removes any duplicate rows from the combined result set.
- A union requires that the number, name, and data type of the columns in the SELECT queries are the same or compatible.
- A union can be used to combine data from different tables or views that have a similar structure or meaning.
- A union can be written as:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION
SELECT column1, column2, ..., columnN FROM table2
UNION
...
UNION
SELECT column1, column2, ..., columnN FROM tableN;
```

- A union can also be modified with the ALL keyword to include duplicate rows in the result set. This can be written as:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION ALL
SELECT column1, column2, ..., columnN FROM table2
UNION ALL
...
UNION ALL
SELECT column1, column2, ..., columnN FROM tableN;
```

- A union can be used to perform various tasks, such as:

  - Combining data from different sources or databases
  - Creating a summary report from multiple tables or views
  - Performing set operations such as intersection, difference, or union
  - Simplifying complex queries by breaking them into smaller parts
  - Enhancing query performance by reducing the number of joins or subqueries

- A union can be combined with other SQL clauses, such as ORDER BY, GROUP BY, HAVING, or WHERE, to further manipulate the result set. However, these clauses must be applied to the entire union, not to individual SELECT queries. For example:

```sql
SELECT name, salary FROM employees
UNION
SELECT name, income FROM freelancers
ORDER BY salary DESC;
```

- A union is different from a join, which compares columns from two tables to create result rows composed of columns from both tables. A union does not create individual rows from columns gathered from two tables, but concatenates result sets from two queries. For example:

```sql
-- This is a join
SELECT e.name, e.department, d.location FROM employees e
JOIN departments d ON e.department = d.name;

-- This is a union
SELECT name, department FROM employees
UNION
SELECT name, location FROM departments;
```

- A union is also different from a subquery, which is a query nested inside another query. A union is a set operator that combines multiple queries, while a subquery is a query component that can be used in various places, such as in the SELECT, FROM, or WHERE clauses. For example:

```sql
-- This is a subquery
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- This is a union
SELECT name, salary FROM employees
UNION
SELECT name, income FROM freelancers;
```

- A union is a powerful and versatile SQL operator that can be used to combine data from different sources, perform set operations, simplify complex queries, and enhance query performance. It is important to understand the syntax and rules of a union, as well as the differences between a union and other SQL concepts, such as joins and subqueries.



### Intersection

- The intersection operation in SQL is used to combine two queries and return only the records that are common to both the queries.
- The syntax of the intersection operation is:

```sql
SELECT column_list
FROM table1
INTERSECT
SELECT column_list
FROM table2;
```

- The column_list in both the queries must have the same number and order of columns, and the data types must be compatible.
- The intersection operation eliminates any duplicate rows from the result set.
- The intersection operation can be used to find the common values in two or more tables. For example, to find the customers who have ordered both books and DVDs from an online store, we can use the following query:

```sql
SELECT customer_id
FROM orders
WHERE product_type = 'book'
INTERSECT
SELECT customer_id
FROM orders
WHERE product_type = 'DVD';
```

- The intersection operation can also be combined with other set operations, such as union and except, using parentheses to specify the order of execution. For example, to find the customers who have ordered books or DVDs, but not both, we can use the following query:

```sql
(SELECT customer_id
FROM orders
WHERE product_type = 'book'
UNION
SELECT customer_id
FROM orders
WHERE product_type = 'DVD')
EXCEPT
(SELECT customer_id
FROM orders
WHERE product_type = 'book'
INTERSECT
SELECT customer_id
FROM orders
WHERE product_type = 'DVD');
```



### Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several types of statements, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- DDL statements are used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, or constraints.
- DML statements are used to insert, update, delete, or merge data in the database tables or views.
- DCL statements are used to grant or revoke permissions and privileges to users or roles on the database objects or operations.
- DQL statements are used to retrieve data from the database tables or views, using various clauses, operators, functions, and expressions.
- SQL supports various data types, such as numeric, character, date, time, interval, boolean, binary, etc.
- SQL supports various constraints, such as primary key, foreign key, unique, not null, check, default, etc., to enforce the integrity and validity of the data.
- SQL supports various operators, such as arithmetic, comparison, logical, bitwise, set, etc., to perform calculations, comparisons, and logical operations on the data.
- SQL supports various functions, such as aggregate, scalar, window, string, numeric, date, time, etc., to perform various operations and transformations on the data.
- SQL supports various clauses, such as select, from, where, group by, having, order by, limit, offset, etc., to specify the data source, filter, aggregate, sort, and limit the data in the query result.
- SQL supports various expressions, such as case, subquery, join, union, intersect, except, etc., to combine, compare, or manipulate the data from multiple tables or queries.
- SQL supports various keywords, such as distinct, all, as, alias, in, between, like, null, is, exists, etc., to modify or qualify the data in the query result.



### Transaction Control Commands

- Transaction Control Language (TCL) is a subset of SQL that is used to manage transactions in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the statements in a transaction are executed successfully or none of them are executed at all.
- Consistency means that a transaction preserves the integrity of the database and does not violate any constraints or rules.
- Isolation means that a transaction is not affected by the concurrent execution of other transactions and does not interfere with them.
- Durability means that the effects of a transaction are permanent and persist even in the event of a system failure or power outage.
- The following commands are used to control transactions in SQL:
  - **COMMIT**: This command is used to make a transaction permanent in the database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK**: This command is used to undo the changes made by the transaction and restore the database to its previous state before the transaction started. It aborts the current transaction and discards any changes made by it.
  - **SAVEPOINT**: This command is used to create points within a transaction that can be used to roll back to a specific state in case of an error or failure. It allows partial undo of a transaction.
  - **SET TRANSACTION**: This command is used to specify the characteristics of a transaction, such as its isolation level, name, or read-only status. It must be executed before any other SQL statement in the transaction.



## Unit 6 - PL/SQL

- PL/SQL stands for Procedural Language extensions to the Structured Query Language.
- SQL is a popular language for both querying and updating data in the relational database management systems (RDBMS).
- PL/SQL is a combination of SQL along with the procedural features of programming languages.
- PL/SQL is one of three key programming languages embedded in the Oracle Database, along with SQL itself and Java.
- PL/SQL allows you to create stored procedures, functions, triggers, packages, and other database objects.
- PL/SQL also supports features such as variables, constants, arrays, collections, loops, conditional statements, exception handling, and cursors.
- PL/SQL programs are composed of blocks, which have a structure of declaration, execution, and exception sections.
- PL/SQL programs can be executed by the Oracle Database server or by a client application.
- PL/SQL programs can interact with SQL statements by using bind variables, placeholders, and dynamic SQL.
- PL/SQL programs can improve the performance and security of database applications by reducing the network traffic and enforcing access control.



### Introduction for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that allows users to write procedural code in a database environment.
- PL/SQL is a block-structured language that consists of statements, expressions, variables, constants, data types, operators, control structures, exceptions, cursors, and subprograms.
- PL/SQL supports features such as modularity, encapsulation, abstraction, and reusability. It also provides error handling and security mechanisms.
- PL/SQL can be used to create and execute stored procedures, functions, triggers, and packages in a database. These are reusable units of code that can perform complex tasks and improve performance and maintainability.
- PL/SQL can also be used to embed SQL statements in a procedural program, and to manipulate data using cursors and collections. These are data structures that allow users to access and manipulate multiple rows of data in a single operation.
- PL/SQL can interact with other programming languages such as Java, C, and C++. It can also use external libraries and call external procedures.
- PL/SQL is supported by Oracle and other relational database management systems that follow the SQL standard. It is widely used for developing database applications and business logic.



### Features of PL/SQL

- PL/SQL is a **procedural language** that extends the capabilities of SQL by adding features such as variables, control structures, loops, exceptions, and subprograms .
- PL/SQL is **tightly integrated** with SQL, which means that you can use SQL statements and functions within PL/SQL blocks, and pass data between SQL and PL/SQL easily  .
- PL/SQL offers **extensive error checking** and debugging tools, such as the PL/SQL compiler, the PL/SQL debugger, and the PL/SQL warnings  .
- PL/SQL offers **numerous data types**, including scalar, composite, reference, and large object (LOB) types, as well as user-defined types and collections  .
- PL/SQL supports **structured programming** through functions and procedures, which can be stored in the database as schema objects and reused by other applications  .
- PL/SQL supports **object-oriented programming** by allowing you to create and manipulate objects, such as tables, views, types, and methods  .
- PL/SQL supports the development of **web applications and server pages** by providing features such as native dynamic SQL, the UTL_HTTP package, and the PL/SQL gateway  .
- PL/SQL is **portable** and **secure**, as it runs on any platform that supports Oracle Database, and it can protect sensitive data and code from unauthorized access  .



### Syntax and Constructs for the Notes of the Unit 6 - PL/SQL in the Subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that adds procedural features to the relational database language.
- PL/SQL allows users to define and execute blocks of code that can manipulate data, handle exceptions, create variables, constants, cursors, procedures, functions, triggers, and packages .
- The basic unit of PL/SQL is a block, which consists of three sections: declaration, execution, and exception. The declaration section is optional and defines the variables, constants, cursors, and user-defined exceptions. The execution section is mandatory and contains the executable statements that perform the logic of the block. The exception section is optional and handles the errors that may occur during the execution of the block.
- The syntax of a PL/SQL block is as follows:

```
DECLARE
  --optional declarations
BEGIN
  --mandatory executable statements
EXCEPTION
  --optional exception handlers
END;
/
```

- PL/SQL supports many data types, such as scalar, composite, reference, and large object (LOB) types. Scalar types include numeric, character, boolean, and date types. Composite types include record and collection types. Reference types include cursor and REF CURSOR types. LOB types include BLOB, CLOB, NCLOB, and BFILE types.
- PL/SQL identifiers are names of constants, variables, exceptions, procedures, cursors, and reserved words. They must start with a letter and can be followed by letters, numerals, dollar signs, underscores, and number signs. They cannot exceed 30 characters in length.
- PL/SQL supports many operators, such as arithmetic, comparison, logical, set, and string operators. They are used to perform calculations, comparisons, and manipulations on data values.
- PL/SQL supports many control structures, such as conditional, iterative, and sequential structures. They are used to control the flow of execution of the block. Conditional structures include IF-THEN-ELSE, CASE, and NULL statements. Iterative structures include LOOP, WHILE-LOOP, FOR-LOOP, and EXIT statements. Sequential structures include GOTO and NULL statements.
- PL/SQL supports many SQL statements, such as SELECT, INSERT, UPDATE, DELETE, MERGE, and CALL statements. They are used to query and modify data in the database. PL/SQL also supports some SQL clauses, such as INTO, VALUES, and RETURNING clauses. They are used to assign query results to variables, specify values for insert or update operations, and return values from DML statements.
- PL/SQL supports many built-in functions, such as character, numeric, date, conversion, and miscellaneous functions. They are used to perform various operations on data values, such as formatting, manipulation, calculation, and conversion.
- PL/SQL supports many built-in packages, such as DBMS_OUTPUT, UTL_FILE, DBMS_SQL, and DBMS_JOB packages. They are used to perform various tasks, such as displaying output, reading and writing files, executing dynamic SQL, and scheduling jobs.



### SQL within PL/SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- PL/SQL stands for Procedural Language/Structured Query Language, which is an extension of SQL that allows developers to write procedural code using SQL statements within its syntax .
- PL/SQL programs are composed of blocks, which are the basic units of execution. A block can contain declarations, executable statements, and exception handlers .
- PL/SQL blocks can be nested within each other, creating subprograms, functions, procedures, triggers, and packages .
- PL/SQL blocks can be compiled by the Oracle Database server and stored inside the database, or they can be executed dynamically using the EXECUTE IMMEDIATE statement or the DBMS_SQL package .
- PL/SQL blocks can interact with SQL statements in two ways: static SQL and dynamic SQL.
  - Static SQL is when the SQL statements are known at compile time and embedded within the PL/SQL block. Static SQL can use bind variables, which are placeholders for values that are supplied at run time.
  - Dynamic SQL is when the SQL statements are constructed at run time and executed using the EXECUTE IMMEDIATE statement or the DBMS_SQL package. Dynamic SQL can execute any SQL statement, including DDL (Data Definition Language) and DCL (Data Control Language) statements.
- PL/SQL blocks can also use cursor variables, which are pointers to result sets of SQL queries. Cursor variables can be passed as parameters to subprograms, allowing for modular and reusable code.
- PL/SQL blocks can output the results of SQL queries using the DBMS_OUTPUT package, which provides procedures for printing messages to the standard output device or a buffer. Alternatively, PL/SQL blocks can return the results of SQL queries using the PIPE ROW statement, which sends a row of data to a pipelined table function.



### DML in PL/SQL

- DML stands for Data Manipulation Language. It is a subset of SQL that is used to manipulate data in tables and views .
- DML statements can be executed from within any PL/SQL block of code, as long as the user has access to the schema objects.
- The main types of DML statements are:
  - INSERT: used to insert new rows into a table or view .
  - UPDATE: used to modify existing rows in a table or view .
  - DELETE: used to remove existing rows from a table or view .
  - MERGE: used to combine the data from two tables or views based on a matching condition .
- DML statements can be used with variables, expressions, conditions, and subqueries to perform complex data manipulation operations .
- DML statements do not implicitly commit the current transaction, meaning that the changes made by them are not permanent until the user explicitly commits or rolls back the transaction.
- DML statements can be used with the RETURNING clause to return the values of the affected rows after the execution .
- DML statements can raise exceptions if they encounter errors or violations of constraints during the execution.
- DML statements can be combined with PL/SQL control structures, such as loops, conditional statements, and exception handlers, to create more dynamic and flexible programs.



### Cursors

A cursor is a pointer to a result set, or the data that results from a query. Cursors let you fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.

There are two types of cursors in PL/SQL: implicit and explicit.

- Implicit cursors are automatically created by Oracle whenever an SQL statement is executed. You can access the attributes of an implicit cursor using the SQL prefix. For example, SQL%ROWCOUNT returns the number of rows affected by the last SQL statement.
- Explicit cursors are user-defined cursors that allow you to name and control the result set of a query. You can declare, open, fetch, and close an explicit cursor using PL/SQL statements. You can also define parameters for an explicit cursor and use them in the query.

Some advantages of using explicit cursors are:

- You can fetch the rows of the result set one by one or in bulk.
- You can perform complex logic on each row of the result set.
- You can use the same query with different parameters to get different result sets.
- You can handle exceptions that may occur during the execution of the query.

Some examples of explicit cursor declarations are:

- `DECLARE CURSOR c_emp IS SELECT * FROM employees;` -- This declares a cursor named c_emp that selects all rows from the employees table.
- `DECLARE CURSOR c_dept (p_deptno NUMBER) IS SELECT * FROM departments WHERE department_id = p_deptno;` -- This declares a cursor named c_dept that takes a parameter p_deptno and selects all rows from the departments table where the department_id matches the parameter value.
- `DECLARE CURSOR c_sal IS SELECT last_name, salary FROM employees FOR UPDATE;` -- This declares a cursor named c_sal that selects the last_name and salary columns from the employees table and locks the rows for update.



### Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database catalog .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to the procedure. The body contains the declarative, executable, and exception-handling parts of the procedure .
- A stored procedure can be created using the CREATE PROCEDURE statement, which has the following syntax :

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
  (parameter1 [IN|OUT|IN OUT] parameter_type1,
   parameter2 [IN|OUT|IN OUT] parameter_type2,
   ...
   parameterN [IN|OUT|IN OUT] parameter_typeN)
IS
  -- declarative part
  -- variables, constants, cursors, exceptions, etc.
BEGIN
  -- executable part
  -- SQL statements and PL/SQL code
EXCEPTION
  -- exception-handling part
  -- actions to handle errors
END;
```

- A stored procedure can be executed using the EXECUTE or EXEC command, which has the following syntax :

```sql
EXECUTE schema.procedure_name(parameter1, parameter2, ..., parameterN);
```

- A stored procedure can be dropped using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE schema.procedure_name;
```



### Stored function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement or another PL/SQL block .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function has the following syntax :

```sql
CREATE [ OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
[declarative section]
BEGIN
[executable section]
RETURN expression;
END [function_name];
```

- The parameter_list consists of zero or more parameters, each with a name, a data type, and an optional mode (IN, OUT, or IN OUT) .
- The return_type specifies the data type of the value that the function returns .
- The declarative section declares the variables, constants, cursors, or exceptions that are used by the function .
- The executable section contains the statements that define the logic of the function .
- The RETURN statement specifies the expression that evaluates to the value that the function returns .
- The function_name at the end of the block is optional and can be used to improve readability .
- A stored function can be executed by using the function name followed by the argument list in parentheses .
- A stored function can be used in a SQL statement wherever an expression of the same data type is allowed .
- A stored function can also be used in another PL/SQL block by assigning its return value to a variable or using it in an expression .



### Database Triggers

- A database trigger is a special stored procedure that is run when specific actions occur within a database.
- Most triggers are defined to run when changes are made to a table’s data. Triggers can be defined to run instead of or after DML (Data Manipulation Language) actions such as INSERT, UPDATE, and DELETE.
- A database trigger is procedural code that is automatically executed in response to certain events on a particular table or view in a database.
- The trigger is mostly used for maintaining the integrity of the information on the database.
- Database triggers are defined on a table, stored in the associated database, and executed as a result of an INSERT, UPDATE, or DELETE statement being issued against a table, no matter which user or application issues the statement.
- Database triggers can be used to implement complex data interactions, such as auditing, logging, validation, or synchronization.
- SQL Server lets you create multiple triggers for each DML, DDL, or LOGON event. For example, if you have two DML triggers for a table, both will fire when an INSERT, UPDATE, or DELETE statement is issued against the table.
- DDL triggers are a special kind of trigger that fire in response to Data Definition Language (DDL) statements. They can be used to perform administrative tasks, such as auditing and regulating database operations.



### Indices for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

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
- PL/SQL Cursors and Exceptions
  - What are cursors and why use them?
  - Types of cursors (implicit, explicit, parameterized, ref cursors)
  - Cursor attributes and operations
  - What are exceptions and why handle them?
  - Types of exceptions (predefined, user-defined, unnamed)
  - Exception propagation and scope
  - Exception handlers and statements (RAISE, RAISE_APPLICATION_ERROR)
- PL/SQL Subprograms
  - What are subprograms and why use them?
  - Types of subprograms (procedures, functions, packages)
  - Subprogram parameters and modes (IN, OUT, IN OUT, NOCOPY)
  - Subprogram overloading and resolution
  - Subprogram invocation and execution
  - Subprogram scope and visibility
- PL/SQL Triggers
  - What are triggers and why use them?
  - Types of triggers (row, statement, DML, instead-of, system)
  - Trigger attributes and operations
  - Trigger restrictions and guidelines
  - Trigger enabling and disabling
  - Trigger mutating table error and solutions
- PL/SQL Collections and Records
  - What are collections and records and why use them?
  - Types of collections (associative arrays, nested tables, varrays)
  - Collection methods and operations
  - Collection bulk binding and performance
  - What are records and how to define them?
  - Record operations and attributes
  - Record comparison and assignment



## Unit 7 - Transaction Processing Concepts

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has four main properties: **atomicity**, **consistency**, **isolation**, and **durability** (ACID).
- **Atomicity** means that a transaction either completes all of its operations or none of them. If a transaction fails, the database is restored to its state before the transaction started.
- **Consistency** means that a transaction preserves the integrity constraints of the database. A transaction can only bring the database from one valid state to another valid state.
- **Isolation** means that a transaction executes as if it were the only transaction in the system. The intermediate results of a transaction are not visible to other transactions, and a transaction does not see the effects of other transactions that are executed concurrently.
- **Durability** means that the effects of a committed transaction are permanent and will not be lost in the event of a system failure.
- Transaction processing systems are systems that support large-scale, concurrent, and reliable execution of transactions on a database. They use various techniques such as locking, logging, recovery, and concurrency control to ensure the ACID properties of transactions.



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

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four main properties, collectively known as ACID, that ensure the reliability and correctness of the database operations.
- The four properties are:

  - **Atomicity**: This means that a transaction is either executed completely or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state before the transaction started.
  - **Consistency**: This means that a transaction must preserve the integrity constraints and business rules of the database. A transaction cannot leave the database in an inconsistent state, such as violating a primary key or a foreign key constraint.
  - **Isolation**: This means that a transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only transaction in the system. The intermediate results of a transaction are not visible to other transactions until the transaction commits.
  - **Durability**: This means that the effects of a committed transaction are permanent and persist even in the case of system failures. The database system must ensure that the committed data is not lost or corrupted by using recovery techniques such as logging and checkpointing.



### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the same outcome as if the transactions were executed serially, one after the other.
- Serializability is important for maintaining the consistency and correctness of a database in a concurrent environment.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that preserves the order of conflicting operations (read-write, write-read, write-write) between transactions.
- View serializability is a weaker form of serializability that preserves the final state of the database and the read-write dependencies between transactions.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- There are two techniques to test serializability: serialization graph and precedence graph.
- A serialization graph is a directed graph of the entire transactions of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions.
- A precedence graph is a subset of the serialization graph that only contains the edges that indicate the order of conflicting operations between transactions.
- A schedule is conflict serializable if and only if its serialization graph or precedence graph is acyclic, meaning that it does not contain any cycles.
- A schedule is view serializable if and only if it is view equivalent to a serial schedule, meaning that it produces the same final state of the database and the same read-write dependencies as a serial schedule.
- View serializability can be tested by checking the following three conditions for each transaction in the schedule:
  - Initial read condition: the transaction reads the initial value of a data item if and only if no other transaction writes to that data item before it in the serial schedule.
  - Final write condition: the transaction writes the final value of a data item if and only if no other transaction writes to that data item after it in the serial schedule.
  - Read-write dependency condition: the transaction reads the value of a data item written by another transaction if and only if the other transaction precedes it in the serial schedule.
- If all three conditions are satisfied for all transactions in the schedule, then the schedule is view serializable. Otherwise, it is not view serializable.



### Serializability of schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- Serializability is a property of a schedule that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one after the other without any overlap in time.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a type of serializability where two schedules are equivalent if they have the same order of conflicting operations, where a conflict is a pair of operations from different transactions that access the same data item and at least one of them is a write operation.
- View serializability is a type of serializability where two schedules are equivalent if they have the same view of the database, which means that they read the same initial values, write the same final values, and read the same values written by other transactions.
- Serializability is important for concurrency control, which is the mechanism that ensures the isolation and atomicity of transactions in a database system.
- Serializability can be checked by using a precedence graph, which is a directed graph that represents the dependencies between transactions based on their conflicting operations. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- Serializability can also be enforced by using locking protocols, which are rules that govern when and how transactions can acquire and release locks on data items. A locking protocol is said to be conflict serializable if it guarantees that any schedule generated by it is conflict serializable.
- Serializability is the highest level of isolation that can be provided by a database system, but it may also incur a high cost in terms of performance and concurrency. Therefore, some database systems may allow lower levels of isolation that trade off serializability for efficiency, such as read committed, repeatable read, and snapshot isolation.



### Conflict and View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions, which may lead to inconsistency or anomalies in the database.
- Serializability is the property of a schedule that ensures the same outcome as a serial schedule, regardless of the order of operations.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be conflicting if all conditions satisfy:
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

- The schedule S is conflict serializable because it can be transformed into a serial schedule S' by swapping the non-conflicting operations R(B) and W(B) of T1 with R(B) and W(B) of T2:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
|     | R(B) |
|     | W(B) |

- The schedule S' is equivalent to the serial schedule T1 -> T2.

#### View Serializability

- A schedule is view serializable if it is view equivalent to a serial schedule, meaning that it preserves the following conditions:
  - The same transaction reads the initial value of each data item
  - The same transaction writes the final value of each data item
  - The same transaction reads the value of each data item that has been written by another transaction
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(A) |
|     | W(A) |
| R(B) |    |
| W(B) |    |

- The schedule S is view serializable because it is view equivalent to the serial schedule T2 -> T1, which satisfies the following conditions:
  - T1 reads the initial value of B
  - T2 reads the initial value of A
  - T2 writes the final value of A
  - T1 writes the final value of B
  - T2 reads the value of A written by T1
- Note that the schedule S is not conflict serializable because it cannot be transformed into a serial schedule by swapping non-conflicting operations, as all the operations are conflicting.



### Recoverability

- Recoverability is the ability of a database system to restore the database to a consistent state after a failure or an abort of a transaction.
- A transaction is a logical unit of work that consists of a sequence of operations on the database, such as read, write, insert, delete, etc.
- A transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints and business rules of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failure.
- A failure is any event that causes the database system to stop normal operation, such as power outage, disk crash, software bug, etc.
- An abort is the intentional termination of a transaction before it commits, usually due to some error or violation of a constraint.
- A recovery mechanism is a component of the database system that ensures recoverability by restoring the database to a consistent state after a failure or an abort.
- A recovery mechanism typically uses a combination of the following techniques:
  - Logging: recording the changes made by transactions in a persistent log file before applying them to the database.
  - Checkpointing: periodically writing the contents of the main memory buffers to the disk to reduce the amount of work to be done during recovery.
  - Undoing: reversing the effects of uncommitted transactions that may have left the database in an inconsistent state.
  - Redoing: reapplying the effects of committed transactions that may have been lost due to a failure.
- A recovery mechanism must ensure that the following properties are satisfied:
  - No committed transaction is lost: the effects of any transaction that committed before the failure are reflected in the database after the recovery.
  - No uncommitted transaction is reflected: the effects of any transaction that did not commit before the failure are not reflected in the database after the recovery.
  - No cascading aborts: the abort of one transaction does not cause the abort of another transaction that may have read some data written by the first transaction.



### Recovery from transaction failures

- A transaction failure is an event that causes a transaction to abort or terminate before it can commit its changes to the database.
- A transaction failure can be caused by various reasons, such as system failure, user error, deadlock, concurrency control violation, or integrity constraint violation.
- When a transaction failure occurs, the database may be left in an inconsistent state, meaning that some of the changes made by the transaction may have been applied to the database, while others may not have been applied.
- To ensure the consistency and integrity of the database, the DBMS must perform recovery from transaction failures, which is the process of restoring the database to a consistent state that existed before the transaction failure.
- There are two main types of recovery techniques used in DBMS:
  - Rollback/Undo recovery technique: This technique is based on the principle of undoing the effects of a transaction that has not completed successfully. It uses the information stored in the log file, which records the history of all the transactions and their actions, to undo the changes made by the transaction to the database. This technique is also known as backward recovery.
  - Rollforward/Redo recovery technique: This technique is based on the principle of redoing the effects of a transaction that has committed successfully. It uses the information stored in the log file, which records the history of all the transactions and their actions, to redo the changes made by the transaction to the database. This technique is also known as forward recovery.
- Depending on the type of failure, the DBMS may use either one or both of these techniques to recover from transaction failures. For example, if the failure occurs due to a system crash, the DBMS may use both rollback and rollforward techniques to recover the database. If the failure occurs due to a user error, the DBMS may use only rollback technique to recover the database.
- In a partitioned database environment, where the database is distributed across multiple servers, the recovery from transaction failures may involve more than one server. If a transaction failure occurs on one server, the DBMS may need to recover the database on both the failed server and any other server that was participating in the transaction . This may require coordination and communication among the servers to ensure the consistency and integrity of the database.



### Two-phase commit protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort (roll back) the transaction. It ensures that either all the changes are committed or none of them are, even in the case of site failures and message losses.

The protocol involves two phases:

- **Phase 1: Prepare phase**. The coordinator (Ci) of the transaction (T) sends a Prepare T message to all the sites where T executed, and places a log record <Prepare T> on its site. Each site that receives the message decides whether to commit or abort T locally, and sends its vote to the coordinator. If the site votes to commit, it also writes a log record <Ready T> and waits for the coordinator's decision. If the site votes to abort, it writes a log record <Abort T> and undoes the changes of T.

- **Phase 2: Commit phase**. The coordinator collects the votes from all the sites. If all the sites voted to commit, the coordinator decides to commit T globally, and writes a log record <Commit T> on its site. It then sends a Commit T message to all the sites that voted to commit. Each site that receives the message writes a log record <Commit T> and makes the changes of T permanent. If any site voted to abort, or the coordinator did not receive a vote from some site, the coordinator decides to abort T globally, and writes a log record <Abort T> on its site. It then sends an Abort T message to all the sites that voted to commit. Each site that receives the message writes a log record <Abort T> and undoes the changes of T.

The two-phase commit protocol is a blocking protocol; the failure of a single node blocks progress until the node recovers. Moreover, if the coordinator fails, then the database is left in an inconsistent state and only recovers once the coordinator recovers. This leads to another drawback as the protocol’s latency depends on the slowest node.



### Log Based Recovery in DBMS

- Log based recovery is a technique used in DBMS to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: a unique identifier for each transaction
  - Operation: the type of operation performed by the transaction, such as read, write, commit, abort, etc.
  - Data item: the name of the data item affected by the operation
  - Old value: the value of the data item before the operation
  - New value: the value of the data item after the operation
- A log record is written to a stable storage device before the actual operation is performed on the database. This is called write-ahead logging (WAL) principle.
- A log record is also written when a transaction starts or ends  . For example, <T1, Start> indicates that transaction T1 has started, and <T1, Commit> indicates that transaction T1 has committed.
- Log based recovery can be classified into two types:
  - Undo logging: this type of logging ensures that all the changes made by an uncommitted transaction are undone in case of a failure. It uses the old values stored in the log records to restore the database to its previous state.
  - Redo logging: this type of logging ensures that all the changes made by a committed transaction are redone in case of a failure. It uses the new values stored in the log records to reapply the operations on the database.
- Log based recovery can also use a combination of undo and redo logging, depending on the type of failure and the state of the transactions.
- Log based recovery requires the use of checkpoints, which are points in time when the database and the log are synchronized. A checkpoint record is written to the log to indicate that all the transactions before the checkpoint have committed and their changes have been written to the database. Checkpoints reduce the amount of work required for recovery by limiting the number of log records that need to be scanned.



### Checkpoints for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

- Define the concept of a transaction, which is a logical unit of database processing that consists of a set of operations on data objects (such as tuples, relations, files, etc.) .
- Explain the properties of transactions, which are atomicity, consistency, isolation, and durability (ACID). Atomicity means that a transaction either executes all or none of its operations. Consistency means that a transaction preserves the integrity constraints of the database. Isolation means that a transaction does not interfere with other concurrent transactions. Durability means that the effects of a transaction are permanent even in the case of failures  .
- Describe the types of failures that can occur in a transaction processing system, such as transaction failures, system failures, media failures, and network failures. Transaction failures are caused by logical errors or user aborts. System failures are caused by hardware or software errors that affect the main memory or the CPU. Media failures are caused by physical damage to the secondary storage devices. Network failures are caused by communication problems between the components of a distributed system .
- Discuss the methods for recovery from failures, such as undo logging, redo logging, and shadow paging. Undo logging records the before images of the data objects that are modified by a transaction, and uses them to restore the database to a consistent state in case of a failure. Redo logging records the after images of the data objects that are modified by a transaction, and uses them to reapply the changes in case of a failure. Shadow paging maintains two copies of each page in the database, one for the current state and one for the previous state, and switches between them in case of a failure .
- Explain the concept of concurrency control, which is the process of managing the simultaneous execution of transactions in a shared database, to ensure the serializability and correctness of the transactions  .
- Compare the different techniques for concurrency control, such as locking, timestamping, validation, and multiversion. Locking is a mechanism that grants exclusive access to a data object to a transaction, and prevents other transactions from accessing or modifying it. Timestamping is a mechanism that assigns a unique identifier to each transaction, and uses it to order the operations on the data objects. Validation is a mechanism that checks the consistency of the transactions before committing them to the database. Multiversion is a mechanism that maintains multiple versions of each data object, and allows transactions to access the appropriate version based on their timestamps  .
- Summarize the challenges and benefits of transaction processing in a distributed system, such as increased availability, performance, scalability, and reliability, as well as increased complexity, overhead, and security risks .



### Deadlock Handling

- A deadlock is a situation where a set of transactions are blocked, waiting for each other to release locks on the data items they need.
- A deadlock can occur when two or more transactions request locks on the same data items in a conflicting mode, such as exclusive or shared.
- A deadlock can also occur when transactions hold locks on multiple data items and request more locks in a circular manner, such as T1 holds a lock on A and requests a lock on B, while T2 holds a lock on B and requests a lock on A.
- Deadlocks are undesirable because they waste system resources and reduce concurrency and throughput.
- There are three main methods to handle deadlocks: prevention, avoidance, and detection and recovery.

#### Deadlock Prevention

- Deadlock prevention is a technique that ensures that deadlocks never occur by imposing some restrictions on how transactions can acquire locks.
- One common method of deadlock prevention is to use a **timestamp ordering** protocol, which assigns a unique timestamp to each transaction when it starts, and uses the timestamps to order the lock requests.
- Another common method of deadlock prevention is to use a **wait-die** or **wound-wait** protocol, which compares the timestamps of the requesting and holding transactions, and either aborts or delays the requesting transaction based on the comparison.
- Deadlock prevention has the advantage of simplicity and low overhead, but it may also cause unnecessary aborts or delays, and reduce concurrency and performance.

#### Deadlock Avoidance

- Deadlock avoidance is a technique that allows transactions to acquire locks dynamically, but avoids granting a lock request that may lead to a deadlock in the future.
- One common method of deadlock avoidance is to use a **wait-for graph**, which is a directed graph that represents the waiting relationships among transactions. A node in the graph is a transaction, and an edge from Ti to Tj means that Ti is waiting for Tj to release a lock.
- The system maintains the wait-for graph and checks for cycles whenever a lock request is made. If granting a lock request would create a cycle in the graph, the system denies the request and makes the transaction wait.
- Deadlock avoidance has the advantage of allowing more concurrency and flexibility than deadlock prevention, but it also requires more overhead and complexity to maintain and check the wait-for graph.

#### Deadlock Detection and Recovery

- Deadlock detection and recovery is a technique that allows transactions to acquire locks freely, but periodically checks for the existence of deadlocks and takes actions to resolve them.
- One common method of deadlock detection is to use a **timeout** mechanism, which sets a limit on how long a transaction can wait for a lock. If the limit is exceeded, the system assumes that the transaction is involved in a deadlock and aborts it.
- Another common method of deadlock detection is to use a **wait-for graph**, as in deadlock avoidance, but only construct and check the graph periodically, rather than for every lock request.
- Deadlock detection and recovery has the advantage of allowing the maximum concurrency and simplicity, but it also has the disadvantage of wasting system resources and causing cascading aborts when deadlocks occur.



## Unit 8 - Concurrency Control Techniques

- Concurrency control techniques are methods to ensure the correctness and consistency of data in a database system when multiple transactions are executed concurrently.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by the transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and timestamp-based concurrency control.
- Concurrency control techniques can also be classified based on the level of data abstraction they operate on: record-level, page-level, or file-level.
- Record-level concurrency control techniques lock individual records or tuples in the database. They provide the finest granularity of locking and the highest degree of concurrency, but also incur the highest overhead of locking and unlocking operations.
- Page-level concurrency control techniques lock entire pages or blocks of records in the database. They provide a coarser granularity of locking and a lower degree of concurrency, but also reduce the overhead of locking and unlocking operations.
- File-level concurrency control techniques lock entire files or tables in the database. They provide the coarsest granularity of locking and the lowest degree of concurrency, but also eliminate the overhead of locking and unlocking operations.



### Concurrency control

Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating the data integrity of the database   .

Concurrency control techniques can be classified into two categories: lock-based protocols and timestamp-based protocols.

#### Lock-based protocols

Lock-based protocols use locks to prevent multiple transactions from accessing the same data item at the same time. A lock is a mechanism that grants or denies access to a data item based on its state. There are two types of locks: shared locks and exclusive locks.

- A shared lock (S-lock) allows a transaction to read a data item, but not to modify it. Multiple transactions can hold shared locks on the same data item concurrently.
- An exclusive lock (X-lock) allows a transaction to read and modify a data item, but not to share it with other transactions. Only one transaction can hold an exclusive lock on a data item at a time.

A transaction must acquire the appropriate lock before accessing a data item, and release the lock after finishing the access. A lock manager is responsible for granting, denying, and releasing locks according to some rules. Some of the common lock-based protocols are:

- Two-phase locking (2PL): A transaction must acquire all the locks it needs before releasing any lock. This ensures that the transaction is serializable, meaning that its effect is equivalent to executing it alone in some order. However, 2PL may cause deadlocks, where two or more transactions are waiting for each other to release locks.
- Strict two-phase locking (Strict 2PL): A transaction must hold all its exclusive locks until it commits or aborts. This ensures that the transaction is recoverable, meaning that its changes are not overwritten by another transaction before it commits. Strict 2PL also prevents cascading aborts, where one transaction aborts and causes other transactions to abort as well.
- Conservative two-phase locking (Conservative 2PL): A transaction must acquire all the locks it needs before it starts execution. This ensures that the transaction is deadlock-free, meaning that it does not wait for any lock during its execution. However, conservative 2PL may cause low concurrency, where some transactions are delayed or rejected unnecessarily.

#### Timestamp-based protocols

Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that reflects the start time of a transaction. Each transaction is assigned a timestamp when it begins, and each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS).

- The read timestamp (RTS) of a data item is the largest timestamp of any transaction that has successfully read the data item.
- The write timestamp (WTS) of a data item is the largest timestamp of any transaction that has successfully written the data item.

A transaction must compare its timestamp with the timestamps of the data item before accessing it, and follow some rules to ensure serializability and recoverability. Some of the common timestamp-based protocols are:

- Basic timestamp ordering (BTO): A transaction can read a data item if its timestamp is greater than or equal to the WTS of the data item. A transaction can write a data item if its timestamp is greater than both the RTS and the WTS of the data item. If a transaction violates any of these rules, it is aborted and restarted with a new timestamp. BTO ensures serializability, but not recoverability or freedom from cascading aborts.
- Thomas' write rule (TWR): A transaction can read a data item if its timestamp is greater than or equal to the WTS of the data item. A transaction can write a data item if its timestamp is greater than the WTS of the data item, and the write is not ignored. A write is ignored if the timestamp of the transaction is less than or equal to the RTS of the data item, meaning that the write is outdated and has no effect. TWR ensures serializability and recoverability, but not freedom from cascading aborts.
- Multiversion timestamp ordering (MVTO): A transaction can read the latest version of a data item that has a WTS less than or equal to the timestamp of the transaction. A transaction can write a new version of a data item if its timestamp is greater than the WTS of the current version of the data item. Each version of a data item has its own RTS and WTS. MVTO ensures serializability, recoverability, and freedom from cascading aborts. However, MV



### Locking Techniques for Concurrency Control

Concurrency control is the process of managing concurrent access to a shared database by multiple transactions. Concurrency control ensures that the transactions are executed in a way that preserves the consistency and integrity of the database.

One of the most common concurrency control techniques is locking. Locking is an operation that grants a transaction permission to read or write a data item. A lock manager is a subsystem that manages the acquisition and release of locks by transactions.

There are different types of locks, such as:

- Binary locks: These locks have only two states, locked or unlocked. A transaction can either lock a data item for exclusive access or leave it unlocked for shared access.
- Shared and exclusive locks: These locks allow multiple transactions to read the same data item concurrently, but only one transaction can write to it. A transaction can acquire a shared lock (S-lock) to read a data item or an exclusive lock (X-lock) to write to it. A data item can have multiple S-locks but only one X-lock at a time.
- Read and write locks: These locks are similar to shared and exclusive locks, but they are more fine-grained. A transaction can acquire a read lock (R-lock) to read a data item or a write lock (W-lock) to write to it. A data item can have multiple R-locks but only one W-lock at a time. A W-lock is compatible with an R-lock, but not with another W-lock.
- Intention locks: These locks are used to indicate the intention of a transaction to acquire a lock on a lower level of granularity. For example, a transaction can acquire an intention shared lock (IS-lock) on a table to indicate that it will acquire S-locks on some rows of the table. An intention exclusive lock (IX-lock) indicates that the transaction will acquire X-locks on some rows of the table. An intention lock is compatible with another intention lock, but not with a data lock.
- Certify locks: These locks are used in multi-version concurrency control techniques, where each transaction works on a local version of the data item and commits the changes to the global version only after certifying that no conflicts exist. A transaction can acquire a certify lock (C-lock) on a data item to indicate that it has completed its updates on the local version and is ready to commit. A C-lock is compatible with an R-lock, but not with another C-lock or a W-lock.

Locking techniques can be classified into two categories based on the timing of lock acquisition and release:

- Strict two-phase locking (2PL): In this technique, a transaction follows two phases: a growing phase and a shrinking phase. In the growing phase, the transaction can acquire locks but cannot release them. In the shrinking phase, the transaction can release locks but cannot acquire new ones. This technique ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.
- Non-strict two-phase locking: In this technique, a transaction can release locks before committing, but it cannot acquire new locks after releasing any lock. This technique allows more concurrency than strict 2PL, but it may not ensure serializability. However, it ensures recoverability, which means that the effects of a transaction are not visible to other transactions until it commits.



### Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use system time or logical counters as timestamps to order the transactions and ensure serializability.
- Timestamps are assigned to each transaction when it is created and to each read or write operation when it is issued.
- The timestamps determine the precedence order of the transactions and the operations, and any conflicting operations are executed according to their timestamps.
- There are two types of timestamp ordering protocols: basic timestamp ordering and optimistic timestamp ordering.
- Basic timestamp ordering protocol uses two timestamps for each data item: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item, and WTS is the largest timestamp of any transaction that has successfully written the data item.
- Basic timestamp ordering protocol enforces two rules: read-write rule and write-write rule. The read-write rule states that a transaction T can read a data item X only if the timestamp of T is greater than or equal to the WTS of X. The write-write rule states that a transaction T can write a data item X only if the timestamp of T is greater than both the RTS and the WTS of X.
- If a transaction T violates either of the rules, it is aborted and restarted with a new timestamp.
- Basic timestamp ordering protocol ensures conflict serializability, but it may cause cascading aborts, which means that aborting one transaction may cause other transactions to abort as well.
- Optimistic timestamp ordering protocol avoids cascading aborts by delaying the validation of transactions until they are ready to commit. It divides the execution of each transaction into three phases: read phase, validation phase, and write phase.
- In the read phase, a transaction T reads the data items from the database and stores them in a local buffer. It also records the timestamps of the data items in two sets: read set (RS) and write set (WS).
- In the validation phase, a transaction T checks if it can commit without violating serializability. It uses two timestamps: start timestamp (ST) and commit timestamp (CT). ST is the timestamp assigned to T when it is created, and CT is the current timestamp when T enters the validation phase.
- Optimistic timestamp ordering protocol enforces three rules: read-write rule, write-write rule, and write-read rule. The read-write rule states that a transaction T can commit only if for each data item X in its WS, the WTS of X in the database is less than the ST of T. The write-write rule states that a transaction T can commit only if for each data item X in its WS, the CT of T is greater than the CT of any other transaction that has written X and committed. The write-read rule states that a transaction T can commit only if for each data item X in its RS, the WTS of X in the database is equal to the WTS of X in the local buffer of T.
- If a transaction T violates any of the rules, it is aborted and restarted with a new timestamp.
- In the write phase, a transaction T writes the data items from its local buffer to the database and updates the WTS of the data items accordingly.
- Optimistic timestamp ordering protocol ensures conflict serializability and avoids cascading aborts, but it may cause more aborts than basic timestamp ordering protocol, especially when the degree of concurrency is high.



### Validation Based Protocol in DBMS

- Validation Based Protocol is a concurrency control technique that works on the assumption that very few transactions interfere with each other, and therefore there is no need for checking while the transaction is executing  .
- It is also called Optimistic Concurrency Control Technique because it optimistically allows transactions to execute without any locking or checking, and only validates them at the end  .
- Validation Based Protocol divides the execution of a transaction into three phases: read phase, validation phase, and write phase  .
- In the read phase, the transaction reads the data items from the database and stores them in a local buffer. It does not write anything to the database in this phase  .
- In the validation phase, the transaction checks whether it can commit without violating the serializability of the schedule. It uses timestamps to determine the order of transactions and compares them with the read and write sets of other transactions  .
- In the write phase, if the transaction passes the validation, it writes the updated data items from the local buffer to the database. Otherwise, it aborts and restarts  .
- Validation Based Protocol ensures serializability and avoids deadlock, but it may cause more aborts and restarts than locking protocols. It also requires more storage space for maintaining the read and write sets of transactions   .



### Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows the following rules :
  - Follow multi-granularity compatibility function
  - Lock root of tree first, any mode
  - Node Q can be locked by T i in S or IS only if parent(Q) locked by T i in IX or IS
  - Node Q can be locked by T i in X, SIX, IX only if parent(Q) locked by T i in IX, SIX
  - T i is two-phase
  - T i can unlock node Q only if none of Q’s descendants are locked by T i
- Multiple granularity locking protocol uses the following types of locks :
  - Shared (S): Allows a transaction to read a data item
  - Exclusive (X): Allows a transaction to read and write a data item
  - Intention Shared (IS): Indicates that a transaction intends to lock some of the descendants of a node in shared mode
  - Intention Exclusive (IX): Indicates that a transaction intends to lock some of the descendants of a node in exclusive mode
  - Shared and Intention Exclusive (SIX): Indicates that a transaction intends to lock some of the descendants of a node in exclusive mode and also wants to read the node itself
- Multiple granularity locking protocol can be represented graphically as a tree, where each node corresponds to a data item or a set of data items, and the root node represents the entire database. For example, consider the following tree, which consists of four levels of nodes:

```
    A
   / \
  B   C
 / \ / \
D  E F  G
```

- In this tree, A represents the entire database, B and C represent two relations, D, E, F, and G represent four tuples, and the edges represent the parent-child relationship. A transaction can lock any node in the tree according to the rules and types of locks mentioned above. For example, a transaction T1 can lock node B in IX mode and node D in X mode, indicating that it intends to write tuple D in relation B. Another transaction T2 can lock node A in IS mode and node C in S mode, indicating that it intends to read relation C in the database. These locks are compatible and do not cause any conflict. However, if a transaction T3 tries to lock node A in X mode, it will conflict with both T1 and T2 and will have to wait until they release their locks.



### Multi-version schemes for concurrency control

- Multi-version schemes are a type of concurrency control method that allow concurrent access to the database without locking the data.
- Multi-version schemes maintain different versions of data items, each with a version number and a timestamp.
- Each transaction reads the most recent version of a data item that is compatible with its timestamp, and writes a new version of a data item with an incremented version number and its own timestamp.
- Multi-version schemes avoid the problems of locking, such as deadlocks, starvation, and blocking, and improve the performance of database applications in a multiuser environment.
- Multi-version schemes can be classified into two types: optimistic and pessimistic.
- Optimistic multi-version schemes assume that conflicts are rare and allow transactions to execute without checking for concurrency violations until they commit. At commit time, transactions are validated against the versions of data items they have read and written, and are aborted if they violate the serializability property.
- Pessimistic multi-version schemes assume that conflicts are frequent and check for concurrency violations before transactions execute any operation. Transactions are aborted if they try to read or write a data item that has been modified by another transaction with a higher priority or a later timestamp.
- Examples of multi-version schemes are multiversion two-phase locking (MV2PL), multiversion timestamp ordering (MVTO), and snapshot isolation (SI).



### Recovery with Concurrent Transaction

- Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions executing simultaneously.
- Recovery with concurrent transaction is necessary to ensure the ACID properties of transactions, especially atomicity and durability.
- Recovery with concurrent transaction can be done in the following four ways:
  - Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if locking is used, then the recovery scheme can use the lock table to identify the transactions that were active at the time of failure and undo their effects. If timestamp ordering is used, then the recovery scheme can use the timestamps to order the transactions and redo their effects.
  - Transaction rollback: In this scheme, the recovery scheme can undo the effects of a transaction that has failed or aborted by using the log records. The log records contain the information about the operations performed by the transaction, such as the old and new values of the data items. The recovery scheme can use the log records to restore the old values of the data items and make the transaction appear as if it never executed.
  - Checkpoints: In this scheme, the recovery scheme can reduce the amount of work needed to recover from a failure by periodically taking a snapshot of the database and the log records. A checkpoint is a point in time when the database and the log records are synchronized and consistent. The recovery scheme can use the checkpoint as a starting point for recovery and only process the log records after the checkpoint.
  - Restart recovery: In this scheme, the recovery scheme can handle the case when the system fails during the recovery process itself. The recovery scheme can use a special log record called restart record to mark the beginning of the recovery process. The restart record contains the information about the transactions that need to be redone or undone. The recovery scheme can use the restart record to resume the recovery process from where it left off.



## Unit 9 - Database Security

- Database security is the protection of data and information stored in a database from unauthorized access, modification, or deletion.
- Database security involves implementing various measures, such as encryption, authentication, authorization, auditing, backup, and recovery, to ensure the confidentiality, integrity, and availability of data.
- Database security is important for various reasons, such as:
  - Protecting sensitive and personal data from identity theft, fraud, or cyberattacks.
  - Complying with legal and ethical regulations and standards, such as GDPR, HIPAA, PCI DSS, etc.
  - Maintaining the reputation and trust of customers, partners, and stakeholders.
  - Preventing data loss or corruption due to hardware failures, natural disasters, or human errors.
  - Enhancing the performance and efficiency of database operations and applications.
- Database security can be classified into two categories: physical security and logical security.
  - Physical security refers to the protection of the database server and its components from physical threats, such as theft, fire, water, power outage, etc. Physical security measures include locking the server room, installing fire alarms and sprinklers, using uninterruptible power supply (UPS), etc.
  - Logical security refers to the protection of the data and information stored in the database from logical threats, such as unauthorized access, modification, or deletion. Logical security measures include encrypting the data, requiring user authentication and authorization, enforcing access control policies, auditing the database activities, etc.



### Types of security for the notes of the Unit 9 - Database Security in the subject of Basics of Data Base Management System

Database security refers to the process of protecting and safeguarding the database from unauthorized access or cyber-attacks. There are different types of database security that should be implemented in your business, such as:

- **Authentication**: Database authentication is the type of database security that verifies the user’s login credentials which are stored in the database. If the user’s login credentials match in the database, then the user can access the database. Authentication can be done using passwords, biometrics, tokens, or certificates.
- **Database Encryption**: Database encryption is the type of database security that transforms the data in the database into an unreadable format using a secret key or algorithm. Database encryption can be applied to the whole database, a specific table, a column, or a row. Database encryption can protect the data from unauthorized access, modification, or theft.
- **Backup Database**: Backup database is the type of database security that creates a copy of the database and stores it in a separate location. Backup database can help to recover the data in case of data loss, corruption, or disaster. Backup database can be done manually or automatically, and can be stored on-premise or off-premise.
- **Physical Security**: Physical security is the type of database security that prevents unauthorized physical access to the database server or storage. Physical security can include locks, alarms, cameras, guards, or biometric scanners. Physical security can protect the database from theft, damage, or sabotage.
- **Application Security**: Application security is the type of database security that protects the database from malicious attacks that originate from the application layer. Application security can include input validation, output encoding, parameterized queries, secure coding practices, and security testing. Application security can prevent SQL/NoSQL injection attacks, buffer overflow exploitations, or cross-site scripting attacks .
- **Access Control**: Access control is the type of database security that regulates who can access what data in the database. Access control can be based on the user’s role, privilege, or context. Access control can enforce the principle of least privilege, which means that users should only have the minimum access necessary to perform their tasks. Access control can prevent data leakage, data tampering, or data misuse .
- **Web Application Firewall**: Web application firewall is the type of database security that monitors and filters the incoming and outgoing traffic between the web application and the database. Web application firewall can detect and block malicious requests, such as SQL/NoSQL injection attacks, that try to exploit the database vulnerabilities. Web application firewall can also provide logging and auditing capabilities for the database activity .

These are some of the types of database security that can help to protect the database from various threats and risks. Database security is an essential part of database management and should be implemented according to the best practices and standards.



### System Failure

- A system failure is an event that causes the database to stop functioning normally and may result in data loss, corruption, or unauthorized access.
- System failures can be caused by various factors, such as hardware malfunctions, software bugs, power outages, network disruptions, natural disasters, human errors, or malicious attacks.
- System failures can affect the database security in terms of confidentiality, integrity, and availability of the data.
- Confidentiality is the protection of data from unauthorized disclosure or access. A system failure may compromise confidentiality if the data is exposed to unauthorized users or leaked to external sources.
- Integrity is the protection of data from unauthorized modification or deletion. A system failure may compromise integrity if the data is altered, erased, or corrupted by the failure or by the recovery process.
- Availability is the protection of data from unauthorized denial of service or access. A system failure may compromise availability if the data is inaccessible or unavailable to authorized users or applications.
- To prevent or mitigate the impact of system failures, database security best practices include:
  - Implementing backup and recovery mechanisms to restore the database to a consistent state after a failure. Backup copies of the database and log files should be made regularly and stored in a secure location.
  - Applying patches and updates to the database software and the operating system to fix any vulnerabilities or bugs that may cause failures or allow exploitation.
  - Encrypting the data at rest and in transit to prevent unauthorized access or disclosure in case of a failure .
  - Monitoring and auditing the database activity and performance to detect and respond to any signs of failures or anomalies .
  - Educating and training the database users and administrators on the proper use and maintenance of the database and the security policies and procedures .

