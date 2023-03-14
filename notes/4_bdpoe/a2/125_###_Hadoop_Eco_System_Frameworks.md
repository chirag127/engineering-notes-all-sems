 Here is the content in markdown format on the topic ### Hadoop Eco System Frameworks:

### Hadoop Eco System Frameworks

The Hadoop ecosystem refers to the framework and components that make up the Hadoop distributed processing system. The Hadoop ecosystem includes the following major components:

1. Hadoop Common: The common utilities that support the other Hadoop modules. It includes filesystems (HDFS), configurations, deployment scripts, etc.
2. Hadoop Distributed File System (HDFS): A distributed filesystem that stores data on commodity machines, providing very high aggregate bandwidth across the cluster.
3. Hadoop YARN: A framework for job scheduling and cluster resource management. It replaces Hadoop's initial job scheduler, which could only handle MapReduce jobs. YARN can handle various workloads, including real-time processing.
4. Hadoop MapReduce: A YARN-based system for parallel processing of large data sets. It divides the work into independent chunks which are processed in parallel on multiple nodes in a cluster.
5. Hadoop Ozone: An object store for Hadoop. It provides scalable and redundant storage for data on HDFS using object storage concepts.

Some key points to remember:

- Hadoop is scalable and fault-tolerant.
- HDFS splits files into large blocks and distributes them across nodes.
- YARN allocates resources to various frameworks and applications running on Hadoop.
- MapReduce consists of mappers (splitting and mapping) and reducers (shuffling and reducing).

Advantages of Hadoop include:

- Scalability: Hadoop can scale to petabytes of data and thousands of nodes.
- Fault tolerance: Hadoop is highly fault tolerant due to data replication and persistent storage.
- Low cost: Hadoop runs on commodity hardware and is open source.
- Flexibility: Hadoop supports various data types (structured, unstructured) and workloads (batch, interactive, real-time).

Applications of Hadoop include:

- Web indexing
- Log processing
- Social network analysis
- Genome sequencing analysis
- Internet of Things
- And more!