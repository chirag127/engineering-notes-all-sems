#### User Defined Functions in Pig

- User Defined Functions (UDFs) are functions that can be written by the user to perform custom operations on Pig data.
- UDFs can be written in Java, Python, Ruby, Groovy, or JavaScript and registered with Pig using the REGISTER statement.
- UDFs can be used in Pig scripts to transform, filter, join, group, or aggregate data.
- UDFs can be classified into four types: Eval, Filter, Load, and Store.

  - Eval functions take one or more input values and return a single output value. They can be used in expressions, projections, or assignments. For example, UPPER is an eval function that converts a string to uppercase.
  - Filter functions take a single input value and return a boolean value. They can be used in the FILTER operator to select records that satisfy a condition. For example, IsEmpty is a filter function that checks if a bag or map is empty.
  - Load functions take a file name or a directory name as input and return a bag of tuples. They can be used in the LOAD operator to read data from external sources. For example, PigStorage is a load function that reads data from files in a specified format.
  - Store functions take a bag of tuples as input and a file name or a directory name as output. They can be used in the STORE operator to write data to external sources. For example, PigStorage is also a store function that writes data to files in a specified format.

- UDFs can be invoked by using their fully qualified class name or by using an alias defined by the DEFINE statement. For example, DEFINE myUpper com.example.MyUpper; A = LOAD 'data.txt' AS (name:chararray); B = FOREACH A GENERATE myUpper(name);
- UDFs can be tested using the ILLUSTRATE operator, which shows an example of how the UDF works on a sample of data.
- UDFs can be packaged into JAR files and distributed to other users or clusters. The JAR files can be registered with Pig using the REGISTER statement or the -Dpig.additional.jars property.
- UDFs can be documented using the @description, @param, and @return annotations in the Java code. The documentation can be viewed using the DESCRIBE FUNCTION statement. For example, DESCRIBE FUNCTION myUpper;