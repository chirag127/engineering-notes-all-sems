#### Execution Modes of Pig

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It has two execution modes:

1. **Local Mode:** In this mode, Pig runs on a single machine without requiring Hadoop or HDFS. It is used for development and testing of Pig scripts.

2. **MapReduce Mode:** In this mode, Pig runs on a Hadoop cluster and requires HDFS. It is used for processing large data sets in a distributed environment.

Both modes can be invoked by specifying the appropriate command line option when running Pig. For example, to run Pig in local mode, the command would be `pig -x local`. To run Pig in MapReduce mode, the command would be `pig` or `pig -x mapreduce`.