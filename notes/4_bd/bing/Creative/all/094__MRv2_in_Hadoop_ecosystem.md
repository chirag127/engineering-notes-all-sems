#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator)  .
- YARN is a resource management and scheduling layer that lies beneath the MapReduce layer and separates it from HDFS (Hadoop Distributed File System)   .
- MRv2 is also known as Hadoop 2, which is a major improvement over Hadoop 1 or MRv1, which had the following limitations   :
  - HDFS and MapReduce were tightly coupled, which means that non-batch applications could not run on Hadoop 1.
  - The JobTracker was responsible for creating and assigning tasks to DataNodes, which could become a bottleneck and a single point of failure when the cluster scaled out beyond 4,000 nodes.
  - The cluster's capacity was measured in MapReduce slots, which could lead to underutilization or overallocation of resources.
- MRv2 introduces the following features and benefits    :
  - YARN decouples HDFS and MapReduce, which enables other types of applications to run on Hadoop, such as streaming, interactive, graph, and machine learning.
  - YARN introduces the ResourceManager for each cluster, and the NodeManager for each DataNode, which handle the resource allocation and monitoring for the applications.
  - YARN also introduces the ApplicationMaster for each job, which runs on a slave node and coordinates the tasks and resources for the job.
  - The cluster's capacity is measured in memory and CPU units, which allows for more efficient and flexible utilization of resources.
  - MRv2 supports high availability and scalability by allowing redundant NameNodes and federation of multiple NameSpaces.
  - MRv2 supports snapshots of the file system, which helps in disaster recovery and backup.
  - MRv2 provides backward compatibility of the old MapReduce APIs, which means that the existing MapReduce applications can run on the new framework without any modification. 
- A possible mnemonic to remember the difference between MRv1 and MRv2 is: MRv1 is **M**ore **R**estricted, MRv2 is **M**ore **R**esourceful.