Hadoop streaming is a utility that allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. It is useful for writing MapReduce programs in languages other than Java, such as Python, Ruby, Perl, etc. Hadoop streaming works by passing the input data to the mapper script as standard input, and reading the output data from the standard output. Similarly, the reducer script receives the intermediate key-value pairs as standard input, and writes the final output to the standard output. Hadoop streaming handles the communication between the nodes and the partitioning of the data.

To use Hadoop streaming, you need to specify the following options:

- `-input`: the input directory or file in HDFS
- `-output`: the output directory in HDFS
- `-mapper`: the mapper executable or script
- `-reducer`: the reducer executable or script
- `-file`: the local file or directory to be copied to each mapper and reducer node

For example, to run a word count program using Python scripts as the mapper and reducer, you can use the following command:

```bash
hadoop jar $HADOOP_HOME/hadoop-streaming.jar \
-input /user/input \
-output /user/output \
-mapper mapper.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py
```

Where `mapper.py` and `reducer.py` are the Python scripts that implement the word count logic. You can also use other options to customize the Hadoop streaming job, such as `-combiner`, `-partitioner`, `-numReduceTasks`, etc. For more details, you can refer to the Hadoop streaming documentation .