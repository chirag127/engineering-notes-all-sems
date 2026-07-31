# Scaling Out for the Notes of the Unit 2 - Hadoop in the Subject of Big Data

- Scaling out is a technique of increasing the processing power and storage capacity of a system by adding more nodes or servers, rather than upgrading the existing ones.
- Scaling out is also known as horizontal scaling or data parallelism, as it involves splitting the data into smaller chunks and processing them in parallel across multiple nodes.
- Scaling out is suitable for big data applications, as it can handle large volumes, high velocity, and variety of data, while providing fault tolerance, load balancing, and scalability.
- Hadoop is an open-source framework that enables scaling out of big data applications by providing a distributed file system (HDFS) and a distributed processing engine (MapReduce).
- Hadoop can run on commodity hardware and can scale from a few nodes to thousands of nodes, depending on the data size and processing needs.
- Hadoop follows a master-slave architecture, where a single master node (NameNode) manages the metadata and coordinates the data access, and multiple slave nodes (DataNodes) store and process the data blocks.
- Hadoop also supports other components and tools, such as Hive, Pig, Spark, HBase, etc., that provide higher-level abstractions and functionalities for big data analytics.
- Some of the benefits of scaling out with Hadoop are:
  - Cost-effectiveness: Hadoop can run on low-cost hardware and use open-source software, reducing the capital and operational expenses.
  - Performance: Hadoop can leverage the parallelism and locality of data to speed up the processing and reduce the network overhead.
  - Reliability: Hadoop can replicate the data blocks across multiple nodes and handle node failures gracefully, ensuring data availability and consistency.
  - Flexibility: Hadoop can handle structured, semi-structured, and unstructured data, and support various data formats and schemas.
  - Scalability: Hadoop can scale linearly by adding more nodes to the cluster, without affecting the existing nodes or data.
- Some of the challenges of scaling out with Hadoop are:
  - Complexity: Hadoop requires a lot of configuration and tuning, and involves low-level programming and debugging, which can be difficult and time-consuming for developers and administrators.
  - Security: Hadoop does not provide strong security mechanisms, such as encryption, authentication, authorization, etc., and relies on external tools and frameworks, such as Kerberos, Ranger, Sentry, etc., to ensure data protection and privacy.
  - Data quality: Hadoop does not enforce any data quality checks or validations, and allows any type of data to be ingested and processed, which can result in data inconsistency, incompleteness, or inaccuracy.
  - Resource management: Hadoop does not have a sophisticated resource management system, and relies on external tools and frameworks, such as YARN, Mesos, Kubernetes, etc., to allocate and schedule the resources across the cluster.