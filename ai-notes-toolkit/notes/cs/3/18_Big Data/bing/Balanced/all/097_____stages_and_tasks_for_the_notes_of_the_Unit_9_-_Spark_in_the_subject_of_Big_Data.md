# Stages and Tasks in Spark

- Spark is a distributed computing framework that executes parallel tasks on a cluster of nodes.
- Spark divides a job into smaller units of work called stages and tasks, which are executed by different executor nodes in the cluster.
- A stage is a set of parallel tasks that operate on a subset of the data. The tasks within a stage are dependent on each other and are executed in a specific order, so the output of one task is used as input for the next task.
- A task is a unit of work that is assigned to an executor node. A task processes a single partition of the data and performs a series of transformations and actions on it.
- The number of tasks in a stage is equal to the number of partitions of the input data. The number of stages in a job depends on the shuffle boundaries, which are the points where the data needs to be redistributed across the cluster.
- Shuffle is an operation that transfers data between executor nodes, such as groupByKey, reduceByKey, join, etc. Shuffle creates a new stage and increases the network and disk I/O overhead.
- Spark uses a DAG (Directed Acyclic Graph) scheduler to create and optimize the execution plan for a job. The DAG scheduler analyzes the logical plan of the job and divides it into stages and tasks based on the shuffle boundaries and the available resources in the cluster.
- Spark also uses a task scheduler to assign tasks to executor nodes and monitor their progress. The task scheduler handles failures and retries of tasks and stages, and balances the load across the cluster.