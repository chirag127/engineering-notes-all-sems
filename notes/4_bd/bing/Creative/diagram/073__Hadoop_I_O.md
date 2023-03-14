Hadoop I/O is the system that handles the input and output of data in a Hadoop cluster. It consists of four main components:

- Hadoop Distributed File System (HDFS): This is the storage layer that splits the incoming data into blocks and distributes them across the nodes in the cluster. HDFS also maintains data integrity by using checksums and replication.
- MapReduce: This is the processing layer that applies a map function to each data block and then reduces the results into a final output. MapReduce is based on the MapReduce programming model that allows for parallel and distributed processing of large datasets.
- YARN: This is the resource management layer that allocates and schedules the resources (CPU, memory, disk, network) for the applications running on the cluster. YARN also provides a generic interface for other data processing tools to integrate with Hadoop.
- Hadoop Common: This is the utility layer that provides the common libraries and utilities that are used by the other components. Hadoop Common also includes the configuration and security modules for the cluster.

The following diagram illustrates the basic architecture of a Hadoop I/O system:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop Node   |    |   Hadoop Node   |    |   Hadoop Node   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+