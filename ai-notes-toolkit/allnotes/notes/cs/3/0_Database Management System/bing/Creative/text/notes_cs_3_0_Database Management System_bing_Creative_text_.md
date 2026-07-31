

## Unit 1 - Introduction

- In this unit, you will learn about the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be divided into two main branches: symbolic AI and sub-symbolic AI.
  - Symbolic AI uses symbols and rules to represent and manipulate knowledge, such as logic, search, planning, and expert systems.
  - Sub-symbolic AI uses numerical and statistical methods to model and learn from data, such as neural networks, evolutionary algorithms, and reinforcement learning.
- AI can also be classified into different types based on the level of intelligence and the domain of application, such as narrow AI, general AI, and super AI.
  - Narrow AI is the type of AI that can perform specific tasks well, but cannot generalize to other tasks or domains, such as face recognition, speech recognition, and chess playing.
  - General AI is the type of AI that can perform any intellectual task that a human can, and can transfer knowledge and skills across domains, such as natural language understanding, common sense reasoning, and creativity.
  - Super AI is the type of AI that can surpass human intelligence and capabilities in all domains, and can potentially create and control other AI systems, such as artificial superintelligence, artificial god, and singularity.
- AI has many applications and benefits for various fields and industries, such as education, health care, entertainment, business, and security.
  - AI can enhance learning outcomes, personalize instruction, and provide feedback and assessment for education.
  - AI can improve diagnosis, treatment, and prevention of diseases, and support health care professionals and patients for health care.
  - AI can create realistic and immersive simulations, games, and movies, and generate novel and diverse content for entertainment.
  - AI can optimize processes, reduce costs, and increase profits, and provide insights and recommendations for business.
  - AI can protect data, systems, and networks, and detect and prevent threats and attacks for security.
- AI also poses many challenges and risks for society and humanity, such as ethical, social, legal, and existential issues.
  - AI can raise ethical questions about the values, rights, and responsibilities of humans and machines, such as fairness, accountability, transparency, and privacy.
  - AI can have social impacts on the culture, economy, and politics of human societies, such as bias, discrimination, unemployment, and inequality.
  - AI can create legal dilemmas and conflicts about the regulation, governance, and liability of AI systems and agents, such as laws, standards, and policies.
  - AI can threaten the existence and survival of humans and other species, and challenge the meaning and purpose of life, such as superintelligence, singularity, and alignment.



### Overview for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A database is a collection of related data that can be stored, manipulated, and retrieved by a computer system.
- A database management system (DBMS) is a software system that provides the functionality to create, maintain, and manipulate databases.
- A DBMS consists of three components: data, data dictionary, and database engine.
- Data is the actual information stored in the database, such as names, addresses, phone numbers, etc.
- Data dictionary is the metadata that describes the structure, format, and constraints of the data in the database.
- Database engine is the core component that performs the operations on the data, such as insertion, deletion, modification, retrieval, etc.
- A DBMS can be classified into different types based on the data model, the logical structure that defines how the data is organized and manipulated.
- Some common data models are: hierarchical, network, relational, object-oriented, and NoSQL.
- A hierarchical data model organizes the data in a tree-like structure, where each node has one parent and zero or more children.
- A network data model organizes the data in a graph-like structure, where each node can have multiple parents and multiple children.
- A relational data model organizes the data in a tabular structure, where each row represents a record and each column represents an attribute.
- An object-oriented data model organizes the data in a class-based structure, where each object is an instance of a class and has attributes and methods.
- A NoSQL data model organizes the data in a non-tabular structure, such as key-value pairs, documents, graphs, or columns.
- A DBMS can also be classified into different types based on the level of abstraction, the degree of hiding the implementation details from the users.
- Some common levels of abstraction are: physical, logical, and view.
- A physical level of abstraction describes how the data is physically stored and accessed in the database, such as the file format, the indexing method, the disk allocation, etc.
- A logical level of abstraction describes what data is stored in the database and the relationships among the data, such as the data model, the schema, the constraints, etc.
- A view level of abstraction describes how the data is presented to the users and the applications, such as the queries, the reports, the forms, etc.
- A DBMS can also be classified into different types based on the distribution, the degree of sharing the data among multiple sites or nodes.
- Some common types of distribution are: centralized, decentralized, and distributed.
- A centralized DBMS stores and manages the data in a single site or node, such as a single server or a single computer.
- A decentralized DBMS stores and manages the data in multiple independent sites or nodes, such as a network of servers or computers.
- A distributed DBMS stores and manages the data in multiple interconnected sites or nodes, such as a cloud of servers or computers.
- A DBMS can also be classified into different types based on the concurrency, the degree of allowing multiple users or applications to access and modify the data simultaneously.
- Some common types of concurrency are: serial, concurrent, and parallel.
- A serial DBMS processes the requests one by one, in a sequential order, such as a single-user or a single-threaded system.
- A concurrent DBMS processes the requests concurrently, in an interleaved order, such as a multi-user or a multi-threaded system.
- A parallel DBMS processes the requests in parallel, in a simultaneous order, such as a cluster or a grid system.



### Database System vs File System

- A file system is a collection of files organized in a hierarchical structure, where each file contains data records.
- A database system is a collection of data organized in a logical structure, where each data item has a name and a value, and can be accessed by queries.
- Some advantages of database system over file system are:
  - Data independence: The database system allows the separation of data and application programs, so that changes in data structure or storage do not affect the application programs.
  - Data integrity: The database system enforces rules and constraints to ensure the consistency and validity of data.
  - Data security: The database system provides mechanisms to control the access and manipulation of data by authorized users and prevent unauthorized access.
  - Data sharing: The database system allows multiple users and applications to access and update the same data concurrently and consistently.
  - Data recovery: The database system supports backup and recovery of data in case of failures or disasters.
  - Data manipulation: The database system provides a high-level query language to retrieve and manipulate data easily and efficiently.



### Database System Concept and Architecture

- A database system is a software package that allows users to create, manipulate, and access data stored in a database.
- A database system consists of several components, such as the database, the database management system (DBMS), the application programs, and the users.
- The database is a collection of related data that represents some aspects of the real world. The data is organized in a logical and structured way to facilitate efficient processing and retrieval.
- The database management system (DBMS) is the software that interacts with the database and the application programs. The DBMS provides various functions, such as data definition, data manipulation, data control, and data administration.
- The application programs are the software that use the DBMS to access and manipulate the data in the database. The application programs can be written in various programming languages, such as SQL, Java, C#, etc.
- The users are the people who interact with the database system through the application programs or directly through the DBMS. The users can be classified into different categories, such as database administrators, database designers, application developers, and end users.
- The architecture of a database system is the way the components of the system are organized and communicate with each other. The architecture of a database system can be influenced by various factors, such as the primary computer system, the network environment, the data distribution, and the user requirements.
- The architecture of a database system can be classified into different types, such as centralized, decentralized, hierarchical, single-tier, multi-tier, client-server, and parallel. Each type of architecture has its own advantages and disadvantages, depending on the specific application and context.
- A centralized database system is a system where the database and the DBMS are located on a single computer system. A centralized database system is simple and easy to manage, but it has limited scalability and reliability.
- A decentralized database system is a system where the database and the DBMS are distributed across multiple computer systems. A decentralized database system can improve scalability and reliability, but it introduces complexity and overhead in data management and communication.
- A hierarchical database system is a system where the database and the DBMS are organized in a hierarchical structure, with a root node and several child nodes. A hierarchical database system can simplify data access and control, but it can also limit data independence and flexibility.
- A single-tier database system is a system where the database, the DBMS, and the application programs are all located on the same computer system. A single-tier database system is easy to implement and maintain, but it has poor performance and security.
- A multi-tier database system is a system where the database, the DBMS, and the application programs are divided into different tiers or layers, each running on a separate computer system. A multi-tier database system can improve performance and security, but it also increases complexity and cost.
- A client-server database system is a type of multi-tier database system where the database and the DBMS are located on a server machine, and the application programs are located on client machines. A client-server database system can support multiple concurrent users and applications, but it can also suffer from network congestion and server overload.
- A parallel database system is a type of decentralized database system where the database and the DBMS are partitioned and replicated across multiple computer systems that work in parallel. A parallel database system can achieve high performance and availability, but it also requires sophisticated synchronization and coordination mechanisms.



### Data Model Schema and Instances

- A data model is a collection of concepts and rules for describing the structure, meaning, and constraints of the data stored in a database.
- A schema is a description of a particular collection of data, using a given data model.
- An instance is the actual data stored in a database at a particular moment in time, conforming to a schema.
- A schema can be specified at different levels of abstraction, such as conceptual, logical, and physical.
- A conceptual schema is a high-level description of the data and its relationships, independent of any implementation details.
- A logical schema is a more detailed description of the data and its constraints, using a specific data model, such as the relational model or the object-oriented model.
- A physical schema is a low-level description of how the data is stored and accessed, using physical structures such as files, records, indexes, etc.
- A schema can also be specified for different views of the data, such as external, internal, and stored.
- An external schema is a subset of the conceptual schema that defines how a particular user or application sees the data.
- An internal schema is a subset of the logical schema that defines how the data is organized and accessed by the database system.
- A stored schema is a subset of the physical schema that defines how the data is physically stored on the disk or other storage devices.



### Data Independence and Database Language and Interfaces

- Data independence is the property of a database system that allows the data and the applications to be changed independently of each other.
- Data independence can be classified into two types: logical data independence and physical data independence.
- Logical data independence is the ability to change the logical structure of the database (such as the schema, tables, views, etc.) without affecting the existing applications that access the data.
- Physical data independence is the ability to change the physical structure of the database (such as the storage devices, file organization, indexes, etc.) without affecting the logical structure or the applications that access the data.
- Data independence is achieved by using a three-level architecture for the database system, which consists of the external level, the conceptual level, and the internal level.
- The external level defines the views of the data for different users or applications, which are tailored to their specific needs and requirements.
- The conceptual level defines the logical structure of the data for the entire database, which is independent of the physical implementation or the user views.
- The internal level defines the physical structure of the data, which is how the data is stored and organized on the storage devices.
- The three levels are connected by two mappings: the external-conceptual mapping and the conceptual-internal mapping, which define how the data is transformed from one level to another.
- The database language and interfaces are the means of communication between the users or applications and the database system.
- The database language and interfaces can be classified into two types: data definition language (DDL) and data manipulation language (DML).
- Data definition language (DDL) is the language that is used to define the structure of the data at the different levels of the database system, such as the schema, tables, views, constraints, etc.
- Data manipulation language (DML) is the language that is used to manipulate the data in the database, such as inserting, updating, deleting, querying, etc.
- The database language and interfaces can also be classified into two types: procedural and non-procedural.
- Procedural language and interface require the user or application to specify both what data is needed and how to retrieve or manipulate it, such as SQL or QBE.
- Non-procedural language and interface require the user or application to specify only what data is needed, and the database system determines how to retrieve or manipulate it, such as natural language or graphical user interface.



### Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects such as tables, views, indexes, schemas, etc. 
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas. 
- DDL is used to specify the logical and physical characteristics of the data, such as data types, constraints, relationships, etc. 
- DDL is also used to grant or revoke access rights and privileges to database objects. 
- Some common DDL commands are CREATE, ALTER, DROP, RENAME, TRUNCATE, COMMENT, etc. 
- DDL is a part of the Structured Query Language (SQL), which is a standard language for interacting with relational databases. 
- DDL is executed by the database management system (DBMS), which interprets and validates the DDL statements and updates the data dictionary accordingly. 
- DDL is different from Data Manipulation Language (DML), which is used to insert, update, delete, and query data in a database. 
- DDL is also different from Data Control Language (DCL), which is used to control the transactions and concurrency in a database. 
- DDL is an essential component of database design and development, as it defines the schema and integrity of the data.



### DML for the notes of the Unit 1 - Introduction in the subject of Database Management System

- DML stands for Data Manipulation Language, which is a family of computer languages that allow users to manipulate data in a database.
- DML is a subset of SQL (Structured Query Language), which is the most widely used language for interacting with relational databases.
- DML statements are used to query, edit, add, delete and update row-level data from database tables or views.
- The main DML statements are:
  - SELECT: retrieve data from one or more tables or views.
  - INSERT: add new rows of data to a table or view.
  - UPDATE: modify existing rows of data in a table or view.
  - DELETE: remove existing rows of data from a table or view.
  - MERGE: combine the data from two or more tables or views into one table or view.
- DML statements can be executed directly by the user, or embedded in a program or a stored procedure.
- DML statements can be affected by constraints, triggers, indexes, views and other database objects.
- DML statements can also use functions, operators, expressions, conditions, clauses and subqueries to manipulate the data.
- DML statements can return a result set, a message, a row count, or an error.
- DML statements can be categorized into two types: procedural and non-procedural.
  - Procedural DML: specifies what data is needed and how to get it.
  - Non-procedural DML: specifies what data is needed without specifying how to get it.
- SQL is an example of a non-procedural DML, as it allows the user to specify the desired result without specifying the steps to achieve it.



### Overall Database Structure

- A database is a collection of information that is related to a particular subject or purpose, such as tracking customer orders or maintaining a music collection.
- A database can be considered a structure in realization of the database language. The states of a created conceptual schema are transformed into an explicit mapping, the database schema. This describes how real-world entities are modeled in the database.
- A database schema consists of a set of tables, each with a name, columns, data types, constraints, and relationships with other tables.
- A database management system (DBMS) is a software that extracts information from the database in response to queries. A DBMS also provides functions for defining, storing, manipulating, and protecting the data in the database.
- The database system is divided into three components: query processor, storage manager, and disk storage.
  - The query processor is responsible for interpreting and executing the queries written in a database language, such as SQL. It also performs query optimization, which is the process of finding the most efficient way to execute a query.
  - The storage manager is responsible for managing the allocation and deallocation of disk space, as well as the movement of data between disk and main memory. It also provides mechanisms for concurrency control, recovery, and security.
  - The disk storage is the physical device where the data is stored. It consists of files, pages, and records. A file is a collection of pages, a page is a fixed-size unit of disk space, and a record is a logical unit of data that corresponds to a row in a table.



### Data Modeling Using the Entity Relationship Model

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical method for data modeling using entities, attributes, and relationships.
- Entities are the basic units of data that have a unique identity and properties. Examples of entities are students, courses, books, etc.
- Attributes are the characteristics or features of entities that describe them. Examples of attributes are name, age, address, etc.
- Relationships are the associations or connections between entities that indicate how they are related to each other. Examples of relationships are enrolls, teaches, borrows, etc.
- Entity Relationship Diagram (ERD) is a diagram that shows the entities, attributes, and relationships in a database using symbols and connectors.
- ERD symbols include:
  - Rectangles for entities
  - Ovals for attributes
  - Diamonds for relationships
  - Lines for connections
  - Cardinality symbols for indicating the number of occurrences of an entity in a relationship
- ERD connectors include:
  - Solid lines for mandatory participation
  - Dashed lines for optional participation
  - Double lines for identifying relationships
  - Single lines for non-identifying relationships
- ERD rules include:
  - Each entity must have a unique name and a primary key attribute
  - Each attribute must belong to one and only one entity
  - Each relationship must have a name and a degree (the number of entities involved)
  - Each relationship must have a cardinality (the number of instances of one entity that can be associated with one instance of another entity)
  - Each relationship must have a participation constraint (the minimum and maximum number of instances of one entity that must be associated with one instance of another entity)
- ERD examples include:

ERD example 1

This ERD shows the entities Customer, Order, and Product, and their attributes and relationships. The cardinality symbols indicate that a customer can place zero or more orders, an order must belong to one and only one customer, an order can contain one or more products, and a product can be in zero or more orders. The participation constraints indicate that a customer must place at least one order, an order must contain at least one product, and a product does not have to be in any order.

ERD example 2

This ERD shows the entities Student, Course, and Enrollment, and their attributes and relationships. The cardinality symbols indicate that a student can enroll in zero or more courses, a course can have zero or more students enrolled, and an enrollment must involve one and only one student and one and only one course. The participation constraints indicate that a student does not have to enroll in any course, a course does not have to have any student enrolled, and an enrollment must exist for every pair of student and course. The double lines indicate that the relationship Enrollment is identifying, meaning that the primary key of Enrollment is composed of the primary keys of Student and Course.



### ER Model Concepts

- The ER model is a conceptual data model that describes the entities, attributes, and relationships in a database. It is used to design and represent the logical structure of a database.   
- An entity is a real-world object or concept that can be identified uniquely and has some properties. For example, a student, a course, a book, etc.  
- An attribute is a property or characteristic of an entity that describes some aspect of it. For example, name, age, address, etc. Attributes can be simple or composite, single-valued or multi-valued, stored or derived, etc.  
- A relationship is an association or connection between two or more entities that expresses some meaningful dependency or interaction. For example, a student enrolls in a course, a book belongs to a library, etc. Relationships can have cardinality constraints and participation constraints that specify the number and type of entities involved.   
- An ER diagram is a graphical representation of the ER model using symbols and notation. It shows the entities, attributes, and relationships in a database schema. It can be used to communicate the design and requirements of a database to the stakeholders.



### Notation for ER Diagram

