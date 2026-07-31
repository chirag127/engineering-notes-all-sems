### Hadoop Streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution. It allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer .
- Hadoop streaming works by passing the input data to the mapper as standard input and reading the output data from the mapper as standard output. Similarly, the reducer receives the mapper output as standard input and writes the final output to standard output .
- Hadoop streaming uses the Hadoop jar command with the hadoop-streaming.jar file to specify the mapper and reducer scripts, the input and output directories, and other options .
- Hadoop streaming supports various languages, such as Python, Ruby, Perl, Bash, etc. as long as they can read from standard input and write to standard output .
- Hadoop streaming also supports specifying a Java class as the mapper and/or the reducer, as well as using the built-in identity mapper and reducer .
- Hadoop streaming is a powerful feature that enables users to write their code in any language of their own choice and leverage the scalability and fault-tolerance of Hadoop.