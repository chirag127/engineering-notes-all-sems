### Database System Concepts and Architecture

A database is an organized collection of data, stored and accessed electronically. A database management system (DBMS) is a software system that enables users to define, create, maintain, and control access to the database.

The architecture of a database system is greatly influenced by the underlying computer system on which the database is running. The main components of a database system are:

1. **Storage Manager**: responsible for storing, retrieving, and updating data in the database.
2. **Query Processor**: responsible for interpreting and executing queries submitted by users.
3. **Transaction Manager**: responsible for ensuring the atomicity, consistency, isolation, and durability (ACID) properties of transactions.
4. **Metadata**: data that describes the structure of the database, including the schema, data types, and constraints.

The architecture of a database system can be divided into three levels:

1. **External Level**: the user's view of the database. This level describes how the data is presented to the user.
2. **Conceptual Level**: the community view of the database. This level describes the logical structure of the data, independent of how it is stored or presented to the user.
3. **Internal Level**: the physical representation of the data in the database. This level describes how the data is stored and accessed on the underlying computer system.

The process of mapping between the external, conceptual, and internal levels is known as data abstraction. This allows the database system to hide the complexity of data storage and manipulation from the user, providing a simpler and more user-friendly interface.