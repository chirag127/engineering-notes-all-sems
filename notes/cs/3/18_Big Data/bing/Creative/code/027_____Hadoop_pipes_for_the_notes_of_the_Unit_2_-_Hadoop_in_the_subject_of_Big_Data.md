### Hadoop pipes

- Hadoop pipes is the name of the C++ interface to Hadoop MapReduce .
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function .
- Pipes does not use JNI (Java Native Interface), which means that the C++ code does not need to be compiled for a specific platform.
- Pipes provides a set of C++ classes and methods that wrap the Java MapReduce API and allow the user to implement the map and reduce functions in C++ .
- Pipes also provides a template library called Hadoop Template Library (HTL) that simplifies the development of C++ map and reduce functions.
- To use Pipes, the user needs to compile the C++ code using the Hadoop pipes library and run it using the hadoop pipes command .
- The hadoop pipes command has several options to specify the input, output, mapper, reducer, combiner, partitioner, and other parameters .
- Pipes can be used to run C++ code on Hadoop clusters without modifying the existing Java framework .
- Pipes can also be used to run other languages that can interact with C++, such as Python, Ruby, or Perl.
- Pipes can offer better performance and efficiency than Streaming for some applications that require intensive computation or complex data structures .