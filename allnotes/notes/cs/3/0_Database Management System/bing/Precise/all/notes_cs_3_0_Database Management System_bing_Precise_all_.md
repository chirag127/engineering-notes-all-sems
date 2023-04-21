

## Unit 1 - Introduction

1. The introduction is the first part of any written work, speech, or presentation.
2. It serves to provide the reader or listener with an overview of the topic and the main points that will be covered.
3. The introduction should be clear, concise, and engaging to capture the attention of the audience.
4. It should also provide enough background information to help the reader or listener understand the context of the topic.
5. The introduction should be structured in a logical manner, with a clear progression of ideas.
6. It is important to avoid including too much detail in the introduction, as this can overwhelm the reader or listener and detract from the main points of the work.
7. The introduction should also include a thesis statement, which is a clear and concise statement of the main argument or point of the work.
8. The thesis statement should be specific and focused, and should be supported by the evidence presented in the body of the work.
9. The introduction should also include a preview of the main points that will be covered in the body of the work, to help the reader or listener follow the progression of ideas.
10. In summary, the introduction serves to provide the reader or listener with an overview of the topic, background information, a thesis statement, and a preview of the main points that will be covered in the body of the work. It should be clear, concise, engaging, and structured in a logical manner.



### Overview for the notes of the Unit 1 - Introduction in the subject of Database Management System

1. A database is a collection of related data that is organized and stored in a way that allows for efficient retrieval and manipulation.
2. A database management system (DBMS) is a software system that provides tools for managing and accessing the data stored in a database.
3. The primary functions of a DBMS include data storage, retrieval, and manipulation, as well as ensuring the integrity and security of the data.
4. Common types of DBMSs include relational, hierarchical, network, and object-oriented.
5. The relational model is the most widely used model for organizing data in a DBMS.
6. The Structured Query Language (SQL) is the standard language for managing and querying data in a relational DBMS.
7. A database schema defines the structure of the data in a database, including the tables, columns, and relationships between them.
8. Normalization is the process of organizing data in a database to minimize redundancy and improve data integrity.
9. Transactions are used to ensure that data is updated in a consistent and reliable manner.
10. Concurrency control mechanisms are used to manage simultaneous access to data by multiple users.




# Database System vs File System

Unit 1 - Introduction in the subject of Database Management System

- A **database system** is a software application that is used to manage, store, and retrieve data. It provides a structured way to organize and access data, and typically includes features such as data validation, data security, and data backup and recovery.

- A **file system**, on the other hand, is a method of organizing and storing files on a storage device, such as a hard drive or solid-state drive. It provides a way to organize files into directories and subdirectories, and to manage file permissions and attributes.

- One key difference between a database system and a file system is the way data is organized and accessed. In a database system, data is organized into tables with rows and columns, and can be accessed using a query language such as SQL. In a file system, data is stored in files, and can be accessed by navigating the directory structure and opening the appropriate file.

- Another difference is the level of data validation and security provided by each system. Database systems typically include built-in mechanisms for ensuring data integrity and consistency, and for managing user access to data. File systems, on the other hand, rely on the operating system to manage file permissions and attributes.

- In terms of data backup and recovery, database systems often provide more advanced features than file systems. For example, many database systems include the ability to perform incremental backups, which only backup changes to the data since the last backup. This can make the backup process faster and more efficient. File systems, on the other hand, typically require a full backup of all data each time a backup is performed.

- In summary, a database system provides a more structured and feature-rich way to manage, store, and retrieve data, while a file system provides a simpler way to organize and access files. The choice between the two systems will depend on the specific needs of the user and the type of data being managed.



### Database System Concept and Architecture

#### Unit 1 - Introduction

1. A **database** is a collection of related data that represents some aspect of the real world.
2. A **database management system (DBMS)** is a software system that enables users to define, create, maintain, and control access to the database.
3. The **database system** is the DBMS software together with the data itself.
4. The **database system environment** includes hardware, software, data, procedures, and people.
5. The **three-schema architecture** proposes that the database be viewed at three levels: the internal level, the conceptual level, and the external level.
6. The **internal level** defines how the data is physically stored and accessed.
7. The **conceptual level** defines the logical structure of the data, independent of how it is physically stored.
8. The **external level** defines the user's view of the data, which may be different for different users.
9. The **data independence** is the ability to change the schema at one level without having to change the schema at the next higher level.
10. The **data model** is a collection of concepts that can be used to describe the structure of a database.
11. The **entity-relationship (ER) model** is a widely used data model for database design.
12. The **relational model** is another widely used data model, based on the concept of relations or tables.
13. The **Structured Query Language (SQL)** is a standard language for managing and querying relational databases.
14. The **database design** is the process of designing the database schema, including the conceptual, external, and internal levels.
15. The **database application** is a software program that interacts with the database to perform specific tasks, such as data entry, querying, and reporting.



### Data Model Schema and Instances

A **data model** is a conceptual representation of the data structures that are required by a database. The data structures include the data objects, the associations between data objects, and the rules that govern these associations.

