#### Jobs in Spark

A job in Spark is a parallel computation of tasks. Each action operation will create one Spark job. Each Spark job will be converted to a DAG which includes one or more stages. A stage is a group of tasks that can be executed in parallel. A task is a unit of work that is sent to an executor. An executor is a process that runs on a worker node and executes tasks assigned by the driver. A driver is the process that coordinates the execution of a Spark application. A Spark application is a user program that uses the Spark API to perform some analysis or processing on data.

The following diagram illustrates the basic architecture of a Spark application and the relationship between jobs, stages and tasks:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Spark Driver  |       |   Spark Driver  |       |   Spark Driver  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Spark Context  |       |  Spark Context  |       |  Spark Context  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   DAG Scheduler |       |   DAG Scheduler |       |   DAG Scheduler |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Task Scheduler|       |   Task Scheduler|       |   Task Scheduler|
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Job 1 (DAG)  |       |    Job 2 (DAG)  |       |    Job 3 (DAG)  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Stage 1      |       |    Stage 2      |       |    Stage 3      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 1       |       |    Task 2       |       |    Task 3       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 4       |       |    Task 5       |       |    Task 6       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 7       |       |    Task 8       |       |    Task 9       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 10      |       |    Task 11      |       |    Task 12      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 11      |       |    Task 12      |       |    Task 13      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 12      |       |    Task 13      |       |    Task 14      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 13      |       |    Task 14      |       |    Task 15      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Task 14      |       |    Task 15      |