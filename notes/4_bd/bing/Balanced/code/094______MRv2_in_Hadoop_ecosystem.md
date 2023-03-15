#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a component of Hadoop 2 that separates the resource management and scheduling tasks from the data processing layer   .
- MRv2 provides backward compatibility with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries can run without any modification on the new framework .
- MRv2 also supports new APIs such as org.apache.hadoop.mapreduce, which offer more features and flexibility than the old ones .
- MRv2 enables other application engines to utilize YARN and Hadoop, such as Spark, Hive, Pig, and Tez, while also improving the performance of MapReduce   .
- MRv2 uses a Capacity Scheduler that supports multi-tenancy and allows different users and groups to share the cluster resources according to predefined policies .
- MRv2 consists of two main components: the ApplicationMaster and the Container. The ApplicationMaster is responsible for negotiating resources with the ResourceManager and launching and monitoring the Containers. The Container is a unit of execution that runs the Map or Reduce tasks on the NodeManager  .