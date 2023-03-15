# Hadoop Pipes

- Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce .
- Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data in parallel on large clusters of commodity hardware in a reliable, fault-tolerant manner.
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function . JNI is not used.
- Hadoop Pipes provides a set of C++ classes and macros that wrap the socket communication and allow the user to implement the map and reduce functions as subclasses of the Mapper and Reducer classes .
- Hadoop Pipes also provides a template program called hadoopStreaming that can be used to launch a Pipes job from the command line .
- Hadoop Pipes requires the user to compile the C++ code and link it with the Pipes library, which is part of the Hadoop distribution  .
- Hadoop Pipes can be used to write MapReduce applications in C++ that can leverage the performance and efficiency of native code, as well as the existing C++ libraries and tools  .
- Hadoop Pipes can also be used to pass large data records to map/reduce tasks by using the RecordReader and RecordWriter interfaces, which allow the user to define how the input and output data are split and serialized.