#### MRv2 in Hadoop ecosystem

- MRv2 stands for **MapReduce version 2**, which is an application framework that runs within YARN (Yet Another Resource Negotiator) on Hadoop 2 .
- YARN is a **cluster resource management** layer that separates the resource allocation and scheduling tasks from the data processing logic of MapReduce .
- MRv2 provides **backward compatibility** with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries of MapReduce applications can run on MRv2 without any modification.
- MRv2 also provides **improved performance** and **scalability** of MapReduce applications, as well as **fault tolerance** and **security** features.
- MRv2 enables **multi-tenancy** support and **diverse workloads** on Hadoop 2, as YARN can allocate resources to other application engines besides MapReduce, such as Spark, Storm, Tez, etc. .