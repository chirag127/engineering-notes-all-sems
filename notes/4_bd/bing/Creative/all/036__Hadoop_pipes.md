#### Hadoop pipes

- Hadoop pipes is the name of the C++ interface to Hadoop MapReduce .
- It allows you to create and run MapReduce jobs with C++ code as the mapper and/or the reducer .
- It can improve the performance of applications that require high numerical computation.
- It uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function .
- It does not use standard input and output or JNI to communicate with the map and reduce code.
- It requires the C++ application code to be compiled and linked with the Hadoop pipes libraries .
- It provides a set of abstract classes that the C++ code needs to implement, such as Mapper, Reducer, RecordReader, RecordWriter, etc .
- It also provides a utility class called HadoopPipes that can launch the C++ application as a MapReduce job .
- It supports counters, status updates, configuration variables, and custom partitioners, comparators, and aggregators .

Some advantages of Hadoop pipes are:

- It can leverage the existing C++ libraries and tools for numerical computation, such as BLAS, LAPACK, etc.
- It can avoid the overhead of serialization and deserialization of data between Java and C++.
- It can use the native C++ data types and containers, such as std::string, std::vector, etc.

Some disadvantages of Hadoop pipes are:

- It requires more effort to compile and link the C++ code with the Hadoop pipes libraries.
- It may not be compatible with some Hadoop features, such as security, compression, etc.
- It may not be portable across different platforms and architectures.

Some examples of Hadoop pipes applications are:

- Matrix multiplication
- K-means clustering
- Word count

Some mnemonics and learning tricks for Hadoop pipes are:

- Remember that pipes uses sockets, not standard input and output or JNI.
- Remember that pipes stands for C++ interface to Hadoop MapReduce .
- Remember that pipes requires the C++ code to implement the abstract classes provided by Hadoop .
- Remember that pipes can improve the performance of numerical applications.