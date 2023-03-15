# Unit 9 - Spark

### Jobs

- In the context of Apache Spark, a job is a unit of work that is distributed across the cluster for parallel processing.
- A job is triggered when an action is called on a resilient distributed dataset (RDD) or a DataFrame.
- A job is divided into stages, which are further divided into tasks.
- Each task is a unit of work that is sent to an executor for processing.
- The stages of a job are determined by the shuffle boundaries in the lineage of the RDD or DataFrame.
- The Spark scheduler is responsible for scheduling and managing the execution of jobs.
- The scheduler divides the job into stages and assigns tasks to available executors.
- The progress of a job can be monitored through the Spark web UI or through the SparkContext API.
- Jobs can be submitted to a Spark cluster through the Spark shell, through the `spark-submit` command, or through a programmatic API.
- Jobs can be cancelled or killed through the Spark web UI or through the SparkContext API.
