### Installing spark for the notes of the Unit 9 - Spark in the subject of Big Data

- Spark is an open-source distributed computing framework that can process large-scale data sets using in-memory caching and parallel processing.
- Spark can run on various platforms, such as Hadoop, Mesos, Kubernetes, standalone, or in the cloud.
- To install Spark, you need to have Java 8 or later and Scala 2.12 or later installed on your system.
- You can download the latest version of Spark from https://spark.apache.org/downloads.html and extract the archive file to a desired location.
- You can set the environment variables `SPARK_HOME` and `PATH` to point to the Spark installation directory and its `bin` subdirectory, respectively.
- You can verify the installation by running `spark-shell` or `pyspark` in a terminal, which will launch an interactive Spark session.
- You can also run Spark applications using `spark-submit` command, which takes various options and arguments to specify the application details, such as the main class, the jar file, the input and output files, the configuration parameters, etc.
- You can configure Spark using `spark-defaults.conf`, `spark-env.sh`, and `log4j.properties` files in the `conf` subdirectory of the Spark installation directory, or by passing the configuration options to `spark-submit` or `spark-shell`.
- You can monitor the Spark applications using the web UI, which is available at http://localhost:4040 by default, or using the Spark history server, which can be started by running `sbin/start-history-server.sh` in the Spark installation directory.