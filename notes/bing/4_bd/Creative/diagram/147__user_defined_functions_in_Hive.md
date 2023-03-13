User defined functions (UDFs) in Hive are custom functions that can be developed in Java, integrated with Hive, and built on top of a Hadoop cluster to allow for efficient and complex computation that would not otherwise be possible with simple SQL. They can be useful and very powerful, and yet online documentation is pretty weak.

There are three types of UDFs in Hive:

- UDF: This type of UDF takes one or more columns as input and returns a single value as output. For example, a UDF that converts a string to uppercase.
- UDAF: This type of UDF takes multiple rows as input and returns a single value as output. For example, a UDAF that calculates the average of a column.
- UDTF: This type of UDF takes one or more columns as input and returns multiple rows as output. For example, a UDTF that splits a string into words.

The following diagram illustrates the basic architecture of a UDF in Hive using ASCII art:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Hive CLI     |      |    HiveServer   |      |    Hadoop MR    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  ADD JAR udf.jar|----->|  ADD JAR udf.jar|----->|  ADD JAR udf.jar|
|                 |      |                 |      |                 |
|  CREATE FUNCTION|----->|  CREATE FUNCTION|----->|  CREATE FUNCTION|
|  my_udf AS      |      |  my_udf AS      |      |  my_udf AS      |
|  'com.example.  |      |  'com.example.  |      |  'com.example.  |
|  MyUDF'         |      |  MyUDF'         |      |  MyUDF'         |
|                 |      |                 |      |                 |
|  SELECT my_udf( |----->|  SELECT my_udf( |----->|  SELECT my_udf( |
|  col) FROM table|      |  col) FROM table|      |  col) FROM table|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The steps involved in creating and using a UDF in Hive are    :

- Write a Java class that extends the UDF, UDAF or UDTF abstract class and implements the evaluate method with the desired logic.
- Compile the Java class and package it into a JAR file.
- Copy the JAR file to a location accessible by Hive, such as HDFS or a local directory.
- Use the ADD JAR command on the Hive CLI or HiveServer to register the JAR file with Hive.
- Use the CREATE FUNCTION command to create a function name and associate it with the fully qualified class name of the UDF.
- Use the function name in a SELECT statement to apply the UDF to the input columns.