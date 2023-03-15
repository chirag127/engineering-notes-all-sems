### Hadoop Eco System and YARN

Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers. Hadoop consists of several components, such as HDFS, MapReduce, Hive, Pig, HBase, etc. These components form the Hadoop ecosystem, which provides various tools and services for data ingestion, storage, processing, analysis, and management.

YARN stands for Yet Another Resource Negotiator. It is a sub-project of Hadoop that provides a platform for resource management and job scheduling. YARN was introduced in Hadoop 2.0 to overcome the limitations of MapReduce, such as scalability, efficiency, and flexibility. YARN allows multiple applications to run on the same Hadoop cluster, using different processing frameworks, such as Spark, Flink, Storm, etc.

The architecture of YARN consists of two main components: the ResourceManager (RM) and the ApplicationMaster (AM). The RM is responsible for allocating and managing the resources across the cluster, such as memory, CPU, disk, network, etc. The AM is responsible for coordinating and monitoring the execution of a specific application, such as a MapReduce job or a Spark application. The AM communicates with the RM to request and release resources, and with the NodeManagers (NMs) to launch and monitor the containers that run the application tasks.

The following code block shows an example of how to run a Spark application on YARN:

```bash
# Set the HADOOP_CONF_DIR environment variable to point to the Hadoop configuration directory
export HADOOP_CONF_DIR=/etc/hadoop/conf

# Submit the Spark application using the spark-submit script
spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master yarn \
  --deploy-mode cluster \
  --executor-memory 1G \
  --num-executors 3 \
  /path/to/spark-examples.jar \
  10
```

The above code will submit a Spark application that calculates the value of pi using 10 partitions. The application will run on YARN in cluster mode, meaning that the driver program will run on a container allocated by the RM. The application will request 3 executors, each with 1 GB of memory, to run the tasks. The spark-submit script will automatically upload the application jar and the Hadoop configuration files to the HDFS, and launch the AM on a container. The AM will then request and launch the executor containers, and coordinate the execution of the tasks. The output of the application will be written to the standard output of the driver container, which can be accessed using the YARN logs command.