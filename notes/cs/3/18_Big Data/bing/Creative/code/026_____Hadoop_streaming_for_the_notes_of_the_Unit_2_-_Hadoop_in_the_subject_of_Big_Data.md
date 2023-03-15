### Hadoop Streaming

Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. For example, you can use Python, Ruby, Perl, or any other scripting language to write your MapReduce programs.

Some of the advantages of Hadoop streaming are:

- It enables you to use any programming language that supports standard input and output for data processing.
- It simplifies the development and testing of MapReduce programs, as you do not need to compile or package them.
- It allows you to leverage the existing libraries and tools in your preferred language for data analysis and manipulation.

Some of the disadvantages of Hadoop streaming are:

- It may incur some performance overhead, as the data needs to be serialized and deserialized between the Java framework and the external processes.
- It may not support some advanced features of the MapReduce framework, such as counters, custom partitioners, combiners, etc.
- It may not handle complex data types or binary data very well, as the data needs to be formatted as text.

The basic steps to use Hadoop streaming are:

- Write your mapper and reducer scripts in your chosen language, and make them executable.
- Upload your scripts and input data to HDFS.
- Run the Hadoop streaming command with the appropriate options, such as -input, -output, -mapper, -reducer, etc.
- Check the output and logs of your job in HDFS or the web interface.

The Hadoop streaming command options are listed here: https://hadoop.apache.org/docs/current/hadoop-streaming/HadoopStreaming.html

An example of a Hadoop streaming command is:

```bash
hadoop jar $HADOOP_HOME/hadoop-streaming.jar \
-input myInputDirs \
-output myOutputDir \
-mapper /bin/cat \
-reducer /usr/bin/wc
```

This command runs a MapReduce job that copies the input data as the mapper output, and counts the number of lines, words, and bytes as the reducer output. The mapper and reducer scripts are the standard Unix commands cat and wc, respectively. The input and output directories are specified in HDFS.