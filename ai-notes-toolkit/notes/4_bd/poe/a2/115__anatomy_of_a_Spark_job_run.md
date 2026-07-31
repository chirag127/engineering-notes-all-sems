 Here is the content in formal tone with points and without emojis or external links:

#### Anatomy of a Spark job run

1. Client program: The client program is the application that triggers the Spark job. It includes the app logic and transformations on the input data.
2. Cluster manager: The cluster manager is the service that allocates resources to the application. It tracks resource availability on each node in the cluster and schedules tasks to run on the nodes.
3. Driver program: The driver program is the process that contains the main() function of the application and drives the overall application execution.
4. Executors: Executors are worker processes launched by the cluster manager to run the tasks. They receive tasks from the driver and report task status/results back to the driver.
5. Tasks: Tasks are the smallest unit of work that gets scheduled in a Spark application. They get dispatched to the executors by the driver for execution.

The steps in a Spark job run are:

1. The client program defines the transformations and actions and submits the application to the cluster manager
2. The cluster manager launches the driver program
3. The driver requests executors from the cluster manager
4. The cluster manager launches executors on the cluster nodes
5. The driver schedules tasks to the executors
6. The executors run the tasks and send results back to the driver
7. The driver aggregates the results and returns to the client program