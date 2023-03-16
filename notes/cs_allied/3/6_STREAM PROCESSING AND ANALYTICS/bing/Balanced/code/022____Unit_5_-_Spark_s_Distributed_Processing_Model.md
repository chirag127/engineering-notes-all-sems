```markdown
## Unit 5 - Spark’s Distributed Processing Model

- Apache Spark is a general-purpose distributed data processing engine that can handle various big data scenarios  .
- Spark provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs .
- Spark also supports a rich set of higher-level tools, such as Spark SQL, MLlib, GraphX and Spark Streaming.
- Spark uses the MapReduce framework to distribute the data and computations across a cluster of nodes.
- Spark has two main components: the driver and the executors.
  - The driver is the process that runs the main() method of the application and creates the SparkSession object.
  - The executors are the processes that run on the worker nodes and perform the tasks assigned by the driver.
- Spark uses the concept of resilient distributed datasets (RDDs) to represent the data in a distributed manner.
  - RDDs are immutable, partitioned collections of records that can be operated on in parallel.
  - RDDs can be created from various sources, such as files, databases, or existing collections in memory.
  - RDDs support two types of operations: transformations and actions.
    - Transformations create new RDDs from existing ones, such as map, filter, join, etc.
    - Actions trigger the computation and return the results to the driver, such as count, collect, save, etc.
- Spark uses a lazy evaluation model, which means that the transformations are not executed until an action is called.
  - This allows Spark to optimize the execution plan and avoid unnecessary data movement and computation.
  - Spark also caches the intermediate results of RDDs in memory or disk for faster access in subsequent operations.
- Spark uses a directed acyclic graph (DAG) to represent the logical execution plan of the application.
  - A DAG is a graph of RDDs and their dependencies, where each node is an RDD and each edge is a transformation.
  - Spark divides the DAG into stages, where each stage contains a set of tasks that can be executed in parallel on the same data.
  - Spark then schedules the tasks to run on the executors based on the data locality and availability.
- Spark supports fault tolerance by using lineage information to recover the lost data in case of node failures.
  - Lineage is the sequence of transformations that produced an RDD from the original data source.
  - Spark can recompute the missing partitions of an RDD by retracing its lineage from the available data.
  - Spark can also checkpoint the RDDs to external storage to reduce the recomputation cost.
```