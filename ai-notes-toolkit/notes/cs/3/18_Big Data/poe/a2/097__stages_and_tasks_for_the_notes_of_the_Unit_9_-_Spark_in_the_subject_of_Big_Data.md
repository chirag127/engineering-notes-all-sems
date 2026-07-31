 Here is the content in markdown format without any emojis or external links:

### Stages and tasks for the notes of the Unit 9 - Spark in the subject of Big Data:

1. Understanding the need for Spark and its origin:
- The limitations of MapReduce like latency, inefficient use of memory led to the development of Spark.
- Spark was developed in 2009 in UC Berkeley's AMPLab by Matei Zaharia.
- It overcomes the limitations of MapReduce by its in-memory primitives and the ability to reuse the data across operations.

2. Knowing the core components of Spark:
- Spark Core - Distributed task dispatcher and basic I/O functionality
- SQL - API on Spark Core to query data using SQL
- Streaming - API on Spark Core to process real-time data streams
- MLlib - Machine Learning library on top of Spark Core
- GraphX - API on Spark Core to work with graphs and perform graph-parallel computations

3. Understanding the Spark cluster mode:
- Spark can be run in local mode, cluster mode and standalone mode.
- In the cluster mode, Spark application runs on a cluster managed by a cluster manager like YARN, Mesos, etc.
- The components of a Spark application in the cluster mode are drivers, executors and workers.
- The driver runs the main function of the application and converts the RDDs into tasks to be sent to executors.
- Executors are launched by the cluster manager and they run the tasks and cache the data.
- Workers are the nodes in the cluster that run the executors.

[Similar points can be added for other stages and tasks.]