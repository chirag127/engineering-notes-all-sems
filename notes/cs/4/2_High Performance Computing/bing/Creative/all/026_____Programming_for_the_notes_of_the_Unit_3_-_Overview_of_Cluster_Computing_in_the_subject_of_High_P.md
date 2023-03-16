# Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

## Cluster Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) together in a network to perform a common task.
- Cluster computing can provide faster computational speed, enhanced data integrity, higher availability, and better scalability than a single computer.
- Cluster computing can be classified into two types: loosely coupled and tightly coupled.
  - Loosely coupled clusters have each node running its own operating system and software, and communicate with each other through a network interface.
  - Tightly coupled clusters have each node running the same operating system and software, and communicate with each other through a high-speed interconnect.
- Cluster computing can be used for various applications, such as scientific computing, data analysis, web hosting, load balancing, and fault tolerance.

## Cluster Architecture

- A typical cluster architecture consists of the following components:
  - Head node: The head node is the central node that controls and coordinates the activities of the cluster. It is responsible for scheduling jobs, managing resources, and providing access to the cluster for users and applications.
  - Compute nodes: The compute nodes are the nodes that perform the actual computation and processing of the cluster. They receive tasks from the head node and execute them in parallel.
  - Storage nodes: The storage nodes are the nodes that provide storage space for the cluster. They can be either local or distributed, depending on the cluster configuration and the data requirements.
  - Network: The network is the medium that connects the nodes together and enables data transfer and communication among them. The network can be either a local area network (LAN) or a wide area network (WAN), depending on the cluster size and location.

## Cluster Programming

- Cluster programming is the process of developing and running applications that can utilize the cluster resources and achieve high performance and efficiency.
- Cluster programming can be done using various tools and frameworks, such as:
  - Message Passing Interface (MPI): MPI is a standard for writing parallel programs that communicate through messages. MPI provides a set of functions and libraries that allow programmers to create, send, receive, and synchronize messages among processes in a cluster.
  - OpenMP: OpenMP is a standard for writing parallel programs that use shared memory. OpenMP provides a set of directives and functions that allow programmers to specify parallel regions, loops, and tasks in a cluster.
  - MapReduce: MapReduce is a framework for writing parallel programs that process large-scale data sets. MapReduce provides a simple programming model that consists of two functions: map and reduce. The map function applies a transformation to each input data element and produces intermediate key-value pairs. The reduce function aggregates the intermediate values associated with the same key and produces the final output.