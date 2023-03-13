#### Running MRv1 in YARN

- MRv1 stands for MapReduce version 1, which is the original framework for processing large-scale data sets in parallel using the map and reduce functions.
- YARN stands for Yet Another Resource Negotiator, which is the resource management layer of Hadoop that allows multiple applications to run on the same cluster and share resources dynamically.
- Running MRv1 in YARN means using YARN as the execution engine for MRv1 applications, instead of the default JobTracker and TaskTracker daemons that MRv1 uses.
- To run MRv1 in YARN, the following steps are required:
  - Enable the MRv1 compatibility mode in YARN by setting the `mapreduce.framework.name` property to `yarn` in the `mapred-site.xml` file.
  - Use the `yarn` command in the Hadoop-YARN bin folder to submit MRv1 applications, instead of the `hadoop` command. For example, `yarn jar wordcount.jar WordCount input output`.
  - Monitor the MRv1 applications using the ResourceManager web interface, which shows the basic cluster metrics, list of applications, and nodes associated with the cluster. The ResourceManager web interface can be accessed at `http://<ResourceManager-Host>:8088`.
- Running MRv1 in YARN has the following advantages:
  - It allows MRv1 applications to coexist with other applications that use YARN, such as Spark, Hive, and Pig, and share the cluster resources efficiently.
  - It improves the scalability and reliability of MRv1 applications, as YARN can handle more concurrent jobs and recover from failures faster than the JobTracker and TaskTracker daemons.
  - It simplifies the migration from MRv1 to MRv2, which is the newer version of MapReduce that is designed to run on YARN natively. MRv2 has more features and performance improvements than MRv1, such as support for high-availability, speculative execution, and combiners.