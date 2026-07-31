### Fair and Capacity Schedulers in Hadoop Eco System and YARN

- **Fair Scheduler**: The Fair Scheduler is a pluggable scheduler for Hadoop that allows YARN applications to share resources in a large cluster fairly. It is designed to provide a more predictable and consistent allocation of resources to applications, regardless of their demand, by ensuring that each application gets an equal share of the resources over time.

- **Capacity Scheduler**: The Capacity Scheduler is another pluggable scheduler for Hadoop that is designed to allow multiple organizations to share a large cluster while ensuring that each organization is allocated a guaranteed minimum share of the resources. It works by dividing the resources of the cluster into multiple queues, each of which is assigned a certain capacity, and then allocating resources to applications within each queue based on their demand.

Both the Fair and Capacity Schedulers are designed to improve the utilization of resources in a Hadoop cluster and provide a more predictable and consistent allocation of resources to applications. They are both part of the Hadoop Eco System and can be used with YARN to manage the allocation of resources in a large cluster.
