
#### Block Abstraction in HDFS

* HDFS (Hadoop Distributed File System) is a distributed file system that allows for large-scale data storage and processing.
* Blocks are the basic unit of storage in HDFS. A block is a fixed-size contiguous set of bytes, typically 64MB or 128MB in size. Blocks are the physical storage units of HDFS, and the smallest unit of data that can be read or written.
* Blocks are stored in a distributed manner across multiple machines in the cluster, and are replicated to provide fault tolerance.
* The block abstraction in HDFS allows for data to be split into blocks and stored across multiple nodes in a cluster, providing scalability and fault tolerance.
* HDFS also provides high throughput access to data, by allowing multiple clients to read and write data in parallel.