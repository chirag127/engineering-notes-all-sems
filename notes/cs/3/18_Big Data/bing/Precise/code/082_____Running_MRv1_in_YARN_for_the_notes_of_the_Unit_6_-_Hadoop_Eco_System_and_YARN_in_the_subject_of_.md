### Running MRv1 in YARN

1. MRv1, also known as Hadoop MapReduce version 1, is a framework for processing large data sets in a distributed computing environment.
2. YARN, or Yet Another Resource Negotiator, is a resource management layer in Hadoop that allows multiple data processing engines to share resources in a cluster.
3. To run MRv1 in YARN, the MRv1 job must be submitted to the YARN resource manager, which will allocate resources and schedule the job for execution.
4. The YARN resource manager will launch application masters for the MRv1 job, which will then request containers from the resource manager to run the map and reduce tasks.
5. The map and reduce tasks will be executed in the containers, and the results will be written to HDFS.
6. Once the MRv1 job is completed, the application master will release the resources back to the resource manager.
