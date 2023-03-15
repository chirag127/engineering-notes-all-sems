#### Comparison of Hive with traditional databases

Hive is a data warehouse software system that provides data query and analysis on large datasets stored in Hadoop. Hive supports a SQL-like interface called HiveQL, which allows users to perform various operations on the data such as creating tables, loading data, querying, aggregating, joining, etc. Hive is not a full-fledged database, but rather a data warehouse that applies schema on read time, meaning that the data is not validated or transformed until it is queried.

Traditional databases, such as MySQL, PostgreSQL, Oracle, MS SQL Server, etc., are relational database management systems (RDBMS) that store data in structured tables with predefined schemas. Traditional databases enforce schema on write time, meaning that the data is validated and transformed before it is stored in the database. Traditional databases support SQL as the standard query language, and also provide various features such as transactions, indexes, triggers, views, etc.

Some of the main differences between Hive and traditional databases are:

- Hive is designed for batch processing and analytical queries on large datasets, while traditional databases are designed for online transaction processing (OLTP) and operational queries on smaller datasets.
- Hive does not support record-level updates, insertions, and deletions, while traditional databases support these operations using SQL commands such as UPDATE, INSERT, and DELETE.
- Hive does not support transactions, concurrency control, or ACID properties, while traditional databases support these features to ensure data consistency and integrity.
- Hive does not support indexes, triggers, views, or stored procedures, while traditional databases support these features to improve query performance and functionality.
- Hive is very easily scalable at low cost, as it can run on commodity hardware and leverage the distributed storage and processing capabilities of Hadoop. Traditional databases are not very scalable, as they require expensive hardware and complex architectures to scale up or out.
- Hive is based on the Hadoop notion of write once, read many (WORM), meaning that the data is loaded into Hive once and then queried multiple times. Traditional databases support read and write operations on the data at any time.

References:

: https://sensaran.wordpress.com/2016/01/30/comparison-with-hive-with-traditional-database/
: https://www.tutorialslink.com/Articles/A-Comparative-of-Traditional-RDBMS-and-HiveQL-in-Hadoop-Enviromnent/1266
: http://hadooptutorial.info/hive-vs-rdbms
: https://www.geeksforgeeks.org/difference-between-rdbms-and-hive
: https://www.quora.com/How-is-the-Apache-Hive-different-from-the-traditional-database