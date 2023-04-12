

## Unit 1 - Introduction

- This unit introduces the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be divided into two main branches: symbolic AI and sub-symbolic AI.
- Symbolic AI uses logic, rules, and symbols to represent and manipulate knowledge. Examples of symbolic AI include expert systems, knowledge bases, and logic programming.
- Sub-symbolic AI uses numerical and statistical methods to model and learn from data. Examples of sub-symbolic AI include neural networks, evolutionary algorithms, and reinforcement learning.
- AI can also be classified according to the type and complexity of the problem it solves. Some common types of AI problems are:
  - Search: finding a solution or a path from a given state to a goal state, such as in chess or navigation.
  - Planning: generating and executing a sequence of actions to achieve a goal, such as in robotics or scheduling.
  - Constraint satisfaction: finding values for a set of variables that satisfy a set of constraints, such as in sudoku or timetabling.
  - Optimization: finding the best or optimal solution among a set of possible solutions, such as in traveling salesman or portfolio selection.
  - Classification: assigning a label or a category to an input, such as in spam detection or face recognition.
  - Regression: predicting a numerical value for an input, such as in stock price prediction or weather forecasting.
  - Clustering: grouping similar inputs together, such as in customer segmentation or image segmentation.
  - Natural language processing: understanding and generating natural language, such as in machine translation or chatbots.
  - Computer vision: processing and interpreting visual information, such as in face detection or object recognition.
  - Speech recognition: converting speech signals into text, such as in voice assistants or dictation software.
  - Speech synthesis: converting text into speech signals, such as in text-to-speech or voice feedback.
  - Machine learning: the subfield of AI that focuses on creating systems that can learn from data and improve their performance over time, such as in neural networks or reinforcement learning.
- AI systems can be evaluated according to various criteria, such as:
  - Accuracy: how well the system performs the task or produces the correct output.
  - Efficiency: how fast or how much resources the system uses to perform the task or produce the output.
  - Robustness: how well the system handles errors, uncertainties, or changes in the input or the environment.
  - Explainability: how well the system can provide reasons or justifications for its actions or outputs.
  - Ethicality: how well the system respects the moral values and principles of humans and society, such as fairness, privacy, or safety.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of ### Overview for the notes of the Unit 1 - Introduction in the subject of Database Management System. Here is the content I have written:

# Overview for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A database is a collection of related data that can be stored, manipulated, and retrieved by a software system.
- A database management system (DBMS) is a software system that provides the functionality to create, maintain, and query databases.
- A DBMS consists of three components: data, data model, and database language.
- Data is the raw information that is stored in the database, such as numbers, text, images, etc.
- Data model is the logical structure and organization of the data, such as tables, records, fields, etc.
- Database language is the set of commands and syntax that allows the users and applications to interact with the database, such as SQL, DDL, DML, etc.
- A DBMS can be classified into different types based on the data model, such as relational, hierarchical, network, object-oriented, etc.
- A DBMS can also be classified into different types based on the level of abstraction, such as conceptual, physical, and external.
- A DBMS can provide various benefits, such as data independence, data integrity, data security, data consistency, data sharing, data recovery, etc.
- A DBMS can also pose various challenges, such as data complexity, data redundancy, data inconsistency, data isolation, data concurrency, data privacy, etc.
- A DBMS can be used for various applications, such as banking, e-commerce, social media, education, health care, etc.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of Database System vs File System for the Unit 1 - Introduction in the subject of Database Management System.

# Database System vs File System

- A file system is a collection of files and folders that are stored on a disk or other storage device. A file system organizes data in a hierarchical structure, where each file or folder has a name and a path. A file system can store any type of data, such as text, images, audio, video, etc.
- A database system is a software application that manages a collection of data that are organized in a logical and structured way. A database system provides a way to store, retrieve, update, and manipulate data using a query language, such as SQL. A database system can store data in various formats, such as tables, graphs, documents, etc.
- The main differences between a file system and a database system are:

  - A file system does not have a schema, which means that the structure and meaning of the data are not defined. A database system has a schema, which means that the data are described by a set of rules and constraints that specify the data types, relationships, and integrity.
  - A file system does not have a query language, which means that the data can only be accessed by specifying the file name and path. A database system has a query language, which means that the data can be accessed by specifying the conditions and criteria that the data must satisfy.
  - A file system does not have concurrency control, which means that the data can be corrupted or inconsistent if multiple users or processes access or modify the same file at the same time. A database system has concurrency control, which means that the data are protected and synchronized by using locking mechanisms and transaction management.
  - A file system does not have backup and recovery, which means that the data can be lost or damaged if the file system crashes or fails. A database system has backup and recovery, which means that the data can be restored and recovered by using backup files and logs.



# Database System Concept and Architecture

- A database system is a collection of software components that manage the storage, retrieval, and manipulation of data in a structured and organized way.
- A database system consists of three main components: the data, the database management system (DBMS), and the database applications.
- The data is the actual information stored in the database, such as tables, records, fields, values, etc.
- The DBMS is the software that provides the functionality to create, maintain, and access the database. It also enforces the rules and constraints that ensure the integrity, security, and consistency of the data.
- The database applications are the programs that interact with the DBMS and the data to perform specific tasks, such as querying, updating, reporting, analyzing, etc.
- The architecture of a database system refers to the way the components are organized and communicate with each other. It also defines the levels of abstraction and the interfaces that separate the components and hide the implementation details.
- There are different types of database system architectures, such as centralized, decentralized, hierarchical, single-tier, multi-tier, client-server, parallel, distributed, etc. Each type has its own advantages and disadvantages depending on the requirements and constraints of the system.
- A common way to describe the architecture of a database system is to use the ANSI/SPARC three-schema architecture, which consists of three levels of schemas: the external schema, the conceptual schema, and the internal schema.
- The external schema defines the views of the data for different users or applications. It allows each user or application to see only the relevant and authorized part of the data, and to use their own names and formats for the data elements.
- The conceptual schema defines the logical structure and organization of the data for the entire database. It describes the entities, attributes, relationships, constraints, and operations on the data, without specifying how they are stored or implemented.
- The internal schema defines the physical structure and storage of the data on the computer system. It describes how the data is organized in files, records, blocks, indexes, etc., and how they are accessed and manipulated by the DBMS.
- The three-schema architecture provides data independence, which is the ability to change one level of schema without affecting the other levels. There are two types of data independence: logical data independence and physical data independence.
- Logical data independence is the ability to change the conceptual schema without affecting the external schemas. It allows the DBMS to support different views of the data for different users or applications, and to modify the logical structure of the data without affecting the existing views.
- Physical data independence is the ability to change the internal schema without affecting the conceptual schema. It allows the DBMS to optimize the physical storage and access of the data without affecting the logical structure of the data.



# Data Model Schema and Instances

- A data model is a collection of concepts and rules for describing the structure, meaning, and constraints of the data stored in a database.
- A schema is the formal description of the structure and organization of the data in a database. It defines the tables, columns, keys, relationships, and constraints of the data.
- An instance is the set of data stored in a database at a particular moment of time. It represents the current state and values of the data.
- A schema is static and does not change frequently, whereas an instance is dynamic and changes constantly as the data is inserted, updated, or deleted.
- A schema can be represented by a diagram or a text, whereas an instance can be represented by a table or a record.
- A schema can be of three types: logical, physical, and view. A logical schema describes the data in terms of its entities, attributes, and relationships. A physical schema describes how the data is stored and accessed in the database system. A view schema describes a subset or a projection of the data for a specific purpose or user.
- An example of a schema and an instance for a student database is shown below:

Logical schema:

Student (StudentID, Name, Major, GPA)
Course (CourseID, Title, Credits)
Enroll (StudentID, CourseID, Grade)

Physical schema:

Student: stored in a file named student.dat, with fixed-length records of 50 bytes each, and StudentID as the primary key.
Course: stored in a file named course.dat, with variable-length records of up to 100 bytes each, and CourseID as the primary key.
Enroll: stored in a file named enroll.dat, with fixed-length records of 20 bytes each, and (StudentID, CourseID) as the primary key.

View schema:

StudentView: a view of the Student table that shows only the Name and GPA of the students.
CourseView: a view of the Course table that shows only the Title and Credits of the courses.

Instance:

Student:

| StudentID | Name | Major | GPA |
|-----------|------|-------|-----|
| 1001 | Alice | CS | 3.8 |
| 1002 | Bob | Math | 3.5 |
| 1003 | Charlie | CS | 3.2 |

Course:

| CourseID | Title | Credits |
|----------|-------|---------|
| CS101 | Introduction to Programming | 4 |
| CS102 | Data Structures and Algorithms | 4 |
| MATH101 | Calculus I | 3 |

Enroll:

| StudentID | CourseID | Grade |
|-----------|----------|-------|
| 1001 | CS101 | A |
| 1001 | CS102 | B |
| 1002 | MATH101 | A |
| 1003 | CS101 | C |
| 1003 | CS102 | B |

StudentView:

| Name | GPA |
|------|-----|
| Alice | 3.8 |
| Bob | 3.5 |
| Charlie | 3.2 |

CourseView:

| Title | Credits |
|-------|---------|
| Introduction to Programming | 4 |
| Data Structures and Algorithms | 4 |
| Calculus I | 3 |



# Data Independence and Database Language and Interfaces

## Data Independence

- Data independence is a property of DBMS that allows the database schema to be changed at one level without affecting the schema at the next higher level.
- Data independence helps to keep the data separated from the programs that use it, which increases the flexibility, maintainability and adaptability of the database system.
- Data independence can be achieved by using the three-schema architecture, which consists of three levels of abstraction: external, conceptual and internal.
- There are two types of data independence: logical and physical .

### Logical Data Independence

- Logical data independence is the ability to change the conceptual schema without affecting the external schemas or the application programs .
- Logical data independence allows the database administrator to modify the structure or organization of the data, such as adding, deleting or renaming tables, columns, views or relationships, without changing the way the data is accessed by the users or programs .
- Logical data independence is important for evolving the database to meet changing requirements or business rules, without affecting the existing applications or users .

### Physical Data Independence

- Physical data independence is the ability to change the internal schema without affecting the conceptual schema or the external schemas .
- Physical data independence allows the database administrator to modify the physical storage or implementation of the data, such as changing the file organization, indexing, compression, encryption or partitioning, without changing the logical structure or organization of the data .
- Physical data independence is important for improving the performance, security, reliability or availability of the database, without affecting the logical meaning or interpretation of the data .

## Database Language and Interfaces

- Database language and interfaces are the means of communication between the users or programs and the DBMS.
- Database language and interfaces provide different levels of functionality, abstraction and ease of use for different categories of users or programs.
- There are three main types of database language and interfaces: data definition language (DDL), data manipulation language (DML) and data query language (DQL).

### Data Definition Language (DDL)

- Data definition language (DDL) is a database language that is used to define the database schema, such as creating, altering or dropping tables, columns, views, indexes, constraints or triggers.
- Data definition language (DDL) is used by the database administrator or the database designer to specify the logical and physical structure of the data.
- Data definition language (DDL) statements are executed by the DBMS and stored in the data dictionary, which is a special database that contains the metadata or information about the database schema.

### Data Manipulation Language (DML)

- Data manipulation language (DML) is a database language that is used to manipulate the data in the database, such as inserting, updating, deleting or retrieving data.
- Data manipulation language (DML) is used by the end users or the application programs to perform various operations on the data.
- Data manipulation language (DML) statements are executed by the DBMS and may affect the data in the database or the data in the buffer cache, which is a temporary memory area that stores the most frequently accessed data.

### Data Query Language (DQL)

- Data query language (DQL) is a database language that is used to query the data in the database, such as selecting, filtering, sorting, grouping, aggregating or joining data.
- Data query language (DQL) is used by the end users or the application programs to retrieve the data that satisfies certain criteria or conditions.
- Data query language (DQL) statements are executed by the DBMS and may involve the data in the database or the data in the buffer cache, which is a temporary memory area that stores the most frequently accessed data.
- Data query language (DQL) is often a subset or a part of data manipulation language (DML), such as the SELECT statement in SQL.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here is the content for the topic of Data Definition Language in Unit 1 - Introduction.

# Data Definition Language

- Data Definition Language (DDL) is a subset of SQL that is used to define and modify the structure of database objects such as tables, views, indexes, constraints, etc.
- DDL statements are executed by the database system to create, alter, or drop database objects.
- DDL statements are also used to grant or revoke permissions on database objects to users or roles.
- Some of the common DDL statements are:

  - CREATE: This statement is used to create a new database object such as a table, view, index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table named students with three columns: id, name, and age.
  - ALTER: This statement is used to modify the structure or properties of an existing database object such as a table, view, index, etc. For example, `ALTER TABLE students ADD COLUMN email VARCHAR(50);` adds a new column named email to the students table.
  - DROP: This statement is used to delete an existing database object such as a table, view, index, etc. For example, `DROP TABLE students;` deletes the students table and all its data.
  - RENAME: This statement is used to change the name of an existing database object such as a table, view, index, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.
  - TRUNCATE: This statement is used to delete all the data from an existing table without deleting the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table but keeps the table structure.
  - COMMENT: This statement is used to add or modify a comment on a database object such as a table, column, view, etc. For example, `COMMENT ON TABLE students IS 'This table stores the information of students';` adds a comment to the students table.
  - GRANT: This statement is used to grant permissions on a database object to a user or a role. For example, `GRANT SELECT, INSERT, UPDATE ON students TO user1;` grants the permissions to select, insert, and update data on the students table to the user named user1.
  - REVOKE: This statement is used to revoke permissions on a database object from a user or a role. For example, `REVOKE UPDATE ON students FROM user1;` revokes the permission to update data on the students table from the user named user1.



# DML

DML stands for Data Manipulation Language. It is a family of computer languages that are used to manipulate data in a database. DML statements allow users to perform the following operations on data:

- Insert data into database tables
- Retrieve data from database tables
- Delete data from database tables
- Update data in database tables

Some of the common DML statements are:

- SELECT: This statement is used to query data from one or more tables or views. It can also be used to join, filter, group, and sort data.
- INSERT: This statement is used to add new rows of data to a table or view. It can also be used to copy data from another table or view.
- DELETE: This statement is used to remove existing rows of data from a table or view. It can also be used to delete data based on a condition.
- UPDATE: This statement is used to modify existing rows of data in a table or view. It can also be used to update data based on a condition.

DML is a subset of SQL, which is the most widely used database language. SQL also includes other types of statements, such as DDL (Data Definition Language), which is used to create and modify the structure of database objects, and DCL (Data Control Language), which is used to grant and revoke permissions on database objects.

DML statements can also trigger other actions in the database, such as constraints, indexes, views, and triggers. Constraints are rules that enforce data integrity and validity. Indexes are structures that improve the performance of data retrieval. Views are virtual tables that display data from one or more tables. Triggers are special types of stored procedures that automatically execute when a DML event occurs on a table or view.



# Overall Database Structure

A database is a collection of information that is related to a particular subject or purpose, such as tracking customer orders or maintaining a music collection. A database can be considered a structure in realization of the database language. A database management system (DBMS) is a software that extracts information from the database in response to queries.

The overall database structure consists of the following components:

- **Database schema**: This describes how real-world entities are modeled in the database. It defines the logical structure of the data, such as tables, columns, relationships, constraints, etc. A database schema can be represented in different levels of abstraction, such as conceptual, logical, and physical.
- **Query processor**: This is the component that processes the queries from the users or applications and translates them into low-level instructions for the storage manager. It also performs query optimization, which is the process of finding the most efficient way to execute a query.
- **Storage manager**: This is the component that manages the allocation of space on disk storage and the data structures used to represent information stored on disk. It also provides functions for accessing, inserting, deleting, modifying, and locking data.
- **Disk storage**: This is the component that stores the actual data on the physical devices, such as hard disks, flash drives, etc. It also organizes the data into files, pages, and records, and provides mechanisms for ensuring data integrity and security.

The following diagram illustrates the overall database structure:

Overall Database Structure

: Database schema - Wikipedia
: Structure of Database Management System - GeeksforGeeks
: Database | Definition, Types, & Facts | Britannica
: Learn the structure of an Access database - Microsoft Support



# Data Modeling Using the Entity Relationship Model

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity relationship (ER) model is a widely used data modeling technique that uses graphical symbols and connectors to depict the entities and their relationships in a database.
- An entity is a real-world object or concept that can be identified and distinguished from others. For example, a student, a course, or a book.
- A relationship is an association or link between two or more entities. For example, a student enrolls in a course, or a book belongs to a category.
- An entity relationship diagram (ERD) is a visual representation of an ER model, using rectangles to represent entities, diamonds to represent relationships, and lines to connect them. Optionally, attributes and cardinalities can be added to provide more details about the entities and relationships.
- An attribute is a property or characteristic of an entity or a relationship. For example, a student entity may have attributes such as name, ID, and major. A relationship may have attributes such as date, duration, or role.
- A cardinality is a constraint that specifies the number of instances of one entity that can be associated with each instance of another entity in a relationship. For example, a student can enroll in many courses, but a course can have only one instructor. This can be expressed as a one-to-many (1:N) cardinality.
- There are different types of relationships in ER model, such as one-to-one (1:1), one-to-many (1:N), many-to-one (N:1), and many-to-many (N:M). Each type has a different meaning and implication for the database design.
- ER model can be used to design and represent the conceptual, logical, and physical levels of a database. The conceptual level describes the entities and relationships in a high-level and abstract way, without considering the implementation details. The logical level describes the entities and relationships in a more detailed and structured way, using specific data types and constraints. The physical level describes how the entities and relationships are stored and accessed in a specific database system, using physical structures and indexes.
- ER model can help the database designers and developers to understand the requirements and specifications of a database, to communicate and collaborate with the stakeholders, to verify and validate the design, and to implement and maintain the database.



# ER Model Concepts

The ER model is a conceptual data model that describes the entities, attributes, and relationships in a database. It is used to design and represent the logical structure of a database. The ER model consists of the following basic concepts:

- **Entity**: An entity is a real-world object or thing that can be identified uniquely. For example, a student, a course, a teacher, etc. An entity is represented by a rectangle in an ER diagram.
- **Entity type**: An entity type is a collection of entities that share the same properties or characteristics. For example, the entity type Student represents all the students in a database. An entity type has a name and a set of attributes.
- **Entity set**: An entity set is a set of entities of the same entity type. For example, the entity set Students contains all the student entities in a database. An entity set is also represented by a rectangle in an ER diagram.
- **Attribute**: An attribute is a property or characteristic of an entity or a relationship. For example, the attributes of the entity type Student are Name, Roll No, Age, etc. An attribute has a name and a domain (or data type). An attribute is represented by an ellipse in an ER diagram.
- **Attribute types**: There are different types of attributes based on their values and dependencies. Some common attribute types are:

  - **Simple attribute**: An attribute that cannot be divided into subparts. For example, Name, Age, etc.
  - **Composite attribute**: An attribute that can be divided into subparts. For example, Address can be divided into Street, City, State, etc.
  - **Single-valued attribute**: An attribute that has only one value for a given entity. For example, Roll No, Age, etc.
  - **Multi-valued attribute**: An attribute that can have more than one value for a given entity. For example, Phone No, Email, etc.
  - **Derived attribute**: An attribute that can be derived from other attributes. For example, Total Marks can be derived from Marks of different subjects.
  - **Key attribute**: An attribute that can uniquely identify an entity in an entity set. For example, Roll No, Employee ID, etc.

