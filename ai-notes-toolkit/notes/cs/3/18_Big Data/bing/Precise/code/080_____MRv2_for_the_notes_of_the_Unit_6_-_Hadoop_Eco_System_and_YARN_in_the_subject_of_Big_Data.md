### MRv2

MRv2, also known as YARN (Yet Another Resource Negotiator), is the second generation of the MapReduce framework for processing large data sets with a parallel, distributed algorithm on a cluster. It is a part of the Hadoop ecosystem and was introduced in Hadoop 2.0.

Here are some key points about MRv2:

1. MRv2 separates the resource management and job scheduling/monitoring functions into separate daemons. The idea is to have a global ResourceManager (RM) and per-application ApplicationMaster (AM).
2. The ResourceManager and per-node slave, the NodeManager (NM), form the data-computation framework.
3. The ResourceManager is the ultimate authority that arbitrates resources among all the applications in the system.
4. The per-application ApplicationMaster is, in effect, a framework-specific library and is tasked with negotiating resources from the ResourceManager and working with the NodeManager(s) to execute and monitor the tasks.
5. MRv2 is designed to be more scalable, efficient, and flexible than the original MapReduce framework.
6. MRv2 allows for other data processing frameworks, such as Spark and Tez, to run on Hadoop, providing users with more options for processing their data.
