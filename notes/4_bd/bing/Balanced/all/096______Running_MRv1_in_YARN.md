#### Running MRv1 in YARN

- MRv1 stands for MapReduce version 1, which is the original version of the MapReduce framework for distributed data processing in Hadoop.
- YARN stands for Yet Another Resource Negotiator, which is the newer version of the MapReduce framework, also known as MRv2.
- YARN separates the resource management and scheduling functions from the data processing logic, allowing for more flexibility and scalability in running different types of applications on Hadoop.
- MRv1 applications can run on YARN with some minor changes, such as using the `yarn` command instead of the `hadoop` command, and specifying the `mapreduce.framework.name` property as `yarn` in the configuration file.
- MRv1 applications can be monitored on the ResourceManager web interface, which shows the cluster metrics, applications, and nodes. The JobHistoryServer web interface can also be used to view the details of completed MRv1 jobs on YARN.
- MRv1 applications can use different schedulers on YARN, such as FIFO, Fair, or Capacity, to allocate resources based on different policies and priorities.