- ER diagram stands for Entity Relationship diagram, which is a graphical representation of the logical structure of a database .
- ER diagram shows the entities, attributes and relationships of a database schema .
- Entities are the objects or concepts that are stored in a database, such as students, courses, employees, etc. Entities are represented by rectangles in ER diagrams   .
- Attributes are the properties or characteristics of entities, such as name, age, address, etc. Attributes are represented by ovals or inside entities in ER diagrams   .
- Relationships are the associations or interactions between entities, such as enrolled, works for, manages, etc. Relationships are represented by diamonds or with lines in ER diagrams   .
- There are different types of notations and symbols for ER diagrams, such as arrow notation, Barker's notation, Chen's notation, crow's foot notation, UML notation and IDEF1X notation   .
- Each notation has its own way of showing the cardinality, optionality and participation of entities and relationships in ER diagrams   .
- Cardinality is the number of instances of one entity that can or must be associated with each instance of another entity, such as one-to-one, one-to-many, many-to-one or many-to-many   .
- Optionality is the possibility of the existence of a relationship, such as mandatory or optional   .
- Participation is the degree of involvement of an entity in a relationship, such as total or partial   .
- For example, using arrow notation, a one-to-one mandatory relationship between entity A and entity B is shown as:

arrow notation example

- Using crow's foot notation, a one-to-many optional relationship between entity A and entity B is shown as:

crow's foot notation example

- Using Chen's notation, a many-to-many relationship between entity A and entity B with an attribute C is shown as:

Chen's notation example

- ER diagrams are useful for designing, documenting and communicating database schemas   .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of mapping constraints for the unit 1 - introduction in the subject of database management system.

### Mapping Constraints

- Mapping constraints are rules that define how the entities and relationships in an entity-relationship (ER) diagram can be mapped to the tables and columns in a relational database schema.
- Mapping constraints can be classified into three types: cardinality constraints, participation constraints, and key constraints.
- Cardinality constraints specify the number of instances of one entity that can be associated with each instance of another entity in a relationship. Cardinality constraints can be one-to-one, one-to-many, many-to-one, or many-to-many.
- Participation constraints specify whether the participation of an entity in a relationship is mandatory or optional. Participation constraints can be total or partial.
- Key constraints specify the attributes that uniquely identify each entity or relationship instance. Key constraints can be primary keys, foreign keys, or composite keys.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some keys for the notes of the Unit 1 - Introduction in the subject of Database Management System:

### Keys for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A **database** is a collection of related data that can be stored, manipulated, and retrieved by a computer system.
- A **database management system (DBMS)** is a software system that provides the functionality to create, maintain, and access databases.
- A **database application** is a software program that interacts with a database to perform specific tasks, such as querying, updating, or reporting data.
- A **database system** consists of a database, a DBMS, and one or more database applications.
- A **data model** is a conceptual representation of the structure and meaning of the data in a database. It defines the data elements, their attributes, and their relationships.
- A **relational data model** is a data model that represents data as a collection of tables, where each table consists of rows and columns. A row is also called a **tuple** or a **record**, and a column is also called an **attribute** or a **field**.
- A **primary key** is an attribute or a combination of attributes that uniquely identifies each row in a table. A **foreign key** is an attribute or a combination of attributes in one table that references the primary key of another table. A **referential integrity constraint** is a rule that ensures that the foreign key values in one table match the primary key values in the referenced table.
- A **schema** is a description of the structure and constraints of a database. A **database instance** is a snapshot of the data in a database at a given point in time. A **database state** is the set of all database instances that satisfy the schema constraints.
- A **data definition language (DDL)** is a language that allows the user to define the schema of a database. A **data manipulation language (DML)** is a language that allows the user to manipulate the data in a database, such as inserting, deleting, updating, or querying data. A **data control language (DCL)** is a language that allows the user to control the access and security of a database, such as granting or revoking privileges to users or roles.
- A **query** is a request to retrieve data from a database that satisfies certain conditions. A **query language** is a language that allows the user to specify queries. A **query processor** is a component of a DBMS that parses, optimizes, and executes queries.
- A **transaction** is a logical unit of work that consists of a sequence of operations on a database, such as reading or writing data. A **transaction management system** is a component of a DBMS that ensures that transactions are executed in a correct and consistent manner, and that the database state is restored in case of failures or errors. A **concurrency control mechanism** is a technique that coordinates the concurrent execution of transactions and prevents conflicts or inconsistencies. A **recovery mechanism** is a technique that restores the database state to a consistent state after a failure or error.
- A **database design** is a process of creating a database schema that meets the requirements and objectives of a database system. A **database design methodology** is a systematic approach to database design that consists of a series of steps or phases. A **conceptual database design** is a phase of database design that involves creating a high-level data model that captures the essential features and constraints of the data. A **logical database design** is a phase of database design that involves mapping the conceptual data model to a specific data model, such as the relational data model. A **physical database design** is a phase of database design that involves choosing the physical storage structures and access methods for the data, such as indexes, partitions, or clusters.



### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A **super key** is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- For example, in a relation STUDENT with attributes RollNo, Name, Address, Phone, Email, the set {RollNo, Name} is a super key, since no two students can have the same roll number and name. However, the attribute Name is not essential for uniqueness, as {RollNo} is also a super key by itself.
- A super key is a **generalization** of a candidate key, which is a minimal super key, meaning that it does not have any extra attributes that can be removed without losing the uniqueness property.
- A candidate key is also called a **primary key** if it is chosen as the main way of identifying tuples in a relation. There can be more than one candidate key in a relation, but only one primary key.
- For example, in the STUDENT relation, {RollNo} and {Email} are both candidate keys, since they can uniquely identify a student and they are minimal. However, only one of them can be chosen as the primary key, such as {RollNo}.
- A super key is also a **specialization** of a key, which is a set of attributes that can uniquely identify a tuple in a relation, as well as all tuples in any relation that is related to it by referential integrity constraints.
- A key is also called a **foreign key** if it is used to link two relations by referring to the primary key of another relation.
- For example, in a relation COURSE with attributes CourseID, CourseName, Instructor, the set {CourseID} is a key, since it can uniquely identify a course and any course that is related to it by enrollment or prerequisite relations. The attribute Instructor is a foreign key, since it refers to the primary key {RollNo} of the STUDENT relation.



### Candidate Key

- A candidate key is a specific type of field in a relational database that can identify each unique record independently of any other data.
- A candidate key is a minimal superkey. In other words, it is any set of columns that have a unique combination of values in each row (which makes it a superkey), with the additional constraint that removing any column could produce duplicate combinations of values (which makes it a minimal superkey).
- A candidate key can be a single column or a combination of columns, as long as it satisfies the uniqueness and minimality properties.
- A table can have more than one candidate key, but only one of them can be chosen as the primary key, which is the candidate key selected by the database administrator to uniquely identify tuples in a table.
- To find the candidate keys of a table, we can use the following algorithm:
  - List all the possible superkeys of the table, i.e., all the sets of columns that have unique values in each row.
  - Eliminate any superkey that contains another superkey, i.e., any set of columns that has a subset of columns that is also a superkey.
  - The remaining superkeys are the candidate keys of the table.



### Primary Key

- A primary key is a special column or combination of columns in a relational database table that uniquely identifies each row in the table    .
- A primary key is used as a unique identifier to quickly access and manipulate data within the table .
- A table can have only one primary key, which can be either a single column or a composite key (a set of columns)   .
- A primary key must satisfy the following properties  :
  - **Uniqueness**: No two rows in the table can have the same primary key value.
  - **Non-nullability**: The primary key column(s) cannot contain null values, as null values cannot be used to identify rows.
  - **Stability**: The primary key value should not change frequently, as it may affect the integrity and performance of the database.
  - **Simplicity**: The primary key should be as simple and concise as possible, to avoid unnecessary complexity and overhead.
- A primary key can be either natural or surrogate :
  - A natural key is a column or set of columns that have a logical relationship to the data in the table, such as a student ID or a phone number.
  - A surrogate key is a column or set of columns that have no inherent meaning to the data in the table, such as a randomly generated number or a sequential number.
- A primary key can be defined using the PRIMARY KEY constraint in the CREATE TABLE or ALTER TABLE statements.
- A primary key can be referenced by other tables to establish relationships between them, using foreign keys.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some points on generalization for the notes of the Unit 1 - Introduction in the subject of Database Management System:

- Generalization is a process of extracting common characteristics or features from a set of entities and creating a generalized entity that can represent all the entities in the set.
- Generalization is a bottom-up approach, where we start with specific entities and combine them into a more general entity based on their similarities.
- Generalization is useful for reducing redundancy, complexity and inconsistency in the database design.
- Generalization can be represented by an **is-a** relationship, where the generalized entity is a superclass or a parent class, and the specific entities are subclasses or child classes.
- Generalization can be applied to both entities and relationships. For example, we can generalize the entities Student and Teacher into a superclass Person, or we can generalize the relationships Enrolls and Teaches into a superclass Involves.
- Generalization can be partial or total, depending on whether all the subclasses are included in the generalization or not. For example, if we generalize the entities Car, Bike and Bus into a superclass Vehicle, it can be a partial generalization if there are other types of vehicles that are not included, or a total generalization if all the types of vehicles are included.
- Generalization can be disjoint or overlapping, depending on whether the subclasses are mutually exclusive or not. For example, if we generalize the entities Male and Female into a superclass Gender, it can be a disjoint generalization if a person can belong to only one gender, or an overlapping generalization if a person can belong to more than one gender.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of aggregation for the unit 1 - introduction in the subject of database management system.

### Aggregation

- Aggregation is a process of combining two or more entities or relationships into a higher-level entity or relationship.
- Aggregation is used to represent complex relationships or to simplify the design of a database schema.
- Aggregation can be seen as a form of abstraction that hides the details of the lower-level entities or relationships and exposes only the relevant attributes and operations of the higher-level entity or relationship.
- Aggregation can be applied to both binary and n-ary relationships, as well as to both entity sets and relationship sets.
- Aggregation can be nested, meaning that an aggregated entity or relationship can be further aggregated with another entity or relationship.
- Aggregation can be represented graphically using a dashed rectangle around the entities or relationships that are aggregated, and a solid line connecting the aggregated entity or relationship to the rest of the schema.

#### Example of aggregation

Consider the following database schema for a university:

Schema without aggregation

In this schema, there are four entity sets: Student, Course, Department, and Instructor, and three relationship sets: Enroll, Offer, and Works_for. The Enroll relationship set connects Student and Course, and has an attribute Grade. The Offer relationship set connects Course and Department, and has an attribute Semester. The Works_for relationship set connects Instructor and Department, and has an attribute Salary.

Suppose we want to represent the relationship between a student and the instructor who teaches the course that the student is enrolled in. One way to do this is to create a new relationship set called Teaches, which connects Student and Instructor, and has an attribute Course_id. However, this would introduce redundancy in the schema, as the same information can be derived from the existing relationship sets Enroll and Offer. Moreover, this would make the schema more complex and harder to maintain.

A better way to do this is to use aggregation. We can aggregate the Enroll and Offer relationship sets into a higher-level relationship set called Section, which represents a section of a course offered by a department in a given semester. The Section relationship set has an attribute Section_id, which is a composite key of Course_id and Semester. The Section relationship set connects Student and Course, and inherits the attribute Grade from the Enroll relationship set. The Section relationship set also connects Course and Department, and inherits the attribute Semester from the Offer relationship set. The Section relationship set can then be related to the Instructor entity set by a new relationship set called Teaches, which has no attributes.

The following diagram shows the schema after applying aggregation:

Schema with aggregation

In this schema, the Teaches relationship set represents the relationship between a student and the instructor who teaches the section of the course that the student is enrolled in. The Teaches relationship set can be derived from the Section relationship set and the Works_for relationship set. The schema is simpler and more concise than the original one, and avoids redundancy and inconsistency.



### Reduction of an ER Diagrams to Tables

- An ER diagram is a graphical representation of the entities and relationships in a database.
- A table is a collection of rows and columns that store data in a relational database.
- The process of converting an ER diagram to tables is called reduction or mapping.
- The basic steps for converting an ER diagram to tables are:

  - Convert each entity set to a table with the same name and attributes.
  - Choose a primary key for each table that uniquely identifies each row.
  - Convert each relationship set to a table with the same name and attributes.
  - Include the primary keys of the participating entity sets as foreign keys in the relationship table.
  - Choose a primary key for the relationship table that combines the foreign keys and any other attributes.
  - If the relationship is one-to-one or one-to-many, the relationship table can be merged with one of the entity tables by adding the attributes of the relationship to the entity table.
  - If the relationship is many-to-many, the relationship table cannot be merged and must be kept as a separate table.
  - If the entity set or relationship set has any constraints, such as cardinality, participation, or generalization, they must be enforced by using appropriate techniques, such as null values, default values, triggers, or check constraints.

- An example of converting an ER diagram to tables is given below:

ER diagram

- The ER diagram has three entity sets: Student, Course, and Instructor, and two relationship sets: Enroll and Teach.
- The entity sets can be converted to tables as follows:

| Student | Course | Instructor |
|---------|--------|------------|
| S_ID (PK) | C_ID (PK) | I_ID (PK) |
| S_Name | C_Name | I_Name |
| S_Age | C_Credit | I_Salary |

- The relationship sets can be converted to tables as follows:

| Enroll | Teach |
|--------|-------|
| S_ID (FK) | I_ID (FK) |
| C_ID (FK) | C_ID (FK) |
| Grade | |

- The primary keys for the relationship tables are the combinations of the foreign keys, i.e., (S_ID, C_ID) for Enroll and (I_ID, C_ID) for Teach.
- The Enroll relationship is many-to-many, so it cannot be merged with any entity table.
- The Teach relationship is one-to-many, so it can be merged with the Course table by adding the I_ID attribute to the Course table.
- The final tables after reduction are:

| Student | Course | Enroll |
|---------|--------|--------|
| S_ID (PK) | C_ID (PK) | S_ID (FK, PK) |
| S_Name | C_Name | C_ID (FK, PK) |
| S_Age | C_Credit | Grade |
| | I_ID (FK) | |



### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates the extensions to the original entity-relationship (ER) model, used in the design of databases . The EER model reflects more precisely the properties and constraints that are found in complex databases. The EER model includes the following concepts in addition to the ER model concepts  :

- **Subclasses and Superclasses**: A subclass is a subset of entities that belong to a superclass, and inherits all the attributes and relationships of the superclass. A superclass is a superset of entities that share some common attributes or relationships. For example, a subclass STUDENT can be derived from a superclass PERSON, and inherit the attributes name, address, and phone from the superclass.
- **Specialization and Generalization**: Specialization is the process of defining one or more subclasses from a superclass based on some distinguishing characteristics. Generalization is the reverse process of abstraction, where common attributes and relationships are combined from several subclasses to form a superclass. For example, a superclass VEHICLE can be generalized from the subclasses CAR, TRUCK, and BIKE, and have the common attribute license_plate.
- **Category or Union Type**: A category or union type is a subclass that represents a collection of entities from different superclasses that share a common attribute or relationship. A category or union type is also called a shared subclass. For example, a category EMPLOYEE can be derived from the superclasses SALARIED_EMPLOYEE and HOURLY_EMPLOYEE, and have the common attribute employee_id.
- **Aggregation**: Aggregation is the process of grouping together entities and relationships into a single abstract entity type. Aggregation is used to represent a part-of relationship between an entity and a collection of entities. For example, an entity COURSE can be aggregated with the relationship OFFERED_BY to form an abstract entity type COURSE_OFFERING, which represents a part-of relationship between a course and a department.



### Relationship of Higher Degree

- A relationship of higher degree is a relationship that involves more than two entities.
- A relationship of higher degree can be represented by a diamond-shaped symbol with the names of the participating entities around it.
- A relationship of higher degree can have attributes associated with it, which are shown inside the diamond symbol.
- A relationship of higher degree can have cardinality ratios and participation constraints, which are shown by placing numbers and symbols near the entity names.
- A relationship of higher degree can be converted into an equivalent set of binary relationships by introducing a new entity type that represents the relationship and linking it to the original entities.
- A relationship of higher degree can be used to model complex real-world situations, such as a student taking multiple courses taught by multiple instructors, or a product being composed of multiple parts supplied by multiple vendors.



## Unit 2 - Relational Data Model and Language

- Relational Data Model and Language is a way of representing and manipulating data in a relational database.
- A relational database is a type of database that stores data in the form of relations (tables), where each row represents a tuple (record) and each column represents an attribute (field).
- A relational database may use SQL (Structured Query Language) as its language for data definition, manipulation, and querying, but SQL is not the same as the relational model.
- The relational model has some key concepts and terms, such as:

  - Relation: A set of tuples that have the same attributes. A relation is also called a table or a file.
  - Attribute: A property or characteristic of an entity or a relationship. An attribute is also called a field or a column.
  - Tuple: A single data item that consists of a set of attribute values. A tuple is also called a record or a row.
  - Domain: A set of possible values for an attribute. A domain is also called a data type or a format.
  - Key: An attribute or a set of attributes that uniquely identifies a tuple in a relation. A key is also called an identifier or a primary key.
  - Foreign Key: An attribute or a set of attributes in one relation that refers to the key of another relation. A foreign key is also called a reference or a secondary key.
  - Constraint: A rule that specifies some conditions that the data in a relation must satisfy. A constraint is also called a restriction or a validation rule.
  - Schema: A description of the structure and organization of a database. A schema is also called a definition or a specification.
  - Instance: A snapshot of the data in a database at a given point in time. An instance is also called a state or a content.
  - Relational Algebra: A set of operators that can be applied to relations to produce new relations. Relational algebra is used to define and manipulate data in a relational database.
  - Relational Calculus: A set of expressions that can be used to specify queries on relations. Relational calculus is used to retrieve data from a relational database.



