#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a component of Hadoop 2 that separates the resource management and scheduling tasks from the data processing layer   .
- MRv2 provides backward compatibility with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries can run without any modification on the new framework .
- MRv2 also supports new APIs such as org.apache.hadoop.mapreduce, which offer more features and flexibility than the old ones .
- MRv2 enables Hadoop to support other application engines besides MapReduce, such as Spark, Storm, and Tez, which can utilize YARN for cluster resource management   .
- MRv2 improves the performance of MapReduce by allowing dynamic allocation of resources, fine-grained control over tasks, and better fault tolerance  .