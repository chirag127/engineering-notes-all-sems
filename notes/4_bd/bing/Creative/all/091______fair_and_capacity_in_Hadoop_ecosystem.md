#### Fair and Capacity in Hadoop Ecosystem

- Hadoop is a batch processing ecosystem that can handle large-scale data analysis using distributed computing.
- Hadoop has a resource management layer called YARN (Yet Another Resource Negotiator) that allocates resources to different applications running on the cluster.
- Hadoop also has a scheduling layer that decides the order and priority of the applications and tasks that are submitted to the cluster.
- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.
- FIFO (First In First Out) scheduler is the simplest and default scheduler that executes the applications in the order of their submission. It does not consider the priority, size, or resource requirements of the applications.
- Capacity scheduler is a more advanced scheduler that allows multiple queues with different capacities and priorities to be created. Each queue can have its own configuration, access control, and resource limits. The capacity scheduler tries to ensure that each queue gets its fair share of resources, but also allows for resource borrowing and preemption among queues.
- Fair scheduler is another advanced scheduler that aims to provide equal and fair access to resources for all applications. It does not use queues, but instead assigns resources to applications based on their demand and weight. The fair scheduler can also support hierarchical pools, preemption, and reservation of resources .
- The choice of scheduler depends on the use case and the requirements of the applications. Some factors to consider are the number and diversity of applications, the resource availability and utilization, the SLA and QoS expectations, and the trade-off between fairness and efficiency.