### Relational Data Model Concepts

- A relational data model is a way of representing data as a collection of tables, where each table consists of rows and columns .
- The tables are also called relations, and each row in a table is called a tuple .
- Each column in a table is called an attribute, and it represents a property or characteristic of the tuples in the relation .
- A relation schema is the name of the relation and the set of attributes that define it . For example, STUDENT(RollNo, Name, Age, Address) is a relation schema for a table that stores information about students.
- A relation instance is a snapshot of the data in a relation at a given point in time . For example, the following table is a relation instance of the STUDENT relation schema:

| RollNo | Name | Age | Address |
|--------|------|-----|---------|
| 101    | Alice| 20  | A1      |
| 102    | Bob  | 21  | A2      |
| 103    | Carol| 19  | A3      |

- The degree of a relation is the number of attributes in its schema . For example, the degree of the STUDENT relation is 4.
- The cardinality of a relation is the number of tuples in its instance . For example, the cardinality of the STUDENT relation is 3.
- A primary key is an attribute or a set of attributes that uniquely identifies each tuple in a relation . For example, RollNo is a primary key for the STUDENT relation.
- A foreign key is an attribute or a set of attributes in one relation that refers to the primary key of another relation . For example, if there is another relation called COURSE(CourseID, CourseName, Instructor), then CourseID can be a foreign key in a relation called ENROLLMENT(RollNo, CourseID, Grade) that links students and courses.
- A relational database is a collection of relations that are logically connected by primary and foreign keys . For example, the following diagram shows a relational database that consists of four relations: STUDENT, COURSE, ENROLLMENT, and INSTRUCTOR.

Relational Database Diagram

- Relational integrity constraints are rules that ensure the validity and consistency of the data in a relational database . There are two types of relational integrity constraints: domain constraints and referential integrity constraints.
- Domain constraints specify the set of permissible values for each attribute in a relation . For example, the domain constraint for the Age attribute in the STUDENT relation can be that it must be a positive integer.
- Referential integrity constraints ensure that a foreign key value in one relation either matches a primary key value in another relation or is null . For example, the referential integrity constraint for the CourseID attribute in the ENROLLMENT relation can be that it must exist in the COURSE relation or be null.
- Relational data modeling is the process of designing a relational database by identifying the entities, attributes, and relationships that are relevant for the data requirements . Relational data modeling involves the following steps:
  - Define the purpose and scope of the database
  - Identify the entities and their attributes
  - Determine the primary and foreign keys for each relation
  - Normalize the relations to avoid data redundancy and anomalies
  - Draw the entity-relationship diagram to show the logical structure of the database
  - Implement the physical design of the database using a relational database management system (RDBMS)



### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- There are four types of integrity constraints in the relational data model: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

#### Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- For example, the attribute `age` of a relation `student` can have a domain constraint that limits its values to positive integers less than or equal to 150.

#### Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by declaring primary keys or candidate keys for the relations.
- For example, the attribute `student_id` of a relation `student` can be a primary key that uniquely identifies each student.

#### Entity Integrity Constraints

- Entity integrity constraints ensure that each tuple in a relation has a distinct and non-null value for its primary key.
- Entity integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule.
- For example, the relation `student` cannot have two tuples with the same value for `student_id`, or a tuple with a null value for `student_id`.

#### Referential Integrity Constraints

- Referential integrity constraints ensure that the values of a foreign key in a relation match the values of a primary key in another relation.
- Referential integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule, or by cascading the changes to the related tuples.
- For example, the relation `enrollment` has a foreign key `student_id` that references the primary key `student_id` of the relation `student`. If a tuple is inserted or updated in `enrollment` with a value for `student_id` that does not exist in `student`, the referential integrity constraint is violated. This can be prevented by rejecting the operation, or by inserting or updating the corresponding tuple in `student`.



### Entity Integrity for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Entity integrity is a rule that ensures that each record in a table has a unique and non-null identifier, called the primary key  .
- The primary key is a column or a combination of columns that can uniquely identify a row in a table  .
- Entity integrity prevents duplicate records, missing values, and inconsistent data in a table  .
- Entity integrity is essential for maintaining data quality, integrity, and consistency in a relational database  .
- Entity integrity is enforced by the database management system (DBMS) by checking the primary key values before inserting, updating, or deleting data in a table  .
- Entity integrity is also related to referential integrity, which is another rule that ensures that the foreign key values in a table are consistent with the primary key values in the related table.
- Entity integrity and referential integrity are the two main types of data integrity in a relational database .



### Referential Integrity

- Referential integrity is a property of data stating that all its references are valid .
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist .
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key.
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table.
- Referential integrity ensures that relationships between tables remain consistent .
- Referential integrity prevents the insertion, update, or deletion of data that would violate the consistency of the relationships.
- Referential integrity can be enforced by using constraints, triggers, or application logic.
- Referential integrity is a type of data integrity, which is a broader concept that encompasses the accuracy, validity, and consistency of data in a database.



### Keys Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple in a relation.
- A key constraint is a rule that specifies that the values of a key must be distinct for all tuples in a relation.
- There are different types of keys and key constraints in the relational data model, such as:
  - Superkey: a set of attributes that contains a key.
  - Candidate key: a minimal superkey, that is, a superkey that has no proper subset that is also a superkey.
  - Primary key: a candidate key that is chosen by the database designer to identify tuples in a relation.
  - Foreign key: a set of attributes in a relation that references the primary key of another relation (or the same relation).
  - Referential integrity constraint: a rule that ensures that the values of a foreign key match the values of the primary key that it references, or are null.
- Keys and key constraints are important for the following reasons:
  - They ensure the uniqueness and identity of tuples in a relation, which avoids data duplication and inconsistency.
  - They enable the definition of relationships between relations, which allows querying and manipulating data across multiple tables.
  - They support the normalization of relations, which is a process of decomposing relations into smaller and simpler ones that avoid data anomalies.



### Domain Constraints for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Domain constraints are user-defined columns that help the user to enter the value according to the data type.
- Domain constraints specify that each attribute is bound to have a value that lies in a specific range of values.
- Domain constraints ensure that the values of an attribute are atomic, meaning they are the smallest indivisible units.
- Domain constraints can be enforced by using data types, formats, ranges, or sets of permissible values.
- Domain constraints are part of the schema definition of a relation, also known as a table or file.
- Domain constraints are important for maintaining the integrity and consistency of data in a relational database.



### Relational Algebra

- Relational algebra is a theory that uses algebraic structures for modeling data, and defining queries on it with a well founded semantics.
- Relational algebra is a procedural query language, where the user tells the system to carry out a set of operations to obtain the desired results.
- Relational algebra provides a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.
- Relational databases store tabular data represented as relations. Queries over relational databases often likewise return tabular data represented as relations.
- Relational algebra operations are designed to do the most common things that we need to do with relations in a database.

#### Basic Relational Algebra Operations

- **SELECT** (σ): The SELECT operation is used for selecting a subset of the tuples according to a given selection condition . For example, σ<sub>age > 20</sub>(Student) selects all the tuples from the Student relation where the age attribute is greater than 20.
- **PROJECT** (π): The PROJECT operation is used for eliminating all attributes of the input relation but those mentioned in the projection list . For example, π<sub>name, age</sub>(Student) returns a relation with only the name and age attributes of the Student relation.
- **UNION** (∪): The UNION operation is used for combining two relations that have the same set of attributes . For example, Student ∪ Teacher returns a relation that contains all the tuples from both Student and Teacher relations. The result relation does not have any duplicate tuples.
- **INTERSECTION** (∩): The INTERSECTION operation is used for finding the common tuples between two relations that have the same set of attributes . For example, Student ∩ Teacher returns a relation that contains only the tuples that are present in both Student and Teacher relations.
- **DIFFERENCE** (-): The DIFFERENCE operation is used for finding the tuples that are present in one relation but not in another relation that have the same set of attributes . For example, Student - Teacher returns a relation that contains only the tuples that are present in Student but not in Teacher relation.
- **CARTESIAN PRODUCT** (×): The CARTESIAN PRODUCT operation is used for combining every tuple of one relation with every tuple of another relation . For example, Student × Course returns a relation that contains all possible pairs of tuples from Student and Course relations. The result relation has the attributes of both the input relations.



### Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a **non-procedural** query language that describes **what** data to retrieve from a relational database, without specifying **how** to do it  .
- Relational calculus is based on **mathematical logic**, specifically **predicate calculus** , which uses variables, constants, operators, quantifiers, and predicates to form expressions.
- Relational calculus is an **integral part** of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- Relational calculus can be classified into two types: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**   .
- Tuple relational calculus uses **tuple variables** to represent rows of a relation, and checks every row with a **predicate expression** condition . For example, the query to find the names of all students who have enrolled in the course CS101 can be written as:

  `{T.name | STUDENT(T) AND T.course = 'CS101'}`

  where T is a tuple variable, STUDENT is a relation, and name and course are attributes.
- Domain relational calculus uses **domain variables** to represent individual values of attributes, and combines them with a **membership condition** to specify a relation  . For example, the same query as above can be written as:

  `{<x> | ∃y (STUDENT(x, y) AND y = 'CS101')}`

  where x and y are domain variables, STUDENT is a relation, and name and course are attributes.
- Both types of relational calculus are **equivalent** in expressive power, meaning that any query that can be written in one form can also be written in the other form  .
- Relational calculus is also **equivalent** to relational algebra, another query language that is **procedural** and specifies **how** to manipulate data in a relational database  .
- Relational calculus is a **declarative** language that focuses on the **semantics** or meaning of the query, rather than the **syntax** or form of the query  .
- Relational calculus is a **safe** language that guarantees to produce a finite and valid result for any query, as long as the query satisfies the **domain and range restrictions**  . These restrictions ensure that the variables in the query are bound to values from the database, and that the result of the query is a subset of the database.



### Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a declarative query language for relational databases.
- Relational calculus allows users to specify what data they want to retrieve from the database, without specifying how to do it.
- Tuple and domain calculus differ in the way they use variables to represent data.

#### Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables are tuples that belong to a relation.
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate that involves `t` and other constants or variables.
- The result of the query is the set of all tuples `t` that satisfy the predicate `P(t)`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the set of all employees who earn more than 5000.
- TRC can express any query that can be expressed in relational algebra, and vice versa. This means that TRC is relationally complete.

#### Domain Relational Calculus (DRC)

- In domain relational calculus, variables are values that belong to the domains of attributes, rather than tuples of relations.
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `x1, x2, ..., xn` are domain variables and `P(x1, x2, ..., xn)` is a predicate that involves the variables and other constants or relations.
- The result of the query is the set of all ordered n-tuples of values that satisfy the predicate `P(x1, x2, ..., xn)`.
- For example, the query `{<e.Name, e.Salary> | e ∈ Employee and e[Salary] > 5000}` returns the set of all pairs of names and salaries of employees who earn more than 5000.
- DRC can also express any query that can be expressed in relational algebra, and vice versa. However, some queries in DRC may be unsafe, meaning that they may return an infinite number of tuples. Therefore, DRC is not relationally complete unless it is restricted to safe queries.



### Introduction on SQL for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- SQL was developed in the 1970s by IBM and later standardized by ANSI and ISO.
- SQL can perform various operations on data, such as creating, querying, updating, deleting, and controlling access to data.
- SQL is composed of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- SQL is based on the relational model, which represents data as tables consisting of rows and columns. Each table has a name and a set of attributes, which are the columns of the table. Each row of a table is called a tuple, which is an instance of the table. Each attribute has a domain, which is the set of possible values for that attribute.
- SQL supports various data types, such as numeric, character, date, time, boolean, and binary. SQL also supports complex data types, such as arrays, lists, sets, and user-defined types.
- SQL supports various constraints, which are rules that enforce the integrity and consistency of the data. Some common constraints are primary key, foreign key, unique, not null, and check.
- SQL supports various operators, which are symbols that perform calculations or comparisons on data. Some common operators are arithmetic (+, -, *, /, %), comparison (=, <, >, <=, >=, <>, !=), logical (AND, OR, NOT), and set (UNION, INTERSECT, EXCEPT, IN, EXISTS, ANY, ALL).
- SQL supports various functions, which are predefined or user-defined routines that perform specific tasks on data. Some common functions are aggregate (SUM, AVG, MIN, MAX, COUNT, etc.), string (CONCAT, SUBSTR, TRIM, UPPER, LOWER, etc.), date and time (CURRENT_DATE, CURRENT_TIME, EXTRACT, DATE_PART, etc.), and conversion (CAST, COALESCE, NULLIF, etc.).
- SQL supports various clauses, which are keywords that specify the structure and content of a query. Some common clauses are SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT.
- SQL supports various statements, which are complete commands that perform a specific action on data. Some common statements are CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, and GRANT.



### Characteristics of SQL

SQL is a computer language used to store, manipulate, and retrieve data from a relational database. SQL has the following characteristics:

- **Easy to learn**: SQL is an extremely practical and user-friendly language. Even if you have no prior experience with programming, you can learn the basic syntax and commands of SQL in a short time.
- **Wide variety of commands**: SQL supports a wide variety of commands such as DDL (Data Definition Language) commands, DML (Data Manipulation Language) commands, DCL (Data Control Language) commands, and TCL (Transaction Control Language) commands. These commands allow you to perform different tasks on the database, such as creating, modifying, deleting, querying, and controlling data.
- **Stored procedures**: A stored procedure is a set of SQL statements that can be executed as a single unit. Stored procedures can improve the performance, security, and maintainability of the database applications. Stored procedures can also accept parameters and return values.
- **High performance**: SQL provides high-performance programming capability for highly transactional, heavy workload, and high usage database systems. SQL programming gives various ways to describe the data more analytically, such as using aggregate functions, subqueries, joins, and views.
- **Portability**: SQL is a standard language that is supported by most of the relational database management systems, such as Oracle, MySQL, SQL Server, PostgreSQL, and SQLite. SQL can also run on different platforms, such as Windows, Linux, and Mac OS. This makes SQL portable and compatible across different systems.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some advantages of SQL for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Advantages of SQL

- **Faster and efficient query processing**: SQL can process a large amount of data in a very short amount of time. This high speed can boost the amount of data retrieval and manipulation  .
- **No coding skills required**: SQL uses simple English phrases and keywords to perform data operations. For data retrieval, large number of lines of code is not required. All basic keywords such as SELECT, INSERT, UPDATE, DELETE, etc. are easy to learn and use.
- **Standardized language**: SQL is a standardized language that is widely used and supported by many database management systems. SQL follows the ANSI (American National Standards Institute) and ISO (International Organization for Standardization) standards. This makes SQL portable and compatible across different platforms and systems  .
- **Integration**: SQL can be integrated with other programming languages such as Java, C#, Python, etc. to perform complex data operations and analysis. SQL can also be embedded in web applications and scripts to interact with databases.
- **Data security and integrity**: SQL provides various features and functions to ensure data security and integrity. SQL allows the creation of user roles and permissions to control the access and modification of data. SQL also supports data validation, encryption, backup, and recovery mechanisms to protect data from unauthorized or accidental changes .



### SQL Data Types and Literals

SQL data types are used to represent the nature of the data that can be stored in the database table. Every field or column in a table is given a data type when a table is defined. These data types describe the kind of information which can be stored in a column .

SQL literals are the values that are used to represent a constant value in a SQL statement. They are also known as constants. There are four kinds of literal values supported in SQL. They are:

- Character string: A sequence of characters enclosed by single quotes, such as 'Hello' or 'SQL'.
- Bit string: A sequence of binary digits (0 or 1) enclosed by single quotes, such as '1010' or '0011'.
- Exact numeric: A decimal number with a fixed precision and scale, such as 123.45 or 0.01.
- Approximate numeric: A floating-point number with an approximate precision and scale, such as 1.23E4 or 3.14E-2.

Some examples of SQL literals are:

- SELECT 'Hello' AS Greeting;
- SELECT '1010' AS BitString;
- SELECT 123.45 AS ExactNumeric;
- SELECT 1.23E4 AS ApproximateNumeric;

Some of the common SQL data types are :

- CHAR(n): A fixed-length character string of n characters, where n is a positive integer.
- VARCHAR(n): A variable-length character string of up to n characters, where n is a positive integer.
- INT: An integer number with a range of -2,147,483,648 to 2,147,483,647.
- DECIMAL(p, s): A decimal number with a precision of p digits and a scale of s digits, where p and s are positive integers.
- FLOAT(n): A floating-point number with a precision of n bits, where n is a positive integer.
- DATE: A date value in the format of YYYY-MM-DD, such as 2021-12-31.
- TIME: A time value in the format of HH:MM:SS, such as 23:59:59.
- DATETIME: A combination of date and time values, such as 2021-12-31 23:59:59.

Some examples of SQL data types are:

