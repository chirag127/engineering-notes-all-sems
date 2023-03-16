## Unit 5 - Spark’s Distributed Processing Model

- Apache Spark is a general-purpose distributed data processing engine that can handle big data workloads  .
- Spark provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs .
- Spark also supports a rich set of higher-level tools including Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Spark Streaming for stream processing.
- Spark uses the MapReduce framework to distribute the data and computation across multiple nodes in a cluster.
- Spark has a master-slave architecture, where the master node is called the driver and the slave nodes are called the executors.
- The driver is responsible for creating and managing the SparkContext, which is the main entry point for Spark applications. The SparkContext coordinates the execution of tasks on the executors.
- The executors are responsible for running the tasks assigned by the driver and returning the results. The executors also store and cache data in memory or disk.
- Spark divides the data into logical partitions called RDDs (Resilient Distributed Datasets), which are immutable and fault-tolerant collections of records that can be operated on in parallel .
- Spark supports two types of operations on RDDs: transformations and actions. Transformations create new RDDs from existing ones, while actions trigger the computation and return the results to the driver or write them to external storage .
- Spark uses lazy evaluation, which means that transformations are not executed until an action is called. This allows Spark to optimize the execution plan and avoid unnecessary data movement .
- Spark also uses a DAG (Directed Acyclic Graph) scheduler, which tracks the dependencies between RDDs and stages, and determines the optimal way to execute the tasks on the cluster .
- Spark can run on various cluster managers, such as Hadoop YARN, Apache Mesos, or standalone mode. Spark can also run locally on a single machine for testing or development purposes .