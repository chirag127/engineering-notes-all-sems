### Hadoop Pipes

- Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce .
- Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data in parallel on large clusters of commodity hardware in a reliable, fault-tolerant manner.
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function . JNI is not used.
- To use Hadoop Pipes, the following steps are required :
  - Write the map and reduce functions in C++ using the Pipes API.
  - Compile the C++ code into a binary executable file.
  - Write a Java driver class that configures and runs the Pipes job.
  - Compile the Java driver class into a jar file.
  - Run the jar file with the binary executable file as an argument.
- Hadoop Pipes provides some advantages over Streaming, such as:
  - Faster communication between the tasktracker and the map/reduce process, as sockets are more efficient than standard input/output.
  - More control over the map/reduce process, as the Pipes API allows the C++ code to access the task status, counters, and configuration.
  - Better integration with the Hadoop framework, as the C++ code can use the same libraries and data types as the Java code.
- Hadoop Pipes also has some limitations, such as :
  - More complex and error-prone development, as the C++ code has to be compiled and linked with the Pipes libraries, and the Java driver class has to be written separately.
  - Less portability and compatibility, as the binary executable file has to be compatible with the operating system and architecture of the cluster nodes, and the Pipes API may not support all the features of the MapReduce framework.
  - More difficulty in passing large data records to the map/reduce tasks, as the Pipes API expects the input to be a contiguous block of bytes, which may be impractical for some applications.