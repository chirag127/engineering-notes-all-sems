#### Hadoop streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution.
- The utility allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer.
- The mapper and reducer scripts can be written in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc.
- Hadoop streaming works by passing the input data to the mapper script as lines of text via standard input, and collecting the output data from the mapper script as lines of text via standard output.
- The output data from the mapper script is then shuffled and sorted by Hadoop, and passed to the reducer script as lines of text via standard input, grouped by key.
- The output data from the reducer script is then collected by Hadoop as the final output of the MapReduce job.
- Hadoop streaming can be invoked by using the `hadoop jar` command with the `hadoop-streaming.jar` file as the argument, followed by various options to specify the input, output, mapper, reducer, and other parameters of the job.
- For example, the following command runs a MapReduce job with a Python script as the mapper and a shell command as the reducer:

```
hadoop jar hadoop-streaming.jar \
-input myInputDirs \
-output myOutputDir \
-mapper mapper.py \
-reducer /bin/wc
```

- Hadoop streaming is a powerful feature that enables users to leverage the scalability and fault-tolerance of Hadoop with any programming language of their choice.