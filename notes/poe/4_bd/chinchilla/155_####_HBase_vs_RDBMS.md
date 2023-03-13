#### HBase vs RDBMS

HBase and RDBMS are two different types of databases that are used for different purposes. Here are some key differences between HBase and RDBMS:

##### HBase

HBase is a NoSQL database that is designed to handle large amounts of structured and unstructured data. Here are some key features of HBase:

- **Column-oriented:** HBase stores data in columns rather than rows, making it more efficient for data retrieval.
- **Distributed:** HBase is designed to run on a cluster of computers, making it highly scalable and fault-tolerant.
- **Schemaless:** HBase does not enforce a schema, allowing for more flexibility in data storage and retrieval.
- **Key-value store:** HBase stores data in key-value pairs, making it easy to search and retrieve data.

##### RDBMS

RDBMS stands for Relational Database Management System. It is a type of database that is based on the relational model. Here are some key features of RDBMS:

- **Table-oriented:** RDBMS stores data in tables, with each table having a predefined schema.
- **ACID-compliant:** RDBMS follows the ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring data consistency and reliability.
- **SQL-based:** RDBMS uses SQL (Structured Query Language) for data manipulation and retrieval.
- **Relational:** RDBMS stores data in a relational manner, with each table having relationships with other tables.

##### Differences between HBase and RDBMS

Here are some key differences between HBase and RDBMS:

- **Data model:** HBase stores data in a column-oriented manner, while RDBMS stores data in a table-oriented manner.
- **Schema enforcement:** HBase does not enforce a schema, while RDBMS enforces a predefined schema.
- **Scalability:** HBase is highly scalable and fault-tolerant, while RDBMS has limitations on scalability.
- **Query language:** HBase does not use SQL for data retrieval, while RDBMS uses SQL for data manipulation and retrieval.
- **Data types:** HBase supports a limited set of data types, while RDBMS supports a wide range of data types.
- **Consistency:** HBase does not provide strong consistency guarantees, while RDBMS provides strong consistency guarantees.

##### Mnemonics and learning tricks:

- One possible mnemonic to remember the difference between HBase and RDBMS is to think of HBase as a "horizontal" database (with data stored in columns), while RDBMS is a "vertical" database (with data stored in tables). 
- Another possible mnemonic is to think of HBase as a "flexible" database (with no enforced schema) and RDBMS as a "rigid" database (with a predefined schema).