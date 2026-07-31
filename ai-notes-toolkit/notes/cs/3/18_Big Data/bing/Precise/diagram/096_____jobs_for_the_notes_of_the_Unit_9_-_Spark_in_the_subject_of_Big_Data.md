### Unit 9 - Spark

#### Jobs

- A job in Spark refers to a parallel computation consisting of multiple tasks that gets spawned in response to a Spark action.
- Jobs are divided into stages, which are a collection of tasks that can run in parallel.
- Each stage contains tasks that perform the same computation, but on different data partitions.
- Jobs are triggered by actions, such as `count()` or `collect()`, which return a value to the driver program or write data to an external storage system.
- Jobs are submitted to a cluster manager, which is responsible for allocating resources and scheduling tasks on the cluster.
- The Spark scheduler pipelines narrow transformations, which allows multiple stages to be computed together, reducing the need for data shuffling.
- The progress of a job can be monitored through the Spark web UI, which displays information about completed and active stages, as well as task progress and executor logs.
