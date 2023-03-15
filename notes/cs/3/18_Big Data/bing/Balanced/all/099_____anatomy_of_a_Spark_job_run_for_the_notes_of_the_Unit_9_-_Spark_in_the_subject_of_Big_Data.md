# Anatomy of a Spark job run

- A Spark job is a unit of execution that corresponds to an action on a Spark RDD, DataFrame or Dataset, such as `collect()`, `count()`, `saveAsTextFile()`, etc.
- A Spark job consists of one or more stages, which are logical units of computation that depend on each other.
- A stage consists of one or more tasks, which are the smallest units of execution that run on a single executor JVM and process a partition of data.
- A Spark application contains several components, such as the driver, the master, the cluster manager and the executors, which interact with each other to run a Spark job.
- The driver is the process that runs the main() method of the Spark application and creates the SparkContext object. It is responsible for converting the user code into a logical plan, optimizing it, and generating a physical plan that consists of stages and tasks. It also coordinates the execution of tasks on the executors and collects the results.
- The master is the process that acts as the cluster manager for Spark standalone mode. It allocates resources to applications and assigns tasks to executors. It also monitors the status of the applications and the executors.
- The cluster manager is the service that manages the resources and the scheduling of tasks on the cluster. It can be Spark standalone, YARN, Mesos or Kubernetes, depending on the deployment mode of the Spark application.
- The executors are the processes that run on the worker nodes and execute the tasks assigned by the driver or the master. They also store the data in memory or disk, and communicate with the driver and other executors.
- The following diagram illustrates the anatomy of a Spark job run:

![Anatomy of a Spark job run](https://miro.medium.com/max/1400/1*4Ls1f7wZ1n0Z8zY0YQ2kCg.png)

- Source: [Anatomy of a Spark Application — in a nutshell](https://medium.com/@meenakshisundaramsekar/anatomy-of-a-spark-application-in-a-nutshell-2e542d5f334e)