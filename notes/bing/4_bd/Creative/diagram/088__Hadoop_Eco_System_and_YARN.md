Hadoop Eco System and YARN
---
Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers. Hadoop consists of several components, such as Hadoop Distributed File System (HDFS), MapReduce, Hive, Pig, HBase, Oozie, Sqoop, Zookeeper, etc. These components work together to provide various functionalities, such as data storage, data processing, data analysis, data ingestion, data management, etc. The Hadoop ecosystem is the collection of all these components and the tools that interact with them.

YARN stands for Yet Another Resource Negotiator. It is a sub-project of Hadoop that provides a platform for managing and scheduling resources in a Hadoop cluster. YARN was introduced in Hadoop 2.0 to overcome the limitations of MapReduce, such as scalability, resource utilization, and application diversity. YARN separates the resource management and job scheduling functions from the data processing logic, allowing multiple types of applications to run on the same Hadoop cluster.

The following diagram illustrates the basic architecture of YARN:

```
+-----------------+        +-----------------+
|                 |        |                 |
|   Client Node   |        |   Master Node   |
|                 |        |                 |
+-----------------+        +-----------------+
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    |
      |    |                    |    +-----------------+
      |    |                    |    |                 |
      |    |                    +---->  Resource       |
      |    |                         |  Manager (RM)    |
      |    |                         |                 |
      |    |                         +-----------------+
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    |
      |    |                              |    +-----------------+
      |    |                              |    |                 |
      |    |                              +---->  Node Manager   |
      |    |                                   |  (NM)           |
      |    |                                   |                 |
      |    |                                   +-----------------+
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    |
      |    |                                        |    +-----------------+
      |    |                                        |    |                 |
      |    |                                        +---->  Application    |
      |    |                                             |  Master (AM)    |
      |    |                                             |                 |
      |    |                                             +-----------------+
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    |
      |    |                                                  |    +-----------------+
      |    |                                                  |    |                 |
      |    |                                                  +---->  Container      |
      |    |                                                       |                 |
      |    |                                                       +-----------------+
      |    |
      |    +-----------------+
      |    |                 |
      +---->  Application    |
           |  Master (AM)    |
           |                 |
           +-----------------+
                |    |
                |    |
                |    |
                |    |
                |    |
                |    |
                |    |
                |    |
                |    |
                |    |
                |    |
                |    +