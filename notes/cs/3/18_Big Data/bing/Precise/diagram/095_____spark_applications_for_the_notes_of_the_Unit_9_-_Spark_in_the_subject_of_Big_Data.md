### Unit 9 - Spark Applications

1. Spark Applications consist of a driver process and a set of executor processes.
2. The driver process runs the main function, sits on a node in the cluster, and is responsible for three things: maintaining information about the Spark Application; responding to a user’s program or input; and analyzing, distributing, and scheduling work across the executors.
3. Spark applications run as independent sets of processes on a cluster, coordinated by the driver program.
4. The driver consists of the user's program and a Spark session. The Spark session takes the user's program and divides it into smaller tasks that are handled by the executors.
5. A Spark application runs as independent processes, coordinated by the SparkSession object in the driver program. The resource or cluster manager assigns tasks to workers, one task per partition. A task applies its unit of work to the dataset in its partition and outputs a new partition dataset.
6. For running applications on a cluster, head to the deployment overview.
7. The SparkContext can connect to the cluster manager, which allocates resources across applications. The cluster manager is Apache Hadoop YARN.