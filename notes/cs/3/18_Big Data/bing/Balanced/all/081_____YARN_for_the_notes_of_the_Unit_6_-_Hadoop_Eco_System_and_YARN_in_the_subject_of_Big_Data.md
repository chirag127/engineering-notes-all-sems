# YARN

YARN stands for Yet Another Resource Negotiator. It is a component of Hadoop that manages the resources and scheduling of tasks in a Hadoop cluster. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0.

## YARN Architecture

The main components of YARN architecture are:

- **Client**: It submits the application (such as MapReduce job) to the Resource Manager and monitors its progress.
- **Resource Manager**: It is the master daemon of YARN that allocates and manages the resources among all the applications in the cluster.
- **Scheduler**: It is a part of the Resource Manager that performs scheduling based on the application requirements and available resources. It does not perform any monitoring or tracking of the application status. It is a pure scheduler that supports different policies such as FIFO, fair, and capacity.
- **Application Manager**: It is another part of the Resource Manager that is responsible for accepting the application submission, negotiating the first container for the application, and launching the Application Master.
- **Application Master**: It is a per-application framework-specific entity that runs in a container and coordinates the execution of the application tasks on the cluster. It requests resources from the Resource Manager and works with the Node Managers to execute and monitor the tasks.
- **Node Manager**: It is the slave daemon of YARN that runs on each node in the cluster and manages the containers, resources, and task execution on that node. It communicates with the Resource Manager and the Application Master to report the status of the containers and the tasks.

The following diagram shows the YARN architecture and the interaction among its components:

![YARN Architecture](https://www.geeksforgeeks.org/wp-content/uploads/YARN-Architecture.png)

## Key Features of YARN

Some of the key features of YARN are:

- It decouples the resource management and the programming model from MapReduce and enables other frameworks to run on Hadoop, such as Spark, Hive, and Pig.
- It improves the scalability, efficiency, and utilization of the cluster by allowing multiple applications to share the resources dynamically.
- It supports high availability and security features for the Resource Manager and the Node Manager.
- It provides a web-based user interface and REST APIs for monitoring and managing the applications and the cluster.