 Here is the content in markdown format for Hadoop Eco System and YARN:

### Hadoop Eco System and YARN

The Hadoop ecosystem refers to the suite of tools and modules that are designed to work with Hadoop. Some of the major components of the Hadoop ecosystem are:

- HDFS - Hadoop Distributed File System: The primary storage system used by Hadoop. It splits files into large blocks and distributes them across nodes in a cluster.
- MapReduce: A programming model for large scale data processing. It consists of two major tasks - Map and Reduce. The Map task partitions the input dataset into smaller chunks which are processed by the Reduce tasks.
- YARN: A framework for job scheduling and cluster resource management. It allows multiple data processing frameworks to handle data stored in the Hadoop Distributed File System.

Some key points to remember about YARN are:

- It separates resource management and job scheduling/monitoring functions.
- The ResourceManager allocates resources and handles resource requests from applications.
- The NodeManager is the per-node agent that launches and monitors containers.
- The ApplicationMaster is responsible for negotiating resources from the ResourceManager and working with the NodeManager(s) to execute and monitor the containers for its application.
- YARN has a client service to submit and monitor applications.

Advantages of YARN:

- Supports multiple data processing frameworks besides MapReduce like Spark, Hive, Pig, etc.
- Scales to larger clusters and supports more applications simultaneously.
- Improved utilization of cluster resources.
- Separates concerns of resource management and job scheduling.

Applications of Hadoop Eco System and YARN:

- Processing and storing huge volumes of data
- Log processing and analysis
- Recommendation systems
- Image processing
- Genomics and bioinformatics
- Machine learning

[Include detailed diagrams, codes, tables, more advantages/disadvantages/examples/applications as needed]