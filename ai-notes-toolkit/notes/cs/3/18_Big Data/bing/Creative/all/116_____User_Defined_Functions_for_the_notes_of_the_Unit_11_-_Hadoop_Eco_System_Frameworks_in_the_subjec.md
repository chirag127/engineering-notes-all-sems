# User Defined Functions

User defined functions (UDFs) are functions that can be implemented by the developer to extend the functionality of Hadoop and its ecosystem frameworks, such as Pig and Hive. UDFs can be called in almost all Hadoop operators and can perform custom processing on the data.

## Types of UDFs

There are three main types of UDFs in Hadoop:

- **Scalar UDFs**: These are functions that take one or more input values and return a single output value. For example, a function that converts a string to uppercase or a function that calculates the square root of a number. Scalar UDFs can be used in expressions, filters, projections, and joins.

- **Aggregate UDFs**: These are functions that take a group of values and return a single value. For example, a function that calculates the average, sum, count, or maximum of a group of values. Aggregate UDFs can be used in group by clauses and window functions.

- **Table UDFs**: These are functions that take one or more input values and return a table of values. For example, a function that splits a string into an array of words or a function that generates a sequence of numbers. Table UDFs can be used in lateral views and subqueries.

## How to write a UDF

The steps to write a UDF in Hadoop are:

- **Create a Java class** that extends the appropriate interface or abstract class for the type of UDF. For example, for scalar UDFs, the class should extend `org.apache.hadoop.hive.ql.exec.UDF` or implement `org.apache.hadoop.hive.ql.udf.generic.GenericUDF`. For aggregate UDFs, the class should extend `org.apache.hadoop.hive.ql.exec.UDAF` or implement `org.apache.hadoop.hive.ql.udf.generic.GenericUDAFEvaluator`. For table UDFs, the class should implement `org.apache.hadoop.hive.ql.udf.generic.GenericUDTF`.

- **Override the required methods** for the type of UDF. For example, for scalar UDFs, the method `evaluate` should be overridden to define the logic of the function. For aggregate UDFs, the methods `init`, `iterate`, `merge`, `terminatePartial`, and `terminate` should be overridden to define the logic of the aggregation. For table UDFs, the methods `initialize`, `process`, and `close` should be overridden to define the logic of the table generation.

- **Compile the Java class** into a JAR file and export the UDF to the JAR.

- **Register the UDF** in Hadoop using the `CREATE FUNCTION` or `CREATE TEMPORARY FUNCTION` statement. For example, `CREATE FUNCTION my_udf AS 'com.example.MyUDF' USING JAR 'hdfs:///user/hive/udfs/my_udf.jar';`.

- **Call the UDF** in Hadoop queries using the function name. For example, `SELECT my_udf(col1) FROM table1;`.

## Benefits of UDFs

Some of the benefits of using UDFs in Hadoop are:

- **Customization**: UDFs allow the developer to implement custom logic and functionality that are not available in the built-in functions of Hadoop.

- **Reusability**: UDFs can be reused in multiple queries and across different frameworks, such as Pig and Hive.

- **Performance**: UDFs can improve the performance of Hadoop queries by reducing the number of map-reduce jobs and data shuffling. UDFs can also leverage the distributed processing and parallelism of Hadoop.