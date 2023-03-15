#### User Defined Functions in Hive

- User defined functions (UDFs) are custom functions that can be used to perform specific tasks or calculations in Hive queries.
- UDFs can be written in Java, Scala, Python or any other language that Hive supports through its API.
- UDFs can be classified into three types based on their input and output:
  - Scalar UDFs: These are functions that take one or more input values and return a single output value. For example, a function that converts a string to uppercase or a function that calculates the square root of a number.
  - Aggregate UDFs: These are functions that take a set of input values and return a single output value that summarizes the input. For example, a function that calculates the average or the sum of a group of values.
  - Table UDFs: These are functions that take one or more input values and return a table of output values. For example, a function that splits a string into multiple rows or a function that generates a sequence of numbers.
- To use a UDF in Hive, the following steps are required:
  - Write the UDF code in the chosen language and compile it into a JAR file.
  - Register the JAR file in Hive using the `ADD JAR` command or the `hive.aux.jars.path` configuration property.
  - Register the UDF class in Hive using the `CREATE [TEMPORARY] FUNCTION` command and specify the name, return type and arguments of the function.
  - Use the UDF in Hive queries by invoking the function name with the appropriate arguments.