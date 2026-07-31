# Unit 3 - Overview of Cluster Computing

## What is Cluster Computing?

- Cluster computing is a form of high-performance computing that involves connecting multiple computers (nodes) on a network to work together as a single system.
- Cluster computing provides solutions to solve difficult problems by providing faster computational speed, enhanced data integrity, and higher availability.
- Cluster computing can be classified into two types: loosely coupled and tightly coupled.
  - Loosely coupled clusters have each node perform different tasks, and communicate with each other only when necessary. An example of a loosely coupled cluster is a web server cluster that distributes the workload among different nodes.
  - Tightly coupled clusters have each node perform the same task, and communicate with each other frequently. An example of a tightly coupled cluster is a parallel computing cluster that uses a common memory or message passing interface to coordinate the computation.

## Why Cluster Computing?

- Cluster computing has several advantages over traditional single-node computing, such as:
  - Scalability: Cluster computing can easily scale up or down by adding or removing nodes, depending on the demand and resources available.
  - Reliability: Cluster computing can tolerate node failures by using redundancy and fault tolerance mechanisms, such as replication, checkpointing, and failover.
  - Cost-effectiveness: Cluster computing can leverage the existing hardware and software infrastructure, and use commodity components to build a cluster, rather than investing in expensive supercomputers.
  - Flexibility: Cluster computing can support different types of applications and workloads, and can be customized and configured according to the user's needs and preferences.

## How Cluster Computing Works?

- Cluster computing works by using a software layer that manages the communication and coordination among the nodes, and provides a unified interface to the user or application.
- The software layer can be divided into three components: cluster middleware, cluster management, and cluster application.
  - Cluster middleware is the software that enables the nodes to communicate and share data with each other, and provides services such as load balancing, scheduling, security, and monitoring. Examples of cluster middleware are MPI, OpenMP, Hadoop, and Spark.
  - Cluster management is the software that controls the configuration, deployment, and maintenance of the cluster, and provides services such as resource allocation, node discovery, and fault detection. Examples of cluster management are Kubernetes, Slurm, and Torque.
  - Cluster application is the software that runs on the cluster and performs the computation or processing of the data. Examples of cluster applications are scientific simulations, machine learning, and data analytics.