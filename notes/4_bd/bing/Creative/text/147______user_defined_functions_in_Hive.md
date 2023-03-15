#### User Defined Functions in Hive

- User defined functions (UDFs) are custom functions that can be developed in Java, integrated with Hive, and built on top of a Hadoop cluster to allow for efficient and complex computation that would not otherwise be possible with simple SQL.
- UDFs can be useful and very powerful, and yet online documentation is pretty weak.
- UDFs can be classified into three types: simple, generic, and aggregate.
- Simple UDFs are the most common type of UDFs. They take one or more primitive types as input and return a single primitive type as output.
- Generic UDFs are more flexible than simple UDFs. They can take complex types such as arrays, maps, or structs as input or output, and they can also handle null values.
- Aggregate UDFs are also known as user defined aggregate functions (UDAFs). They take a set of values as input and return a single value as output, such as sum, count, or average.
- To create a UDF, one needs to write a Java class that extends the appropriate interface or abstract class depending on the type of UDF.
- For simple UDFs, the interface is org.apache.hadoop.hive.ql.exec.UDF.
- For generic UDFs, the abstract class is org.apache.hadoop.hive.ql.udf.generic.GenericUDF.
- For aggregate UDFs, the abstract class is org.apache.hadoop.hive.ql.udf.generic.GenericUDAFEvaluator.
- The Java class must implement the evaluate method that defines the logic of the UDF.
- The Java class must also be packaged into a JAR file and registered in Hive using the CREATE FUNCTION command.
- To use a UDF in a Hive query, one can simply invoke it by its name and pass the arguments as required.
- To check which UDFs are loaded in the current Hive session, one can use the SHOW FUNCTIONS command.
- To drop a UDF from the current Hive session, one can use the DROP FUNCTION command.
- To list the details of a UDF, such as its class name, type, and usage, one can use the DESCRIBE FUNCTION command.
- Some examples of built-in UDFs in Hive are concat, substr, upper, lower, trim, length, round, floor, ceil, abs, sin, cos, tan, sqrt, log, exp, etc.
- Some examples of custom UDFs in Hive are decode, date_add, date_sub, datediff, etc.