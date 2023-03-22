 Here are the notes for Unit 4 - HDFS (Hadoop Distributed File System) in Markdown format:

### HDFS (Hadoop Distributed File System)

1. HDFS is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.

2. HDFS creates multiple replicas of data blocks and distributes them on compute nodes throughout a cluster to enable reliable, extremely rapid computations.

3. The HDFS architecture is comprised of a NameNode, DataNodes, and Clients. The NameNode manages the file system namespace and regulates access to files by clients. DataNodes store data blocks and serve read/write requests from clients. Clients use the HDFS protocol to communicate with the NameNode and DataNodes.

4. HDFS provides interfaces for applications to move themselves closer to where the data is located. This results in very high aggregate bandwidth across the cluster.

5. The file system is highly fault-tolerant and is designed to be deployed on low-cost hardware. It provides high throughput access to application data and is suitable for applications that have large data sets.

6. HDFS is designed to support very large files. Applications that are compatible with HDFS are those that deal with large data sets, or those that need streaming access to file system data at high bandwidth.

7. The key benefits of HDFS are:

- Scalability: HDFS is designed to scale up from single servers to large clusters of machines.
- Fault tolerance: Data is automatically replicated to handle failures.
- Cost: HDFS is designed to reliably store very large data sets with streaming access patterns with high aggregate bandwidth and scale to large clusters with low-cost hardware.
- Simplicity: The HDFS architecture is simple. It consists of a single NameNode and multiple DataNodes.