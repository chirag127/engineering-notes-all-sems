 Here is the content in markdown format for user defined functions in Hive:

#### User Defined Functions in Hive

User Defined Functions (UDFs) in Hive allow you to define your own functions to be used in Hive queries. This provides flexibility to calculate complex data or implement custom logic that is not available in the built-in Hive functions.

There are three types of UDFs in Hive:

1. UDFs (User Defined Functions): Takes one or more scalar values as input and returns a single scalar value as output.

2. UDAFs (User Defined Aggregate Functions): Takes multiple input values and returns a single aggregate value.

3. UDTFs (User Defined Table Functions): Takes one or more input rows and generates zero or more output rows.

**Advantages:**
- Provide custom functionality not available in built-in functions
- Reuse custom logic and avoid repeated complex calculations
- Extract business logic from queries for better readability and maintainability

**Steps to create UDFs:**
1. Implement the interface `org.apache.hadoop.hive.ql.exec.UDF` for UDF or extend the class `org.apache.hadoop.hive.ql.udf.generic.GenericUDF` for generic UDFs.
2. Build and package the UDF into a JAR file.
3. Register the UDF in Hive by using the CREATE FUNCTION statement and specifying the JAR file location.
4. Use the UDF in Hive queries.

**Considerations:**
- UDFs add processing overhead and can slow down query execution.
- UDF code is not optimized - use built-in functions whenever possible for performance.
- UDF JAR files must be available on all nodes in the cluster for distributed execution.
- Use descriptive function names and parameter names for easy understanding.

**Examples:**

UDF to convert Celsius to Fahrenheit:
```
CREATE FUNCTION celsius_to_fahrenheit AS 'celsius_udf.CelsiusToFahrenheit' USING JAR 'celsius_udf.jar';

SELECT celsius_to_fahrenheit(15) FROM dual;
-- Returns 59
```

UDAF to calculate average of a numeric column:
```
CREATE FUNCTION average_udf AS 'average_udf.AverageUDAF' USING JAR 'average_udf.jar';

SELECT average_udf(col) FROM table;
```