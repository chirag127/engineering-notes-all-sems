# Stages and Tasks for the Notes of the Unit 9 - Spark

Spark is a distributed computing framework that allows processing large-scale data in parallel using clusters of machines. Spark applications consist of the following components:

- Application: A Spark application is a user program that runs on the Spark cluster. It can be written in Scala, Python, Java, or R. A Spark application can have one or more Spark jobs.
- Job: A Spark job is a parallel computation of tasks that is triggered by an action operation, such as `count()`, `save()`, or `collect()`. Each action operation will create one Spark job. Each Spark job will be converted to a DAG (Directed Acyclic Graph) which includes one or more stages.
- Stage: A Spark stage is a smaller set of tasks that depend on each other. Stages are created for each job based on shuffle boundaries, i.e. what operations can be performed serially or in parallel. Not all Spark operations or actions can happen in a single stage without data shuffling, thus they may be divided into multiple stages. For example, a `map()` operation can be done in parallel on different partitions of the input data, but a `reduceByKey()` operation requires shuffling the data by key before applying the reduce function. Therefore, a Spark job that consists of a `map()` followed by a `reduceByKey()` will have two stages: one for the `map()` and one for the `reduceByKey()`.
- Task: A Spark task is a unit of work that is executed by an executor on a worker node. A task corresponds to a partition of the input data and a set of transformations to apply on it. A task can also produce intermediate data that is stored in memory or disk for the next stage. A task can fail due to various reasons, such as network errors, memory errors, or hardware failures. Spark can automatically retry failed tasks on different executors or nodes.

The following diagram illustrates the relationship between application, job, stage, and task in Spark:

![Spark Components](https://kontext.tech/images/spark/spark-basics-application-driver-executor-job-stage-and-task-walkthrough/spark-basics-application-driver-executor-job-stage-and-task-walkthrough-1.png)

Source: [Spark Basics - Application, Driver, Executor, Job, Stage and Task Walkthrough](https://kontext.tech/article/1166/spark-basics-application-driver-executor-job-stage-and-task-walkthrough) 

Some key points to remember about stages and tasks in Spark are:

- Spark uses a DAG scheduler to optimize the execution plan of a job based on the dependencies and transformations of the RDDs.
- Spark uses a task scheduler to assign tasks to executors based on the availability of resources and data locality.
- Spark stages are divided into two types: narrow and wide. Narrow stages are those that do not require data shuffling, such as `map()`, `filter()`, or `union()`. Wide stages are those that require data shuffling, such as `groupBy()`, `join()`, or `sortBy()`. Wide stages are also called shuffle stages, and they mark the boundaries of a job.
- Spark tasks are executed in parallel within a stage, but stages are executed sequentially within a job. The number of tasks in a stage is equal to the number of partitions of the RDD that is being processed in that stage. The number of tasks in a job is equal to the sum of the tasks in all the stages of that job.
- Spark tasks can be monitored and debugged using the Spark UI, which shows the status, duration, input/output size, shuffle read/write size, and errors of each task in each stage of each job. The Spark UI can also show the DAG visualization of each job and the event timeline of each stage.