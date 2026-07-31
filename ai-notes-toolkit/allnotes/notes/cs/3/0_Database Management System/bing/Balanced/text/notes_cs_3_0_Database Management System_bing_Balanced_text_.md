

## Unit 1 - Introduction

- In this unit, you will learn about the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI is a broad and interdisciplinary field that draws from computer science, mathematics, logic, psychology, philosophy, linguistics, and other disciplines.
- AI can be classified into different types, such as:
  - Weak AI or narrow AI: AI systems that are designed to perform a specific task or domain, such as face recognition, chess playing, or speech recognition.
  - Strong AI or general AI: AI systems that can perform any intellectual task that a human can, such as understanding natural language, solving complex problems, or exhibiting common sense.
  - Artificial superintelligence: AI systems that can surpass human intelligence and capabilities in all domains, such as creativity, social skills, or moral reasoning.
- AI can also be classified into different approaches, such as:
  - Symbolic AI or classical AI: AI systems that use symbols and rules to represent and manipulate knowledge, such as logic, search, planning, and expert systems.
  - Subsymbolic AI or connectionist AI: AI systems that use numerical values and networks to model and learn from data, such as neural networks, deep learning, and reinforcement learning.
  - Hybrid AI: AI systems that combine symbolic and subsymbolic methods to leverage the strengths of both approaches, such as neural-symbolic integration, neuroevolution, and neuro-fuzzy systems.
- AI has many applications and benefits for various domains and industries, such as:
  - Healthcare: AI can help diagnose diseases, recommend treatments, monitor patients, and discover new drugs.
  - Education: AI can help personalize learning, assess students, provide feedback, and tutor students.
  - Business: AI can help optimize operations, analyze data, automate tasks, and enhance customer service.
  - Entertainment: AI can help create content, generate music, design games, and produce movies.
  - Security: AI can help detect threats, prevent fraud, protect data, and enforce laws.
  - Environment: AI can help monitor climate change, conserve resources, reduce pollution, and protect wildlife.
- AI also poses many challenges and risks for society and humanity, such as:
  - Ethical: AI can raise moral dilemmas, such as privacy, fairness, accountability, transparency, and human dignity.
  - Social: AI can affect human relationships, such as employment, education, culture, and communication.
  - Legal: AI can create legal issues, such as liability, regulation, ownership, and rights.
  - Safety: AI can cause harm, such as accidents, errors, malfunctions, and attacks.
  - Existential: AI can threaten human existence, such as superintelligence, singularity, and alignment.



### Overview for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A database is a collection of related data that can be stored, manipulated, and retrieved by a computer system.
- A database management system (DBMS) is a software system that provides the functionality to create, maintain, and access databases.
- A DBMS consists of three main components: data, data dictionary, and database engine.
- Data is the actual information stored in the database, such as names, addresses, phone numbers, etc.
- Data dictionary is a set of metadata that describes the structure, format, and constraints of the data in the database.
- Database engine is the core component that performs the operations on the data, such as insertion, deletion, modification, retrieval, etc.
- A DBMS can support different types of data models, such as relational, hierarchical, network, object-oriented, etc.
- A data model is a logical representation of the data and the relationships among them.
- A relational data model is based on the concept of tables, where each table consists of rows (records) and columns (attributes).
- A hierarchical data model is based on the concept of parent-child relationships, where each record can have one parent and multiple children.
- A network data model is based on the concept of links, where each record can have multiple parents and multiple children.
- An object-oriented data model is based on the concept of objects, where each object consists of data and methods (functions) that operate on the data.
- A DBMS can support different types of languages, such as data definition language (DDL), data manipulation language (DML), data query language (DQL), etc.
- A DDL is used to define the structure and constraints of the data in the database, such as creating, altering, or dropping tables, indexes, views, etc.
- A DML is used to manipulate the data in the database, such as inserting, deleting, updating, or merging records, etc.
- A DQL is used to query the data in the database, such as selecting, sorting, filtering, or joining records, etc.
- A DBMS can support different types of users, such as database administrators (DBAs), database designers, application developers, end users, etc.
- A DBA is responsible for the overall management and maintenance of the database system, such as creating, backing up, restoring, securing, tuning, or monitoring the database, etc.
- A database designer is responsible for the logical design and modeling of the database, such as identifying the data requirements, entities, attributes, relationships, and constraints, etc.
- An application developer is responsible for the development and implementation of the applications that interact with the database, such as writing the code, testing, debugging, or deploying the applications, etc.
- An end user is the person who uses the applications to access the data in the database, such as entering, viewing, or analyzing the data, etc.



### Database System vs File System

- A file system is a software that organizes and manages files on a storage media, such as a hard disk or a flash drive. A file system stores data in a hierarchical structure of directories and files, and provides basic operations such as creating, deleting, renaming, copying, and moving files. A file system does not have any built-in mechanism for ensuring data consistency, security, integrity, or recovery in case of failures. A file system is suitable for storing unstructured or semi-structured data, such as documents, images, audio, video, etc.    

- A database management system (DBMS) is a software that allows you to access, create, and administer databases. A database is a collection of structured data that is organized in tables, records, and fields, and follows a predefined schema. A DBMS provides advanced operations such as querying, updating, indexing, and joining data, as well as enforcing data constraints, rules, and relationships. A DBMS also has mechanisms for ensuring data consistency, security, integrity, and recovery in case of failures. A DBMS is suitable for storing structured or relational data, such as customer information, inventory, transactions, etc.     

- A DBMS is generally better than a file system for most applications, as it offers the following advantages:

  - Data independence: A DBMS separates the logical and physical views of data, which means that the application does not need to know how the data is stored or accessed. A file system, on the other hand, requires the application to handle the details of data storage and retrieval, such as file names, paths, formats, etc.   

  - Data consistency and integrity: A DBMS ensures that the data is consistent and valid across the database, by enforcing data constraints, rules, and relationships. A file system does not have any such mechanism, and relies on the application to ensure data consistency and integrity. This can lead to data anomalies, errors, and inconsistencies, especially when multiple applications access the same data.     

  - Data security and authorization: A DBMS provides mechanisms for controlling who can access, modify, or delete data, by implementing user authentication, authorization, and encryption. A file system does not have any such mechanism, and relies on the operating system or the application to provide data security and authorization. This can lead to data breaches, unauthorized access, or data loss, especially when the data is shared or distributed.     

  - Data recovery and backup: A DBMS provides mechanisms for recovering and restoring data in case of failures, such as power outages, hardware malfunctions, or human errors. A DBMS also allows for periodic backup of data, to prevent data loss or corruption. A file system does not have any such mechanism, and relies on the user or the application to perform data recovery and backup. This can lead to data loss, corruption, or inconsistency, especially when the data is critical or large.     

  - Data manipulation and analysis: A DBMS provides a powerful and standardized language for manipulating and analyzing data, such as SQL (Structured Query Language). A DBMS also allows for complex operations, such as indexing, joining, sorting, filtering, aggregating, and grouping data, as well as performing calculations, functions, and procedures on data. A file system does not have any such language or operation, and relies on the application to perform data manipulation and analysis. This can lead to inefficient, redundant, or inaccurate data processing, especially when the data is large or complex.     

  - Data concurrency and performance: A DBMS manages concurrent access to data efficiently, by implementing locking, isolation, and transaction mechanisms. A DBMS also optimizes data access and storage, by using caching, buffering, indexing, and partitioning techniques. A file system does not have any such mechanism or technique, and relies on the application to manage concurrent access and performance. This can lead to data



### Database System Concept and Architecture

- A database system is a collection of software components that manage the storage, retrieval, and manipulation of data in a database.
- A database system consists of three main components: the data, the database management system (DBMS), and the database applications.
- The data is the collection of facts and information that is stored in the database. The data can be structured or unstructured, and can have different levels of abstraction, such as conceptual, logical, and physical.
- The database management system (DBMS) is the software that provides the functionality for creating, maintaining, and accessing the database. The DBMS handles the tasks of data definition, data manipulation, data control, and data administration.
- The database applications are the programs that interact with the database to perform various operations, such as querying, updating, analyzing, and reporting. The database applications can be classified into two types: online and batch.
- The architecture of a database system is the way the components are organized and communicate with each other. The architecture can be influenced by the primary computer system on which the database system runs, such as centralized, decentralized, or parallel.
- The architecture of a database system can also be seen as either single-tier or multi-tier. A single-tier architecture is where the DBMS and the database applications run on the same machine. A multi-tier architecture is where the DBMS and the database applications are distributed across different machines, and communicate through a network.
- A common multi-tier architecture is the client/server architecture, where one or more client machines request services from one or more server machines. The server machines can be further divided into database servers, application servers, and web servers, depending on the type of service they provide.
- A database system also has a data model, which is a collection of concepts that describe the structure and behavior of the data in the database. The data model includes the data types, the relationships, the constraints, and the operations that can be performed on the data.
- A database system also has a schema, which is a description of the data in a specific data model. The schema can have different levels of abstraction, such as external, conceptual, and internal. The external schema defines the view of the data for a specific database application. The conceptual schema defines the overall logical structure of the data for the entire database. The internal schema defines the physical storage and representation of the data in the database.



### Data Model Schema and Instances

- A data model is a collection of concepts and rules for describing the structure, meaning, and constraints of the data stored in a database.
- A schema is the formal description of the structure and organization of the data in a database. It defines the tables, columns, keys, relationships, and constraints of the data.
- An instance is the set of data stored in a database at a particular moment of time. It represents the current state and values of the data.
- A schema is static and does not change frequently, while an instance is dynamic and changes constantly as the data is inserted, updated, or deleted.
- A schema can be represented by different levels of abstraction, such as logical schema, physical schema, and view schema.
  - Logical schema: It describes the database design at the logical level, using entities, attributes, and relationships. It is independent of the physical implementation and storage details of the data.
  - Physical schema: It describes the database design at the physical level, using files, records, fields, and indexes. It specifies how the data is stored, accessed, and manipulated by the database system.
  - View schema: It describes the database design at the user level, using views, queries, and reports. It defines how the data is presented and accessed by different users and applications.
- A schema can be represented by different notations, such as entity-relationship diagrams, relational algebra, or SQL statements.
- An instance can be represented by different formats, such as tables, records, tuples, or XML documents.



### Data Independence and Database Language and Interfaces

- Data independence is a property of DBMS that allows the database schema to be changed at one level without affecting the schema at the next higher level.
- Database schema is the logical structure and organization of the data in the database.
- There are two types of data independence: logical data independence and physical data independence .
- Logical data independence means that the conceptual schema can be changed without affecting the external schema or the application programs .
- Conceptual schema is the level of abstraction that describes the logical structure and relationships of the data in the database.
- External schema is the level of abstraction that defines the views of different users or applications on the data in the database.
- Physical data independence means that the internal schema can be changed without affecting the conceptual schema or the external schema .
- Internal schema is the level of abstraction that describes the physical storage and access methods of the data in the database.
- Data independence provides several benefits, such as:
  - It allows the data to be separated from the programs that use it, which enhances the security, integrity, and portability of the data.
  - It allows the database to evolve and adapt to changing requirements and technologies without affecting the existing applications.
  - It reduces the maintenance and development costs of the database and the applications.
- Database language is a set of commands and syntax used to define, manipulate, and query the data in the database.
- There are three types of database languages: data definition language (DDL), data manipulation language (DML), and data query language (DQL).
- Data definition language (DDL) is used to specify the structure and organization of the data in the database, such as creating, altering, or dropping tables, indexes, views, etc..
- Data manipulation language (DML) is used to insert, update, delete, and retrieve the data in the database, such as inserting a new record, updating an existing record, deleting a record, etc..
- Data query language (DQL) is used to query the data in the database, such as selecting, filtering, sorting, grouping, aggregating, etc..
- Database interface is a software component that allows the users or applications to interact with the database using the database language.
- There are different types of database interfaces for different categories of users, such as:
  - Graphical user interface (GUI) is a user-friendly interface that provides graphical elements, such as menus, buttons, icons, etc., to perform database operations.
  - Command-line interface (CLI) is a text-based interface that requires the user to type commands and parameters to perform database operations.
  - Application programming interface (API) is a set of functions and protocols that allows the application programs to access and manipulate the database using the database language.
  - Web interface is a web-based interface that allows the user to access and manipulate the database using a web browser and a web server.



### Data Definition Language

- Data Definition Language (DDL) is a computer language used to create and modify the structure of database objects such as tables, views, indexes, schemas, etc.   
- DDL statements are similar to a computer programming language for defining data structures, especially database schemas. 
- DDL is used to specify the logical and physical characteristics of the data, such as data types, constraints, relationships, etc.  
- DDL is also used to grant or revoke access rights and privileges to database objects.  
- Some common DDL commands are CREATE, ALTER, DROP, RENAME, TRUNCATE, COMMENT, etc.  
- DDL is a part of the Structured Query Language (SQL), which is a standard language for interacting with relational databases.   
- DDL is executed by the database management system (DBMS), which interprets and validates the DDL statements and updates the data dictionary accordingly.  
- The data dictionary is a repository of metadata that describes the structure and properties of the database objects.  
- DDL is different from Data Manipulation Language (DML), which is used to insert, update, delete, and query data in a database.  
- DDL is also different from Data Control Language (DCL), which is used to control the transactions and concurrency in a database.



### DML for the notes of the Unit 1 - Introduction in the subject of Database Management System

- DML stands for Data Manipulation Language  .
- It is a subset of SQL statements that are used to manipulate the data in the database   .
- It includes the following commands: SELECT, INSERT, UPDATE, DELETE, MERGE, etc  .
- The purpose of DML is to store, modify, retrieve, delete and update data in the database .
- DML commands are not auto-committed, which means they need to be explicitly committed or rolled back to make the changes permanent or undo them .
- DML commands can be used with clauses such as WHERE, GROUP BY, HAVING, ORDER BY, etc to filter, aggregate, sort and limit the data .
- DML commands can also be used with subqueries, joins, views, functions, etc to perform complex operations on the data .
- DML commands can be executed interactively or embedded in a program.
- DML commands can be categorized into two types: procedural and non-procedural.
  - Procedural DML requires the user to specify what data is needed and how to get it.
  - Non-procedural DML requires the user to specify only what data is needed, and the system determines how to get it.
  - SQL is an example of a non-procedural DML.
- DML is different from DDL (Data Definition Language), which is used to define the structure and schema of the database .
- DML is also different from DCL (Data Control Language), which is used to control the access and privileges of the database .



### Overall Database Structure

- A database is a collection of information that is related to a particular subject or purpose, such as tracking customer orders or maintaining a music collection.
- A database can be considered a structure in realization of the database language. The states of a created conceptual schema are transformed into an explicit mapping, the database schema. This describes how real-world entities are modeled in the database.
- A database schema consists of a set of tables, each with a name, columns, data types, constraints, and relationships with other tables.
- A database management system (DBMS) is a software that extracts information from the database in response to queries. A DBMS also provides functions for defining, storing, manipulating, and protecting the data in the database.
- The database system is divided into three components: query processor, storage manager, and disk storage.
  - The query processor is responsible for interpreting and executing the queries issued by the users or applications. It also performs query optimization, which is the process of finding the most efficient way to execute a query.
  - The storage manager is responsible for managing the allocation and deallocation of disk space, as well as the movement of data between disk and main memory. It also provides mechanisms for concurrency control, recovery, and security.
  - The disk storage is the physical device where the data is stored. It consists of files, pages, and records. A file is a collection of pages, a page is a fixed-size unit of disk space, and a record is a logical unit of data that corresponds to a row in a table.



### Data Modeling Using the Entity Relationship Model

