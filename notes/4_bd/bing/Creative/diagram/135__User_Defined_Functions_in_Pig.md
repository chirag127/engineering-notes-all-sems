User Defined Functions (UDFs) in Pig are custom functions that can be used to perform custom processing on data. UDFs can be written in six languages: Java, Jython, Python, JavaScript, Ruby and Groovy. Java UDFs have the most extensive support and can be used for data load/store, column transformation, and aggregation. Other languages have limited support and can only be used for column transformation.

A UDF in Pig consists of three parts: a class definition, a constructor, and an exec method. The class definition specifies the name and the type of the UDF. The constructor initializes the UDF with any parameters. The exec method takes an input tuple and returns an output value.

The following diagram illustrates the basic architecture of a UDF in Pig:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Pig Script     |     |  Pig Runtime    |     |  UDF Class      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  REGISTER       |---->|  Load UDF Jar   |---->|  Load UDF Class |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  DEFINE         |---->|  Create UDF     |---->|  Call UDF       |
|                 |     |  Instance       |     |  Constructor    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  GENERATE       |---->|  Call UDF       |---->|  Call UDF       |
|                 |     |  exec Method    |     |  exec Method    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The Pig script registers the UDF jar file, defines the UDF name and type, and generates the output using the UDF. The Pig runtime loads the UDF jar file, creates an instance of the UDF class, and calls the exec method of the UDF. The UDF class loads the UDF class, calls the UDF constructor, and executes the UDF logic.