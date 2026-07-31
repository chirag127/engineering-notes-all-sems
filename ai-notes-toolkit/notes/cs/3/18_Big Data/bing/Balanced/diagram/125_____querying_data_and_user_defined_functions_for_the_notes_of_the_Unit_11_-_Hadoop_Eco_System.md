### Querying Data and User Defined Functions for the Notes of the Unit 11 - Hadoop Eco System

- Querying data in Hadoop is done using Hive, a data warehouse framework that provides a SQL-like dialect called HiveQL for summarizing and analyzing large data sets stored in HDFS .
- HiveQL supports various data types, such as primitive types (int, string, boolean, etc.), complex types (array, map, struct, etc.), and partitioned types (date, timestamp, etc.).
- HiveQL also supports various operators, such as arithmetic, comparison, logical, and bitwise operators, as well as functions, such as aggregate, string, math, date, and conditional functions.
- User defined functions (UDFs) are custom functions that can be written in any programming language, such as Java, Python, or Scala, and plugged into Hive queries using the TRANSFORM clause  .
- UDFs can be used to perform complex calculations, transformations, or tests on column values that are not supported by the built-in functions of Hive .
- UDFs can be categorized into three types: scalar, generic, and table functions .
  - Scalar UDFs take one or more input values and return a single output value .
  - Generic UDFs are similar to scalar UDFs, but they can handle different data types and null values .
  - Table UDFs take one or more input values and return a table of output values .
- UDFs can be created, registered, and used in Hive using the following steps  :
  - Write and compile the UDF code in a Hadoop- and Hive-compatible Java project, and export it to a JAR file .
  - Copy the JAR file to a location accessible by Hive, such as HDFS or a local directory .
  - Register the JAR file and the UDF class name in Hive using the ADD JAR and CREATE FUNCTION commands .
  - Use the UDF in a Hive query by calling its name and passing the required arguments .