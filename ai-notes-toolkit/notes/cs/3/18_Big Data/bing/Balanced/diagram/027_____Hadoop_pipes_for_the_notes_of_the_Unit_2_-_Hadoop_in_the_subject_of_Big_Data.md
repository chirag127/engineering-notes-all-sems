### Hadoop Pipes

- Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce .
- Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data in parallel on large clusters of commodity hardware in a reliable, fault-tolerant manner.
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function .
- Pipes does not use JNI (Java Native Interface), which is a programming framework that allows Java code to call and be called by native applications or libraries written in other languages such as C, C++ and assembly.
- Pipes provides a set of classes and methods that allow the user to implement the map and reduce functions in C++, and to access the Hadoop configuration and file system from C++ code .
- Pipes also provides a template project that can be used to create and compile a Pipes application using the GNU Autotools.
- Pipes requires the user to install the Hadoop native libraries and the Hadoop C++ libraries on the cluster nodes, and to specify the path to the Pipes executable and the Hadoop configuration files when submitting a Pipes job .
- Pipes has some limitations, such as the inability to pass large data records to map/reduce tasks as a contiguous block of bytes, which may require the user to implement custom serialization and deserialization methods.