- **Relationship**: A relationship is an association or connection between two or more entities. For example, a student enrolls in a course, a teacher teaches a course, etc. A relationship is represented by a diamond in an ER diagram.
- **Relationship type**: A relationship type is a collection of relationships that share the same meaning and properties. For example, the relationship type Enrolls represents all the enrollments of students in courses. A relationship type has a name and a degree (or number of participating entity types).
- **Relationship set**: A relationship set is a set of relationships of the same relationship type. For example, the relationship set Enrolls contains all the enrollments of students in courses in a database. A relationship set is also represented by a diamond in an ER diagram.
- **Relationship degree**: The degree of a relationship is the number of entity types that participate in the relationship. For example, the degree of the relationship type Enrolls is 2, as it involves two entity types: Student and Course. Some common relationship degrees are:

  - **Unary relationship**: A relationship that involves only one entity type. For example, a student is a friend of another student.
  - **Binary relationship**: A relationship that involves two entity types. For example, a student enrolls in a course.
  - **Ternary relationship**: A relationship that involves three entity types. For example, a student takes a course from a teacher.
  - **N-ary relationship**: A relationship that involves n entity types. For example, a student works on a project with other students and a supervisor.

- **Relationship cardinality**: The cardinality of a relationship is the number of occurrences of one entity type that can be associated with one occurrence of another entity type. For example, the cardinality of the relationship type Enrolls is one-to-many, as one student can enroll in many courses, but one course can be enrolled by only one student. Some common relationship cardinalities are:

  - **One-to-one**: A relationship where one entity of one entity type can be associated with only one entity of another entity type. For example, a student has a locker.
  - **One-to-many**: A relationship where one entity of one entity type can be associated with many entities of another entity type. For example, a teacher teaches many courses.
  - **Many-to-one**: A relationship where many entities of one entity



# Notation for ER Diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw an ER diagram, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entities**: Entities are the basic objects or concepts in the database, such as customers, products, orders, etc. They are represented by rectangles with the entity name inside. For example:

entity

- **Attributes**: Attributes are the properties or characteristics of the entities, such as name, age, price, quantity, etc. They are represented by ovals with the attribute name inside, connected to the entity by a line. For example:

attribute

- **Relationships**: Relationships are the associations or interactions between the entities, such as buys, sells, owns, etc. They are represented by diamonds with the relationship name inside, connected to the entities by lines. For example:

relationship

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. They are represented by underlining the attribute name. For example:

key

- **Cardinality**: Cardinality is the number of occurrences of one entity that are associated with one occurrence of another entity in a relationship. It is represented by placing numbers or symbols near the relationship line. For example:

cardinality

- **Participation**: Participation is the degree of involvement of an entity in a relationship. It can be either total or partial. Total participation means that every occurrence of an entity must participate in the relationship, while partial participation means that some occurrences of an entity may not participate in the relationship. It is represented by placing a double line or a single line near the entity. For example:

participation

- **Generalization**: Generalization is the process of grouping common attributes and relationships of two or more entities into a higher-level entity. It is represented by a triangle with the word "is a" above it, connecting the higher-level entity to the lower-level entities. For example:

generalization

- **Specialization**: Specialization is the process of dividing a higher-level entity into two or more lower-level entities based on some distinguishing characteristics. It is represented by a triangle with the word "is a" above it, connecting the lower-level entities to the higher-level entity. For example:

specialization

- **Aggregation**: Aggregation is the process of combining two or more entities or relationships into a single entity or relationship. It is represented by a dashed rectangle enclosing the entities or relationships to be aggregated, connected to the resulting entity or relationship by a line. For example:

aggregation

These are some of the common notations and symbols used to draw an ER diagram. Different modeling methodologies may use different notations and symbols, but the basic concepts are the same. An ER diagram is a useful tool for designing and documenting a database.



# Mapping Constraints for the notes of the Unit 1 - Introduction in the subject of Database Management System

- Mapping constraints are rules that define how many entities can be associated with each other in a relationship set .
- Mapping constraints are also known as cardinality ratios or cardinalities.
- Mapping constraints are important for designing and validating the entity-relationship (ER) model of a database .
- Mapping constraints can be classified into four types based on the number of entities involved in a relationship set  :
  - One-to-one (1:1): Each entity in one entity set can be related to at most one entity in another entity set, and vice versa. For example, each employee can have at most one spouse, and each spouse can have at most one employee.
  - One-to-many (1:N): Each entity in one entity set can be related to many entities in another entity set, but each entity in the other entity set can be related to at most one entity in the first entity set. For example, each department can have many employees, but each employee can belong to at most one department.
  - Many-to-one (N:1): Each entity in one entity set can be related to at most one entity in another entity set, but each entity in the other entity set can be related to many entities in the first entity set. This is the inverse of the one-to-many mapping constraint. For example, each employee can have at most one manager, but each manager can have many employees.
  - Many-to-many (N:M): Each entity in one entity set can be related to many entities in another entity set, and vice versa. For example, each student can take many courses, and each course can have many students.
- Mapping constraints can be represented graphically using the ER diagram notation  . The cardinality ratio is indicated by placing the appropriate numbers near the relationship symbol. For example, the following ER diagram shows a one-to-many relationship between department and employee:

ER diagram of department and employee

- Mapping constraints can also be enforced using primary and foreign key constraints in the relational database model . A primary key is a column or a set of columns that uniquely identifies each row in a table. A foreign key is a column or a set of columns that references the primary key of another table. A foreign key constraint ensures that the values in the foreign key column match the values in the referenced primary key column. For example, the following SQL statements create two tables, department and employee, and enforce the one-to-many mapping constraint between them using primary and foreign key constraints:

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

- Mapping constraints can also be specified using the minimum and maximum participation of each entity set in a relationship set  . The minimum participation indicates whether an entity must participate in at least one relationship instance or not. The maximum participation indicates whether an entity can participate in more than one relationship instance or not. The minimum and maximum participation can be represented using the ER diagram notation by placing a double line for total participation (min = 1) and a single line for partial participation (min = 0) near the entity set. The maximum participation is implied by the cardinality ratio. For example, the following ER diagram shows that each department must have at least one employee (total participation), and each employee can belong to at most one department (one-to-many cardinality):

ER diagram of department and employee with participation

- Mapping constraints are useful for describing the semantics and constraints of the real-world entities and relationships that are modeled by the database  . They help to avoid data inconsistency, redundancy, and anomalies in the database. They also help to optimize the database design and performance by reducing the number of tables and joins required to store and



# Keys for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A database is a collection of related data that is organized and stored in a structured way.
- A database management system (DBMS) is a software system that provides the functionality to create, manipulate, and query databases.
- A data model is a conceptual representation of the data and the relationships among them in a database.
- A schema is a description of the structure and constraints of a database, usually expressed in a data definition language (DDL).
- A data dictionary is a collection of metadata that describes the data elements, their attributes, and their relationships in a database.
- A query language is a language that allows users to specify and retrieve data from a database, usually expressed in a data manipulation language (DML).
- A transaction is a logical unit of work that consists of a sequence of operations on a database, and that either commits or aborts as a whole.
- A concurrency control mechanism is a technique that ensures the consistency and isolation of transactions that access a database concurrently.
- A recovery mechanism is a technique that ensures the durability and atomicity of transactions that access a database, by restoring the database to a consistent state in case of failures.
- A database security mechanism is a technique that protects the database from unauthorized access, modification, or disclosure, by enforcing policies and rules on the users and the data.



# Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple.
- A candidate key is also a super key, but not every super key is a candidate key.
- For example, consider a relation STUDENT with attributes RollNo, Name, Address, and Phone. A possible super key is {RollNo, Name}, since no two students can have the same roll number and name. However, this super key is not a candidate key, because we can remove the Name attribute and still have a unique identifier for each student. Therefore, a candidate key is {RollNo}.
- A super key can have any number of attributes, as long as they can uniquely identify a tuple. For example, {RollNo, Name, Address, Phone} is also a super key, but it is not minimal.
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier for the relation. The primary key is also a super key and a candidate key. The other candidate keys are called alternate keys or secondary keys.



# Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a database  .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and removing any attribute from it would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier of the relation .
- The other candidate keys that are not chosen as the primary key are called alternate keys or secondary keys.
- A candidate key can be a single attribute or a combination of attributes, depending on the data and the functional dependencies in the relation .
- A candidate key should satisfy the following properties:
  - Uniqueness: No two tuples in the relation should have the same values for the candidate key attributes.
  - Irreducibility: No subset of the candidate key attributes should have the uniqueness property.
  - Non-nullability: The candidate key attributes should not have null values in any tuple.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Database Management System. Here are some notes on the topic of Primary Key for Unit 1 - Introduction.

# Primary Key

- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key is a constraint that enforces the uniqueness and non-nullability of the values in the key column(s).
- A primary key can be defined at the time of table creation using the `PRIMARY KEY` keyword, or after the table is created using the `ALTER TABLE` statement.
- A table can have only one primary key, but the primary key can consist of multiple columns, forming a composite key.
- A primary key can be referenced by other tables to establish a relationship between them, using the `FOREIGN KEY` constraint.
- A primary key can also be used to create indexes on the table, to improve the performance of queries that use the key column(s) in the `WHERE` clause or the `JOIN` condition.

## Example

- Consider the following table that stores the details of students in a college.

| Student_ID | Name | Email | Phone | Major |
|------------|------|-------|-------|-------|
| 101        | Alice | alice@gmail.com | 1234567890 | CS |
| 102        | Bob | bob@yahoo.com | 2345678901 | Math |
| 103        | Charlie | charlie@hotmail.com | 3456789012 | Physics |
| 104        | David | david@gmail.com | 4567890123 | CS |

- In this table, the `Student_ID` column can be chosen as the primary key, as it uniquely identifies each student and is not null.
- The primary key can be defined as follows:

```sql
CREATE TABLE Students (
  Student_ID INT PRIMARY KEY,
  Name VARCHAR(50) NOT NULL,
  Email VARCHAR(50) UNIQUE,
  Phone VARCHAR(10) UNIQUE,
  Major VARCHAR(20)
);
```

- Alternatively, the primary key can be defined after the table is created as follows:

```sql
ALTER TABLE Students
ADD PRIMARY KEY (Student_ID);
```

- The primary key can be used to reference the `Students` table from another table, such as the `Courses` table, using the `FOREIGN KEY` constraint. For example:

```sql
CREATE TABLE Courses (
  Course_ID INT PRIMARY KEY,
  Course_Name VARCHAR(50) NOT NULL,
  Instructor VARCHAR(50) NOT NULL,
  Student_ID INT,
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID)
);
```

- The primary key can also be used to create an index on the `Students` table, to speed up the queries that use the `Student_ID` column. For example:

```sql
CREATE INDEX idx_students ON Students(Student_ID);
```

- This index can help to find the details of a student with a given ID faster, as the database can use the index to locate the row instead of scanning the whole table. For example:

```sql
SELECT Name, Email, Major FROM Students WHERE Student_ID = 101;
```



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of generalization for the unit 1 - introduction in the subject of database management system.

# Generalization

- Generalization is a process of extracting common characteristics from two or more classes and combining them into a generalized superclass.
- Generalization is also known as abstraction or inheritance in object-oriented programming.
- Generalization reduces complexity by hiding unnecessary details and highlighting relevant features.
- Generalization can be seen as a bottom-up approach, where two or more subclasses are merged into a superclass based on their similarities.
- For example, consider the following subclasses: Student, Teacher, and Staff. They all have some common attributes, such as name, age, and address. We can generalize them into a superclass called Person, which contains these common attributes. The subclasses can inherit these attributes from the superclass and also have their own specific attributes, such as roll number, salary, and department.

Generalization Example

- Generalization can also be applied to relationships between classes. For example, consider the following subclasses: Enroll, Teach, and Employ. They all have some common characteristics, such as a start date, an end date, and a role. We can generalize them into a superclass called Association, which contains these common characteristics. The subclasses can inherit these characteristics from the superclass and also have their own specific characteristics, such as a course, a subject, and a position.

Generalization Example 2

- Generalization can be represented in an entity-relationship diagram (ERD) using a triangle with the word "is a" above it. The superclass is placed above the triangle and the subclasses are placed below the triangle. The attributes and relationships of the superclass are inherited by the subclasses.

Generalization Representation

- Generalization can be implemented in a relational database using either one of the following methods:

  - Single table inheritance: In this method, a single table is created for the superclass and all the subclasses. The table contains all the attributes of the superclass and the subclasses, as well as a discriminator column that indicates the type of the subclass. This method is simple and efficient, but it may result in a lot of null values and redundancy.
  - Class table inheritance: In this method, a separate table is created for each subclass and the superclass. The table for the superclass contains the common attributes and a primary key. The tables for the subclasses contain the specific attributes and a foreign key that references the primary key of the superclass. This method avoids null values and redundancy, but it may require more joins and queries.



# Aggregation for the notes of the Unit 1 - Introduction in the subject of Database Management System

- Aggregation is a process of combining two or more entities to form a more meaningful new entity.
- Aggregation is often used to calculate statistics or to summarize data in a more meaningful way.
- Aggregation can be done using SQL aggregate functions such as SUM, COUNT, AVG, MIN, and MAX.
- Aggregation can also be done using the entity-relationship model (ER model), which is a conceptual diagram that represents the structure of a database and its components.
- Aggregation is needed when the entities are not significant enough to provide meaningful information on their own, or when they should be used for multiple relationships, or when they do not fit the entity-model relationship.
- Aggregation can improve the performance, readability, and maintainability of a database.
- Aggregation can also help to reduce data redundancy and inconsistency.
- Aggregation can be represented by a diamond shape in the ER model, which connects the aggregated entity with the other entities involved in the relationship.
- Aggregation can be classified into two types: simple aggregation and composite aggregation.
- Simple aggregation is when the aggregated entity is independent of the other entities involved in the relationship, and can exist without them.
- Composite aggregation is when the aggregated entity is dependent on the other entities involved in the relationship, and cannot exist without them.
- An example of simple aggregation is a student entity and a course entity, which can be aggregated into a registration entity that represents the relationship between them.
- An example of composite aggregation is a car entity and a wheel entity, which can be aggregated into a car-wheel entity that represents the relationship between them.



# Reduction of an ER Diagram to Tables

An ER diagram is a graphical representation of the entities and relationships in a database. It shows the structure and constraints of the data. An ER diagram can be converted into a relational table, which is a collection of rows and columns that store the data. The conversion of an ER diagram to tables involves the following steps:

- Convert each entity set in the ER diagram into a table. The table name should be the same as the entity set name. The table should have columns for each attribute of the entity set. The primary key of the table should be the same as the primary key of the entity set. If the entity set has a composite primary key, then the table should have a composite primary key as well.
- Convert each relationship set in the ER diagram into a table. The table name should be the same as the relationship set name. The table should have columns for each attribute of the relationship set. The primary key of the table should be a combination of the foreign keys that reference the tables of the participating entity sets. If the relationship set has a composite primary key, then the table should have a composite primary key as well. If the relationship set is many-to-many, then the table should have only the foreign keys as columns. If the relationship set is one-to-many or one-to-one, then the table can be merged with the table of the entity set that participates in the relationship set as the many or the optional side. The foreign key column should be added to the merged table to reference the table of the entity set that participates in the relationship set as the one or the mandatory side.
- Convert each weak entity set in the ER diagram into a table. The table name should be the same as the weak entity set name. The table should have columns for each attribute of the weak entity set. The primary key of the table should be a combination of the foreign key that references the table of the identifying entity set and the partial key of the weak entity set. The foreign key column should also be part of the primary key. If the weak entity set has a composite partial key, then the table should have a composite primary key as well.

Here is an example of an ER diagram and its corresponding tables:

ER diagram

The tables are:

**Student** (Student_ID, Name, Address, Phone, Email)  
**Primary Key**: Student_ID

**Course** (Course_ID, Title, Credits)  
**Primary Key**: Course_ID

**Enroll** (Student_ID, Course_ID, Semester, Grade)  
**Primary Key**: (Student_ID, Course_ID)  
**Foreign Key**: Student_ID references Student  
**Foreign Key**: Course_ID references Course

**Department** (Dept_ID, Name, Location, Phone)  
**Primary Key**: Dept_ID

**Instructor** (Instructor_ID, Name, Salary, Dept_ID)  
**Primary Key**: Instructor_ID  
**Foreign Key**: Dept_ID references Department

**Teach** (Instructor_ID, Course_ID, Semester)  
**Primary Key**: (Instructor_ID, Course_ID)  
**Foreign Key**: Instructor_ID references Instructor  
**Foreign Key**: Course_ID references Course

**Project** (Project_ID, Name, Budget, Dept_ID)  
**Primary Key**: Project_ID  
**Foreign Key**: Dept_ID references Department

**Work_On** (Employee_ID, Project_ID, Hours)  
**Primary Key**: (Employee_ID, Project_ID)  
**Foreign Key**: Employee_ID references Employee  
**Foreign Key**: Project_ID references Project

**Employee** (Employee_ID, Name, Address, Phone, Email, Instructor_ID)  
**Primary Key**: Employee_ID  
**Foreign Key**: Instructor_ID references Instructor



# Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases . It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The main extensions of the EER model are  :

- **Subclasses and Superclasses**: A subclass is a subset of entities of a superclass that share some common attributes or relationships. A superclass is a superset of entities that have some common attributes or relationships. For example, a superclass PERSON can have subclasses STUDENT and TEACHER, each with their own attributes and relationships.
- **Specialization and Generalization**: Specialization is the process of defining subclasses of a superclass based on some distinguishing characteristics. Generalization is the process of defining a superclass of several subclasses based on their common features. For example, a specialization of PERSON can be based on the occupation attribute, resulting in subclasses STUDENT and TEACHER. A generalization of STUDENT and TEACHER can be based on their common attributes, resulting in a superclass PERSON.
- **Category or Union Type**: A category or union type is a subclass that represents a collection of entities from different superclasses that share some common attributes or relationships. A category or union type can be total or partial, depending on whether all or some entities from the superclasses belong to the subclass. For example, a category or union type EMPLOYEE can represent a collection of entities from the superclasses STUDENT and TEACHER that have a common attribute salary.
- **Aggregation**: Aggregation is the process of treating a relationship as an entity, which can have its own attributes and relationships. Aggregation allows representing complex relationships among entities and relationships. For example, an aggregation of the relationship WORKS_FOR between EMPLOYEE and DEPARTMENT can have an attribute position, which represents the role of the employee in the department.

The EER model can be represented graphically using EER diagrams, which use symbols and notations to depict the entities, attributes, relationships, and constraints of the database. Some of the common symbols and notations are:

- **Entity**: A rectangle with the entity name.
- **Attribute**: An oval with the attribute name, connected to the entity or relationship by a line.
- **Relationship**: A diamond with the relationship name, connected to the entities by lines.
- **Key Attribute**: An attribute that uniquely identifies an entity, underlined in the entity name.
- **Composite Attribute**: An attribute that consists of several sub-attributes, represented by an oval with the attribute name and ovals with the sub-attribute names, connected by lines.
- **Multivalued Attribute**: An attribute that can have more than one value for an entity, represented by a double oval with the attribute name.
- **Derived Attribute**: An attribute that can be derived from other attributes, represented by a dashed oval with the attribute name.
- **Weak Entity**: An entity that depends on another entity for its existence, represented by a double rectangle with the entity name.
- **Identifying Relationship**: A relationship that relates a weak entity to its owner entity, represented by a double diamond with the relationship name and a double line connecting to the weak entity.
- **Subclass**: A rectangle with the subclass name inside the rectangle of the superclass, connected by a line with a triangle pointing to the superclass.
- **Superclass**: A rectangle with the superclass name, containing one or more rectangles with the subclass names.
- **Disjoint Constraint**: A constraint that specifies that the subclasses of a superclass are mutually exclusive, represented by a circle with a 'd' inside, connected to the line with the triangle.
- **Overlap Constraint**: A constraint that specifies that the subclasses of a superclass can have common entities, represented by a circle with an 'o' inside, connected to the line with the triangle.
- **Total Constraint**: A constraint that specifies that every entity in the superclass must belong to at least one subclass, represented by a double line connecting the superclass and the subclasses.
- **Partial Constraint**: A constraint that specifies that some entities in the superclass may not belong to any subclass, represented by a single line connecting the superclass and the subclasses.
- **Category or Union Type**: A circle with the category name inside, connected to the superclasses by lines with a triangle pointing to the circle.
- **Aggregation**: A rectangle with a dashed border, enclosing the relationship and the entities involved in the aggregation, connected to another entity



