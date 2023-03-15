#### Running MRv1 in YARN

- MRv1 is the first version of MapReduce, a programming model for processing large-scale data sets in parallel.
- YARN is the second version of MapReduce, also known as MRv2, which separates the resource management and scheduling functions from the data processing component.
- YARN allows running MRv1 applications on a YARN cluster, as well as other types of applications such as Spark, Hive, and Pig.
- To run MRv1 applications on YARN, the following steps are required:
  - Configure the YARN cluster with the appropriate settings for MRv1, such as the map and reduce memory allocation, the number of map and reduce slots per node, and the job history server address.
  - Use the `yarn` command in the Hadoop-YARN bin folder to submit the MRv1 application, instead of the `hadoop` command in the Hadoop-MapReduce bin folder.
  - Specify the `mapred.job.tracker` property as `yarn` in the MRv1 application configuration file, to indicate that the application should run on YARN.
  - Use the ResourceManager web interface to monitor the MRv1 application status, progress, and logs on the YARN cluster.
- Running MRv1 applications on YARN has some advantages, such as:
  - Improved resource utilization and scalability, as YARN can dynamically allocate resources to different applications based on their needs and priorities.
  - Increased compatibility and flexibility, as YARN can support multiple versions and frameworks of MapReduce, as well as other types of applications.
  - Reduced operational overhead, as YARN simplifies the cluster management and administration tasks.