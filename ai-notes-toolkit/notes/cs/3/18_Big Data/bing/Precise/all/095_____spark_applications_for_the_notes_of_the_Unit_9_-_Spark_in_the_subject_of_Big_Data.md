# Unit 9 - Spark

### Spark Applications

- Spark Applications consist of a driver process and a set of executor processes .
- The driver process runs your main () function, sits on a node in the cluster, and is responsible for three things: maintaining information about the Spark Application; responding to a user’s program or input; and analyzing, distributing, and scheduling work across the executors .
- Spark applications run as independent sets of processes on a cluster, coordinated by the driver program .
- The driver consists of your program, like a C# console app, and a Spark session. The Spark session takes your program and divides it into smaller tasks that are handled by the executors .
- A Spark application runs as independent processes, coordinated by the SparkSession object in the driver program. The resource or cluster manager assigns tasks to workers, one task per partition. A task applies its unit of work to the dataset in its partition and outputs a new partition dataset .
- For an in-depth overview of the API, start with the RDD programming guide and the SQL programming guide, or see “Programming Guides” menu for other components. For running applications on a cluster, head to the deployment overview .
- Spark applications run as independent sets of processes on a pool, coordinated by the SparkContext object in your main program, called the driver program. The SparkContext can connect to the cluster manager, which allocates resources across applications. The cluster manager is Apache Hadoop YARN .