# Relationship of Higher Degree

- The degree of a relationship is the number of entity types that participate in the relationship .
- A relationship of higher degree is a relationship that involves more than two entity types .
- A relationship of higher degree can be converted into a set of binary relationships by creating a new entity type that represents the association among the original entity types .
- A relationship of higher degree can also be represented by a relation schema that includes the primary keys of the participating entity types as attributes.
- Examples of relationships of higher degree are:
  - A ternary relationship that relates three entity types, such as Student, Course, and Instructor.
  - A quaternary relationship that relates four entity types, such as Customer, Product, Supplier, and Location.
- Relationships of higher degree are not very common in database design, as they can be complex and difficult to convert into relational tables.



# Unit 2 - Relational Data Model and Language

- Relational Data Model and Language is a way of representing and manipulating data in a relational database.
- A relational database is a collection of data organized into tables, also called relations, where each table has a set of attributes (columns) and a set of tuples (rows).
- A relational database may use SQL (Structured Query Language) as its language for defining, querying, and modifying data, but SQL is not the same as the relational model.
- The relational model is based on the principles of first-order predicate logic, where data is represented as facts or propositions that can be evaluated as true or false.
- The relational model has some advantages over other data models, such as:
  - It is simple and intuitive, as data is organized in a tabular format that is easy to understand and manipulate.
  - It is flexible and expressive, as data can be queried and manipulated using various operators and functions that can combine and transform data from multiple tables.
  - It is consistent and reliable, as data is stored in a normalized form that avoids redundancy and inconsistency, and supports data integrity and security through constraints and rules.
- The relational model has some disadvantages as well, such as:
  - It may not capture the complex and dynamic nature of some real-world data, such as hierarchical, network, or object-oriented data.
  - It may not perform well for some applications that require high scalability, availability, or performance, such as big data, distributed, or real-time systems.
  - It may not support some advanced features or functionalities, such as multimedia, spatial, or temporal data, or user-defined data types and functions.



# Relational Data Model Concepts

The relational data model is a widely used data model for storing and processing data in a database. It is based on the concept of relations, which are logical structures that represent data as a collection of rows and columns. Each row in a relation is called a tuple, and each column is called an attribute. A relation has a name and a set of attributes that define its schema. The schema of a relation is also called its degree, and the number of tuples in a relation is called its cardinality.

Some of the major concepts of the relational data model are:

- **Primary key**: A primary key is an attribute or a set of attributes that uniquely identifies each tuple in a relation. A primary key cannot have null values or duplicate values. A relation can have only one primary key, which is also called the primary key constraint.
- **Foreign key**: A foreign key is an attribute or a set of attributes that references the primary key of another relation. A foreign key establishes a link between two relations, which is also called a relationship. A foreign key can have null values or duplicate values, but it must match the values of the referenced primary key, which is also called the referential integrity constraint.
- **Domain**: A domain is a set of possible values for an attribute. A domain defines the data type, format, and range of values for an attribute. A domain can be predefined or user-defined, and it can be shared by multiple attributes.
- **Null**: A null is a special value that indicates the absence of data or unknown data for an attribute. A null is not the same as zero or an empty string, and it cannot be compared with other values. A null can be allowed or disallowed for an attribute, depending on the business rules and data requirements.
- **View**: A view is a virtual relation that is derived from one or more base relations. A view does not store data physically, but it provides a logical representation of data that can be queried and manipulated. A view can be used to hide the complexity of the underlying data, to restrict the access to the data, or to provide a different perspective of the data.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of integrity constraints for the notes of the unit 2 - relational data model and language in the subject of database management system.

# Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- Integrity constraints can be classified into four types: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

## Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- Domain constraints ensure that the data stored in the relation conforms to the intended meaning and semantics of the attributes.

## Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by declaring primary keys or candidate keys for the relations.
- Key constraints ensure that the data stored in the relation is free of duplication and ambiguity.

## Entity Integrity Constraints

- Entity integrity constraints specify that the primary key attributes of a relation must not have null values.
- Entity integrity constraints can be enforced by declaring primary keys as not null for the relations.
- Entity integrity constraints ensure that the data stored in the relation can be uniquely referenced and identified.

## Referential Integrity Constraints

- Referential integrity constraints specify the consistency and validity of the data across two or more relations that are related by foreign keys.
- Referential integrity constraints can be enforced by declaring foreign keys as references to the primary keys of the referenced relations, and by specifying the actions to be taken when the referenced data is modified or deleted (such as cascade, restrict, set null, or set default).
- Referential integrity constraints ensure that the data stored in the relation is consistent with the data stored in the referenced relations, and that the relationships among the data are maintained.



# Entity Integrity

- Entity integrity is a rule that ensures the **uniqueness** and **non-nullability** of the primary key in a relational table  .
- The primary key is a column or a set of columns that **identifies** each row in the table **distinctly**  .
- Entity integrity prevents the insertion, update, or deletion of data that would cause **duplicate** or **missing** values in the primary key  .
- Entity integrity is important for maintaining the **accuracy** and **consistency** of the data in the database.
- Entity integrity can be enforced by the database system by **checking** the primary key values before performing any data manipulation operation  .
- Entity integrity can also be supported by the database design by **avoiding** the use of null values, default values, or derived values in the primary key  .
- Entity integrity is one of the **normal forms** of database normalization, which is a process of organizing the data in a database to reduce redundancy and improve data integrity.



# Referential Integrity

- Referential integrity is a property of data stating that all its references are valid.
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist.
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key.
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table.
- Referential integrity ensures the accuracy and consistency of data within a relationship.
- Referential integrity also prevents the deletion or modification of data that is referenced by other data.
- To enforce referential integrity, relational database systems use constraints, triggers, or cascading actions .
- Constraints are rules that restrict the values that can be inserted, updated, or deleted in a table.
- Triggers are procedures that are executed automatically when a specified event occurs, such as inserting, updating, or deleting data.
- Cascading actions are actions that are performed automatically on the related data when a primary key value is modified or deleted .
- For example, if a primary key value is deleted, the cascading action can be to delete all the related records in the associated table (cascade delete), or to set their foreign key values to null (set null) .
- Similarly, if a primary key value is updated, the cascading action can be to update all the related records in the associated table with the new value (cascade update), or to set their foreign key values to null (set null) .
- Referential integrity is an important aspect of relational data modeling, as it ensures the validity and consistency of the data and the relationships between tables .



# Keys Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple in a relation.
- A key constraint is a rule that specifies that no two tuples in a relation can have the same values for the key attributes.
- A key constraint ensures the integrity and consistency of the data in a relation.
- There are different types of keys in a relational data model, such as:

  - **Superkey**: A superkey is a set of attributes that contains a key. A superkey may have additional attributes that are not necessary for uniqueness.
  - **Candidate key**: A candidate key is a minimal superkey, that is, a superkey that does not have any redundant attributes. A relation may have more than one candidate key.
  - **Primary key**: A primary key is a designated candidate key that is chosen by the database designer to identify tuples in a relation. A relation can have only one primary key.
  - **Foreign key**: A foreign key is a set of attributes in a relation that references the primary key of another relation. A foreign key establishes a relationship between two relations and enforces referential integrity.



# Domain Constraints for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Domain constraints are the rules that specify the allowed values for each attribute or column in a relation or table .
- Domain constraints are a type of integrity constraint that ensures the data quality and accuracy in a relational database .
- Domain constraints can be defined by the data type, format, range, or set of values for each attribute or column .
- Domain constraints can be enforced by the database management system (DBMS) or by the application program that manipulates the data .
- Domain constraints can be violated if the user tries to insert, update, or delete a value that does not belong to the domain of the attribute or column .
- Domain constraints are important because they prevent the entry of invalid or inconsistent data, and they preserve the semantic meaning of the data in the database .

: Chapter 9 Integrity Rules and Constraints – Database Design – 2nd Edition
: Domain constraints in DBMS - GeeksforGeeks
: Constraints on Relational database model - GeeksforGeeks



# Relational Algebra for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational algebra is a theory that uses algebraic structures for modeling data, and defining queries on it with a well founded semantics.
- Relational algebra is a procedural query language, where the user tells the system to carry out a set of operations to obtain the desired results.
- Relational algebra provides a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.
- Relational databases store tabular data represented as relations. Queries over relational databases often likewise return tabular data represented as relations.
- Relational algebra operations can be classified into two categories: basic and derived.
- Basic operations are those that are directly supported by the relational model, such as selection, projection, union, set difference, Cartesian product, and rename.
- Derived operations are those that can be expressed in terms of the basic operations, such as join, intersection, division, natural join, and assignment.
- Relational algebra operations can be applied to one or more relations and produce a new relation as a result.
- Relational algebra operations can be composed together to form more complex queries.
- Relational algebra operations can be represented by a tree diagram, where the leaves are the input relations and the nodes are the operations.
- Relational algebra operations can be evaluated by applying the operations in a bottom-up manner, starting from the leaves and moving up to the root.



# Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a **non-procedural** query language that describes **what** data to retrieve from a relational database, without specifying **how** to do it  .
- Relational calculus is based on **mathematical logic**, specifically **predicate calculus**, which uses variables, constants, operators, quantifiers, and predicates to form expressions  .
- Relational calculus is an **integral part** of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- Relational calculus can be divided into two types: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**   .
- Tuple relational calculus uses **tuple variables** to represent rows of a relation, and checks every row with a **predicate expression** that evaluates to true or false  .
- Domain relational calculus uses **domain variables** to represent individual values of the attributes of a relation, and forms expressions using **membership conditions** that specify which values belong to which relation  .
- Both types of relational calculus are **equivalent** in expressive power, meaning that any query that can be expressed in one type can also be expressed in the other type .
- Relational calculus is also **equivalent** to relational algebra, another query language that is **procedural** and specifies **how** to manipulate the data in a relational database  .
- Relational calculus is a **declarative** language that can express complex queries in a concise and elegant way, but it is not directly executable by a RDBMS  .
- Relational calculus expressions must satisfy the **safe query** condition, which ensures that the result of a query is finite and can be computed in a reasonable amount of time  .



# Tuple and Domain Calculus

## Tuple Relational Calculus (TRC)

- Tuple relational calculus (TRC) is a **non-procedural** query language used in relational database management systems (RDBMS) to retrieve data from tables.
- TRC is based on the concept of **tuples**, which are ordered sets of attribute values that represent a single row or record in a database table.
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable that ranges over a relation, and `P(t)` is a predicate that evaluates to true or false for each tuple `t` .
- The result of a TRC query is the set of all tuples `t` that satisfy the predicate `P(t)` .
- For example, the query `{t | t ∈ Employee and t[SALARY] > 5000}` returns the set of all tuples `t` that belong to the relation `Employee` and have a salary greater than 5000.

## Domain Relational Calculus (DRC)

- Domain relational calculus (DRC) is another **non-procedural** query language used in RDBMS to retrieve data from tables.
- DRC is based on the concept of **domains**, which are the sets of values that an attribute can take in a relation.
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `x1, x2, ..., xn` are domain variables that take values from the domains of attributes, and `P(x1, x2, ..., xn)` is a predicate that evaluates to true or false for each combination of values .
- The result of a DRC query is the set of all tuples `<x1, x2, ..., xn>` that satisfy the predicate `P(x1, x2, ..., xn)` .
- For example, the query `{<E.NAME, E.SALARY> | E ∈ Employee and E.SALARY > 5000}` returns the set of all pairs of name and salary of employees who have a salary greater than 5000 .

## Comparison between TRC and DRC

- Both TRC and DRC are **equivalent** in expressive power, meaning that any query that can be expressed in one language can also be expressed in the other .
- However, TRC and DRC have different **advantages** and **disadvantages** in terms of readability, simplicity, and safety.
- TRC is more **readable** and **simple** than DRC, as it uses tuple variables that directly refer to the rows of a relation, rather than domain variables that have to be matched with the attributes of a relation.
- DRC is more **safe** than TRC, as it avoids the possibility of generating an infinite set of tuples as a result of a query, which can happen in TRC if the predicate does not constrain the tuple variable enough.
- For example, the query `{t | t ∈ Employee}` in TRC returns the entire relation `Employee`, which may be very large or infinite, whereas the query `{<E.NAME, E.SALARY> | E ∈ Employee}` in DRC returns only the name and salary of each employee, which is a finite set.



# Introduction to SQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- SQL can perform various tasks on data, such as creating, querying, updating, deleting, and managing tables, views, indexes, constraints, triggers, stored procedures, and functions.
- SQL is based on relational algebra and calculus, which are mathematical models for expressing queries on relations (tables).
- SQL has several dialects or variants, such as MySQL, Oracle, SQL Server, PostgreSQL, SQLite, etc. Each dialect may have some specific features or syntax that are not supported by other dialects.
- SQL is divided into several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
  - DDL is used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, constraints, etc.
  - DML is used to manipulate the data in the database, such as inserting, updating, deleting, and merging records.
  - DCL is used to control the access and security of the database, such as granting and revoking permissions and roles to users and groups.
  - DQL is used to query and retrieve data from the database, such as selecting, joining, filtering, grouping, sorting, and aggregating records.
- SQL statements are composed of keywords, identifiers, operators, expressions, clauses, and terminators. Keywords are reserved words that have a specific meaning and function in SQL, such as SELECT, FROM, WHERE, etc. Identifiers are names given to database objects, such as tables, columns, views, etc. Operators are symbols that perform arithmetic, logical, or comparison operations on values, such as +, -, AND, OR, =, etc. Expressions are combinations of values, operators, and functions that produce a result, such as 2 + 3, UPPER(name), etc. Clauses are parts of a SQL statement that specify a condition or an action, such as WHERE name = 'John', ORDER BY age DESC, etc. Terminators are characters that mark the end of a SQL statement, such as a semicolon (;) or a slash (/).
- SQL statements can be executed interactively or in batches. Interactive execution means typing and running one SQL statement at a time in a command-line interface or a graphical user interface. Batch execution means storing multiple SQL statements in a file and running them all at once.



# Characteristics of SQL

SQL is a popularly used acronym for Structured Query Language. It is a computer language used to store, manipulate, and retrieve data from a relational database. SQL may do a variety of other tasks, including database optimization and maintenance.

Some of the main characteristics of SQL are:

- **Easy to learn**: SQL is an extremely practical and user-friendly language. Even if you have no prior experience with programming, you can learn the basic syntax and commands of SQL in a short time.
- **Wide variety of commands**: SQL supports a wide variety of commands such as DDL (Data Definition Language) commands, DML (Data Manipulation Language) commands, DCL (Data Control Language) commands, and TCL (Transaction Control Language) commands. These commands allow you to create, modify, delete, query, and control the data and the database.
- **Stored procedures**: A stored procedure is a set of SQL statements that can be executed as a single unit. Stored procedures can improve the performance, security, and modularity of the database applications.
- **High performance**: SQL provides high-performance programming capability for highly transactional, heavy workload, and high usage database systems. SQL programming gives various ways to describe the data more analytically and efficiently.
- **Portability**: SQL is a standard language that is supported by most of the relational database management systems. SQL can be used to access data from different platforms and operating systems. SQL can also be embedded in other programming languages such as Java, C#, Python, etc.
- **Data definition and data manipulation**: SQL can execute queries against the database to retrieve, insert, update, and delete data. SQL can also describe the data by defining the structure, constraints, and relationships of the tables and columns in the database.



# Advantage of SQL

SQL is a widely used language for managing and manipulating data in relational database systems. SQL has many advantages over other database management languages, such as:

- **Faster and efficient query processing**: SQL can process a large amount of data in a very short amount of time. SQL can perform operations like insertion, deletion, updating, and retrieval of data with simple and concise commands .
- **No coding skills required**: SQL does not require complex programming skills to retrieve data. SQL uses basic keywords and syntax that are easy to learn and understand. SQL also has a standard format that is compatible with different database systems .
- **Data integrity and security**: SQL can enforce rules and constraints on the data to ensure its validity and consistency. SQL can also protect the data from unauthorized access and manipulation by using various security features, such as passwords, encryption, and permissions .
- **Data analysis and reporting**: SQL can perform various analytical functions and calculations on the data, such as aggregation, sorting, filtering, grouping, and joining. SQL can also generate reports and visualizations of the data using various tools and applications .
- **Portability and scalability**: SQL can work with different types of data and database systems, such as MySQL, Oracle, SQL Server, and PostgreSQL. SQL can also handle large and complex data sets and support multiple users and transactions .



# SQL Data Types and Literals

SQL data types are used to represent the nature of the data that can be stored in the database table. Every field or column in a table is given a data type when a table is defined . SQL data types can be categorized into the following groups:

- Numeric: These data types store numeric values, such as integers, decimals, and floating-point numbers. Examples are `INT`, `DECIMAL`, `FLOAT`, and `NUMERIC`.
- Character: These data types store character strings, such as names, addresses, and descriptions. Examples are `CHAR`, `VARCHAR`, `TEXT`, and `NCHAR`.
- Date and time: These data types store date and time values, such as birthdays, appointments, and timestamps. Examples are `DATE`, `TIME`, `DATETIME`, and `TIMESTAMP`.
- Binary: These data types store binary strings, such as images, files, and encryption keys. Examples are `BINARY`, `VARBINARY`, `BLOB`, and `IMAGE`.
- Boolean: These data types store logical values, such as true or false. Examples are `BIT`, `BOOLEAN`, and `TINYINT`.
- Special: These data types store special values, such as spatial data, XML data, JSON data, and variant data. Examples are `GEOMETRY`, `XML`, `JSON`, and `SQL_VARIANT`.

SQL literals are constants that represent fixed values in SQL statements . SQL literals can be of the following types:

- Character string: These literals are enclosed in single quotes, such as `'Hello'`, `'SQL'`, and `'2021-03-15'`.
- Bit string: These literals are binary values that are prefixed with `B` or `0b` and enclosed in single quotes, such as `B'1010'`, `0b1100`, and `B'1001'`.
- Exact numeric: These literals are decimal or integer values that can have an optional sign, such as `123`, `-456`, and `78.90`.
- Approximate numeric: These literals are floating-point values that can have an optional sign and an exponent, such as `1.23E4`, `-5.67E-8`, and `3.14`.



# Types of SQL Commands

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL commands are instructions that can be used to perform various operations on the data, such as creating, modifying, querying, or controlling the database.

SQL commands are divided into five broad categories, based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, or constraints. Some examples of DDL commands are:

  - CREATE: This command is used to create a new table, view, index, or database in the database server.
  - ALTER: This command is used to modify the structure or schema of an existing table, view, index, or database in the database server.
  - DROP: This command is used to delete an existing table, view, index, or database from the database server.
  - RENAME: This command is used to change the name of an existing table, view, index, or database in the database server.
  - TRUNCATE: This command is used to remove all the data from an existing table, but not the table structure or schema.

- **Data Manipulation Language (DML)**: These commands are used to manipulate the data stored in the database, such as inserting, updating, deleting, or merging data. Some examples of DML commands are:

  - INSERT: This command is used to insert new data into a table in the database server.
  - UPDATE: This command is used to modify the existing data in a table in the database server.
  - DELETE: This command is used to remove the existing data from a table in the database server.
  - MERGE: This command is used to combine the data from two or more tables into one table in the database server.

