# Anatomy of a Spark job run

- A Spark job is a unit of execution that corresponds to an action on a Spark RDD, DataFrame or Dataset, such as `collect()`, `count()`, `saveAsTextFile()`, etc.
- A Spark job consists of one or more stages, which are logical units of computation that depend on each other.
- A stage is a set of parallel tasks that perform the same computation on different partitions of the input data.
- A task is a unit of work that runs on a single executor and processes a single partition of the data.
- A Spark application contains several components, such as the driver, the master, the cluster manager and the executors.
- The driver is the process that runs the main() method of the Spark application and creates the SparkContext object. It is responsible for converting the user code into a logical execution plan (DAG) and submitting the Spark jobs to the cluster manager.
- The master is the process that coordinates the allocation of resources and the scheduling of tasks across the cluster. It communicates with the cluster manager and the executors to launch and monitor the Spark jobs.
- The cluster manager is the service that manages the worker nodes and the executors in the cluster. It can be one of the supported cluster managers, such as Spark Standalone, YARN, Mesos or Kubernetes.
- The executors are the processes that run on the worker nodes and execute the tasks assigned by the master. They store the intermediate and final results of the computation in memory or disk and communicate with the driver and the master.

The following diagram illustrates the anatomy of a Spark job run:

![Anatomy of a Spark job run](https://i.stack.imgur.com/6Z0X9.png)

: https://stackoverflow.com/questions/42263270/what-is-the-concept-of-application-job-stage-and-task-in-spark