A **schema** is a description of a particular collection of data, using a given data model. The schema defines the tables, views, indexes, and other elements that make up the database. It also defines the relationships between the different tables and specifies the constraints that must be satisfied by the data.

An **instance** of a database is a snapshot of the data in the database at a given point in time. It is the actual data that is stored in the database, as opposed to the schema, which is the description of the data.

In summary:
- A data model is a conceptual representation of the data structures required by a database.
- A schema is a description of a particular collection of data, using a given data model.
- An instance of a database is a snapshot of the data in the database at a given point in time.



# Data Independence and Database Language and Interfaces

## Data Independence
Data independence refers to the ability to change the schema at one level of a database system without having to change the schema at the next higher level. There are two types of data independence:
1. **Logical data independence:** The ability to change the conceptual schema without having to change the external schema or the application programs. This means that the way data is organized and accessed can be changed without affecting the way data is presented to the users.
2. **Physical data independence:** The ability to change the internal schema without having to change the conceptual schema. This means that the way data is physically stored and accessed can be changed without affecting the logical organization of the data.

## Database Language and Interfaces
A database language is a language used to interact with a database. There are two main types of database languages:
1. **Data Definition Language (DDL):** Used to define the structure of the database, including the schema, tables, views, and indexes.
2. **Data Manipulation Language (DML):** Used to manipulate the data in the database, including inserting, updating, deleting, and querying data.

Database interfaces provide a way for users to interact with the database. There are several types of database interfaces, including:
1. **Graphical User Interfaces (GUIs):** Provide a visual way for users to interact with the database, using windows, icons, and menus.
2. **Command Line Interfaces (CLIs):** Allow users to interact with the database using text-based commands.
3. **Application Programming Interfaces (APIs):** Provide a way for developers to interact with the database programmatically, using a specific programming language.



### Data Definition Language

Data Definition Language (DDL) is a subset of SQL (Structured Query Language) used to define and manage the structure of a database. It includes commands to create, alter, and delete database objects such as tables, views, indexes, and stored procedures.

Some common DDL commands include:

- **CREATE**: This command is used to create new database objects such as tables, views, indexes, and stored procedures. For example, the `CREATE TABLE` command is used to create a new table in the database.

- **ALTER**: This command is used to modify the structure of an existing database object. For example, the `ALTER TABLE` command can be used to add, modify, or delete columns in a table.

- **DROP**: This command is used to delete a database object. For example, the `DROP TABLE` command is used to delete a table from the database.

- **TRUNCATE**: This command is used to delete all data from a table, but it does not delete the table itself.

- **RENAME**: This command is used to rename a database object.

It is important to note that DDL commands do not manipulate the data stored in the database, but rather the structure of the database itself. Data manipulation is done using Data Manipulation Language (DML) commands such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.



### DML (Data Manipulation Language)

DML is a sublanguage of SQL (Structured Query Language) used to manipulate data in a database. It includes commands such as:

1. **SELECT**: used to retrieve data from a database table.
2. **INSERT**: used to add new records to a database table.
3. **UPDATE**: used to modify existing records in a database table.
4. **DELETE**: used to remove records from a database table.

These commands allow users to interact with the data stored in a database, allowing them to retrieve, add, modify, and delete records as needed.

It is important to note that DML commands do not change the structure of the database itself, only the data stored within it. Changes to the structure of the database are made using DDL (Data Definition Language) commands.



### Overall Database Structure

Unit 1 - Introduction to Database Management System

1. A database is a collection of related data that is organized and stored in a structured manner.
2. A database management system (DBMS) is a software system that enables users to create, maintain, and manipulate databases.
3. The overall structure of a database is determined by its schema, which defines the tables, fields, relationships, and constraints within the database.
4. A database schema is typically represented using a data model, such as the Entity-Relationship (ER) model or the Relational model.
5. The ER model represents the database as a collection of entities and relationships, while the Relational model represents the database as a collection of tables with rows and columns.
6. The structure of a database can be modified by altering its schema, which may involve adding or removing tables, fields, relationships, or constraints.
7. The overall structure of a database is important for ensuring data integrity, consistency, and efficiency in data retrieval and manipulation.




# Data Modeling Using the Entity Relationship Model

- Data modeling is the process of creating a conceptual representation of data, which can be used to design and build a database.
- The Entity Relationship (ER) model is a widely used data modeling technique that graphically represents the entities, attributes, and relationships in a database.
- An entity is an object or concept that can be uniquely identified and is important to the organization or system being modeled. Examples of entities include customers, products, and orders.
- Attributes are characteristics or properties of an entity. For example, a customer entity may have attributes such as name, address, and phone number.
- Relationships describe how entities are associated with one another. For example, a customer may place an order, creating a relationship between the customer and order entities.
- The ER model uses a diagram called an Entity Relationship Diagram (ERD) to visually represent the entities, attributes, and relationships in a database.
- ERDs use a set of standard symbols and notations to represent the different components of the model. For example, entities are represented by rectangles, attributes are represented by ovals, and relationships are represented by diamonds.
- The ER model is a powerful tool for designing and building databases, as it provides a clear and concise way to represent the data and its relationships. It is widely used in the design of relational databases, which are the most common type of database used in organizations today.

