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