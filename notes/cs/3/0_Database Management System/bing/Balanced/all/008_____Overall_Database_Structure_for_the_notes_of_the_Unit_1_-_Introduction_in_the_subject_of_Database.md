# Overall Database Structure

A database is a collection of information that is related to a particular subject or purpose, such as tracking customer orders or maintaining a music collection. A database can be considered a structure in realization of the database language. The database system is divided into three components: Query Processor, Storage Manager, and Disk Storage. These are explained as following below:

- **Query Processor**: This component is responsible for interpreting and executing the queries given by the users or applications. It consists of several modules, such as query parser, query optimizer, query executor, etc. The query processor also interacts with the storage manager to access or modify the data in the disk storage.
- **Storage Manager**: This component is responsible for managing the storage and retrieval of data in the disk storage. It consists of several modules, such as buffer manager, file manager, access methods, etc. The storage manager also provides various services, such as data compression, encryption, backup, recovery, etc.
- **Disk Storage**: This component is responsible for storing the data in the physical devices, such as hard disks, flash drives, etc. The data is organized into files, which are further divided into pages or blocks. The disk storage also maintains various metadata, such as file headers, indexes, catalogs, etc.

The database system also uses a database schema to describe how real-world entities are modeled in the database. A database schema consists of the following elements:

- **Tables**: These are the basic units of data storage in a database. Each table represents a set of records or tuples that share the same attributes or fields. For example, a table named Customers may store the information of all the customers of a company.
- **Fields**: These are the individual units of data within a table. Each field represents an attribute or property of the records in the table. For example, a field named CustomerID may store the unique identification number of each customer in the Customers table.
- **Records**: These are the rows or instances of data within a table. Each record represents a single entity or object in the real world. For example, a record in the Customers table may store the information of one customer, such as name, address, phone number, etc.
- **Keys**: These are the fields or combinations of fields that are used to identify or relate the records in the tables. There are different types of keys, such as primary keys, foreign keys, candidate keys, etc. For example, a primary key is a field or combination of fields that uniquely identifies each record in a table, such as CustomerID in the Customers table.
- **Relationships**: These are the associations or links between the tables in a database. There are different types of relationships, such as one-to-one, one-to-many, many-to-many, etc. For example, a one-to-many relationship is a relationship where one record in a table can be related to many records in another table, such as one customer can have many orders.
- **Constraints**: These are the rules or conditions that are applied to the tables, fields, records, or relationships in a database. They are used to ensure the validity, integrity, and consistency of the data in the database. For example, a constraint may specify that a field cannot be null, or that a foreign key must match a primary key in another table.

The database schema can be represented in various ways, such as diagrams, tables, or languages. For example, the following diagram shows a simple database schema for a company that sells products to customers:

![Database schema diagram](https://support.content.office.net/en-us/media/3a9a4f4f-8f7a-4f0f-9b4c-9c9f8f1a0c0a.png)



The following table shows the same database schema in a tabular format:

| Table | Field | Data Type | Key | Constraint |
| --- | --- | --- | --- | --- |
| Customers | CustomerID | Number | Primary | Not Null |
| Customers | FirstName | Text |  | Not Null |
| Customers | LastName | Text |  | Not Null |
| Customers | Address | Text |  |  |
| Customers | City | Text |  |  |
| Customers | State | Text |  |  |
| Customers | ZipCode | Text |  |  |
| Customers | Phone | Text |  |  |
| Products | ProductID | Number