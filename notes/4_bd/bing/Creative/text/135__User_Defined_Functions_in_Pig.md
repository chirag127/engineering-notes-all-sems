#### User Defined Functions in Pig

- User Defined Functions (UDFs) are functions that can be written by the users to perform custom operations on Pig data.
- UDFs can be written in Java, Python, Ruby, Groovy, or JavaScript and registered with Pig using the `REGISTER` statement.
- UDFs can be used in Pig scripts to extend the functionality of Pig built-in operators and functions.
- UDFs can be classified into four types: Eval, Filter, Load, and Store.
  - Eval functions take one or more input values and return a single output value. For example, `UPPER` is an eval function that converts a string to uppercase.
  - Filter functions take a single input value and return a boolean value. For example, `IsNotNull` is a filter function that checks if a value is not null.
  - Load functions take a file name or a directory name as input and return a relation (a bag of tuples). For example, `PigStorage` is a load function that reads data from a file or a directory using a specified delimiter.
  - Store functions take a relation as input and write it to a file or a directory. For example, `PigStorage` is also a store function that writes data to a file or a directory using a specified delimiter.
- UDFs can be invoked in Pig scripts using the `DEFINE` statement, which assigns an alias to the UDF. For example, `DEFINE myUpper com.example.MyUpper();` defines an alias `myUpper` for a custom UDF `com.example.MyUpper`.
- UDFs can be used in expressions, filters, projections, groupings, orderings, joins, and other operations. For example, `A = LOAD 'data.txt' AS (name:chararray, age:int); B = FOREACH A GENERATE myUpper(name), age;` uses the custom UDF `myUpper` to convert the name field to uppercase.