- CREATE TABLE Employee (Name CHAR(20), Salary DECIMAL(10, 2));
- INSERT INTO Employee VALUES ('Alice', 5000.00);
- SELECT Name, Salary FROM Employee WHERE Salary > 4000.00;



### Types of SQL Commands

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL commands are divided into five broad categories based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of database objects such as tables, views, indexes, etc. Some examples of DDL commands are:

  - `CREATE`: This command is used to create a new database object, such as a table, view, index, etc.
  - `ALTER`: This command is used to modify the structure or properties of an existing database object, such as adding or dropping columns, changing data types, renaming objects, etc.
  - `DROP`: This command is used to delete an existing database object, such as a table, view, index, etc.
  - `TRUNCATE`: This command is used to delete all the data from a table, but not the table itself.
  - `RENAME`: This command is used to rename an existing database object, such as a table, view, index, etc.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - `INSERT`: This command is used to insert new data into a table.
  - `UPDATE`: This command is used to modify the existing data in a table.
  - `DELETE`: This command is used to delete the existing data from a table.
  - `SELECT`: This command is used to query or retrieve data from one or more tables.

- **Data Control Language (DCL)**: These commands are used to grant or revoke permissions or access rights to database objects or users. Some examples of DCL commands are:

  - `GRANT`: This command is used to grant permissions or privileges to a user or a role to perform certain operations on database objects.
  - `REVOKE`: This command is used to revoke permissions or privileges from a user or a role to perform certain operations on database objects.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in a database, such as committing or rolling back the changes made by DML commands. Some examples of TCL commands are:

  - `COMMIT`: This command is used to save the changes made by DML commands to the database permanently.
  - `ROLLBACK`: This command is used to undo the changes made by DML commands to the database and restore the previous state.
  - `SAVEPOINT`: This command is used to create a point in a transaction where the changes can be rolled back to if needed.

- **Data Query Language (DQL)**: This is not a separate category of commands, but rather a subset of DML commands that are used to query or retrieve data from database tables. The most common DQL command is `SELECT`, which can be used with various clauses, operators, and functions to filter, sort, group, or aggregate the data. Some examples of DQL commands are:

  - `SELECT * FROM table_name`: This command is used to select all the columns and rows from a table.
  - `SELECT column1, column2 FROM table_name`: This command is used to select specific columns from a table.
  - `SELECT column1, column2 FROM table_name WHERE condition`: This command is used to select specific columns and rows that satisfy a condition from a table.
  - `SELECT column1, column2 FROM table_name ORDER BY column3`: This command is used to select specific columns and rows from a table and sort them by a column.
  - `SELECT column1, column2 FROM table_name GROUP BY column3`: This command is used to select specific columns and rows from a table and group them by a column.
  - `SELECT column1, column2 FROM table_name HAVING condition`: This command is used to select specific columns and rows from a table that satisfy a condition after grouping by a column.
  - `SELECT column1, column2 FROM table_name JOIN table2 ON condition`: This command is used to select specific columns and rows from two or more tables that are related by a condition.



### SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform certain operations on data in a relational database. SQL operators can be classified into four categories:

- Arithmetic operators: These operators are used to perform mathematical calculations on numeric data. For example, `+`, `-`, `*`, `/`, and `%` are arithmetic operators. The procedure for using arithmetic operators is to write them between two operands (values or expressions) that are compatible in data type and size. For example, `SELECT salary + bonus AS income FROM employees;` will add the values of salary and bonus columns and display the result as income.

- Comparison operators: These operators are used to compare two values or expressions and return a Boolean value (TRUE, FALSE, or UNKNOWN) as the result. For example, `=`, `<>`, `<`, `>`, `<=`, `>=`, `BETWEEN`, `IN`, `LIKE`, and `IS NULL` are comparison operators. The procedure for using comparison operators is to write them between two operands that are compatible in data type and size, and use them in conditions such as `WHERE`, `HAVING`, or `JOIN`. For example, `SELECT name FROM students WHERE age BETWEEN 18 AND 22;` will display the names of students whose age is between 18 and 22.

- Logical operators: These operators are used to combine two or more conditions and return a Boolean value as the result. For example, `AND`, `OR`, `NOT`, and `XOR` are logical operators. The procedure for using logical operators is to write them between two or more operands that are Boolean expressions, and use them in conditions such as `WHERE`, `HAVING`, or `JOIN`. For example, `SELECT name FROM customers WHERE city = 'New York' AND gender = 'F';` will display the names of female customers who live in New York.

- Set operators: These operators are used to combine two or more queries and return a single result set. For example, `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT` are set operators. The procedure for using set operators is to write them between two or more operands that are select statements, and make sure that the operands have the same number and data type of columns. For example, `SELECT name FROM employees UNION SELECT name FROM customers;` will display the names of employees and customers without any duplicates.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 2 - Relational data Model and Language in the subject of Database Management System. Here are some tables that you can use for your notes:

### Tables for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

| Relational Data Model | Definition |
| --- | --- |
| Relation | A set of tuples (rows) that have the same attributes (columns) |
| Attribute | A property or characteristic of an entity or relationship type |
| Domain | A set of atomic values that an attribute can take |
| Tuple | An ordered set of attribute values that represent an entity or a relationship instance |
| Degree | The number of attributes in a relation |
| Cardinality | The number of tuples in a relation |
| Primary Key | A minimal set of attributes that uniquely identify a tuple in a relation |
| Foreign Key | A set of attributes in a relation that refer to the primary key of another relation |
| Referential Integrity | A constraint that ensures that a foreign key value either matches a primary key value or is null |

| Relational Algebra | Definition |
| --- | --- |
| Selection | A unary operation that selects a subset of tuples from a relation that satisfy a given condition |
| Projection | A unary operation that selects a subset of attributes from a relation and eliminates duplicates |
| Union | A binary operation that combines two relations with the same degree and compatible domains and eliminates duplicates |
| Intersection | A binary operation that returns the common tuples of two relations with the same degree and compatible domains |
| Difference | A binary operation that returns the tuples of the first relation that are not in the second relation with the same degree and compatible domains |
| Cartesian Product | A binary operation that returns the combination of every tuple of the first relation with every tuple of the second relation |
| Join | A binary operation that combines two relations based on a join condition that specifies how the tuples are matched |
| Natural Join | A special case of join that matches tuples based on the common attributes of the two relations and eliminates duplicates |
| Division | A binary operation that returns the tuples of the first relation that are associated with every tuple of the second relation |

| Relational Calculus | Definition |
| --- | --- |
| Tuple Relational Calculus | A non-procedural query language that specifies the desired tuples using variables, constants, and logical connectives |
| Domain Relational Calculus | A non-procedural query language that specifies the desired tuples using domain variables, constants, and logical connectives |
| Safe Expression | An expression that guarantees to return a finite relation as a result |
| Unsafe Expression | An expression that may return an infinite relation as a result |
| Existential Quantifier | A symbol that denotes the existence of at least one tuple or domain value that satisfies a condition |
| Universal Quantifier | A symbol that denotes the existence of all tuples or domain values that satisfy a condition |



### Views and Indexes

- A **view** is a named query that defines a logical table based on the result of a SELECT statement.
- A view can be used to simplify queries, hide complex joins, restrict access to certain columns or rows, or provide a consistent interface to data that may change over time.
- A view can be created using the CREATE VIEW statement, and can be queried, updated, inserted, or deleted from as if it were a base table.
- A view does not store any data physically, but only references the data in the underlying tables.
- A view can be dropped using the DROP VIEW statement, which does not affect the data in the underlying tables.

- An **index** is a data structure that improves the speed of data retrieval operations on a table by creating a pointer to the location of the data.
- An index can be created on one or more columns of a table, and can be used to quickly find the rows that match a search condition.
- An index can be created using the CREATE INDEX statement, and can be dropped using the DROP INDEX statement.
- An index can also be created on a view, which is called an **indexed view** .
- An indexed view is a view that has been materialized, meaning that the view definition has been computed and the resulting data stored just like a table.
- An indexed view can improve the performance of some types of queries, especially those that involve aggregations, joins, or subqueries.
- An indexed view can be created by creating a unique clustered index on the view using the CREATE UNIQUE CLUSTERED INDEX statement .
- An indexed view has some restrictions, such as the view and the underlying tables must have the same owner, the view must have a schema binding option, and the view must not contain certain elements such as outer joins, subqueries, or non-deterministic functions .



### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A **query** is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language such as SQL, which specifies what data is needed, not how to get it.
- A **subquery** is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used when you need to process data in several steps, or when you want to use the result of one query as an input for another query. Subqueries can also be used to compare values, test for existence, or perform aggregations.
- There are three types of subqueries: scalar, multirow, and correlated.
  - A **scalar subquery** returns a single value that can be used in an expression or a comparison. For example, the following query uses a scalar subquery to find the average salary of all employees:

  ```sql
  SELECT AVG(salary) FROM employees;
  ```

  - A **multirow subquery** returns one or more rows that can be used with operators such as IN, ANY, ALL, or EXISTS. For example, the following query uses a multirow subquery to find the employees who work in the same department as John Smith:

  ```sql
  SELECT name, department FROM employees
  WHERE department IN
  (SELECT department FROM employees
  WHERE name = 'John Smith');
  ```

  - A **correlated subquery** is a subquery that depends on the outer query for its values. It is executed once for each row of the outer query. For example, the following query uses a correlated subquery to find the employees who earn more than the average salary of their department:

  ```sql
  SELECT name, salary, department FROM employees e1
  WHERE salary >
  (SELECT AVG(salary) FROM employees e2
  WHERE e1.department = e2.department);
  ```

- Subqueries can be used in different clauses of a query, such as the WHERE, FROM/JOIN, or SELECT clause. For example, the following query uses a subquery in the FROM clause to join two tables:

  ```sql
  SELECT e.name, e.salary, d.name AS department
  FROM employees e
  JOIN
  (SELECT department_id, name FROM departments) d
  ON e.department = d.department_id;
  ```

- Subqueries can also be nested inside other subqueries, as long as the nesting level does not exceed the limit imposed by the database system. For example, the following query uses a nested subquery to find the employees who work in the same department as the highest-paid employee:

  ```sql
  SELECT name, salary, department FROM employees
  WHERE department =
  (SELECT department FROM employees
  WHERE salary =
  (SELECT MAX(salary) FROM employees));
  ```

- Subqueries are usually contrasted with Common Table Expressions (CTEs) as they have similar use cases. CTEs are temporary named result sets that can be referenced within a query. CTEs can improve the readability and maintainability of complex queries, and can also enable recursive queries. For example, the following query uses a CTE to find the employees who work in the same department as John Smith:

  ```sql
  WITH dept AS
  (SELECT department FROM employees
  WHERE name = 'John Smith')
  SELECT name, department FROM employees
  WHERE department IN dept;
  ```



### Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the `GROUP BY` clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - `COUNT`: returns the number of values in a set or the number of rows that satisfy a condition.
  - `SUM`: returns the sum of all values in a set.
  - `AVG`: returns the average of all values in a set.
  - `MIN`: returns the minimum value in a set.
  - `MAX`: returns the maximum value in a set.

- Aggregate functions can be used in the `SELECT` clause or the `HAVING` clause of a query.
- Aggregate functions ignore `NULL` values in the set, unless otherwise specified.
- Aggregate functions can be combined with other expressions using arithmetic operators, such as `+`, `-`, `*`, `/`, etc.
- Aggregate functions can also be nested within each other, such as `AVG(SUM(salary))`.
- Some examples of queries using aggregate functions are:

  - To find the total number of employees in each department:

    ```sql
    SELECT dept_id, COUNT(*)
    FROM employee
    GROUP BY dept_id;
    ```

  - To find the average salary of employees in each department:

    ```sql
    SELECT dept_id, AVG(salary)
    FROM employee
    GROUP BY dept_id;
    ```

  - To find the highest salary among all employees:

    ```sql
    SELECT MAX(salary)
    FROM employee;
    ```

  - To find the number of employees who earn more than the average salary:

    ```sql
    SELECT COUNT(*)
    FROM employee
    WHERE salary > (SELECT AVG(salary) FROM employee);
    ```



### Relational Data Model and Language

- Relational Data Model and Language is an approach to managing data using a structure and language consistent with first-order predicate logic.
- A relational database stores data in the form of relations (tables), where each row represents a tuple (record) and each column represents an attribute (field).
- A relational database may use SQL (Structured Query Language) as its language, but SQL is not the same thing as a relational model.
- A relational database is designed to organize data and identify relationships between key data points, making it easy to sort and find information.
- A relational database works well for maintaining data integrity and minimizing redundancy. It is often used in point-of-sale systems, as well as for other types of transaction processing.

Some key terms and concepts related to relational data model and language are:

- **Relation**: A relation is a set of tuples that have the same attributes. A relation can be represented as a table, where each row is a tuple and each column is an attribute. A relation has a name and a degree (the number of attributes).
- **Attribute**: An attribute is a property of a relation that describes the characteristics of each tuple. An attribute has a name and a domain (the set of possible values).
- **Tuple**: A tuple is an ordered set of values that correspond to the attributes of a relation. A tuple can be represented as a row in a table. A tuple has a cardinality (the number of values).
- **Key**: A key is an attribute or a set of attributes that uniquely identifies a tuple in a relation. A key can be used to enforce data integrity and referential integrity. A key can be classified as:
  - **Primary key**: A primary key is a key that is chosen by the database designer to identify each tuple in a relation. A primary key cannot have null values or duplicate values.
  - **Candidate key**: A candidate key is a key that can be used as a primary key. A relation may have more than one candidate key, but only one can be chosen as the primary key.
  - **Alternate key**: An alternate key is a candidate key that is not chosen as the primary key. An alternate key can be used as a secondary identifier for a tuple.
  - **Foreign key**: A foreign key is a key that refers to the primary key of another relation. A foreign key can be used to establish a relationship between two relations and enforce referential integrity.
- **Schema**: A schema is a description of the structure and constraints of a database. A schema specifies the name, degree, domain, and key of each relation, as well as the relationships and constraints among the relations.
- **Instance**: An instance is a snapshot of the data stored in a database at a given point in time. An instance consists of a set of tuples for each relation in the schema.
- **Relational algebra**: Relational algebra is a set of operations that can be applied to relations to manipulate and query data. Relational algebra operations can be classified as:
  - **Unary operations**: Unary operations are operations that take one relation as input and produce another relation as output. Examples of unary operations are:
    - **Selection**: Selection is an operation that selects a subset of tuples from a relation that satisfy a given condition. The notation for selection is σ<sub>condition</sub>(relation).
    - **Projection**: Projection is an operation that selects a subset of attributes from a relation and eliminates duplicates. The notation for projection is π<sub>attribute list</sub>(relation).
    - **Rename**: Rename is an operation that changes the name of a relation or an attribute. The notation for rename is ρ<sub>new name</sub>(relation) or ρ<sub>new name/old name</sub>(relation).
  - **Binary operations**: Binary operations are operations that take two relations as input and produce another relation as output. Examples of binary operations are:
    - **Union**: Union is an operation that combines two relations that have the same degree and domain and eliminates duplicates. The notation for union is relation<sub>1</sub> ∪ relation<sub>2</sub>.
    - **Intersection**: Intersection is an operation that selects the common tuples from two relations that have the same degree and domain. The notation for intersection is relation<sub>1</sub> ∩ relation<sub>2</sub>.
    - **Difference**: Difference is an operation that selects the tuples from one relation that are not present in another relation that have the same degree and



### Update and Delete Operations for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes in one or more tuples of a relation, based on a specified condition.
- Delete operations can remove one or more tuples from a relation, based on a specified condition.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and with proper authorization.
- Update and delete operations can be expressed using the relational algebra operators of assignment, selection, projection, and set difference.
- For example, to update the salary of all employees in the EMPLOYEE relation who work in department 5 to 5000, we can write:

  EMPLOYEE := EMPLOYEE - (EMPLOYEE ⋈ DEPT_NO = 5) ∪ (π<EMP_NO, ENAME, JOB, MGR, HIRE_DATE, 5000, COMM, DEPT_NO>(EMPLOYEE ⋈ DEPT_NO = 5))

- To delete all employees in the EMPLOYEE relation who work in department 5, we can write:

  EMPLOYEE := EMPLOYEE - (EMPLOYEE ⋈ DEPT_NO = 5)

- Update and delete operations can also be expressed using the SQL language, which is a widely used standard for relational database manipulation.
- SQL provides the UPDATE and DELETE statements for performing update and delete operations, respectively.
- For example, to update the salary of all employees in the EMPLOYEE table who work in department 5 to 5000, we can write:

  UPDATE EMPLOYEE
  SET SALARY = 5000
  WHERE DEPT_NO = 5;

- To delete all employees in the EMPLOYEE table who work in department 5, we can write:

  DELETE FROM EMPLOYEE
  WHERE DEPT_NO = 5;

- SQL also provides the WHERE clause for specifying the condition for selecting the tuples to be updated or deleted.
- The condition can be a logical expression involving the attributes of the table, constants, comparison operators, logical operators, and parentheses.
- For example, to update the salary of all employees in the EMPLOYEE table who have a salary less than 3000 or more than 7000, we can write:

  UPDATE EMPLOYEE
  SET SALARY = SALARY * 1.1
  WHERE SALARY < 3000 OR SALARY > 7000;

