# Unit 6 - Hadoop Eco System and YARN

### YARN

- YARN stands for Yet Another Resource Negotiator.
- It is one of the major components of Hadoop that allocates and manages the resources and keeps all things working as they should.
- YARN was initially named MapReduce 2 since it powered up the MapReduce of Hadoop 1.0 by addressing its downsides and enabling the Hadoop ecosystem to perform well for the modern challenges.
- The advent of YARN opened the Hadoop ecosystem to many possibilities. YARN was successful in overcoming the limitations of MapReduce v1 and providing a better, flexible, optimized, and efficient backbone for execution engines such as Spark, Storm, Solr, and Tez.
- YARN is the parallel processing framework for implementing distributed computing clusters that processes huge amounts of data over multiple compute nodes.
- Hadoop YARN allows for a compute job to be segmented into hundreds and thousands of tasks.
- The fundamental idea of YARN is to split up the functionalities of resource management and job scheduling/monitoring into separate daemons.
- The idea is to have a global ResourceManager (RM) and per-application ApplicationMaster (AM). An application is either a single job or a DAG of jobs.
- Apache Hadoop ecosystem refers to the various components of the Apache Hadoop software library; it includes open-source projects as well as a complete range of complementary tools.
- Some of the most well-known tools of the Hadoop ecosystem include HDFS, Hive, Pig, YARN, MapReduce, Spark, HBase, Oozie, Sqoop, Zookeeper, etc.