- **Data Query Language (DQL)**: These commands are used to query or retrieve the data from the database, such as selecting, filtering, sorting, or grouping data. Some examples of DQL commands are:

  - SELECT: This command is used to select or extract data from one or more tables or views in the database server.
  - WHERE: This command is used to filter the data based on some conditions or criteria in the database server.
  - ORDER BY: This command is used to sort the data in ascending or descending order based on some columns or expressions in the database server.
  - GROUP BY: This command is used to group the data based on some columns or expressions and apply some aggregate functions on them in the database server.
  - HAVING: This command is used to filter the data after grouping them based on some conditions or criteria in the database server.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of the data in the database, such as granting, revoking, or denying privileges or roles to users or groups. Some examples of DCL commands are:

  - GRANT: This command is used to grant some privileges or roles to a user or a group in the database server.
  - REVOKE: This command is used to revoke some privileges or roles from a user or a group in the database server.
  - DENY: This command is used to deny some privileges or roles to a user or a group in the database server.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, such as committing, rolling back, or saving the changes made by the transactions. Some examples of TCL commands are:

  - COMMIT: This command is used to save the changes made by a transaction to the database server.
  - ROLLBACK: This command is used to undo the changes made by a transaction to the database server.
  - SAVEPOINT: This command is used to create a point in the transaction where the changes can be rolled back to in the database server.



# SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They are used to specify conditions, filter results, perform calculations, or manipulate strings. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used for mathematical operations on numerical data, such as adding, subtracting, multiplying, or dividing. For example, `SELECT 10 + 10;` returns 20.
- Comparison operators: These operators are used to compare two values or expressions and return a Boolean value (true or false). For example, `SELECT 10 > 5;` returns true.
- Logical operators: These operators are used to combine two or more conditions and return a Boolean value. For example, `SELECT 10 > 5 AND 10 < 20;` returns true.
- Bitwise operators: These operators are used to perform bitwise operations on binary data, such as AND, OR, XOR, or NOT. For example, `SELECT 10 & 5;` returns 0.
- String operators: These operators are used to manipulate strings, such as concatenating, extracting, or replacing. For example, `SELECT 'Hello' + 'World';` returns HelloWorld.
- Set operators: These operators are used to combine the results of two or more queries into one result set, such as UNION, INTERSECT, or EXCEPT. For example, `SELECT name FROM table1 UNION SELECT name FROM table2;` returns the names from both tables without duplicates.

The procedure for using SQL operators is to place them between the values or expressions that they operate on, and follow the syntax rules of the SQL clause that they are used in. For example, in the WHERE clause, the operators must be enclosed in parentheses if they have lower precedence than other operators. For example, `SELECT * FROM table WHERE (10 + 10) > 15;` returns the rows where the sum of 10 and 10 is greater than 15.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 2 - Relational data Model and Language in the subject of Database Management System. Here are some tables that you can use for your notes:

### Tables for the notes of the Unit 2 - Relational data Model and Language

- A **relation** is a set of tuples that have the same attributes. A tuple is a single data item in a relation. An attribute is a column of a relation. A relation can be represented as a table with rows and columns.

- A **relational schema** is a set of relation schemas, where each relation schema defines the name, attributes, and constraints of a relation. A relation schema can be written as R(A1, A2, ..., An), where R is the name of the relation and A1, A2, ..., An are the attributes.

- A **relational database** is a collection of relations that conform to a relational schema. A relational database can be represented as a set of tables, where each table corresponds to a relation in the relational schema.

- A **relational algebra** is a set of operations that can be applied to relations or sets of relations to produce new relations. The basic operations of relational algebra are:

  - **Selection** (σ): selects a subset of tuples from a relation that satisfy a given condition. For example, σ<sub>age > 20</sub>(Student) selects the tuples from the Student relation where the age attribute is greater than 20.

  - **Projection** (π): selects a subset of attributes from a relation and eliminates duplicates. For example, π<sub>name, course</sub>(Student) selects the name and course attributes from the Student relation and removes any duplicate tuples.

  - **Union** (∪): combines two relations that have the same set of attributes and eliminates duplicates. For example, Student ∪ Teacher combines the Student and Teacher relations and removes any duplicate tuples.

  - **Intersection** (∩): selects the common tuples from two relations that have the same set of attributes. For example, Student ∩ Teacher selects the tuples that are both in the Student and Teacher relations.

  - **Difference** (-): selects the tuples from the first relation that are not in the second relation, where both relations have the same set of attributes. For example, Student - Teacher selects the tuples that are in the Student relation but not in the Teacher relation.

  - **Cartesian product** (×): combines every tuple from the first relation with every tuple from the second relation, where the two relations can have different sets of attributes. For example, Student × Course combines every tuple from the Student relation with every tuple from the Course relation.

  - **Join** (⋈): combines two relations based on a common attribute or a join condition. For example, Student ⋈<sub>Student.course = Course.id</sub> Course combines the Student and Course relations based on the condition that the course attribute of the Student relation matches the id attribute of the Course relation.

  - **Division** (÷): selects the tuples from the first relation that are associated with every tuple from the second relation, where the second relation is a subset of the first relation. For example, Student ÷ Course selects the tuples from the Student relation that are enrolled in every course in the Course relation.

- A **relational calculus** is a set of expressions that can be used to specify queries on a relational database. The expressions are based on logic and quantifiers. There are two types of relational calculus:

  - **Tuple relational calculus** (TRC): uses variables that range over tuples of a relation. For example, {T.name | Student(T) ∧ T.age > 20} is a TRC expression that returns the names of the students whose age is greater than 20.

  - **Domain relational calculus** (DRC): uses variables that range over domains of attributes. For example, {<x, y> | ∃z(Student(<x, y, z>) ∧ z > 20)} is a DRC expression that returns the pairs of name and course of the students whose age is greater than 20.



# Views and Indexes for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

## Views
- A view is a logical representation of a table or a query that is stored in the database.
- A view can be created from one or more tables or other views, by using a SELECT statement.
- A view can be used to simplify queries, restrict access to data, or provide a consistent interface to data.
- A view does not store any data physically, but only references the data in the underlying tables or views.
- A view can be created, modified, or dropped using the SQL commands CREATE VIEW, ALTER VIEW, or DROP VIEW.
- A view can have the same name as a table, as long as they are in different schemas.
- A view can be queried, updated, inserted, or deleted from, as long as it meets certain conditions.
- A view can be joined with other tables or views, as long as the join conditions are valid.

## Indexes
- An index is a data structure that improves the speed of data retrieval from a table or a view.
- An index can be created on one or more columns of a table or a view, by using a CREATE INDEX statement.
- An index can be used to speed up queries that involve filtering, sorting, grouping, or joining on the indexed columns.
- An index can also enforce uniqueness or referential integrity constraints on the indexed columns.
- An index stores a copy of the indexed columns and a pointer to the corresponding rows in the table or the view.
- An index can be clustered or nonclustered, depending on how the data is physically stored.
- A clustered index determines the order of the rows in the table or the view, and can only be one per table or view.
- A nonclustered index does not affect the order of the rows in the table or the view, and can be multiple per table or view.
- An index can be created, modified, or dropped using the SQL commands CREATE INDEX, ALTER INDEX, or DROP INDEX.
- An index can be disabled, rebuilt, or reorganized using the SQL commands DISABLE INDEX, REBUILD INDEX, or REORGANIZE INDEX.

## Indexed Views
- An indexed view is a view that has a unique clustered index created on it .
- An indexed view is also called a materialized view, because it stores the result of the view definition in a physical table .
- An indexed view can improve the performance of queries that involve aggregations, joins, or complex calculations on the view columns .
- An indexed view can also reduce the storage space and maintenance cost of the underlying tables or views, by eliminating the need for redundant data .
- An indexed view has some limitations and requirements, such as the view definition must be deterministic, schema-bound, and not reference any non-deterministic functions or expressions .
- An indexed view can be created, modified, or dropped using the SQL commands CREATE VIEW, ALTER VIEW, or DROP VIEW, with the WITH SCHEMABINDING and WITH (CLUSTERED) options .
- An indexed view can be queried, updated, inserted, or deleted from, as long as it meets the same conditions as a regular view .
- An indexed view can be joined with other tables or views, as long as the join conditions are valid .



# Queries and Subqueries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A **query** is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language, such as SQL, which specifies the desired result without describing how to compute it.
- A **subquery** is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar (a single value), a single row, a single column, or a table (one or more rows of one or more columns).
- Subqueries are often used when you need to process data in several steps. For the majority of subqueries you’ll see in actual practice, the inner query will execute first and pass its result to the outer query it's nested in. Subqueries are usually contrasted with Common Table Expressions (CTEs) as they have similar use cases.
- Subqueries can be used in different clauses of a query, such as:
  - **WHERE clause**: A subquery in the WHERE clause can be used to filter the rows returned by the outer query based on the values returned by the subquery. For example, the following query returns the names of the employees who have a salary higher than the average salary of all employees:

  ```sql
  SELECT name
  FROM employees
  WHERE salary > (SELECT AVG(salary) FROM employees);
  ```

  - **FROM clause**: A subquery in the FROM clause can be used to create a temporary table that can be joined with other tables in the outer query. For example, the following query returns the names and departments of the employees who work in the same department as John:

  ```sql
  SELECT e.name, e.department
  FROM employees e
  JOIN (SELECT department FROM employees WHERE name = 'John') d
  ON e.department = d.department;
  ```

  - **SELECT clause**: A subquery in the SELECT clause can be used to return a scalar value for each row returned by the outer query. For example, the following query returns the name, salary, and rank of each employee, where the rank is the number of employees who have a higher salary than the current employee:

  ```sql
  SELECT name, salary, (SELECT COUNT(*) FROM employees e2 WHERE e2.salary > e1.salary) AS rank
  FROM employees e1;
  ```

- Subqueries can also be classified into two types based on their dependency on the outer query:
  - **Correlated subquery**: A subquery that references one or more columns from the outer query in its WHERE clause. A correlated subquery cannot be executed independently, and it is re-evaluated for each row returned by the outer query. For example, the following query returns the names of the employees who have the highest salary in their department:

  ```sql
  SELECT name
  FROM employees e1
  WHERE salary = (SELECT MAX(salary) FROM employees e2 WHERE e2.department = e1.department);
  ```

  - **Non-correlated subquery**: A subquery that does not reference any column from the outer query. A non-correlated subquery can be executed independently, and it is evaluated only once for the entire outer query. For example, the following query returns the names of the employees who have a salary higher than 5000:

  ```sql
  SELECT name
  FROM employees
  WHERE salary > (SELECT 5000);
  ```

- A **relational data model** is a data model that represents data as a collection of tables, where each table consists of rows and columns. Each row represents an entity or a record, and each column represents an attribute or a field of the entity. A relational data model also defines constraints and relationships among the tables, such as primary keys, foreign keys, and referential integrity.
- A **relational query language** is a language that allows users to manipulate and query data stored in a relational database. A relational query language can be either procedural or declarative. A procedural query language requires the user to specify the steps or algorithms to retrieve the desired data, while a declarative query language requires the user to specify the desired result without describing how to compute it.
- The most widely used relational query language is **SQL (Structured Query Language)**, which is a declarative language that consists of several commands



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of aggregate functions for the unit 2 - relational data model and language in the subject of database management system.

# Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the GROUP BY clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - COUNT: returns the number of values in a set or the number of rows that satisfy a condition.
  - SUM: returns the sum of all values in a set or the sum of values that satisfy a condition.
  - AVG: returns the average of all values in a set or the average of values that satisfy a condition.
  - MIN: returns the minimum value in a set or the minimum value that satisfies a condition.
  - MAX: returns the maximum value in a set or the maximum value that satisfies a condition.

- Aggregate functions can be used in the SELECT clause, the HAVING clause, or the ORDER BY clause of a query.
- Aggregate functions ignore NULL values in the set of values they operate on, unless otherwise specified by the function.
- Aggregate functions can be nested, meaning that one aggregate function can be used as an argument for another aggregate function.
- Examples of aggregate functions in SQL:

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

  - To find the highest salary among the employees who have a bonus:

    ```sql
    SELECT MAX(salary)
    FROM employee
    WHERE bonus IS NOT NULL;
    ```

  - To find the number of distinct job titles in the employee table:

    ```sql
    SELECT COUNT(DISTINCT job_title)
    FROM employee;
    ```



# Relational Data Model and Language

- Relational Data Model and Language is a way of organizing data in a database into tables, where each table consists of rows (tuples) and columns (attributes).
- A database that uses the relational model is called a relational database. Relational databases may use SQL as their language, but relational databases are not the same thing as an SQL database.
- The relational model is based on the concept of mathematical relations, where each tuple represents a fact that involves a set of values (domains).
- The relational model has some advantages over other data models, such as:
  - It is simple and intuitive, as it represents data in a tabular format that is easy to understand and manipulate.
  - It is flexible and expressive, as it allows complex queries and operations to be performed on the data using a declarative language (SQL).
  - It is consistent and logical, as it follows the rules of first-order predicate logic and ensures data integrity and consistency.
  - It is efficient and scalable, as it allows data to be stored and accessed in an optimized way using indexes, views, and other techniques.
- The relational model has some components and concepts, such as:
  - Relation: A relation is a set of tuples that have the same attributes. A relation is also called a table or a file.
  - Attribute: An attribute is a named column of a relation. An attribute is also called a field or a column.
  - Tuple: A tuple is a row of a relation. A tuple is also called a record or a row.
  - Domain: A domain is a set of allowable values for an attribute. A domain is also called a data type or a format.
  - Degree: The degree of a relation is the number of attributes it has.
  - Cardinality: The cardinality of a relation is the number of tuples it has.
  - Key: A key is a set of one or more attributes that uniquely identifies a tuple in a relation. A key is also called an identifier or a primary key.
  - Foreign Key: A foreign key is a set of one or more attributes in a relation that refers to the key of another relation. A foreign key is also called a reference or a secondary key.
  - Schema: A schema is a description of the structure and constraints of a database. A schema is also called a definition or a specification.
  - Instance: An instance is a snapshot of the data in a database at a given point in time. An instance is also called a state or a content.
  - Constraint: A constraint is a rule that restricts the data that can be stored in a database. A constraint is also called a condition or a restriction.
  - Relational Algebra: Relational algebra is a set of operations that can be applied to relations to manipulate and query data. Relational algebra is also called a query language or a data manipulation language.
  - Relational Calculus: Relational calculus is a set of expressions that can be used to specify queries on relations. Relational calculus is also called a query language or a data definition language.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of update and delete operations for the notes of the unit 2 - relational data model and language in the subject of database management system.

# Update and Delete Operations

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes for a set of tuples that satisfy a given condition.
- Delete operations can remove one or more tuples that satisfy a given condition from a relation.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and with proper authorization.

## Update Operation

- An update operation can be expressed in the form:

```
UPDATE relation_name
SET attribute_name = expression
WHERE condition;
```

- The relation_name specifies the name of the relation to be updated.
- The attribute_name specifies the name of the attribute whose value is to be changed.
- The expression specifies the new value for the attribute, which can be a constant, a variable, or a function of other attributes.
- The condition specifies the criteria for selecting the tuples to be updated.
- The update operation modifies the values of the attribute for all the tuples that satisfy the condition in the relation.
- If the condition is omitted, the update operation applies to all the tuples in the relation.

- For example, the following update operation changes the salary of all the employees in the EMPLOYEE relation who work in the department number 5 by 10%:

```
UPDATE EMPLOYEE
SET SALARY = SALARY * 1.1
WHERE DNO = 5;
```

## Delete Operation

- A delete operation can be expressed in the form:

```
DELETE FROM relation_name
WHERE condition;
```

- The relation_name specifies the name of the relation from which the tuples are to be deleted.
- The condition specifies the criteria for selecting the tuples to be deleted.
- The delete operation removes all the tuples that satisfy the condition from the relation.
- If the condition is omitted, the delete operation removes all the tuples from the relation.

- For example, the following delete operation removes all the employees in the EMPLOYEE relation who have a salary less than 30000:

```
DELETE FROM EMPLOYEE
WHERE SALARY < 30000;
```

## Integrity and Consistency Constraints

- Update and delete operations can violate the integrity and consistency constraints of the database, such as primary key, foreign key, domain, and semantic constraints.
- A primary key constraint requires that the value of the primary key attribute(s) of a relation must be unique and not null for each tuple.
- A foreign key constraint requires that the value of the foreign key attribute(s) of a relation must either match the value of the primary key attribute(s) of another relation, or be null.
- A domain constraint requires that the value of an attribute must belong to a predefined set of values, or a range of values, or a data type.
- A semantic constraint requires that the value of an attribute must satisfy some logical or business rules that are not enforced by the database system.

- For example, the following update operation violates the primary key constraint of the EMPLOYEE relation, as it tries to assign the same SSN value to two different tuples:

```
UPDATE EMPLOYEE
SET SSN = '123456789'
WHERE LNAME = 'Smith' OR LNAME = 'Jones';
```

- The following delete operation violates the foreign key constraint of the DEPARTMENT relation, as it tries to remove a tuple that is referenced by another tuple in the EMPLOYEE relation:

```
DELETE FROM DEPARTMENT
WHERE DNUMBER = 5;
```

- The following update operation violates the domain constraint of the SALARY attribute of the EMPLOYEE relation, as it tries to assign a negative value to it:

```
UPDATE EMPLOYEE
SET SALARY = -1000
WHERE SSN = '123456789';
```

- The following update operation violates the semantic constraint of the BDATE attribute of the EMPLOYEE relation, as it tries to assign a future date to it:

```
UPDATE EMPLOYEE
SET BDATE = '2023-01-01'
WHERE SSN = '123456789';
```

- To prevent the violation of integrity and consistency constraints, the database system must check the validity of the update and delete operations before executing them, and reject them if they are invalid.
- Alternatively, the database system can perform some corrective actions to restore the integrity and consistency of the database, such as cascading the update or delete operations to the related relations, or setting the values of the affected attributes to null.



# Joins for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Joins are operations in relational databases that allow queries across multiple tables by matching rows that satisfy a join condition .
- Joins are based on the relational algebra operation of the same name, which is a combination of Cartesian product and selection .
- Joins are useful for retrieving data from related tables and combining them in a single result table  .
- The prerequisite for using joins is that the tables have foreign key relationships, which link them by a common attribute  .
- There are different types of joins, each with a different syntax and result  . Some of the most common ones are:

  - Theta join: A join that uses a comparison operator other than equality to match rows from different tables. The join condition is denoted by the symbol θ.
  - Equijoin: A join that uses only the equality operator to match rows from different tables. It is a special case of theta join .
  - Natural join: A join that matches rows from different tables based on the common attributes with the same name and data type. It does not use any comparison operator or explicit join condition .
  - Outer join: A join that includes rows from one or both tables that do not have matching rows in the other table. There are three types of outer joins: left, right, and full   .
    - Left outer join: A join that includes all rows from the left table and only the matching rows from the right table   .
    - Right outer join: A join that includes all rows from the right table and only the matching rows from the left table   .
    - Full outer join: A join that includes all rows from both tables, regardless of whether they have matching rows in the other table   .

- The syntax for joins varies depending on the database system and the type of join. However, a general form of a join query is:

  ```sql
  SELECT column_list
  FROM table1 JOIN_TYPE table2
  ON join_condition;
  ```

  where `JOIN_TYPE` is one of the join types mentioned above, and `join_condition` is the expression that specifies how to match rows from both tables .

- Here is an example of a join query that uses the natural join type to combine data from two tables: `employees` and `departments`:

  ```sql
  SELECT employees.first_name, employees.last_name, departments.name
  FROM employees NATURAL JOIN departments;
  ```

  This query will return the first name, last name, and department name of each employee, assuming that both tables have a common attribute called `department_id`.

