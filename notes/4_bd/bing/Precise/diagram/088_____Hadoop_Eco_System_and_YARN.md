### Hadoop Eco System and YARN

Here is an ASCII diagram of the Hadoop Eco System and YARN:

```
+----------------+
|  Hadoop Eco    |
|  System        |
|                |
|  +----------+  |
|  |   YARN   |  |
|  +----------+  |
|                |
|  +----------+  |
|  |   HDFS   |  |
|  +----------+  |
|                |
|  +----------+  |
|  |   Map    |  |
|  |  Reduce  |  |
|  +----------+  |
|                |
+----------------+
```

YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop. It is responsible for managing and allocating resources for the various applications running on the Hadoop cluster. HDFS (Hadoop Distributed File System) is the storage layer of Hadoop, responsible for storing and managing data across the cluster. MapReduce is a programming model for processing large data sets in parallel across the cluster.