- Data modeling is the process of designing and documenting the structure, relationships, and constraints of data in a database system.
- Data modeling can be done at different levels of abstraction, such as conceptual, logical, and physical.
- A conceptual data model is a high-level representation of the data requirements of an organization or a system, independent of any specific database technology or implementation details.
- A logical data model is a more detailed and normalized representation of the data, which specifies the data types, domains, constraints, and relationships of the data elements.
- A physical data model is a representation of how the data will be stored, accessed, and manipulated in a specific database system or platform.
- The entity relationship (ER) model is a widely used conceptual data modeling technique, which uses graphical symbols to represent the entities, attributes, and relationships of a data domain.
- An entity is a real-world object or concept that can be identified and distinguished from other entities. Examples of entities are students, courses, books, etc.
- An attribute is a property or characteristic of an entity that describes some aspect of the entity. Examples of attributes are name, age, address, etc.
- A relationship is an association or connection between two or more entities that expresses some meaningful or relevant information about the entities. Examples of relationships are enrolls, teaches, borrows, etc.
- The ER model can be represented using two types of diagrams: the entity relationship diagram (ERD) and the enhanced entity relationship diagram (EERD).
- The ERD uses the following symbols to represent the components of the ER model:

  - A rectangle for an entity
  - An oval for an attribute
  - A diamond for a relationship
  - A line for a link between an entity and a relationship or between an entity and an attribute
  - A double line for a total participation constraint, which means that every entity in an entity set must participate in a relationship
  - A single line for a partial participation constraint, which means that some entities in an entity set may not participate in a relationship
  - A double oval for a multivalued attribute, which means that an entity can have more than one value for that attribute
  - A dashed oval for a derived attribute, which means that the value of that attribute can be computed from other attributes or relationships
  - A double rectangle for a weak entity, which means that the entity does not have a key attribute of its own and depends on another entity for its identification
  - A double diamond for an identifying relationship, which means that the relationship provides the key attribute for the weak entity

- The EERD extends the ERD with additional symbols and concepts to represent more complex and realistic data scenarios, such as:

  - Subclasses and superclasses, which represent the specialization and generalization of entities based on some distinguishing criteria
  - Inheritance, which means that a subclass inherits all the attributes and relationships of its superclass
  - Disjointness and overlap constraints, which specify whether the subclasses of a superclass are mutually exclusive or can have common entities
  - Total and partial constraints, which specify whether every entity in a superclass must belong to a subclass or not
  - Aggregation, which means that a relationship between two or more entities can be treated as a single entity for the purpose of another relationship
  - Composition, which means that an entity is composed of other entities and has a strong ownership and existence dependency on them
  - Categories, which represent the union of two or more entity sets that share some common attributes or relationships



### ER Model Concepts

- ER model stands for **Entity Relationship model**, which is a high-level conceptual data model diagram  .
- ER model helps to **systematically analyze data requirements** to produce a well-designed database.
- ER model represents **real-world entities** and the **relationships** between them .
- An entity is a **thing of interest** in a specific domain of knowledge, such as a student, a course, a product, etc  .
- An entity type is a **classification** of entities that share common properties or attributes, such as name, age, address, etc  .
- An entity set is a **collection** of entities of the same type, such as all students, all courses, all products, etc .
- A relationship is an **association** between two or more entities, such as a student enrolls in a course, a customer buys a product, etc  .
- A relationship type is a **category** of relationships that have the same characteristics or constraints, such as one-to-one, one-to-many, many-to-many, etc  .
- A relationship set is a **set** of relationships of the same type, such as all enrollments, all purchases, all friendships, etc .
- In ER diagram, the entity types are represented by **rectangles**, the attributes are represented by **ellipses**, the relationships are represented by **diamonds**, and the cardinalities are represented by **numbers** or **symbols**   .
- An example of an ER diagram is shown below:

ER diagram example

: https://www.guru99.com/er-diagram-tutorial-dbms.html
: https://www.tutorialspoint.com/dbms/er_model_basic_concepts.htm
: https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model
: https://www.geeksforgeeks.org/introduction-of-er-model/
: https://www.javatpoint.com/dbms-er-model-concept



### Notation for ER Diagram

- ER diagram stands for Entity Relationship diagram, which is a graphical representation of the logical structure of a database.
- ER diagram shows the entities, attributes and relationships of a database schema.
- There are different notations and symbols used to draw ER diagrams, depending on the level of abstraction and the modeling methodology .
- Some of the common notations and symbols are:

  - **Arrow notation**: This notation uses arrows to indicate the cardinality and participation of entities in a relationship. For example, a single-headed arrow with an open circle means zero or one, a single-headed arrow with a solid circle means one and only one, a double-headed arrow means one or many, and a line without an arrow means many.
  - **Barker's notation**: This notation uses boxes to represent entities and attributes, and diamonds to represent relationships. The cardinality and participation of entities are shown by placing a letter inside the diamond, such as N for many, 1 for one, M for mandatory, and O for optional.
  - **Chen's notation**: This notation uses rectangles to represent entities, ovals to represent attributes, and diamonds to represent relationships. The cardinality and participation of entities are shown by placing numbers or symbols on the lines connecting the entities and the relationships, such as 1, N, M, or O.
  - **Crow's foot notation**: This notation uses rectangles to represent entities, ovals to represent attributes, and lines to represent relationships. The cardinality and participation of entities are shown by placing symbols on the ends of the lines, such as a crow's foot for many, a dash for one, a circle for zero, and a double line for mandatory.
  - **UML notation**: This notation uses rectangles to represent entities, ovals to represent attributes, and lines to represent relationships. The cardinality and participation of entities are shown by placing numbers or symbols on the ends of the lines, such as 0..1, 1, 1..*, or *.
  - **Min-Max notation**: This notation uses rectangles to represent entities, ovals to represent attributes, and lines to represent relationships. The cardinality and participation of entities are shown by placing numbers in parentheses on the ends of the lines, such as (0,1), (1,1), (1,N), or (0,N).

- Here are some examples of ER diagrams using different notations:

  - Arrow notation:

    ```
    +----------+        +----------+
    | Employee |        |  Project |
    +----------+        +----------+
    | emp_id   |        | proj_id  |
    | name     |        | name     |
    | salary   |        | budget   |
    +----------+        +----------+
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |<-----------------|<--+
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
         |                  |   |
    +----------+        +----------+
    |  Works   |        |  Manages |
    +----------+        +----------+
    ```

    This diagram shows that an employee can work on many projects, but a project can have only one manager. The open circle on the employee side of the works relationship means that an employee can work on zero or one projects, while the double-headed arrow on the project side means that a project can have one or many employees working on it. The solid circle on the employee side of the manages relationship means that an employee must manage one and only one project, while the single-headed arrow on the project side means that a project can have zero or one managers.

  - Barker's notation:

    ```
    +----------+        +----------+
    | Employee |

```




### Mapping Constraints

- Mapping constraints are rules that define how the entities and relationships in an ER diagram can be mapped to the tables and columns in a relational schema.
- Mapping constraints can be classified into three types: cardinality ratio, participation constraint, and key constraint.
- Cardinality ratio specifies the maximum number of relationship instances that an entity can participate in. It can be one-to-one, one-to-many, many-to-one, or many-to-many.
- Participation constraint specifies whether the participation of an entity in a relationship is mandatory or optional. It can be total or partial.
- Key constraint specifies that an entity set must have a primary key that uniquely identifies each entity. It can also specify that a relationship set must have a primary key that uniquely identifies each relationship.

- Some examples of mapping constraints are:

  - A student can enroll in at most one department. This is a one-to-many cardinality ratio from department to student.
  - A department must have at least one student enrolled. This is a total participation constraint from department to student.
  - A student must have a unique student ID. This is a key constraint for the student entity set.
  - A student can register for multiple courses, and a course can have multiple students registered. This is a many-to-many cardinality ratio from student to course.
  - A course must have a unique course ID. This is a key constraint for the course entity set.
  - A student and a course can have at most one grade for each other. This is a key constraint for the grade relationship set.



### Keys for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A **database** is a collection of related data that is organized and stored in a structured way.
- A **database management system (DBMS)** is a software system that allows users to create, manipulate, and access databases.
- A **data model** is a conceptual representation of the data and the relationships among them in a database.
- A **relational data model** is a data model that represents data as tables of rows and columns, where each row is a record and each column is an attribute.
- A **primary key** is a column or a set of columns that uniquely identifies each record in a table.
- A **foreign key** is a column or a set of columns that references the primary key of another table, establishing a relationship between the two tables.
- A **schema** is a description of the structure and constraints of a database, including the names and types of the tables, columns, and keys.
- A **query** is a request for information from a database, usually expressed in a structured query language (SQL).
- A **transaction** is a logical unit of work that consists of one or more operations on a database, such as inserting, updating, deleting, or querying data.
- A **concurrency control** mechanism is a technique that ensures the consistency and isolation of transactions when multiple users access the database simultaneously.
- A **recovery** mechanism is a technique that restores the database to a consistent state after a failure, such as a system crash or a power outage.



### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple.
- A candidate key can be derived from a super key by removing the redundant attributes.
- A primary key is a special candidate key that is chosen by the database designer to identify the tuples in a relation.
- A primary key should be non-null and unique for each tuple in a relation.
- A relation can have more than one super key, but only one primary key.
- A super key can be used to enforce referential integrity constraints, which ensure that the values of a foreign key in one relation match the values of a primary key in another relation.
- A super key can also be used to define functional dependencies, which specify the attributes that are determined by another attribute or a set of attributes in a relation.
- A super key can help to reduce data redundancy and inconsistency by eliminating partial and transitive dependencies in a relation.



### Candidate Key

- A candidate key is a minimal set of attributes that can uniquely identify each tuple in a relation.
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key.
- A candidate key must satisfy two properties: uniqueness and minimality.
- Uniqueness means that no two tuples in the relation can have the same values for the attributes of the candidate key.
- Minimality means that no proper subset of the candidate key can also uniquely identify each tuple in the relation.
- For example, consider the following relation STUDENT with attributes RollNo, Name, and Email.

| RollNo | Name | Email |
| ------ | ---- | ----- |
| 101 | Alice | alice@example.com |
| 102 | Bob | bob@example.com |
| 103 | Charlie | charlie@example.com |

- In this relation, RollNo, Name, and Email are all candidate keys, as they can uniquely identify each tuple.
- However, only one of them can be chosen as the primary key, say RollNo.
- The other candidate keys are called alternate keys.



### Primary Key

- A primary key is a special column or combination of columns in a relational database table that uniquely identifies each row in the table    .
- A primary key is used as a unique identifier to quickly access and manipulate data within the table .
- A table can have only one primary key, and a primary key cannot have null values   .
- A primary key can be either a simple key (a single column) or a composite key (a combination of two or more columns)   .
- A primary key can be defined at the time of table creation (using the PRIMARY KEY constraint) or after the table is created (using the ALTER TABLE statement) .
- A primary key can be referenced by other tables to create relationships between tables (using the FOREIGN KEY constraint) .



### Generalization for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A database is a collection of related data that can be stored, manipulated, and retrieved by a software system.
- A database management system (DBMS) is a software system that provides the functionality to create, maintain, and access databases.
- A DBMS can support different types of databases, such as relational, hierarchical, network, object-oriented, document, graph, etc.
- A DBMS can also support different types of data models, such as entity-relationship, relational, object-oriented, etc.
- A data model is a conceptual representation of the data and the relationships among them.
- A schema is a description of the structure and constraints of a database, based on a data model.
- A schema can be specified at different levels of abstraction, such as conceptual, logical, and physical.
- A conceptual schema is a high-level description of the data and the relationships among them, independent of any implementation details.
- A logical schema is a description of the data and the relationships among them, using a specific data model, such as relational or object-oriented.
- A physical schema is a description of how the data and the relationships among them are stored and accessed by the DBMS, such as file structures, indexes, etc.
- A database instance is a snapshot of the data stored in a database at a given point in time.
- A database application is a software program that interacts with a database to perform some tasks, such as querying, updating, or analyzing the data.
- A database application can use different types of interfaces to communicate with the DBMS, such as graphical user interface (GUI), command-line interface (CLI), application programming interface (API), etc.
- A database application can also use different types of languages to specify the operations on the data, such as data definition language (DDL), data manipulation language (DML), data query language (DQL), data control language (DCL), etc.
- A database system is a combination of a database, a DBMS, and a database application.



### Aggregation for the notes of the Unit 1 - Introduction in the subject of Database Management System

- Aggregation is a process of combining data from multiple records or tables and grouping them together based on one or more columns.
- Aggregation can be done using SQL aggregate functions such as SUM, COUNT, AVG, MIN, and MAX.
- Aggregation is often used to calculate statistics or to summarize data in a more meaningful way.
- Aggregation can also be explained using the entity-relationship model (ER model), which is a conceptual diagram that represents the structure of a database and its components.
- Aggregation in ER model is a process of combining two or more entities to form a more meaningful new entity.
- Aggregation in ER model is done when the entities don't make sense on their own without applying the aggregation process.
- For example, a student entity and a course entity can be aggregated to form a new entity called enrollment, which represents the relationship between the student and the course.
- Aggregation in ER model is also needed if a DBMS has a single trivial entity that should be used for multiple relationships, or if an entity-model relationship is not applicable for some entities.
- For example, a person entity can be aggregated with a car entity to form a new entity called driver, which represents the relationship between the person and the car.
- Aggregation in DBMS has many applications across all industries, such as forecasting sales, analyzing customer behavior, measuring performance, and so on.



### Reduction of an ER Diagrams to Tables

- An ER diagram is a graphical representation of the entities and their relationships in a database.
- A table is a collection of rows and columns that store data in a database.
- To convert an ER diagram to a set of tables, we need to follow some rules and steps.
- The rules and steps are:

  - For each entity type in the ER diagram, create a table with the same name and attributes as the entity type.
  - For each one-to-one or one-to-many relationship type in the ER diagram, choose one of the entity types involved in the relationship and add the primary key of the other entity type as a foreign key in the chosen table. The foreign key should have the same name as the primary key of the other entity type. If the relationship type has any attributes, add them as columns in the chosen table as well.
  - For each many-to-many relationship type in the ER diagram, create a new table with the same name as the relationship type and add the primary keys of both entity types involved in the relationship as foreign keys in the new table. The foreign keys should have the same names as the primary keys of the entity types. If the relationship type has any attributes, add them as columns in the new table as well.
  - For each weak entity type in the ER diagram, create a table with the same name and attributes as the weak entity type and add the primary key of the identifying entity type as a foreign key in the weak entity table. The foreign key should have the same name as the primary key of the identifying entity type. The primary key of the weak entity table should be a composite key consisting of the foreign key and the partial key of the weak entity type.
  - For each multivalued attribute in the ER diagram, create a new table with the same name as the attribute and add the primary key of the entity type that has the multivalued attribute as a foreign key in the new table. The foreign key should have the same name as the primary key of the entity type. The new table should also have a column for the value of the multivalued attribute. The primary key of the new table should be a composite key consisting of the foreign key and the value column.
  - For each derived attribute in the ER diagram, do not create a column in the table of the entity type that has the derived attribute. Instead, use a function or a query to calculate the value of the derived attribute whenever needed.
  - For each generalization or specialization in the ER diagram, choose one of the following options:
    - Option 1: Create a table for each entity type in the hierarchy, including the superclass and the subclasses. Add the primary key of the superclass as a foreign key in each subclass table. The foreign key should have the same name as the primary key of the superclass. If the superclass has any attributes that are inherited by the subclasses, add them as columns in the superclass table only. If the subclasses have any attributes that are specific to them, add them as columns in the subclass tables only. If the subclasses have any relationships that are specific to them, add the foreign keys for those relationships in the subclass tables only.
    - Option 2: Create a table for the superclass only and add a column for the type of the entity. The type column should have a value that indicates which subclass the entity belongs to. Add all the attributes of the superclass and the subclasses as columns in the superclass table. If the subclasses have any relationships that are specific to them, add the foreign keys for those relationships in the superclass table as well. Use null values to indicate the absence of attributes or relationships for some entities.



