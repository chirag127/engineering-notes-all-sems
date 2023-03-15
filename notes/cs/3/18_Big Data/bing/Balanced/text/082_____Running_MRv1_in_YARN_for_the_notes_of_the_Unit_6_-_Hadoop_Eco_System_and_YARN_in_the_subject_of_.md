### Running MRv1 in YARN

- MRv1 stands for MapReduce version 1, which is the original framework for processing large-scale data sets in parallel using the map and reduce functions.
- YARN stands for Yet Another Resource Negotiator, which is the resource management layer of Hadoop version 2, which separates the resource management and scheduling functions from the data processing logic.
- Running MRv1 in YARN means using the MapReduce framework to execute applications on top of the YARN cluster, which provides more scalability, flexibility, and efficiency than the MRv1 architecture.
- To run MRv1 in YARN, the following steps are required:
  - Configure the YARN cluster with the appropriate settings for the ResourceManager, NodeManager, and ApplicationMaster services, as well as the mapred-site.xml and yarn-site.xml files.
  - Use the yarn command in the Hadoop-YARN bin folder to submit, monitor, and manage the MRv1 applications, rather than the hadoop command in the Hadoop bin folder.
  - Use the web UI for ResourceManager at http://<ResourceManagerHost>:8088/ to view the cluster metrics, list of applications, and nodes associated with the cluster.
  - Use the web UI for ApplicationMaster at http://<ApplicationMasterHost>:<ApplicationMasterPort>/ to view the details of each application, such as the job status, counters, tasks, and logs.
  - Use the web UI for HistoryServer at http://<HistoryServerHost>:19888/jobhistory/ to view the history of completed applications, such as the job summary, configuration, and statistics.