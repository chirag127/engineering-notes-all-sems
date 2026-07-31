## Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that is designed to run on commodity hardware. It is highly fault-tolerant and provides high throughput access to large datasets. Some key features of HDFS include:

1. **Scalability:** HDFS can scale to handle petabytes of data by distributing it across many machines.
2. **Data Reliability:** HDFS replicates data blocks across multiple machines to ensure data reliability and availability.
3. **High Throughput:** HDFS is optimized for batch processing and provides high throughput for large datasets.
4. **Cost-Effective:** HDFS is designed to run on commodity hardware, making it a cost-effective solution for storing large datasets.

HDFS has a master/slave architecture. The master node, called the NameNode, manages the file system namespace and regulates access to files. The slave nodes, called DataNodes, store the data blocks and perform block-level operations. The NameNode and DataNodes communicate with each other using the Hadoop IPC (Inter-Process Communication) mechanism.

HDFS stores files as a sequence of blocks. Each block is typically 128 MB in size and is replicated across multiple DataNodes for fault tolerance. When a client wants to read a file, the NameNode provides the client with the locations of the blocks that make up the file. The client then reads the data directly from the DataNodes.

HDFS also provides several mechanisms for ensuring data integrity. For example, when a client writes data to HDFS, the data is first written to a local disk on the client machine. Once the data is written to the local disk, the client sends the data to the first DataNode in the pipeline. The first DataNode then sends the data to the second DataNode in the pipeline, and so on. Each DataNode in the pipeline verifies the data before forwarding it to the next DataNode. If any DataNode detects a problem with the data, it notifies the client and the write operation fails.

In summary, HDFS is a distributed file system that provides scalable, reliable, and high-throughput access to large datasets. It is designed to run on commodity hardware and is an integral part of the Hadoop ecosystem.