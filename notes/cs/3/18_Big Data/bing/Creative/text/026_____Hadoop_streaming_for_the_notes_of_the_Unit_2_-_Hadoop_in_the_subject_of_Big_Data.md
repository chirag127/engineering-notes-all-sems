### Hadoop Streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution. It allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer .
- Hadoop streaming works by passing the input data to the mapper script as standard input, and reading the output data from the standard output. Similarly, the reducer script receives the intermediate data from the standard input, and writes the final output to the standard output .
- Hadoop streaming can be used to write MapReduce programs in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc .
- Hadoop streaming can be invoked by using the `hadoop jar` command with the `hadoop-streaming.jar` file as the argument. The command also requires specifying the input and output directories, and the mapper and reducer scripts or executables .
- Hadoop streaming supports various command options, such as specifying the number of reducers, the input and output formats, the partitioner class, the combiner class, the compression codec, the environment variables, etc .
- Hadoop streaming can also use Java classes as the mapper and/or the reducer, by specifying the fully qualified class name instead of the script or executable .
- Hadoop streaming is a powerful feature that enables writing MapReduce programs in any language of choice, without having to implement the Hadoop API.