### Execution Modes of Pig

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It has two execution modes:

1. **Local Mode**: In this mode, Pig runs on a single machine without requiring Hadoop or HDFS. It is used for processing small datasets and for testing and debugging purposes.

2. **MapReduce Mode**: In this mode, Pig runs on a Hadoop cluster and processes data stored in HDFS. It is used for processing large datasets and for production purposes.

In both modes, Pig scripts are translated into a series of MapReduce jobs that are executed on the Hadoop cluster. The choice of execution mode depends on the size of the dataset and the resources available for processing.