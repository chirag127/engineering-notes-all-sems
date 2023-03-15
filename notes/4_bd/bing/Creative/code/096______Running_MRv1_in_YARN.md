#### Running MRv1 in YARN

- MRv1 stands for MapReduce version 1, which is a distributed computing framework for processing large-scale data sets in parallel.
- YARN stands for Yet Another Resource Negotiator, which is a cluster resource management system that allows multiple applications to run on the same cluster of nodes.
- To run MRv1 in YARN, the following steps are required:

  - Configure the YARN properties in the yarn-site.xml file, such as the resource manager address, the node manager address, the scheduler type, the memory and CPU allocation for containers, etc.
  - Configure the MRv1 properties in the mapred-site.xml file, such as the mapreduce.framework.name, the mapreduce.jobhistory.address, the mapreduce.jobhistory.webapp.address, the mapreduce.jobtracker.address, etc.
  - Start the YARN daemons, such as the resource manager, the node manager, and the timeline server, on the appropriate nodes using the start-yarn.sh script.
  - Start the MRv1 daemons, such as the job tracker and the task tracker, on the appropriate nodes using the start-mapred.sh script.
  - Submit the MRv1 jobs using the hadoop jar command, specifying the input and output paths, the mapper and reducer classes, the combiner class, the partitioner class, the number of map and reduce tasks, etc.
  - Monitor the MRv1 jobs using the web UIs of the resource manager, the node manager, the job tracker, the task tracker, and the job history server, or using the hadoop job command.