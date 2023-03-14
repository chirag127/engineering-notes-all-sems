#### Fair and capacity in Hadoop ecosystem

Fair and capacity are two types of schedulers in Hadoop ecosystem that are used to allocate resources to different applications or jobs running on a cluster. They are part of the YARN (Yet Another Resource Negotiator) framework, which is responsible for managing and scheduling the resources across the cluster.

- Fair scheduler: The fair scheduler assigns resources to applications such that all applications get, on average, an equal share of resources over time. It does not consider the priority or the queue of the applications, but rather tries to balance the resource usage among them. The fair scheduler can also be configured to enforce minimum and maximum resource shares for each application, as well as to support hierarchical queues and preemption.

- Capacity scheduler: The capacity scheduler assigns resources to applications based on the capacity and the priority of the queues they belong to. It ensures that each queue gets a guaranteed minimum share of the cluster resources, and can use the excess resources if available. The capacity scheduler can also be configured to support hierarchical queues, preemption, user limits, and node labels.

Some of the advantages and disadvantages of fair and capacity schedulers are:

- Fair scheduler advantages:
  - It is more suitable for multi-tenant environments, where different users or groups run different types of applications on the same cluster.
  - It prevents resource starvation and improves the overall cluster utilization by evenly distributing the resources among the applications.
  - It allows fine-grained control over the resource allocation for each application or queue, as well as the ability to dynamically adjust the weights and shares based on the demand.

- Fair scheduler disadvantages:
  - It may not respect the priority or the order of the applications, which may affect the performance or the SLA (Service Level Agreement) of some applications.
  - It may not be optimal for batch processing or high-throughput applications, which may require more resources than the average share.

- Capacity scheduler advantages:
  - It is more suitable for production environments, where different types of applications have different SLAs and priorities on the same cluster.
  - It ensures that each queue gets a minimum guaranteed share of the cluster resources, and can use the excess resources if available, which improves the performance and the throughput of the applications.
  - It allows fine-grained control over the resource allocation for each queue, as well as the ability to support user limits, node labels, and preemption.

- Capacity scheduler disadvantages:
  - It may cause resource wastage and underutilization, if some queues do not use their allocated resources or have low demand.
  - It may cause resource starvation and unfairness, if some queues have high demand and exceed their allocated resources or their user limits.

Some of the mnemonics and learning tricks for fair and capacity schedulers are:

- Fair scheduler: Think of a fair as a place where everyone gets a chance to enjoy the rides and attractions, regardless of their order or preference. Similarly, the fair scheduler gives every application a chance to use the cluster resources, regardless of their priority or queue.
- Capacity scheduler: Think of a capacity as a limit or a constraint on how much something can hold or accommodate. Similarly, the capacity scheduler limits the resource usage of each queue based on its capacity and priority.