#### User Defined Functions in Hive

- User defined functions (UDFs) are custom functions that can be developed in Java, integrated with Hive, and built on top of a Hadoop cluster to allow for efficient and complex computation that would not otherwise be possible with simple SQL.
- UDFs can be useful and very powerful, and yet online documentation is pretty weak.
- UDFs can be classified into three types: simple, generic, and table.
- Simple UDFs are the most common type of UDFs. They take one or more primitive types as input and return a single primitive type as output. For example, a simple UDF can convert a string to uppercase or calculate the square root of a number.
- Generic UDFs are more flexible than simple UDFs. They can take complex types such as arrays, maps, or structs as input and output. For example, a generic UDF can split a string into an array of words or concatenate two arrays into one.
- Table UDFs are also known as user defined table generating functions (UDTFs). They can take one or more primitive types as input and return a table (a set of rows) as output. For example, a table UDF can explode an array into multiple rows or parse a JSON string into a table.
- To create a UDF in Hive, the following steps are required   :
  - Write the Java code for the UDF, implementing the appropriate interface (UDF, GenericUDF, or GenericUDTF) and overriding the necessary methods (evaluate, initialize, or close).
  - Compile the Java code and package it into a JAR file, along with any dependencies.
  - Register the JAR file in Hive using the ADD JAR command or the hive.aux.jars.path property.
  - Register the UDF class in Hive using the CREATE FUNCTION command, specifying the name, return type, and arguments of the UDF.
  - Use the UDF in Hive queries like a normal built-in function, invoking it by its name and passing the required arguments.
- To check which UDFs are loaded in the current Hive session, the SHOW FUNCTIONS command can be used.
- To drop a UDF from Hive, the DROP FUNCTION command can be used.