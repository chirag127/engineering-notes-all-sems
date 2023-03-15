### Hadoop Streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution .
- The utility allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer   .
- For example, you can use Python, Perl, Ruby, Bash, or any other language that can read from standard input and write to standard output to write your mapper and reducer scripts  .
- Hadoop streaming works by passing the input data to the mapper script as lines of text via standard input, and collecting the output data from the mapper script as lines of text via standard output  .
- The output data of the mapper script is then shuffled and sorted by Hadoop, and passed to the reducer script as lines of text via standard input, grouped by key  .
- The output data of the reducer script is then collected by Hadoop as lines of text via standard output, and written to the output directory in HDFS  .
- To run a Hadoop streaming job, you need to use the `hadoop jar` command with the `hadoop-streaming.jar` file as the argument, and specify the input and output directories, the mapper and reducer scripts, and any other options you need  .
- For example, the following command runs a Hadoop streaming job that uses the `/bin/cat` command as the mapper and the `/usr/bin/wc` command as the reducer:

```
hadoop jar hadoop-streaming.jar \
-input myInputDirs \
-output myOutputDir \
-mapper /bin/cat \
-reducer /usr/bin/wc
```

- Hadoop streaming supports various command options, such as specifying a Java class as the mapper or reducer, specifying the number of map or reduce tasks, specifying the input and output formats, specifying the partitioner class, specifying the combiner class, specifying the compression codec, and so on .
- You can find the full list of Hadoop streaming command options in the official documentation .
- Hadoop streaming is a powerful feature that enables you to use any language of your choice to write MapReduce scripts, as long as the language can handle text input and output .
- However, Hadoop streaming also has some limitations, such as the overhead of launching external processes, the lack of type safety and error checking, the dependence on the text format, and the difficulty of debugging .
- Therefore, you should use Hadoop streaming only when you have a specific reason to use a non-Java language, or when you want to quickly prototype or test your MapReduce logic .