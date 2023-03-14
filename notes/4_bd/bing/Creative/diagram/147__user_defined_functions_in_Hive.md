User defined functions in Hive are custom functions that can be written in Java and integrated with Hive to perform complex operations that are not possible with the built-in functions. There are two types of user defined functions in Hive: simple UDF and generic UDF. A simple UDF extends the org.apache.hadoop.hive.ql.exec.UDF class and implements a single evaluate() method that takes and returns primitive types. A generic UDF extends the org.apache.hadoop.hive.ql.udf.generic.GenericUDF class and implements three methods: initialize(), evaluate() and getDisplayString(). A generic UDF can handle complex types such as structs, maps and arrays, and can also support variable arguments and overloading.

The following diagram illustrates the basic architecture of a user defined function in Hive:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Hive Client   |     |   Hive Server   |     |   Hadoop Job    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |  CREATE FUNCTION      |                        |
      |----------------------->|                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |  LOAD JAR FILE         |
      |                        |----------------------->|
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |  SELECT UDF(...)      |                        |
      |----------------------->|                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |  EXECUTE UDF           |
      |                        |----------------------->|
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |  RETURN RESULT         |
      |                        |<-----------------------|
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |  DISPLAY RESULT        |                        |
      |<-----------------------|                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
```