### Extended ER Model

- The extended entity-relationship (EER) model is an extension of the entity-relationship (ER) model that incorporates more semantic information into the conceptual design of databases.
- The EER model introduces new concepts such as **subclasses**, **superclasses**, **specialization**, **generalization**, **category** and **inheritance** to capture more complex and hierarchical relationships among entities and attributes.
- A **subclass** is a subset of entities that belong to a larger entity set, called a **superclass**. A subclass inherits all the attributes and relationships of its superclass, and may have additional attributes and relationships that are specific to it.
- A **specialization** is the process of defining one or more subclasses of an entity type based on some distinguishing characteristics. For example, a specialization of EMPLOYEE could be MANAGER, ENGINEER, or SECRETARY, based on the job title attribute.
- A **generalization** is the reverse process of specialization, where several entity types are combined into a single entity type based on their common attributes and relationships. For example, a generalization of MANAGER, ENGINEER, and SECRETARY could be EMPLOYEE, based on the shared attributes such as name, salary, and department.
- A **category** (or **union type**) is a special type of entity that represents the collection of entities from different entity types that share a common relationship with another entity type. For example, a category of OWNER could include entities from PERSON, COMPANY, and BANK, that are related to the entity type PROPERTY through the relationship OWNS.
- **Inheritance** is the property of subclasses that allows them to inherit the attributes and relationships of their superclasses. Inheritance can be **total** or **partial**, and **disjoint** or **overlapping**.
  - **Total** inheritance means that every entity in the superclass must belong to at least one subclass. **Partial** inheritance means that some entities in the superclass may not belong to any subclass.
  - **Disjoint** inheritance means that an entity can belong to only one subclass of a given superclass. **Overlapping** inheritance means that an entity can belong to more than one subclass of a given superclass.



### Relationship of Higher Degree

- A relationship of higher degree is a relationship that involves more than two entities.
- For example, a ternary relationship is a relationship of degree three, which means it relates three entities.
- A common example of a ternary relationship is the **enrolls** relationship between **student**, **course**, and **section** entities. A student enrolls in a section of a course, and a section belongs to a course.
- A relationship of higher degree can be represented in an entity-relationship (ER) diagram using a diamond-shaped symbol with the name of the relationship and the degree as a subscript.
- For example, the **enrolls** relationship can be represented as:

enrolls

- A relationship of higher degree can also be converted into an equivalent set of binary relationships by introducing a new entity that represents the combination of the original entities.
- For example, the **enrolls** relationship can be converted into two binary relationships by introducing a new entity called **enrollment** that has the primary keys of **student**, **course**, and **section** as its attributes.
- The new ER diagram would look like:

enrollment

- The advantage of converting a relationship of higher degree into binary relationships is that it simplifies the design and implementation of the database schema.
- The disadvantage is that it may introduce redundancy and inconsistency in the data, as the same information may be stored in multiple places.



## Unit 2 - Relational data Model and Language

- Relational data model is a way of representing data in tables, where each row represents an entity or a record, and each column represents an attribute or a field.
- Relational data model is based on the concept of mathematical relations, which are sets of ordered tuples or pairs of values.
- Relational data model has some advantages over other data models, such as simplicity, flexibility, integrity, and scalability.
- Relational data model has some limitations, such as lack of support for complex data types, semantic ambiguity, and performance issues.
- Relational data language is a set of commands or statements that are used to manipulate data in a relational database.
- Relational data language can be divided into two categories: data definition language (DDL) and data manipulation language (DML).
- Data definition language (DDL) is used to create, modify, or delete the structure of tables and other database objects, such as indexes, views, and constraints.
- Data manipulation language (DML) is used to insert, update, delete, or query data from tables and other database objects.
- Some examples of relational data languages are SQL, QBE, and Rel.



### Relational Data Model Concepts

The relational data model is a widely used data model for storing and processing data in a database. It is based on the concept of relations, which are logical structures that represent data as a collection of rows and columns. Each row in a relation is called a tuple, and each column is called an attribute. A relation can also be defined by a schema, which specifies the name and domain of each attribute.

Some of the major concepts in the relational data model are:

- **Primary key**: A primary key is a set of one or more attributes that uniquely identifies each tuple in a relation. A primary key must not contain null values, and it must be minimal, meaning that no subset of the primary key can also uniquely identify each tuple. A primary key is also called a candidate key or a superkey.
- **Foreign key**: A foreign key is a set of one or more attributes in a relation that references the primary key of another relation. A foreign key establishes a relationship between two relations, and it enforces referential integrity, meaning that the values of the foreign key must either match the values of the primary key in the referenced relation, or be null.
- **Domain**: A domain is a set of possible values for an attribute. A domain defines the data type, format, and constraints of an attribute. For example, a domain for a student ID attribute could be a set of integers between 1000 and 9999.
- **Degree**: The degree of a relation is the number of attributes in its schema. For example, a relation with four attributes has a degree of four.
- **Cardinality**: The cardinality of a relation is the number of tuples in it. For example, a relation with 10 tuples has a cardinality of 10.
- **Relation instance**: A relation instance is a snapshot of the data in a relation at a given point in time. A relation instance can change over time as tuples are inserted, deleted, or updated.
- **Relational algebra**: Relational algebra is a set of operations that can be applied to relations to manipulate and query data. Some of the basic operations are selection, projection, join, union, intersection, and difference. Relational algebra provides a formal foundation for the relational data model and the SQL language.



### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- There are four types of integrity constraints in the relational data model: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

#### Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- For example, the attribute `age` of a relation `student` can have a domain constraint that limits its values to positive integers less than or equal to 150.

#### Key Constraints

- Key constraints specify one or more attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by declaring primary keys or candidate keys for the relations.
- For example, the attribute `student_id` of a relation `student` can be a primary key that uniquely identifies each student.

#### Entity Integrity Constraints

- Entity integrity constraints ensure that every tuple in a relation has a unique and non-null value for its primary key.
- Entity integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule.
- For example, the relation `student` cannot have two tuples with the same value for `student_id`, or a tuple with a null value for `student_id`.

#### Referential Integrity Constraints

- Referential integrity constraints ensure that a value that appears in one relation for a given set of attributes also appears in another relation for a corresponding set of attributes.
- Referential integrity constraints can be enforced by declaring foreign keys that reference primary keys of other relations.
- For example, the attribute `course_id` of a relation `enrollment` can be a foreign key that references the primary key `course_id` of a relation `course`. This ensures that every course enrolled by a student exists in the `course` relation.



### Entity Integrity

- Entity integrity is a rule that ensures that each entity in a table has a unique and non-null identifier or primary key.
- A primary key is a column or a combination of columns that can uniquely identify each row in a table.
- Entity integrity prevents duplicate or missing data in a table and ensures that each entity can be distinguished from others.
- Entity integrity is enforced by the database system by rejecting any insertion, update, or deletion that violates the rule.
- Entity integrity is important for maintaining data quality, consistency, and accuracy in a relational database.



### Referential Integrity

- Referential integrity is a property of data stating that all its references are valid .
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist .
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key .
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table .
- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- Referential integrity prevents the creation of orphan records, which are records that have no corresponding data in the related table .
- Referential integrity also prevents the deletion or modification of data that is referenced by other data .
- Referential integrity can be enforced by working with primary and foreign keys .
- Referential integrity can also be enforced by using constraints, triggers, or cascading actions .
- Referential integrity is a type of data integrity, which is the overall accuracy, completeness, and consistency of data in a database .



### Keys Constraints

- A key is a set of one or more attributes that can uniquely identify a tuple in a relation.
- A key constraint is a rule that specifies that the values of a key must be distinct, i.e., no two tuples can have the same key value.
- A key can be either a candidate key or a primary key.
- A candidate key is a minimal set of attributes that can uniquely identify a tuple, i.e., no proper subset of the candidate key can serve as a key.
- A primary key is a candidate key that is chosen by the database designer to identify tuples in a relation.
- A relation can have more than one candidate key, but only one primary key.
- A primary key can be either a simple key or a composite key.
- A simple key is a key that consists of a single attribute.
- A composite key is a key that consists of two or more attributes.
- A foreign key is a set of attributes in a relation that references the primary key of another relation (or the same relation in case of recursive relationships).
- A foreign key constraint is a rule that specifies that the values of a foreign key must either match the values of an existing primary key in the referenced relation, or be null.
- A foreign key constraint enforces the referential integrity of the database, i.e., it ensures that there are no dangling references or orphan tuples.



### Domain Constraints

- Domain constraints are the rules that specify the valid values for an attribute in a relation.
- Domain constraints are part of the relational data model and are enforced by the DBMS.
- Domain constraints can be defined by specifying the data type, format, range, or set of permissible values for an attribute.
- Domain constraints help to ensure the integrity and consistency of the data in the database.
- Domain constraints can be violated by inserting, updating, or deleting data that does not conform to the rules.
- Domain constraints can be checked by using SQL commands such as CREATE TABLE, ALTER TABLE, or CHECK.



### Relational Algebra

- Relational algebra is a theory that uses algebraic structures for modeling data, and defining queries on it with a well founded semantics.
- Relational algebra provides a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.
- Relational databases store tabular data represented as relations. Queries over relational databases often likewise return tabular data represented as relations.
- Relational algebra is considered as a procedural query language, where the user tells the system to carry out a set of operations to obtain the desired results.
- Relational algebra operations are designed to do the most common things that we need to do with relations in a database.
- Relational algebra operations can be divided into two categories: basic and derived.
- Basic operations are those that are directly supported by the relational model, such as selection, projection, union, set difference, Cartesian product, and rename.
- Derived operations are those that can be expressed in terms of the basic operations, such as intersection, natural join, division, assignment, and aggregate functions.
- Relational algebra operations can be applied to one or more relations and produce a new relation as a result.
- Relational algebra operations can be represented by symbols or by expressions in a query language.
- Relational algebra operations can be composed together to form more complex queries.
- Relational algebra operations can be evaluated by using various algorithms and data structures, such as indexes, hash tables, and sorting.



### Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a **non-procedural** query language that describes **what** data to retrieve from a relational database, without specifying **how** to do it  .
- Relational calculus is based on **mathematical logic**, specifically **predicate calculus**, which uses variables, constants, operators, quantifiers, and predicates to form expressions  .
- Relational calculus is an **integral part** of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- Relational calculus can be classified into two types: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**   .
- Tuple relational calculus uses **tuple variables** to represent rows of a relation and **predicate expressions** to specify the conditions for selecting tuples  . For example, the query to find the names and phone numbers of book stores that sell a book titled "Some Sample Book" can be written as:

```
{t.StoreName, t.StorePhone | t ∈ Bookstore ∧ ∃b(b ∈ Book ∧ b.BookstoreID = t.BookstoreID ∧ b.BookTitle = "Some Sample Book")}
```

- Domain relational calculus uses **domain variables** to represent individual values of the attributes of a relation and **predicate expressions** to specify the conditions for selecting values  . For example, the same query as above can be written as:

```
{x, y | ∃z(Bookstore(x, y, z) ∧ ∃w(Book(z, w, "Some Sample Book")))}
```

- Both TRC and DRC are **equivalent** in expressive power, meaning that any query that can be written in one form can also be written in the other form  .
- Relational calculus is also **equivalent** to relational algebra, another query language that is **procedural** and specifies **how** to manipulate the relations to obtain the desired result  .
- Relational calculus is a **declarative** language that allows users to focus on the **logic** of the query, rather than the **implementation** details  .
- Relational calculus is a **formal** language that has a **well-defined syntax** and **semantics**, and can be used to **prove** the correctness and optimality of query processing algorithms  .



### Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a declarative query language for relational databases.
- Relational calculus allows users to specify what they want to retrieve from the database, without describing how to do it.
- Tuple and domain calculus differ in the way they use variables to represent the data.

#### Tuple Relational Calculus (TRC)

- In TRC, variables are tuples that belong to a relation.
- A TRC query has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate that involves `t` and possibly other tuple variables.
- A TRC query returns the set of all tuples `t` that satisfy the predicate `P(t)`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the set of all employees who earn more than 5000.
- TRC can express any query that can be expressed in relational algebra, and vice versa. This means that TRC is relationally complete.

#### Domain Relational Calculus (DRC)

- In DRC, variables are values that belong to the domains of the attributes of a relation.
- A DRC query has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `<x1, x2, ..., xn>` is a list of domain variables and `P(x1, x2, ..., xn)` is a predicate that involves the domain variables and possibly constants.
- A DRC query returns the set of all tuples `<x1, x2, ..., xn>` that satisfy the predicate `P(x1, x2, ..., xn)`.
- For example, the query `{<E.Name, E.Salary> | E ∈ Employee and E.Salary > 5000}` returns the set of names and salaries of all employees who earn more than 5000.
- DRC can also express any query that can be expressed in relational algebra, and vice versa. This means that DRC is also relationally complete.

#### Comparison of TRC and DRC

- Both TRC and DRC are declarative and expressive query languages for relational databases.
- TRC is more intuitive and natural for users who are familiar with the concept of tuples and relations.
- DRC is more flexible and concise for users who want to specify the attributes and values of interest.
- TRC and DRC are equivalent in expressive power, but some queries may be easier to write in one form than the other.



### Introduction to SQL

SQL is a computer language for storing, manipulating, and retrieving data in a relational database. SQL allows you to create, modify and query databases. SQL is a standard language that is used by most relational databases. SQL is used to access and manipulate data stored in tables.

Some of the main features of SQL are:

- SQL is a declarative language, which means you specify what you want to do, not how to do it.
- SQL is a structured language, which means it follows a set of rules and syntax.
- SQL is a query language, which means it can be used to ask questions and get answers from the data.
- SQL is a data definition language, which means it can be used to create, alter, and delete database objects such as tables, views, indexes, etc.
- SQL is a data manipulation language, which means it can be used to insert, update, and delete data in tables.
- SQL is a data control language, which means it can be used to grant and revoke permissions and roles to users and groups.

SQL is divided into several sublanguages, such as:

- Data Query Language (DQL): used to select data from tables.
- Data Manipulation Language (DML): used to insert, update, and delete data in tables.
- Data Definition Language (DDL): used to create, alter, and drop database objects.
- Data Control Language (DCL): used to grant and revoke permissions and roles.
- Transaction Control Language (TCL): used to manage transactions and concurrency.

SQL is supported by many relational database management systems (RDBMS), such as MySQL, Oracle, SQL Server, PostgreSQL, etc. Each RDBMS may have some variations and extensions to the standard SQL syntax and features, but the core concepts and commands are the same.

SQL is a powerful and versatile language that can be used for various purposes, such as:

- Data analysis and reporting
- Data warehousing and business intelligence
- Data integration and migration
- Data validation and quality
- Data security and auditing
- Data modeling and design
- Application development and testing

SQL is a widely used and popular language that is essential for anyone who works with data. Learning SQL can help you to understand and manipulate data in a relational database, and to communicate with other data professionals and systems. SQL can also help you to develop your logical thinking and problem-solving skills.



### Characteristics of SQL

SQL is a computer language used to store, manipulate, and retrieve data from a relational database. SQL has the following characteristics:

