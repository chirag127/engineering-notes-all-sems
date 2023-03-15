### Anatomy of a Spark job run

- A Spark job is a unit of execution that corresponds to an action on a Spark RDD, DataFrame or Dataset, such as `collect()`, `saveAsTextFile()` or `count()`.
- A Spark job consists of one or more stages, which are parallel computations that operate on a subset of the data and produce intermediate results.
- A stage is divided into tasks, which are the smallest unit of execution that run on a single executor (a process that runs on a worker node and executes tasks).
- A task applies a transformation or an action to a partition of the data, such as `map()`, `filter()` or `reduceByKey()`.
- A task may depend on the output of other tasks from previous stages, which are stored in memory or disk as shuffle files.
- A Spark job is executed by the driver program, which is the main program that creates the SparkSession and defines the Spark operations.
- The driver program communicates with the cluster manager, which is a service that allocates resources (such as CPU cores and memory) to the Spark application across the cluster.
- The cluster manager can be a standalone service, or a framework such as YARN or Mesos.
- The driver program also communicates with the Spark master, which is a process that coordinates the execution of Spark jobs across the cluster.
- The Spark master assigns tasks to the executors, which are processes that run on the worker nodes and execute tasks.
- The Spark master also monitors the status of the executors and the tasks, and handles failures and retries.
- The Spark master and the executors communicate through the Spark UI, which is a web interface that shows the details of the Spark application, such as the stages, tasks, resources, logs and metrics.