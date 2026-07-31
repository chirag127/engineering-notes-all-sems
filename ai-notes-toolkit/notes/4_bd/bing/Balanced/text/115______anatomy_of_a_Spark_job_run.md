#### Anatomy of a Spark job run

- A Spark job is a unit of execution that corresponds to an action on a Spark application, such as `collect()` or `saveAsTextFile()`.
- A Spark job consists of one or more stages, which are parallel computations that operate on a subset of the data.
- A stage is divided into tasks, which are the smallest unit of execution that run on a single executor (a process that runs on a worker node).
- A task applies a transformation or an action to a partition of an RDD (a distributed collection of data).
- A Spark job is executed by the Spark scheduler, which creates a directed acyclic graph (DAG) of stages and tasks based on the dependencies between RDDs.
- The Spark scheduler submits the stages and tasks to the cluster manager, which allocates resources (such as CPU cores and memory) to the executors.
- The executors run the tasks and send the results back to the driver (the process that runs the Spark application).
- The driver collects the results and returns them to the user or writes them to a storage system.