### User Defined Functions

- User defined functions (UDFs) are functions that can be implemented by the developer to extend the functionality of Hadoop frameworks such as Pig and Hive.
- UDFs can be written in Java or other languages such as Python, Ruby, or Scala, and can be called from Pig scripts or Hive queries.
- UDFs can be used to perform custom processing, transformation, filtering, or aggregation on the data stored in Hadoop.
- UDFs can be classified into three types based on their input and output:
  - Scalar UDFs: These functions take one or more input values and return a single output value. For example, a function that converts a string to uppercase or a function that calculates the square root of a number.
  - Aggregate UDFs: These functions take a group of values and return a single value. For example, a function that computes the average or the median of a set of numbers.
  - Table UDFs: These functions take one or more input values and return a table of values. For example, a function that splits a string into words or a function that generates a sequence of numbers.
- UDFs can be registered and invoked in different ways depending on the framework:
  - In Pig, UDFs can be registered using the REGISTER statement, and invoked using the DEFINE statement or directly in the script. For example:

  ```
  REGISTER myudfs.jar; -- register a JAR file containing UDFs
  DEFINE myfunc myudfs.MyFunc; -- define an alias for a UDF
  A = LOAD 'data.txt' AS (name:chararray, age:int); -- load some data
  B = FOREACH A GENERATE myfunc(name); -- apply the UDF to the data
  ```
  - In Hive, UDFs can be registered using the ADD JAR statement, and invoked using the CREATE FUNCTION statement or directly in the query. For example:

  ```
  ADD JAR myudfs.jar; -- add a JAR file containing UDFs
  CREATE TEMPORARY FUNCTION myfunc AS 'myudfs.MyFunc'; -- create a temporary function for a UDF
  SELECT name, myfunc(age) FROM data; -- apply the UDF to the data
  ```