- **Easy to learn**: SQL is an extremely practical and user-friendly language. Even if you have no prior experience with programming, you can learn the basic syntax and commands of SQL in a short time.
- **Wide variety of commands**: SQL supports a wide variety of commands such as DDL (Data Definition Language) commands, DML (Data Manipulation Language) commands, DCL (Data Control Language) commands, and TCL (Transaction Control Language) commands. These commands allow you to perform different tasks on the database, such as creating, modifying, deleting, querying, and controlling data.
- **Stored procedures**: A stored procedure is a set of SQL statements that can be executed as a single unit. Stored procedures can improve the performance, security, and maintainability of the database. They can also reduce the network traffic and the complexity of the application code.
- **High performance**: SQL provides high-performance programming capability for highly transactional, heavy workload, and high usage database systems. SQL programming gives various ways to describe the data more analytically, such as using aggregate functions, subqueries, joins, and views.
- **Portability**: SQL is a standard language that is supported by most of the relational database management systems, such as Oracle, MySQL, SQL Server, PostgreSQL, and SQLite. SQL can also run on different platforms, such as Windows, Linux, and Mac OS. This makes SQL portable and compatible across different systems.



### Advantage of SQL for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- SQL is a **standardized** language for manipulating relational data, which means it is widely supported by different database systems and applications.
- SQL is a **declarative** language, which means it allows the user to specify **what** data they want to retrieve or modify, without having to specify **how** to do it. This makes SQL easier to learn and use than procedural languages.
- SQL is a **high-level** language, which means it abstracts away the low-level details of data storage and retrieval, and allows the user to focus on the logical structure and meaning of the data.
- SQL is a **flexible** language, which means it can perform a variety of operations on data, such as selection, projection, join, aggregation, grouping, sorting, filtering, etc. SQL can also combine multiple operations in a single query, using subqueries, views, and functions.
- SQL is a **powerful** language, which means it can express complex queries and calculations on data, using operators, expressions, and clauses. SQL can also handle large amounts of data efficiently, using indexes, transactions, and concurrency control.



### SQL Data Types and Literals

- SQL data types are the categories of values that can be stored in a column of a table or a variable in a program.
- SQL data types are divided into two main groups: scalar and non-scalar.
- Scalar data types store a single value, such as a number, a string, a date, or a boolean.
- Non-scalar data types store a collection of values, such as an array, a table, or a spatial object.
- SQL data types can be further classified into standard and user-defined data types.
- Standard data types are predefined by the SQL language and supported by most database systems, such as INTEGER, VARCHAR, DATE, etc.
- User-defined data types are created by the user using the CREATE TYPE statement, and can be based on existing data types or defined as distinct types with specific constraints and methods.
- SQL literals are the explicit values that can be assigned to a data type, such as 42, 'Hello', or TRUE.
- SQL literals can be classified into four categories: numeric, string, date/time, and boolean literals.
- Numeric literals are the values that can be assigned to numeric data types, such as INTEGER, DECIMAL, FLOAT, etc. They can be written with or without a decimal point, and can have an optional sign (+ or -) and an optional exponent (E or e followed by a number).
- String literals are the values that can be assigned to string data types, such as CHAR, VARCHAR, TEXT, etc. They are enclosed in single quotes (' '), and can contain any character except the single quote itself, which must be escaped by doubling it ('').
- Date/time literals are the values that can be assigned to date/time data types, such as DATE, TIME, TIMESTAMP, etc. They are written in a specific format, depending on the data type and the database system, and can include separators, such as dashes (-), slashes (/), colons (:), or spaces ( ).
- Boolean literals are the values that can be assigned to boolean data types, such as BOOLEAN, BIT, etc. They are written as TRUE or FALSE, or as 1 or 0, depending on the database system.



### Types of SQL Commands

SQL (Structured Query Language) is a standard language for manipulating and querying data in relational databases. SQL commands can be classified into four main categories:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of database objects, such as tables, views, indexes, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc.
  - ALTER: This command is used to modify the structure or properties of an existing database object, such as adding, deleting, or renaming columns, constraints, etc.
  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc.
  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, etc.
  - TRUNCATE: This command is used to delete all the data from a table, but not the table structure itself.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - INSERT: This command is used to insert one or more rows of data into a table.
  - UPDATE: This command is used to modify one or more rows of data in a table.
  - DELETE: This command is used to delete one or more rows of data from a table.
  - SELECT: This command is used to retrieve data from one or more tables, based on certain criteria or conditions.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of users and roles on database objects, such as granting or revoking privileges, creating or dropping users, etc. Some examples of DCL commands are:

  - GRANT: This command is used to grant one or more privileges to a user or a role on a database object, such as SELECT, INSERT, UPDATE, DELETE, etc.
  - REVOKE: This command is used to revoke one or more privileges from a user or a role on a database object, such as SELECT, INSERT, UPDATE, DELETE, etc.
  - CREATE USER: This command is used to create a new user in the database, with a username and a password.
  - DROP USER: This command is used to delete an existing user from the database, along with their privileges and objects.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, such as committing or rolling back the changes made by DML commands, setting the isolation level, etc. Some examples of TCL commands are:

  - COMMIT: This command is used to save the changes made by DML commands in the database permanently.
  - ROLLBACK: This command is used to undo the changes made by DML commands in the database, and restore the previous state.
  - SAVEPOINT: This command is used to create a point in the transaction, where the changes can be rolled back to, without affecting the entire transaction.
  - SET TRANSACTION: This command is used to set the isolation level of the transaction, which determines how the transaction is affected by other concurrent transactions. The isolation levels are: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, and SERIALIZABLE.



### SQL Operators and Their Procedure

- SQL operators are symbols or keywords that are used to perform various operations on data in a relational database.
- SQL operators can be classified into four categories: arithmetic, comparison, logical, and set operators.
- Arithmetic operators are used to perform mathematical calculations on numeric values or expressions. They include `+`, `-`, `*`, `/`, and `%` (modulo).
- Comparison operators are used to compare two values or expressions and return a Boolean value (`TRUE`, `FALSE`, or `NULL`). They include `=`, `<>` (not equal), `<`, `>`, `<=`, `>=`, `BETWEEN`, `IN`, `LIKE`, and `IS NULL`.
- Logical operators are used to combine two or more Boolean values or expressions and return a Boolean value. They include `AND`, `OR`, `NOT`, and `XOR`.
- Set operators are used to combine two or more result sets from different queries and return a single result set. They include `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT` (or `MINUS`).

- The procedure for using SQL operators is as follows:
  - Identify the type of operation to be performed on the data and choose the appropriate operator(s).
  - Write the SQL query using the operator(s) and the operands (values or expressions) in the correct syntax and order.
  - Execute the query and check the result set for accuracy and completeness.
  - If needed, modify the query or use additional operators to refine the result set.



### Tables for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A table is a collection of data organized in rows and columns.
- A table has a name, a set of attributes, and a set of tuples.
- An attribute is a column of a table that represents a property or characteristic of the entities in the table.
- A tuple is a row of a table that represents an instance or occurrence of the entities in the table.
- A table can be represented as a set of tuples, or as a matrix of values, where each row corresponds to a tuple and each column corresponds to an attribute.
- A table can also be represented as a relation, which is a mathematical concept that defines a set of ordered pairs, where each pair consists of a value from the domain of each attribute.
- A table has a degree, which is the number of attributes in the table, and a cardinality, which is the number of tuples in the table.
- A table has a schema, which is the description of the structure and constraints of the table, such as the name, the attributes, the data types, the primary key, the foreign key, etc.
- A table has a state, which is the set of tuples that are currently stored in the table at a given point in time.
- A table can be manipulated using a relational data language, such as SQL, which allows users to create, update, delete, and query data in the table.



### Views and Indexes

- A **view** is a named query that defines a logical table based on the result of a SELECT statement.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface to different tables.
- A view can be created, modified, or dropped using the CREATE VIEW, ALTER VIEW, or DROP VIEW statements.
- A view can be queried, updated, inserted, or deleted from as if it were a base table, subject to some restrictions.
- A view does not store any data physically, but only references the data in the underlying tables.
- An **index** is a data structure that improves the speed of data retrieval operations on a table.
- An index can be created on one or more columns of a table, providing a sorted look-up for the rows.
- An index can be created, modified, or dropped using the CREATE INDEX, ALTER INDEX, or DROP INDEX statements.
- An index can reduce the number of disk accesses required to find a row or a range of rows, thus improving query performance.
- An index can also enforce uniqueness constraints on a table, preventing duplicate values in the indexed columns.
- An index requires additional disk space and maintenance overhead, and can slow down data modification operations on a table.
- An **indexed view** is a special type of view that has a unique clustered index on it, and stores the view data physically as a table .
- An indexed view can improve the performance of queries that join and aggregate data from multiple tables .
- An indexed view has some limitations and requirements, such as the same owner as the referenced tables, the SCHEMABINDING option, and the compatibility level of the database .
- An indexed view can be created, modified, or dropped using the same statements as a regular view, but with the addition of the WITH clause to specify the index options .
- An indexed view can be used explicitly by referencing its name in a query, or implicitly by the query optimizer if the query matches the view definition .



### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A query is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language such as SQL, which specifies what data is needed, not how to get it.
- A subquery is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used when you need to process data in several steps, or when you want to use the result of one query as an input for another query. Subqueries can also be used to compare values, test for existence, or perform aggregations.
- There are three types of subqueries: scalar, multirow, and correlated.
  - A scalar subquery returns a single value and can be used anywhere a literal value can be used, such as in a WHERE clause, a SELECT clause, or an assignment statement. For example:

    ```sql
    SELECT name, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees);
    ```

    This query returns the name and salary of employees who earn more than the average salary of all employees. The scalar subquery `(SELECT AVG(salary) FROM employees)` returns the average salary as a single value.

  - A multirow subquery returns one or more rows and can be used with operators such as IN, ANY, ALL, EXISTS, or NOT EXISTS. For example:

    ```sql
    SELECT name, department_id
    FROM employees
    WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
    ```

    This query returns the name and department ID of employees who work in departments located in New York. The multirow subquery `(SELECT department_id FROM departments WHERE location = 'New York')` returns a set of department IDs that match the condition.

  - A correlated subquery is a subquery that depends on the outer query for its values. A correlated subquery is executed once for each row of the outer query, and the result of the subquery is compared with the value of the outer query row. For example:

    ```sql
    SELECT name, salary
    FROM employees e
    WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);
    ```

    This query returns the name and salary of employees who earn more than the average salary of their department. The correlated subquery `(SELECT AVG(salary) FROM employees WHERE department_id = e.department_id)` returns the average salary for each department, using the department ID from the outer query row.

- Relational data model and language is a way of representing and manipulating data in a database using tables, columns, rows, and keys. A relational database is a collection of tables, each with a unique name and a set of columns. A row in a table is a record of data, and a column is an attribute of data. A key is a column or a combination of columns that uniquely identifies a row in a table.
- A relational query language is a language that allows users to access and manipulate data in a relational database. The most widely used relational query language is SQL, which stands for Structured Query Language. SQL has commands for creating, modifying, querying, and deleting data and tables in a database. SQL also has features for defining views, functions, procedures, triggers, and constraints. SQL is a standard language, but different database systems may have different extensions or variations of SQL.



### Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the `GROUP BY` clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - `COUNT`: returns the number of values in a set or the number of rows that satisfy a condition.
  - `SUM`: returns the sum of all values in a set or the sum of values that satisfy a condition.
  - `AVG`: returns the average of all values in a set or the average of values that satisfy a condition.
  - `MIN`: returns the minimum value in a set or the minimum value that satisfies a condition.
  - `MAX`: returns the maximum value in a set or the maximum value that satisfies a condition.

- Aggregate functions can be used in the `SELECT` clause, the `HAVING` clause, or the `ORDER BY` clause of a query.
- Aggregate functions ignore `NULL` values in the set of values they operate on, unless otherwise specified by the `ALL` or `DISTINCT` modifiers.
- Examples of aggregate functions:

  - `SELECT COUNT(*) FROM student;` returns the number of rows in the `student` table.
  - `SELECT AVG(marks) FROM student WHERE grade = 'A';` returns the average marks of students who have grade A.
  - `SELECT MIN(salary), MAX(salary) FROM employee GROUP BY department;` returns the minimum and maximum salary for each department.
  - `SELECT department, SUM(salary) AS total_salary FROM employee GROUP BY department HAVING SUM(salary) > 100000;` returns the department and the total salary for each department that has a total salary greater than 100000.
  - `SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 1;` returns the name and salary of the employee with the highest salary.



### Relational Data Model and Language

- Relational Data Model and Language is a way of organizing and manipulating data in a relational database using tables and SQL commands.
- A relational database is a collection of relations (tables) that store data in rows (tuples) and columns (attributes).
- A relation has a name and a set of attributes. Each attribute has a name and a domain (a set of possible values).
- A tuple is a row of values, one for each attribute of the relation. A tuple represents an entity or a relationship among entities.
- A key is a set of one or more attributes that uniquely identifies a tuple in a relation. A primary key is a key that is chosen to be the main identifier of a relation. A foreign key is a key that references a primary key of another relation.
- A relational schema is a set of relation names, attributes, domains, and constraints that define the structure of a relational database.
- A relational instance is a set of tuples that satisfy the relational schema at a given point in time.
- A relational algebra is a set of operations that can be applied to relations or sets of relations to produce new relations. The basic operations are selection, projection, union, set difference, Cartesian product, and join.
- A relational calculus is a declarative language that allows users to specify what data they want from a relational database, without specifying how to get it. The basic elements are variables, constants, operators, and quantifiers.
- SQL (Structured Query Language) is a widely used relational language that combines aspects of both relational algebra and relational calculus. SQL allows users to create, manipulate, and query relational databases using statements that consist of clauses, expressions, predicates, and queries.



### Update and Delete Operations for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes in one or more tuples of a relation, based on a specified condition.
- Delete operations can remove one or more tuples from a relation, based on a specified condition.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and in accordance with the defined constraints and rules.
- The syntax for update and delete operations in SQL (Structured Query Language) is as follows:

```sql
-- Update operation
UPDATE <relation_name>
SET <attribute_name> = <new_value>, ...
WHERE <condition>;

-- Delete operation
DELETE FROM <relation_name>
WHERE <condition>;
```

- The `<relation_name>` is the name of the relation to be updated or deleted from.
- The `<attribute_name>` is the name of the attribute to be updated.
- The `<new_value>` is the new value to be assigned to the attribute.
- The `<condition>` is a logical expression that specifies which tuples to be updated or deleted.
- The `WHERE` clause is optional, but if omitted, all tuples in the relation will be updated or deleted.
- The `SET` clause can update multiple attributes at once, separated by commas.
- The update and delete operations can be combined with other SQL clauses, such as `ORDER BY`, `LIMIT`, `JOIN`, etc., to perform more complex operations.

- Some examples of update and delete operations in SQL are:

```sql
-- Update the salary of all employees who work in department 10 by 10%
UPDATE employee
SET salary = salary * 1.1
WHERE dept_no = 10;

-- Delete all employees who have not worked for more than a year
DELETE FROM employee
WHERE hire_date < CURRENT_DATE - INTERVAL '1 year';

-- Update the name and phone number of the supplier with id 123
UPDATE supplier
SET name = 'ABC Inc.', phone = '555-1234'
WHERE id = 123;

-- Delete all orders that have been shipped
DELETE FROM order
WHERE status = 'shipped';
```



