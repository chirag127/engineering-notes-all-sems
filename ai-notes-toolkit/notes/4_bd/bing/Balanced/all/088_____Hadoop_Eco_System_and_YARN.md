### Hadoop Eco System and YARN

- Hadoop Eco System is a collection of open source projects and tools that work together to provide a scalable and reliable platform for big data processing and analysis.
- YARN (Yet Another Resource Negotiator) is a core component of Hadoop Eco System that manages the resources and scheduling of applications running on Hadoop clusters.
- YARN was introduced in Hadoop 2.0 as an improvement over the MapReduce framework of Hadoop 1.0, which had some limitations such as:
  - Fixed programming model (MapReduce) and data format (key-value pairs).
  - Single master node (JobTracker) that was responsible for both resource management and job scheduling, leading to scalability and reliability issues.
  - Inefficient utilization of cluster resources, as MapReduce jobs had to wait for the completion of previous jobs before starting.
- YARN architecture consists of two main components: ResourceManager (RM) and ApplicationMaster (AM).
  - ResourceManager is a global daemon that runs on a master node and oversees the allocation and management of resources (CPU, memory, disk, network) across the cluster.
  - ApplicationMaster is a per-application daemon that runs on a worker node and coordinates the execution and monitoring of tasks for a specific application.
  - An application can be a single job or a DAG (directed acyclic graph) of jobs, such as MapReduce, Spark, Hive, Pig, etc.
  - Each application submits a request to the ResourceManager for launching an ApplicationMaster, which then negotiates with the ResourceManager for the required resources and launches the tasks on the worker nodes.
  - The worker nodes run another daemon called NodeManager, which communicates with the ResourceManager and the ApplicationMaster, and manages the containers that run the tasks.
  - A container is a logical unit of resources (CPU, memory, disk, network) that is allocated to a task by the ResourceManager.
- YARN provides the following advantages over the MapReduce framework of Hadoop 1.0:
  - Flexible programming model and data format, as YARN supports various types of applications and frameworks besides MapReduce, such as Spark, Hive, Pig, etc.
  - Scalable and reliable resource management and job scheduling, as YARN separates these functionalities into different daemons (ResourceManager and ApplicationMaster) and allows multiple applications to run concurrently on the same cluster.
  - Efficient utilization of cluster resources, as YARN dynamically allocates and releases resources based on the demand and availability, and allows for resource sharing and preemption among applications.