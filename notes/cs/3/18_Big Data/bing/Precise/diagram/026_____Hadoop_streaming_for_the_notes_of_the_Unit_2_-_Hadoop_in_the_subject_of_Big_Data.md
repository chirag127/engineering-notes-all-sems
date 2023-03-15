### Hadoop Streaming

Hadoop Streaming is a utility that comes with the Hadoop distribution. This utility allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer.

Here are some key points to remember about Hadoop Streaming:

1. Hadoop Streaming allows you to use languages other than Java for writing MapReduce jobs.
2. The input to the mapper and the output from the reducer must be in text format.
3. The mapper and the reducer communicate with Hadoop via the standard input and output streams.
4. Hadoop Streaming provides a number of command line options to configure the job.
5. The utility can be used to run MapReduce jobs on data stored in HDFS or on data stored in other file systems supported by Hadoop.

Hadoop Streaming is a powerful tool for writing MapReduce jobs in languages other than Java. It provides a flexible and easy-to-use interface for working with data stored in Hadoop. However, it is important to note that the performance of jobs written using Hadoop Streaming may not be as good as jobs written in Java, due to the overhead of data serialization and deserialization.