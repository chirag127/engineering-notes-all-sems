 Here is the content in Markdown format without any emojis or external links:

### Hadoop Ecosystem Frameworks

1. HDFS - Hadoop Distributed File System
- Master-slave architecture
- Files are split into blocks and distributed across clusters
- Replication provides fault tolerance
- High throughput access to application data

2. YARN - Yet Another Resource Negotiator
- Resource management platform
- Separates resource management and job scheduling/monitoring
- Has ResourceManager and NodeManager
- Supports multiple data processing frameworks

3. MapReduce
- Programming model for processing large data sets
- Uses distributed algorithms that process the data in parallel
- Has Map and Reduce phases
- Scales to thousands of nodes

4. Hive
- Data warehouse infrastructure built on top of Hadoop
- Uses SQL-like language called HiveQL
- Translates queries into MapReduce jobs
- Good for summarizing, querying, and analyzing large data sets

5. Pig
- Platform for analyzing large data sets
- Uses Pig Latin language
- Compiles queries into sequences of MapReduce programs
- Handles complex data transformations and interactions between data sets

6. HBase
- Distributed, scalable, big data store
- Built on top of HDFS
- Stores data in tables with rows and columns
- Like a distributed, scalable implementation of a Bigtable
- Good for random, real-time read/write access to big data

7. ZooKeeper
- Centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services
- Stores data in a hierarchical name space
- Pulls data via watches and can trigger actions or recover from errors
- Used by Hadoop for coordination and service discovery