### Running MRv1 in YARN

1. MRv1, also known as MapReduce version 1, is a framework for processing large data sets in a distributed computing environment.
2. YARN, or Yet Another Resource Negotiator, is a resource management layer in Hadoop that allows multiple data processing engines to share resources in a cluster.
3. To run MRv1 in YARN, the MRv1 application must be configured to use YARN as its resource manager.
4. This can be done by setting the `mapreduce.framework.name` property to `yarn` in the MRv1 configuration file.
5. Once this is done, the MRv1 application can be submitted to the YARN resource manager for execution.
6. The YARN resource manager will then allocate resources to the MRv1 application and manage its execution on the cluster.
7. This allows MRv1 to take advantage of the resource management capabilities of YARN, such as dynamic resource allocation and preemption.
8. Running MRv1 in YARN can improve the efficiency and scalability of MRv1 applications, allowing them to process larger data sets more quickly.
