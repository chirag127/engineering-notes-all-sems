#### User defined functions in Hive

- User defined functions (UDFs) are custom functions that can be created and used in Hive queries to perform specific tasks that are not supported by the built-in functions.
- UDFs can be written in Java, Python, or any other scripting language that supports the Hive UDF interface.
- UDFs can be categorized into three types: scalar, aggregate, and table.
- Scalar UDFs take one or more input values and return a single output value. For example, a UDF that converts a string to uppercase.
- Aggregate UDFs take a set of input values and return a single output value. For example, a UDF that calculates the average of a column.
- Table UDFs take one or more input values and return a table of output values. For example, a UDF that splits a string into multiple rows.
- To create a UDF in Hive, the following steps are required:
  - Write the UDF code in the chosen language and compile it into a JAR file (for Java) or a ZIP file (for Python).
  - Add the JAR or ZIP file to the Hive classpath using the `ADD JAR` or `ADD FILE` command.
  - Register the UDF with Hive using the `CREATE FUNCTION` command, specifying the name, class, and type of the UDF.
  - Use the UDF in Hive queries by invoking the name and passing the arguments.
- To drop a UDF in Hive, the `DROP FUNCTION` command can be used.
- To list all the UDFs in Hive, the `SHOW FUNCTIONS` command can be used.