### Joins for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Joins are operations in relational databases that allow queries across multiple database tables.
- Joins merge data stored in different tables and output it in filtered form in a results table.
- Joins are based on the relational algebra operation of the same name – a combination of Cartesian product and selection.
- The prerequisite for joins is that the selected tables are linked to one another using foreign key relationships.
- The most important join types include the following:
  - Theta (θ) join: Theta join combines tuples from different relations provided they satisfy the theta condition. The join condition is denoted by the symbol θ.
  - Equijoin: When theta join uses only equality comparison operator, it is said to be equijoin.
  - Natural join (⋈): Natural join does not use any comparison operator. It automatically matches the columns with the same name and data type from both the tables.
  - Outer join: Outer join returns all the tuples from one relation and only the matching tuples from the other relation.
  - Left outer join (R S): Left outer join returns all the tuples from the left relation R and only the matching tuples from the right relation S.
  - Right outer join (R S): Right outer join returns all the tuples from the right relation S and only the matching tuples from the left relation R.
  - Full outer join (R S): Full outer join returns all the tuples from both the relations R and S, regardless of whether they match or not.
- Joins are used to stitch the database back together to make it easy to read and use. They match rows between tables. In most cases, we’re matching a column value from one table with another.
- Joins can be expressed using SQL syntax, such as SELECT, FROM, WHERE, ON, USING, etc .
- Joins can also be represented using Venn diagrams or relational diagrams to visualize the relationships between tables.
- Joins are essential for data modeling, which is the process of identifying entities and their relationships.
- Joins can improve the performance, flexibility, and scalability of the database system.



### Unions

- A union is a set operation that combines the tuples of two relations into one relation.
- A union can only be performed on two relations that are union-compatible, meaning they have the same number of attributes and the corresponding attributes have the same data type .
- A union eliminates any duplicate tuples from the result relation .
- A union can be expressed in relational algebra as R1 UNION R2, where R1 and R2 are the two relations to be unioned.
- A union can be expressed in SQL as SELECT * FROM R1 UNION SELECT * FROM R2, where R1 and R2 are the two tables to be unioned.
- A union can be used to retrieve data from more than one table simultaneously and then combine the results into one table.
- A union can be useful for combining data from different sources or categories that have the same structure . For example, a union can be used to combine sales data from different regions or product lines.



### Intersection

- Intersection is a relational algebra operation that returns the common tuples from two relations.
- The symbol for intersection is ∩.
- The intersection of two relations R and S, denoted by R ∩ S, is the relation that contains all the tuples that are in both R and S.
- The intersection operation is commutative, meaning that R ∩ S = S ∩ R.
- The intersection operation is associative, meaning that (R ∩ S) ∩ T = R ∩ (S ∩ T).
- The intersection operation is idempotent, meaning that R ∩ R = R.
- The intersection operation is distributive over union, meaning that R ∩ (S ∪ T) = (R ∩ S) ∪ (R ∩ T).
- The intersection operation requires that the two relations have the same degree (number of attributes) and the same domain (type of values) for each attribute.
- The intersection operation preserves the attribute names and the order of the attributes from the first relation.
- The intersection operation can be implemented using a nested loop join algorithm, a hash join algorithm, or a sort-merge join algorithm.



### Minus

- Minus is a relational algebra operation that returns the tuples that are in the first relation but not in the second relation.
- Minus is also known as difference or set difference.
- Minus is denoted by the symbol `-`.
- Minus is a binary operation that requires both relations to have the same number and type of attributes.
- Minus is commutative, meaning that `R - S` is not necessarily equal to `S - R`.
- Minus can be used to find the tuples that are unique to one relation or to eliminate the common tuples from two relations.
- Minus can be expressed in SQL using the `EXCEPT` or `MINUS` keyword, depending on the database system.
- Minus can be combined with other relational algebra operations such as selection, projection, join, union, and intersection.
- Minus can be illustrated using a Venn diagram, where the shaded area represents the result of the minus operation.

Venn diagram of minus operation



### Cursors

- A cursor is a database object that allows you to manipulate data in a row-by-row manner.
- A cursor can be thought of as a pointer to a specific row within a query result .
- Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval, addition and removal of database records.
- Cursors extend result processing by:
  - Allowing positioning at specific rows of the result set.
  - Retrieving one row or block of rows from the current position in the result set.
  - Supporting data modifications to the rows at the current position in the result set.
- A cursor's lifecycle involves the following steps :
  - Declare a cursor: A cursor is declared by defining a SQL statement that returns a result set.
  - Open a cursor: A cursor is opened by executing the SQL statement and populating the result set.
  - Fetch data from a cursor: A cursor is fetched by moving the pointer to a row and retrieving the data from that row.
  - Close a cursor: A cursor is closed by releasing the result set and freeing the resources associated with the cursor.
  - Deallocate a cursor: A cursor is deallocated by removing the cursor definition from the database server.
- Cursors can be classified into different types based on their characteristics, such as :
  - Forward-only or scrollable: A forward-only cursor can only move from the first row to the last row, while a scrollable cursor can move in any direction.
  - Static or dynamic: A static cursor works on a snapshot of the result set, while a dynamic cursor reflects any changes made to the underlying data.
  - Keyset-driven or insensitive: A keyset-driven cursor works on a set of keys that identify the rows in the result set, while an insensitive cursor works on a copy of the result set.
  - Local or global: A local cursor is visible only within the scope of the batch, stored procedure, or trigger that declares it, while a global cursor is visible to all sessions on the database server.
- Cursors are useful when you need to perform complex logic or calculations on individual rows, or when you need to update data in a non-set-based manner.
- Cursors have some drawbacks, such as :
  - Consuming more memory and CPU resources than set-based operations.
  - Increasing the risk of locking and blocking issues due to holding locks on the data for a longer duration.
  - Reducing the performance and scalability of the database application due to the overhead of cursor operations.



### Triggers for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A trigger is a stored procedure that is executed automatically when a specified event occurs on a table or view in a database.
- A trigger can be used to enforce business rules, data integrity, security policies, or perform other actions such as auditing, logging, or notification.
- A trigger has three main components: a triggering event, a trigger condition, and a trigger action.
- A triggering event is the type of operation that activates the trigger, such as INSERT, UPDATE, or DELETE.
- A trigger condition is an optional Boolean expression that determines whether the trigger action should be executed or not, based on the data values or state of the database.
- A trigger action is a sequence of SQL statements or commands that are executed when the trigger is activated and the condition is satisfied.
- A trigger can be classified into two types: row-level triggers and statement-level triggers.
- A row-level trigger is executed once for each row that is affected by the triggering event, and has access to the old and new values of the row.
- A statement-level trigger is executed once for the whole statement that causes the triggering event, and does not have access to the individual rows.
- A trigger can also be classified into two types based on the timing of execution: before triggers and after triggers.
- A before trigger is executed before the triggering event takes place, and can be used to validate or modify the data before it is inserted, updated, or deleted.
- An after trigger is executed after the triggering event takes place, and can be used to perform additional actions or check the results of the operation.
- A trigger can be created, altered, or dropped using the CREATE TRIGGER, ALTER TRIGGER, or DROP TRIGGER statements in SQL.
- A trigger can be enabled or disabled using the ENABLE TRIGGER or DISABLE TRIGGER statements in SQL.
- A trigger can be viewed using the SHOW TRIGGERS statement or the INFORMATION_SCHEMA.TRIGGERS table in SQL.



### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it does not return a value like a function does.
- A procedure can be invoked by other PL/SQL blocks, triggers, procedures, functions, or applications written in different languages such as Java, PHP, etc.
- A procedure can be created using the CREATE PROCEDURE statement, which has the following syntax:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype [DEFAULT expr],
  parameter2 [mode] datatype [DEFAULT expr],
  ...)]
IS | AS
  [declaration_section]
BEGIN
  executable_section
[EXCEPTION
  exception_section]
