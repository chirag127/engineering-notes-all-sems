#### Fair and Capacity in Hadoop Ecosystem

- Hadoop is a batch processing ecosystem that can handle large-scale data analysis using distributed computing.
- Hadoop has a distributed storage layer called HDFS (Hadoop Distributed File System) that splits the incoming data into blocks and stores them across multiple nodes in a cluster.
- Hadoop also has a distributed processing layer called YARN (Yet Another Resource Negotiator) that manages the resources and tasks for the applications running on the cluster.
- Hadoop uses schedulers to allocate resources and schedule tasks for the applications based on different policies and priorities.
- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.
- FIFO (First In First Out) scheduler is the simplest and default scheduler that assigns resources to jobs in the order of their submission. It does not consider the priority or size of the jobs and can cause starvation for smaller or later jobs.
- Capacity scheduler is a more advanced scheduler that allows multiple queues with different capacities and priorities to be configured. Each queue can have a minimum and maximum capacity and can run multiple jobs concurrently. The capacity scheduler can enforce limits on the resources used by each user or group and can support preemption and reservation of resources.
- Fair scheduler is another advanced scheduler that aims to provide fair and equal share of resources to all jobs over time. It dynamically balances the resources between the running jobs and can support hierarchical queues with weights and min/max shares. The fair scheduler can also consider the priority and size of the jobs and can support preemption and delay scheduling.