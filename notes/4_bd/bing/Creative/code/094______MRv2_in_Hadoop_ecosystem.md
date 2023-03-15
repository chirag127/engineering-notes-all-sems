#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a component of Hadoop 2 that separates the resource management and scheduling tasks from the data processing layer   .
- YARN allows multiple applications to run on the same Hadoop cluster, such as MapReduce, Spark, Hive, etc.   .
- MRv2 is backward compatible with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries can run without any modification on the new framework .
- MRv2 also supports new APIs such as org.apache.hadoop.mapreduce, which offer more flexibility and functionality .
- MRv2 improves the performance of MapReduce by allowing dynamic allocation of resources, speculative execution, and high availability  .
- MRv2 also supports security features such as Kerberos authentication, encryption, and authorization .