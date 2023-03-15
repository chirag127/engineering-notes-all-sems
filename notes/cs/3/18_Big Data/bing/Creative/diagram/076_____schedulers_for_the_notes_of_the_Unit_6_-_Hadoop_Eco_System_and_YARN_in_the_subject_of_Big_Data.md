### Schedulers for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- Schedulers are algorithms that allocate resources to applications running on a Hadoop cluster based on some criteria  .
- Schedulers are pluggable components that can be configured in the YARN ResourceManager.
- YARN stands for Yet Another Resource Negotiator, which is the resource management layer of Hadoop.
- YARN consists of a ResourceManager, a NodeManager, an ApplicationMaster, and a Container.
- The ResourceManager is the central authority that arbitrates resources among all the applications in the system.
- The NodeManager is the per-machine framework agent who is responsible for containers, monitoring their resource usage (cpu, memory, disk, network) and reporting the same to the ResourceManager/Scheduler.
- The ApplicationMaster is the framework-specific library that negotiates resources from the ResourceManager and works with the NodeManager(s) to execute and monitor the tasks.
- The Container is the basic unit of resource allocation in YARN, which encapsulates some amount of memory, cpu, disk and network that can be allocated to an application.

- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.
- FIFO (First In First Out) Scheduler: This is the simplest scheduler that assigns resources to applications in the order of their submission. It does not consider the resource requirements or the priority of the applications. It is suitable for small clusters with simple workloads.
- Capacity Scheduler: This is a more advanced scheduler that allows multiple queues to be created, each with a configurable capacity and priority . It ensures that each queue gets a minimum share of the cluster resources, and can use the free resources when available . It also supports hierarchical queues, preemption, access control, and resource limits . It is suitable for large clusters with multiple tenants and diverse workloads .
- Fair Scheduler: This is another advanced scheduler that aims to provide fair sharing of resources among applications . It dynamically adjusts the resource allocation to each application based on the demand and the configured weights . It also supports multiple queues, preemption, access control, and resource limits . It is suitable for large clusters with heterogeneous workloads and different service level agreements .