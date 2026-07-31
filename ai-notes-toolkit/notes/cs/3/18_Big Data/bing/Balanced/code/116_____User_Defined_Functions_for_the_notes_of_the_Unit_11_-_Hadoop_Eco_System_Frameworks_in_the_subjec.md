### User Defined Functions

- User Defined Functions (UDFs) are custom functions that can be applied to data in a Hadoop ecosystem framework, such as Hive, Pig, or Spark.
- UDFs allow users to extend the functionality of the framework by implementing their own logic and algorithms on the data.
- UDFs can be written in various languages, such as Java, Python, Scala, or Ruby, depending on the framework and the interface used.
- UDFs can be categorized into different types based on their input and output, such as:
  - Scalar UDFs: These take one or more input values and return a single output value. For example, a UDF that converts a string to uppercase or a UDF that calculates the square root of a number.
  - Aggregate UDFs: These take a group of input values and return a single output value that summarizes the group. For example, a UDF that computes the average or the standard deviation of a set of numbers.
  - Table UDFs: These take one or more input values and return a table of output values. For example, a UDF that splits a string into multiple words or a UDF that generates a sequence of numbers.
  - Window UDFs: These take a group of input values and return a single output value for each input value based on a window or a partition of the group. For example, a UDF that calculates the cumulative sum or the moving average of a set of numbers.
- UDFs can be registered and invoked in different ways depending on the framework and the interface used. For example, in Hive, UDFs can be registered using the `CREATE FUNCTION` statement and invoked using the `SELECT` statement. In Pig, UDFs can be registered using the `REGISTER` statement and invoked using the `FOREACH` statement. In Spark, UDFs can be registered using the `spark.udf.register` method and invoked using the `withColumn` method.