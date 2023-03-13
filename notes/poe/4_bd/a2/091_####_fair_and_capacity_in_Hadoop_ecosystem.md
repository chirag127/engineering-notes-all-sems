 Here is the content in markdown format on the topic #### fair and capacity in Hadoop ecosystem:

#### Fair and Capacity in Hadoop Ecosystem

The Hadoop ecosystem aims to provide fair and maximum utilization of cluster resources. The following points discuss how fair and capacity is achieved in Hadoop:

- **Resource Manager (RM)**: The RM ensures fair sharing of resources among applications. It allocates resources to applications based on demands and availability. It supports multiple scheduling policies like Capacity Scheduler, Fair Scheduler, FIFO Scheduler, etc. to achieve fairness and maximize utilization.
- **Capacity Scheduler**: It supports multi-tenancy and ensures guaranteed capacity to queues. It allocates resources to queues based on configured capacities. Additional resources are allocated to queues if required and if capacities of other queues are not violated. This ensures fairness and high utilization.
- **Fair Scheduler**: It ensures all jobs get roughly equal share of resources over time. It allocates resources to jobs based on configured min and max shares. Unused resources from queues/users can be utilized by others to maximize utilization.
- **YARN Node Manager (NM)**: The NM monitors resource usage on slave nodes and reports to RM. If a container is idle/underutilizing, the RM can allocate the resources to other applications to achieve high utilization.
- **Container reuse**: The RM/NM can reuse containers from completed tasks for new tasks from same/different applications. This avoids overhead of creating new containers and increases resource utilization.

The above points cover how Hadoop achieves fair sharing of resources and maximum utilization through key components and features. Learning the working of these components and scheduling policies/algorithms helps understand fair and capacity in the Hadoop ecosystem.