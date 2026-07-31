#### Block Abstraction in HDFS

- HDFS (Hadoop Distributed File System) is a distributed file system designed to store large data sets across multiple machines.
- HDFS uses the concept of block abstraction to manage the storage of data.
- In HDFS, files are divided into blocks of fixed size (default size is 128 MB) and these blocks are distributed across the nodes in the cluster.
- Each block is stored on multiple nodes (default replication factor is 3) to ensure data availability and fault tolerance.
- The NameNode is responsible for managing the metadata of the blocks, including the location of each block and the list of DataNodes that store the block.
- The DataNodes are responsible for storing the blocks and serving read and write requests from clients.
- When a client wants to read a file, it contacts the NameNode to obtain the location of the blocks that make up the file. The client then reads the data directly from the DataNodes that store the blocks.
- When a client wants to write a file, it contacts the NameNode to obtain a list of DataNodes where the blocks should be stored. The client then writes the data directly to the DataNodes.
- Block abstraction allows HDFS to scale horizontally by adding more DataNodes to the cluster, and to handle failures by replicating blocks on multiple DataNodes.

Mnemonic: **H**DFS uses **B**lock abstraction to manage the storage of data, with a **D**efault block size of 128 MB and a **D**efault replication factor of 3, managed by the **N**ameNode and stored on **D**ataNodes.