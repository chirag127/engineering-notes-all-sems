### Fair and Capacity for the Notes of the Unit 6 - Hadoop Eco System and YARN in the Subject of Big Data

- Hadoop Eco System is a collection of open source projects and tools that work together to provide a distributed computing platform for big data processing and analysis.
- YARN (Yet Another Resource Negotiator) is a core component of Hadoop Eco System that provides resource management and job scheduling for Hadoop applications.
- YARN was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0, such as scalability, efficiency, and flexibility.
- YARN architecture consists of two main components: ResourceManager (RM) and ApplicationMaster (AM).
- ResourceManager is a global daemon that manages the cluster resources and allocates them to different applications based on their requirements and priorities.
- ApplicationMaster is a per-application daemon that negotiates resources with the ResourceManager, coordinates the execution of tasks across the cluster, and monitors the progress and status of the application.
- YARN also supports multiple programming models and frameworks, such as MapReduce, Spark, Hive, Pig, etc., that can run on top of YARN and leverage its resource management capabilities.
- YARN enables fair and capacity scheduling for Hadoop applications, which means that it ensures that each application gets a fair share of resources according to its needs and the cluster capacity, and that no application is starved or over-allocated.
- Fair scheduling is a method of assigning resources to applications such that each application gets an equal share of resources over time, regardless of the number and size of the applications.
- Capacity scheduling is a method of assigning resources to applications such that each application gets a minimum guaranteed share of resources, and the remaining resources are distributed among the applications based on their demands and weights.
- YARN supports both fair and capacity scheduling through pluggable schedulers, such as FairScheduler and CapacityScheduler, that can be configured and customized according to the cluster and application requirements.
- YARN also supports hierarchical queues, preemption, reservations, and labels for fine-grained and flexible resource allocation and management.