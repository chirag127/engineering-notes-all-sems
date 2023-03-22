 Here is the markdown content for the given topic:

### Hadoop Configuration for Unit 5 - Hadoop Environment

1. Hadoop distributed file system (HDFS)
- HDFS splits files into large blocks (typically 128MB) and stores multiple replicas of them across different nodes in the cluster.
- This provides very high aggregate bandwidth across the cluster.
- The default replication factor is 3, so that even if one node fails, the data can still be accessed.
- The master node is called the NameNode and manages the file system namespace and regulates access to files.
- DataNodes are the slave nodes that store the blocks and serve read/write requests.

2. MapReduce
- MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster.
- The computation takes a set of input key/value pairs, and produces a set of output key/value pairs.
- The Map and Reduce phases are both parallelized and run on different nodes in the cluster.
- The Map phase does the data filtering/sorting and the Reduce phase does the final aggregation or summarization.
- Hadoop takes care of automatically partitioning data and scheduling tasks across the cluster.

3. Hadoop YARN
- YARN (Yet Another Resource Negotiator) is the cluster resource management system in Hadoop.
- It splits up cluster resource management into a global ResourceManager and per-application ApplicationMaster.
- The ResourceManager arbitrates resources in the cluster and handles scheduling.
- The ApplicationMaster negotiates resources from the ResourceManager and works with NodeManagers to execute and monitor the containers.
- This separation enables YARN to support various data processing frameworks beyond MapReduce.

[No external links added and content written in a formal tone with points as requested.]