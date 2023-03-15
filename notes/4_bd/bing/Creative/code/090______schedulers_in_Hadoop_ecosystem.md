#### Schedulers in Hadoop ecosystem

Schedulers are algorithms that are used to schedule tasks in a Hadoop cluster when there are multiple requests from different clients. Schedulers help to optimize the utilization of resources and access the unused capacity of the cluster. There are mainly three types of schedulers in Hadoop:

- **FIFO (First In First Out) Scheduler**: This is the simplest and default scheduler in Hadoop. It assigns tasks to the nodes in the order of their arrival. It does not consider the priority, size, or resource requirements of the tasks. It is suitable for small clusters with homogeneous workloads.

- **Capacity Scheduler**: This is a more advanced scheduler that allows multiple queues to be created, each with a configurable capacity and priority. The queues can be hierarchical and can have sub-queues. The tasks are assigned to the nodes based on the capacity and priority of the queues. This scheduler supports multi-tenancy and resource sharing among different users and groups.

- **Fair Scheduler**: This is another advanced scheduler that aims to provide fair and equal share of resources to all the tasks, regardless of the queue or user. It dynamically adjusts the resource allocation based on the demand and availability of the cluster. It also supports hierarchical queues, preemption, and weight-based shares. This scheduler is suitable for large clusters with heterogeneous and dynamic workloads.