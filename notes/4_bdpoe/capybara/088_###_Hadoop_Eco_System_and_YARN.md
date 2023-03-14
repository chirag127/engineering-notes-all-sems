### Hadoop Eco System and YARN

Hadoop is an open-source framework that facilitates the storage and processing of large data sets in a distributed computing environment. It is a part of the Apache Software Foundation and was initially developed by Doug Cutting and Mike Cafarella in 2005. Hadoop Eco System is a set of various tools and technologies that are used to process and analyze large amounts of data stored in Hadoop Distributed File System (HDFS). Yet Another Resource Negotiator (YARN) is one of the most important components of the Hadoop Eco System that manages resources and schedules tasks in a Hadoop cluster.

#### Hadoop Eco System Components

1. Hadoop Distributed File System (HDFS) - It is a distributed file system that provides high throughput access to application data.

2. MapReduce - It is a programming model used to process large amounts of data in parallel across a Hadoop cluster.

3. YARN - It is a resource management system that allocates resources to applications and schedules tasks across a Hadoop cluster.

4. Hive - It is a data warehousing tool that provides a SQL-like interface to query large-scale data stored in Hadoop.

5. Pig - It is a high-level scripting language used to analyze large datasets in Hadoop.

6. HBase - It is a distributed database that supports structured data storage for large tables.

7. Sqoop - It is a tool used to transfer data between Hadoop and relational databases.

8. Flume - It is a tool used to collect, aggregate, and move large amounts of data from various sources to Hadoop.

9. Oozie - It is a workflow scheduler used to manage Hadoop jobs.

#### YARN

YARN is a resource management system that separates the processing and resource management functions of Hadoop into different daemons. It enables multiple applications to share a Hadoop cluster by providing a central platform to manage cluster resources. YARN has two main components:

1. Resource Manager - It manages resources and schedules tasks across the cluster.

2. Node Manager - It runs on each node of the cluster and manages resources such as CPU, memory, and disk.

#### Advantages of YARN

1. YARN is a flexible and scalable resource management system that can manage various types of workloads.

2. It allows multiple applications to run on the same cluster, which improves resource utilization and reduces costs.

3. YARN provides a centralized platform to manage cluster resources, which simplifies cluster management and reduces administrative overhead.

#### Mnemonics and Learning Tricks

There are no easy mnemonics or learning tricks available for the Hadoop Eco System and YARN. However, it is important to understand the role and function of each component to effectively use them for processing and analyzing large amounts of data. A good way to remember the components is to relate them to their function and use cases. For example, HDFS is used for storing large amounts of data, MapReduce is used for processing data in parallel, and YARN is used for managing resources and scheduling tasks across a cluster.