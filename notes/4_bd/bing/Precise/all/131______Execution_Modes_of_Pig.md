#### Execution Modes of Pig

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It has two execution modes:

1. **Local Mode:** In this mode, Pig runs on a single machine. It does not require Hadoop or HDFS. All files are installed and run using the local host and file system. This mode is suitable for processing small data sets.

2. **MapReduce Mode:** In this mode, Pig runs on a Hadoop cluster. It requires Hadoop and HDFS. Pig translates the scripts into MapReduce jobs and runs them on the Hadoop cluster. This mode is suitable for processing large data sets.
