### YARN

YARN stands for **Yet Another Resource Negotiator**. It is a component of Hadoop that was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0's MapReduce framework. YARN is responsible for managing and allocating resources to the applications running on a Hadoop cluster, and scheduling tasks to be executed on different nodes. YARN enables Hadoop to support a variety of data processing frameworks, such as Spark, Hive, Pig, etc., besides MapReduce.

The main components of YARN architecture are:

- **Client**: It submits the application (a single job or a DAG of jobs) to the Resource Manager and monitors its progress.
- **Resource Manager**: It is the master daemon of YARN that coordinates the allocation of resources (such as memory and CPU) among all the applications in the cluster. It consists of two sub-components:
  - **Scheduler**: It performs scheduling based on the resource requests from the applications and the available resources in the cluster. It is a pure scheduler that does not perform any monitoring or tracking of the application status. It supports various scheduling policies, such as FIFO, Fair, and Capacity.
  - **Application Manager**: It is responsible for accepting the application submission, negotiating the first container for the application, and launching the Application Master on that container. It also restarts the Application Master if it fails or expires.
- **Node Manager**: It is the slave daemon of YARN that runs on each node in the cluster and manages the containers (the units of resource allocation) on that node. It communicates with the Resource Manager to report the resource utilization and availability on the node, and with the Application Master to execute the tasks assigned to the containers.
- **Application Master**: It is a per-application framework-specific entity that runs in a container and negotiates resources from the Resource Manager. It also works with the Node Manager to execute and monitor the tasks on the containers. It is the main component that implements the logic and coordination of the application execution.

The following diagram illustrates the YARN architecture and the flow of an application submission and execution:

![YARN architecture diagram](https://www.geeksforgeeks.org/wp-content/uploads/YARN-Architecture.png)