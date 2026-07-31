### User Defined Functions

- User defined functions (UDFs) are custom functions that can be created and used in various Hadoop eco system frameworks, such as Hive, Pig, and Spark.
- UDFs allow users to extend the functionality of the existing frameworks and perform complex operations that are not supported by the built-in functions.
- UDFs can be written in different programming languages, such as Java, Python, Scala, etc., depending on the framework and the interface used.
- UDFs can be categorized into different types, such as scalar, aggregate, table, and window functions, based on the input and output they produce.
- Scalar UDFs take one or more input values and return a single output value. For example, a UDF that converts temperature from Celsius to Fahrenheit.
- Aggregate UDFs take a set of input values and return a single output value. For example, a UDF that calculates the average of a column.
- Table UDFs take one or more input values and return a table of output values. For example, a UDF that splits a string into multiple words.
- Window UDFs take a set of input values and return a single output value for each input value, based on a specified window or partition. For example, a UDF that calculates the rank of a value within a group.