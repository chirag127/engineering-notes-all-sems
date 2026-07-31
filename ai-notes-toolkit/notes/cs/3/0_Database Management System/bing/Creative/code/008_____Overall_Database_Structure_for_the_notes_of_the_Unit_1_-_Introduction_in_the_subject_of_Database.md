### Overall Database Structure

A database is a collection of information that is related to a particular subject or purpose, such as tracking customer orders or maintaining a music collection. A database can be considered a structure in realization of the database language. A database management system (DBMS) is a software that extracts information from the database in response to queries.

The overall database structure consists of the following components:

- **Database schema**: This describes how real-world entities are modeled in the database. It defines the logical structure of the data and the relationships among the data items. A database schema can be represented by a set of rules, diagrams, or tables.
- **Query processor**: This is the component that processes the queries issued by the users or applications. It parses, analyzes, optimizes, and executes the queries using the database schema and the data stored in the database. It also handles the transactions, concurrency control, and recovery mechanisms.
- **Storage manager**: This is the component that manages the allocation of space on disk storage and the data structures used to represent the stored data. It provides functions for creating, deleting, modifying, and retrieving data from the database. It also performs buffering, caching, indexing, and hashing techniques to improve the performance and reliability of the database.
- **Disk storage**: This is the component that stores the actual data of the database on the physical disk devices. It consists of files, pages, records, and fields that store the data values. It also maintains the metadata, such as the file headers, pointers, and statistics, that describe the properties and locations of the data.

The following diagram illustrates the overall database structure:

```
+-----------------+
|  Query Processor|
+-----------------+
        |
        |
+-----------------+
|  Storage Manager|
+-----------------+
        |
        |
+-----------------+
|   Disk Storage  |
+-----------------+
```