#### Running MRv1 in YARN

- MRv1 is the first version of MapReduce, a programming model for processing large-scale data sets in parallel.
- YARN is the second version of MapReduce, also known as MRv2, which separates the resource management and scheduling functions from the data processing component.
- YARN allows running MRv1 applications on a YARN cluster, as well as other types of applications such as Spark, Hive, and Pig.
- To run MRv1 applications on YARN, the following steps are required:
  - Configure the YARN cluster with the appropriate settings for MRv1, such as the map and reduce memory limits, the number of map and reduce slots per node, and the job history server address.
  - Use the `yarn` command instead of the `hadoop` command to submit MRv1 applications to the YARN cluster. For example, `yarn jar hadoop-mapreduce-examples-2.x.x.jar wordcount input output`.
  - Monitor the MRv1 applications using the ResourceManager web interface, which shows the cluster metrics, the list of applications, and the nodes associated with the cluster. The ResourceManager web interface can be accessed at `http://<ResourceManager-Host>:8088`.
  - Alternatively, use the `yarn` command to view the application status, logs, and history. For example, `yarn application -list`, `yarn logs -applicationId <application_id>`, and `yarn history -applicationId <application_id>`.
- Running MRv1 applications on YARN has some advantages and disadvantages compared to running them on MRv1. Some of them are:
  - Advantages:
    - YARN provides better resource utilization and scalability than MRv1, as it can dynamically allocate resources to different applications based on their needs and priorities.
    - YARN supports running multiple types of applications on the same cluster, which enables more flexibility and interoperability for data processing and analysis.
    - YARN has a more fault-tolerant and high-availability architecture than MRv1, as it eliminates the single point of failure of the JobTracker and uses ZooKeeper for leader election and coordination.
  - Disadvantages:
    - YARN requires more configuration and tuning than MRv1, as it has more parameters and options to set for the ResourceManager, the NodeManager, and the ApplicationMaster.
    - YARN has a higher learning curve than MRv1, as it introduces new concepts and components such as the ApplicationMaster, the Container, and the Timeline Server.
    - YARN may not be fully compatible with some MRv1 applications, especially those that use custom input and output formats, combiners, counters, or distributed cache. Some of these features may need to be modified or rewritten to work on YARN.