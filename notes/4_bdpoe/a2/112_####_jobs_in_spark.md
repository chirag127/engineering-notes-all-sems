 Here is the content in markdown format for the topic #### jobs in spark:

#### Jobs in Spark

The main jobs in Spark are:

1. Driver program: The driver program contains the main function and creates the SparkContext. The driver program splits up the work into tasks and coordinates them.

Mnemonic: The driver drives the Spark application.

2. Cluster manager: The cluster manager is responsible for allocating resources to the application. It launches executors on the slave nodes for the application.

3. Executors: The executors are responsible for running the individual tasks on the cluster. They fetch the data from the storage and perform the required operations and cache or write back the results.

Learning trick: Remember E for Executors, they execute the tasks.

4. Tasks: The actual computation units of the application are tasks. The driver splits up the work into tasks and assigns them to the executors.

Advantages:
- Fault tolerance: Spark has builtin fault tolerance by replicating the data across the cluster. If any node fails, the task is restarted on another node.
- Speed: Spark performs the tasks in memory hence taking advantage of the speed of RAM and cache. This makes it 100x faster than Hadoop for some applications.
- General purpose: Spark can be used for different types of applications like batch processing, streaming, MLlib, GraphX, etc.

Disadvantages:
- Resource management: Efficient resource management and allocation is difficult in Spark. Idle resources cannot be fully utilized.
- Data shuffling: The data shuffling process can become a bottleneck in Spark for some applications. The data has to be redistributed for every stage of an application.

Applications: Spark is used by many companies for real-time processing of large data. Some examples are:
- Recommendation systems by companies like Netflix, Uber, etc.
- Real-time analytics by companies like Conviva, Decibel Insight, etc.
- Graph processing by companies like Databricks, Neo4j, etc.