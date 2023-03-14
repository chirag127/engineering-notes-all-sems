#### Tables in Hive

- Tables in Hive are similar to tables in a relational database management system, except that they store data in HDFS or other storage systems accessible by the cluster    .
- Tables in Hive are broadly classified into two types: internal tables and external tables  .
- Internal tables are also known as managed tables, because Hive manages their data and metadata. When an internal table is dropped, both the data and the metadata are deleted  .
- External tables are also known as unmanaged tables, because Hive does not manage their data. When an external table is dropped, only the metadata is deleted, but the data remains intact  .
- Internal tables are suitable for data that is temporary, transient, or exclusive to Hive. External tables are suitable for data that is shared, permanent, or used by other applications  .
- The general syntax for creating a table in Hive is  :

```
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name
(col_name data_type [COMMENT 'col_comment'], ...)
[COMMENT 'table_comment']
[ROW FORMAT row_format]
[FIELDS TERMINATED BY char]
[STORED AS file_format];
```

- To create an internal table, omit the `EXTERNAL` keyword. To create an external table, include the `EXTERNAL` keyword and specify the location of the data using the `LOCATION` clause  .
- To load data into a table, use the `LOAD DATA` command for local or HDFS files, or the `INSERT` command for query results  .
- To display the data in a table, use the `SELECT` command with various clauses and functions  .
- To identify the type of a table, use the `DESCRIBE FORMATTED` command and look for the `Table Type` property. If it is `MANAGED_TABLE`, then it is an internal table. If it is `EXTERNAL_TABLE`, then it is an external table .

- Here is an example of creating an internal table, loading data from a local file, and displaying the data  :

```
-- Create a database named company
CREATE DATABASE company;

-- Use the company database
USE company;

-- Create an internal table named employees with five columns
CREATE TABLE employees (
id INT,
name STRING,
country STRING,
department STRING,
salary INT
);

-- Load data from a local file named employees.txt into the employees table
-- The file has data separated by hyphens
LOAD DATA LOCAL INPATH '/home/user/employees.txt' OVERWRITE INTO TABLE employees;

-- Display the data in the employees table
SELECT * FROM employees;
```

- Here is an example of creating an external table, loading data from an HDFS file, and displaying the data  :

```
-- Create a database named company
CREATE DATABASE company;

-- Use the company database
USE company;

-- Create an external table named customers with four columns
-- Specify the location of the data on HDFS
CREATE EXTERNAL TABLE customers (
id INT,
name STRING,
city STRING,
orders INT
)
LOCATION '/user/hive/customers';

-- Load data from an HDFS file named customers.txt into the customers table
-- The file has data separated by commas
LOAD DATA INPATH '/user/hive/customers.txt' OVERWRITE INTO TABLE customers;

-- Display the data in the customers table
SELECT * FROM customers;
```

- Here is an example of identifying the type of a table :

```
-- Use the company database
USE company;

-- Describe the employees table in a formatted way
DESCRIBE FORMATTED employees;

-- Look for the Table Type property
-- It is MANAGED_TABLE, so it is an internal table
Table Type: MANAGED_TABLE

-- Describe the customers table in a formatted way
DESCRIBE FORMATTED customers;

-- Look for the Table Type property
-- It is EXTERNAL_TABLE,