

#### Execution Modes of Pig

1. Local Mode: Pig scripts are executed on the local system. This mode is suitable for debugging and testing purposes.
2. MapReduce Mode: This mode is used to execute Pig scripts on a Hadoop cluster. In this mode, the Pig script is translated into MapReduce jobs and submitted to the cluster.
3. Tez Mode: This mode is used to execute Pig jobs using Apache Tez, which is a distributed execution engine. This mode is more efficient than MapReduce mode, as it reduces the number of MapReduce jobs.
4. Spark Mode: This mode is used to execute Pig jobs using Apache Spark, which is a fast and general-purpose distributed data processing engine. This mode is more efficient than MapReduce and Tez modes.