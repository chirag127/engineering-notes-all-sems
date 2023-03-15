#### User Defined Functions in Pig

- User defined functions (UDFs) are custom functions that can be written in Java, Python, or other languages and used in Pig scripts to perform specific tasks that are not supported by the built-in functions.
- UDFs can be used to manipulate data, perform complex calculations, call external services, or implement custom logic that is not possible with the existing Pig operators and functions.
- UDFs can be classified into four types based on their input and output: Eval functions, Filter functions, Load/Store functions, and Aggregate functions.
- Eval functions take one or more input values and return a single output value. For example, a UDF that converts a string to uppercase or a UDF that calculates the distance between two points.
- Filter functions take a single input value and return a boolean value indicating whether the input satisfies a certain condition. For example, a UDF that checks if a string contains a specific word or a UDF that filters out records based on some criteria.
- Load/Store functions are used to read data from or write data to external sources, such as files, databases, or web services. For example, a UDF that loads data from a JSON file or a UDF that stores data to a MongoDB collection.
- Aggregate functions take a bag of values as input and return a single output value that summarizes the input. For example, a UDF that computes the average, median, or standard deviation of a set of numbers or a UDF that concatenates a set of strings.

- To write a UDF in Java, one needs to extend the appropriate abstract class from the org.apache.pig.EvalFunc, org.apache.pig.FilterFunc, org.apache.pig.LoadFunc, or org.apache.pig.Algebraic interface, depending on the type of the UDF, and implement the required methods.
- To write a UDF in Python, one needs to use the @outputSchema decorator to specify the output schema of the UDF and define a function that takes the input arguments and returns the output value.
- To use a UDF in a Pig script, one needs to register the UDF jar file or Python script using the REGISTER statement and then invoke the UDF by its name and pass the required arguments. For example, REGISTER myudfs.jar; A = LOAD 'data.txt' AS (name:chararray, age:int); B = FOREACH A GENERATE myudfs.ToUpper(name), myudfs.AgeGroup(age);