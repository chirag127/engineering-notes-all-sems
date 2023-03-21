

### Running MRv1 in YARN

In this unit, we will learn about running MapReduce version 1 (MRv1) in YARN. MRv1 is the classic MapReduce engine that was used in Hadoop versions 1.x and earlier. YARN, on the other hand, is the resource management layer introduced in Hadoop 2.x and later versions. 

Here are some points to keep in mind when running MRv1 in YARN:

- MRv1 is not the default MapReduce engine in YARN. By default, YARN uses MapReduce version 2 (MRv2), which is the newer and more efficient version of MapReduce. However, MRv1 can still be used in YARN if required.
- To run MRv1 in YARN, you need to set the property `mapreduce.framework.name` to `classic`. This can be done either in the `mapred-site.xml` configuration file or as a command-line argument when submitting the job.
- When running MRv1 in YARN, you can specify the maximum amount of memory and CPU cores that each map task and reduce task can use. This is done using the `mapreduce.{map|reduce}.memory.mb` and `mapreduce.{map|reduce}.cpu.vcores` properties, respectively. By default, each task is allocated 1GB of memory and 1 CPU core.
- MRv1 in YARN supports job priorities, just like in the classic Hadoop MapReduce. Jobs can be classified as either `HIGH`, `NORMAL`, or `LOW` priority. Higher priority jobs get more resources and are scheduled before lower priority jobs.
- MRv1 in YARN also supports job scheduling based on queues. Each queue has a certain amount of resources allocated to it, and jobs submitted to that queue can use only those resources. This allows for better resource management and sharing in multi-tenant environments.
- When using MRv1 in YARN, you can still use the familiar Hadoop command-line tools like `hadoop jar` and `hadoop fs` to submit and manage jobs. However, some of the options and syntax may be different from those used in MRv2.
- Finally, it's worth noting that MRv1 is considered to be a legacy technology and is not recommended for new applications. MRv2 is faster, more scalable, and has better support for new features like YARN services and timeline server. However, if you have existing MRv1 jobs that need to be migrated to YARN, or if you need to run MRv1-specific applications, it's good to know that it's still possible to do so in YARN.

That concludes our overview of running MRv1 in YARN. Remember to set the `mapreduce.framework.name` property to `classic`, and use the `mapreduce.{map|reduce}.memory.mb` and `mapreduce.{map|reduce}.cpu.vcores` properties to control resource allocation. Good luck with your MRv1 in YARN jobs!