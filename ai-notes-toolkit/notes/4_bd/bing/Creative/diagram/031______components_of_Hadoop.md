#### Components of Hadoop

Hadoop is a framework for distributed storage and processing of large-scale data sets. It consists of the following components:

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that stores data in a distributed manner across multiple nodes in a cluster. HDFS provides high availability, fault tolerance, scalability, and data locality. HDFS splits data into fixed-size blocks and replicates them across different nodes for redundancy. HDFS also supports a hierarchical namespace and allows users to create, delete, rename, and move files and directories  .

- **Hadoop MapReduce**: This is the processing layer of Hadoop that implements a parallel programming model for processing large data sets. MapReduce consists of two phases: map and reduce. In the map phase, data is read from HDFS and transformed into key-value pairs by user-defined functions. In the reduce phase, the key-value pairs are aggregated, sorted, and written back to HDFS by user-defined functions. MapReduce provides scalability, fault tolerance, and load balancing by distributing the tasks across multiple nodes in a cluster  .

- **Hadoop YARN**: This is the resource management layer of Hadoop that allocates and manages resources for different applications running on a cluster. YARN stands for Yet Another Resource Negotiator. YARN consists of two components: a global Resource Manager that oversees the entire cluster and a per-node Node Manager that monitors and reports the resource usage of each node. YARN also supports a pluggable scheduler that assigns resources to different applications based on their priority, queue, and resource requirements  .

- **Hadoop Common**: This is a set of shared libraries and utilities that support the other components of Hadoop. Hadoop Common provides common functionalities such as configuration, logging, serialization, security, and networking. Hadoop Common also defines the Hadoop API that allows users to interact with the Hadoop system.

The following diagram illustrates the components of Hadoop and their interactions:

```
+-----------------+       +-----------------+
|                 |       |                 |
|  Hadoop Common  |       |  Hadoop Common  |
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|   Hadoop YARN   |       |   Hadoop YARN   |
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
+-----------------+       +-----------------+
|                 |       |                 |
| Hadoop MapReduce|       | Hadoop MapReduce|
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|     HDFS        |       |     HDFS        |
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|     Data        |       |     Data        |
|                 |       |                 |
+-----------------+       +-----------------+
```

: https://www.datavail.com/blog/3-core-components-of-the-hadoop-framework/
: https://www.digitalvidya.com/blog/what-is-hadoop/
: https://www.educba.com/hadoop-components/