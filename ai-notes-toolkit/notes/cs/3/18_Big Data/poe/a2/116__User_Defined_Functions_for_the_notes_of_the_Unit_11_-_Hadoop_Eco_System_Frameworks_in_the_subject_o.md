 Here is the content in markdown format without any emojis or external links and in a formal tone:

### User Defined Functions for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data

1. UDFs are programming constructs that allow you to define custom functions to operate on rows, expressions, and perform other processing on DataFrames or SQL queries.
2. UDFs allow you to extend the vocabulary of Spark SQL with your own functions. This can be used to perform custom data processing logic or integrate with external machine learning libraries.
3. There are two types of UDFs:

- Scalar functions: Take zero or more rows as input and return a single value as output.
- Aggregate functions: Take zero or more rows as input and return multiple rows as output.

4. To create a UDF, you have to:

- Define the function in Python.
- Register the function to create a UDF object.
- Invoke the UDF in SQL or DataFrame operations.

5. UDFs can be reused across queries and sessions. They execute on executors and are Scala/Java/Python functions underneath.

Does this content meet your requirements? Let me know if you would like me to modify or add anything.