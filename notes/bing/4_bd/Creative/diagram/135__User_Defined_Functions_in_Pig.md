User Defined Functions (UDFs) are custom functions that can be used to perform specific processing in Apache Pig. UDFs can be implemented in six languages: Java, Jython, Python, JavaScript, Ruby and Groovy. UDFs are different from built-in functions, which are predefined and do not need to be registered.

The following diagram illustrates the basic architecture of a User Defined Function in Pig:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Pig Script    |      |   Pig Latin     |      |   Pig Runtime   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  LOAD data;     |      |                 |      |                 |
|  DEFINE func    |----->|  Register UDF   |----->|  Load UDF class |
|  data = FOREACH |      |                 |      |                 |
|  GENERATE func; |      |                 |      |                 |
|  STORE data;    |      |                 |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The steps involved in using a UDF are:

- Write the UDF code in one of the supported languages and compile it into a JAR file (for Java) or a script file (for other languages).
- Load the data to be processed using the LOAD statement in the Pig script.
- Define the UDF using the DEFINE statement and provide the name, path and arguments of the UDF.
- Register the UDF using the REGISTER statement and provide the JAR file or script file name.
- Apply the UDF to the data using the FOREACH or FILTER statement and generate the output.
- Store the output using the STORE statement in the Pig script.