END [procedure_name];
```

- The procedure name is a valid identifier that follows the naming rules of PL/SQL.
- The optional parameter list contains the names, modes, data types, and default values of the parameters. The mode can be IN, OUT, or IN OUT, indicating the direction of data flow between the procedure and the caller. The default mode is IN, which means the parameter is read-only. The OUT mode means the parameter is write-only, and the IN OUT mode means the parameter is both readable and writable.
- The IS or AS keyword separates the header and the body of the procedure.
- The optional declaration section contains the declarations of local variables, constants, cursors, and other items that are used in the procedure body.
- The mandatory executable section contains the PL/SQL statements that implement the logic of the procedure. It must have at least one executable statement, and it must end with a semicolon.
- The optional exception section handles the errors that may occur during the execution of the procedure. It contains one or more exception handlers that associate an exception name with a sequence of statements to handle it.
- The optional procedure name at the end of the block is used for readability and consistency. It must match the name at the beginning of the block.
- A procedure can be modified using the CREATE OR REPLACE PROCEDURE statement, which replaces the existing definition of the procedure with the new one.
- A procedure can be deleted using the DROP PROCEDURE statement, which removes the procedure definition and its dependencies from the database.



## Unit 3 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design and makes it easier to query, update, and maintain the data.
- There are several levels of normalization, each with a specific goal and criteria. The most common levels are:
  - First normal form (1NF): Each table has a primary key and each column contains atomic values (i.e., values that cannot be further divided).
  - Second normal form (2NF): Each table is in 1NF and each non-key column depends on the whole primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): Each table is in 2NF and each non-key column depends only on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): Each table is in 3NF and every determinant (i.e., a set of columns that determines another column) is a candidate key (i.e., a minimal set of columns that uniquely identifies a row).
  - Fourth normal form (4NF): Each table is in BCNF and there are no multi-valued dependencies (i.e., situations where a column can have more than one value for a given primary key).
  - Fifth normal form (5NF): Each table is in 4NF and there are no join dependencies (i.e., situations where a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys).
- To normalize a database, one can follow these steps:
  - Identify the entities and attributes that need to be stored in the database and create a conceptual model (e.g., an entity-relationship diagram).
  - Convert the conceptual model into a logical model (e.g., a relational schema) and assign primary keys and foreign keys to the tables.
  - Apply the normalization rules to the logical model and check if it satisfies the desired level of normalization. If not, decompose the tables into smaller ones and repeat the process until the desired level is reached.
  - Convert the logical model into a physical model (e.g., a SQL script) and implement the database on the RDBMS.



### Functional dependencies

- A functional dependency (FD) is a constraint between two sets of attributes from a relation.
- A functional dependency X -> Y means that the values of Y are determined by the values of X. In other words, if two tuples have the same values for X, they must also have the same values for Y.
- A functional dependency is a property of the semantics or meaning of the attributes. It does not depend on the actual data in the relation.
- A functional dependency can be represented by an arrow diagram, where the attributes on the left of the arrow are called the determinant and the attributes on the right are called the dependent.
- For example, consider a relation Student with attributes RollNo, Name, Branch, and CGPA. A possible functional dependency is RollNo -> Name, which means that the name of a student is uniquely determined by their roll number. This can be represented by the following arrow diagram:

```
RollNo -> Name
```

- A relation is said to satisfy a functional dependency if the dependency holds for every possible instance of the relation.
- A set of functional dependencies F is said to be a cover for a relation R if F logically implies all the functional dependencies that hold on R.
- A set of functional dependencies F is said to be minimal if it is a cover for R and no proper subset of F is a cover for R. A minimal cover has the following properties:
  - No functional dependency in F has an extraneous attribute, i.e., an attribute that can be removed from the determinant or the dependent without affecting the cover.
  - No functional dependency in F can be derived from the other functional dependencies in F, i.e., F has no redundant dependencies.
  - Every functional dependency in F has a single attribute on the right side, i.e., F is in canonical form.
- A set of functional dependencies can be used to test whether a relation is in a certain normal form, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), or Boyce-Codd normal form (BCNF). These normal forms are defined based on the concepts of keys, superkeys, prime attributes, and non-prime attributes, which are explained below:
  - A superkey of a relation R is a set of attributes that uniquely identifies each tuple in R. For example, {RollNo, Name} is a superkey of Student, since no two students can have the same roll number and name.
  - A key of a relation R is a minimal superkey, i.e., a superkey that has no proper subset that is also a superkey. For example, {RollNo} is a key of Student, since it is a superkey and no subset of it is a superkey.
  - A relation R can have more than one key, in which case they are called candidate keys. For example, {RollNo} and {Name, Branch} are both candidate keys of Student.
  - A prime attribute of a relation R is an attribute that belongs to some key of R. For example, RollNo, Name, and Branch are prime attributes of Student.
  - A non-prime attribute of a relation R is an attribute that does not belong to any key of R. For example, CGPA is a non-prime attribute of Student.
- A relation R is in 1NF if every attribute of R is atomic, i.e., it cannot be further decomposed into smaller values. For example, Student is in 1NF, since all its attributes are atomic.
- A relation R is in 2NF if it is in 1NF and every non-prime attribute of R is fully functionally dependent on every key of R, i.e., it does not depend on a proper subset of any key. For example, Student is in 2NF, since CGPA is fully functionally dependent on {RollNo} and {Name, Branch}, which are the keys of Student.
- A relation R is in 3NF if it is in 2NF and every non-prime attribute of R is non-transitively dependent on every key of R, i.e., it does not depend on another non-prime attribute that depends on a key. For example, Student is in 3NF, since CGPA does not depend on any other non-prime attribute that depends on a key of Student.
- A relation R is in BCNF if it is in 3NF and every determinant of R is a superkey of R, i.e., there is no functional dependency X -> Y where X is not a superkey and Y is a non-prime attribute. For example, Student is in BCNF, since the only determinant of Student is RollNo,



### Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

- Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table such that the value of one attribute determines the value of another attribute.
- There are different levels of normal forms, each with a stricter set of requirements than the previous one. The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF).
- A table is said to be in a certain normal form if it satisfies all the conditions of that normal form and all the previous normal forms. For example, a table is in 3NF if it is in 2NF and also satisfies the 3NF condition.
- The main benefits of normalizing a database are:
  - It eliminates or reduces data duplication, which saves storage space and improves performance.
  - It ensures data consistency and accuracy, which prevents data anomalies and errors.
  - It facilitates data manipulation and querying, which simplifies the database design and maintenance.

- The main drawbacks of normalizing a database are:
  - It may increase the number of tables and joins, which can affect the complexity and efficiency of some queries.
  - It may require more foreign keys and indexes, which can increase the overhead of insert, update, and delete operations.
  - It may not reflect the natural or logical structure of some data domains, which can affect the usability and understandability of the database.

- The following are the definitions and examples of the common normal forms:

  - First normal form (1NF): A table is in 1NF if it does not contain any composite or multi-valued attributes, i.e., each attribute has a single atomic value. For example, a table that stores the name, address, and phone numbers of customers is not in 1NF if the phone number attribute can have multiple values for a customer. To convert it to 1NF, we can either split the phone number attribute into separate attributes for each type of phone number (e.g., home, work, mobile), or create a separate table for phone numbers with a foreign key reference to the customer table.

  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there is no partial dependency. For example, a table that stores the order details of customers is not in 2NF if it has a composite primary key of order ID and product ID, and also has attributes such as customer name, product name, and product price. In this case, the customer name is partially dependent on the order ID, and the product name and price are partially dependent on the product ID. To convert it to 2NF, we can create separate tables for customers, products, and orders, and link them with foreign keys.

  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there is no transitive dependency. For example, a table that stores the order details of customers is not in 3NF if it has attributes such as order ID, customer ID, customer address, product ID, product name, and product price. In this case, the customer address is transitively dependent on the customer ID, and the product name and price are transitively dependent on the product ID. To convert it to 3NF, we can remove the customer address, product name, and product price from the order table, and store them in the customer and product tables respectively.

  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there is no non-trivial functional dependency where the left-hand side is not a superkey. For example, a table that stores the enrollment details of students is not in BCNF if it has attributes such as student ID, course ID, instructor ID, and grade. In this case, the instructor ID determines the course ID, which is a non-trivial functional dependency where the left-hand side is not a superkey. To convert it to BCNF, we can split the table into two tables, one



### Database Design and Normalization Notes

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- The benefits of database normalization are:
  - It improves the clarity and consistency of the data and its relationships.
  - It avoids data anomalies, such as insertion, deletion, and update anomalies, that can cause data inconsistency and corruption.
  - It reduces the storage space and improves the performance of the database system.
  - It makes the database more flexible and adaptable to changing business requirements.
- The process of database normalization involves applying a series of rules or normal forms to a table until it satisfies a certain level of normalization. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values, meaning each cell can hold only one value, and there are no repeating groups of columns.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be determined by a subset of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be determined by another non-key attribute.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies on non-key attributes.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, meaning there are no attributes that depend on a set of values rather than a single value.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and there are no join dependencies, meaning the table cannot be decomposed into smaller tables without losing information.
- To apply the normal forms to a table, the following steps are usually followed:
  - Identify the functional dependencies between the attributes of the table, meaning which attributes determine the values of other attributes.
  - Identify the candidate keys of the table, meaning the minimal set of attributes that can uniquely identify each row of the table.
  - Identify the primary key of the table, meaning the candidate key that is chosen to be the main identifier of the table.
  - Check if the table satisfies the normal form that is desired, and if not, decompose the table into smaller tables that satisfy the normal form and preserve the functional dependencies.
  - Define the referential integrity constraints between the tables, meaning the rules that ensure the consistency of the data across the tables.



### Second

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design and makes it easier to query, update, and maintain the data.
- There are several levels of normalization, each with a specific goal and criteria. The most common levels are:

  - First normal form (1NF): A table is in 1NF if every column contains only atomic values (i.e., values that cannot be further divided) and every row is unique (i.e., no duplicate rows).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key (i.e., no partial dependencies).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key (i.e., no transitive dependencies).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (i.e., a column or a set of columns that determines another column) is a candidate key (i.e., a minimal set of columns that uniquely identifies a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies (i.e., situations where a column or a set of columns can have more than one value for a given primary key value).
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (i.e., situations where a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys without losing any information).

- To normalize a database, one can follow a step-by-step process of applying the normalization rules to each table and checking if it satisfies the desired normal form. If not, the table can be split into smaller tables that meet the criteria. This process can be repeated until the database is fully normalized or until a satisfactory level of normalization is achieved. 
- Normalization has many benefits, such as:

  - Eliminating data anomalies (i.e., inconsistencies or errors that arise when data is inserted, updated, or deleted).
  - Reducing data duplication and storage space.
  - Improving data consistency and accuracy.
  - Enhancing data security and integrity.
  - Facilitating data manipulation and analysis.
  - Increasing query performance and efficiency.

- Normalization also has some drawbacks, such as:

  - Increasing the number of tables and joins, which can make the database more complex and harder to understand.
  - Requiring more processing power and memory, which can affect the system performance and scalability.
  - Introducing data redundancy at the application level, which can require more coding and logic to handle the normalized data.
  - Losing some information or relationships that are not captured by the normal forms, which can limit the flexibility and functionality of the database.

- Therefore, normalization is not a one-size-fits-all solution, but rather a trade-off between the advantages and disadvantages of different levels of normalization. Depending on the requirements and objectives of the database, one may choose to normalize the database to a certain level or to denormalize it (i.e., reverse the normalization process) to achieve a balance between normalization and performance.



### Third Normal Form

- Third normal form (3NF) is a database design principle that aims to reduce data redundancy and improve data integrity.
- A relation is in 3NF if it is in second normal form (2NF) and every non-key attribute is non-transitively dependent on the primary key.
- Non-transitive dependency means that there is no functional dependency between two non-key attributes that is mediated by another non-key attribute.
- For example, consider a relation R(A, B, C, D) with the following functional dependencies: A -> B, B -> C, C -> D. This relation is not in 3NF because C is transitively dependent on A through B, and D is transitively dependent on A through C.
- To convert a relation to 3NF, we need to decompose it into smaller relations that eliminate the transitive dependencies. In this case, we can decompose R into R1(A, B), R2(B, C), and R3(C, D).
- The benefits of 3NF are that it reduces data duplication, avoids update anomalies, and preserves the dependencies in the original relation.



### BCNF

- BCNF stands for **Boyce-Codd Normal Form**     .
- It is an advanced version of **3NF (Third Normal Form)**   .
- A table or a relation is in BCNF if it satisfies two conditions    :
  - It is already in 3NF.
  - For every functional dependency X -> Y, X is either a **super key** or a **candidate key**    .
- A functional dependency X -> Y means that the value of Y is determined by the value of X .
- A super key is a set of attributes that can uniquely identify a tuple in a relation .
- A candidate key is a minimal super key, that is, a super key that does not have any redundant attribute .
- BCNF eliminates the possibility of having **non-trivial functional dependencies** of attributes on anything other than a superset of a candidate key .
- Non-trivial functional dependencies are those that do not follow from the definition of a key.
- BCNF ensures that every attribute in a relation depends only on the key, the whole key, and nothing but the key .
- BCNF is also sometimes referred to as **3.5NF** or **3.5 Normal Form** .

#### Example

- Consider a relation R with five attributes: R(ABCDE).
- The functional dependencies are: FD = {A -> BC, C -> DE).
- The candidate key is: {A}.
- To check if R is in BCNF, we inspect each of the functional dependencies:
  - A -> BC: This satisfies the second condition of BCNF, as A is a candidate key.
  - C -> DE: This violates the second condition of BCNF, as C is not a super key.
- To convert R into BCNF, we decompose it into two relations:
  - R1(ABC) with FD = {A -> BC}.
  - R2(CDE) with FD = {C -> DE}.
- Both R1 and R2 are in BCNF, as they have only one functional dependency each, and the left-hand side is a candidate key.



### Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that states that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but it usually has little influence on how the database is actually designed .
- Inclusion dependency can be expressed as R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ denotes the subset relation  .
- Inclusion dependency can be checked by performing a natural join of R and S on the corresponding columns and comparing the result with R. If the result is equal to R, then the IND holds; otherwise, it is violated.
- Inclusion dependency can be enforced by creating a foreign key constraint on R that references S, or by creating a view that joins R and S and restricting the updates on R to the view.



### Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R  .
- Lossless join decomposition is important for removing redundancy and anomalies from databases while preserving the original data .
- Lossless join decomposition can be verified using the following criteria :
  - Let F be the set of functional dependencies that hold on R, and F+ be the closure of F.
  - Let R1 and R2 be the decomposed relations of R, and R1 ∩ R2 be the set of common attributes between them.
  - The decomposition is lossless if and only if one of the following functional dependencies is in F+:
    - R1 ∩ R2 → R1
    - R1 ∩ R2 → R2
- Lossless join decomposition can also be achieved using decomposition algorithms such as BCNF and 3NF, which are based on the concepts of normal forms and keys.



### Normalization using FD

- Normalization is the process of designing a relational database schema to minimize redundancy and anomalies.
- Functional dependency (FD) is a constraint that describes the relationship between attributes in a relation.
- A FD X -> Y means that the values of Y are determined by the values of X. Two tuples sharing the same values of X will necessarily have the same values of Y.
- A FD is trivial if Y is a subset of X, or full if Y is not a subset of X.
- A FD is called a partial dependency if there is a proper subset of X that can also determine Y.
- A FD is called a transitive dependency if there is an attribute Z that is not part of the candidate key and X -> Z and Z -> Y.
- Normalization uses FDs to decompose a relation into smaller relations that satisfy certain normal forms.
- Normal forms are defined based on the types of FDs that a relation can or cannot have.
- The most common normal forms are:

  - First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. All attributes are atomic.
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and has no partial dependencies.
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and has no transitive dependencies.
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key.

- Normalization can be done by applying a series of decomposition rules based on the FDs of a relation.
- Decomposition rules aim to preserve the information and the dependencies of the original relation.
- Decomposition rules include:

  - Decomposition by projection: Given a relation R and a FD X -> Y, decompose R into two relations R1(X,Y) and R2(X,Z), where Z is the set of attributes of R that are not in X or Y.
  - Decomposition by synthesis: Given a relation R and a set of FDs F, decompose R into a set of relations that are in BCNF and whose FDs are logically implied by F.
  - Decomposition by analysis: Given a relation R and a set of FDs F, decompose R into a set of relations that are in 3NF and whose FDs are logically implied by F.



### MVD

- MVD stands for Multivalued Dependency.
- It is a type of functional dependency that occurs when a relation has more than one multivalued attribute, and the values of one attribute depend on the values of another attribute.
- For example, in a relation R(A, B, C), where A, B, and C are multivalued attributes, an MVD A ->> B means that for each value of A, there is a set of values for B, and this set is independent of the values of C.
- MVDs can cause redundancy and inconsistency in a relation, and they violate the Fourth Normal Form (4NF).
- To eliminate MVDs, we can decompose the relation into two or more relations, such that each relation has only one multivalued attribute, and the MVDs are preserved in the decomposed relations.
- For example, to decompose R(A, B, C) with the MVD A ->> B, we can create two relations R1(A, B) and R2(A, C), and the MVD A ->> B is preserved in R1.



# Unit 3 - Database Design and Normalization

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
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization helps in achieving the following benefits:
  - Improved Database Design: Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.
  - Reduced Data Anomalies: Normalization helps in reducing the data anomalies, such as insertion, update, and deletion anomalies, that may arise due to redundant or dependent data. Data anomalies can lead to data inconsistency, data loss, or data corruption.
  - Enhanced Data Integrity: Normalization helps in enhancing the data integrity, by enforcing the constraints and relationships between the data. Data integrity ensures that the data is valid, accurate, and consistent throughout the database.
  - Optimized Performance: Normalization helps in optimizing the performance of the database, by reducing the size of the data, avoiding unnecessary joins, and facilitating the use of indexes and query optimization techniques.

## Normal Forms
- Normal forms are the rules or standards that define the level of normalization of a database schema. The higher the normal form, the more normalized the schema is.
- There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF). Each normal form has a set of criteria or conditions that must be satisfied by the schema.
- The process of normalization involves applying the normal forms in a sequential order, starting from 1NF and moving up to the highest applicable normal form. Each normal form builds on the previous one, and removes a certain type of redundancy or dependency from the schema.
- The following is a brief overview of the normal forms and their criteria:

  - 1NF: A table is in 1NF if it contains only atomic values, i.e., each cell can hold only one value, and there are no repeating groups or arrays of values within a row or column.
  - 2NF: A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - 3NF: A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - BCNF: A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no non-trivial functional dependencies that violate the key constraint.
  - 4NF: A table is in 4NF if it is in BCNF and has no multi-valued dependencies, i.e., there are no attributes that depend on a set of attributes rather than a single attribute.
  - 5NF: A table is in 5NF if it is in 4NF and has no join dependencies, i.e., there are no subsets of attributes that can be projected out and joined back without loss of information.

## References
: https://www.w3schools.in/DBMS/database-normalization/
[^



### Alternative Approaches to Database Design

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- There are different approaches and techniques for database design, depending on the requirements, preferences, and constraints of the database developers and users.
- Some of the alternative approaches to database design are:

  - **Top-down approach**: This approach starts with identifying the main entities and relationships in the data domain, and then refining them into smaller and more detailed components. This approach is useful for designing databases that have a clear and well-defined scope and purpose, and that need to conform to certain standards and rules.  
  - **Bottom-up approach**: This approach starts with collecting and analyzing the data sources and requirements, and then grouping them into logical and coherent units. This approach is useful for designing databases that have a complex and dynamic data domain, and that need to accommodate diverse and changing needs.  
  - **Normalization**: This is a technique for organizing data in tables in such a way that it reduces data redundancy and dependency. Larger tables are divided into smaller tables and are linked together using relationships. This technique is useful for designing databases that have a high degree of consistency and integrity, and that need to support efficient and accurate queries and updates. 
  - **NoSQL**: This is a term for a class of database systems that do not follow the relational model and do not use SQL as the query language. NoSQL databases store data in different data structures, such as JSON documents, key-value pairs, graphs, or columns. This technique is useful for designing databases that have a large and typically unstructured data domain, and that need to support rapid scalability and flexibility.



## Unit 4 - Transaction Processing Concept

- A transaction is a logical unit of work that accesses and possibly modifies data in a database or a system.
- A transaction processing system (TPS) is a system that supports the execution of transactions in a reliable, efficient and secure manner.
- A transaction has four main properties, also known as ACID properties:
  - Atomicity: A transaction is either executed completely or not at all. If a transaction fails, all the changes made by it are rolled back.
  - Consistency: A transaction preserves the consistency of the database or the system by ensuring that it satisfies all the integrity constraints and business rules.
  - Isolation: A transaction is executed in isolation from other concurrent transactions, meaning that it does not interfere with or see the intermediate results of other transactions.
  - Durability: A transaction ensures that the changes made by it are permanent and will not be lost due to system failures or errors.
- A transaction can have one of the following states:
  - Active: The initial state of a transaction when it starts execution.
  - Partially committed: The state of a transaction when it has executed its final statement but has not yet committed.
  - Committed: The state of a transaction when it has successfully completed and its changes are made permanent.
  - Failed: The state of a transaction when it encounters an error or aborts due to some reason.
  - Aborted: The state of a transaction when it has been rolled back and its changes are undone.
- A transaction manager is a component of a TPS that is responsible for coordinating the execution of transactions and ensuring their ACID properties. It performs the following functions:
  - Scheduling: It decides the order and timing of transactions to be executed.
  - Logging: It records the history of transactions and their changes in a log file for recovery purposes.
  - Concurrency control: It controls the concurrent execution of transactions and prevents conflicts and inconsistencies.
  - Recovery: It restores the database or the system to a consistent state in case of failures or errors.



### Transaction System

A transaction system is a system that processes and records the daily transactions of a business or an organization. A transaction is a single unit of work or logic that involves one or more operations on a database. A transaction system ensures that the transactions are performed in a consistent, reliable, and atomic way, meaning that either all the operations in a transaction are completed successfully or none of them are.

Some examples of transaction systems are:

- CRM (Customer Relationship Management) system: This system manages the interactions and relationships with the customers of a business. It stores information such as customer profiles, contacts, preferences, orders, feedback, etc. A transaction in this system could be adding a new customer, updating an existing customer, or deleting a customer.
- HRM (Human Resources Management) system: This system manages the employees and their activities in an organization. It stores information such as employee details, payroll, benefits, performance, training, etc. A transaction in this system could be hiring a new employee, updating an employee's salary, or terminating an employee.
- ERP (Enterprise Resource Planning) system: This system integrates and coordinates the various functions and processes of an organization. It stores information such as inventory, production, sales, accounting, purchasing, etc. A transaction in this system could be placing an order, manufacturing a product, or issuing an invoice.

A transaction system uses a database management system (DBMS) to store and manipulate the data in the database. A DBMS is a software tool that enables users to access and interact with the underlying data in the database. A DBMS provides features such as data definition, data manipulation, data security, data backup, data recovery, etc.

A transaction system uses a transaction management component of the DBMS to ensure the integrity and consistency of the data in the database. A transaction management component is responsible for:

- Defining the boundaries of a transaction: A transaction begins with a start transaction statement and ends with either a commit or a rollback statement. A commit statement means that the transaction is successful and the changes made by the transaction are permanent. A rollback statement means that the transaction is unsuccessful and the changes made by the transaction are undone.
- Enforcing the ACID properties of a transaction: A transaction must satisfy the following properties to ensure the reliability of the data in the database:
  - Atomicity: A transaction is either fully completed or not completed at all. There is no partial completion of a transaction.
  - Consistency: A transaction preserves the consistency rules of the database, such as integrity constraints, triggers, etc. A transaction does not leave the database in an inconsistent state.
  - Isolation: A transaction is isolated from other concurrent transactions. The intermediate results of a transaction are not visible to other transactions, and the final results of a transaction are only visible after the transaction is committed.
  - Durability: A transaction is durable, meaning that the changes made by a transaction are permanent and will not be lost in case of a system failure or a power outage.
- Handling concurrency and recovery issues: A transaction management component uses various techniques and algorithms to deal with the problems that may arise when multiple transactions are executed simultaneously or when a system failure occurs. Some of these techniques and algorithms are:
  - Locking: A locking mechanism is used to prevent multiple transactions from accessing or modifying the same data item at the same time. A lock is a variable that indicates the status of a data item, such as whether it is available, locked for reading, or locked for writing. A transaction must acquire a lock on a data item before accessing or modifying it, and release the lock after finishing the operation. A locking mechanism ensures the isolation and consistency of transactions, but it may also cause problems such as deadlock, starvation, or reduced performance.
  - Timestamping: A timestamping mechanism is used to order the transactions based on their start time or their commit time. A timestamp is a unique identifier that indicates the time at which a transaction begins or ends. A timestamping mechanism uses the timestamps of transactions to determine whether they can access or modify a data item, and whether they can commit or abort. A timestamping mechanism ensures the serializability of transactions, meaning that the concurrent execution of transactions is equivalent to some serial execution of the same transactions. A timestamping mechanism avoids the problems of locking, but it may also cause problems such as cascading aborts, wasted work, or increased storage requirements.
  - Logging: A logging mechanism is used to record the changes made by transactions to the database. A log is a file that contains the information about the transactions, such as their start time, commit time, rollback time, and the operations they



### Testing of Serializability

- Serializability is the property of a schedule that ensures the consistency of a database.
- A schedule is serializable if it is equivalent to some serial schedule, where transactions are executed one after another without any interleaving of operations.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is based on the order of conflicting operations, such as read-write, write-read, or write-write, on the same data item by different transactions.
- View serializability is based on the read and write operations of each transaction on each data item, regardless of the order of conflicting operations.
- To test for conflict serializability, we can use a precedence graph, which is a directed graph where the nodes are transactions and the edges are conflicts.
- To test for view serializability, we can use a polygraph, which is a directed graph where the nodes are operations and the edges are dependencies.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.
- A schedule is view serializable if and only if its polygraph is acyclic and has a unique sink node for each data item.



### Serializability of Schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- Serializability is a desirable property of a schedule because it ensures that concurrent transactions do not interfere with each other and preserve the consistency and correctness of the database.
- There are two main types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stronger notion of serializability that requires that the order of conflicting operations (read-write, write-read, or write-write) in a schedule is the same as in a serial schedule. Two schedules are conflict equivalent if they have the same order of conflicting operations.
- View serializability is a weaker notion of serializability that requires that the read and write operations of each transaction in a schedule have the same effect as in a serial schedule. Two schedules are view equivalent if they have the same initial read, final write, and read-from relations.
- Conflict serializability can be checked by constructing a precedence graph of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- View serializability can be checked by comparing the read and write operations of each transaction in a schedule with those in a serial schedule. A schedule is view serializable if and only if it is view equivalent to some serial schedule.



### Conflict & View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions, which may lead to inconsistency or anomalies in the database.
- A schedule is serializable if it is equivalent to some serial schedule, meaning that it produces the same final state of the database as the serial schedule.
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
- The schedule S is conflict serializable, as it can be transformed into a serial schedule S' by swapping the non-conflicting operations R(B) and W(B) of T1 with R(B) and W(B) of T2.

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
|     | R(B) |
|     | W(B) |

- The schedule S' is serial, as it executes T1 followed by T2, and produces the same final state of the database as S.

#### View Serializability

- A schedule is view serializable if it is view equivalent to some serial schedule, meaning that it preserves the same read-write dependencies as the serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item.
  - They have the same final write operations on each data item.
  - They have the same update operations on each data item, meaning that if a transaction T reads the value of a data item A written by another transaction U in one schedule, then T must also read the value of A written by U in the other schedule.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(A) |
|     | W(A) |
| R(B) |    |
| W(B) |    |

- The schedule S is not serial, as it interleaves operations from T1 and T2.
- The schedule S is view serializable, as it is view equivalent to a serial schedule S' that executes T2 followed by T1.

| T1 | T2 |
|----|----|
|     | R(A) |
|     | W(A) |
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |

- The schedule S' is serial, as it executes T2 followed by T1, and preserves the same read-write dependencies as S.



### Recoverability for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- Recoverability is the property of a schedule that ensures that the database can be restored to a consistent state after a transaction failure or system crash .
- A schedule is a sequence of operations performed by one or more transactions on the database.
- A transaction is a logical unit of work that accesses and possibly modifies the contents of a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that the transaction preserves the internal consistency of the database.
- Isolation means that the execution of a transaction does not interfere with the execution of other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failure.
- A transaction can be in one of the following states: active, partially committed, committed, failed, or aborted.
- Active is the initial state of a transaction, where it is executing its operations.
- Partially committed is the state of a transaction after it has executed its final operation, but before it has committed.
- Committed is the state of a transaction after it has successfully completed and its effects are recorded in the database.
- Failed is the state of a transaction after it has encountered an error that prevents it from continuing its execution.
- Aborted is the state of a transaction after it has been rolled back and its effects are undone from the database.
- A transaction can be aborted either by the system (due to a hardware failure, system crash, or deadlock) or by the user (due to a logical error or cancellation).
- A schedule is recoverable if it ensures that no transaction commits before all the transactions whose changes it has read commit.
- A schedule is irrecoverable if it allows a transaction to commit before some transaction whose changes it has read commits or aborts.
- An irrecoverable schedule can lead to a cascading rollback, where the abort of one transaction causes the abort of other transactions that have read its changes.
- A schedule is cascadeless if it ensures that no transaction reads a data item until the last transaction that has written it commits.
- A cascadeless schedule avoids the problem of cascading rollback and reduces the amount of undo work.
- A schedule is strict if it ensures that no transaction reads or writes a data item until the last transaction that has written it commits.
- A strict schedule is also cascadeless, but it is more restrictive than a cascadeless schedule.
- A strict schedule is desirable for recovery purposes, as it simplifies the undo and redo operations.
- A schedule can be classified into one of the following types, based on its recoverability property:
  - Irrecoverable: A schedule that is not recoverable.
  - Recoverable: A schedule that is recoverable but not cascadeless.
  - Cascadeless: A schedule that is cascadeless but not strict.
  - Strict: A schedule that is strict.
- Example: Consider the following schedule of two transactions T1 and T2, where R(x) denotes reading data item x, W(x) denotes writing data item x, and C denotes commit:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|    | R(A) |
|    | W(A) |
| C  |    |
|    | C  |

- This schedule is irrecoverable, as T2 commits after reading the uncommitted change of T1. If T1 aborts after T2 commits, the database will be inconsistent.
- To make this schedule recoverable, T2 should not commit before T1 commits. For example, the following schedule is recoverable:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|    | R(A) |
|    | W(A) |
|    | C  |
| C  |    |

- To make this schedule cascadeless, T2 should not read A until T1 commits. For example, the following schedule is cascadeless:



### Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations on the database.
- A transaction failure can be caused by various reasons, such as user errors, system errors, concurrency control violations, or hardware failures.
- To recover from transaction failures, the database management system (DBMS) must ensure the atomicity and durability of transactions, which are two of the ACID properties of transactions.
- Atomicity means that either all the operations of a transaction are executed or none. Durability means that the effects of a committed transaction are permanent and not lost due to any failure.
- There are three main techniques for recovery from transaction failures in DBMS: logging, checkpointing, and shadow paging.

#### Logging

- Logging is a technique that records the changes made by transactions to the database in a separate file called the log or the journal.
- The log contains information such as the transaction id, the operation performed, the old value and the new value of the data item, and the commit or abort status of the transaction.
- The log is used to undo or redo the operations of transactions in case of a failure, depending on whether the transaction was committed or aborted before the failure.
- There are two types of logging: undo logging and redo logging.
- Undo logging is a technique that uses the log to undo the effects of uncommitted transactions after a failure. It restores the old values of the data items that were modified by the uncommitted transactions.
- Redo logging is a technique that uses the log to redo the effects of committed transactions after a failure. It applies the new values of the data items that were modified by the committed transactions.
- A combination of undo and redo logging is also possible, which is called undo/redo logging.

#### Checkpointing

- Checkpointing is a technique that periodically writes the contents of the main memory buffers to the disk, and records a special entry called the checkpoint in the log.
- The checkpoint entry indicates the point in time when the DBMS was in a consistent state, and all the transactions before the checkpoint were committed and their effects were written to the disk.
- The checkpointing technique reduces the amount of work that the DBMS has to do for recovery after a failure, as it only has to consider the transactions that occurred after the checkpoint.
- There are two types of checkpointing: fuzzy checkpointing and synchronous checkpointing.
- Fuzzy checkpointing is a technique that allows the DBMS to continue processing transactions while performing the checkpointing operation. It does not require the DBMS to flush all the buffers to the disk at once, but rather in batches.
- Synchronous checkpointing is a technique that requires the DBMS to stop processing transactions while performing the checkpointing operation. It ensures that all the buffers are flushed to the disk at once, and no transaction is active during the checkpoint.

#### Shadow Paging

- Shadow paging is a technique that uses a separate file or page table to keep track of the changes made by transactions to the database.
- The shadow page table contains the addresses of the original pages of the database, which are not modified by the transactions. The current page table contains the addresses of the modified pages of the database, which are stored in a different location on the disk.
- The shadow page table is never updated by the transactions, but only by the DBMS when a transaction commits. The current page table is updated by the transactions as they modify the database.
- The shadow paging technique does not require logging or checkpointing, as it can recover from a failure by simply discarding the current page table and using the shadow page table to access the database.
- However, the shadow paging technique has some disadvantages, such as the overhead of maintaining two page tables, the difficulty of handling concurrent transactions, and the waste of disk space due to the duplication of pages.



### Log Based Recovery in DBMS

- Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A transaction log contains the following information for each transaction  :
  - Transaction ID: a unique identifier for the transaction
  - Operation: the type of operation performed by the transaction, such as read, write, commit, abort, etc.
  - Data item: the name of the data item affected by the operation
  - Old value: the value of the data item before the operation
  - New value: the value of the data item after the operation
- A log file is maintained in some stable storage device, such as a disk or a tape, so that it can be accessed even if the main memory is lost  .
- The process of storing the logs should be done before the actual changes are made to the database, to ensure that the logs reflect the correct sequence of operations.
- Log based recovery can be classified into two types: undo logging and redo logging.
  - Undo logging: this type of logging records the old values of the data items before the changes are made by the transactions. It is used to undo the effects of the transactions that are not committed at the time of failure, by restoring the old values to the database.
  - Redo logging: this type of logging records the new values of the data items after the changes are made by the transactions. It is used to redo the effects of the transactions that are committed at the time of failure, by applying the new values to the database.
- Log based recovery can also be combined to form undo/redo logging, which records both the old and the new values of the data items. It is used to undo the effects of the uncommitted transactions and redo the effects of the committed transactions at the time of failure.
- Log based recovery can be implemented using various algorithms, such as immediate update, deferred update, checkpointing, fuzzy checkpointing, etc. These algorithms differ in the way they write the logs and the changes to the database, and the way they handle the recovery process.



### Checkpoints for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A transaction is a logical unit of work that represents a real-world event of data processing.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either executes all or none of its operations.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it is the only one in the system, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.
- A transaction can have one of the following states: active, partially committed, committed, failed, or aborted.
- A transaction begins in the active state, where it executes its operations.
- A transaction enters the partially committed state when it executes its final operation.
- A transaction enters the committed state when it successfully completes and its changes are recorded in the database.
- A transaction enters the failed state when it encounters an error or aborts due to some reason.
- A transaction enters the aborted state when it is rolled back and its changes are undone from the database.
- A transaction can be aborted by the user, the system, or the concurrency control mechanism.
- A transaction can be rolled back by using undo and redo operations, which are based on the transaction log.
- A transaction log is a file that records all the changes made by transactions to the database.
- A transaction log entry contains the transaction id, the data item, the old value, and the new value.
- An undo operation restores the old value of a data item from the log.
- A redo operation applies the new value of a data item from the log.
- A checkpoint is a point in time when the database and the transaction log are synchronized.
- A checkpoint ensures that all the committed transactions are written to the database and all the active transactions are written to the log.
- A checkpoint reduces the recovery time in case of a system failure, as only the transactions after the checkpoint need to be considered.
- A checkpoint can be performed periodically, or triggered by some events, such as the log size reaching a limit, or the system shutting down.



### Deadlock Handling

- A deadlock is an unwanted situation in which two or more transactions are waiting indefinitely for each other to release locks on shared resources   .
- A deadlock can occur in both centralized and distributed database systems, but the latter has some additional challenges such as transaction location and transaction control.
- There are three classical approaches for deadlock handling, namely   :
  - Deadlock prevention: This approach ensures that a deadlock can never occur by imposing some constraints on the transactions, such as ordering the resources, avoiding hold and wait, or using timeouts. However, this approach may reduce concurrency and increase overhead.
  - Deadlock avoidance: This approach allows a deadlock to occur, but avoids it by using some information about the resource requirements of the transactions, such as the number and type of resources needed. A common technique is to use a banker's algorithm, which grants a request only if it does not lead to an unsafe state. However, this approach may require accurate and complete information, which may not be available or feasible in some cases.
  - Deadlock detection and removal: This approach allows a deadlock to occur, but detects it by using some mechanism, such as a wait-for graph or a timeout. Once a deadlock is detected, it is removed by aborting or rolling back some or all of the transactions involved in the deadlock. However, this approach may incur a high cost of detection and recovery, and may affect the performance and reliability of the system.
- The choice of the deadlock handling approach depends on several factors, such as the frequency and severity of deadlocks, the availability and accuracy of information, the overhead and complexity of the mechanism, and the impact on the system performance and throughput    .



### Distributed Database for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A distributed database is a collection of databases that are physically distributed over different locations and connected by a network.
- A distributed transaction is a database transaction that involves two or more network hosts, each providing transactional resources such as data, locks, or logs.
- A transaction manager is responsible for creating and managing a global transaction that encompasses all operations against such resources.
- A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that the transaction preserves the integrity constraints of the database.
- Isolation means that the transaction does not interfere with other concurrent transactions.
- Durability means that the effects of the transaction are permanent and survive failures.
- A distributed transaction can be executed using a two-phase commit protocol, which consists of two phases: prepare and commit.
- In the prepare phase, the transaction manager asks each participant to vote on whether to commit or abort the transaction, based on their local operations and resources.
- In the commit phase, the transaction manager decides whether to commit or abort the transaction, based on the votes received from the participants, and informs them of the decision.
- A transaction becomes in-doubt if the two-phase commit protocol fails, due to network or system failures, and the transaction manager or some participants do not know the final outcome of the transaction.
- An in-doubt transaction must be resolved by either committing or aborting it, based on the available information and recovery mechanisms.



### Distributed Data Storage for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A distributed database is a database that is stored across multiple computers or sites that are connected by a network .
- A distributed database management system (DDBMS) is a centralized software system that manages a distributed database in a manner as if it were all stored in a single location .
- A distributed database incorporates transaction processing, which is a program including a collection of one or more database operations.
- Transaction processing is an atomic process that is either entirely executed or not at all.
- In a distributed database system, transaction processing can be challenging because of the following issues:
  - Concurrency control: ensuring that concurrent transactions do not interfere with each other and maintain data consistency.
  - Distributed commit: ensuring that a transaction that spans multiple sites is either committed or aborted at all sites.
  - Failure recovery: ensuring that the system can recover from partial or total failures of sites or network links.
  - Data replication: ensuring that copies of data at different sites are consistent and up-to-date.
- To address these issues, distributed database systems use various techniques, such as:
  - Two-phase locking: a protocol that acquires and releases locks on data items to prevent conflicts among concurrent transactions.
  - Two-phase commit: a protocol that coordinates the commit or abort decision of a distributed transaction among all the sites involved.
  - Distributed snapshots: a method of capturing the global state of a distributed system at a certain point in time.
  - Quorum consensus: a method of ensuring data consistency among replicated copies by requiring a minimum number of sites to agree on a data value.
  - Timestamp ordering: a method of ordering transactions based on their logical timestamps to ensure serializability.



### Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system . Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

Some of the reasons for using concurrency control methods in DBMS are:

- To apply isolation through mutual exclusion between conflicting transactions
- To resolve read-write and write-write conflict issues
- To preserve database consistency through constantly preserving execution obstructions
- To improve the performance and throughput of the system by allowing concurrent access

Some of the common concurrency control methods in DBMS are :

- Lock-based protocols: These protocols use locks to prevent multiple transactions from accessing the same data item at the same time. Locks can be shared or exclusive, and can be granted or denied based on the compatibility matrix. Locks can also be applied at different levels of granularity, such as table, page, or record. Lock-based protocols ensure serializability, but may cause problems such as deadlock, starvation, or cascading rollback.
- Timestamp-based protocols: These protocols use timestamps to order the transactions and determine their precedence. Each transaction is assigned a unique timestamp when it enters the system, and each data item has a read timestamp and a write timestamp to record the last transaction that accessed it. Timestamp-based protocols use validation rules to check if a transaction can read or write a data item without violating serializability. Timestamp-based protocols avoid deadlock, but may cause more aborts and waste of resources.
- Validation-based protocols: These protocols divide the execution of a transaction into three phases: read phase, validation phase, and write phase. In the read phase, the transaction reads the data items from the database and stores them in a local buffer. In the validation phase, the transaction checks if it can commit without violating serializability, using some validation tests. In the write phase, the transaction writes the updated data items to the database. Validation-based protocols avoid deadlock and cascading rollback, but may have high overhead and concurrency issues.
- Multiversion protocols: These protocols allow multiple versions of the same data item to coexist in the database, and assign different versions to different transactions based on some criteria. Multiversion protocols can be based on locks, timestamps, or validation, and can improve the concurrency and availability of the system. However, multiversion protocols may require more storage space and maintenance for the versions, and may have complexity and consistency issues.



### Directory System for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A directory system is a way of organizing and accessing the notes of a unit in a subject.
- A directory system can have different levels of hierarchy, such as folders, subfolders, files, etc.
- A directory system can have different naming conventions, such as alphanumeric, descriptive, etc.
- A directory system can have different attributes, such as size, date, type, etc.
- A directory system can have different operations, such as create, delete, rename, move, copy, etc.
- A directory system can have different permissions, such as read, write, execute, etc.
- A directory system can have different types, such as local, network, distributed, etc.

- A possible directory system for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System is:

```
DBMS
└── Unit 4 - Transaction Processing Concept
    ├── Introduction.md
    ├── Transaction Properties.md
    ├── Transaction States.md
    ├── Concurrency Control.md
    │   ├── Locking Techniques.md
    │   ├── Timestamp Ordering.md
    │   └── Multiversion Concurrency Control.md
    ├── Serializability.md
    ├── Recoverability.md
    ├── Recovery Techniques.md
    │   ├── Log-based Recovery.md
    │   ├── Shadow Paging.md
    │   └── Checkpoints.md
    └── Deadlock.md
        ├── Deadlock Prevention.md
        ├── Deadlock Avoidance.md
        ├── Deadlock Detection.md
        └── Deadlock Recovery.md
