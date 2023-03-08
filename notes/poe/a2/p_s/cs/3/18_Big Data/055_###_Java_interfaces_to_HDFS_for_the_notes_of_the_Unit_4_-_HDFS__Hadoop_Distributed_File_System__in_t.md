 Here is the content in Markdown format for the given topics:

#### User Defined Functions in Pig
- User Defined Functions (UDFs) in Pig allows the user to extend the Pig Latin language with their own functions.
- Pig UDFs can be written in Java, Python, JavaScript, Ruby or C++.
- UDFs can perform complex data analysis that is not built-in as a core function in Pig.
- Steps to write a UDF:
1. Extend the EvalFunc or FilterFunc class for the required usage(Evaluation or Filtering function).
2. Override the exec() method to provide the logic or processing to be done.
3. Build the UDF into a JAR file.
4. Register the UDF using the REGISTER command before using it in the Pig Latin script.
- Advantages: Provides customization and extensibility to Pig Latin. Can be reused across multiple scripts.
- Disadvantages: Needs additional effort to write, compile and package the UDF. May have performance overheads.
- Example: A UDF to calculate the average of a bag of numbers.
- Applications: Performing complex calculations, data validation, data transformation logic, etc.

### Java interfaces to HDFS for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data
- The Java interfaces to access HDFS are:
1. FileSystem - Allows basic file system operations like create, delete, rename, etc.
2. FSDataInputStream - Allows to read data from HDFS.
3. FSDataOutputStream - Allows to write data to HDFS.
4. FileContext - Alternative interface with more functionality. Supports file system paths, opens/creates files and checks file statuses.
- To access HDFS using Java, we need to set up the Hadoop configuration and instantiate a FileSystem/FileContext object by passing the configuration.
- We can then use the respective input/output streams or methods to read/write data to/from HDFS.
- Advantages: Java interfaces provide full functionality of HDFS and are suitable for complex applications.
- Disadvantages: Need to set up Hadoop and its dependencies. Tedious to use for simple operations.
- Examples: Reading a file, writing a file, deleting a directory, etc.
- Applications: Any Java application that needs to access data in HDFS.