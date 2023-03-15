## Unit 9 - Spark

- Spark is a distributed computing framework that allows processing large-scale data in parallel and in memory.
- Spark consists of a core engine and a set of libraries that provide various functionalities such as SQL, streaming, machine learning, and graph processing.
- Spark runs on a cluster of machines, where each machine is called a node. A node can be either a master or a worker. The master node coordinates the execution of tasks and the worker nodes execute the tasks.
- Spark uses a data abstraction called resilient distributed dataset (RDD), which is a collection of elements that can be partitioned across the nodes and operated on in parallel.
- Spark supports two types of operations on RDDs: transformations and actions. Transformations create new RDDs from existing ones, such as map, filter, join, etc. Actions trigger the computation and return a value or write data to an external system, such as count, collect, save, etc.
- Spark also provides a higher-level data abstraction called DataFrame, which is a distributed collection of rows organized into named columns. DataFrames can be created from various sources, such as files, databases, or RDDs. DataFrames support a rich set of operations, such as SQL queries, aggregations, joins, etc.
- Spark supports various programming languages, such as Scala, Python, Java, and R. Spark also provides an interactive shell and a web-based notebook for exploring data and running code.
- Spark can run on various cluster managers, such as Hadoop YARN, Apache Mesos, or standalone mode. Spark can also run locally on a single machine for testing or development purposes.