```



## Unit 5 - Concurrency Control Techniques

- Concurrency control techniques are methods to ensure the correctness and consistency of data in a database system when multiple transactions are executed concurrently.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by the transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them by validating the transactions before committing them. Examples of optimistic techniques are validation-based protocols, multiversion concurrency control, and snapshot isolation.
- Concurrency control techniques can also be classified based on the level of granularity of the data items that are locked or validated. The level of granularity can range from the entire database to a single record or field. The trade-off between the level of granularity and the performance of the system depends on the degree of contention and the overhead of locking or validation.
- Concurrency control techniques can also be classified based on the type of conflicts that they handle. The type of conflicts can be read-write, write-write, or write-read. Different techniques may have different rules for handling different types of conflicts. For example, two-phase locking handles read-write and write-write conflicts by using shared and exclusive locks, while timestamp ordering handles write-read conflicts by using wait-die and wound-wait schemes.



### Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system . Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

The main objectives of concurrency control are:

- To apply isolation through mutual exclusion between conflicting transactions
- To resolve read-write and write-write conflict issues
- To preserve database consistency through constantly preserving execution obstructions
- To ensure serializability and recoverability of transactions

The main techniques of concurrency control are :

- Lock-based protocols: These protocols use locks to prevent multiple transactions from accessing the same data item at the same time. Locks can be shared or exclusive, and can be granted or denied by a lock manager. Locks can also be classified into binary, multiple, or tree-structured locks.
- Timestamp-based protocols: These protocols use timestamps to order the transactions and determine their precedence. Timestamps can be either logical or physical, and can be assigned either at the beginning or at the end of a transaction. Timestamps can also be used to implement optimistic or pessimistic concurrency control.
- Validation-based protocols: These protocols use a validation phase to check whether a transaction can be committed or aborted. Validation can be done either before, during, or after the execution phase of a transaction. Validation can also be based on serializability graphs or certification tests.
- Multiversion protocols: These protocols use multiple versions of data items to allow concurrent read operations without locking. Each version of a data item has a read timestamp and a write timestamp, and a transaction can read the latest version that is compatible with its timestamp. Multiversion protocols can also use locks or timestamps to control write operations.



### Locking Techniques for Concurrency Control

- Locking is a mechanism to enforce mutual exclusion and prevent data inconsistency in concurrent transactions.
- A lock is a variable associated with a data item that describes the status of the item with respect to possible operations that can be applied to it.
- Generally, there are two types of locks: binary locks and shared/exclusive locks.
- Binary locks have two states: locked and unlocked. A transaction can lock a data item before accessing it and unlock it after finishing. Only one transaction can hold a lock on a data item at a time.
- Shared/exclusive locks have three states: unlocked, shared, and exclusive. A transaction can lock a data item in shared mode or exclusive mode. Multiple transactions can hold shared locks on the same data item, but only one transaction can hold an exclusive lock. A transaction needs an exclusive lock to write a data item and a shared lock to read it.
- A locking protocol is a set of rules that govern when and how transactions acquire and release locks. A locking protocol should ensure serializability and avoid deadlock.
- Some common locking protocols are:
  - Two-phase locking (2PL): A transaction must obtain all the locks it needs before it releases any lock. It has two phases: growing phase and shrinking phase. In the growing phase, the transaction can only acquire locks. In the shrinking phase, the transaction can only release locks. 2PL ensures serializability but may cause deadlock.
  - Strict two-phase locking (Strict 2PL): A transaction must hold all its exclusive locks until it commits or aborts. It is a variation of 2PL that ensures recoverability and cascadelessness in addition to serializability. It may also cause deadlock.
  - Conservative two-phase locking (Conservative 2PL): A transaction must obtain all the locks it needs before it starts execution. It is also called static or pre-claiming 2PL. It prevents deadlock but may cause unnecessary blocking and low concurrency.
  - Timestamp ordering: A transaction is assigned a unique timestamp when it starts. The timestamp determines the serial order of transactions. A transaction can access a data item only if its timestamp is higher than the timestamp of the last transaction that accessed the same item. Otherwise, the transaction is aborted and restarted with a new timestamp. Timestamp ordering ensures serializability and avoids deadlock, but may cause high abort rate and starvation.



### Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of concurrency control methods that do not use locks to ensure serializability of transactions   .
- Time stamping protocols assign a unique timestamp to each transaction when it is created, which represents its logical start time   .
- The timestamp can be either the system time or a logical counter that increments with each transaction .
- The timestamp ordering protocol ensures that any conflicting read and write operations are executed in timestamp order, meaning that older transactions get priority over newer ones   .
- The timestamp ordering protocol can be implemented using two methods: basic timestamp ordering and Thomas' write rule  .
- Basic timestamp ordering checks the timestamp of each transaction against the read timestamp (RTS) and write timestamp (WTS) of the data item it accesses, and rejects the operation if it violates the timestamp order  .
- Thomas' write rule is a variation of basic timestamp ordering that allows some write operations to be ignored instead of rejected, if they do not affect the final outcome of the schedule  .
- The advantages of timestamp ordering protocol are that it avoids deadlock, reduces locking overhead, and preserves causality among transactions  .
- The disadvantages of timestamp ordering protocol are that it may cause more aborts, waste resources, and suffer from the problem of starvation  .
- Time stamping protocols are suitable for applications that have low data contention and high read frequency .



### Validation Based Protocol

- Validation based protocol is a type of concurrency control technique that works on the validation rules and time-stamps .
- It is also known as optimistic concurrency control technique because it assumes that very less interference occurs, therefore, there is no need for checking while the transaction is executing .
- The protocol consists of three phases for managing concurrent transactions: read phase, validation phase, and write phase  .
- In the read phase, the transaction can read data values from the database but the write operation or updates are only applied to the local data copies, not the actual database.
- In the validation phase, the transaction is checked for serializability using certain validation rules based on the time-stamps of the transactions  .
- In the write phase, the transaction can write the updated values to the database if it passes the validation phase, otherwise it is aborted and restarted  .
- The validation based protocol avoids locking and ensures serializability, but it may cause more aborts and restarts than other concurrency control techniques .




### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows a tree structure to represent the hierarchy of data items. The root node represents the entire database, and the leaf nodes represent the smallest data items. The intermediate nodes represent the data items of different sizes.
- Multiple granularity locking protocol follows some rules to ensure serializability and avoid deadlock:
  - Follow multi-granularity compatibility function
  - Lock root of tree first, any mode
  - Node Q can be locked by Ti in S or IS only if parent(Q) locked by Ti in IX or IS
  - Node Q can be locked by Ti in X, SIX, IX only if parent(Q) locked by Ti in IX, SIX
  - Ti is two-phase
  - Ti can unlock node Q only if none of Q’s descendants are locked by Ti
- Multiple granularity locking protocol uses the following lock modes:
  - S (Shared): Allows read access to the data item
  - X (Exclusive): Allows read and write access to the data item
  - IS (Intention Shared): Indicates the intention to lock some descendant node in S mode
  - IX (Intention Exclusive): Indicates the intention to lock some descendant node in X mode
  - SIX (Shared Intention Exclusive): Indicates the intention to lock some descendant node in X mode and also allows read access to the current node



### Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data items to coexist in the database.
- The main idea is to grant an appropriate version of a data item to each read request, while write requests operate on a copy of the data item, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data item from other transactions.
- The benefits of multi version schemes are increased concurrency, reduced locking overhead, and improved performance.
- The challenges of multi version schemes are maintaining consistency, avoiding conflicts, and managing storage space for multiple versions.
- There are different types of multi version schemes, such as timestamp-based, validation-based, and snapshot-based, that use different criteria to determine which version of a data item to read or write.
- Timestamp-based schemes assign a unique timestamp to each transaction and each version of a data item, and use the timestamps to order the transactions and the versions.
- Validation-based schemes allow transactions to read and write any version of a data item, but validate the transactions at commit time to ensure serializability.
- Snapshot-based schemes create a snapshot of the database for each transaction, and allow transactions to read and write only the versions of the data items in their snapshot.



### Recovery with Concurrent Transactions

Recovery with concurrent transactions is the process of restoring the database to a consistent state after a failure, while ensuring the ACID properties of transactions. Recovery with concurrent transactions can be done in the following four ways:

- **Interaction with concurrency control**: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if locking is used for concurrency control, then the recovery scheme must ensure that the locks are released after a transaction commits or aborts. Similarly, if timestamp ordering is used for concurrency control, then the recovery scheme must ensure that the timestamps are assigned correctly and consistently.
- **Transaction rollback**: In this scheme, the recovery scheme can undo the effects of a transaction that has failed or aborted, by using the log records. The log records contain the information about the changes made by the transaction, such as the old and new values of the data items. The recovery scheme can use the log records to restore the old values of the data items that were modified by the transaction, and discard the new values. This process is called transaction rollback or undo.
- **Checkpoints**: In this scheme, the recovery scheme can reduce the amount of work needed to recover from a failure, by periodically taking a snapshot of the database and the log records. This snapshot is called a checkpoint, and it marks a point in time when the database is in a consistent state. The recovery scheme can use the checkpoint to determine the starting point for recovery, and ignore the log records that were generated before the checkpoint. This process is called checkpointing or partial rollback.
- **Restart recovery**: In this scheme, the recovery scheme can handle the situation when the system crashes during the recovery process itself. The recovery scheme can use a special log record called restart record, which indicates the point in time when the recovery process started. The recovery scheme can use the restart record to resume the recovery process from where it left off, and avoid repeating the same work. This process is called restart recovery or redo.



### Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Oracle is a relational database management system that supports concurrent access of data by multiple users and transactions.
- Oracle uses a multiversion concurrency control (MVCC) model to provide read consistency and isolation levels for queries and transactions.
- Oracle also uses various types of locks to ensure data integrity and prevent conflicts among concurrent updates of the same data.
- Some of the concurrency control techniques used by Oracle are:

  - Statement-level read consistency: Oracle ensures that each query sees a consistent view of the data as of the time the query started, regardless of any changes made by other transactions. Oracle achieves this by using undo segments to store the before-images of the data and applying them to the current data when necessary.
  - Transaction-level read consistency: Oracle can also provide a consistent view of the data for all the queries in a transaction, as of the time the transaction started. This is achieved by setting the isolation level of the transaction to SERIALIZABLE or READ ONLY, which prevents the transaction from seeing any changes made by other transactions after the transaction began.
  - Oracle isolation levels: Oracle supports four isolation levels for transactions: READ COMMITTED, SERIALIZABLE, READ ONLY, and RESUMABLE. Each isolation level determines the degree of concurrency and consistency that a transaction can have with other transactions. For example, READ COMMITTED is the default isolation level, which allows a transaction to see the changes made by other transactions that have committed, but not the changes made by uncommitted transactions. SERIALIZABLE is the highest isolation level, which ensures that a transaction sees a snapshot of the data as of the time the transaction started, and prevents any conflicts or anomalies that could occur due to concurrent transactions.
  - Oracle locks: Oracle uses different types of locks to protect data from concurrent modifications and ensure data integrity. Some of the locks used by Oracle are:

    - Data locks: These are locks that are acquired on data blocks or rows when a transaction modifies or queries the data. Data locks can be exclusive or shared, depending on the type of operation performed by the transaction. Exclusive locks prevent other transactions from modifying or querying the same data, while shared locks allow other transactions to query the same data, but not modify it.
    - Latch locks: These are lightweight locks that are used to protect the internal structures and memory areas of the Oracle database, such as the buffer cache, the redo log buffer, the data dictionary cache, etc. Latch locks are acquired and released quickly, and do not cause any blocking or waiting among transactions.
    - Enqueue locks: These are locks that are used to serialize access to database resources that are not protected by data locks or latch locks, such as tablespaces, rollback segments, sequences, etc. Enqueue locks are acquired and released by the lock manager, and can cause blocking or waiting among transactions if the requested resource is unavailable.