- Here is another example of a join query that uses the left outer join type to combine data from two tables: `customers` and `orders`:

  ```sql
  SELECT customers.customer_id, customers.name, orders.order_id, orders.total
  FROM customers LEFT OUTER JOIN orders
  ON customers.customer_id = orders.customer_id;
  ```

  This query will return the customer ID, name, order ID, and total of each customer and their orders, as well as the customers who have not placed any orders.



# Unions

- A union is a set operation that combines the results of two or more queries into one result set.
- A union can be used to retrieve data from more than one table simultaneously and then merge the results.
- A union requires that the queries involved have the same number of columns and that the corresponding columns have the same data type.
- A union eliminates any duplicate rows from the result set, unless the keyword ALL is used.
- A union can be expressed in relational algebra as R1 UNION R2, where R1 and R2 are union-compatible relations.
- A union can be expressed in SQL as SELECT * FROM R1 UNION SELECT * FROM R2, where R1 and R2 are union-compatible tables.



# Intersection

- Intersection is a relational algebra operation that returns the common tuples (rows) of two relations.
- The symbol for intersection is ∩.
- The two relations must be union-compatible, meaning they have the same number and type of attributes (columns).
- The result of intersection has the same schema (attribute names and types) as the input relations.
- Intersection can be expressed using set difference as follows: R1 ∩ R2 = R1 - (R1 - R2).
- Intersection is commutative, meaning R1 ∩ R2 = R2 ∩ R1.
- Intersection is associative, meaning (R1 ∩ R2) ∩ R3 = R1 ∩ (R2 ∩ R3).
- Intersection is idempotent, meaning R ∩ R = R.

## Example

Suppose we have two relations R and S with the following tuples:

| R | S |
|---|---|
| a | a |
| b | c |
| c | d |
| d | e |

Then, R ∩ S = {a, c, d}. The result has the same schema as R and S, and contains only the tuples that are present in both relations.



# Relational Data Model and Language

## Introduction

- A relational data model is a way of organizing data in a database into tables, also called relations.
- Each table consists of rows, also called tuples, and columns, also called attributes.
- Each table has a primary key, which is a column or a combination of columns that uniquely identifies each row.
- Tables can be linked by foreign keys, which are columns that refer to the primary key of another table.
- A relational database is a database that uses the relational model to store and manipulate data.
- A relational database may use SQL (Structured Query Language) as its language, but SQL is not the same as the relational model.
- SQL is a standard language for querying, updating, and managing data in relational databases.
- SQL has many dialects, such as MySQL, Oracle, PostgreSQL, SQLite, etc.

## Advantages of Relational Data Model and Language

- Relational data model and language are simple and intuitive to understand and use.
- Relational data model and language are based on mathematical logic and set theory, which provide a solid foundation for data integrity and consistency.
- Relational data model and language support data independence, which means that the physical structure of the data can be changed without affecting the logical structure of the data.
- Relational data model and language support data manipulation operations, such as selection, projection, join, union, intersection, difference, etc.
- Relational data model and language support data constraints, such as primary key, foreign key, not null, unique, etc, which ensure the validity and accuracy of the data.
- Relational data model and language support data security, which means that the access and modification of the data can be controlled by the database administrator.
- Relational data model and language support data optimization, which means that the performance and efficiency of the data processing can be improved by using indexes, views, triggers, stored procedures, etc.

## Disadvantages of Relational Data Model and Language

- Relational data model and language may not be suitable for complex or unstructured data, such as multimedia, documents, graphs, etc.
- Relational data model and language may not be able to handle large-scale or distributed data, such as big data, cloud data, etc.
- Relational data model and language may not be able to support real-time or dynamic data, such as streaming data, sensor data, etc.
- Relational data model and language may not be able to support concurrent or parallel data, such as multi-user, multi-thread, multi-core, etc.
- Relational data model and language may not be able to support flexible or heterogeneous data, such as schema-less, semi-structured, or mixed data types, etc.
- Relational data model and language may not be able to support advanced or specialized data, such as spatial, temporal, fuzzy, probabilistic, etc.



# Cursors

- A cursor is a database object that allows you to manipulate data in a row-by-row manner .
- A cursor can be used to perform operations such as retrieval, insertion, deletion, and update of data in a result set .
- A cursor can be declared by defining a SQL statement that returns a result set, and then assigning a name to the cursor .
- A cursor can be opened by executing the SQL statement and fetching the first row of the result set .
- A cursor can be moved to the next or previous row of the result set by using fetch commands .
- A cursor can be closed by releasing the result set and freeing the resources associated with the cursor .
- A cursor can be deallocated by removing the cursor definition from the database server .
- A cursor can be classified into different types based on the characteristics of the result set, such as static, dynamic, forward-only, scrollable, keyset-driven, etc  .
- A cursor can be useful when you need to process data in a sequential or conditional manner, or when you need to perform complex calculations or validations on data.
- A cursor can also have some disadvantages, such as performance overhead, concurrency issues, complexity, and resource consumption.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here are some triggers for the notes of the Unit 2 - Relational data Model and Language:

# Triggers for the notes of the Unit 2 - Relational data Model and Language

- Define the relational data model and its components: relation, attribute, tuple, domain, degree, cardinality, primary key, foreign key, etc.
- Explain the concept of relational integrity constraints: entity integrity, referential integrity, domain integrity, etc.
- Describe the relational algebra operations: select, project, union, set difference, Cartesian product, rename, join, division, etc. and give examples of each.
- Illustrate the use of relational algebra to express queries and manipulate data in a relational database.
- Define the relational calculus and its variants: tuple relational calculus and domain relational calculus.
- Compare and contrast the relational algebra and the relational calculus in terms of expressive power, procedural vs. declarative nature, and safe vs. unsafe queries.
- Explain the concept of views and their advantages and disadvantages in a relational database.
- Describe the SQL language and its components: data definition language (DDL), data manipulation language (DML), data control language (DCL), and data query language (DQL).
- Demonstrate the use of SQL to create, alter, and drop tables, indexes, views, and other database objects.
- Demonstrate the use of SQL to insert, update, delete, and query data in a relational database.
- Apply the SQL aggregate functions, group by clause, and having clause to perform complex queries and calculations on data.
- Use the SQL subqueries, joins, and set operations to combine data from multiple tables and relations.
- Explain the concept of null values and their implications for SQL queries and operations.
- Apply the SQL constraints, triggers, and stored procedures to enforce business rules and logic in a relational database.



# Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it cannot return a value directly like a function.
- A procedure can be invoked by other PL/SQL blocks, procedures, functions, triggers, or applications written in different languages such as Java, PHP, etc.
- A procedure can be created using the CREATE PROCEDURE statement, which has the following syntax:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype [DEFAULT expr],
  parameter2 [mode] datatype [DEFAULT expr],
  ...)]
IS | AS
  [local declarations]
BEGIN
  [executable statements]
[EXCEPTION
  [exception handlers]]
END [procedure_name];
```

- The CREATE OR REPLACE option allows to modify an existing procedure without dropping it.
- The procedure name must be unique within the schema and follow the naming rules of SQL identifiers.
- The parameters can be of three modes: IN, OUT, or IN OUT. The IN parameters are used to pass values to the procedure, the OUT parameters are used to return values from the procedure, and the IN OUT parameters are used to do both. The mode defaults to IN if not specified.
- The datatype of the parameters can be any valid PL/SQL datatype, such as NUMBER, VARCHAR2, DATE, BOOLEAN, etc. The DEFAULT option allows to assign a default value to the parameter if it is not passed by the caller.
- The IS or AS keyword marks the beginning of the procedure body, which consists of three optional sections: local declarations, executable statements, and exception handlers.
- The local declarations section is used to declare and initialize local variables, constants, cursors, and other PL/SQL constructs that are only visible within the procedure.
- The executable statements section is used to write the PL/SQL logic that performs the task of the procedure. It can include SQL statements, control structures, loops, assignments, calls to other subprograms, etc.
- The exception handlers section is used to handle any errors or exceptions that may occur during the execution of the procedure. It can include predefined or user-defined exceptions, and use the RAISE, RAISE_APPLICATION_ERROR, or PRAGMA EXCEPTION_INIT statements to raise or handle them.
- The END keyword marks the end of the procedure body, which can be optionally followed by the procedure name for clarity.

- To execute a procedure, it can be called by using the EXECUTE or EXEC command, or by using the procedure name followed by parentheses and the actual parameters, if any. For example:

```sql
EXECUTE adjust_salary(100, 10); -- using EXECUTE command
adjust_salary(100, 10); -- using procedure name
```

- To view the source code of a procedure, it can be queried from the USER_SOURCE, ALL_SOURCE, or DBA_SOURCE data dictionary views, depending on the privileges of the user. For example:

```sql
SELECT text FROM user_source
WHERE name = 'ADJUST_SALARY'
ORDER BY line;
```

- To drop a procedure, it can be deleted by using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE procedure_name;
```

- To modify a procedure, it can be altered by using the CREATE OR REPLACE PROCEDURE statement, which will replace the existing procedure with the new one. Alternatively, it can be dropped and recreated with the new code. For example:

```sql
CREATE OR REPLACE PROCEDURE adjust_salary
(emp_id IN NUMBER, percentage IN NUMBER)
IS
  new_salary NUMBER;
BEGIN
  SELECT salary * (1 + percentage/100) INTO new_salary
  FROM employees
  WHERE employee_id = emp_id;
  
  UPDATE employees
  SET salary = new_salary
  WHERE employee_id = emp_id;
  
  DBMS_OUTPUT.PUT_LINE('Salary adjusted for employee ' || emp_id);
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    RAISE_APPLICATION_ERROR(-20001, 'Invalid employee id');
END adjust_salary;
```



# Unit 3 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design and makes it easier to query, update, and maintain the data.
- There are several levels of normalization, each with a specific set of criteria that a table must satisfy to be in that normal form. The most common levels are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups of data and every column has a single value for each row.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key of the table.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key of the table and not on any other non-key column.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (a column or a set of columns that determines the value of another column) is a candidate key (a minimal set of columns that uniquely identifies a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and it has no multi-valued dependencies (a situation where a column or a set of columns depends on another column or a set of columns, and both are independent of the primary key).
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and it has no join dependencies (a situation where a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys without losing any information).
- Normalization is a progressive process, meaning that a higher level of normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization has many benefits, such as:
  - Eliminating data anomalies (inconsistencies or errors that occur when data is inserted, updated, or deleted).
  - Reducing data duplication and storage space.
  - Improving data consistency and accuracy.
  - Enhancing data security and integrity.
  - Facilitating data manipulation and analysis.
- Normalization also has some drawbacks, such as:
  - Increasing the number of tables and joins, which may affect the performance and complexity of queries.
  - Losing some information about the relationships between data, which may require additional constraints or business rules to enforce.
  - Requiring more effort and expertise to design and implement a normalized database.



# Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- Functional dependency is a constraint between two sets of attributes in a relation from a database.
- Functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- Functional dependency is denoted by an arrow, such as X → Y, which means that the value of Y is determined by the value of X.
- Functional dependency is an essential factor in designing database parameters and functions to help store and manage data.
- Functional dependency is used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity.
- There are four primary types of functional dependency :
  - Trivial functional dependency: A dependent is always a subset of the determinant, such as X → X or X → XY.
  - Non-trivial functional dependency: A dependent is strictly not a subset of the determinant, such as X → Y, where Y is not a part of X.
  - Multivalued functional dependency: A determinant can have more than one dependent, such as X → YZ, where Y and Z are independent of each other.
  - Transitive functional dependency: A dependent is indirectly determined by the determinant through another attribute, such as X → Y and Y → Z, which implies X → Z.
- Functional dependency can be used to check the normal forms of a relation, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
- Functional dependency can be used to decompose a relation into smaller relations that preserve the original information and satisfy the desired normal form.
- Functional dependency can be used to find the candidate keys, superkeys, and primary keys of a relation, which are the minimal sets of attributes that can uniquely identify a tuple.



# Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity. Normalization is the process of applying these rules to a database schema. There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are:

- **First Normal Form (1NF)**: A table is in 1NF if it does not contain any composite or multi-valued attributes. That is, each attribute should have a single atomic value and each row should have a unique identifier (primary key).
- **Second Normal Form (2NF)**: A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there should be no partial dependencies, where an attribute depends on only a part of the primary key.
- **Third Normal Form (3NF)**: A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there should be no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.
- **Boyce-Codd Normal Form (BCNF)**: A table is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there should be no non-trivial functional dependencies, where a non-key attribute determines another non-key attribute.

The following table shows an example of a table that is not in any normal form and how it can be normalized to different levels:

| Student ID | Name | Course ID | Course Name | Instructor |
|------------|------|-----------|-------------|------------|
| 101        | Alice | CS101     | Programming | Bob        |
| 101        | Alice | CS102     | Data Structures | Carol     |
| 102        | Bob   | CS101     | Programming | Bob        |
| 102        | Bob   | CS103     | Algorithms  | Dave       |
| 103        | Carol | CS102     | Data Structures | Carol     |
| 103        | Carol | CS103     | Algorithms  | Dave       |

This table is not in 1NF because it has a composite attribute (Course ID, Course Name, Instructor) and a multi-valued attribute (Course ID). To convert it to 1NF, we need to split the composite attribute into separate attributes and create a new table for the multi-valued attribute. The result is:

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Student ID | Course ID |
|------------|-----------|
| 101        | CS101     |
| 101        | CS102     |
| 102        | CS101     |
| 102        | CS103     |
| 103        | CS102     |
| 103        | CS103     |

| Course ID | Course Name | Instructor |
|-----------|-------------|------------|
| CS101     | Programming | Bob        |
| CS102     | Data Structures | Carol     |
| CS103     | Algorithms  | Dave       |

This table is in 1NF but not in 2NF because the attributes Course Name and Instructor are partially dependent on the primary key Course ID. To convert it to 2NF, we need to remove the partial dependencies and create a new table for the non-key attributes. The result is:

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Student ID | Course ID |
|------------|-----------|
| 101        | CS101     |
| 101        | CS102     |
| 102        | CS101     |
| 102        | CS103     |
| 103        | CS102     |
| 103        | CS103     |

| Course ID | Course Name |
|-----------|-------------|
| CS101     | Programming |
| CS102     | Data Structures |
| CS103     | Algorithms  |

| Course Name | Instructor |
|-------------|------------|
| Programming | Bob        |
| Data Structures | Carol     |
| Algorithms  | Dave       |

This table is in 2NF but not in 3NF because the attribute Instructor is transitively dependent on the primary



# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its rules.
  - Ensure data integrity, consistency, and quality.
  - Support efficient data access and manipulation.
  - Facilitate data security and privacy.
  - Allow for data scalability and maintainability.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization helps in achieving the following benefits :
  - Improved database design: Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.
  - Reduced data anomalies: Normalization helps in avoiding data anomalies, such as insertion, deletion, and update anomalies, that can occur due to data redundancy and inconsistency. Normalization ensures that each piece of data is stored in only one place, and that any changes to the data are reflected in all the related tables.
  - Enhanced data security: Normalization helps in enhancing data security by allowing for more granular access control and auditing. Normalization allows for defining different levels of permissions and privileges for different tables and columns, and for tracking the changes made to the data by different users.
  - Increased data efficiency: Normalization helps in increasing data efficiency by reducing the storage space and improving the performance of data operations. Normalization eliminates the need to store duplicate data, and thus saves disk space and memory. Normalization also simplifies the queries and transactions, and thus reduces the network traffic and processing time.

## Normal Forms
- Normal forms are the rules or standards that define the degree of normalization of a database schema.
- Normal forms are based on the concept of functional dependencies, which are the relationships between the attributes of a table that determine how one attribute can be derived from another attribute or a set of attributes.
- Normal forms are applied sequentially, starting from the lowest level (first normal form) to the highest level (fifth normal form), to progressively reduce the redundancy and dependency of data in a database schema.
- The most commonly used normal forms are  :
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, i.e., each attribute can have only one value for each record, and there are no repeating groups of attributes, i.e., each record can have only one instance of each attribute.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., each non-key attribute can be uniquely identified by the primary key, and not by any subset of the primary key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., each non-key attribute can be uniquely identified by the primary key, and not by any other non-key attribute or a set of non-key attributes.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., each attribute or a set of attributes that can determine the value of another attribute or a set of attributes is a potential primary key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and it has no multi-valued dependencies, i.e., there are no attributes or a set of attributes that can have more than one value for a single record, and that are independent of the primary key.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and it has no join dependencies, i.e., there are no subsets of attributes that can be joined together to form the original table, and that are not implied



# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and storage formats.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, insertion, update, and deletion of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Scalability: The database should be able to accommodate the growth and changes in the data volume and complexity, without compromising the performance or functionality.
  - Maintainability: The database should be easy to modify, debug, and enhance, without affecting the existing functionality or data quality.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity and organization of data.
- Normalization also helps to avoid the following problems that may arise from a poorly designed schema:
  - Anomalies: Inconsistencies or errors in the data that occur due to the duplication or omission of data in different tables.
  - Update anomalies: When a change in one table is not reflected in another table, leading to data inconsistency or loss.
  - Insertion anomalies: When a new record cannot be inserted into a table without violating some constraint or creating redundant data.
  - Deletion anomalies: When deleting a record from a table causes the loss of related data in another table.
- Normalization is based on the concept of functional dependency, which is a relationship between two sets of attributes, such that the value of one set determines the value of the other set.
- Normalization applies a series of rules or normal forms to a schema, each of which reduces the degree of redundancy and dependency in the schema.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute has a single value for each record.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, or in other words, there are no transitive dependencies between non-key attributes.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, or in other words, there are no partial dependencies between candidate keys and non-key attributes.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies, or in other words, there are no non-key attributes that depend on a subset of a composite key.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, or in other words, it cannot be decomposed into smaller tables without losing information.



# Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- 3NF was originally defined by E. F. Codd in 1971.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two non-prime attributes, such that one non-prime attribute determines another non-prime attribute through the primary key.
- For example, consider a table with the following attributes: Student_ID, Student_Name, Course_ID, Course_Name, Instructor_ID, Instructor_Name.
  - The primary key is (Student_ID, Course_ID).
  - The non-prime attributes are Student_Name, Course_Name, Instructor_ID, Instructor_Name.
  - There is a transitive dependency between Course_ID and Instructor_ID, because Course_ID determines Instructor_ID through the primary key.
  - There is also a transitive dependency between Instructor_ID and Instructor_Name, because Instructor_ID determines Instructor_Name.
  - To convert this table to 3NF, we need to remove the transitive dependencies by creating separate tables for Course and Instructor, as shown below:

| Student_ID | Student_Name | Course_ID |
|------------|--------------|-----------|
| S001       | Alice        | C001      |
| S002       | Bob          | C002      |
| S003       | Charlie      | C001      |
| S004       | David        | C003      |

| Course_ID | Course_Name | Instructor_ID |
|-----------|-------------|---------------|
| C001      | Database    | I001          |
| C002      | Programming | I002          |
| C003      | Math        | I003          |

| Instructor_ID | Instructor_Name |
|---------------|-----------------|
| I001          | John            |
| I002          | Mary            |
| I003          | Peter           |

- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the 3NF.
  - The 3NF always ensures functional dependency preserving and lossless decomposition.
  - The 3NF reduces the storage space and improves the performance of the queries.
  - The 3NF makes the database more consistent and easier to maintain.



# BCNF

BCNF stands for Boyce-Codd Normal Form. It is a form of database normalization that ensures that there are no anomalies or redundancies in the data. BCNF is a stricter version of 3NF (Third Normal Form), which requires that every non-prime attribute is fully functionally dependent on the primary key, and that there are no transitive dependencies.

A table is in BCNF if and only if for every functional dependency X -> Y, X is a superkey of the table. A superkey is a set of attributes that uniquely identifies a tuple in the table. A candidate key is a minimal superkey, meaning that no proper subset of it is a superkey. A primary key is a chosen candidate key that is used to refer to the tuples in the table.

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

This table is not in BCNF, because the functional dependency Instructor ID -> Instructor Name violates the condition. The left-hand side, Instructor ID, is not a superkey, as it is a proper subset of the candidate keys.

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

The first table has the same candidate keys as the original table, and the only functional dependency is Student ID, Course ID -> Instructor ID, Grade, which satisfies the BCNF condition. The second table has Instructor ID as the only candidate key and the only functional dependency is Instructor ID -> Instructor Name, which also satisfies the BCNF condition.

## Advantages of BCNF

Some of the advantages of BCNF are:

- It reduces data redundancy and duplication, as the same information is not stored in multiple tables.
- It improves data integrity and consistency, as any update, insertion, or deletion of data does not cause anomalies or inconsistencies.
- It simplifies the queries and joins, as the tables are smaller and more normalized.



# Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that specifies that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency is less prevalent than functional dependency, join dependency and multivalued dependency .
- Inclusion dependency can be represented by the notation R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], which means that the columns A1, A2, ..., An of relation R are a subset of the columns B1, B2, ..., Bn of relation S  .
- Inclusion dependency can be checked by performing a natural join of the two relations and comparing the result with the relation on the left-hand side of the IND.
- Inclusion dependency can be enforced by creating a foreign key constraint on the columns of the relation on the left-hand side of the IND and referencing the columns of the relation on the right-hand side of the IND.
- Inclusion dependency can be violated if a tuple is inserted or updated in the relation on the left-hand side of the IND that does not match any tuple in the relation on the right-hand side of the IND.
- Inclusion dependency can be satisfied if a tuple is deleted or updated in the relation on the right-hand side of the IND that does not affect any tuple in the relation on the left-hand side of the IND.
- Inclusion dependency can be useful for modeling subtyping, inheritance, generalization and specialization in object-oriented and entity-relationship databases.



