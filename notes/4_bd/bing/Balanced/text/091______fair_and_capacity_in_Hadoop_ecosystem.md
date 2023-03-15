#### Fair and Capacity in Hadoop Ecosystem

- Hadoop is a batch processing ecosystem that can handle large-scale data analysis using distributed computing.
- Hadoop has a distributed storage layer called HDFS (Hadoop Distributed File System) that splits the incoming data into blocks and stores them across multiple nodes in a cluster.
- Hadoop also has a distributed processing layer called YARN (Yet Another Resource Negotiator) that manages the resources and tasks for the applications running on the cluster.
- Hadoop uses schedulers to allocate resources and schedule tasks for the applications based on different policies and priorities.
- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.
- FIFO (First In First Out) scheduler is the simplest and default scheduler that assigns resources to jobs in the order they are submitted. It does not consider the priority or size of the jobs and can cause starvation for smaller or later jobs.
- Capacity scheduler is a more advanced scheduler that allows multiple queues with different capacities and priorities to be created for different groups of users or applications. It ensures that each queue gets a minimum share of the cluster resources and can use the excess resources if available. It also supports preemption and limits for the queues to avoid starvation and resource wastage.
- Fair scheduler is another advanced scheduler that aims to provide a fair share of resources to all the jobs over time. It dynamically balances the resources between the running jobs based on their demand and priority. It also supports multiple queues with weights and min/max shares to accommodate different needs and preferences. It also supports preemption and limits for the queues to avoid starvation and resource wastage.