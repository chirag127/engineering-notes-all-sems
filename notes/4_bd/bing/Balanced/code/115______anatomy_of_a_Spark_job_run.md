#### Anatomy of a Spark job run

- A Spark job is a unit of execution that corresponds to an action on a Spark RDD, DataFrame or Dataset, such as `collect()`, `saveAsTextFile()` or `count()`.
- A Spark job consists of one or more stages, which are parallel computations that operate on a partitioned dataset.
- A stage is divided into tasks, which are the smallest unit of execution that run on a single executor (a process that runs on a worker node).
- A Spark application contains several components, such as the driver, the master, the cluster manager and the executors, which communicate and coordinate the execution of a Spark job.
- The driver is the process that runs the main() method of the Spark application and creates the SparkContext object. It is responsible for converting the user code into a logical plan (a DAG of RDDs) and a physical plan (a DAG of stages and tasks), and submitting the Spark job to the cluster manager.
- The master is the process that coordinates the allocation of resources and the scheduling of tasks across the worker nodes. It can be either a standalone process, a YARN ResourceManager, a Mesos master or a Kubernetes API server, depending on the cluster mode.
- The cluster manager is the service that manages the worker nodes and the executors that run on them. It can be either Spark's own standalone cluster manager, YARN, Mesos or Kubernetes, depending on the cluster mode.
- The executors are the processes that run on the worker nodes and execute the tasks assigned by the driver. They also store the data partitions in memory or disk, and communicate with the driver and other executors.
- The following diagram illustrates the anatomy of a Spark job run:

![Anatomy of a Spark job run](https://i.stack.imgur.com/0Zf0o.png)