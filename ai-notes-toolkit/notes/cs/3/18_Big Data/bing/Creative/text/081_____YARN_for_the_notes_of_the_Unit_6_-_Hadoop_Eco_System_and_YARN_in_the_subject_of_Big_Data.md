### YARN

YARN stands for Yet Another Resource Negotiator. It is a component of Hadoop that was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0's MapReduce framework. YARN is responsible for managing and allocating resources to the applications running on a Hadoop cluster, as well as scheduling and monitoring the tasks executed on different nodes. YARN enables Hadoop to support various types of applications, such as batch processing, stream processing, interactive analysis, machine learning, etc.

The main components of YARN architecture are:

- **Client**: It submits the application (such as a MapReduce job) to the Resource Manager and monitors its progress.
- **Resource Manager**: It is the master daemon of YARN that coordinates the allocation of resources among all the applications in the cluster. It consists of two sub-components: the Scheduler and the Application Manager.
- **Scheduler**: It performs scheduling based on the resource requests from the applications and the available resources in the cluster. It is a pure scheduler that does not perform any monitoring or tracking of the application status. It supports various scheduling policies, such as FIFO, Fair, Capacity, etc.
- **Application Manager**: It is responsible for accepting the application submission, negotiating the first container for the application, and launching the Application Master on that container.
- **Application Master**: It is a per-application instance that runs on a container and manages the application's execution. It requests resources from the Scheduler, communicates with the Node Managers to launch and monitor the containers, and reports the application status to the Resource Manager.
- **Node Manager**: It is the slave daemon of YARN that runs on each node in the cluster and manages the containers on that node. It monitors the resource usage and health of the containers, and reports them to the Resource Manager. It also handles the commands from the Application Master to start or stop the containers.