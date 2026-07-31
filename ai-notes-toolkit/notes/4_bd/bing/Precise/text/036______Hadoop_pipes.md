#### Hadoop Pipes
- Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce.
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function.
- JNI is not used.
- Hadoop Pipes uses sockets to enable tasktrackers to communicate processes running the C++ map or reduce functions.
- To run Hadoop pipes on IBM PowerLinux systems, build your Hadoop version for PowerLinux and compile the pipes libraries as described in step 1.
- Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner.
- If it weren't for the size of the records, the Hadoop Pipes API would be fine: but this seems to be based around passing the input to map/reduce tasks as a contiguous block of bytes, which is impractical in this case.