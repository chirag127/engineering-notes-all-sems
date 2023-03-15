#### Hadoop pipes

- Hadoop pipes is the name of the C++ interface to Hadoop MapReduce .
- Hadoop pipes allows users to write map and reduce functions in C++ and run them on a Hadoop cluster.
- Hadoop pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function . JNI is not used.
- Hadoop pipes requires users to compile the C++ code and link it with the pipes library, which provides the implementation of the Hadoop API in C++.
- Hadoop pipes also requires users to implement a factory class that creates map and reduce objects on demand.
- Hadoop pipes can be run on any platform that supports sockets and C++, such as Linux, Windows, or IBM PowerLinux.
- Hadoop pipes can handle large data records by using the RecordReader and RecordWriter interfaces, which allow users to define how to split and serialize the data.