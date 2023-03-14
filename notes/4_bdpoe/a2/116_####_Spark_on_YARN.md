 Here is the content in markdown format for the topic #### Spark on YARN:

#### Spark on YARN

- Spark can run on YARN, a widely deployed resource manager and scheduler. Running Spark on YARN has following advantages:
- YARN isolates resources for each application and enforces limits and security.
- Spark can share a cluster with other data processing frameworks and YARN applications.
- YARN's pluggable scheduler allows using diverse scheduling strategies such as capacity and fair sharing.

To run Spark on YARN:

1. Configure YARN by setting YARN properties in yarn-site.xml.
2. Copy spark-assembly-x.x.x.jar and spark-yarn-x.x.x.jar to nodes.
3. Launch a YARN Application for Spark using yarn-client or yarn-cluster mode:

yarn-client mode:
$ ${SPARK_HOME}/bin/spark-submit \
  --master yarn \
  --deploy-mode client \
  --executor-memory <executor-memory> \
  --driver-memory <driver-memory> \
  <application-jar>

yarn-cluster mode:
$ ${SPARK_HOME}/bin/spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --executor-memory <executor-memory> \
  --driver-memory <driver-memory> \
  <application-jar>

Advantages of Spark on YARN:
- YARN manages resource allocation and isolation for applications.
- YARN's pluggable scheduler allows using diverse strategies like capacity and fair sharing.
- Spark applications share clusters with other data processing frameworks and YARN applications.

Disadvantages of Spark on YARN:
- Complex setup and dependency management.
- Heterogeneous clusters require separately building and distributing applications for each resource manager.

Hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.