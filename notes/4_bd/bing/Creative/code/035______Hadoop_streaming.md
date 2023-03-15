Hadoop streaming is a utility that allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. You can use any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc. Hadoop streaming works by passing the input data to the mapper script as lines of text, and collecting the output data from the reducer script as lines of text. The mapper and reducer scripts communicate with the Hadoop framework through the standard input and output streams.

To use Hadoop streaming, you need to specify the following options:

- `-input`: the input directory or file in HDFS
- `-output`: the output directory in HDFS
- `-mapper`: the mapper executable or script
- `-reducer`: the reducer executable or script

Optionally, you can also specify other options, such as:

- `-file`: the local file to be copied to the Hadoop cluster
- `-combiner`: the combiner executable or script
- `-partitioner`: the partitioner class name
- `-numReduceTasks`: the number of reduce tasks

For example, to run a word count job using Python scripts as the mapper and reducer, you can use the following command:

```bash
hadoop jar $HADOOP_HOME/hadoop-streaming.jar \
-input /user/input \
-output /user/output \
-mapper mapper.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py
```

This command will copy the `mapper.py` and `reducer.py` files from the local file system to the Hadoop cluster, and run them as the mapper and reducer for the input and output directories in HDFS. The mapper script will read the input lines from standard input, split them into words, and emit each word with a count of 1 as the key-value pair. The reducer script will read the key-value pairs from standard input, sum the counts for each word, and emit the word and the total count as the output. The output will be stored in the `/user/output` directory in HDFS.

#### Hadoop streaming