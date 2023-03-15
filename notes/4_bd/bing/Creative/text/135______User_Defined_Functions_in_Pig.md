#### User Defined Functions in Pig

- User defined functions (UDFs) are custom functions that can be written in Java, Python, Ruby, or Groovy and used in Pig scripts to perform specific tasks that are not supported by the built-in functions.
- UDFs can be used to manipulate data, perform complex calculations, call external services, or interact with other systems.
- UDFs can be classified into four types: Eval, Filter, Load, and Store.
- Eval functions take one or more input values and return a single output value. They can be used in expressions, projections, or as arguments to other functions. For example, UPPER is an eval function that converts a string to uppercase.
- Filter functions take a single input value and return a boolean value. They can be used in the FILTER operator to filter out records that do not satisfy a condition. For example, IsEmpty is a filter function that checks if a bag or a map is empty.
- Load functions take a file name or a URI as an input and return a bag of tuples. They can be used in the LOAD operator to read data from various sources, such as files, databases, or web services. For example, PigStorage is a load function that reads data from files in a specified format.
- Store functions take a bag of tuples as an input and a file name or a URI as an output. They can be used in the STORE operator to write data to various destinations, such as files, databases, or web services. For example, PigStorage is a store function that writes data to files in a specified format.
- To use a UDF in a Pig script, the UDF must be registered using the REGISTER statement, which specifies the name and location of the UDF jar file or script file. For example, REGISTER myudfs.jar; or REGISTER myudfs.py USING jython as myfuncs;
- To invoke a UDF in a Pig script, the UDF name must be prefixed with the namespace, which is either the name of the jar file or the alias given to the script file. For example, myudfs.UPPER($0) or myfuncs.myfunc($0, $1);
- UDFs can also be defined inline using the DEFINE statement, which specifies the name and the class name of the UDF. For example, DEFINE MyUpper myudfs.UPPER; or DEFINE MyFunc myfuncs.myfunc;
- UDFs can also be tested using the ILLUSTRATE operator, which shows an example of how the UDF works on a sample of the input data. For example, ILLUSTRATE MyUpper; or ILLUSTRATE MyFunc;