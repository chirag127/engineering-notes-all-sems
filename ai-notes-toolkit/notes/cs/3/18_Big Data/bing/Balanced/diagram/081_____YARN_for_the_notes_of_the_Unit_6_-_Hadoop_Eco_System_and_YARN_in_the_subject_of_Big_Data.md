### YARN

YARN stands for Yet Another Resource Negotiator. It is a component of Hadoop that manages the resources and the execution of applications in a Hadoop cluster. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as scalability, resource utilization, and support for non-MapReduce applications.

The main components of YARN architecture are:

- **Client**: It submits the application (a single job or a DAG of jobs) to the Resource Manager and monitors its progress.
- **Resource Manager**: It is the master daemon of YARN that allocates and manages the resources among all the applications in the cluster. It consists of two sub-components: Scheduler and Application Manager.
- **Scheduler**: It performs scheduling based on the resource requests from the applications and the available resources in the cluster. It is a pure scheduler that does not perform any monitoring or tracking of the application status. It supports various scheduling policies, such as FIFO, Capacity, and Fair.
- **Application Manager**: It is responsible for accepting the application submission, negotiating the first container for the application, and launching the Application Master on that container.
- **Application Master**: It is a per-application framework-specific entity that negotiates and obtains the resources from the Resource Manager and works with the Node Managers to execute and monitor the tasks.
- **Node Manager**: It is the slave daemon of YARN that runs on each node in the cluster and manages the containers (units of resource allocation) on that node. It communicates with the Resource Manager to report the resource utilization and availability, and with the Application Master to launch and monitor the containers.

The following diagram illustrates the YARN architecture and the flow of an application execution:

![YARN architecture diagram](https://www.geeksforgeeks.org/wp-content/uploads/YARN-Architecture.png)

Some of the key features and benefits of YARN are:

- It decouples the programming model from the resource management, allowing multiple types of applications (such as MapReduce, Spark, Hive, etc.) to run on the same platform.
- It improves the resource utilization and efficiency of the cluster by dynamically allocating the resources based on the application needs and the cluster availability.
- It enhances the scalability and reliability of the cluster by distributing the responsibilities of the Job Tracker in Hadoop 1.0 to multiple components in YARN.
- It supports high availability and security features, such as ResourceManager failover, Kerberos authentication, and ACLs.