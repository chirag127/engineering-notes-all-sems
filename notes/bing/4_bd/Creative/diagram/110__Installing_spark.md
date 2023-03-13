Installing spark depends on the operating system and the mode of deployment. Spark can run on Windows, Linux, or Mac OS, and can be deployed in standalone mode, on a cluster, or in the cloud. The basic steps for installing spark are:

- Verify the Java installation on the system. Spark requires Java 8 or higher. You can check the Java version by running the command `java -version` in the terminal.
- Install Scala, the programming language used by Spark. You can download Scala from https://www.scala-lang.org/download/ or use a package manager such as Homebrew or apt-get.
- Download the latest version of Apache Spark from https://spark.apache.org/downloads.html. Choose the package type, the Spark version, and the Hadoop version according to your needs.
- Extract the downloaded file to the desired location. For example, you can create a folder named Spark in the root of your C: drive and extract the file there.
- Set the environment variables for Spark and Java. You need to add the paths of Spark and Java to the system PATH variable, and also set the SPARK_HOME and JAVA_HOME variables. You can do this by editing the .bashrc file on Linux or Mac OS, or the system properties on Windows.
- Verify the Spark installation by running the command `spark-shell` in the terminal. This will launch the interactive Spark shell, where you can run Spark commands and queries.

The following diagram illustrates the basic architecture of a Spark installation in standalone mode:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Master       |       |    Worker 1     |       |    Worker 2     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| spark://master  |       | spark://worker1 |       | spark://worker2 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Driver       |       |    Executor     |       |    Executor     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Application  |       |    Task 1       |       |    Task 2       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The master node is responsible for coordinating the cluster and scheduling the tasks. The worker nodes are responsible for running the tasks assigned by the master. The driver node is responsible for running the application code and creating the Spark session. The executor nodes are responsible for running the tasks in parallel. The tasks are the units of work that perform the computation on the data.