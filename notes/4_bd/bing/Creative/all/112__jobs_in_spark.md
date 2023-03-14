#### Jobs in Spark

- A job in Spark is a parallel computation that consists of multiple tasks that run on different nodes of a cluster.
- A job is created when an action is invoked on an RDD or a DataFrame, such as count, collect, save, etc.
- A job can have one or more stages, depending on the number of shuffle operations required to complete the job.
- A stage is a set of tasks that can run in parallel, without data shuffling between them.
- A task is a unit of work that is sent to an executor to process a partition of data.
- A task can be either a map task or a reduce task, depending on the type of operation it performs on the data.
- A map task applies a transformation function to each record in the input partition and produces an output partition.
- A reduce task aggregates the records from multiple input partitions and produces a single output partition.
- A task can also have dependencies on other tasks, such as narrow dependencies or wide dependencies.
- A narrow dependency is a one-to-one or one-to-many relationship between partitions of the parent and child RDDs, such as map, filter, etc.
- A wide dependency is a many-to-many relationship between partitions of the parent and child RDDs, such as reduceByKey, join, etc.
- A wide dependency requires a shuffle operation to redistribute the data across the cluster, which creates a new stage in the job.
- A job can be submitted to Spark using the SparkSession or the SparkContext object, which act as the entry point to the Spark application.
- A job can be monitored and managed using the Spark UI, which provides information about the stages, tasks, executors, and resources of the job.
- A job can also be configured using various parameters, such as the number of partitions, the number of cores, the memory allocation, the serialization format, the compression codec, the scheduler mode, etc.

Some mnemonics and learning tricks for the jobs in Spark are:

- To remember the difference between a job and a stage, think of a job as a journey and a stage as a stop.
- To remember the difference between a map task and a reduce task, think of a map task as a mapper and a reduce task as a reducer.
- To remember the difference between a narrow dependency and a wide dependency, think of a narrow dependency as a narrow road and a wide dependency as a wide road.
- To remember the difference between a SparkSession and a SparkContext, think of a SparkSession as a session and a SparkContext as a context.