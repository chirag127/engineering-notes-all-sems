#### Execution Modes of Pig

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It has two execution modes:

1. **Local Mode**: In this mode, Pig runs on a single machine without requiring Hadoop or HDFS. It is used for development and testing of Pig scripts.

2. **MapReduce Mode**: In this mode, Pig runs on a Hadoop cluster and requires Hadoop and HDFS. It is used for processing large data sets.

In both modes, Pig scripts are translated into a series of MapReduce jobs that are run on the Hadoop cluster. The choice of execution mode depends on the size of the data set and the resources available for processing. For small data sets, local mode is sufficient, while for large data sets, MapReduce mode is more appropriate.