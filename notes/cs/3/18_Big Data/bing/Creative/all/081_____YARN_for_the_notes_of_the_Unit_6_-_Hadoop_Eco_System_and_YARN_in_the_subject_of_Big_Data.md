# YARN

YARN stands for Yet Another Resource Negotiator. It is a component of Hadoop that manages the resources and the scheduling of tasks on a Hadoop cluster. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as scalability, resource utilization, and application support.

## YARN Architecture

The main components of YARN architecture are:

- **Client**: It submits the application (such as MapReduce job) to the Resource Manager and monitors its progress.
- **Resource Manager**: It is the master daemon of YARN that coordinates the allocation and management of resources among all the applications in the cluster.
- **Scheduler**: It is a part of the Resource Manager that performs the scheduling of tasks based on the resource requests from the applications and the available resources in the cluster. It is a pure scheduler that does not perform any monitoring or tracking of the application status. It supports different scheduling policies, such as FIFO, Fair, and Capacity.
- **Application Manager**: It is another part of the Resource Manager that is responsible for accepting the application submission, negotiating the first container for the application, and launching the Application Master.
- **Application Master**: It is a process that runs on a container and manages the life cycle of an application. It communicates with the Resource Manager to request and release resources, and with the Node Managers to launch and monitor the containers that run the application tasks.
- **Node Manager**: It is the slave daemon of YARN that runs on each node in the cluster and manages the containers on that node. It monitors the resource usage and health of the containers, and reports them to the Resource Manager. It also communicates with the Application Masters to execute and stop the containers.

The following diagram shows the YARN architecture and the interaction among its components:

![YARN Architecture](https://www.geeksforgeeks.org/wp-content/uploads/YARN-Architecture.png)

## Key Features of YARN

Some of the key features of YARN are:

- **Scalability**: YARN can scale up to thousands of nodes and millions of tasks in a cluster, by separating the resource management and the application logic.
- **Resource Utilization**: YARN can utilize the cluster resources more efficiently, by allowing multiple applications to run on the same cluster and share the resources dynamically.
- **Application Support**: YARN can support various types of applications, not only MapReduce, but also Spark, Hive, Pig, Flink, etc. It also supports user-defined applications that implement the YARN API.
- **High Availability**: YARN can provide high availability for the Resource Manager and the Application Masters, by using ZooKeeper and the failover mechanism.
- **Security**: YARN can enforce security for the applications and the data, by using Kerberos authentication, authorization, and encryption.