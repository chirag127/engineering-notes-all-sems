# Map Reduce Framework and Basics

MapReduce is a programming model or pattern within the Hadoop framework that is used to access big data stored in the Hadoop File System (HDFS). It allows us to perform distributed and parallel processing on large data sets in a distributed environment.

The MapReduce framework consists of the following components:

- A single master node that runs the **ResourceManager** and the **JobTracker**. The ResourceManager is responsible for allocating resources to the applications and managing the cluster nodes. The JobTracker is responsible for scheduling the jobs' component tasks on the slave nodes, monitoring them and re-executing the failed tasks. 
- Multiple slave nodes that run the **NodeManager** and the **TaskTracker**. The NodeManager is responsible for launching and monitoring the containers that run the applications. The TaskTracker is responsible for executing the tasks as directed by the JobTracker. 
- An **MRAppMaster** per application that runs on a container and coordinates the execution of the map and reduce tasks.

The MapReduce framework operates on the principle of **data locality**, which means that it tries to move the computation to the data, rather than the other way around. This reduces the network traffic and improves the performance.

The MapReduce framework consists of two distinct phases: **Map** and **Reduce**. As the name MapReduce suggests, the reducer phase takes place after the mapper phase has been completed.

- The **Map** phase takes the input data, which is split into smaller blocks, and applies a user-defined map function to each block. The map function processes the input key-value pairs and produces another set of intermediate key-value pairs as output. The output of the map phase is then shuffled and sorted by the framework before passing them on to the reduce phase. 
- The **Reduce** phase takes the output of the map phase, which is grouped by the key, and applies a user-defined reduce function to each group. The reduce function aggregates the values associated with the same key and produces a final output key-value pair. The output of the reduce phase is then written to the HDFS. 

There are two intermediate steps between the Map and Reduce phases: **Combine** and **Partition**.

- The **Combine** step is an optional step that can be used to reduce the amount of data transferred between the map and reduce phases. It applies a user-defined combine function to the output of the map phase on the same node, which performs a partial aggregation of the values with the same key. The output of the combine step is then shuffled and sorted by the framework.
- The **Partition** step is a mandatory step that determines how the output of the map phase is distributed among the reducers. It applies a user-defined partition function to the output key of the map phase, which returns a partition number for each key. The partition number decides which reducer will receive the key-value pair. The default partition function is a hash function, but it can be customized by the user.

The following diagram illustrates the MapReduce framework and its phases:

![MapReduce Framework](https://www.talend.com/wp-content/uploads/2019/07/mapreduce-framework.png)