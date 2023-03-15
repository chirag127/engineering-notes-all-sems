#### User Defined Functions in Pig

- User defined functions (UDFs) are a way to specify custom processing in Pig.
- UDFs can be implemented in six languages: Java, Jython, Python, JavaScript, Ruby and Groovy.
- UDFs can be used to perform operations that are difficult or impossible to express in Pig Latin, such as complex calculations, text processing, data cleansing, etc.
- UDFs can be registered with Pig using the `REGISTER` statement, which specifies the location of the UDF implementation file.
- UDFs can be invoked in Pig Latin scripts using the `DEFINE` statement, which assigns an alias to the UDF and optionally specifies its arguments and return type.
- UDFs can be classified into four types based on their functionality:
  - Eval functions: These functions take one or more input values and return a single output value. Examples are `LOWER`, `UPPER`, `SUBSTRING`, etc.
  - Load/store functions: These functions are used to read and write data from and to various sources and formats. Examples are `PigStorage`, `TextLoader`, `JsonLoader`, etc.
  - Filter functions: These functions take a single input value and return a boolean value indicating whether the input satisfies a certain condition. Examples are `IsEmpty`, `IsNull`, `Matches`, etc.
  - Aggregate functions: These functions take a bag of values and return a single output value that summarizes the input. Examples are `SUM`, `AVG`, `COUNT`, etc.