- To delete all employees in the EMPLOYEE table who have a job title of 'CLERK' or 'SALESMAN', we can write:

  DELETE FROM EMPLOYEE
  WHERE JOB IN ('CLERK', 'SALESMAN');

- SQL also provides the SET clause for specifying the new values for the attributes to be updated.
- The new values can be constants, expressions involving the attributes of the table, or subqueries that return a single value.
- For example, to update the salary of all employees in the EMPLOYEE table to be equal to the average salary of their department, we can write:

  UPDATE EMPLOYEE
  SET SALARY = (SELECT AVG(SALARY) FROM EMPLOYEE E2 WHERE E2.DEPT_NO = EMPLOYEE.DEPT_NO);

- To delete all employees in the EMPLOYEE table who have a salary higher than the average salary of their department, we can write:

  DELETE FROM EMPLOYEE
  WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE E2 WHERE E2.DEPT_NO = EMPLOYEE.DEPT_NO);



### Joins for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Joins are operations in relational databases that allow queries across multiple database tables.
- Joins merge data stored in different tables by matching up rows in each table that relate to one another based on some common attributes or foreign key relationships .
- Joins are based on the relational algebra operation of the same name, which is a combination of Cartesian product and selection.
- The most important types of joins are:
  - Theta (θ) join: This join combines tuples from different relations provided they satisfy the theta condition, which is a comparison operator such as =, <, >, etc. The join condition is denoted by the symbol θ.
  - Equijoin: This is a special case of theta join, where the theta condition is only the equality operator. Equijoins are often used to link tables by their primary and foreign keys.
  - Natural join: This join does not use any comparison operator, but instead matches tuples from different relations based on their common attribute names. Natural joins eliminate duplicate columns from the result.
  - Outer join: This join includes tuples from one or both relations that do not have a matching tuple in the other relation. Outer joins can be left, right, or full, depending on which relation's tuples are preserved in the result.
- Joins are useful for accessing data from multiple tables in a single query, and for creating relationships between tables in a data model.
- Joins can be written using different syntaxes, such as using the JOIN keyword, using commas to separate tables, or using subqueries. The syntax may vary depending on the database system and the type of join.



### Unions

- A union is a set operation that combines the tuples of two relations into one relation.
- A union can only be performed on two relations that are **union-compatible**, meaning they have the same number of attributes and the corresponding attributes have the same data type .
- A union eliminates any duplicate tuples from the result relation .
- A union can be expressed in relational algebra as R1 UNION R2, where R1 and R2 are the two relations to be unioned.
- A union can be expressed in SQL as SELECT * FROM R1 UNION SELECT * FROM R2, where R1 and R2 are the two tables to be unioned.
- A union can be used to retrieve data from more than one table simultaneously and then combine the results into one table.
- A union can be useful for combining data from different sources or data models, such as logical tables and physical tables.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of intersection for the unit 2 - relational data model and language in the subject of database management system.

### Intersection

- Intersection is a set operation that returns the common tuples from two relations.
- Intersection is denoted by the symbol ∩.
- Intersection can only be applied to two relations that have the same degree and the same domain for each attribute.
- Intersection is commutative, meaning that R ∩ S = S ∩ R.
- Intersection is associative, meaning that (R ∩ S) ∩ T = R ∩ (S ∩ T).
- Intersection can be expressed in terms of difference, meaning that R ∩ S = R - (R - S).
- Intersection can be implemented using nested loops, hash tables, or sorting and merging algorithms.
- Intersection can be used to find common values or attributes in two relations, such as finding students who are enrolled in both math and physics courses.



### Relational Data Model and Language

- Relational Data Model and Language is a way of organizing and manipulating data in a relational database using tables and SQL .
- A relational database is a collection of relations (tables) that store data in rows (tuples) and columns (attributes)  .
- A relation has a name and a set of attributes. Each attribute has a name and a domain (a set of possible values) .
- A tuple is a row of a relation that represents an entity or a relationship. Each tuple has a value for each attribute of the relation .
- A key is a set of attributes that uniquely identifies a tuple in a relation. A primary key is a key that is chosen to be the main identifier of a relation. A foreign key is a key that references a primary key of another relation .
- A relational schema is a set of relation names and their attributes. A relational database schema is a set of relational schemas that defines the structure of a relational database .
- A relational instance is a set of tuples for each relation in a relational schema. A relational database instance is a set of relational instances that represents the state of a relational database at a given time .
- A relational algebra is a set of operations that can be applied to relations or sets of relations to produce new relations. Relational algebra operations include selection, projection, union, intersection, difference, product, join, division, and renaming .
- A relational calculus is a declarative language that can be used to express queries on relations. Relational calculus uses logical formulas to specify the conditions for selecting tuples from relations. There are two types of relational calculus: tuple relational calculus and domain relational calculus .
- SQL (Structured Query Language) is a widely used language for defining, manipulating, and querying data in relational databases. SQL has three main components: Data Definition Language (DDL), Data Manipulation Language (DML), and Data Query Language (DQL)  .
- DDL is used to create, alter, and drop relations and other database objects. DDL commands include CREATE, ALTER, and DROP .
- DML is used to insert, update, and delete data in relations. DML commands include INSERT, UPDATE, and DELETE .
- DQL is used to retrieve data from relations based on certain criteria. DQL commands include SELECT, FROM, WHERE, GROUP BY, HAVING, and ORDER BY .
- SQL also supports other features such as constraints, indexes, views, functions, triggers, transactions, and authorization .



### Cursors

- A cursor is a database object that allows you to manipulate data in a row-by-row manner.
- A cursor can be thought of as a pointer to a specific row within a query result .
- Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval, addition and removal of database records.
- Cursors are an extension to result sets that provide mechanisms for positioning at specific rows, retrieving one row or block of rows, and supporting data modifications.
- Cursors are useful when you need to perform complex logic on a row-by-row basis, or when you need to access the same result set multiple times.
- Cursors have four steps in their lifecycle: declare, open, fetch, and close .
  - Declare a cursor: A cursor is declared by defining a SQL statement that returns a result set.
  - Open a cursor: A cursor is opened by executing the SQL statement and allocating memory for the result set.
  - Fetch a cursor: A cursor is fetched by moving the pointer to a specific row and retrieving the data from that row.
  - Close a cursor: A cursor is closed by releasing the memory allocated for the result set and deleting the cursor object.
- Cursors can have different types and options that affect their behavior and performance .
  - Static cursor: A static cursor creates a temporary copy of the result set and works on that copy. It is not affected by any changes made to the underlying data.
  - Dynamic cursor: A dynamic cursor reflects any changes made to the underlying data in the result set. It allows scrolling forward and backward, and updating and deleting rows.
  - Forward-only cursor: A forward-only cursor only allows scrolling forward through the result set. It is faster than a static or dynamic cursor, but does not support backward scrolling or data modifications.
  - Keyset-driven cursor: A keyset-driven cursor creates a temporary set of keys that identify the rows in the result set. It allows scrolling forward and backward, and updating rows, but not deleting or inserting rows.
  - Read-only cursor: A read-only cursor does not allow any data modifications to the result set. It is faster than an updatable cursor, but does not support updating, deleting, or inserting rows.
  - Scroll cursor: A scroll cursor allows scrolling forward and backward through the result set. It can be either static, dynamic, or keyset-driven.
  - Updatable cursor: An updatable cursor allows data modifications to the result set. It can be either dynamic or keyset-driven.



### Triggers

- A trigger is a special kind of stored procedure that is executed automatically when a certain event occurs on a table or view in a database.
- A trigger can be used to enforce integrity constraints, audit data changes, implement business rules, or perform other actions based on the data modification.
- A trigger has three main components: a triggering event, a trigger condition, and a trigger action.
- A triggering event is the type of operation that causes the trigger to fire, such as insert, update, or delete.
- A trigger condition is an optional Boolean expression that determines whether the trigger action should be executed or not, based on the data values before and after the triggering event.
- A trigger action is a sequence of SQL statements that are executed when the trigger fires and the trigger condition is true.
- A trigger can be defined as either row-level or statement-level, depending on whether it fires once for each affected row or once for the entire statement.
- A trigger can also be defined as either before or after, depending on whether it fires before or after the triggering event.
- A trigger can be created, altered, dropped, enabled, or disabled using the SQL commands CREATE TRIGGER, ALTER TRIGGER, DROP TRIGGER, ENABLE TRIGGER, or DISABLE TRIGGER, respectively.
- A trigger can be queried using the data dictionary views, such as USER_TRIGGERS, ALL_TRIGGERS, or DBA_TRIGGERS, depending on the level of access.



### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it cannot return a value like a function.
- A procedure can be invoked by other PL/SQL blocks, triggers, procedures, functions, or applications written in different languages such as Java, PHP, etc.
- A procedure has a header and a body. The header contains the keyword PROCEDURE, the name of the procedure, and the list of parameters in parentheses. The body contains the keyword IS (or AS), the declaration section, the keyword BEGIN, the executable section, and the keyword END.
- A procedure can be created using the CREATE PROCEDURE statement, or using a PL/SQL block with the keyword CREATE OR REPLACE PROCEDURE.
- A procedure can be executed using the EXECUTE statement, or by using the procedure name followed by the list of arguments in parentheses.
- A procedure can be modified using the ALTER PROCEDURE statement, or by using a PL/SQL block with the keyword CREATE OR REPLACE PROCEDURE.
- A procedure can be deleted using the DROP PROCEDURE statement.

Some examples of procedures in SQL/PL SQL are:

- A procedure to increase the salary of an employee by a given percentage:

```sql
CREATE OR REPLACE PROCEDURE adjust_salary (p_emp_id IN NUMBER, p_percent IN NUMBER)
IS
  v_salary NUMBER;
BEGIN
  SELECT salary INTO v_salary FROM employees WHERE employee_id = p_emp_id;
  UPDATE employees SET salary = v_salary * (1 + p_percent/100) WHERE employee_id = p_emp_id;
  COMMIT;
END;
```

- A procedure to display the details of an employee:

```sql
CREATE OR REPLACE PROCEDURE show_employee (p_emp_id IN NUMBER)
IS
  v_first_name VARCHAR2(20);
  v_last_name VARCHAR2(20);
  v_email VARCHAR2(25);
  v_salary NUMBER;
BEGIN
  SELECT first_name, last_name, email, salary INTO v_first_name, v_last_name, v_email, v_salary FROM employees WHERE employee_id = p_emp_id;
  DBMS_OUTPUT.PUT_LINE('Employee ID: ' || p_emp_id);
  DBMS_OUTPUT.PUT_LINE('First Name: ' || v_first_name);
  DBMS_OUTPUT.PUT_LINE('Last Name: ' || v_last_name);
  DBMS_OUTPUT.PUT_LINE('Email: ' || v_email);
  DBMS_OUTPUT.PUT_LINE('Salary: ' || v_salary);
END;
```

- A procedure to insert a new employee into the database:

```sql
CREATE OR REPLACE PROCEDURE add_employee (p_first_name IN VARCHAR2, p_last_name IN VARCHAR2, p_email IN VARCHAR2, p_salary IN NUMBER)
IS
  v_emp_id NUMBER;
BEGIN
  SELECT MAX(employee_id) + 1 INTO v_emp_id FROM employees;
  INSERT INTO employees (employee_id, first_name, last_name, email, salary) VALUES (v_emp_id, p_first_name, p_last_name, p_email, p_salary);
  COMMIT;
END;
```



## Unit 3 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing data into tables with well-defined relationships and constraints.
- The main steps of database design are:
  - Requirement analysis: Identify the purpose, scope, and users of the database system.
  - Conceptual design: Create an abstract model of the data using a high-level notation such as entity-relationship (ER) diagrams or unified modeling language (UML) diagrams.
  - Logical design: Translate the conceptual model into a logical schema using a specific data model such as relational, hierarchical, or network.
  - Physical design: Choose the physical storage structures, access methods, and performance tuning parameters for the database system.
- The main benefits of normalization are:
  - Eliminate data anomalies: Data anomalies are inconsistencies or errors that occur when data is inserted, updated, or deleted in a database. Normalization prevents data anomalies by ensuring that each piece of data is stored in only one place and that the dependencies among data are properly enforced by the database system.
  - Minimize data redundancy: Data redundancy is the duplication of data in a database. Normalization minimizes data redundancy by eliminating unnecessary or derived attributes and by splitting large tables into smaller ones with fewer columns.
  - Enhance data integrity: Data integrity is the accuracy and consistency of data in a database. Normalization enhances data integrity by defining primary keys, foreign keys, and other constraints that ensure the validity and uniqueness of data.
- The main levels of normalization are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or arrays of data. Each row represents a single record and each column represents a single attribute. All values are atomic, meaning they cannot be further decomposed into smaller parts.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. Functional dependency means that the value of one attribute determines the value of another attribute. Full functional dependency means that the dependency cannot be reduced to a subset of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. Transitive dependency means that the value of one attribute depends on the value of another attribute that is not part of the primary key. Non-transitive dependency means that the dependency is direct and not indirect.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key. A determinant is an attribute or a set of attributes that determines the value of another attribute. A candidate key is a minimal set of attributes that uniquely identifies a record in a table.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies. A multi-valued dependency means that the value of one attribute depends on the value of another attribute, and both attributes are part of the primary key.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies. A join dependency means that a table can be decomposed into two or more tables and then reconstructed by joining them on their common attributes without losing any information.



### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database  .
- A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X is called the determinant and Y is called the dependent  .
- A functional dependency X -> Y means that for every valid instance of X, that value of X uniquely determines the value of Y .
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A trivial functional dependency is one where the dependent is always a subset of the determinant. For example, A -> A or A -> AB are trivial functional dependencies .
  - Non-trivial functional dependency: A non-trivial functional dependency is one where the dependent is strictly not a subset of the determinant. For example, A -> B or AB -> C are non-trivial functional dependencies .
  - Multivalued functional dependency: A multivalued functional dependency is one where the determinant determines more than one attribute that are independent of each other. For example, A ->> B and A ->> C are multivalued functional dependencies, where B and C are independent of each other .
  - Transitive functional dependency: A transitive functional dependency is one where the determinant determines another attribute that in turn determines the dependent. For example, A -> B and B -> C are transitive functional dependencies, where A determines B and B determines C .
- Functional dependencies are used to define various normal forms of a relation, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF) .
- Normalization is the process of decomposing a relation into smaller relations that satisfy certain properties, such as eliminating partial dependencies, transitive dependencies, multivalued dependencies, and join dependencies .
- Normalization helps to achieve the following objectives :
  - Reduce data redundancy and duplication
  - Avoid data anomalies, such as insertion, deletion, and update anomalies
  - Preserve data integrity and consistency
  - Enhance data security and performance
  - Simplify data manipulation and querying



### Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

- Normal forms are used to eliminate or reduce redundancy in database tables and to ensure data integrity.
- Normalization is the process of structuring a relational database in accordance with a series of normal forms.
- There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are 1NF, 2NF, 3NF, and BCNF.
- A relation is in 1NF if it does not contain any composite or multi-valued attribute. That is, each attribute should be atomic and have a single value for each tuple.
- A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there should be no partial dependency of any attribute on the primary key.
- A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there should be no transitive dependency of any attribute on the primary key.
- A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there should be no dependency of any attribute on a non-key attribute.
- Normalization helps to avoid anomalies such as insertion, deletion, and update anomalies that can occur when data is redundant or inconsistent.
- Normalization also helps to improve the performance and efficiency of the database by reducing the size of the tables and the number of joins required.
- Normalization has some drawbacks such as increased complexity, loss of information, and reduced query flexibility.



### Unit 3 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- The benefits of database normalization are:
  - It improves the clarity and consistency of the data and its relationships.
  - It avoids data anomalies such as insertion, deletion, and update anomalies that can cause data inconsistency and corruption.
  - It reduces the storage space and improves the performance of the database system.
  - It makes the database more flexible and adaptable to changing business requirements.
- The drawbacks of database normalization are:
  - It may increase the number of tables and joins, which can complicate the queries and affect the performance of the database system.
  - It may lose some information that is derived from the original table, such as the total amount of an order or the average salary of an employee.
  - It may not be suitable for some applications that require denormalized data for analytical or reporting purposes.
- The process of database normalization involves applying a series of rules or normal forms to a table until it satisfies a certain level of normalization. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic or indivisible.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key or the whole key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key or the whole key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key or a superkey.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and it has no multivalued dependencies or independent relationships between non-key attributes.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and it has no join dependencies or lossless decompositions that are not implied by the candidate keys.
- The steps to normalize a table are:
  - Identify the functional dependencies and candidate keys of the table.
  - Check if the table is in 1NF and eliminate any repeating groups or multivalued attributes by creating new tables and establishing foreign key relationships.
  - Check if the table is in 2NF and eliminate any partial dependencies by creating new tables and establishing foreign key relationships.
  - Check if the table is in 3NF and eliminate any transitive dependencies by creating new tables and establishing foreign key relationships.
  - Check if the table is in BCNF and eliminate any non-key determinants that are not candidate keys by creating new tables and establishing foreign key relationships.
  - Check if the table is in 4NF and eliminate any multivalued dependencies by creating new tables and establishing foreign key relationships.
  - Check if the table is in 5NF and eliminate any join dependencies that are not implied by the candidate keys by creating new tables and establishing foreign key relationships.
