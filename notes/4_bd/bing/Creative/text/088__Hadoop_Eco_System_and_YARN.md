### Hadoop Eco System and YARN

- Hadoop Eco System refers to the various components of the Apache Hadoop software library; it includes open source projects as well as a complete range of complementary tools.
- Some of the most well-known tools of the Hadoop ecosystem include HDFS, Hive, Pig, YARN, MapReduce, Spark, HBase, Oozie, Sqoop, Zookeeper, etc.
- YARN stands for Yet Another Resource Negotiator, but it's commonly referred to by the acronym alone. It is one of the core components in open source Apache Hadoop suitable for resource management .
- YARN enables Hadoop to support different processing types, such as interactive queries, streaming data, real time applications, and machine learning .
- YARN also offers job scheduling and monitors the operations of the applications running in a Hadoop cluster .
- YARN has two main components: Resource Manager and Node Manager.
  - Resource Manager is a single daemon that runs on the master server and allocates the cluster resources. It has a scheduler for scheduling the required jobs and an ApplicationManager for accepting the job submissions and executing the necessary Application Master.
  - Node Manager is a daemon that runs on each data server and manages the containers, which are the units of computation and memory. It also communicates with the Resource Manager and the Application Master.
  - Application Master is a daemon that runs on a data server and manages the life cycle of a single application. It negotiates the resources with the Resource Manager and coordinates the tasks with the Node Manager.
- YARN was introduced as a layer that separates the resource management layer and the processing layer in Hadoop. It was initially named MapReduce 2 since it powered up the MapReduce of Hadoop 1.0 by addressing its downsides and enabling the Hadoop ecosystem to perform well for the modern challenges .
- YARN made Hadoop much more flexible, efficient and scalable. It also reduced the size of the Hadoop cluster and increased the utilization of the resources .