# User Defined Functions

- User defined functions (UDFs) are custom functions that can be used to perform specific tasks on data in Hadoop.
- UDFs can be written in various languages, such as Java, Python, Ruby, or Scala, and can be invoked from different Hadoop frameworks, such as MapReduce, Hive, Pig, or Spark.
- UDFs can be classified into three types based on their input and output:

  - **Scalar UDFs**: These functions take one or more scalar values as input and return a single scalar value as output. For example, a UDF that converts a string to uppercase or a UDF that calculates the square root of a number.
  - **Aggregate UDFs**: These functions take a set of values as input and return a single aggregated value as output. For example, a UDF that computes the average or the sum of a group of values.
  - **Table UDFs**: These functions take one or more tables as input and return a table as output. For example, a UDF that performs a join or a filter operation on two or more tables.

- UDFs can be registered and used in different ways depending on the framework. For example, in Hive, UDFs can be registered using the `CREATE FUNCTION` statement and used in SQL queries. In Pig, UDFs can be registered using the `REGISTER` statement and used in Pig Latin scripts. In Spark, UDFs can be registered using the `spark.udf.register` method and used in Spark SQL or DataFrames.