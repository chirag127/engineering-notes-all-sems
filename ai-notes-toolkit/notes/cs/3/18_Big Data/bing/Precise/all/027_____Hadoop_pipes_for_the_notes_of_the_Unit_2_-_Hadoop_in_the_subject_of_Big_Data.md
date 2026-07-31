### Hadoop Pipes

- Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce.
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function.
- JNI is not used.
- Hadoop Pipes uses sockets to enable tasktrackers to communicate processes running the C++ map or reduce functions.