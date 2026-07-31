#### Scaling out with Hadoop

- Hadoop is an open-source software framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models.
- It is designed to scale up from single servers to thousands of machines, each offering local computation and storage.
- Hadoop achieves reliability by replicating the data across multiple hosts, and hence does not require RAID storage on hosts.
- With the default replication value, 3, data is stored on three nodes: two on the same rack, and one on a different rack.
- Data nodes can talk to each other to rebalance data, to move copies around, and to keep the replication of data high.
- Hadoop is designed to be rack-aware, meaning that it can take into account the location of data nodes in relation to each other in order to reduce network traffic between them.
- Hadoop can be used to scale out data processing by adding more nodes to the cluster, allowing for the processing of larger data sets.
- Hadoop's architecture is designed to be modular, allowing for the addition of new data processing components as needed.
- Hadoop's MapReduce programming model allows for the easy parallelization of data processing tasks, making it well-suited for scaling out data processing.
- Hadoop's distributed file system, HDFS, is designed to be fault-tolerant, meaning that it can continue to operate even in the event of node failure.
- Hadoop's ability to scale out data processing makes it a popular choice for big data applications, where large amounts of data need to be processed quickly.