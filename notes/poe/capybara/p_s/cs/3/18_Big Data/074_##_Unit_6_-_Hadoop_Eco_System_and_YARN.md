## Unit 6 - Hadoop Eco System and YARN

Apache Hadoop is an open-source software framework that is used to store and process large data sets in a distributed computing environment. Hadoop is designed to be scalable and fault-tolerant, and it has become one of the most popular big data processing tools in the world. One of the key components of Hadoop is the YARN (Yet Another Resource Negotiator) framework, which is used to manage the resources of a Hadoop cluster. The following are some of the topics that are covered in this unit:

### Hadoop Eco System

The Hadoop Eco System is a collection of open-source software projects that are used to extend the functionality of Hadoop. The following are some of the most important components of the Hadoop Eco System:

1. HDFS (Hadoop Distributed File System): This is the primary storage system for Hadoop. HDFS is designed to store large data sets across multiple machines in a cluster.

2. MapReduce: This is a programming model that is used to process large data sets in parallel across a Hadoop cluster. MapReduce divides the data into smaller chunks and distributes them across the cluster for processing.

3. Pig: This is a high-level platform for creating MapReduce programs. Pig provides a simple scripting language that can be used to write MapReduce programs without having to write Java code.

4. Hive: This is a data warehousing tool that allows users to query large data sets using SQL-like syntax. Hive is built on top of Hadoop and provides a familiar interface for users who are familiar with SQL.

5. HBase: This is a distributed and scalable NoSQL database that is built on top of Hadoop. HBase is designed to store large data sets in a distributed environment and provides fast access to data.

6. ZooKeeper: This is a distributed coordination service that is used to manage the configuration of Hadoop clusters. ZooKeeper provides a simple and reliable way to manage the configuration of a Hadoop cluster.

### YARN

YARN (Yet Another Resource Negotiator) is a framework that is used to manage the resources of a Hadoop cluster. YARN allows multiple applications to share the resources of a cluster and provides a way to manage the allocation of resources to different applications. The following are some of the key features of YARN:

1. Resource Manager: This is the central component of YARN. The Resource Manager is responsible for managing the resources of a Hadoop cluster and allocating resources to different applications.

2. Node Manager: This is a daemon that runs on each node in the cluster. The Node Manager is responsible for managing the resources of the node and reporting the available resources to the Resource Manager.

3. Application Master: This is a component that runs inside each application. The Application Master is responsible for managing the resources that are allocated to the application by the Resource Manager.

4. Containers: Containers are units of resource allocation in YARN. Each application is allocated one or more containers, and the application runs inside the container.

5. Fair Scheduler: This is a scheduler that is used to allocate resources to different applications in a fair and equitable manner. The Fair Scheduler ensures that each application gets a fair share of the available resources.

In conclusion, Hadoop Eco System and YARN are important components of the Hadoop framework. Understanding these components is essential for anyone who wants to work with big data and build scalable and fault-tolerant applications.