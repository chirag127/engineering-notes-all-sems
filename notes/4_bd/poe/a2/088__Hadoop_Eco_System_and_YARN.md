 Here is the content in formal tone without any emojis or external links in markdown format:

### Hadoop Eco System and YARN

1. Hadoop Eco System refers to the collection of open source tools developed by Apache Software Foundation for distributed storage and processing of very large data sets. The core components of Hadoop Eco System are:

- Hadoop Common: Provides libraries and utilities used by other Hadoop modules
- Hadoop Distributed File System (HDFS): A distributed file system that stores data on commodity machines, providing very high aggregate bandwidth across the cluster
- MapReduce: A programming model for large scale data processing
- YARN: A framework for job scheduling and cluster resource management

2. YARN stands for Yet Another Resource Negotiator. It is a cluster management technology for Hadoop. The key features of YARN are:

- It separates the resource management and job scheduling/monitoring functions
- It consists of a global ResourceManager and per-application ApplicationMaster
- The ResourceManager arbitrates resources among competing applications and performs admission control and scheduling of applications
- The ApplicationMaster is responsible for negotiating resources from the ResourceManager and working with the NodeManager(s) to execute and monitor the containers and their resource utilization
- YARN enables running multiple data processing engines on top of HDFS besides MapReduce like Spark, Tez, Flink, etc. allowing Hadoop to be more flexible and efficient in modern data processing requirements.

The content summarizes the key points about Hadoop Eco System and YARN. Please let me know if you would like me to elaborate on any of the points or add more details.