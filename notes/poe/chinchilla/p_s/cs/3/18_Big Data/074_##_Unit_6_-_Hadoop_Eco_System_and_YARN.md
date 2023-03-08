## Unit 6 - Hadoop Eco System and YARN

Hadoop is a distributed computing framework that enables the processing of large data sets across clusters of computers. YARN (Yet Another Resource Negotiator) is one of the key components of the Hadoop ecosystem that manages resources in a Hadoop cluster.

### Hadoop Eco System

The Hadoop ecosystem consists of various components that work together to provide a comprehensive solution for big data processing. Some of the key components of the Hadoop ecosystem are:

1. HDFS (Hadoop Distributed File System): HDFS is a distributed file system that stores data across multiple nodes in a Hadoop cluster.

2. MapReduce: MapReduce is a programming model that allows the processing of large data sets across clusters of computers.

3. YARN: YARN is a resource management system that manages resources in a Hadoop cluster.

4. Pig: Pig is a high-level platform for creating MapReduce programs used to analyze large data sets.

5. Hive: Hive is a data warehousing system that provides tools to enable easy data summarization, querying, and analysis of large datasets stored in Hadoop.

6. Spark: Spark is a fast and general-purpose cluster computing system that provides APIs in Java, Scala, and Python for large-scale data processing.

### YARN

YARN is one of the key components of the Hadoop ecosystem that manages resources in a Hadoop cluster. It is responsible for managing resources such as CPU, memory and disk, and assigns them to different applications running on the cluster. YARN consists of two main components:

1. Resource Manager: The Resource Manager is responsible for managing resources in the cluster. It receives resource requests from applications and allocates resources to them.

2. Node Manager: The Node Manager is responsible for managing resources on a single node in the cluster. It communicates with the Resource Manager to allocate resources to applications running on that node.

#### Advantages of YARN

1. YARN allows for the efficient use of resources, as it can allocate CPU, memory, and disk resources to different applications running on the cluster.

2. YARN provides a flexible framework for running various types of applications, including MapReduce, Spark, and Tez.

3. YARN provides fault tolerance by automatically detecting and recovering from node failures.

4. YARN provides a unified platform for managing resources across multiple applications, making it easier to manage large clusters.

#### Disadvantages of YARN

1. YARN can be complex to set up and configure, which can be a barrier to entry for some users.

2. YARN requires a significant amount of resources to run, which can be expensive.

#### Example

Suppose we have a Hadoop cluster with four nodes, each with eight CPU cores and 16 GB of memory. We want to run two MapReduce jobs and one Spark job on this cluster. YARN will allocate resources to these applications based on their resource requirements and the available resources in the cluster.

#### Applications of YARN

1. YARN is used to manage resources in Hadoop clusters running various types of applications, including MapReduce, Spark, and Tez.

2. YARN can be used for resource management in other distributed computing frameworks.

In conclusion, YARN is a key component of the Hadoop ecosystem that manages resources in a Hadoop cluster. It provides a flexible framework for running various types of applications and allows for the efficient use of resources. However, it can be complex to set up and configure, and requires a significant amount of resources to run.