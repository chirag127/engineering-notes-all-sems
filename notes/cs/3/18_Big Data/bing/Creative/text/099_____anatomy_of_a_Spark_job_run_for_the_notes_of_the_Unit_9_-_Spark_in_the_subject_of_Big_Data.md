### Anatomy of a Spark job run

- A Spark job is a unit of execution that corresponds to an action on a Spark RDD, DataFrame or Dataset, such as `collect()`, `saveAsTextFile()` or `count()`.
- A Spark job consists of one or more stages, which are logical units of computation that depend on each other.
- A stage is a set of parallel tasks that perform the same operation on different partitions of the input data.
- A task is a unit of work that runs on a single executor and processes a single partition of the input data.
- A Spark application contains several components, such as the driver, the master, the cluster manager and the executors.
- The driver is the process that runs the main() method of the Spark application and creates the SparkContext object. It is responsible for submitting the Spark jobs to the cluster and coordinating the execution of the tasks.
- The master is the process that coordinates the allocation of resources and the scheduling of tasks across the cluster. It communicates with the cluster manager and the executors.
- The cluster manager is the service that manages the worker nodes and the executors in the cluster. It can be a standalone service, a YARN service or a Mesos service.
- The executors are the processes that run on the worker nodes and execute the tasks assigned by the master. They store the intermediate and final results of the tasks in memory or disk.
- The Spark scheduler builds an execution graph (or DAG) for each Spark job and divides it into stages based on the data dependencies. It then assigns the tasks to the executors based on the data locality and the availability of resources.
- The Spark UI is a web interface that shows the details of the Spark application, such as the stages, the tasks, the executors, the storage and the environment. It can be accessed at http://driver-node:4040.