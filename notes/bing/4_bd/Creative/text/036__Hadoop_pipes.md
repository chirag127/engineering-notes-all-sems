#### Hadoop pipes

- Hadoop pipes is the name of the C++ interface to Hadoop MapReduce .
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function . JNI is not used.
- Hadoop pipes is a SWIG-compatible C++ API to implement MapReduce applications (non JNI™ based).
- Hadoop pipes can be used to run C++ code within the MapReduce framework in IBM Spectrum Symphony.
- Hadoop pipes requires building the Hadoop version for the target system and compiling the pipes libraries.
- Hadoop pipes operates exclusively on <key, value> pairs, that is, the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job.
- Hadoop pipes may have difficulty in passing large data records to map/reduce tasks as a contiguous block of bytes.