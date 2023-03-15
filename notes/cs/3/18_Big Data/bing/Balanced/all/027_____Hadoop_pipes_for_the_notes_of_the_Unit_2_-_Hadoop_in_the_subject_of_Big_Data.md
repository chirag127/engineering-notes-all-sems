# Hadoop Pipes

- Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce .
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function .
- Pipes does not use JNI (Java Native Interface), which means that the C++ code does not need to be compiled for a specific platform.
- Pipes provides a set of C++ classes and methods that wrap the Java classes and methods of the Hadoop MapReduce framework .
- To use Pipes, the C++ code needs to implement the Mapper and Reducer interfaces, and optionally the RecordReader and RecordWriter interfaces .
- The C++ code also needs to link with the libhadooppipes.a and libhadooputils.a libraries, which are provided by the Hadoop distribution .
- To run a Pipes job, the Hadoop Pipes command is used, which takes the same arguments as the Hadoop Streaming command, except that the -mapper and -reducer options specify the C++ executables instead of the scripts  .
- The Hadoop Pipes command also requires the -libjars option to specify the hadoop-core.jar and hadoop-pipes.jar files, which are needed by the Java side of the Pipes framework .
- A Pipes job can be run on any platform that supports sockets, as long as the C++ code is compiled for that platform  .
- A Pipes job can handle large data records by using custom RecordReader and RecordWriter implementations that split the records into smaller chunks and send them over the socket.