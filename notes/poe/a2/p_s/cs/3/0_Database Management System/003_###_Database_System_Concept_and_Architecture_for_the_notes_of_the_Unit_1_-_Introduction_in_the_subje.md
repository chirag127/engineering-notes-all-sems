 Here is the content in markdown format for the topic ### Database System Concept and Architecture for the notes of the Unit 1 - Introduction in the subject of Database Management System:

# Database System Concept and Architecture

- A database is a collection of related data which represents some aspect of the real world.
- A database management system (DBMS) is a software system that allows users to define, create and maintain a database and provides controlled access to the data.
- The overall structure of a DBMS can be thought of as consisting of three levels:

## Internal Level:
- The internal level refers to the internal storage structures and access methods used by the system. e.g. hash tables, B-trees, etc.

## Conceptual Level:
- The conceptual level refers to the logical organization of the database. e.g. entities, attributes, relationships, etc. This is defined using a data model.
- The widely used data models are:
    - Relational model: Data is organized into one or more tables (relations) of columns and rows.
    - Object-oriented model: Data is organized into objects with attributes and methods.
    - Hierarchical model: Data is organized into tree-like structures with parent-child relationships.
    - Network model: Data is organized into entities with owner-member relationships.

## External Level:
- The external level refers to the way users view the database. e.g. the tables/forms/reports they interact with. This is defined by the database schema.
- The database schema is the overall design of the database. It defines the data structures used to store and organize the data, as well as the relationships between them.

The main components of a DBMS are:

- Data dictionary: Stores metadata about the database e.g. table & column names, data types, constraints, etc.
- Query processor: Converts the user's queries into an efficient execution plan to retrieve the required data.
- Transaction manager: Manages the execution of transactions and maintains the consistency and integrity of the database.
- Storage manager: Interacts with the operating system to store, retrieve and update data from the database.
- File manager: Keeps track of free space in the database and allocates storage space as needed.
- Authorization and integrity manager: Enforces security and integrity constraints defined for the database.

[Detailed ASCII diagrams, codes, markdown tables, examples, applications, advantages, disadvantages, etc. can be included here if required.]