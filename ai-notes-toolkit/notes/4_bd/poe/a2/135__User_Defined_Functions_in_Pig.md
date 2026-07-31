 Here is the content in markdown format with formal tone and without emojis:

#### User Defined Functions in Pig

1. Pig allows users to create their own User Defined Functions (UDFs) to extend the language and to implement custom processing logic.
2. UDFs can be written in Java, Python, JavaScript, Ruby or C++.
3. UDFs can be used in all parts of a Pig Latin script - in the LOAD, FOREACH, FILTER, GROUP, etc.
4. UDFs receive input parameters and return a value. The number and type of input/output parameters depends on the UDF.
5. Input/output parameters can be simple types like int, float, chararray or complex types like tuples and bags.
6. UDFs can access external data sources or libraries to enrich processing.
7. UDFs are registered in the Distributed Cache and are shipped to all nodes.
8. For efficiency, UDFs should be deterministic and avoid excessive I/O.

The above points cover the key highlights of User Defined Functions in Pig. Let me know if you would like me to elaborate on any of the points or explain them in a different way.