### Running MRv1 in YARN

- MRv1 stands for MapReduce version 1, which is the original framework for processing large-scale data sets in parallel using the map and reduce functions.
- YARN stands for Yet Another Resource Negotiator, which is the resource management layer of Hadoop version 2, which separates the resource management and scheduling functions from the data processing logic.
- Running MRv1 in YARN means using the MapReduce framework to execute applications on top of the YARN cluster, which provides more scalability, flexibility and efficiency than the MRv1 architecture.
- To run MRv1 in YARN, the following steps are required:
  - Configure the YARN properties in the yarn-site.xml file, such as the ResourceManager address, the NodeManager address, the memory and CPU allocation for containers, etc.
  - Configure the MapReduce properties in the mapred-site.xml file, such as the framework name (yarn), the application master class, the shuffle handler class, etc.
  - Use the yarn command in the Hadoop-YARN bin folder to submit, monitor and kill applications, rather than the hadoop command in the Hadoop bin folder.
  - Use the web UI for ResourceManager at http://<ResourceManagerHost>:8088/ to view the cluster metrics, the list of applications and the nodes associated with the cluster.
  - Use the web UI for ApplicationMaster at http://<ApplicationMasterHost>:<ApplicationMasterPort>/ to view the details of a specific application, such as the job status, the progress, the counters, the tasks, etc.
- Running MRv1 in YARN has the following benefits:
  - It allows multiple applications to run concurrently on the same cluster, sharing the resources dynamically and fairly.
  - It enables the support for other types of applications besides MapReduce, such as Spark, Hive, Pig, etc.
  - It improves the fault tolerance and availability of the cluster, by having a separate ResourceManager and ApplicationMaster for each application, and by supporting the recovery of failed applications and containers.
  - It enhances the security and isolation of the cluster, by using Kerberos authentication and authorization, and by running the applications in separate containers with limited privileges.