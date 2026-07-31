#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a component of Hadoop 2 that separates the resource management and scheduling tasks from the data processing layer   .
- YARN allows multiple applications to run on the same Hadoop cluster, such as MapReduce, Spark, Hive, etc.   .
- MRv2 is backward compatible with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries can run without any modification on the new framework .
- MRv2 also supports the org.apache.hadoop.mapreduce APIs, which are more flexible and efficient than the old APIs .
- MRv2 improves the performance of MapReduce by allowing dynamic allocation of resources, speculative execution, and high availability  .
- MRv2 consists of two components: the MapReduce Application Master (MRAppMaster) and the MapReduce Container (MRContainer) .
- The MRAppMaster is responsible for negotiating resources with the YARN ResourceManager, launching and monitoring the MRContainers, and coordinating the data flow between the MRContainers .
- The MRContainer is responsible for executing the map or reduce tasks assigned by the MRAppMaster, and reporting the progress and status to the MRAppMaster .
- The MRAppMaster and the MRContainers communicate with each other through the YARN NodeManager, which is a daemon that runs on each node of the cluster and manages the containers .