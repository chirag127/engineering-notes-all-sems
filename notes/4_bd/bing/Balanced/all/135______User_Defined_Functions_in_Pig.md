#### User Defined Functions in Pig

- User defined functions (UDFs) are custom functions that can be written in Java, Python, or other languages and used in Pig scripts to perform specific tasks that are not supported by the built-in functions.
- UDFs can be used to manipulate data, perform complex calculations, call external services, or integrate with other frameworks.
- UDFs can be classified into four types: eval, filter, load/store, and aggregate functions.
- Eval functions take one or more input values and return a single output value. For example, a UDF that converts a string to uppercase or a UDF that calculates the distance between two points.
- Filter functions take a single input value and return a boolean value indicating whether the input satisfies a certain condition. For example, a UDF that filters out records with null values or a UDF that checks if a string matches a regular expression.
- Load/store functions are used to read and write data from and to various sources and formats. For example, a UDF that loads data from a JSON file or a UDF that stores data to a MongoDB collection.
- Aggregate functions take a bag of values as input and return a single output value. For example, a UDF that computes the average, median, or standard deviation of a set of numbers.

- To write a UDF in Java, one needs to extend the appropriate abstract class from the org.apache.pig package and implement the required methods. For example, to write an eval function, one needs to extend the EvalFunc class and implement the exec method.
- To write a UDF in Python, one needs to use the @outputSchema decorator to specify the output schema of the function and the @udfType decorator to specify the type of the function. For example, to write an eval function, one needs to use the @outputSchema("output:chararray") and @udfType("eval") decorators.
- To use a UDF in a Pig script, one needs to register the UDF jar file or the Python script using the REGISTER statement and then invoke the UDF using the function name and the input arguments. For example, to use an eval function named UpperCase that takes a string as input and returns the uppercase version of it, one needs to write:

```
REGISTER UpperCase.jar;
A = LOAD 'data.txt' AS (name:chararray);
B = FOREACH A GENERATE UpperCase(name);
```