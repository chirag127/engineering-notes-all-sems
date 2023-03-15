### How does HDFS store data?

- HDFS (Hadoop Distributed File System) is a distributed file system that runs on a cluster of nodes and stores large amounts of data in a scalable and fault-tolerant way.
- HDFS stores data in the form of files, which are divided into fixed-size blocks (default size is 128 MB, but can be configured) and distributed across the cluster.
- Each block is replicated on multiple DataNodes (usually three, but can be configured) to ensure high availability and reliability in case of node failures or network partitions.
- The NameNode is the master node that manages the file system namespace and the metadata of the files and blocks. It keeps track of the location and status of each block and DataNode in the cluster.
- The DataNodes are the worker nodes that store the blocks and serve the read and write requests from the clients. They also perform periodic block reports and heartbeats to the NameNode to update their status and availability.
- The clients interact with the NameNode to perform file system operations, such as creating, deleting, renaming, or appending files. They also communicate with the DataNodes to read or write data to the blocks.
- HDFS provides a way for MapReduce to process large data sets in parallel by splitting them into blocks and distributing them across the cluster. Each MapReduce task can access a subset of the data locally on the DataNode, reducing the network overhead and improving the performance.