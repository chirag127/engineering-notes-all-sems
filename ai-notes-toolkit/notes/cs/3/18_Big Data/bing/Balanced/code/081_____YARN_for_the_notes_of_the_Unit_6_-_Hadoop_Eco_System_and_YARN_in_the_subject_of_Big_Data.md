### YARN

YARN stands for Yet Another Resource Negotiator. It is a component of Hadoop that manages the resources and the execution of applications on a Hadoop cluster. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as scalability, resource utilization, and support for non-MapReduce applications.

The main components of YARN architecture are:

- **Client**: It submits the application (a single job or a DAG of jobs) to the Resource Manager and monitors its progress.
- **Resource Manager**: It is the master daemon of YARN that allocates and manages the resources among all the applications in the cluster. It has two sub-components:
  - **Scheduler**: It performs scheduling based on the resource requests from the applications and the available resources in the cluster. It is a pure scheduler that does not perform any monitoring or tracking of the application status. It supports different scheduling policies, such as FIFO, Capacity, and Fair.
  - **Application Manager**: It is responsible for accepting the application submission, negotiating the first container for the application, and launching the Application Master on that container. It also maintains the application metadata and handles the application failures and restarts.
- **Node Manager**: It is the slave daemon of YARN that runs on each node in the cluster and manages the containers (the units of resource allocation) on that node. It communicates with the Resource Manager to report the resource utilization and availability on the node. It also communicates with the Application Master to launch and monitor the containers assigned to the application.
- **Application Master**: It is the master of an application that runs on a container and coordinates the execution of the application tasks on different containers. It requests resources from the Resource Manager and works with the Node Manager to execute and monitor the containers. It also handles the application logic and the failures of the tasks.