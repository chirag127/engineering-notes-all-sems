#### Anatomy of a Spark job run

Spark application contains several components, all of which exist whether you are running Spark on a single machine or across a cluster of hundreds or thousands of nodes. The components of the Spark application are Driver, the Master, the Cluster Manager and the Executors .

- Driver: The Driver is the process that runs the main() method of the Spark application and creates the SparkContext. The Driver is responsible for planning, scheduling and executing the Spark jobs. The Driver also returns the results or status of the jobs to the client .
- Master: The Master is the process that coordinates the cluster of workers and allocates resources for the Spark jobs. The Master can be either a standalone process, a YARN ResourceManager, or a Mesos master .
- Cluster Manager: The Cluster Manager is the service that manages the cluster of workers and communicates with the Master. The Cluster Manager can be either a standalone service, a YARN NodeManager, or a Mesos slave .
- Executors: The Executors are the processes that run the tasks of the Spark jobs on the workers. The Executors communicate with the Driver and the Cluster Manager, and cache data in memory or disk for reuse .

A Spark job is a unit of execution that corresponds to an action on the Spark application. A Spark job consists of one or more stages, which are divided by shuffle boundaries. A shuffle boundary occurs when the data needs to be redistributed across the cluster, such as in a join or a groupBy operation .

A stage is a set of tasks that can be executed in parallel on the same data. A stage contains a number of partitions, which are the smallest units of data that can be processed by a task. A task is a unit of computation that runs on an Executor and applies a transformation or an action on a partition .

A DAG (Directed Acyclic Graph) is a representation of the Spark job that shows the dependencies between the stages and the tasks. The DAG is built by the Driver based on the transformations and actions in the Spark application. The DAG is used by the Driver to schedule and execute the Spark job .

The following diagram illustrates the anatomy of a Spark job run:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Driver     |      |     Master     |      | Cluster Manager|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      +---------------------->                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      +---------------------->                      +----------------+
      |                      |                      |                      |                |
      |                      |                      |                      |    Executor    |
      |                      |                      |                      |                |
      |                      |                      |                      +----------------+
      |                      |                      |                      |                |
      |                      |                      |                      |    Executor    |
      |                      |                      |                      |                |
      |                      |                      |                      +----------------+
      |                      |                      |                      |                |
      |                      |                      |                      |    Executor    |
      |                      |                      |                      |                |
      |                      |                      |                      +----------------+
      |                      |                      |                      |                |
      |                      |                      |                      |    Executor    |
      |                      |                      |                      |                |
      |                      |                      |                      +----------------+
      |                      |                      |                      |                |
      |                      |                      |                      |    Executor    |
      |                      |                      |                      |                |
      |                      |                      |                      +----------------+
      |                      |                      |                      |                |
      |                      |                      |                      |