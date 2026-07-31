### YARN

YARN stands for Yet Another Resource Negotiator. It is a component of Hadoop that manages the resources and the execution of applications in a Hadoop cluster. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as scalability, resource utilization, and support for non-MapReduce applications.

The main components of YARN architecture are:

- **Client**: It submits the application (a single job or a DAG of jobs) to the Resource Manager and monitors its progress.
- **Resource Manager**: It is the master daemon of YARN that allocates and manages the resources among all the applications in the cluster. It consists of two sub-components: the Scheduler and the Application Manager.
- **Scheduler**: It performs scheduling based on the resource requests from the applications and the available resources in the cluster. It is a pure scheduler that does not perform any monitoring or tracking of the application status. It supports various scheduling policies, such as FIFO, Capacity, and Fair.
- **Application Manager**: It is responsible for accepting the application submission, negotiating the first container for the application, and launching the Application Master on that container.
- **Application Master**: It is a per-application framework-specific entity that negotiates the resources from the Resource Manager and works with the Node Managers to execute and monitor the tasks. It also handles the failures and retries of the tasks.
- **Node Manager**: It is the slave daemon of YARN that runs on each node in the cluster and manages the containers (the units of resource allocation) on that node. It monitors the resource usage and health of the containers and reports them to the Resource Manager. It also communicates with the Application Master to launch and stop the containers.

The following diagram illustrates the YARN architecture and the flow of an application execution:

![YARN architecture diagram](https://www.geeksforgeeks.org/wp-content/uploads/YARN-Architecture.png)

Source: https://www.geeksforgeeks.org/hadoop-yarn-architecture/