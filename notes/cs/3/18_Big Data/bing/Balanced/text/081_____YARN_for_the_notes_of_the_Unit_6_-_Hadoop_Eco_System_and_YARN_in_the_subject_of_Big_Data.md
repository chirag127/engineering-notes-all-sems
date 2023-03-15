### YARN

- YARN stands for Yet Another Resource Negotiator. It is a component of Hadoop that manages the resources and scheduling of tasks in a Hadoop cluster.
- YARN was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0, which relied on a single JobTracker for resource management and job scheduling.
- YARN enables Hadoop to support multiple types of applications, such as MapReduce, Spark, Hive, etc., and to scale up to thousands of nodes and petabytes of data.
- The main components of YARN architecture are:

  - Client: It submits the application (a single job or a DAG of jobs) to the Resource Manager and monitors its progress.
  - Resource Manager: It is the master daemon of YARN that allocates resources (such as memory and CPU) to the applications and maintains the cluster health.
  - Scheduler: It is a part of the Resource Manager that performs scheduling based on the application priority, resource availability, and queue policies. It does not perform any monitoring or tracking of the application status. There are different types of schedulers, such as Capacity Scheduler, Fair Scheduler, etc.
  - Application Manager: It is a part of the Resource Manager that accepts the application submission, negotiates the first container for the application, and launches the Application Master.
  - Application Master: It is a per-application daemon that runs in a container and coordinates with the Resource Manager and the Node Managers to execute and monitor the tasks. It also handles the application failures and retries.
  - Node Manager: It is a slave daemon that runs on each node and manages the containers, monitors the resource usage, and reports to the Resource Manager.
  - Container: It is a unit of resource allocation that encapsulates a set of resources (such as memory, CPU, disk, network, etc.) and executes a task. A container can run on a physical or virtual machine.

- The following diagram illustrates the YARN architecture and the flow of an application:

![YARN architecture](https://www.geeksforgeeks.org/wp-content/uploads/YARN-Architecture.png)

- The key features of YARN are:

  - Scalability: YARN can scale up to thousands of nodes and petabytes of data, as the Resource Manager does not perform any task execution or monitoring, and the Application Masters run in parallel.
  - Compatibility: YARN supports the existing MapReduce applications as well as other types of applications, such as Spark, Hive, etc., by providing a common platform for resource management and scheduling.
  - Flexibility: YARN allows the developers to customize the Application Masters and the containers according to their application logic and resource requirements.
  - Efficiency: YARN optimizes the resource utilization and throughput by allocating the resources dynamically and fairly among the applications and the queues.
  - High Availability: YARN provides fault tolerance and reliability by supporting the recovery and restart of the Resource Manager and the Application Masters, and by using the ZooKeeper for leader election and coordination.