#### Fair and Capacity in Hadoop Ecosystem

- Hadoop is a batch processing ecosystem that can handle large-scale data analysis using distributed computing.
- Hadoop has a resource management layer called YARN (Yet Another Resource Negotiator) that allocates resources to different applications running on the cluster.
- Hadoop also has a scheduling layer that decides the order and priority of the applications that request resources from YARN.
- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.
- FIFO (First In First Out) Scheduler is the simplest and default scheduler that assigns resources to applications based on their submission time. It does not consider the priority, size, or resource requirements of the applications. It is suitable for small clusters with homogeneous and predictable workloads.
- Capacity Scheduler is a more advanced scheduler that allows multiple queues to be created, each with a fixed percentage of the cluster capacity. Each queue can have its own access control, priority, and resource limits. The Capacity Scheduler can handle heterogeneous and dynamic workloads, and can support multi-tenancy and preemption.
- Fair Scheduler is another advanced scheduler that aims to provide fair and equal share of resources to all applications over time. It does not require predefined queues or capacities, but dynamically balances the resources among the running applications. The Fair Scheduler can also handle heterogeneous and dynamic workloads, and can support multi-tenancy, preemption, and weight-based priorities.