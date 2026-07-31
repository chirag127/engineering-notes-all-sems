### Querying Data and User Defined Functions for the Notes of the Unit 11 - Hadoop Eco System

- Querying data in Hadoop is done using **Hive**, a data warehouse system that provides a SQL-like language called **HiveQL** for data analysis and summarization .
- HiveQL supports various data types, such as primitive types (int, string, boolean, etc.), complex types (array, map, struct, etc.), and partitioned types (date, timestamp, etc.).
- HiveQL also supports various operators, such as arithmetic, comparison, logical, and bitwise operators, as well as functions, such as aggregate, string, math, date, and conditional functions.
- User defined functions (UDFs) are custom functions that can be written in Java and used in HiveQL queries to extend the functionality of Hive  .
- UDFs can be classified into three types: simple UDFs, generic UDFs, and table generating UDFs.
- Simple UDFs are the easiest to write and use, as they take one or more primitive types as input and return a primitive type as output.
- Generic UDFs are more flexible and powerful, as they can take complex types as input and output, and can also handle null values and variable arguments.
- Table generating UDFs are also known as user defined table functions (UDTFs), and they can return multiple rows and columns as output from a single input row.
- To use UDFs in Hive, the following steps are required :
  - Write and compile the Java code for the UDF in a Hadoop- and Hive-compatible project, and export it to a JAR file.
  - Copy the JAR file to the Hadoop file system, and register it with Hive using the `ADD JAR` command.
  - Create a temporary or permanent function in Hive using the `CREATE [TEMPORARY] FUNCTION` command, and specify the class name of the UDF in the JAR file.
  - Use the function in HiveQL queries as needed, and drop the function when it is no longer needed using the `DROP [TEMPORARY] FUNCTION` command.