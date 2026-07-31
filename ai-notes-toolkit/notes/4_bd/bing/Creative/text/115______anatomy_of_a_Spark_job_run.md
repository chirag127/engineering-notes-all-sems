#### Anatomy of a Spark job run

- A Spark job is a parallel computation that runs on a cluster of nodes and consists of one or more stages.
- A stage is a set of tasks that perform the same computation on different partitions of the input data.
- A task is a unit of work that runs on a single executor and processes a single partition of the input data.
- An executor is a process that runs on a worker node and executes tasks assigned by the driver.
- A driver is the process that coordinates the execution of a Spark job and runs the user-defined main function.
- A Spark job run follows these steps:

  1. The user submits a Spark application to the cluster manager, which allocates resources and launches the driver and executors.
  2. The driver converts the user-defined logic into a logical plan, which is then optimized and translated into a physical plan of stages and tasks.
  3. The driver sends the tasks to the executors and monitors their progress and status.
  4. The executors run the tasks and communicate with each other to exchange data if needed.
  5. The executors send the results and metrics back to the driver, which collects and aggregates them.
  6. The driver terminates the executors and releases the resources when the job is finished.