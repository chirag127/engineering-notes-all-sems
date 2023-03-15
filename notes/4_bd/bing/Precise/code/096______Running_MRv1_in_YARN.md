#### Running MRv1 in YARN

- MRv1, also known as MapReduce version 1, is a framework for processing large data sets in parallel across a cluster of computers.
- YARN, or Yet Another Resource Negotiator, is a resource management layer in Hadoop that allows multiple data processing engines to share a common cluster.
- To run MRv1 in YARN, the following steps can be taken:
  1. Ensure that the Hadoop cluster is properly configured to use YARN as the resource manager.
  2. Set the `mapreduce.framework.name` property to `yarn` in the `mapred-site.xml` configuration file.
  3. Submit the MapReduce job to the cluster using the `hadoop jar` command, specifying the input and output paths, as well as any other necessary job configuration options.
  4. Monitor the progress of the job using the YARN web UI or the `yarn application` command.
- Running MRv1 in YARN allows for more efficient resource utilization and better scalability compared to running MRv1 in standalone mode.