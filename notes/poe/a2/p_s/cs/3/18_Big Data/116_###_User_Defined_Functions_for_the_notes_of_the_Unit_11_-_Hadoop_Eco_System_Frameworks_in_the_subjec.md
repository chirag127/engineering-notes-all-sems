 Here is the content in markdown format for the topic -

### User Defined Functions

User Defined Functions (UDFs) are functions written by the user to extend the functionality of Hive. They enable users to implement their own logic / algorithms that are not already available in Hive.

Some key points about UDFs:

- UDFs are written in Java / Python and then registered with Hive to be used in queries.
- UDFs can be used in the SELECT, WHERE, HAVING clauses of a query. They can be used to calculate complex expressions or implement custom logic.
- UDFs provide a way to push down processing to the MapReduce layer, thereby improving performance.
- Two types of UDFs:

1. Scalar UDFs - Take zero or more columns and return a single column.
2. Aggregate UDFs - Take multiple rows / columns and return a single aggregate value. They are used with GROUP BY.

Advantages of UDFs:

- Provide custom implementations not available in Hive.
- Improve performance by pushing down complex logic to the MapReduce layer.

Disadvantages of UDFs:

- Need separate code to be maintained for the UDF.
- Debugging UDFs can be difficult.
- Performance might not always be better than Hive expressions. UDF invocation has some overhead.

Examples of UDFs:

- A UDF to calculate the logarithm of a value
- A UDF to implement a custom similarity function
- Aggregate UDFs to calculate weighted averages, percentiles, etc.

Applications of UDFs:

- Implementing machine learning algorithms
- Performing custom transformations or calculations
- Adding business specific logic
- etc.