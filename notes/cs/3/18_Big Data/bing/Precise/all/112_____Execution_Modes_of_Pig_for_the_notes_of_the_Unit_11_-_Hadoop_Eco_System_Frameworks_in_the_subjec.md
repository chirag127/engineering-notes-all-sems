### Execution Modes of Pig

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It can be executed in three modes:

1. **Local Mode:** In local mode, Pig runs on a single machine without requiring Hadoop or HDFS. It is used for processing small datasets and for testing and debugging purposes.

2. **MapReduce Mode:** In MapReduce mode, Pig runs on a Hadoop cluster and processes data stored in HDFS. It is used for processing large datasets.

3. **Tez Mode:** In Tez mode, Pig runs on a Hadoop cluster and processes data stored in HDFS using the Tez execution engine. It is used for processing large datasets and provides faster execution time compared to MapReduce mode.

These are the three execution modes of Pig that can be used for processing data in different scenarios. It is important to choose the appropriate mode based on the size of the dataset and the processing requirements.