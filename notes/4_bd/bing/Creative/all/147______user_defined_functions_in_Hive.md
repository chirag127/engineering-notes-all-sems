# User Defined Functions in Hive

- User defined functions (UDFs) are custom functions that can be developed in Java, integrated with Hive, and built on top of a Hadoop cluster to allow for efficient and complex computation that would not otherwise be possible with simple SQL.
- UDFs can be useful and very powerful, and yet online documentation is pretty weak.
- UDFs can be classified into three types: simple UDFs, generic UDFs, and UDAFs.
- Simple UDFs are the most common type of UDFs. They take one or more primitive types as input and return a single primitive type as output.
- Generic UDFs are more flexible and can handle complex types such as arrays, maps, and structs as input and output.
- UDAFs (User Defined Aggregate Functions) are used to perform aggregation operations on multiple rows of data and return a single value as output.
- To create a UDF, one needs to write a Java class that extends the appropriate interface (org.apache.hadoop.hive.ql.exec.UDF for simple UDFs, org.apache.hadoop.hive.ql.udf.generic.GenericUDF for generic UDFs, and org.apache.hadoop.hive.ql.udf.generic.GenericUDAFEvaluator for UDAFs) and implement the required methods .
- To use a UDF in Hive, one needs to register the UDF with Hive by using the CREATE FUNCTION command and specifying the name of the function, the name of the Java class, and the path to the JAR file containing the class  .
- Alternatively, one can use the ADD JAR command to add the JAR file to the classpath and then use the CREATE TEMPORARY FUNCTION command to register the UDF for the current session only.
- To check which UDFs are loaded in the current Hive session, one can use the SHOW FUNCTIONS command.
- To invoke a UDF in a Hive query, one can use the function name followed by the arguments in parentheses, just like a built-in function .
- Some examples of UDFs are:

  - datediff: returns the number of days between two dates
  - date_add: returns the date after adding a number of days to a given date
  - date_sub: returns the date after subtracting a number of days from a given date
  - decode: returns the string representation of a binary value using a specified character set
  - ngrams: returns the n-grams from a set of words
  - concat_ws: returns the concatenation of strings with a separator
  - percentile: returns the approximate percentile value of a numeric column at a given percentage