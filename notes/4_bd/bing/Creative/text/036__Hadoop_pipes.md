#### Hadoop pipes

- Hadoop pipes is a utility that allows you to create and run MapReduce jobs with C++ code as the mapper and/or the reducer  .
- Hadoop pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function, unlike Hadoop streaming which uses standard input and output .
- Hadoop pipes can improve the performance of applications that require high numerical computation by using C++ code.
- To use Hadoop pipes, you need to compile the C++ libraries and the sample programs using Apache Ant or Maven .
- You also need to specify the Hadoop pipes executable and the C++ mapper and reducer classes as arguments to the Hadoop jar command .
- For example, to run the wordcount example using Hadoop pipes, you can use the following command:

```bash
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming.jar \
 -D hadoop.pipes.java.recordreader=true \
 -D hadoop.pipes.java.recordwriter=true \
 -input myInputDirs \
 -output myOutputDir \
 -program /bin/wordcount \
 -reduces 10
```