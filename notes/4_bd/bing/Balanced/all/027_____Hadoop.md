### Hadoop

- Hadoop is an open-source software framework for storing data and running applications on clusters of commodity hardware.
- Hadoop provides massive storage for any kind of data, enormous processing power and the ability to handle virtually limitless concurrent tasks or jobs.
- Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage. In this way, Hadoop can efficiently store and process large datasets ranging in size from gigabytes to petabytes of data.
- Hadoop is a collection of open-source software utilities that facilitates using a network of many computers to solve problems involving massive amounts of data and computation. It provides a software framework for distributed storage and processing of big data using the MapReduce programming model.
- Hadoop consists of four main components: Hadoop Common, Hadoop Distributed File System (HDFS), Hadoop MapReduce and Hadoop YARN.
  - Hadoop Common: It contains the libraries and utilities needed by other Hadoop modules.
  - Hadoop Distributed File System (HDFS): It is a distributed file system that provides high-throughput access to application data. It stores data across multiple nodes in a cluster, and replicates data for fault tolerance.
  - Hadoop MapReduce: It is a programming model and software framework for writing applications that process large amounts of data in parallel on clusters of nodes. It consists of two phases: map and reduce. The map phase takes input data and transforms it into key-value pairs. The reduce phase aggregates the values with the same key and produces the output.
  - Hadoop YARN: It is a resource management platform responsible for managing compute resources in clusters and using them for scheduling of users' applications. It allocates resources to different applications based on their requirements and priorities.
- Hadoop can be used for various big data applications, such as data analysis, data mining, data warehousing, machine learning, natural language processing, image processing, etc.
- Hadoop has some advantages, such as:
  - Scalability: Hadoop can scale up to thousands of nodes and handle petabytes of data.
  - Cost-effectiveness: Hadoop can run on commodity hardware, which reduces the cost of hardware and maintenance.
  - Flexibility: Hadoop can store and process any kind of data, whether structured, unstructured or semi-structured.
  - Reliability: Hadoop can handle failures and recover data by replicating it across multiple nodes.
  - Parallelism: Hadoop can process data in parallel on multiple nodes, which increases the speed and efficiency of computation.
- Hadoop also has some disadvantages, such as:
  - Complexity: Hadoop requires a lot of configuration and tuning, and has a steep learning curve.
  - Security: Hadoop does not have built-in security features, and relies on external tools and frameworks for authentication, authorization and encryption.
  - Latency: Hadoop is not suitable for real-time processing, as it has a high latency due to the batch processing nature of MapReduce.
  - Data Quality: Hadoop does not have any data quality checks, and may store and process low-quality or inaccurate data.

- A possible mnemonic to remember the four main components of Hadoop is: **H**ave **C**ommon **F**iles **M**apped and **R**educed by **Y**ARN.