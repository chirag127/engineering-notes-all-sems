## Unit 6 - Hadoop Eco System and YARN

- Hadoop Eco System is a collection of open source projects and tools that work together to provide a scalable and reliable platform for big data processing and analysis.
- YARN (Yet Another Resource Negotiator) is a core component of Hadoop Eco System that manages the resources and scheduling of applications running on Hadoop clusters.
- YARN was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as low resource utilization, fixed programming model, and lack of support for non-MapReduce applications.
- YARN architecture consists of two main components: ResourceManager (RM) and ApplicationMaster (AM).
  - ResourceManager is a global daemon that oversees the allocation and management of resources (such as CPU, memory, disk, network) across the cluster nodes.
  - ApplicationMaster is a per-application daemon that coordinates the execution of tasks and monitors the progress and status of the application.
- YARN also supports a pluggable scheduler that can be configured to meet different requirements, such as capacity, fairness, priority, etc.
- YARN enables the Hadoop Eco System to run various types of applications, such as batch, interactive, streaming, graph, machine learning, etc., by providing a common framework for resource management and isolation.
- YARN also enhances the performance, scalability, and reliability of the Hadoop Eco System by allowing for dynamic resource allocation, fault tolerance, security, and multi-tenancy.