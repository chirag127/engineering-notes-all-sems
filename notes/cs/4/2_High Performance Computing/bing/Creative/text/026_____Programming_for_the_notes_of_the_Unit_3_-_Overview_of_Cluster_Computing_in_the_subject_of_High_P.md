### Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for high-performance tasks  .
- Cluster computing can provide faster computational speed, enhanced data integrity, higher availability, and better scalability than a single computer .
- Cluster computing can be classified into two types: loosely coupled and tightly coupled.
  - Loosely coupled clusters have nodes that are independent and communicate only when necessary. They are suitable for tasks that can be divided into smaller subtasks and executed in parallel with minimal coordination.
  - Tightly coupled clusters have nodes that are synchronized and communicate frequently. They are suitable for tasks that require high data exchange and coordination among the nodes.
- Cluster computing can also be categorized based on the architecture and functionality of the nodes, such as homogeneous or heterogeneous, symmetric or asymmetric, fail-over or load-balancing, etc .
- Cluster computing requires software tools to manage the nodes, distribute the workload, monitor the performance, and handle the faults  .
  - Some examples of cluster management software are Kubernetes, Apache Mesos, Hadoop, and MPI  .
  - Some examples of cluster programming models are MapReduce, Spark, OpenMP, and CUDA  .
- Cluster computing has many applications in various domains, such as scientific computing, big data analytics, web services, machine learning, and gaming  .