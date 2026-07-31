## Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that is designed to run on commodity hardware. It is highly fault-tolerant and provides high throughput access to application data. Some key features of HDFS include:

1. **Scalability:** HDFS can scale to handle petabytes of data by distributing it across many machines.
2. **Data Reliability:** HDFS replicates data across multiple machines to ensure that data is not lost due to hardware failure.
3. **High Throughput:** HDFS is optimized for batch processing and can provide high throughput for large data sets.
4. **Cost-Effective:** HDFS is designed to run on commodity hardware, making it a cost-effective solution for storing large amounts of data.

HDFS has a master/slave architecture. The master node, called the NameNode, manages the file system namespace and regulates access to files by clients. The slave nodes, called DataNodes, store the actual data. Clients read and write data by interacting with the DataNodes, while the NameNode ensures that the file system remains consistent.

In summary, HDFS is a distributed file system that provides scalable, reliable, and cost-effective storage for large data sets. It is an essential component of the Hadoop ecosystem and is widely used in big data applications.