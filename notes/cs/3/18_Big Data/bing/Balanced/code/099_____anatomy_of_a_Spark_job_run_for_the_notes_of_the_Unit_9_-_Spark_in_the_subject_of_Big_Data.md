### Anatomy of a Spark job run

- A Spark job is a unit of execution that corresponds to an action on a Spark RDD, DataFrame or Dataset, such as `collect()`, `count()`, `saveAsTextFile()`, etc.
- A Spark job consists of one or more stages, which are logical units of computation that depend on each other.
- A stage is a set of parallel tasks that perform the same operation on different partitions of the input data.
- A task is a unit of work that runs on a single executor and processes a single partition of the input data.
- A Spark application contains several components, such as the driver, the master, the cluster manager and the executors.
- The driver is the process that runs the main() method of the Spark application and creates the SparkContext object. It is responsible for converting the user code into a logical plan and submitting the Spark jobs to the cluster manager.
- The master is the process that coordinates the allocation of resources and the scheduling of tasks across the cluster. It communicates with the cluster manager and the executors.
- The cluster manager is the service that manages the worker nodes and the executors in the cluster. It can be one of the supported cluster managers, such as YARN, Mesos, Kubernetes or standalone.
- The executors are the processes that run on the worker nodes and execute the tasks assigned by the master. They also store the intermediate and final results of the computation in memory or disk.
- The Spark scheduler is the component that builds the execution graph and divides the Spark job into stages and tasks. It also handles the dependencies, failures and retries of the tasks.
- The DAG (Directed Acyclic Graph) is the representation of the logical plan of the Spark job. It shows the dependencies and transformations of the RDDs, DataFrames or Datasets involved in the computation.
- The DAGScheduler is the component that converts the DAG into a physical plan and creates the stages and tasks for each Spark job. It also tracks the lineage and the shuffle dependencies of the RDDs, DataFrames or Datasets.
- The TaskScheduler is the component that assigns the tasks to the executors and monitors their status. It also handles the task failures and resubmissions.