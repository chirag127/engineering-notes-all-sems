#### Hadoop pipes

- Hadoop pipes is the name of the C++ interface to Hadoop MapReduce .
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function .
- Pipes does not use JNI (Java Native Interface), which means that the C++ code does not need to be compiled for each platform.
- To use Pipes, the C++ code must implement the HadoopPipes::Mapper and HadoopPipes::Reducer classes, which have similar methods to the Java Mapper and Reducer interfaces.
- The C++ code must also link to the libhadooppipes.a and libhadooputils.a libraries, which are provided by Hadoop.
- To run a Pipes job, the hadoop pipes command is used, which takes similar options to the hadoop jar command for Java MapReduce jobs.
- The hadoop pipes command requires the following options:
  - -input: the input directory or file
  - -output: the output directory
  - -program: the executable file containing the C++ code
  - -mapper: the name of the mapper class
  - -reducer: the name of the reducer class
- Optionally, the hadoop pipes command can also take the following options:
  - -combiner: the name of the combiner class
  - -inputformat: the name of the input format class
  - -outputformat: the name of the output format class
  - -partitioner: the name of the partitioner class
  - -jobconf: a key-value pair to set a configuration property
- An example of a hadoop pipes command is:

```bash
hadoop pipes \
-input /user/input \
-output /user/output \
-program /user/wordcount \
-mapper WordCountMapper \
-reducer WordCountReducer
```

- Advantages of Pipes:
  - It allows writing MapReduce programs in C++, which may be faster or more convenient than Java for some applications.
  - It does not incur the overhead of JNI, which may improve the performance and portability of the C++ code.
- Disadvantages of Pipes:
  - It requires the C++ code to be compiled and distributed to the cluster nodes, which may be more complex than using Java or scripting languages.
  - It does not support the full functionality of the Java MapReduce API, such as counters, distributed cache, or custom writable types.
  - It may be less stable or reliable than the Java MapReduce API, as it is less widely used and tested.
- A possible mnemonic to remember the difference between Streaming and Pipes is:

Streaming: Standard input/output, Scripting languages, Slow, Simple, Stable

Pipes: Sockets, C++, Fast, Complex, Experimental