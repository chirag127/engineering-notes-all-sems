### Fair and Capacity Schedulers in Hadoop Eco System and YARN

- **Fair Scheduler**: The Fair Scheduler is a pluggable scheduler for Hadoop that allows YARN applications to share resources in a large cluster fairly. It is designed to provide a more predictable and consistent share of resources to each application over time, regardless of the current demand for resources.

- **Capacity Scheduler**: The Capacity Scheduler is another pluggable scheduler for Hadoop that allows YARN applications to share resources in a large cluster based on predefined capacities. It is designed to provide a guaranteed capacity to each queue, while still allowing for the efficient utilization of unused resources.

- Both the Fair Scheduler and the Capacity Scheduler are designed to provide a fair and efficient allocation of resources to applications in a Hadoop cluster. They both support hierarchical queues, preemption, and configurable allocation policies.

- The choice between the Fair Scheduler and the Capacity Scheduler depends on the specific needs and requirements of the Hadoop cluster and its applications. The Fair Scheduler is generally better suited for environments where there is a need for more predictable and consistent resource allocation, while the Capacity Scheduler is better suited for environments where there is a need for guaranteed capacity and efficient utilization of unused resources.

- Both schedulers are highly configurable and can be customized to meet the specific needs of a Hadoop cluster. It is important to carefully evaluate the requirements of the cluster and its applications before choosing a scheduler and configuring its settings.