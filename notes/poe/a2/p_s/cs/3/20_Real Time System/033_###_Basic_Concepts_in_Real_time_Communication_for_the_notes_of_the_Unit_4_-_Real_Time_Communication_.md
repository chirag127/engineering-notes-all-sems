 Here is the content in markdown format for the given topic:

#### Cluster Specification in Hadoop Environment

- A Hadoop cluster consists of multiple machines that work together to store and process data using the Hadoop framework.
- The main components of a Hadoop cluster are:

1. NameNode: Responsible for storing metadata (data about the data) and for coordination between nodes in the cluster. typically only one per cluster.
2. DataNodes: Responsible for storing data in the Hadoop Distributed File System (HDFS). There are typically multiple DataNodes in a cluster.
3. JobTracker (in Hadoop 1): Responsible for distributing MapReduce jobs and tasks to TaskTrackers (in Hadoop 1). One per cluster.
4. TaskTrackers (in Hadoop 1): Responsible for executing MapReduce tasks as assigned by the JobTracker (in Hadoop 1). Multiple per cluster.
5. ResourceManager (in Hadoop 2+): Responsible for allocating resources (memory, CPU) to applications and scheduling applications' component tasks. One per cluster.
6. NodeManager (in Hadoop 2+): Works with the ResourceManager to launch and manage containerized application tasks and monitor their resource usage. Multiple per cluster.

- Other common components include:

1. Client: The machine where Hadoop commands are submitted to the cluster.
2. Secondary NameNode: Performs regular checkpoints of the namespace state from the primary NameNode. One per cluster.
3. Gateway: Provides a single point of access/egress for a Hadoop cluster. One per cluster.

- The specification of a Hadoop cluster will depend on the use case and data to be processed and the number/size of machines used will depend on the scale of data and workload. Larger clusters provide more storage and processing power at the cost of increased complexity and resource utilization.

- Advantages: Scalable, Fault-tolerant, Cost-effective
- Disadvantages: Complex to setup and manage, Requires many machines
- Applications: Big data analysis, processing logs, machine learning, etc.