#### Fair and Capacity in Hadoop Ecosystem

- Hadoop is a batch processing ecosystem that can handle large-scale data analysis using distributed computing.
- Hadoop has a distributed storage layer called HDFS (Hadoop Distributed File System) that splits the incoming data into blocks and stores them across multiple nodes in a cluster.
- Hadoop also has a distributed processing layer called YARN (Yet Another Resource Negotiator) that manages the resources and tasks for the applications running on the cluster.
- Hadoop uses schedulers to allocate resources and schedule tasks for the applications based on different policies and priorities.
- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.

##### FIFO Scheduler

- FIFO (First In First Out) Scheduler is the simplest and default scheduler in Hadoop.
- It assigns resources and tasks to the applications in the order of their submission.
- It does not consider the priority, size, or resource requirements of the applications.
- It can cause resource starvation and low cluster utilization if there are long-running or high-resource applications in the queue.

##### Capacity Scheduler

- Capacity Scheduler is a more advanced and flexible scheduler in Hadoop.
- It divides the cluster resources into multiple queues, each with a predefined capacity and a set of properties.
- It assigns resources and tasks to the applications based on the queue they belong to, their priority, and their resource requirements.
- It can support multiple tenants, hierarchical queues, preemption, resource sharing, and elasticity.
- It can improve cluster utilization and throughput by balancing the load across the queues.

##### Fair Scheduler

- Fair Scheduler is another advanced and flexible scheduler in Hadoop.
- It also divides the cluster resources into multiple queues, each with a weight and a set of properties.
- It assigns resources and tasks to the applications based on the queue they belong to, their priority, and their resource requirements.
- It can support multiple tenants, hierarchical queues, preemption, resource sharing, and elasticity.
- It can improve cluster utilization and fairness by ensuring that each application gets an equal share of resources over time.