- An example of database normalization is:

  - Consider a table called Employee that stores the employee ID, name, department, salary, and projects of each employee in a company.

  | EmployeeID | Name | Department | Salary | Projects |
  | --- | --- | --- | --- | --- |
  | 101 | Alice | Sales | 5000 | A, B |
  | 102 | Bob | Marketing | 6000 | B, C |
  | 103 | Charlie | Sales | 7000 | A, C |
  | 104 | David | Marketing | 8000 | C, D |

  - The functional dependencies of the table are:

    - EmployeeID -> Name, Department, Salary
    - Department -> Salary
    - EmployeeID, Project -> Project

  - The candidate keys of the table are:

    - EmployeeID
    - EmployeeID, Project

  - The table is not in 1NF because it has a multivalued attribute (Projects) that can have more than one value for each employee.

  - To convert the table to 1NF, we create a new table called EmployeeProject that stores the employee ID



### Second

- Database design is the process of organizing the data and relationships in a database system to achieve optimal performance, accuracy, and integrity.
- Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies.
- Normalization involves decomposing a table into less redundant (and smaller) tables without losing information; defining foreign keys in the old table referencing the primary keys of the new ones. The objective is to isolate data so that additions, deletions, and modifications of an attribute can be made in just one table and then propagated through the rest of the database via the defined foreign keys.
- There are different levels of normalization, called normal forms, that follow certain rules or criteria. The higher the normal form, the more normalized the database is. The most common normal forms are:

  - First normal form (1NF): A table is in 1NF if it contains no repeating groups of data and every attribute value is atomic (not divisible into smaller parts).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there is no partial dependency of any attribute on a part of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there is no dependency of any attribute on another non-key attribute.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key. A determinant is an attribute or a set of attributes that uniquely determines another attribute in a functional dependency.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies. A multi-valued dependency occurs when a determinant can determine multiple values of another attribute independently of each other.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies. A join dependency occurs when a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys without any loss or duplication of data.

- Normalization has many benefits, such as:

  - It reduces the amount of space a database consumes by eliminating duplicate data.
  - It makes it easier to maintain and update the database without causing data inconsistency or integrity problems.
  - It improves the efficiency of queries by reducing the number of joins and indexes required.
  - It ensures that the database conforms to the rules of the relational model and supports the basic relational operations.

- Normalization also has some drawbacks, such as:

  - It can increase the complexity of the database design by creating more tables and relationships.
  - It can increase the number of queries and transactions needed to perform certain operations, which can affect performance and concurrency.
  - It can make some business rules or constraints harder to enforce or implement at the database level.



### Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two or more non-prime attributes that are indirectly determined by the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name.
  - The primary key is (Student ID, Course ID).
  - The non-prime attributes are Student Name, Course Name, Instructor ID, Instructor Name.
  - There is a transitive dependency between Course Name and Course ID, and between Instructor Name and Instructor ID, because they are functionally dependent on each other and not on the primary key.
  - To convert this table to 3NF, we need to remove the transitive dependencies by creating separate tables for Course and Instructor, and referencing them by their IDs in the original table.
- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the Third Normal Form.
  - The Third Normal Form ensures functional dependency preserving and lossless decomposition, which means that the original data can be reconstructed from the normalized tables without any loss or inconsistency.
  - The Third Normal Form reduces the storage space and improves the performance of the database queries.



### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form)   .
- A relation is in BCNF if it is in 3NF and for every functional dependency X -> Y, X is a super key or a candidate key    .
- A super key is a set of attributes that can uniquely identify a tuple in a relation .
- A candidate key is a minimal super key, that is, a super key that does not contain any redundant attribute .
- A functional dependency X -> Y means that the values of Y are determined by the values of X .
- A relation that is not in BCNF may have redundancy, inconsistency, and update anomalies   .
- To convert a relation into BCNF, we need to decompose it into smaller relations that satisfy the BCNF condition   .
- Decomposition should preserve the functional dependencies and the information of the original relation  .
- An example of a relation that is not in BCNF and how to decompose it into BCNF is given below :

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 |
| 1 | 2 | 6 | 7 | 8 |
| 9 | 10| 3 | 4 | 5 |
| 9 | 10| 6 | 7 | 8 |

- The relation R(ABCDE) has the following functional dependencies: FD = {A -> BC, C -> DE}
- The candidate key is {A}
- The functional dependency C -> DE violates the BCNF condition, because C is not a super key or a candidate key
- To decompose R into BCNF, we can split it into two relations: R1(AC) and R2(CDE)
- R1 and R2 are in BCNF, because the only functional dependencies are A -> C and C -> DE, and both A and C are candidate keys in their respective relations
- R1 and R2 also preserve the functional dependencies and the information of R, because we can join them on the common attribute C to get back R

| A | C |
|---|---|
| 1 | 3 |
| 1 | 6 |
| 9 | 3 |
| 9 | 6 |

| C | D | E |
|---|---|---|
| 3 | 4 | 5 |
| 6 | 7 | 8 |

- The advantages of BCNF are that it reduces redundancy, inconsistency, and update anomalies, and ensures data integrity and normalization   .



### Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a statement in which some columns of a relation are contained in other columns of the same or different relation.
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed.
- Inclusion dependency is a generalized form of referential constraints, which are used to enforce the integrity of the data.
- A foreign key is an example of inclusion dependency, where the values of a column in one relation must be a subset of the values of a column in another relation.
- The syntax of inclusion dependency is R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ means subset.
- The inclusion dependency holds for a database if each tuple that is a member of the relation corresponding to the left-hand side is also in the relation corresponding to the right-hand side.
- Inclusion dependency can be checked by using the SQL query: SELECT * FROM R WHERE NOT EXISTS (SELECT * FROM S WHERE R.A1 = S.B1 AND R.A2 = S.B2 AND ... AND R.An = S.Bn).
- Inclusion dependency can be violated by inserting, deleting, or updating tuples in either relation. To prevent this, triggers or constraints can be used to enforce the inclusion dependency.



### Lossless Join Decomposition

- Lossless join decomposition is a process of decomposing a relation R into two or more relations R1, R2, ... such that a natural join of the smaller relations yields back the original relation R  .
- This property guarantees that no information is lost from the original relation during the decomposition and that no spurious tuples are generated .
- Lossless join decomposition is essential for removing redundancy and anomalies from databases while preserving the original data .
- A decomposition of R into R1 and R2 is lossless if and only if at least one of the following functional dependencies holds in the closure of the set of functional dependencies of R  :
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- The above condition can be checked using the following algorithm:
  - Create a table with R1 attributes as rows and R2 attributes as columns.
  - Mark the cells that correspond to the common attributes of R1 and R2 with the attribute name.
  - For each functional dependency X → Y in the closure of the set of functional dependencies of R, mark the cells that correspond to X and Y with the same symbol (e.g., *).
  - Repeat the previous step until no more cells can be marked.
  - If all the cells in a row or a column are marked with the same symbol, then the decomposition is lossless. Otherwise, it is lossy.



### Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Normal forms are defined based on the concept of functional dependencies (FDs).

A functional dependency (FD) is a constraint that describes the relationship between attributes in a relation. It has the form X -> Y, where X and Y are sets of attributes of the relation. It means that the values of Y are determined by the values of X. In other words, if two tuples have the same values for X, they must also have the same values for Y.

For example, consider a relation Student with attributes StudentID, Name, Address, and Course. A possible FD for this relation is StudentID -> Name, which means that the name of a student is uniquely determined by their student ID. Another possible FD is Course -> Address, which means that the address of a student is determined by the course they are enrolled in.

The main steps of normalization using FDs are:

- Identify all the candidate keys of the relation. A candidate key is a minimal set of attributes that can uniquely identify a tuple in the relation.
- Identify all the FDs that hold in the relation. This can be done by analyzing the meaning and semantics of the attributes and the data.
- Check if the relation satisfies the normal forms. There are different levels of normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF). Each normal form has a specific condition that the relation must satisfy based on the FDs.
- If the relation does not satisfy a normal form, decompose it into smaller relations that do. This can be done by using different algorithms, such as synthesis algorithm or decomposition algorithm. The goal is to preserve the FDs and the data in the original relation, and to avoid creating new anomalies or redundancy.
- Repeat the steps for each of the smaller relations until all of them are in the desired normal form.

Some of the benefits of normalization using FDs are:

- It reduces data redundancy and storage space.
- It avoids update, insertion, and deletion anomalies that can cause data inconsistency.
- It improves data integrity and quality.
- It facilitates query processing and optimization.



### MVD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- MVD stands for **Multivalued Dependency** , which is a type of constraint between two sets of attributes in a relation.
- MVD means that for a single value of attribute A, multiple values of attribute B exist. For example, if a person has multiple hobbies and works on multiple projects, then there is a MVD between the person and the hobbies, and between the person and the projects.
- MVD is written as A --> --> B, which means A is multivalued dependent on B . This implies that the values of B are independent of each other for a given value of A.
- MVD plays a role in the **Fourth Normal Form (4NF)** of database normalization  , which is a process of eliminating redundancy and inconsistency in data .
- A relation is in 4NF if it is in **Boyce-Codd Normal Form (BCNF)** and has no MVD  . BCNF is a stricter version of **Third Normal Form (3NF)**, which requires that every determinant of a relation be a candidate key.
- To check for MVD, we can use the **complementation rule** , which states that if A --> --> B holds in a relation R, then A --> --> (R - (A U B)) also holds, where R - (A U B) is the set of attributes in R that are not in A or B .
- To remove MVD, we can use the **decomposition rule** , which states that if A --> --> B holds in a relation R, then we can decompose R into two relations: R1(A, B) and R2(A, R - (A U B)), where R1 and R2 are in 4NF .
- Decomposing a relation into 4NF preserves the **lossless join property** , which means that we can reconstruct the original relation from the decomposed relations by using the natural join operation .
- Decomposing a relation into 4NF may or may not preserve the **dependency preservation property** , which means that we can check the functional dependencies of the original relation by using the functional dependencies of the decomposed relations .



# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, and relationships that represent the information and business rules of a domain.
- Database design also involves choosing appropriate data types, constraints, indexes, and other properties for the tables and columns.
- Database design aims to achieve the following objectives:
  - Reduce data redundancy and inconsistency by avoiding duplication and conflicts.
  - Ensure data integrity and accuracy by enforcing rules and constraints on the data.
  - Enhance data security and privacy by restricting access and manipulation of the data.
  - Improve data performance and scalability by optimizing the storage and retrieval of the data.
  - Facilitate data maintenance and evolution by allowing changes and updates to the data structure.

