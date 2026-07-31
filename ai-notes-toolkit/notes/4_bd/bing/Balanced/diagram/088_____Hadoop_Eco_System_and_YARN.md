### Hadoop Eco System and YARN

- Hadoop is an open source framework that allows for distributed processing of large and complex data sets across clusters of computers.
- Hadoop consists of four main modules: Hadoop Common, Hadoop Distributed File System (HDFS), Hadoop MapReduce and Hadoop YARN.
- Hadoop Common provides the common utilities and libraries that are used by other Hadoop modules.
- HDFS is a distributed file system that stores data across multiple nodes in a cluster, providing high availability, fault tolerance and scalability.
- MapReduce is a programming model that enables parallel processing of large data sets using key-value pairs.
- YARN is a resource management layer that allocates and manages the resources and schedules the jobs in a Hadoop cluster.
- YARN stands for Yet Another Resource Negotiator. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as low resource utilization, lack of support for non-MapReduce applications and fixed job execution model.
- YARN separates the resource management and job scheduling functions from the data processing logic, allowing for multiple types of applications to run on the same Hadoop cluster, such as Spark, Hive, Pig, HBase, etc.
- YARN consists of two main components: a global ResourceManager (RM) and per-application ApplicationMaster (AM).
- The RM is responsible for managing the resources in the cluster, such as memory, CPU, disk and network bandwidth. It consists of two sub-components: a Scheduler and an ApplicationsManager.
- The Scheduler allocates resources to the applications based on various criteria, such as capacity, fairness, priority, etc. It supports multiple scheduling policies, such as FIFO, Capacity and Fair.
- The ApplicationsManager accepts the application submissions, negotiates the first container for the AM and monitors the AMs in the cluster.
- The AM is responsible for coordinating the execution of a specific application in the cluster, such as a MapReduce job or a Spark application. It requests resources from the RM, launches and monitors the containers that run the tasks and handles the failures and retries.
- A container is a unit of resource allocation in YARN. It represents a fixed amount of memory, CPU, disk and network bandwidth that can be used by a task.
- YARN also provides a NodeManager (NM) on each node in the cluster, which acts as a slave daemon that communicates with the RM and the AMs. It monitors the resource usage and health of the node, launches and kills the containers and reports the status of the containers to the RM and the AMs.
- YARN enables Hadoop to be more flexible, efficient and scalable, as it supports multiple types of applications, improves the resource utilization and allows for dynamic allocation and sharing of resources in the cluster.