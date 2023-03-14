#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a resource management and scheduling layer that lies beneath the MapReduce layer in Hadoop 2  .
- MRv2 separates the resource management and scheduling tasks from the MapReduce programming framework, which allows non-batch applications to run on Hadoop 2  .
- MRv2 also provides high system availability and scalability, as it supports redundant NameNodes and snapshots for disaster recovery  .
- MRv2 is backward compatible with MRv1, which means that the compiled binaries of MRv1 can run on MRv2 without any modification  .
- MRv2 also supports new MapReduce APIs, such as org.apache.hadoop.mapreduce, which offer more flexibility and functionality than the old APIs  .