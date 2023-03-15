#### Hadoop streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution. It allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer.
- Hadoop streaming works by passing the input data to the mapper as standard input and collecting the output from the mapper as standard output. Similarly, the reducer receives the mapper output as standard input and writes the final output to standard output.
- Hadoop streaming supports any language that can read from standard input and write to standard output. For example, you can use Python, Ruby, Perl, Bash, etc. to write your mapper and reducer scripts.
- Hadoop streaming also supports specifying a Java class as the mapper and/or the reducer. This can be useful if you want to use some existing Java code or libraries in your MapReduce job.
- To use Hadoop streaming, you need to specify the following options:

  - `-input`: the input directory or file in HDFS
  - `-output`: the output directory in HDFS
  - `-mapper`: the mapper executable or script
  - `-reducer`: the reducer executable or script
  - `-file`: the local file or directory to be copied to each mapper and reducer node
  - `-inputformat`: the input format class (optional, default is TextInputFormat)
  - `-outputformat`: the output format class (optional, default is TextOutputFormat)
  - `-partitioner`: the partitioner class (optional, default is HashPartitioner)
  - `-numReduceTasks`: the number of reduce tasks (optional, default is 1)

- An example of using Hadoop streaming with Python scripts is:

  ```
  hadoop jar $HADOOP_HOME/hadoop-streaming.jar \
  -input input_dir \
  -output output_dir \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
  ```

- Some advantages of Hadoop streaming are:

  - It is easy to use and flexible. You can write your MapReduce logic in any language you are comfortable with.
  - It can leverage existing code or libraries in different languages. You can reuse your existing code or use third-party libraries without rewriting them in Java.
  - It can handle complex data types and formats. You can use any data format or serialization method as long as your mapper and reducer can parse and process it.

- Some disadvantages of Hadoop streaming are:

  - It may have lower performance than native Java MapReduce. This is because Hadoop streaming adds an extra layer of communication and serialization between the mapper and reducer processes.
  - It may have higher memory and disk usage than native Java MapReduce. This is because Hadoop streaming stores the intermediate data as text files, which may be larger and less compressed than binary files.
  - It may have less error handling and debugging support than native Java MapReduce. This is because Hadoop streaming relies on the mapper and reducer scripts to handle errors and exceptions, which may not be consistent or robust across different languages.