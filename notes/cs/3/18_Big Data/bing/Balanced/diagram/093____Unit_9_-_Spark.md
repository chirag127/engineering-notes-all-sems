## Unit 9 - Spark

- Spark is a distributed computing framework that allows processing large-scale data in parallel and in memory.
- Spark consists of a core engine and a set of libraries that provide various functionalities such as SQL, streaming, machine learning, and graph processing.
- Spark runs on a cluster of machines, where each machine is called a node. A node can be either a master or a worker.
- The master node coordinates the execution of tasks across the worker nodes, and the worker nodes run the tasks assigned by the master node.
- A task is a unit of work that can be executed on a single node. A task can be part of a stage, which is a group of tasks that can be executed in parallel. A stage can be part of a job, which is a logical unit of work that consists of one or more stages.
- Spark uses a data abstraction called resilient distributed dataset (RDD), which is a collection of elements that can be partitioned across the nodes of the cluster and operated on in parallel.
- RDDs can be created from various sources, such as files, databases, or other RDDs. RDDs can be transformed by applying operations such as map, filter, join, or reduce. RDDs can also be cached in memory or on disk for faster access.
- Spark also provides a higher-level data abstraction called DataFrame, which is a distributed collection of rows organized into named columns. DataFrames can be created from various sources, such as files, databases, or RDDs. DataFrames can be manipulated by using SQL-like expressions or domain-specific language (DSL) methods.
- Spark supports various programming languages, such as Scala, Python, Java, and R. Spark also provides an interactive shell and a web-based user interface for monitoring and debugging applications.