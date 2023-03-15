### Querying Data and User Defined Functions for the Notes of the Unit 11 - Hadoop Eco System

- Querying data in Hadoop means using a SQL-like dialect called HiveQL to perform analysis and summarization of data stored in HDFS.
- HiveQL supports various data types, operators, functions, and clauses to manipulate and query data in Hadoop.
- HiveQL also allows users to create, alter, and drop tables, databases, views, and user-defined functions (UDFs) in Hadoop.
- UDFs are custom functions that extend the functionality of HiveQL by allowing users to write their own application logic for processing column values during a query.
- UDFs can be written in Java, Python, or any other programming language that can interact with Hadoop.
- UDFs can be categorized into three types: scalar, generic, and table.
- Scalar UDFs take one or more input values and return a single output value. They are similar to built-in functions in HiveQL, such as concat, upper, lower, etc.
- Generic UDFs are more flexible and can handle complex data types, such as arrays, maps, and structs. They can also implement custom logic for null handling, type conversion, and exception handling.
- Table UDFs take one or more input tables and return one or more output tables. They are useful for performing transformations, aggregations, and joins on large data sets.
- To use a UDF in a Hive query, the user needs to register the UDF with Hive using the CREATE FUNCTION statement, and then call the UDF using the SELECT statement.
- The syntax for creating a UDF is:

```sql
CREATE [TEMPORARY] FUNCTION [db_name.]function_name AS class_name
[USING JAR|FILE|ARCHIVE 'file_uri' [, JAR|FILE|ARCHIVE 'file_uri'] ];
```

- The syntax for calling a UDF is:

```sql
SELECT [db_name.]function_name(arguments) FROM table_name;
```

- Here are some examples of UDFs in Hive:

```sql
-- A scalar UDF that converts a string to uppercase
CREATE FUNCTION upper AS 'org.apache.hadoop.hive.ql.udf.UDFUpper';
SELECT upper(name) FROM employees;

-- A generic UDF that splits a string into an array of substrings
CREATE FUNCTION split AS 'org.apache.hadoop.hive.ql.udf.generic.GenericUDFSplit';
SELECT split(address, ',') FROM customers;

-- A table UDF that explodes an array into multiple rows
CREATE FUNCTION explode AS 'org.apache.hadoop.hive.ql.udf.generic.GenericUDFExplode';
SELECT id, explode(interests) FROM users;
```

- UDFs can be dropped using the DROP FUNCTION statement, and their information can be retrieved using the DESCRIBE FUNCTION statement.