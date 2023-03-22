 Here are the notes in markdown format on the topic "fair and capacity for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data":

### Hadoop Ecosystem and YARN

- Hadoop ecosystem refers to the collection of open source tools and technologies that are designed to work with the Hadoop framework. The tools work together to solve the complex problem of big data storage and analysis.
- Some of the major components of Hadoop ecosystem are:
    - HDFS - Hadoop Distributed File System - For storing huge data
    - MapReduce - For processing and analyzing the stored data
    - YARN - Yet Another Resource Negotiator - For job scheduling and cluster resource management
    - Hive - For querying and managing large datasets residing in distributed storage
    - Pig - For analyzing large data sets
    - HBase - A scalable and distributed database that supports structured data storage for large tables
    - ZooKeeper - For coordinating distributed applications and maintaining configuration information
    - Oozie - For scheduling Hadoop jobs
- YARN stands for Yet Another Resource Negotiator. It is a cluster management technology for job scheduling and resource allocation.
- Key benefits of YARN:
    - Allows you to use programming models other than MapReduce like graph processing and interactive querying.
    - Supports multi-tenancy i.e. allows multiple applications to share clusters.
    - Scalable and high utilization of cluster resources.
    - Reliable and fault tolerant.
- Main components of YARN:
    - ResourceManager - Manages resources and schedules applications.
    - NodeManager - Manages containers, monitors resource usage and handles resource requests.
    - ApplicationMaster - Negotiates resources from ResourceManager and works with NodeManager(s) to execute and monitor the containers for an application.
- The flow in YARN is: Application submits to ResourceManager -> ApplicationMaster is allocated -> Container is allocated on NodeManagers -> Tasks run in containers -> Monitoring and completion.