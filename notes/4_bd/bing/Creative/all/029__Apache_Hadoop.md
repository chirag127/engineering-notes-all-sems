#### Apache Hadoop

- Apache Hadoop is a collection of open-source software utilities that facilitates using a network of many computers to solve problems involving massive amounts of data and computation. 
- It provides a software framework for distributed storage and processing of big data using the MapReduce programming model. 
- Hadoop was originally designed for computer clusters built from commodity hardware, which is still the common use. 
- It has since also found use on clusters of higher-end hardware. 
- All the modules in Hadoop are designed with a fundamental assumption that hardware failures are common occurrences and should be automatically handled by the framework. 
- The core of Apache Hadoop consists of a storage part, known as Hadoop Distributed File System (HDFS), and a processing part which is a MapReduce programming model. 
- Hadoop splits files into large blocks and distributes them across nodes in a cluster. 
- It then transfers packaged code into nodes to process the data in parallel. 
- This approach takes advantage of data locality, where nodes manipulate the data they have access to. 
- This allows the dataset to be processed faster and more efficiently than it would be in a more conventional supercomputer architecture that relies on a parallel file system where computation and data are distributed via high-speed networking. 
- The base Apache Hadoop framework is composed of the following modules: 
  - Hadoop Common – contains libraries and utilities needed by other Hadoop modules;
  - Hadoop Distributed File System (HDFS) – a distributed file-system that stores data on commodity machines, providing very high aggregate bandwidth across the cluster;
  - Hadoop YARN – (introduced in 2012) a platform responsible for managing computing resources in clusters and using them for scheduling users' applications;
  - Hadoop MapReduce – an implementation of the MapReduce programming model for large-scale data processing.
  - Hadoop Ozone – (introduced in 2020) An object store for Hadoop
- The term Hadoop is often used for both base modules and sub-modules and also the ecosystem, or collection of additional software packages that can be installed on top of or alongside Hadoop, such as Apache Pig, Apache Hive, Apache HBase, Apache Phoenix, Apache Spark, Apache ZooKeeper, Apache Impala, Apache Flume, Apache Sqoop, Apache Oozie, and Apache Storm. 

- A possible mnemonic to remember the core modules of Hadoop is **CHYMO** (Common, HDFS, YARN, MapReduce, Ozone).
- A possible learning trick to understand the MapReduce programming model is to think of it as a two-step process: 
  - Map: Apply a function to each input data element and produce a set of intermediate key-value pairs.
  - Reduce: Combine the intermediate values associated with the same key and produce the final output.
- A possible ascii diagram to illustrate the Hadoop architecture is:

```
+-----------------+       +-----------------+
|   Hadoop Ecosystem      |       |   Hadoop Ecosystem      |
|   (Pig, Hive, HBase,    |       |   (Pig, Hive, HBase,    |
|   Spark, etc.)          |       |   Spark, etc.)          |
+-----------------+       +-----------------+
         |                         |
         |                         |
         v                         v
+-----------------+       +-----------------+
|   Hadoop Common |       |   Hadoop Common |
+-----------------+       +-----------------+
         |                         |
         |                         |
         v                         v
+-----------------+       +-----------------+
|   Hadoop YARN   |       |   Hadoop YARN   |
+-----------------+       +-----------------+
         |                         |
         |                         |
         v                         v
+-----------------+       +-----------------+
|   Hadoop MapReduce      |       |   Hadoop MapReduce      |
+-----------------+       +-----------------+
         |                         |
         |                         |
         v                         v
+-----------------+       +-----------------+
|   Hadoop HDFS   |       |   Hadoop HDFS   |
+-----------------+       +-----------------+
         |                         |
         |                         |
         v                         v
+-----------------+       +-----------------+
|   Hadoop Ozone  |       |   Hadoop