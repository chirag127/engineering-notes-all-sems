#### Running MRv1 in YARN

- MRv1, also known as MapReduce version 1, is a framework for processing large data sets in a distributed computing environment.
- YARN, or Yet Another Resource Negotiator, is a resource management layer in Hadoop that allows multiple data processing engines to share resources in a cluster.
- To run MRv1 in YARN, the following steps can be followed:
  1. Install and configure Hadoop with YARN.
  2. Set the `mapreduce.framework.name` property to `yarn` in the `mapred-site.xml` configuration file.
  3. Submit the MapReduce job using the `hadoop jar` command, specifying the input and output paths, as well as any other necessary job parameters.
  4. Monitor the progress of the job using the YARN Resource Manager web UI or the `yarn application` command.
- Running MRv1 in YARN allows for more efficient resource utilization and better scalability compared to running MRv1 in standalone mode.