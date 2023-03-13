#### HBase vs RDBMS

- HBase and RDBMS are both database management systems that store and manipulate data.
- HBase is a NoSQL database that is based on the Hadoop Distributed File System (HDFS) and supports semi-structured and unstructured data. RDBMS is a relational database that is based on the Structured Query Language (SQL) and supports structured data.
- HBase is designed for horizontal scalability, high availability, and fast random access. RDBMS is designed for vertical scalability, ACID transactions, and complex queries.
- HBase stores data in tables that consist of rows and columns, where each row has a unique key and each column belongs to a column family. RDBMS stores data in tables that consist of rows and columns, where each row has a primary key and each column has a data type and constraints.
- HBase supports sparse tables, where not every row has to have a value for every column. RDBMS supports normalized tables, where data is organized into multiple related tables to avoid redundancy and inconsistency.
- HBase does not support joins, subqueries, or aggregations natively, but relies on external tools such as Hive or Pig to perform these operations. RDBMS supports joins, subqueries, and aggregations natively, and provides various functions and operators to manipulate data.
- HBase does not enforce a schema on the data, but allows the user to define the column families and the compression and encoding options for each column family. RDBMS enforces a schema on the data, and requires the user to define the tables and the columns before inserting data.
- HBase is suitable for applications that need to handle large volumes of data, such as web analytics, social media, or sensor data. RDBMS is suitable for applications that need to handle complex transactions, such as banking, e-commerce, or inventory management.

A possible mnemonic to remember the differences between HBase and RDBMS is:

- HBase is Horizontal, Hadoop, and High-speed.
- RDBMS is Relational, SQL, and Structured.