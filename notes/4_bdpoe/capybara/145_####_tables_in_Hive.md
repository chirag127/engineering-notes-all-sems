#### Tables in Hive

Tables in Hive are similar to tables in relational databases. They are used to store data in an organized manner and can be queried using SQL-like queries. Hive tables can be classified into two types: managed tables and external tables.

##### Managed Tables

Managed tables, also known as internal tables, are tables whose data is managed by Hive. In other words, when you create a managed table in Hive, Hive creates a directory in HDFS to store the table data. The table schema, data, and metadata are stored in this directory. 

Advantages of Managed Tables:
- Data is managed by Hive, so it is easy to maintain.
- Data is stored in HDFS, which has built-in fault tolerance and replication.
- Hive can optimize queries on managed tables by creating indexes and partitions.

Disadvantages of Managed Tables:
- Data cannot be accessed outside of Hive.
- Data cannot be shared between different Hive instances.
- Managing data in HDFS can be challenging for some users.

##### External Tables

External tables are tables whose data is not managed by Hive. When you create an external table in Hive, you specify the location of the table data. Hive does not move or modify the data in any way. 

Advantages of External Tables:
- Data can be accessed outside of Hive.
- Data can be shared between different Hive instances.
- Data can be managed by tools other than Hive.

Disadvantages of External Tables:
- Data is not managed by Hive, so it can be challenging to maintain.
- Data is not stored in HDFS, so it does not have built-in fault tolerance and replication.
- Hive cannot optimize queries on external tables.

Mnemonics and Learning Tricks:
- Remember that managed tables are internal to Hive, so their data is managed by Hive. External tables are external to Hive, so their data is not managed by Hive.
- Think of managed tables as being "in-house" and external tables as being "outsourced."

Example:
```
CREATE TABLE employees (
  id INT,
  name STRING,
  salary DOUBLE
) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';

INSERT INTO employees VALUES (1, 'John', 50000.0);
INSERT INTO employees VALUES (2, 'Jane', 60000.0);
INSERT INTO employees VALUES (3, 'Bob', 70000.0);

SELECT * FROM employees;
```

In this example, we create a managed table called "employees" with three columns: "id", "name", and "salary". We then insert three rows into the table and query the table to retrieve all the data.

Applications:
- Storing and querying large amounts of data.
- Data warehousing and business intelligence.
- Data analysis and reporting.