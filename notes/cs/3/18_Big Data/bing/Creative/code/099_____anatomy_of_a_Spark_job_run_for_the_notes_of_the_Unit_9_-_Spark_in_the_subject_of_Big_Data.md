### Anatomy of a Spark job run

A Spark job is a unit of execution that corresponds to an action on a Spark RDD, DataFrame or Dataset. A Spark job consists of one or more stages, which are divided into tasks that run in parallel on the cluster nodes. A Spark job is executed by a Spark application, which is a program that uses the Spark API to manipulate data and perform computations.

The main components of a Spark application are:

- **Driver**: The driver is the process that runs the main() method of the Spark application and creates the SparkSession object. The driver coordinates the execution of the Spark job and communicates with the cluster manager and the executors.
- **Master**: The master is the process that runs on a designated node in the cluster and acts as the leader of the cluster. The master is responsible for resource allocation and scheduling of the Spark jobs. The master can be either a standalone process, a Mesos master, a YARN resource manager, or a Kubernetes API server.
- **Cluster Manager**: The cluster manager is the service that manages the worker nodes in the cluster and allocates resources to the Spark applications. The cluster manager can be either a standalone service, a Mesos cluster, a YARN cluster, or a Kubernetes cluster.
- **Executors**: The executors are the processes that run on the worker nodes and execute the tasks assigned by the driver. The executors store the data partitions in memory or disk and perform the computations on them. The executors communicate with the driver and the master through the Spark RPC framework.

The anatomy of a Spark job run can be illustrated by the following diagram:

```text
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Driver       |      |    Master       |      | Cluster Manager |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
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
       |                      |                      |
       |                      |                      |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Executor     |      |    Executor     |      |    Executor     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The steps involved in a Spark job run are:

1. The driver program invokes an action on a Spark RDD, DataFrame or Dataset, such as collect(), count(), saveAsTextFile(), etc.
2. The driver analyzes the lineage of the RDD, DataFrame or Dataset and builds a directed acyclic graph (DAG) of logical operators that represent the transformations and actions.
3. The driver splits the DAG into one or more stages, where each stage contains a set of operators that can be executed in parallel without data shuffling. The stages are divided by shuffle boundaries, which are operators that require data movement across the cluster, such as reduceByKey(), join(), groupBy(), etc.
4. The driver submits the stages to the master, which assigns them to the cluster manager. The cluster manager allocates resources to the stages and launches executors on the worker nodes.
5. The master sends the tasks to the executors, where each task corresponds to a partition of the input data and a subset of the operators in the stage. The executors fetch the data partitions from the driver or other executors, perform the computations on them, and store the intermediate or final results in memory or disk.
6. The executors send the task status and metrics to the driver and the master. The driver monitors the progress of the job and handles failures and retries. The master updates the cluster manager about the resource usage and availability.
7. The driver collects the final results from the executors and returns them to the user program or writes them to an external storage system.

Some references for further reading are:

-  What is the concept of application, job, stage and task in spark?
-  The Anatomy of a Spark Job - ignacio-alorre/Spark GitHub Wiki
-  The 4 Key Concepts in the