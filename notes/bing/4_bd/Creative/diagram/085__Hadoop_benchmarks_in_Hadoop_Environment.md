Hadoop benchmarks are tests that measure the performance of a Hadoop cluster in various aspects, such as HDFS read and write, MapReduce sorting, and data generation. Hadoop provides some built-in benchmark applications that can be run on a Hadoop cluster using the command-line interface. Some of the common Hadoop benchmarks are:

- TestDFSIO: This benchmark tests the read and write performance of HDFS by using one map task per file. It can be run with the following commands:

`hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-*-tests.jar TestDFSIO -write -nrFiles <number of files> -fileSize <size of each file>`

`hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-*-tests.jar TestDFSIO -read -nrFiles <number of files> -fileSize <size of each file>`

- TeraSort: This benchmark tests the sorting performance of MapReduce by using a custom partitioner and a custom output format. It consists of three components: TeraGen, TeraSort, and TeraValidate. TeraGen generates random data, TeraSort sorts the data using MapReduce, and TeraValidate validates the output. They can be run with the following commands:

`hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar teragen <number of 100-byte rows> <output directory>`

`hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar terasort <input directory> <output directory>`

`hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar teravalidate <output directory> <report directory>`

- Pi: This benchmark estimates the value of pi by using a Monte Carlo method. It can be run with the following command:

`hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi <number of maps> <number of samples per map>`

The following diagram illustrates the basic architecture of a Hadoop cluster and how the benchmark applications interact with it:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    NameNode     |       |    DataNode     |       |    DataNode     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    JobTracker   |       |    TaskTracker  |       |    TaskTracker  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Client       |       |    Map Task     |       |    Map Task     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Benchmark    |       |    Reduce Task  |       |    Reduce Task  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+

```

The client node runs the benchmark application, which submits a job to the JobTracker on the NameNode. The JobTracker assigns map and reduce tasks to the TaskTrackers on the DataNodes, which execute them in parallel. The map tasks read data from HDFS and process it, while the reduce tasks aggregate the results and write them back to HDFS. The benchmark application collects the output and reports the performance metrics.