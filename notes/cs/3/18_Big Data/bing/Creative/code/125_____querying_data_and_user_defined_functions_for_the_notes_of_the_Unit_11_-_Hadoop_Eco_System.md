### Querying Data and User Defined Functions for the Notes of the Unit 11 - Hadoop Eco System

- Apache Hive is a data warehouse system for Apache Hadoop that enables data summarization, querying, and analysis of data stored in Hadoop files.
- HiveQL is a SQL-like dialect used for writing queries in Hive. HiveQL supports a variety of data types, operators, functions, and clauses.
- User-defined functions (UDFs) are custom functions that extend the functionality of HiveQL. UDFs can be written in Java and called from a Hive query .
- There are three types of UDFs in Hive: simple, generic, and table-generating.
  - Simple UDFs take one or more primitive types as input and return a primitive type as output. They are implemented using the org.apache.hadoop.hive.ql.exec.UDF interface.
  - Generic UDFs can take complex types such as arrays, maps, and structs as input and output. They are implemented using the org.apache.hadoop.hive.ql.udf.generic.GenericUDF interface.
  - Table-generating UDFs (also known as UDTFs) can produce multiple rows and columns as output from a single input row. They are implemented using the org.apache.hadoop.hive.ql.udf.generic.GenericUDTF interface.
- To use a UDF in a Hive query, the following steps are required :
  - Write and compile the UDF code in Java using a Hadoop- and Hive-compatible Java project.
  - Export the UDF to a JAR file and copy it to a location accessible by Hive.
  - Register the UDF in Hive using the CREATE FUNCTION statement, specifying the name, class, and type of the UDF.
  - Invoke the UDF in a Hive query using the name defined in the CREATE FUNCTION statement.
- UDFs can improve the performance and expressiveness of Hive queries, but they also have some limitations and challenges:
  - UDFs are executed in a separate Java virtual machine (JVM) from the Impala daemon, which adds overhead and latency to the query execution.
  - UDFs cannot access the query state or context, such as the current database, user, or session variables.
  - UDFs cannot modify the schema or data of the tables involved in the query.
  - UDFs must be compatible with the data types and formats supported by Hive and Impala.
  - UDFs must be tested and debugged carefully to ensure correctness and robustness.