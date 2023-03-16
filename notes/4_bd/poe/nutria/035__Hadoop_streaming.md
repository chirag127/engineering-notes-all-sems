
#### Hadoop Streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution and allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer.
- It is used to process large amounts of data in parallel across a Hadoop cluster.
- The data is typically stored in HDFS and processed by MapReduce jobs.
- The mapper and reducer can be written in any language as long as it can read from standard input and write to standard output.
- The utility takes care of splitting the input data into chunks, scheduling the job across the cluster, and managing inter-process communication.
- It also provides an API for writing custom MapReduce jobs in Java.
- Hadoop streaming is a powerful tool for processing large datasets in a distributed environment and is widely used in many organizations.