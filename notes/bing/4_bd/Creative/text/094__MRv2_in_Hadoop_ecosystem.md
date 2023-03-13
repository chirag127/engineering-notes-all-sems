#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a new component in Hadoop 2 that separates the resource management and scheduling tasks from the MapReduce layer   .
- YARN allows other application engines to utilize Hadoop and its distributed file system (HDFS), while also improving the performance and scalability of MapReduce   .
- MRv2 is backward compatible with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries can run without any modification on the new framework .
- MRv2 also supports a new set of org.apache.hadoop.mapreduce APIs that offer more flexibility and functionality .
- MRv2 can run on different schedulers, such as the Capacity Scheduler, the Fair Scheduler, and the FIFO Scheduler, which provide different ways of allocating resources and prioritizing jobs  .
- MRv2 enables multi-tenancy support, which means that different users and applications can share the same cluster and data nodes without interfering with each other  .