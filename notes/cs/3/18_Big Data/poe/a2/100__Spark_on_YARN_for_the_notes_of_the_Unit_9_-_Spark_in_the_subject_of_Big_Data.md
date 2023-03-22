 Here is the content in markdown format without any emojis or external links and being formal:

### Spark on YARN for the notes of the Unit 9 - Spark in the subject of Big Data

1. YARN is a cluster management technology for Hadoop. It can manage computing and storage resources in clusters and allocates resources dynamically to various applications.
2. Spark can run on YARN, allowing us to use the distributed computing capabilities of YARN to scale our Spark applications.
3. When we run Spark on YARN, YARN takes care of allocating and managing resources for our application across the cluster. It also ensures that our application has the resources it needs and can scale the application to use more or fewer resources as needed.
4. To run Spark on YARN, we package our application into a YARN application and submit it to YARN. YARN then allocates containers for our application and starts the Spark application.
5. Key benefits of running Spark on YARN are:
    - We can use the storage already available through HDFS for our data.
    - We can utilize the computing resources managed by YARN to scale our Spark processing.
    - We can run multiple processing frameworks on YARN and not be limited to just Spark. Other frameworks like MapReduce and Storm can also utilize the cluster.
6. Some key configurations when running Spark on YARN:
    - spark.yarn.am.memory: Amount of memory to allocate for the Spark Application Master process.
    - spark.yarn.executor.memory: Amount of memory to allocate for each executor.
    - spark.yarn.executor.cores: Number of cores to allocate for each executor.