# Lossless Join Decomposition

- Lossless join decomposition is a process of splitting a relation R into two or more relations R1, R2, ... such that the natural join of the smaller relations gives back the original relation R.
- Lossless join decomposition is important for database design and normalization, as it helps to remove redundancy and anomalies from the database while preserving the original data .
- A decomposition of R into R1 and R2 is lossless if and only if one of the following functional dependencies holds in the closure of the set of functional dependencies F of R :
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
- The above condition can be checked using Armstrong's axioms or by constructing a table with the attributes of R as columns and the attributes of R1 and R2 as rows. The table is then filled with the values of R1 and R2, and the natural join of R1 and R2 is obtained by combining the rows with the same values in the common attributes.
- Lossless join decomposition can be achieved by using decomposition algorithms such as BCNF or 3NF, which ensure that the decomposed relations are in a higher normal form and satisfy the lossless join property.



# Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Normal forms are defined based on the concept of functional dependencies (FDs).

A functional dependency (FD) for a relation R is a formula of the form X -> Y, where X and Y are sets of attributes of R. It means that the values of Y are determined by the values of X. In other words, two tuples in R that have the same values for X must also have the same values for Y.

For example, in a relation R(A, B, C, D), the FD A -> B means that the value of B depends on the value of A. If two tuples in R have the same value for A, they must also have the same value for B.

There are different types of FDs, such as trivial, full, partial, and transitive. A trivial FD is one where Y is a subset of X, such as A -> A. A full FD is one where Y is not a subset of X, and X is a candidate key of R, such as A -> B. A partial FD is one where Y is not a subset of X, and X is not a candidate key of R, but a proper subset of a candidate key, such as AB -> C. A transitive FD is one where Y is not a subset of X, and there exists another attribute Z such that X -> Z and Z -> Y, such as A -> B and B -> C.

Normalization using FDs involves applying a series of rules or tests to check whether a relation satisfies a certain normal form, and if not, how to decompose it into smaller relations that do. The most common normal forms are:

- First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. That is, each attribute value is atomic and indivisible.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and has no partial FDs. That is, each non-key attribute is fully dependent on the whole primary key.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and has no transitive FDs. That is, each non-key attribute is directly dependent on the primary key, and not on any other non-key attribute.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and has no non-trivial FDs that violate the key constraint. That is, each attribute is fully dependent on a candidate key, and not on any other attribute.

The process of normalization using FDs can be summarized as follows:

- Start with a relation R and a set of FDs F that hold on R.
- Check whether R is in BCNF. If yes, stop. If no, find a non-trivial FD X -> Y that violates the key constraint, and decompose R into two relations: R1 = (X, Y) and R2 = (R - Y) + X. Preserve the FDs that hold on R1 and R2, and add any new FDs that are implied by F.
- Repeat step 2 for each relation until all relations are in BCNF.

The benefits of normalization using FDs are:

- It reduces data redundancy and storage space.
- It eliminates update, insertion, and deletion anomalies that may cause data inconsistency.
- It improves data integrity and query efficiency.



# MVD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- MVD stands for **Multivalued Dependency**, which is a type of constraint between two sets of attributes in a relation.
- MVD means that for a single value of attribute A, multiple values of attribute B exist. For example, if a person has multiple hobbies and works on multiple projects, then there is a MVD between the person and the hobbies, and between the person and the projects.
- MVD is written as A --> --> B, which means A is multivalued dependent on B. This implies that the values of B are independent of each other for a given value of A.
- MVD plays a role in the **4NF** (Fourth Normal Form) database normalization, which is a process of reducing redundancy and anomalies in a database.
- 4NF requires that a relation should be in **BCNF** (Boyce-Codd Normal Form) and should not contain any MVD. BCNF is a stricter form of **3NF** (Third Normal Form), which requires that every determinant should be a candidate key.
- To check if a relation is in 4NF, we need to identify all the MVDs in the relation and verify that they are trivial or implied by the candidate keys. A MVD is trivial if B is a subset of A, or A and B together form the whole relation. A MVD is implied by the candidate keys if A is a superkey.
- To convert a relation into 4NF, we need to decompose it into smaller relations that do not contain any MVD. This can be done by applying the BCNF algorithm and replacing the MVDs as FDs (Functional Dependencies). The decomposition should preserve the dependencies and the data.



# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its information needs.
  - Ensure data integrity, consistency, and quality.
  - Minimize data redundancy and duplication.
  - Optimize data access and performance.
  - Facilitate data maintenance and evolution.
- Database design follows a top-down or bottom-up approach, depending on the level of abstraction and detail required.
  - Top-down approach: Starts with a conceptual model that captures the high-level concepts and relationships, and then refines it into a logical model that specifies the data types and constraints, and finally translates it into a physical model that defines the storage and implementation details.
  - Bottom-up approach: Starts with a physical model that reflects the existing data sources and structures, and then abstracts it into a logical model that generalizes the data types and constraints, and finally creates a conceptual model that summarizes the main concepts and relationships.
- Database design can use different data models to represent the data and its structure, such as:
  - Relational model: Represents data as tables (relations) with rows (tuples) and columns (attributes), and defines relationships and constraints using primary keys, foreign keys, and referential integrity rules.
  - Hierarchical model: Represents data as a tree-like structure with nodes (records) and links (pointers), and defines relationships and constraints using parent-child and ancestor-descendant associations.
  - Network model: Represents data as a graph-like structure with nodes (records) and links (pointers), and defines relationships and constraints using owner-member and set associations.
  - Entity-relationship model: Represents data as a set of entities and relationships, and defines attributes and constraints using entity types, relationship types, and cardinality ratios.
  - Object-oriented model: Represents data as a collection of objects and classes, and defines attributes and constraints using inheritance, encapsulation, and polymorphism.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization also helps to improve the database design by ensuring the following properties:
  - Atomicity: Each attribute value is indivisible and cannot be further decomposed.
  - Consistency: Each attribute value conforms to a predefined domain and format.
  - Uniqueness: Each row in a table can be uniquely identified by a primary key or a combination of attributes.
  - Non-redundancy: Each attribute value is stored only once and can be derived from other attributes if needed.
  - Dependency preservation: Each functional dependency between attributes is preserved in the normalized schema.
  - Lossless decomposition: No information is lost or added when splitting or joining tables.
- Normalization is based on the concept of functional dependency, which is a relationship between two sets of attributes, such that the value of one set determines the value of the other set.
- Normalization applies a series of rules or normal forms to check and eliminate the anomalies or problems caused by functional dependencies, such as:
  - First normal form (1NF): Eliminates repeating groups or multivalued attributes by ensuring that each attribute value is atomic and unique within a row.
  - Second normal form (2NF): Eliminates partial dependencies by ensuring that each non-key attribute depends on the whole primary key and not on a subset of it.
  - Third normal form (3NF): Eliminates transitive dependencies by ensuring that each non-key attribute depends only on the primary key and not on any other non-key attribute.
  - Boyce-Codd normal form (BCNF): Eliminates non-trivial dependencies by ensuring that each determinant is a candidate key or a superkey.
  - Fourth normal form (4NF): Eliminates multivalued dependencies by ensuring that each attribute depends on the primary key and not on any other attribute or set of attributes.
  - Fifth normal form (5NF): Eliminates join dependencies by ensuring that each table is irreducible and cannot be further decomposed without losing information.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on alternative approaches to database design for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System.

# Alternative Approaches to Database Design

- Database design is the process of defining the structure, organization, and relationships of data in a database.
- Database design can be influenced by various factors, such as the application requirements, the data characteristics, the performance goals, and the available tools and techniques.
- There are different approaches to database design, each with its own advantages and disadvantages. Some of the common approaches are:

## Top-Down Approach

- The top-down approach starts with a high-level conceptual model of the data, such as an entity-relationship diagram (ERD), and then refines it into a logical model, such as a relational schema, and finally into a physical model, such as a set of tables and indexes.
- The top-down approach is useful for capturing the overall business requirements and ensuring consistency and completeness of the data model.
- The top-down approach can also facilitate communication and collaboration among the stakeholders, such as the users, analysts, and developers.
- However, the top-down approach can be time-consuming and rigid, as it requires a lot of upfront planning and analysis, and may not accommodate changes easily.

## Bottom-Up Approach

- The bottom-up approach starts with a low-level physical model of the data, such as a set of tables and indexes, and then abstracts it into a logical model, such as a relational schema, and finally into a conceptual model, such as an ERD.
- The bottom-up approach is useful for exploiting the existing data sources and optimizing the performance and efficiency of the database.
- The bottom-up approach can also adapt to changes quickly and incrementally, as it does not rely on a predefined data model.
- However, the bottom-up approach can be difficult and complex, as it requires a lot of reverse engineering and integration, and may not capture the business requirements and semantics of the data.

## Agile Approach

- The agile approach is a hybrid of the top-down and bottom-up approaches, which aims to deliver a database design that is both user-centric and data-driven.
- The agile approach follows an iterative and incremental process, where the database design is developed and refined through a series of cycles, each involving user feedback, data analysis, and prototyping.
- The agile approach is useful for handling complex and dynamic data requirements, as it allows for flexibility and experimentation, and delivers value and functionality in short time frames.
- However, the agile approach can be challenging and risky, as it requires a high level of collaboration and coordination, and may compromise the quality and consistency of the database design.

## Alternative Techniques

- Besides the traditional relational database design, there are also alternative techniques that can be used to design a database, such as:

### Normalization

- Normalization is a technique that organizes the data in a database into tables that are free of redundancy and dependency, and that follow certain rules or normal forms.
- Normalization is useful for ensuring the integrity, consistency, and accuracy of the data, as well as facilitating the manipulation and maintenance of the data.
- However, normalization can also introduce some drawbacks, such as increased complexity, reduced performance, and loss of information.

### Denormalization

- Denormalization is a technique that reverses the effects of normalization, by introducing some redundancy and dependency into the data, such as by combining or splitting tables, or adding derived or duplicate columns.
- Denormalization is useful for improving the performance, efficiency, and usability of the database, as well as simplifying the queries and operations on the data.
- However, denormalization can also introduce some drawbacks, such as decreased integrity, consistency, and accuracy of the data, as well as complicating the manipulation and maintenance of the data.

### NoSQL

- NoSQL is a term that refers to a variety of non-relational database systems that store and manage data in different ways, such as by using documents, graphs, key-value pairs, or columns.
- NoSQL is useful for handling large, diverse, and unstructured data sets, as well as supporting scalability, availability, and flexibility of the database.
- However, NoSQL can also introduce some drawbacks, such as lack of standardization, compatibility, and security, as well as trade-offs between consistency and availability of the data.



# Unit 4 - Transaction Processing Concept

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database or a file system .
- A **transaction processing system (TPS)** is a software system that executes transactions and ensures that they are completed correctly and reliably.
- A transaction has four main properties, known as **ACID** :
  - **Atomicity**: A transaction must either be executed in its entirety or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction must preserve the integrity and validity of the database. It must not violate any integrity constraints or business rules.
  - **Isolation**: A transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only one in the system.
  - **Durability**: A transaction must ensure that its effects are permanent and persistent, even in the event of system failures or power outages.
- A transaction can have one of the following outcomes:
  - **Commit**: The transaction is successfully completed and its changes are made permanent in the database.
  - **Rollback**: The transaction is aborted and its changes are undone in the database.
  - **Partial commit**: The transaction is partially completed and some of its changes are made permanent in the database. This is an undesirable outcome that violates atomicity and consistency.
- A transaction can be executed in different modes, depending on the level of isolation and concurrency control required:
  - **Serial**: The transactions are executed one after another, in a sequential order. This mode ensures the highest level of isolation and consistency, but reduces the system throughput and performance.
  - **Parallel**: The transactions are executed simultaneously, in an overlapping or interleaved order. This mode improves the system throughput and performance, but may cause conflicts and inconsistencies among transactions.
  - **Mixed**: The transactions are executed in a combination of serial and parallel modes, depending on the degree of conflict and dependency among transactions. This mode balances the trade-off between isolation and concurrency, but requires more complex algorithms and protocols to manage transactions.



# Transaction System

A transaction system is a system that processes and records the daily transactions of a business or an organization. A transaction is a single unit of work or logic that involves one or more operations on a database, such as inserting, updating, deleting, or querying data. A transaction system ensures that the transactions are performed in a consistent, reliable, and atomic way, meaning that either all the operations in a transaction are completed successfully or none of them are. A transaction system also ensures that the transactions are isolated from each other, meaning that they do not interfere with each other's effects on the database. A transaction system also maintains the integrity and security of the database by enforcing rules and constraints on the data and preventing unauthorized access or modification.

Some examples of transaction systems are:

- CRM (customer relationship management) systems, which store and manage information about customers, such as their contact details, preferences, purchase history, feedback, etc.
- HRM (human resources management) systems, which store and manage information about employees, such as their personal details, qualifications, performance, attendance, payroll, benefits, etc.
- ERP (enterprise resource planning) systems, which integrate and coordinate various business functions, such as accounting, inventory, production, sales, marketing, etc.

A transaction system typically uses a database management system (DBMS) as the underlying software tool to store, access, and manipulate the data in the database. A DBMS is a software tool that enables users to perform various actions on a database, such as defining the database schema, creating tables and indexes, inserting and retrieving data, executing queries and commands, etc. A DBMS also provides features and functions to support transaction management, such as concurrency control, locking, logging, recovery, backup, etc.

Some examples of DBMS are:

- MySQL, which is an open-source, relational DBMS that uses the SQL (structured query language) as the standard language for interacting with the database.
- MongoDB, which is an open-source, non-relational (or NoSQL) DBMS that uses JSON (JavaScript object notation) as the format for storing and exchanging data.
- Oracle, which is a proprietary, relational DBMS that offers advanced features and capabilities for enterprise-level applications and transactions.



# Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to some serial schedule, where the transactions are executed one after the other without any interleaving of operations.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stronger notion of serializability that requires that the order of any two conflicting operations (read or write on the same data item) in the schedule is the same as the order in some serial schedule.
- View serializability is a weaker notion of serializability that requires that the read and write operations of each transaction in the schedule have the same effect as in some serial schedule, but the order of the operations may differ.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph or a precedence graph is a directed graph of the transactions in a schedule, where an edge from transaction Ti to transaction Tj indicates that Ti must precede Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its serialization graph is acyclic, meaning that it does not contain any cycles or loops.
- A schedule is view serializable if and only if it is conflict serializable or it can be transformed into a conflict serializable schedule by swapping non-conflicting operations.
- To construct a serialization graph for a given schedule, we follow these steps:
  - Create a node for each transaction in the schedule.
  - For each pair of transactions Ti and Tj, where i < j, draw an edge from Ti to Tj if one of the following conditions holds:
    - Ti performs a write operation on some data item X and Tj performs a read or write operation on X later in the schedule.
    - Ti performs a read operation on some data item X and Tj performs a write operation on X later in the schedule.
  - Check if the graph contains any cycles. If yes, the schedule is not conflict serializable. If no, the schedule is conflict serializable and the topological order of the nodes in the graph is a serial schedule equivalent to the given schedule.
- To check if a schedule is view serializable, we follow these steps:
  - Check if the schedule is conflict serializable by constructing its serialization graph. If yes, the schedule is view serializable and the serial schedule is the same as the conflict serializable schedule.
  - If the schedule is not conflict serializable, try to swap non-conflicting operations in the schedule to eliminate cycles in the serialization graph. If this is possible, the schedule is view serializable and the serial schedule is the one obtained after the swapping. If this is not possible, the schedule is not view serializable.



# Serializability of Schedules

- A schedule is a sequence of operations performed by one or more transactions on a database.
- A schedule is serial if it executes one transaction at a time, without any interleaving of operations from different transactions.
- A schedule is non-serial if it allows concurrent execution of two or more transactions, with some interleaving of operations from different transactions.
- A schedule is serializable if it is equivalent to some serial schedule with the same transactions.
- Serializability is a desirable property of a schedule, as it ensures the consistency and isolation of transactions.
- There are two main methods to check the serializability of a schedule: conflict serializability and view serializability.

## Conflict Serializability

- Two operations in a schedule are said to conflict if they belong to different transactions, access the same data item, and at least one of them is a write operation.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Conflict serializability can be tested by constructing a precedence graph (or serializability graph) for the given schedule.
- A precedence graph is a directed graph where the nodes represent the transactions and the edges represent the conflicts between them.
- An edge from Ti to Tj means that Ti must precede Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.

## View Serializability

- A schedule is view serializable if it is view equivalent to some serial schedule with the same transactions.
- Two schedules are view equivalent if they satisfy the following conditions:
  - For each data item, the same transaction reads its initial value in both schedules.
  - For each data item, the same transaction writes its final value in both schedules.
  - For each data item, the set of transactions that read the value written by a transaction is the same in both schedules.
- View serializability is a more general notion than conflict serializability, as it allows some schedules that are not conflict serializable.
- View serializability can be tested by constructing a polygraph (or view graph) for the given schedule.
- A polygraph is a directed graph where the nodes represent the transactions and the edges represent the view dependencies between them.
- An edge from Ti to Tj means that Ti must precede Tj in any serial schedule view equivalent to the given schedule.
- A schedule is view serializable if and only if its polygraph is acyclic.



# Conflict & View Serializable Schedule

## Introduction

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if each transaction in it is executed one after another without any interleaving of operations.
- A schedule is non-serial if the operations of different transactions are interleaved.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

## Conflict Serializability

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

- The schedule S is not serial, but it is conflict serializable because it can be transformed into a serial schedule S' by swapping the non-conflicting operations R(B) and W(B) of T1 with R(B) and W(B) of T2:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
|     | R(B) |
|     | W(B) |

