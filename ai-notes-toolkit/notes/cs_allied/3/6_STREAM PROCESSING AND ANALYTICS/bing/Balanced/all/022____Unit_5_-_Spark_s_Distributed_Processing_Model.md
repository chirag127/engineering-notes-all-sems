# Unit 5 - Spark's Distributed Processing Model

- Spark is an open-source, general-purpose distributed processing engine that can handle big data workloads .
- Spark uses the MapReduce framework to parallelize tasks across multiple nodes in a cluster.
- Spark supports several programming languages, such as Java, Scala, Python and R, and provides high-level APIs for data processing.
- Spark also offers a rich set of libraries for various domains, such as Spark SQL, MLlib, GraphX and Spark Streaming .
- Spark's core abstraction is the Resilient Distributed Dataset (RDD), which is a distributed collection of data that can be operated on in parallel.
- RDDs can be created from various sources, such as files, databases, or existing collections in memory.
- RDDs support two types of operations: transformations and actions.
- Transformations create new RDDs from existing ones, such as map, filter, join, etc.
- Actions perform computations on RDDs and return results to the driver program, such as count, collect, save, etc.
- Spark uses lazy evaluation, which means that transformations are not executed until an action is called.
- Spark also uses in-memory caching and optimized query execution to achieve fast performance .
- Spark can run on various cluster managers, such as Hadoop YARN, Apache Mesos, or standalone mode .