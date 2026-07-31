### Execution Modes of Pig

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It can be executed in three modes:

1. **Local Mode:** In this mode, Pig runs on a single machine without requiring Hadoop or HDFS. It is used for testing and debugging purposes.

2. **MapReduce Mode:** In this mode, Pig runs on a Hadoop cluster and requires HDFS. It is used for processing large datasets.

3. **Tez Mode:** In this mode, Pig runs on a Hadoop cluster using the Tez execution engine. It is used for faster processing of large datasets.

Each mode has its own advantages and can be chosen based on the requirements of the task at hand. It is important to note that the Pig scripts remain the same, regardless of the execution mode chosen.