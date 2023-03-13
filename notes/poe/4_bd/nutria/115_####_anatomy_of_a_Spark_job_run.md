

#### Anatomy of a Spark Job Run

- A Spark job run consists of a **driver**, **executors**, and **cluster manager**. 
- The **driver** is the main program that runs the Spark job. It is responsible for creating the SparkContext, setting up the environment, and submitting tasks to the executors. 
- The **executors** are the programs that execute the tasks. They are responsible for running the user-defined code, managing resources, and returning the results to the driver. 
- The **cluster manager** is responsible for managing the resources in the cluster. It is responsible for scheduling tasks, allocating resources, and monitoring the health of the cluster. 
- A Spark job run consists of several phases: **scheduling**, **execution**, **shuffle**, and **cleanup**. 
- In the **scheduling** phase, the driver submits tasks to the cluster manager. The cluster manager then schedules the tasks to the executors. 
- In the **execution** phase, the executors execute the tasks. They read the data, perform the computation, and write the results. 
- In the **shuffle** phase, the executors exchange data between each other. This allows them to perform distributed computations. 
- In the **cleanup** phase, the driver collects the results from the executors and writes them to the output. 
- Finally, the driver shuts down the cluster manager and the executors. 

Mnemonic: **SEDS** - Scheduling, Execution, Shuffle, and Cleanup.