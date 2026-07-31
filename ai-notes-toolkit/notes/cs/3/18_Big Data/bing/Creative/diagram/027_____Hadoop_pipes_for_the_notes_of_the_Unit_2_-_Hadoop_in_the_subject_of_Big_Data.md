### Hadoop Pipes

- Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce .
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function .
- Hadoop Pipes requires the following components:
  - A C++ program that implements the map and reduce functions using the Hadoop Pipes API.
  - A Java program that acts as a driver for the C++ program and sets up the job configuration.
  - A binary executable file that is compiled from the C++ program and is distributed to the cluster nodes.
- Hadoop Pipes provides the following benefits:
  - It allows users to write map and reduce functions in C++, which may be faster than Java or other languages.
  - It avoids the overhead of launching external processes and parsing text data as in Streaming.
  - It supports combiners and partitioners in C++.
- Hadoop Pipes also has some limitations :
  - It requires users to compile the C++ program for each platform and distribute the binary file to the cluster nodes.
  - It does not support counters, side data distribution, or custom input and output formats in C++.
  - It may have difficulty in passing large data records to the map and reduce tasks.