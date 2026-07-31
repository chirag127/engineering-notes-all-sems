#### User Defined Functions in Pig

- User defined functions (UDFs) are a way to specify custom processing in Pig.
- UDFs can be implemented in six languages: Java, Jython, Python, JavaScript, Ruby and Groovy.
- UDFs can be used to perform operations that are difficult or impossible to express in Pig Latin, such as complex calculations, text processing, data cleansing, etc.
- UDFs can be registered and invoked in Pig scripts using the REGISTER and DEFINE statements.
- UDFs can be categorized into four types based on their input and output: Eval functions, Load/Store functions, Filter functions and Aggregate functions.
- Eval functions take one or more fields as input and return one or more fields as output. They can be used in expressions, FOREACH statements, etc.
- Load/Store functions take a file name or a storage system as input and return a bag of tuples as output. They can be used in LOAD and STORE statements to read and write data from various sources and formats.
- Filter functions take a tuple as input and return a boolean value as output. They can be used in FILTER statements to filter out unwanted records.
- Aggregate functions take a bag of tuples as input and return a single value as output. They can be used in GROUP BY statements to perform aggregations such as sum, count, average, etc.