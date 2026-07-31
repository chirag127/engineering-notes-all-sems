Hello, I am Sydney, your AI assistant. I can help you with your study material for Big Data. Here is the content for the topic of User Defined Functions for the notes of the Unit 11 - Hadoop Eco System Frameworks.

### User Defined Functions

- User Defined Functions (UDFs) are custom functions that can be created and used in various Hadoop Eco System Frameworks, such as Hive, Pig, and Spark, to perform specific tasks on the data.
- UDFs can be written in different programming languages, such as Java, Python, Scala, etc., depending on the framework and the interface used.
- UDFs can be classified into different types based on their input and output, such as:
  - Scalar UDFs: These are the simplest type of UDFs that take one or more input values and return a single output value. For example, a UDF that converts the temperature from Celsius to Fahrenheit.
  - Aggregate UDFs: These are UDFs that take a set of input values and return a single output value that is an aggregation of the input values. For example, a UDF that calculates the average of a column of numbers.
  - Table UDFs: These are UDFs that take one or more input values and return a table of output values. For example, a UDF that splits a string into multiple words and returns a table of words.
  - Window UDFs: These are UDFs that take a set of input values and return a set of output values that are computed based on a sliding window over the input values. For example, a UDF that calculates the moving average of a column of numbers over a window of 3 rows.
- UDFs can be registered and invoked in different ways depending on the framework and the interface used. For example, in Hive, UDFs can be registered using the `CREATE FUNCTION` statement and invoked using the `SELECT` statement. In Pig, UDFs can be registered using the `REGISTER` statement and invoked using the `FOREACH` statement. In Spark, UDFs can be registered using the `spark.udf.register` method and invoked using the `selectExpr` method.
- UDFs can provide various benefits, such as:
  - Customization: UDFs can enable the users to perform custom operations on the data that are not supported by the built-in functions of the framework.
  - Reusability: UDFs can be reused across different queries and scripts, reducing the code duplication and maintenance efforts.
  - Performance: UDFs can improve the performance of the queries and scripts by reducing the number of steps and intermediate data involved in the processing.