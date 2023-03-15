#### Hadoop streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution. It allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer .
- Hadoop streaming works by passing the input data to the mapper as the standard input and collecting the output data from the standard output. Similarly, the reducer receives the intermediate data from the standard input and writes the final output to the standard output .
- Hadoop streaming uses the Hadoop jar command to launch the streaming jobs. The command takes various options to specify the input and output directories, the mapper and reducer scripts, the input and output formats, the partitioner, the combiner, and other parameters .
- Hadoop streaming supports various languages such as Python, Ruby, Perl, Bash, and R for writing the mapper and reducer scripts. The scripts should follow the Hadoop streaming protocol, which is based on the key-value pairs separated by tabs .
- Hadoop streaming is a powerful feature that enables users to leverage the scalability and reliability of Hadoop for processing large-scale data with any programming language of their choice.