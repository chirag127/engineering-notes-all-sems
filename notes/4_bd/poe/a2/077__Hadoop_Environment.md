 Here is the content in markdown format with formal tone and without external links or emojis:

## Hadoop Environment

1. Hadoop Distributed File System (HDFS): HDFS is the primary storage system used by Hadoop. It is highly fault-tolerant and designed to be deployed on low-cost hardware. HDFS provides high throughput access to application data and is suitable for applications that have large data sets.

2. Hadoop MapReduce: MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. MapReduce divides the processing into two main phases:

- The map phase: Each node takes the input data and divides it into smaller sub-problems.
- The reduce phase: The results from the map phase are combined to form the output.

3. Hadoop YARN: Yet Another Resource Negotiator (YARN) is the cluster management technology in Hadoop that allows multiple data processing engines to handle data stored in HDFS. YARN manages resources and schedules applications running on the cluster. It features a central ResourceManager and ApplicationMaster(s) per application to negotiate resources.

4. Hadoop Common: Hadoop Common contains libraries and utilities needed by other Hadoop modules. It includes essentials like filesystem interfaces, logging APIs, and configuration management.

The above points highlight the key components in the Hadoop environment required to deploy and operate a Hadoop cluster. Together, these components enable the distributed processing and storage of big data.