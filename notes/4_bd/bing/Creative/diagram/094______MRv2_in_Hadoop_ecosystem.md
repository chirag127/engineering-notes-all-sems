#### MRv2 in Hadoop ecosystem

- MRv2 stands for **MapReduce version 2**, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a new component in Hadoop 2 that separates the resource management and scheduling tasks from the MapReduce layer   .
- YARN allows multiple applications to run on the same Hadoop cluster, not just MapReduce, and enables better utilization of cluster resources   .
- MRv2 is backward compatible with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries can run without any modification on the new framework .
- MRv2 also supports the org.apache.hadoop.mapreduce APIs, which are more flexible and efficient than the old APIs .
- MRv2 improves the performance of MapReduce by allowing more parallelism, dynamic allocation of resources, and fault tolerance  .