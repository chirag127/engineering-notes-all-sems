# User Defined Functions in Pig

- User defined functions (UDFs) are a way to specify custom processing in Apache Pig, a platform for analyzing large data sets.
- UDFs can be implemented in six languages: Java, Jython, Python, JavaScript, Ruby and Groovy.
- UDFs can be used to extend the functionality of Pig and to use a programming language that the user is comfortable with.
- UDFs can be classified into four types based on their functionality and input/output types:
  - Eval functions: These functions take one or more fields of a tuple as input and return a single field as output. For example, UPPER, LOWER, SUBSTRING, etc.
  - Aggregate functions: These functions take a bag of tuples as input and return a single value as output. For example, SUM, AVG, COUNT, etc.
  - Filter functions: These functions take a tuple as input and return a boolean value as output. For example, IsEmpty, IsNull, etc.
  - Load/Store functions: These functions are used to read/write data from/to different sources/formats. For example, PigStorage, TextLoader, JsonLoader, etc.
- To use a UDF in Pig, the user needs to register the UDF with a name and a path to the UDF implementation file. For example, `REGISTER 'myudf.py' USING jython AS myfuncs;`.
- To invoke a UDF in Pig, the user needs to use the registered name and pass the required arguments. For example, `A = LOAD 'data.txt' AS (name, age, salary); B = FOREACH A GENERATE myfuncs.double(salary);`.