- The schedule S' is serial and equivalent to S in terms of the final state of the database.

## View Serializability

- View serializability is another property of a schedule that ensures the consistency of the database.
- A schedule is view serializable if it is view equivalent to some serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item.
  - They have the same final write operations on each data item.
  - They have the same set of read operations on each data item that read the same value written by the same transaction.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(A) |
|     | W(A) |
| R(B) |    |
| W(B) |    |

- The schedule S is not serial, but it is view serializable because it is view equivalent to a serial schedule S' that executes T1 followed by T2:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(A) |
|     | W(A) |

- The schedule S' is serial and view equivalent to S in terms of the initial reads, final writes, and read-write dependencies.

## Summary

- Conflict serializability and view serializability are two types of serializability that ensure the consistency of the database when concurrent transactions are executed.
- Conflict serializability is based on the order of conflicting operations, while view serializability is based on the effect of read and write operations on the database state.
- Every conflict serializable schedule is also view serializable, but the converse is not true.



# Recoverability

Recoverability is a concept in database management systems (DBMS) that refers to the ability of a system to restore the database to a consistent state after a transaction failure or system crash. Recoverability is important for ensuring the integrity and reliability of the data stored in the database.

A transaction is a logical unit of work that consists of a sequence of operations on the database. A transaction can either commit, which means it successfully completes all its operations and makes its changes permanent, or abort, which means it fails to complete and undoes its changes.

A schedule is a sequence of operations from one or more transactions that are executed by the DBMS. A schedule can be classified into different types based on the order of operations and the commit or abort status of the transactions involved.

## Recoverable Schedules

A schedule is recoverable if no transaction in the schedule commits before all the transactions whose changes it has read commit. In other words, a schedule is recoverable if there is no dirty read, which is a situation where a transaction reads a data item that has been modified by another transaction that has not yet committed.

Recoverable schedules ensure that if a transaction aborts, it will not affect the outcome of any other transaction that has committed. Recoverable schedules are desirable because they prevent the loss of committed data and avoid cascading aborts, which are situations where the abort of one transaction causes the abort of other transactions that have read its changes.

Example:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(B) |
| W(A) |    |
|    | W(B) |
| C |    |
|    | C |

This schedule is recoverable because T1 commits after reading A and T2 commits after reading B, and both A and B are written by committed transactions.

## Non-recoverable Schedules

A schedule is non-recoverable if there is at least one transaction in the schedule that commits before all the transactions whose changes it has read commit. In other words, a schedule is non-recoverable if there is at least one dirty read.

Non-recoverable schedules are problematic because they can lead to inconsistent states of the database if a transaction that has been read by another transaction aborts. Non-recoverable schedules can also cause cascading aborts, which can affect the performance and availability of the system.

Example:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(A) |
| W(A) |    |
|    | C |
| A |    |

This schedule is non-recoverable because T2 commits after reading A, which is written by T1, and T1 aborts. This means that T2 has committed a change that is based on an invalid value of A, and the database is in an inconsistent state. Moreover, T2 has to abort as well, causing a cascading abort.



# Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations.
- A transaction failure can be caused by various reasons, such as system crash, power failure, user error, deadlock, concurrency control violation, or integrity constraint violation.
- To recover from transaction failure, the atomicity and durability of transactions as a whole must be maintained. That is, either all the operations are executed or none, and the effects of committed transactions are preserved even in the presence of failures.
- There are three states of database recovery in DBMS:
  - Consistent state: A state where the database satisfies all the integrity constraints and reflects a correct state of the real world.
  - Inconsistent state: A state where the database violates some integrity constraints or does not reflect a correct state of the real world.
  - Intermediate state: A state where the database is in the process of executing a transaction and has not reached a consistent state yet.
- There are two types of database recovery in DBMS:
  - Crash recovery: This type of recovery occurs when the DBMS or the system crashes due to hardware or software failure. The DBMS must restore the database to a consistent state by undoing the effects of incomplete transactions and redoing the effects of committed transactions.
  - Media recovery: This type of recovery occurs when the database is damaged due to physical errors, such as disk failure, fire, or theft. The DBMS must restore the database to a consistent state by using backup copies of the database and the transaction log.
- There are various recovery techniques in DBMS that use different methods to record and restore the changes made by transactions. Some of the common recovery techniques are  :
  - Deferred update: This technique delays the actual update of the database until the transaction commits. It uses a transaction log to record the changes made by transactions. To recover from a failure, the DBMS scans the log forward and redoes the updates of committed transactions.
  - Immediate update: This technique allows the actual update of the database before the transaction commits. It also uses a transaction log to record the changes made by transactions. To recover from a failure, the DBMS scans the log backward and undoes the updates of uncommitted transactions, and then scans the log forward and redoes the updates of committed transactions.
  - Shadow paging: This technique uses two copies of the database: the current page table and the shadow page table. The current page table points to the pages that are being updated by transactions, while the shadow page table points to the pages that are not updated yet. To recover from a failure, the DBMS discards the current page table and uses the shadow page table as the database.
  - Checkpointing: This technique periodically saves the state of the database and the transaction log to a stable storage. A checkpoint is a point in time when the database and the log are consistent. To recover from a failure, the DBMS only needs to scan the log from the last checkpoint and apply the appropriate actions.



# Log Based Recovery

Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash. It involves the use of transaction logs, which are records of all the transactions performed on the database.

## Advantages of Log Based Recovery

- It provides the ability to maintain or recover data in case of system failure.
- It ensures the atomicity and durability properties of transactions.
- It allows the database to be restored to a consistent state without losing any committed changes.

## Types of Log Based Recovery

There are two main types of log based recovery: undo logging and redo logging.

### Undo Logging

Undo logging is a type of log based recovery that uses the log records to undo the changes made by transactions that did not commit before the failure. It is also known as backward recovery or rollback.

The steps involved in undo logging are:

- Scan the log file backwards from the end to the most recent checkpoint.
- For each log record <Tn, X, V1, V2>, where Tn is the transaction id, X is the data item, V1 is the old value and V2 is the new value, do the following:
  - If the log record is <Tn, commit>, then mark Tn as committed.
  - If the log record is <Tn, start>, then check if Tn is marked as committed. If not, then add Tn to the undo list.
  - If the log record is <Tn, X, V1, V2>, then check if Tn is in the undo list. If yes, then restore the old value of X by writing V1 to the database.
- Write an end record to the log file and flush it to the stable storage.

### Redo Logging

Redo logging is a type of log based recovery that uses the log records to redo the changes made by transactions that committed before the failure. It is also known as forward recovery or rollforward.

The steps involved in redo logging are:

- Scan the log file forward from the most recent checkpoint to the end.
- For each log record <Tn, X, V1, V2>, where Tn is the transaction id, X is the data item, V1 is the old value and V2 is the new value, do the following:
  - If the log record is <Tn, start>, then mark Tn as active.
  - If the log record is <Tn, commit>, then mark Tn as committed and add Tn to the redo list.
  - If the log record is <Tn, X, V1, V2>, then check if Tn is in the redo list. If yes, then restore the new value of X by writing V2 to the database.
- Write an end record to the log file and flush it to the stable storage.

## Example of Log Based Recovery

Consider the following transactions and log records:

| Transaction | Operation |
| ----------- | --------- |
| T1          | Read(A)   |
| T1          | A = A + 100 |
| T1          | Write(A)  |
| T2          | Read(B)   |
| T2          | B = B - 50 |
| T2          | Write(B)  |
| T1          | Commit    |
| T2          | Read(C)   |
| T2          | C = C + 50 |
| T2          | Write(C)  |

| Log Record | Meaning |
| ---------- | ------- |
| <T1, start> | Transaction T1 starts |
| <T1, A, 500, 600> | Transaction T1 updates A from 500 to 600 |
| <T2, start> | Transaction T2 starts |
| <T2, B, 400, 350> | Transaction T2 updates B from 400 to 350 |
| <T1, commit> | Transaction T1 commits |
| <T2, C, 300, 350> | Transaction T2 updates C from 300 to 350 |

Assume that the system crashes after writing the last log record and before writing the commit record for T2. The database state before the crash is:

| Data Item | Value |
| ---------



# Checkpoints for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A transaction is a logical unit of work that represents a real-world event of data processing.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either executes all or none of its operations.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it is the only one in the system, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.
- A transaction can have one of the following states: active, partially committed, committed, failed, or aborted.
- A transaction begins in the active state, where it executes its operations.
- A transaction enters the partially committed state when it issues a commit request, indicating that it has completed its operations successfully.
- A transaction enters the committed state when the commit request is confirmed by the system, and the changes made by the transaction are recorded in the database.
- A transaction enters the failed state when it encounters an error or aborts due to some reason, such as a deadlock or a violation of an integrity constraint.
- A transaction enters the aborted state when it is rolled back by the system, undoing any changes it has made to the database.
- A transaction can be rolled back either partially or fully, depending on how much of its operations have been executed and recorded in the database.
- A transaction can be restarted after being aborted, if the reason for the abort is transient and can be resolved.
- A transaction can be serialized if its operations can be ordered in such a way that the outcome of executing them is equivalent to executing them one at a time.
- A schedule is a sequence of operations from a set of concurrent transactions.
- A schedule is serializable if it is equivalent to a serial schedule, where the transactions are executed one after the other in some order.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations, where two operations conflict if they belong to different transactions and access the same data item, and at least one of them is a write operation.
- A schedule is view serializable if it is equivalent to a serial schedule in terms of the read and write operations on each data item, regardless of the order of non-conflicting operations.
- A schedule is recoverable if no transaction commits before all the transactions whose changes it has read have committed.
- A schedule is cascadeless if no transaction reads a data item before the transaction that has written it has committed.
- A schedule is strict if no transaction reads or writes a data item before the transaction that has written it has committed.
- A concurrency control protocol is a set of rules that govern how concurrent transactions can access and modify the data in the database, without violating the ACID properties.
- A locking protocol is a concurrency control protocol that uses locks to control the access of transactions to data items.
- A lock is a variable associated with a data item that indicates the status of the item with respect to possible operations that can be applied to it.
- A lock can have one of the following modes: shared (S), exclusive (X), or none (N).
- A shared lock allows a transaction to read a data item, but not to write it.
- An exclusive lock allows a transaction to read and write a data item, but not to share it with other transactions.
- A lock can be granted to a transaction if it is compatible with the current lock mode of the data item, according to a lock compatibility matrix.
- A lock can be released by a transaction when it no longer needs to access the data item, or when it commits or aborts.
- A two-phase locking (2PL) protocol is a locking protocol that requires a transaction to obtain all the locks it needs before releasing any lock.
- A 2PL protocol can be classified into the following types: basic, conservative, strict, and rigorous.
- A basic 2PL protocol does not impose any restrictions on when a transaction can acquire or release locks, as long as it follows the 2PL rule.
- A conservative 2PL protocol requires a transaction to request all the locks it needs in advance, before it begins execution, and to hold them until it commits or aborts.
- A strict 2PL protocol requires a transaction to hold all its exclusive locks until it commits or aborts, but allows it to release its shared locks earlier.
- A rigorous 2PL protocol requires a transaction to hold all its locks, both shared and exclusive, until it commits or aborts.
- A deadlock is a situation where two or more transactions are waiting



# Deadlock Handling

A deadlock is a situation in which two or more transactions are waiting indefinitely for one another to release locks on database resources. Deadlocks can cause performance degradation and transaction failure in a database system. Therefore, deadlock handling is an important aspect of transaction processing.

There are three main strategies for deadlock handling in a database system:

- **Deadlock prevention**: This strategy aims to prevent deadlocks from occurring in the first place by imposing some constraints on how transactions can acquire and release locks. For example, a transaction may be required to lock all the resources it needs before it starts, or to follow a predefined order of locking resources. Deadlock prevention ensures that there is no cycle in the wait-for graph, which is a directed graph that represents the dependencies between transactions based on their locks. However, deadlock prevention may also reduce concurrency and increase overhead, as transactions may have to wait longer or lock more resources than necessary.
- **Deadlock avoidance**: This strategy allows transactions to acquire and release locks dynamically, but uses some information about the resource requirements and the current state of the system to decide whether to grant a lock request or not. For example, a transaction may have to declare in advance the maximum number of resources it will need, or the system may maintain a matrix that records the allocation and request of resources by each transaction. Deadlock avoidance ensures that the system is always in a safe state, which is a state that guarantees that all transactions can finish without deadlock. However, deadlock avoidance may also be conservative and pessimistic, as it may reject some lock requests that do not actually lead to deadlock, or it may require more information and computation than available or feasible.
- **Deadlock detection and recovery**: This strategy does not prevent or avoid deadlocks, but rather detects them after they have occurred and takes some actions to resolve them. For example, the system may periodically run a deadlock detection algorithm that checks for cycles in the wait-for graph, or it may use some event-driven mechanisms such as timeouts or lock requests to trigger the detection. Deadlock detection and recovery ensures that the system can recover from deadlocks and continue processing transactions. However, deadlock detection and recovery may also incur some costs and risks, such as wasted resources, aborted transactions, inconsistent data, or lost updates.

The choice of the best strategy for deadlock handling depends on various factors, such as the characteristics of the transactions, the frequency and severity of deadlocks, the availability and accuracy of information, and the performance and reliability requirements of the system. In some cases, a combination of strategies may be used to achieve a balance between the benefits and drawbacks of each strategy.



# Distributed Database

A distributed database is a collection of databases that are physically stored on different network hosts and logically appear as a single database to the user. A distributed database can improve performance, reliability, availability, and scalability of data management.

# Transaction Processing Concept

A transaction is a logical unit of work that consists of one or more SQL statements executed by a single user. A transaction has the following properties:

- Atomicity: A transaction either commits or aborts as a whole. Partial changes are not visible to other users.
- Consistency: A transaction preserves the consistency of the database by ensuring that it satisfies all the integrity constraints.
- Isolation: A transaction is isolated from other concurrent transactions. The intermediate states of a transaction are not visible to other users.
- Durability: The effects of a committed transaction are permanent and survive any system failures.

# Distributed Transaction

A distributed transaction is a transaction that involves two or more network hosts that provide transactional resources, such as databases, message queues, or files. A distributed transaction requires a transaction manager that coordinates the execution and completion of the transaction across all the involved hosts.

# Two-Phase Commit Protocol

The two-phase commit protocol is a mechanism that ensures the atomicity and consistency of a distributed transaction. The protocol involves two phases:

- Prepare phase: The transaction manager asks all the involved hosts to prepare to commit the transaction. Each host executes the transaction locally and sends a reply indicating whether it is ready to commit or not.
- Commit phase: The transaction manager decides whether to commit or abort the transaction based on the replies from all the hosts. If all the hosts are ready to commit, the transaction manager sends a commit message to all the hosts. Otherwise, it sends an abort message. Each host then commits or aborts the transaction accordingly.

# In-Doubt Transactions

A transaction becomes in-doubt if the two-phase commit protocol fails due to a network or system failure. For example, if the transaction manager crashes after sending the prepare message, some hosts may not receive the commit or abort message and remain in a prepared state. In this case, the transaction is in-doubt and its final outcome is unknown.

# Recovery of In-Doubt Transactions

To recover from in-doubt transactions, the transaction manager and the hosts use a mechanism called presumed abort or presumed commit. In this mechanism, each host maintains a log of the prepared transactions and their outcomes. The transaction manager also maintains a log of the committed transactions. When a failure occurs, the transaction manager and the hosts communicate with each other to resolve the in-doubt transactions. The transaction manager can either query the hosts for the status of the prepared transactions, or broadcast the list of the committed transactions. The hosts can then commit or abort the in-doubt transactions based on the information from the transaction manager.



# Distributed Data Storage

- Distributed data storage is a system that stores and processes data on multiple machines, often in a replicated fashion .
- Distributed data storage can be used for various purposes, such as storing application data, metrics, logs, etc, or providing high availability, scalability, and fault tolerance for data-intensive applications.
- Distributed data storage can be classified into two main types: distributed databases and distributed file systems.
  - Distributed databases are systems where users store information on a number of nodes, and the system provides a consistent and coherent view of the data across the nodes.
  - Distributed file systems are systems where users store information on a number of peer network nodes, and the system provides a transparent and uniform access to the files across the nodes.
- Distributed data storage can also be categorized based on the data model, such as relational, key-value, document, columnar, graph, etc.
- Distributed data storage can also be characterized based on the consistency model, such as strong, eventual, causal, etc.
- Distributed data storage can also be evaluated based on the performance, reliability, availability, scalability, and security aspects   .
- Distributed data storage can also be implemented using various technologies, such as Hadoop, Cassandra, MongoDB, Amazon S3, etc    .



# Concurrency Control

Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating the data integrity of the database   .

Some of the objectives of concurrency control are:

- To prevent the loss of data due to concurrent updates by different transactions.
- To maintain the consistency and isolation properties of transactions.
- To avoid deadlock and starvation situations among competing transactions.
- To improve the performance and throughput of the database system.

There are two main approaches to concurrency control: **lock-based** and **timestamp-based** protocols .

## Lock-Based Protocols

Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item. There are two types of locks: **shared** and **exclusive**.

- A shared lock (S-lock) allows a transaction to read a data item, but not to modify it. Multiple transactions can hold S-locks on the same data item concurrently.
- An exclusive lock (X-lock) allows a transaction to read and write a data item, but not to share it with other transactions. Only one transaction can hold an X-lock on a data item at a time.

A lock-based protocol must follow two rules to ensure serializability of transactions:

- **Two-phase locking (2PL)**: A transaction must acquire all the locks it needs before it releases any lock. This means that a transaction goes through two phases: a growing phase, where it acquires locks, and a shrinking phase, where it releases locks.
- **Conflict serializability**: A transaction must not conflict with another transaction that holds a lock on the same data item. This means that a transaction must wait until the conflicting lock is released before it can proceed.

Some of the advantages and disadvantages of lock-based protocols are:

- Advantages:
  - They are simple and easy to implement.
  - They can handle any type of conflict among transactions.
  - They can be combined with other techniques, such as deadlock detection and prevention, to improve concurrency control.
- Disadvantages:
  - They may cause a high degree of blocking and waiting among transactions, which reduces concurrency and performance.
  - They may lead to deadlock situations, where two or more transactions are waiting for each other to release locks.
  - They may cause cascading aborts, where the failure of one transaction causes the rollback of other transactions that depend on its updates.

## Timestamp-Based Protocols

Timestamp-based protocols use timestamps to order the execution of transactions. A timestamp is a unique identifier that reflects the start time of a transaction. Each transaction is assigned a timestamp when it begins, and each data item has two timestamps: a read timestamp (RTS) and a write timestamp (WTS). The RTS records the timestamp of the last transaction that read the data item, and the WTS records the timestamp of the last transaction that wrote the data item.

A timestamp-based protocol must follow two rules to ensure serializability of transactions:

- **Read-write rule**: A transaction T can read a data item X only if T's timestamp is greater than or equal to X's WTS. This means that T can read the latest version of X, and no other transaction can overwrite X after T reads it. If T's timestamp is less than X's WTS, then T is aborted and restarted with a new timestamp.
- **Write-write rule**: A transaction T can write a data item X only if T's timestamp is greater than both X's RTS and X's WTS. This means that T can write a new version of X, and no other transaction can read or write X before T writes it. If T's timestamp is less than or equal to either X's RTS or X's WTS, then T is aborted and restarted with a new timestamp.

Some of the advantages and disadvantages of timestamp-based protocols are:

- Advantages:
  - They do not use locks, so they avoid blocking, waiting, and deadlock situations among transactions.
  - They do not cause cascading aborts, as transactions are aborted before they make any changes to the database.
  - They ensure that transactions are executed in a chronological order, which preserves causality and consistency.
