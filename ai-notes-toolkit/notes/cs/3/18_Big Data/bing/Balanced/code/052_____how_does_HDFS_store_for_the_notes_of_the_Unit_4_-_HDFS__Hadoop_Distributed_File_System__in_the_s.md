### How does HDFS store

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing and processing large-scale data sets in a cluster of commodity hardware.
- HDFS stores data in a distributed manner by dividing the files into fixed-size blocks (default 128 MB) and replicating them across multiple DataNodes in the cluster .
- DataNodes are the slave nodes that store and manage the data blocks, while NameNode is the master node that maintains the file system namespace and the metadata of the blocks .
- HDFS provides a way for MapReduce to process a subset of the data blocks in parallel on different DataNodes, thus achieving high throughput and scalability.
- HDFS also handles failures and recovery of DataNodes by replicating the blocks to other DataNodes and re-balancing the load among the cluster.
- HDFS supports a variety of file formats, such as text, binary, compressed, and serialized. It also provides a command-line interface and a Java API for accessing and manipulating the files.