## Database Normalization
- Database normalization is a technique of database design that organizes the data into tables and columns that are related and independent of each other.
- Database normalization reduces data redundancy and inconsistency by eliminating repeating groups, partial dependencies, and transitive dependencies among the data elements.
- Database normalization also simplifies the database design by ensuring that each table has a single purpose and a clear definition of its primary key and foreign keys.
- Database normalization is based on the concept of normal forms, which are rules and criteria that define the level of normalization of a database.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values (i.e., values that cannot be further divided) and has no repeating groups (i.e., columns that store multiple values of the same type).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (i.e., a column or a set of columns that uniquely determines another column) is a candidate key (i.e., a minimal set of columns that can uniquely identify a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies (i.e., dependencies among two or more columns that are not caused by the primary key).
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (i.e., dependencies that require joining two or more tables to represent the data).
- Database normalization has the following benefits:
  - It reduces data anomalies (i.e., errors or inconsistencies that occur when inserting, updating, or deleting data) by ensuring that each piece of data is stored in one place and is updated consistently.
  - It improves data quality and reliability by enforcing data integrity and accuracy through constraints and rules.
  - It increases data efficiency and flexibility by minimizing the storage space and maximizing the query performance of the data.
  - It facilitates data evolution and maintenance by allowing changes and updates to the data structure without affecting the existing data and applications.



### Alternative Approaches to Database Design

- Database design is the process of defining the structure, organization, and relationships of data in a database.
- Database design can be influenced by various factors, such as the requirements of the application, the characteristics of the data, the performance and scalability needs, and the preferences of the database designer or developer.
- There are different approaches and techniques that can be used to design a database, depending on the context and the goals of the project. Some of the alternative approaches to database design are:

  - **Top-down design**: This approach starts with a high-level conceptual model of the data, such as an entity-relationship diagram (ERD), and then refines it into a logical and physical model. This approach is useful for capturing the business rules and the semantics of the data, and for ensuring consistency and integrity across the database. However, this approach can also be time-consuming, rigid, and difficult to adapt to changing requirements or data sources.

  - **Bottom-up design**: This approach starts with the existing data sources, such as files, spreadsheets, or legacy databases, and then extracts the common attributes and relationships among them to form a logical and physical model. This approach is useful for integrating heterogeneous data sources, and for leveraging the existing data structures and formats. However, this approach can also result in redundancy, inconsistency, and lack of normalization in the database.

  - **Agile design**: This approach follows the principles of agile software development, such as iterative, incremental, and collaborative development, and applies them to database design. This approach involves creating a minimal viable product (MVP) of the database, and then refining and evolving it based on user feedback and changing requirements. This approach is useful for adapting to dynamic and complex environments, and for delivering value to the users quickly and frequently. However, this approach can also result in poor documentation, technical debt, and lack of quality assurance in the database.

  - **NoSQL design**: This approach uses non-relational database systems, such as document, key-value, graph, or columnar databases, to store and manage data. This approach does not follow the traditional relational model, such as tables, rows, columns, and foreign keys, but rather uses alternative data structures, such as JSON documents, key-value pairs, nodes and edges, or wide columns. This approach is useful for handling large and unstructured data sets, and for providing high performance, scalability, and flexibility. However, this approach can also result in loss of consistency, integrity, and standardization in the database.



## Unit 4 - Transaction Processing Concept

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database or a file system .
- A **transaction processing system (TPS)** is a software system that executes transactions and ensures that they are performed reliably and consistently.
- A transaction has four main properties, known as **ACID** :
  - **Atomicity**: A transaction must either complete all of its operations or none of them. If any operation fails, the transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction must preserve the integrity and validity of the database. It must not violate any constraints, rules, or triggers defined on the data.
  - **Isolation**: A transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only one running on the system.
  - **Durability**: A transaction must ensure that its effects are permanent and persist even in the case of system failures or power outages.
- A transaction can have one of the following outcomes:
  - **Commit**: The transaction successfully completes all of its operations and the changes are made permanent in the database.
  - **Abort**: The transaction fails to complete some or all of its operations and the changes are discarded. The database is restored to its previous state.
  - **Partial commit**: The transaction completes some of its operations but not all of them. This is an undesirable outcome and should be avoided by using atomicity.
- A transaction can be executed in two modes:
  - **Flat**: The transaction is executed as a single unit without any subtransactions or savepoints. The transaction can only commit or abort as a whole.
  - **Nested**: The transaction is divided into subtransactions that can have their own commit or abort points. The subtransactions can also be nested within other subtransactions. The transaction can commit or abort partially depending on the outcome of the subtransactions.
- A transaction can be classified into two types based on the nature of its operations:
  - **Read-only**: The transaction only reads data from the database and does not modify it. It does not need to lock any data or log any changes. It can be executed concurrently with other transactions without any conflicts.
  - **Update**: The transaction reads and writes data to the database. It needs to lock the data it accesses and log the changes it makes. It may conflict with other transactions that access the same data.



### Transaction System for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A transaction system is a database system that supports the execution of transactions, which are units of work that must be performed atomically and consistently.
- A transaction system ensures that the database remains in a consistent state after each transaction, and that concurrent transactions do not interfere with each other.
- A transaction system provides the following properties, also known as ACID properties:
  - Atomicity: A transaction is either executed completely or not at all. If a transaction fails, the database is restored to its original state before the transaction started.
  - Consistency: A transaction preserves the integrity constraints and business rules of the database. The database is always in a valid state before and after a transaction.
  - Isolation: A transaction is executed as if it were the only one running in the system. The intermediate results of a transaction are not visible to other transactions, and vice versa.
  - Durability: The effects of a committed transaction are permanent and cannot be lost due to system failures or power outages.
- A transaction system implements various mechanisms to achieve these properties, such as:
  - Locking: A technique that prevents concurrent transactions from accessing or modifying the same data item. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. Locks can be shared or exclusive, depending on the type of operation.
  - Logging: A technique that records the changes made by transactions to the database in a persistent storage device, such as a disk. A log contains information about the transaction id, the data item, the old value, and the new value. Logs are used to undo or redo transactions in case of failures or rollbacks.
  - Recovery: A technique that restores the database to a consistent state after a failure or a rollback. Recovery uses the logs to undo the effects of incomplete or aborted transactions, and to redo the effects of committed transactions that may have been lost due to failures.
  - Concurrency control: A technique that coordinates the execution of concurrent transactions to ensure isolation and consistency. Concurrency control uses locking, timestamps, or other methods to determine the order and validity of transactions. Concurrency control also detects and resolves conflicts and deadlocks among transactions.



### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to some serial schedule, where the transactions are executed one after the other without any interleaving of operations.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stronger notion of serializability that requires that any two conflicting operations (read or write on the same data item) of two transactions in a schedule must have the same order as in some serial schedule.
- View serializability is a weaker notion of serializability that requires that any two transactions in a schedule must have the same read and write operations on the same data items as in some serial schedule, but not necessarily the same order of conflicting operations.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph or a precedence graph is a directed graph of the transactions in a schedule, where an edge from transaction Ti to transaction Tj indicates that Ti must precede Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its serialization graph is acyclic, meaning that it does not contain any cycles of edges.
- A schedule is view serializable if and only if it is conflict serializable or it can be transformed into a conflict serializable schedule by swapping non-conflicting operations.
- To construct a serialization graph for a given schedule, we follow these steps:
  - Create a node for each transaction in the schedule.
  - For each pair of conflicting operations (read or write on the same data item) of two transactions Ti and Tj in the schedule, draw an edge from Ti to Tj if Ti appears before Tj in the schedule.
  - Check if the graph is acyclic. If yes, then the schedule is conflict serializable and the serial order of transactions is given by the topological sorting of the graph. If no, then the schedule is not conflict serializable and may or may not be view serializable.
- To check if a schedule is view serializable, we can use the following algorithm:
  - Construct the serialization graph for the schedule as described above.
  - If the graph is acyclic, then the schedule is view serializable and the serial order of transactions is given by the topological sorting of the graph.
  - If the graph is cyclic, then check if the cycle can be broken by swapping non-conflicting operations of adjacent transactions in the cycle. If yes, then the schedule is view serializable and the serial order of transactions is given by the topological sorting of the modified graph. If no, then the schedule is not view serializable.
- Example: Consider the following schedule of three transactions T1, T2 and T3:

| T1 | T2 | T3 |
|----|----|----|
| R(A) |    |    |
| W(A) |    |    |
|     | R(B) |    |
|     | W(B) |    |
|     |    | R(A) |
|     |    | W(A) |
|     |    | R(B) |
|     |    | W(B) |

- To test the serializability of this schedule, we construct the serialization graph as follows:

serialization graph

- The graph is cyclic, so the schedule is not conflict serializable. However, we can swap the non-conflicting operations R(A) and W(A) of T1 and T3 in the cycle to break the cycle and obtain the following modified schedule:

| T1 | T2 | T3 |
|----|----|----|
|     |    | R(A) |
|     |    | W(A) |
| R(A) |    |    |
| W(A) |    |    |
|     | R(B) |    |
|     | W(B) |    |
|     |    | R(B) |
|     |    | W(B) |

- The serialization graph for the modified schedule is as follows:

modified serialization graph

- The graph is ac



### Serializability of Schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- Serializability is a desirable property of a schedule because it ensures that concurrent transactions do not interfere with each other and preserve the consistency and concurrency of the database .
- There are two main methods to check the serializability of a schedule: conflict serializability and view serializability.
- Conflict serializability: A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations, which are operations that access different data items or are both read operations .
- View serializability: A schedule is view serializable if it is view equivalent to a serial schedule, which means that it preserves the following three conditions :
  - The same transaction reads the initial value of each data item in both schedules.
  - The same transaction writes the final value of each data item in both schedules.
  - The same transaction reads the value of each data item written by another transaction in both schedules.
- Conflict serializability is a stricter criterion than view serializability, which means that every conflict serializable schedule is also view serializable, but not vice versa .
- Serializability can be tested by using a precedence graph, which is a directed graph where the nodes represent transactions and the edges represent conflicts between operations .
- A schedule is conflict serializable if and only if its precedence graph is acyclic .
- A schedule is view serializable if and only if it has a view equivalent serial schedule, which can be found by using a polygraph, which is a directed graph where the nodes represent data items and the edges represent read-write dependencies between transactions .



### Conflict & View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- Conflict serializability is a property of a schedule that ensures the consistency of the database.
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
- Therefore, S is conflict serializable.

#### View Serializability

- View serializability is another property of a schedule that ensures the consistency of the database.
- A schedule is view serializable if it is view equivalent to some serial schedule, meaning that it preserves the following conditions:
  - The same transaction performs the initial read of each data item in both schedules.
  - The same transaction performs the final write of each data item in both schedules.
  - The same set of values are read and written for each data item in both schedules.
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
- The schedule S is not conflict serializable, as it cannot be transformed into a serial schedule by swapping non-conflicting operations.
- However, the schedule S is view serializable, as it is view equivalent to the following serial schedule S'':

| T1 | T2 |
|----|----|
|     | R(A) |
|     | W(A) |
|     | R(B) |
|     | W(B) |
| R(A) |    |
| R(B) |    |
| W(B) |    |

- The schedule S'' is serial and preserves the view conditions of S, as follows:
  - The same transaction (T1) performs the initial read of A in both schedules.
  - The same transaction (T2) performs the final write of A in both schedules.
  - The same transaction (T1) performs the initial read of B in both schedules.
  - The same transaction (T2) performs the final write of B in both schedules.
  - The same set of values are read and written for A and B in both schedules.
- Therefore, S is view serializable.



### Recoverability

- Recoverability is the property of a schedule that ensures that the database state is consistent after a transaction failure or system crash .
- A schedule is recoverable if it does not contain any dirty read, which is when a transaction reads a data item that is written by another uncommitted transaction .
- A schedule is irrecoverable if it contains a dirty read and the transaction that performs the dirty read commits before the transaction that writes the data item commits or aborts .
- A schedule is cascading abort if it contains a dirty read and the transaction that performs the dirty read aborts, causing the transaction that writes the data item to abort as well.
- A schedule is strict if it does not allow any transaction to read or write a data item until the transaction that last wrote the data item commits or aborts.
- A schedule is rigorous if it does not allow any transaction to read or write a data item until the transaction that first wrote the data item commits or aborts.
- Strict and rigorous schedules are recoverable and avoid cascading aborts, but they may reduce concurrency and performance.
- Recoverability is important for online transaction processing (OLTP) systems, which handle a large number of short and concurrent transactions that access and modify the database.
- Recoverability is achieved by using recovery techniques, such as logging, checkpointing, shadow paging, and locking .
- Recovery techniques ensure that the database can be restored to a consistent state after a transaction failure or system crash, by undoing the effects of uncommitted transactions and redoing the effects of committed transactions .



### Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations on the database.
- A transaction failure can be caused by various reasons, such as user errors, system errors, concurrency control violations, deadlock detection, or disk failures.
- To recover from transaction failure, the atomicity and durability of transactions must be maintained. That is, either all the operations of a transaction are executed or none, and the effects of committed transactions are not lost due to failures.
- There are three states of database recovery in DBMS:
  - Consistent state: A state where the database satisfies all the integrity constraints and reflects a correct state of the real world.
  - Inconsistent state: A state where the database violates some integrity constraints or does not reflect a correct state of the real world.
  - Intermediate state: A state where the database is in the process of executing a transaction and has not reached a consistent or inconsistent state yet.
- There are two types of database recovery techniques in DBMS:
  - Deferred update: A technique where the changes made by a transaction are not written to the database until the transaction commits. This ensures that no undo operation is required in case of a failure, but a redo operation may be needed to restore the committed changes.
  - Immediate update: A technique where the changes made by a transaction are written to the database as soon as they occur, even before the transaction commits. This requires both undo and redo operations in case of a failure, to restore the database to a consistent state.
- To implement database recovery techniques, the DBMS uses the following components:
  - Log: A sequential file that records all the updates made by transactions on the database, along with the transaction identifiers, timestamps, and commit or abort flags.
  - Buffer: A memory area that temporarily stores the pages of the database that are being accessed or modified by transactions.
  - Checkpoint: A point in time when the DBMS writes all the modified pages from the buffer to the disk and records a checkpoint entry in the log. This reduces the amount of work needed for recovery in case of a failure.
  - Recovery manager: A module that is responsible for performing the recovery operations, such as undo and redo, based on the information in the log and the buffer.



### Log Based Recovery in DBMS

- Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: A unique identifier for each transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data item: The name of the data item affected by the operation.
  - Old value: The value of the data item before the operation.
  - New value: The value of the data item after the operation.
- A log file is maintained in a stable storage device, such as a disk or a tape, that is not affected by the failure  .
- The log file is updated before the actual changes are made to the database, to ensure that the log reflects the latest state of the database  .
- The log file is used to recover the database in two scenarios  :
  - Undo: If a transaction is aborted or fails before committing, then the log file is used to undo the changes made by the transaction and restore the database to its previous state. This is done by applying the inverse operations of the transaction in the reverse order of the log records.
  - Redo: If a transaction is committed but the changes are not reflected in the database due to a failure, then the log file is used to redo the changes made by the transaction and bring the database to its committed state. This is done by applying the same operations of the transaction in the same order of the log records.
- Log based recovery ensures the atomicity and durability properties of transactions, which are essential for maintaining the consistency and integrity of the database.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some checkpoints for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System:

- Define a transaction and its properties (ACID).
- Explain the concept of concurrency control and why it is needed in a database system.
- Describe the locking protocol and the types of locks (shared, exclusive, etc.).
- Discuss the problems of deadlock and starvation and how to prevent or resolve them.
- Explain the concept of serializability and how to test for it using precedence graphs.
- Describe the timestamp ordering protocol and how it ensures serializability and avoids deadlock.
- Explain the concept of validation (optimistic) protocol and how it ensures serializability and avoids locking.
- Discuss the advantages and disadvantages of the different concurrency control protocols.
- Explain the concept of recovery and why it is needed in a database system.
- Describe the log-based recovery technique and the types of log records (start, commit, abort, etc.).
- Discuss the checkpointing mechanism and how it reduces the recovery time.
- Explain the concept of undo and redo operations and how they are applied during recovery.
- Discuss the advantages and disadvantages of the different recovery techniques.



### Deadlock Handling

- A deadlock is an unwanted situation in which two or more transactions are waiting indefinitely for each other to release locks on shared resources.
- Deadlocks can cause performance degradation, resource wastage and system failure in a database management system (DBMS).
- Deadlocks can be handled by three classical approaches: deadlock prevention, deadlock avoidance and deadlock detection and removal .
- Deadlock prevention is a technique that ensures that at least one of the necessary conditions for deadlock occurrence is violated. For example, by using strict two-phase locking protocol, the hold and wait condition can be prevented .
- Deadlock avoidance is a technique that ensures that the system will always remain in a safe state, where there is at least one possible sequence of resource allocation that will not lead to deadlock. For example, by using timestamp ordering protocol, the circular wait condition can be avoided .
- Deadlock detection and removal is a technique that allows the system to enter a deadlock state, but then detects it and recovers from it. For example, by using a wait-for graph or a timeout mechanism, the deadlock can be detected and then resolved by aborting or rolling back some transactions .
- In a distributed database system, deadlock handling is more complex than in a centralized system, because of the issues of transaction location and transaction control.
- Transaction location refers to the problem of identifying the sites where the transactions involved in a deadlock are executing.
- Transaction control refers to the problem of coordinating the actions of the transactions across different sites.
- In a distributed database system, deadlocks can be classified into two types: global deadlocks and local deadlocks .
- A global deadlock is a deadlock that involves transactions executing at different sites .
- A local deadlock is a deadlock that involves transactions executing at the same site .
- Global deadlocks are harder to detect and resolve than local deadlocks, because they require inter-site communication and cooperation .
- There are two main approaches for global deadlock handling: centralized approach and distributed approach .
- In the centralized approach, one site is designated as the deadlock coordinator, which is responsible for collecting the information about the transactions and resources from all the sites, and detecting and resolving the global deadlocks .
- In the distributed approach, each site is responsible for detecting and resolving the local deadlocks, and communicating with other sites to detect and resolve the global deadlocks .
- The centralized approach has the advantages of simplicity and efficiency, but the disadvantages of single point of failure and communication overhead .
- The distributed approach has the advantages of fault tolerance and scalability, but the disadvantages of complexity and coordination overhead .
- There are various algorithms and protocols for implementing the centralized and distributed approaches, such as the edge-chasing algorithm, the probe-based algorithm, the path-pushing algorithm, etc .
- The choice of the deadlock handling technique depends on the characteristics of the system, such as the frequency of deadlocks, the degree of concurrency, the network topology, the communication cost, etc .



### Distributed Database for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A distributed database is a collection of databases that are physically distributed over different locations and connected by a network. 
- A distributed transaction is a database transaction that involves two or more network hosts.  
- A transaction is a logical unit of work that consists of one or more SQL statements executed by a single user. 
- A transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability. 
- A distributed transaction must also satisfy the following properties: 
  - Serializability: The concurrent execution of distributed transactions should produce the same result as if they were executed serially in some order.
  - Global atomicity: Either all the operations in a distributed transaction are committed or none of them are.
  - Local autonomy: Each site in a distributed system should have some control over the transactions that access its local data.
  - Transparency: The user should not be aware of the distribution of data and the execution of distributed transactions.
- To achieve these properties, a distributed database system uses a two-phase commit protocol, which is a coordination mechanism that ensures the atomicity and consistency of distributed transactions.  
- The two-phase commit protocol involves the following roles and phases:  
  - Coordinator: The site that initiates the distributed transaction and coordinates the commit or rollback process.
  - Participants: The sites that execute the operations of the distributed transaction and vote to commit or abort.
  - Prepare phase: The coordinator asks the participants to prepare to commit and vote. The participants execute the transaction, write the undo and redo logs, and lock the data. Then they send their votes to the coordinator.
  - Commit phase: The coordinator collects the votes and decides to commit or abort the transaction. It sends the decision to the participants. The participants follow the decision and release the locks and logs.
- A distributed transaction may become in-doubt if the two-phase commit protocol fails due to network or system failures.  
- An in-doubt transaction is a transaction whose outcome is unknown or uncertain.  
- To resolve in-doubt transactions, a distributed database system uses a recovery mechanism that involves the following steps:  
  - Detection: The coordinator or the participants detect the failure and try to reconnect with each other.
  - Inquiry: The coordinator or the participants inquire about the status of the transaction from each other or from a third party, such as a transaction manager or a log file.
  - Resolution: The coordinator or the participants decide to commit or abort the transaction based on the inquiry results and the predefined rules or policies.



### Distributed Data Storage for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A distributed data store is a system that stores and processes data on multiple machines.
- A distributed transaction is a set of operations on data that is performed across two or more data repositories (especially databases) .
- A distributed database is a collection of data stored at different sites of a computer network.
- The advantages of distributed data storage include:
  - Higher availability and reliability of data
  - Improved performance and scalability of the system
  - Reduced communication and processing costs
  - Increased autonomy and security of local sites
- The challenges of distributed data storage include:
  - Data consistency and concurrency control
  - Distributed query processing and optimization
  - Distributed transaction management and recovery
  - Distributed schema design and data allocation
- The concepts of distributed transaction processing include:
  - Atomicity: A distributed transaction must either commit or abort as a whole
  - Consistency: A distributed transaction must preserve the integrity constraints of the data
  - Isolation: A distributed transaction must not interfere with other concurrent transactions
  - Durability: The effects of a committed distributed transaction must be permanent
- The techniques of distributed transaction processing include:
  - Two-phase commit protocol: A protocol that ensures atomicity of distributed transactions by using a coordinator and participants
  - Distributed locking: A mechanism that ensures isolation of distributed transactions by using locks on data items
  - Distributed timestamp ordering: A mechanism that ensures isolation of distributed transactions by using logical timestamps on data items
  - Distributed deadlock detection: A mechanism that detects and resolves deadlocks among distributed transactions by using wait-for graphs or timeouts
  - Distributed recovery: A mechanism that ensures durability of distributed transactions by using logs and checkpoints



### Concurrency Control

- Concurrency control is the process of managing simultaneous operations on a database without compromising its consistency and integrity.
- Concurrency control is necessary to ensure that concurrent transactions do not interfere with each other and violate the ACID properties of transactions (Atomicity, Consistency, Isolation, and Durability).
- Concurrency control can be achieved by using various techniques, such as locking, timestamping, validation, and multiversioning.
- Locking is a technique that grants exclusive access to a data item to one transaction at a time, preventing other transactions from reading or modifying it until the lock is released.
- Timestamping is a technique that assigns a unique identifier to each transaction based on the time of its initiation, and uses this identifier to order the transactions and resolve conflicts.
- Validation is a technique that checks the consistency of a transaction before committing it, by comparing its read and write sets with those of other concurrent transactions.
- Multiversioning is a technique that maintains multiple versions of a data item, each with a different timestamp, and allows transactions to access the appropriate version based on their timestamp.



### Directory System for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A directory system is a way of organizing and storing the notes of a unit in a hierarchical structure that reflects the topics and subtopics covered in the unit.
- A directory system can help the user to find, access, and manage the notes more easily and efficiently.
- A directory system can also help the user to review and revise the notes before the exams.
- A possible directory system for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System is as follows:

```
Unit 4 - Transaction Processing Concept
├── Introduction to Transaction Processing
│   ├── Definition and Properties of a Transaction
│   ├── Transaction States and System Failures
│   ├── Concurrent Execution of Transactions
│   └── Serializability and Conflict Serializability
├── Concurrency Control Techniques
│   ├── Lock-Based Protocols
│   │   ├── Binary Locking and Two-Phase Locking
│   │   ├── Deadlocks and Deadlock Prevention
│   │   └── Deadlock Detection and Recovery
│   ├── Timestamp-Based Protocols
│   │   ├── Basic Timestamp Ordering
│   │   ├── Thomas' Write Rule
│   │   └── Multiversion Concurrency Control
│   └── Validation-Based Protocols
│       ├── Basic Validation Technique
│       ├── Serial Validation Technique
│       └── Parallel Validation Technique
└── Recovery Techniques
    ├── Log-Based Recovery
    │   ├── Deferred Update and Immediate Update
    │   ├── Undo Logging and Redo Logging
    │   └── Undo/Redo Logging and Checkpoints
    ├── Shadow Paging
    │   ├── Basic Shadow Paging Technique
    │   ├── Advantages and Disadvantages of Shadow Paging
    │   └── Comparison with Log-Based Recovery
    └── Database Backup and Restore
        ├── Types of Database Backup
        ├── Frequency and Scheduling of Database Backup
        └── Database Restore and Recovery Scenarios
```



## Unit 5 - Concurrency Control Techniques

Concurrency control techniques are methods of managing the simultaneous execution of transactions in a shared database. They aim to preserve the database consistency, enforce the isolation of different transactions, and resolve the conflicts that occur due to the read-write operations of transactions .

The need for concurrency control arises because multiple transactions may access and modify the same data items concurrently, which may lead to inconsistency, lost updates, uncommitted dependency, or incorrect summary.

Some of the common concurrency control techniques are:

- **Two-phase locking protocol**: This technique uses locks to secure the permission to read or write a data item. A transaction goes through two phases: a locking phase, where it acquires locks on the data items it needs, and an unlocking phase, where it releases the locks. The locking phase precedes the unlocking phase, and no new locks can be acquired after releasing a lock. This protocol ensures serializability, which means the concurrent execution of transactions is equivalent to some serial execution of the same transactions .

- **Timestamp ordering protocol**: This technique assigns a unique timestamp to each transaction, which reflects its start time. The timestamp is used to order the transactions and determine their precedence. A transaction can read or write a data item only if its timestamp is higher than the timestamp of the last transaction that wrote the data item. Otherwise, the transaction is aborted and restarted with a new timestamp. This protocol avoids the deadlock problem, which occurs when two or more transactions are waiting for each other to release locks.

- **Multi-version concurrency control**: This technique maintains multiple versions of each data item, each with a different timestamp. A transaction can read the version of a data item that was the latest before its start time, and write a new version of a data item with its own timestamp. This protocol allows more concurrency than the timestamp ordering protocol, as transactions can read older versions of data items without conflicting with other transactions that write newer versions.

- **Validation concurrency control**: This technique divides the execution of a transaction into three phases: a read phase, where the transaction reads data items from the database, a validation phase, where the transaction checks for conflicts with other transactions, and a write phase, where the transaction writes the modified data items to the database. A transaction can commit only if it passes the validation phase, which ensures that its read set and write set do not overlap with the write sets of other transactions that committed during its execution. This protocol avoids locking and aborting transactions, but requires buffering the modified data items until the write phase .



### Concurrency Control

- Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other   .
- It ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the respective database .
- Concurrency control is necessary to prevent problems such as lost updates, dirty reads, unrepeatable reads, and phantom reads that may arise due to concurrent access of the same data by multiple transactions  .
- Concurrency control can be implemented using two main techniques: timestamp-based protocols and lock-based protocols  .
- Timestamp-based protocols assign a unique timestamp to each transaction and use it to order the transactions and determine their precedence. They ensure that older transactions are not affected by newer transactions and that conflicting operations are executed in timestamp order  .
- Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item. There are different types of locks, such as binary locks, shared/exclusive locks, and multiple granularity locks, that provide different levels of concurrency and locking overhead  .
- Both timestamp-based and lock-based protocols have advantages and disadvantages. Timestamp-based protocols avoid the need for locking and deadlock detection, but they may cause more transaction aborts and require extra space for storing timestamps. Lock-based protocols allow more concurrency and flexibility, but they incur locking overhead and may cause deadlocks and starvation  .
- There are other concurrency control techniques, such as optimistic concurrency control, multiversion concurrency control, and validation-based concurrency control, that are based on different assumptions and trade-offs .
- Optimistic concurrency control assumes that conflicts are rare and allows transactions to execute without locking, but validates them before committing. If a conflict is detected, the transaction is aborted and restarted .
- Multiversion concurrency control maintains multiple versions of each data item and assigns them different timestamps. It allows transactions to read the most recent committed version of a data item without locking, but requires locking for writing. It ensures serializability and avoids phantom reads.
- Validation-based concurrency control divides the execution of a transaction into three phases: read phase, validation phase, and write phase. It allows transactions to read and write without locking in the read and write phases, but checks for conflicts in the validation phase. If a conflict is detected, the transaction is aborted and restarted.



### Locking Techniques for Concurrency Control

- Concurrency control is the process of managing simultaneous access to shared data in a database system.
- Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the database state remains valid after each transaction.
- Locking is one of the most common concurrency control techniques, which involves using locks to restrict access to data items by different transactions.
- A lock is a mechanism that grants or denies permission to read or write a data item to a transaction.
- A lock manager is a subsystem that manages the allocation and release of locks for transactions.
- There are different types of locks, such as binary locks, shared/exclusive locks, and multiple granularity locks, that provide different levels of concurrency and isolation.
- A locking protocol is a set of rules that governs how transactions acquire and release locks on data items.
- A locking protocol should ensure serializability, which means that the concurrent execution of transactions should produce the same result as some serial execution of the same transactions.
- One of the most widely used locking protocols is the two-phase locking (2PL) protocol, which divides the transaction into two phases: a growing phase and a shrinking phase.
- In the growing phase, a transaction can acquire locks on data items, but cannot release any lock. In the shrinking phase, a transaction can release locks on data items, but cannot acquire any new lock.
- The 2PL protocol ensures serializability, but it may cause deadlocks, which occur when two or more transactions are waiting for each other to release locks on data items.
- To prevent or resolve deadlocks, various techniques can be used, such as deadlock prevention, deadlock detection, deadlock avoidance, and deadlock recovery.
- Another locking protocol is the timestamp ordering (TO) protocol, which assigns a unique timestamp to each transaction, and uses the timestamps to order the access to data items by different transactions.
- The TO protocol ensures serializability and avoids deadlocks, but it may cause aborts, which occur when a transaction is rolled back and restarted due to a conflict with another transaction.
- To reduce the number of aborts, various techniques can be used, such as multi-version concurrency control (MVCC), validation concurrency control (VCC), and optimistic concurrency control (OCC).
- MVCC maintains multiple versions of each data item, and allows transactions to read the most recent committed version of a data item, without locking it.
- VCC validates each transaction before committing it, by checking if it conflicts with any other transaction that has committed in the meantime.
- OCC assumes that conflicts are rare, and allows transactions to execute without locking any data item, but validates them at the end of the execution.



### Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of concurrency control methods that do not use locks to ensure serializability of transactions   .
- Time stamping protocols assign a unique timestamp to each transaction when it is created, which reflects its logical or physical start time   .
- Time stamping protocols use the timestamps to order the transactions and resolve any conflicts that may arise due to concurrent execution   .
- Time stamping protocols ensure that any conflicting read and write operations are executed in timestamp order, which is equivalent to the serial order of the transactions   .
- Time stamping protocols can be classified into two types: optimistic and pessimistic.
  - Optimistic time stamping protocols assume that conflicts are rare and allow transactions to execute without checking for conflicts until they commit.
  - Pessimistic time stamping protocols check for conflicts before every read and write operation and abort or delay transactions that violate the timestamp order.
- Time stamping protocols have some advantages and disadvantages over lock-based protocols :
  - Advantages:
    - Time stamping protocols avoid deadlock, as transactions do not acquire any locks that need to be released later .
    - Time stamping protocols are more efficient in terms of memory and communication overhead, as transactions do not need to store or exchange any lock information .
    - Time stamping protocols are more suitable for distributed and parallel systems, as transactions can be ordered globally and consistently based on their timestamps .
  - Disadvantages:
    - Time stamping protocols may cause more aborts and restarts of transactions, as conflicts are detected only at commit time or during execution .
    - Time stamping protocols may suffer from the problem of starvation, as older transactions may be repeatedly aborted by newer transactions with higher timestamps .
    - Time stamping protocols may not reflect the actual order of events in the real world, as timestamps are assigned based on the system clock or a logical counter, which may not be synchronized or accurate .



### Validation Based Protocol

- Validation Based Protocol is a concurrency control technique that works on the assumption that interference among transactions is rare and can be detected during validation  .
- It is also called Optimistic Concurrency Control Technique because it does not use locking or timestamping to prevent conflicts, but rather checks for them at the end of the transaction  .
- Validation Based Protocol consists of three phases for each transaction: read phase, validation phase, and write phase   .
- In the read phase, the transaction reads data from the database and makes local copies for updates, but does not write anything to the database   .
- In the validation phase, the transaction checks whether it has any conflicts with other transactions that have already committed or are in the validation phase   .
- A conflict occurs when two transactions access the same data item and at least one of them updates it   .
- The validation phase uses some rules or criteria to decide whether a transaction can commit or has to abort   .
- Some common validation rules are based on timestamps, such as start time, end time, or validation time of each transaction   .
- In the write phase, if the transaction passes the validation, it writes its updates to the database, otherwise it aborts and restarts   .
- Validation Based Protocol has the advantage of avoiding locking overhead and deadlock, but it may incur more aborts and restarts due to conflicts   .



### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows a multi-granularity compatibility function that defines the compatibility of different lock modes on different levels of granularity .
- Multiple granularity locking protocol also follows a set of rules to ensure serializability and avoid deadlock:
  - Lock the root of the tree first, any mode
  - Node Q can be locked by T iin S or IS only if parent(Q) locked by T iin IX or IS
  - Node Q can be locked by T iin X, SIX, IX only if parent(Q) locked by T iin IX, SIX
  - T iis two-phase
  - T ican unlock node Q only if none of Q’s descendants are locked by T i
- Multiple granularity locking protocol can be represented graphically as a tree, where each node represents a data item of a certain granularity and each edge represents the nesting relationship between data items. For example, consider the following tree, which consists of four levels of nodes:

```
          Database
            /  \
           /    \
          /      \
         /        \
        /          \
       /            \
      /              \
     /                \
    /                  \
   /                    \
  /                      \
 /                        \
A                          B
/ \                        / \
/   \                      /   \
/     \                    /     \
/       \                  /       \
/         \                /         \
/           \              /           \
/             \            /             \
/               \          /               \
/                 \        /                 \
/                   \      /                   \
/                     \    /                     \
A1                      A2 B1                      B2
/ \                    / \ / \                    / \
/   \                  /   /   \                  /   \
/     \                /   /     \                /     \
/       \              /   /       \              /       \
/         \            /   /         \            /         \
/           \          /   /           \          /           \
/             \        /   /             \        /             \
/               \      /   /               \      /               \
/                 \    /   /                 \    /                 \
/                   \  /   /                   \  /                   \
/                     \/   /                     \/                     \
A11                      A12 B11                      B12 B21                      B22
```



### Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data objects to exist in the database at the same time.
- The main idea of multi version schemes is to grant an appropriate version of a data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data objects they modify.
- The benefits of multi version schemes are increased concurrency, reduced locking overhead, and improved performance.
- The challenges of multi version schemes are maintaining consistency, avoiding conflicts, and managing storage space for multiple versions.

#### How Multi Version Schemes Work

- While different database management systems may implement multi version schemes in their own ways, a general algorithm for multi version schemes is as follows:

  1. Every data object has a version number that indicates its freshness and validity.
  2. When a transaction wants to read a data object, it is granted the version with the highest version number that is lower than or equal to the transaction's start time. This ensures that the transaction reads a consistent snapshot of the database.
  3. When a transaction wants to write a data object, it creates a copy of the data object with a new version number that is higher than the transaction's start time. The original data object is not modified.
  4. Other transactions can continue to read the older version of the data object while the copy is being updated.
  5. After the write operation is successful, the version number of the copy is incremented and the copy becomes the current version of the data object.
  6. Subsequent read requests use the updated version of the data object.

#### Example of Multi Version Schemes

- Suppose we have a data object X with a version number 1 and a value 10. We also have two transactions T1 and T2 that start at time 1 and 2 respectively. The following table shows the operations performed by the transactions and the versions of X they access.

| Transaction | Operation | Version of X | Value of X |
| ----------- | --------- | ------------ | ---------- |
| T1          | Read X    | 1            | 10         |
| T2          | Write X   | 2            | 20         |
| T1          | Write X   | 3            | 30         |
| T2          | Read X    | 2            | 20         |
| T1          | Commit    | 3            | 30         |
| T2          | Commit    | 2            | 20         |

- As we can see, T1 and T2 read and write different versions of X, and do not interfere with each other. T1 reads the initial version of X, while T2 reads the version created by its own write operation. T1 writes a new version of X, which becomes the current version after T1 commits. T2 writes another version of X, which is discarded after T2 commits, since it is older than the current version.



### Recovery with Concurrent Transaction

- Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions executing simultaneously.
- Recovery with concurrent transaction is necessary to ensure the ACID properties of transactions, especially atomicity and durability.
- Recovery with concurrent transaction can be done in the following four ways:
  - Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if locking is used, then the recovery scheme can use the lock table to identify the transactions that were active at the time of failure and undo their effects. If timestamp ordering is used, then the recovery scheme can use the timestamps to order the transactions and redo their effects.
  - Transaction rollback: In this scheme, the recovery scheme can undo the effects of a transaction that has failed or aborted by using the log records. The log records contain the information about the operations performed by the transaction, such as the old and new values of the data items. The recovery scheme can use the log records to restore the old values of the data items and make the transaction appear as if it never executed.
  - Checkpoints: In this scheme, the recovery scheme can reduce the amount of work needed to recover from a failure by periodically taking a snapshot of the database and the log records. A checkpoint is a point in time when the database and the log records are synchronized and consistent. The recovery scheme can use the checkpoint to start the recovery process from the most recent checkpoint instead of from the beginning of the log.
  - Restart recovery: In this scheme, the recovery scheme can handle the failure of the recovery process itself by using a special log record called restart record. A restart record is a log record that marks the point where the recovery process has reached before it failed. The recovery scheme can use the restart record to resume the recovery process from the point where it left off instead of from the beginning of the log or the checkpoint.



### Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Oracle is a relational database management system that supports concurrent access of data by multiple users and transactions.
- Oracle uses a multiversion concurrency control (MVCC) model to provide read consistency and avoid locking conflicts.
- Oracle also uses various types of locks to ensure data integrity and consistency among transactions.
- Some of the concurrency control techniques used by Oracle are:

  - Statement-level read consistency: Oracle ensures that each query sees a consistent view of the data as of the time the query started, regardless of any changes made by other transactions. This is achieved by using undo segments to reconstruct the previous versions of the data blocks that have been modified by other transactions  .
  - Transaction-level read consistency: Oracle can also provide a consistent view of the data for all the queries in a transaction as of the time the transaction started. This is achieved by using a snapshot isolation level, which assigns a system change number (SCN) to each transaction and uses it to determine the visibility of the data. This isolation level prevents dirty reads, non-repeatable reads, and phantom reads .
  - Oracle isolation levels: Oracle supports four isolation levels for transactions: read committed, serializable, read only, and read write. The default isolation level is read committed, which means that a transaction can only see the changes made by other transactions that have committed. The serializable isolation level ensures that a transaction can only see the data as of the time the transaction started, and prevents any concurrent changes by other transactions. The read only isolation level is similar to serializable, but does not allow any changes by the transaction itself. The read write isolation level allows a transaction to see and modify the data as of the time the transaction started, and prevents any concurrent changes by other transactions .
  - Oracle locks: Oracle uses various types of locks to protect the data from concurrent modifications by other transactions. Some of the locks used by Oracle are:

    - Row locks: Oracle automatically acquires a row lock when a transaction modifies a row. The row lock prevents other transactions from modifying or deleting the same row until the transaction commits or rolls back. Row locks are released when the transaction ends.
    - Table locks: Oracle automatically acquires a table lock when a transaction modifies a table. The table lock prevents other transactions from altering the structure of the table or dropping the table until the transaction commits or rolls back. Table locks can be shared or exclusive, depending on the type of modification. Shared table locks allow other transactions to query or modify the table, but not to alter its structure. Exclusive table locks prevent any other transactions from accessing the table.
    - DML locks: Oracle automatically acquires a DML lock when a transaction performs a data manipulation language (DML) operation, such as insert, update, delete, or merge. The DML lock prevents other transactions from performing conflicting DML operations on the same data until the transaction commits or rolls back. DML locks can be row-level or table-level, depending on the scope of the operation.
    - DDL locks: Oracle automatically acquires a DDL lock when a transaction performs a data definition language (DDL) operation, such as create, alter, drop, truncate, or rename. The DDL lock prevents other transactions from performing any DDL or DML operations on the same object until the transaction commits or rolls back. DDL locks are always exclusive and object-level.
    - Latches and mutexes: Oracle uses latches and mutexes to protect the internal structures of the database, such as the buffer cache, the shared pool, the redo log buffer, and the data dictionary. Latches and mutexes are low-level synchronization mechanisms that are acquired and released very quickly by the database processes. Latches and mutexes are not visible to the users or transactions.

