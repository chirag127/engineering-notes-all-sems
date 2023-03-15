# Hadoop Streaming

Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. For example, you can use Python, Perl, Ruby, or Bash scripts as the mapper and/or the reducer.

Some of the advantages of Hadoop streaming are:

- It enables you to use any programming language that can read from standard input and write to standard output for MapReduce tasks.
- It simplifies the development and testing of MapReduce applications, as you do not need to compile or package your code into Java classes or JAR files.
- It allows you to leverage existing libraries and tools that are written in other languages for data processing and analysis.

Some of the disadvantages of Hadoop streaming are:

- It may incur some performance overhead, as the data needs to be serialized and deserialized between the Java framework and the external processes.
- It may not support some advanced features of the MapReduce framework, such as counters, custom partitioners, combiners, or distributed cache.

To use Hadoop streaming, you need to specify the following options:

- `-input`: The input directory or file in HDFS that contains the data for the MapReduce job.
- `-output`: The output directory in HDFS that will store the results of the MapReduce job.
- `-mapper`: The executable or script that will act as the mapper. It can be a local file or a file in HDFS. It must be executable and have the correct permissions.
- `-reducer`: The executable or script that will act as the reducer. It can be a local file or a file in HDFS. It must be executable and have the correct permissions.

You can also specify other optional options, such as:

- `-file`: A file that will be copied to the working directory of each mapper and reducer task. This can be used to provide additional resources or dependencies for your executable or script.
- `-combiner`: A executable or script that will act as the combiner. It can be a local file or a file in HDFS. It must be executable and have the correct permissions.
- `-partitioner`: A Java class that will act as the partitioner. It must implement the org.apache.hadoop.mapred.Partitioner interface.
- `-numReduceTasks`: The number of reduce tasks for the job.

An example of a Hadoop streaming command is:

```bash
hadoop jar $HADOOP_HOME/hadoop-streaming.jar \
-input /user/input \
-output /user/output \
-mapper /home/user/mapper.py \
-reducer /home/user/reducer.py \
-file /home/user/mapper.py \
-file /home/user/reducer.py
```

This command will run a MapReduce job with the mapper.py and reducer.py scripts as the mapper and reducer, respectively. The scripts will be copied to the working directory of each task. The input and output directories are specified in HDFS. The default number of reduce tasks is 1.