- Disadvantages:
  - They may cause a high rate of aborts and restarts among transactions, which reduces concurrency and performance.
  - They may not handle some types of conflicts, such as read-read and write



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the directory system for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System:

# Unit 4 - Transaction Processing Concept

## Introduction
- Define what is a transaction and its properties (ACID)
- Explain the role of transactions in database systems
- Describe the states of a transaction and the transaction life cycle

## Concurrency Control
- Explain why concurrency control is needed and what are the problems of concurrent execution
- Define serializability and conflict serializability
- Describe the methods of concurrency control: locking, timestamping, validation, and multiversion
- Compare the advantages and disadvantages of each method

## Recovery Techniques
- Explain why recovery techniques are needed and what are the types of failures
- Define the concepts of log, checkpoint, commit, and rollback
- Describe the methods of recovery techniques: deferred update, immediate update, and shadow paging
- Compare the advantages and disadvantages of each method

## Distributed Databases
- Define what is a distributed database and its advantages and disadvantages
- Explain the issues and challenges of distributed database systems
- Describe the methods of distributed concurrency control: two-phase commit, three-phase commit, and voting
- Describe the methods of distributed recovery techniques: backward recovery, forward recovery, and coordinated recovery

## Summary
- Review the main concepts and terms of the unit
- Provide some examples and exercises to test the understanding of the unit
- Provide some references and resources for further reading



## Unit 5 - Concurrency Control Techniques

- Concurrency control techniques are methods to ensure the consistency and isolation of transactions in a database system that allows multiple users to access and modify data simultaneously.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and snapshot isolation.
- The choice of concurrency control technique depends on the characteristics of the application, the workload, and the performance requirements. Some factors to consider are the degree of concurrency, the conflict rate, the overhead of locking and validation, and the response time.



# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

The advantages of a concurrent system are:

- Waiting Time: It reduces the waiting time of processes that are ready to execute.
- CPU Utilization: It increases the CPU utilization by keeping it busy with multiple processes.
- Throughput: It improves the throughput, which is the number of transactions executed per unit time.

The reasons for using concurrency control methods in DBMS are:

- To apply isolation through mutual exclusion between conflicting transactions
- To resolve read-write and write-write conflict issues
- To preserve database consistency through constantly preserving execution obstructions
- To ensure serializability, which is the property that the concurrent execution of transactions is equivalent to some serial execution of the same transactions

The main concurrency control techniques in DBMS are:

- Timestamp-based protocols: These protocols assign a timestamp to each transaction and use them to order the transactions and resolve conflicts. The timestamps can be either generated by the system or by the user.
- Lock-based protocols: These protocols use locks to control the access of transactions to data items. A lock is a variable that can have two values: locked or unlocked. A transaction can request, acquire, and release locks on data items. There are different types of locks, such as binary locks, shared/exclusive locks, and multiple granularity locks.
- Validation-based protocols: These protocols use a validation or certification phase to check if the transactions can be committed without violating serializability. A transaction is executed in three phases: read phase, validation phase, and write phase. The validation phase checks for conflicts with other transactions based on their read and write sets.



# Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the integrity of the database is maintained.

One of the most common concurrency control techniques is locking. Locking is the mechanism of granting or denying access to a data item based on the type of lock applied by a transaction. Locking can prevent conflicts such as lost updates, dirty reads, unrepeatable reads, and phantom reads.

There are different types of locks and locking protocols that can be used for concurrency control. Some of the main ones are:

- **Binary locks**: These are the simplest locks that have only two states: locked or unlocked. A transaction can either lock a data item for exclusive access, or leave it unlocked for shared access. Binary locks can prevent lost updates, but not dirty reads, unrepeatable reads, or phantom reads.

- **Shared and exclusive locks**: These are more sophisticated locks that have three states: unlocked, shared, or exclusive. A transaction can lock a data item in shared mode, which allows other transactions to read the same data item, but not to write it. Alternatively, a transaction can lock a data item in exclusive mode, which prevents other transactions from reading or writing the same data item. Shared and exclusive locks can prevent lost updates and dirty reads, but not unrepeatable reads or phantom reads.

- **Intention locks**: These are locks that indicate the intention of a transaction to lock a data item or a group of data items in a certain mode. For example, a transaction can lock a table in intention-shared mode, which means that it intends to lock some of the rows in the table in shared mode. Intention locks are used to implement hierarchical locking, which allows transactions to lock data items at different levels of granularity, such as tables, pages, or rows. Intention locks can prevent deadlocks and improve concurrency.

- **Certify locks**: These are locks that are used in multi-version concurrency control techniques, which maintain multiple versions of a data item to allow concurrent reads and writes. A transaction can read a committed version of a data item without locking it, but it has to lock a data item in certify mode before committing its write. A certify lock checks if the write is valid and does not conflict with other transactions. Certify locks can improve concurrency and performance, but they require more storage space and overhead.

## Two-Phase Locking Protocol

The two-phase locking protocol is a locking protocol that ensures serializability of transactions, which means that the concurrent execution of transactions is equivalent to some serial execution. The two-phase locking protocol divides the execution of a transaction into two phases:

- **Locking (Growing) phase**: In this phase, a transaction can acquire locks on data items, but cannot release any lock. The transaction can lock data items in any order and mode, as long as it does not violate the compatibility rules of the locks. The locking phase ends when the transaction acquires its last lock.

- **Unlocking (Shrinking) phase**: In this phase, a transaction can release locks on data items, but cannot acquire any new lock. The transaction can unlock data items in any order and mode, as long as it does not violate the consistency rules of the locks. The unlocking phase ends when the transaction releases its last lock.

The two-phase locking protocol guarantees serializability, but it does not prevent deadlocks, which occur when two or more transactions are waiting for each other to release locks. To avoid or resolve deadlocks, the protocol can use techniques such as timeouts, deadlock detection, or deadlock prevention.

## Time Stamp Ordering Protocol

The time stamp ordering protocol is a concurrency control technique that does not use locking, but instead assigns a unique time stamp to each transaction and each data item. The time stamp of a transaction represents its logical start time, and the time stamp of a data item represents the last time it was read or written by a transaction. The time stamp ordering protocol uses the time stamps to order the transactions and the data items, and to determine if a transaction can read or write a data item.

The time stamp ordering protocol has two main rules:

- **Read rule**: A transaction T can read a data item X only if the time stamp of T is greater than or equal to the write time stamp of X, which means that T started after the last transaction that wrote X. Otherwise, T is aborted and restarted with a new time stamp.

- **Write rule**: A transaction T can write a data item X only if the time stamp of T is greater than both the



# Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability   .
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be either the system time or a logical counter  .
- The main idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamp to determine the precedence and compatibility of the transactions   .
- There are two types of time stamping protocols: basic timestamp ordering and timestamp ordering with Thomas' write rule   .

## Basic Timestamp Ordering

- In basic timestamp ordering, each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item, and WTS is the largest timestamp of any transaction that has successfully written the data item   .
- The protocol works as follows   :
  - If a transaction T wants to read a data item X, it checks the WTS of X. If the WTS of X is larger than the timestamp of T, it means that some other transaction has modified X after T started, so T is aborted and restarted with a new timestamp. Otherwise, T is allowed to read X and the RTS of X is updated to the maximum of the RTS of X and the timestamp of T.
  - If a transaction T wants to write a data item X, it checks both the RTS and WTS of X. If either the RTS or WTS of X is larger than the timestamp of T, it means that some other transaction has read or written X after T started, so T is aborted and restarted with a new timestamp. Otherwise, T is allowed to write X and the WTS of X is updated to the timestamp of T.
- The basic timestamp ordering protocol ensures that the transactions are executed in a conflict-serializable order that is consistent with their timestamps. However, it may cause unnecessary aborts and restarts of transactions that do not actually conflict with each other   .

## Timestamp Ordering with Thomas' Write Rule

- Timestamp ordering with Thomas' write rule is a variation of basic timestamp ordering that avoids some unnecessary aborts and restarts by applying a write rule   .
- The write rule states that if a transaction T wants to write a data item X, and the WTS of X is larger than the timestamp of T, then T's write operation can be ignored, because it will be overwritten by a later transaction anyway   .
- The protocol works as follows   :
  - If a transaction T wants to read a data item X, it checks the WTS of X. If the WTS of X is larger than the timestamp of T, it means that some other transaction has modified X after T started, so T is aborted and restarted with a new timestamp. Otherwise, T is allowed to read X and the RTS of X is updated to the maximum of the RTS of X and the timestamp of T.
  - If a transaction T wants to write a data item X, it checks both the RTS and WTS of X. If the RTS of X is larger than the timestamp of T, it means that some other transaction has read X after T started, so T is aborted and restarted with a new timestamp. If the WTS of X is larger than the timestamp of T, it means that some other transaction has written X after T started, so T's write operation is ignored. Otherwise, T is allowed to write X and the WTS of X is updated to the timestamp of T.
- The timestamp ordering with Thomas' write rule protocol ensures that the transactions are executed in a view-serializable order that is consistent with their timestamps. It also reduces the number of



# Validation Based Protocol

- Validation Based Protocol is a type of concurrency control technique that works on the validation rules and timestamps .
- It is also called Optimistic Concurrency Control Technique because it assumes that very few conflicts occur among transactions .
- It does not check for conflicts while the transaction is executing, but only at the end of the transaction .
- It consists of three phases for each transaction: read phase, validation phase, and write phase  .
- In the read phase, the transaction can read data from the database and make updates to the local copies, but not to the actual database.
- In the validation phase, the transaction checks for any conflicts with other transactions that have already committed. If there are no conflicts, the transaction is validated and can proceed to the write phase. Otherwise, the transaction is aborted and restarted  .
- In the write phase, the transaction writes the updated data to the database and commits  .
- The validation phase uses timestamps to determine the order of transactions and detect conflicts. There are two types of timestamps: start timestamp (ST) and end timestamp (ET)  .
- The start timestamp is assigned to a transaction when it enters the read phase. It indicates the logical start time of the transaction  .
- The end timestamp is assigned to a transaction when it completes the read phase. It indicates the logical end time of the transaction  .
- A transaction T1 is said to precede another transaction T2 if ET(T1) < ST(T2). This means that T1 finishes its read phase before T2 starts its read phase  .
- A transaction T1 is said to overlap with another transaction T2 if ST(T1) < ET(T2) and ET(T1) > ST(T2). This means that T1 and T2 have some common time interval in their read phases  .
- A conflict occurs when two overlapping transactions access the same data item and at least one of them updates it  .
- The validation phase uses the following rules to check for conflicts and validate transactions  :
  - If T1 precedes T2, then T1 does not conflict with T2 and both transactions can be validated.
  - If T1 overlaps with T2 and T1 reads a data item that T2 has updated, then T1 conflicts with T2 and T1 must be aborted and restarted.
  - If T1 overlaps with T2 and T1 updates a data item that T2 has read or updated, then T1 conflicts with T2 and T1 must be aborted and restarted.
- The validation based protocol ensures serializability of transactions by validating them in the order of their end timestamps  .
- The validation based protocol has the advantage of avoiding locking and deadlock, but the disadvantage of wasting resources and time for aborting and restarting transactions  .



# Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock.
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity means hierarchically breaking up the database into blocks that can be locked and can be tracked needs what needs to lock and in what fashion. Such a hierarchy can be represented graphically as a tree.
- For example, consider the following tree, which consists of four levels of nodes:

tree

- The root node represents the entire database, the second level nodes represent the files, the third level nodes represent the pages, and the fourth level nodes represent the records.
- There are three types of lock granularity: record level, page level, and file level.
- Record level locking is the finest granularity, where each record can be locked individually. This allows the highest degree of concurrency, but also the highest lock overhead and the highest risk of deadlock.
- Page level locking is the intermediate granularity, where each page (a collection of records) can be locked. This reduces the lock overhead and the risk of deadlock, but also reduces the concurrency.
- File level locking is the coarsest granularity, where each file (a collection of pages) can be locked. This minimizes the lock overhead and the risk of deadlock, but also minimizes the concurrency.
- To implement multiple granularity locking, a compatibility matrix is used to determine which locks are compatible with each other at different levels of the hierarchy.
- The compatibility matrix is as follows:

matrix

- The lock modes are: shared (S), exclusive (X), intention shared (IS), intention exclusive (IX), and shared with intention exclusive (SIX).
- A shared lock (S) allows a transaction to read a data item, but not to write or modify it. A shared lock is compatible with another shared lock, but not with an exclusive lock.
- An exclusive lock (X) allows a transaction to read and write a data item, but not to share it with any other transaction. An exclusive lock is not compatible with any other lock.
- An intention shared lock (IS) indicates that a transaction intends to acquire a shared lock on some data item in the lower level of the hierarchy. An intention shared lock is compatible with another intention shared lock, a shared lock, or a shared with intention exclusive lock, but not with an exclusive lock or an intention exclusive lock.
- An intention exclusive lock (IX) indicates that a transaction intends to acquire an exclusive lock on some data item in the lower level of the hierarchy. An intention exclusive lock is compatible with another intention shared lock or an intention exclusive lock, but not with a shared lock, an exclusive lock, or a shared with intention exclusive lock.
- A shared with intention exclusive lock (SIX) indicates that a transaction has a shared lock on a data item and intends to acquire an exclusive lock on some data item in the lower level of the hierarchy. A shared with intention exclusive lock is compatible with another intention shared lock or a shared lock, but not with an exclusive lock, an intention exclusive lock, or a shared with intention exclusive lock.
- To ensure correctness and consistency, the multiple granularity locking protocol follows these rules:
  - Follow the multi-granularity compatibility function as shown in the matrix.
  - Lock the root of the tree first, in any mode.
  - Node Q can be locked by transaction T in S or IS mode only if the parent of Q is locked by T in IX or IS mode.
  - Node Q can be locked by transaction T in X, SIX



# Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data objects to exist in the database at the same time.
- The main idea of multi version schemes is to grant an appropriate version of a data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data object from other transactions.
- The advantages of multi version schemes are that they increase the concurrency and performance of the database system, and reduce the chances of deadlock and starvation.
- The disadvantages of multi version schemes are that they require more storage space and overhead to maintain multiple versions of data objects, and they may cause inconsistency and anomalies if the versions are not managed properly.
- There are different types of multi version schemes, such as timestamp ordering, multiversion two-phase locking, and snapshot isolation.
- Timestamp ordering is a multi version scheme that assigns a unique timestamp to each transaction, and uses the timestamp to determine the order of execution and the version of the data object to be accessed.
- Multiversion two-phase locking is a multi version scheme that combines two-phase locking with versioning, and allows transactions to read the latest committed version of a data object, while locking the data object for writing.
- Snapshot isolation is a multi version scheme that provides each transaction with a snapshot of the database state at the start of the transaction, and allows transactions to read and write without locking, as long as there are no write-write conflicts.



# Recovery with Concurrent Transactions

- Recovery with concurrent transactions is the process of restoring the database to a consistent state after a failure, while allowing multiple transactions to execute simultaneously.
- Recovery with concurrent transactions can be done in the following four ways:
  - Interaction with concurrency control
  - Transaction rollback
  - Checkpoints
  - Restart recovery

## Interaction with concurrency control

- In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used.
- For example, if the concurrency control scheme is based on locking, then the recovery scheme must ensure that the locks are released properly after a failure, and that the transactions that were waiting for the locks are notified.
- Similarly, if the concurrency control scheme is based on timestamps, then the recovery scheme must ensure that the timestamps are assigned correctly after a failure, and that the transactions that were aborted due to timestamp conflicts are restarted.

## Transaction rollback

- In this scheme, the recovery scheme uses the log records to undo the effects of the transactions that were not committed before the failure.
- The recovery scheme scans the log records in reverse order, from the most recent to the oldest, and applies the undo operation for each log record that belongs to an uncommitted transaction.
- The undo operation restores the previous value of the data item that was modified by the transaction, and writes a new log record to indicate the undo operation.
- The recovery scheme stops when it reaches the oldest log record, or when it encounters a log record that belongs to a committed transaction.

## Checkpoints

- In this scheme, the recovery scheme periodically performs a checkpoint operation, which is a special log record that marks a point in time when the database is in a consistent state.
- The checkpoint operation flushes all the modified data pages from the buffer to the disk, and writes a checkpoint log record to the log file.
- The checkpoint log record contains the list of transactions that were active at the time of the checkpoint, and the list of transactions that were committed since the last checkpoint.
- The checkpoint operation reduces the amount of work that the recovery scheme has to do after a failure, as it only has to scan the log records from the most recent checkpoint to the end of the log file.

## Restart recovery

- In this scheme, the recovery scheme uses the checkpoint log records to perform the restart recovery after a failure.
- The restart recovery consists of two phases: analysis and redo/undo.
- In the analysis phase, the recovery scheme scans the log records from the most recent checkpoint to the end of the log file, and identifies the transactions that were active, committed, or aborted at the time of the failure.
- In the redo/undo phase, the recovery scheme performs the redo operation for the transactions that were committed, and the undo operation for the transactions that were active or aborted.
- The redo operation re-applies the effects of the transactions that were committed, and writes a new log record to indicate the redo operation.
- The undo operation reverses the effects of the transactions that were active or aborted, and writes a new log record to indicate the undo operation.



# Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Oracle is a relational database management system that supports concurrent access of data by multiple users and transactions.
- Oracle uses a multiversion concurrency control (MVCC) model to provide read consistency and isolation levels for queries and transactions  .
- MVCC means that Oracle maintains multiple versions of data in the database, each with a unique system change number (SCN) that indicates when the version was created or modified  .
- Oracle automatically provides statement-level read consistency, which means that all the data that a query sees comes from a single point in time, the time when the query started .
- Oracle can also provide transaction-level read consistency, which means that all the queries in a transaction see the data as it was when the transaction started .
- Oracle supports four isolation levels: read committed, serializable, read only, and read write  .
- Read committed is the default isolation level, which means that a transaction can only see the changes made by other transactions that have committed  .
- Serializable is the highest isolation level, which means that a transaction can only see the changes made by itself, and any other transaction that tries to modify the same data will be blocked or aborted  .
- Read only is a special isolation level, which means that a transaction can only read the data, and any attempt to modify the data will be rejected  .
- Read write is a synonym for read committed, which means that a transaction can read and write the data, and see the changes made by other committed transactions  .
- Oracle uses various types of locks to ensure data integrity and prevent conflicts among concurrent transactions  .
- Oracle uses exclusive locks to prevent other transactions from modifying the same data, and shared locks to prevent other transactions from modifying the data while allowing them to read it  .
- Oracle uses row-level locking, which means that each row in a table can be locked by a transaction, and the lock is released when the transaction commits or rolls back  .
- Oracle also uses table-level locking, which means that a transaction can lock the entire table for exclusive or shared access, depending on the operation performed on the table  .
- Oracle uses implicit locking, which means that the locks are acquired and released automatically by the database, and the user does not need to specify any locking commands  .
- Oracle also supports explicit locking, which means that the user can issue locking commands such as LOCK TABLE, SELECT FOR UPDATE, or DBMS_LOCK to acquire and release locks manually  .
- Oracle uses optimistic locking, which means that the transactions do not acquire locks until they are ready to commit, and they check for conflicts with other transactions at that time  .
- Oracle also uses pessimistic locking, which means that the transactions acquire locks as soon as they access the data, and they hold the locks until they commit or roll back  .
- Oracle uses deadlock detection and resolution, which means that the database detects when two or more transactions are waiting for each other's locks, and aborts one of them to break the deadlock  .
- Oracle uses a lock manager, which is a component of the database that maintains the information about the locks and the transactions that hold them, and enforces the locking rules and policies  .
- Oracle uses a redo log, which is a set of files that record all the changes made to the data by the transactions, and can be used to recover the data in case of a failure  .
- Oracle uses an undo

