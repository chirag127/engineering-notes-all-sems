#### Fair and Capacity in Hadoop Ecosystem

In Hadoop ecosystem, Fair and Capacity schedulers are used to manage the allocation of resources (CPU, memory, disk, etc.) among different users and applications in a fair and efficient manner. These schedulers help in achieving better resource utilization and performance by ensuring that no user or application is starved of resources and that the resources are used optimally.

##### Fair Scheduler

The Fair Scheduler is a pluggable scheduler that allows multiple jobs to share a cluster in a fair manner. It allocates resources to jobs based on their fair share, which is defined as the maximum amount of resources that a job is entitled to, based on the number of jobs in the system and their respective priorities. The Fair Scheduler maintains a queue for each job and allocates resources on a first-come, first-served basis, with each job receiving its fair share of resources. If a job is not using its fair share of resources, the scheduler will allocate the unused resources to other jobs in the queue.

##### Capacity Scheduler

The Capacity Scheduler is another pluggable scheduler that allows multiple organizations to share a cluster in a way that guarantees a minimum amount of resources to each organization. It divides the cluster's resources among multiple queues, each of which is associated with a different organization or user. Each queue is assigned a guaranteed minimum capacity, which ensures that it can always access the resources it needs. If a queue is not using its full capacity, the unused resources can be allocated to other queues that need more resources.

##### Learning Tricks

- For remembering Fair Scheduler, you can think of it as a "fair" way of allocating resources, where each job gets its fair share of resources.
- For remembering Capacity Scheduler, you can think of it as a way of allocating resources based on the "capacity" of each queue, where each queue is guaranteed a minimum amount of resources.

##### Advantages

- Fair and Capacity schedulers help in achieving better resource utilization and performance by ensuring that resources are used efficiently and that no user or application is starved of resources.
- Fair Scheduler ensures that each job gets its fair share of resources, which is determined based on the number of jobs in the system and their respective priorities.
- Capacity Scheduler ensures that each queue is guaranteed a minimum amount of resources, which ensures that each organization or user can access the resources they need.

##### Disadvantages

- Fair and Capacity schedulers can be difficult to configure and tune, especially in large-scale deployments.
- Fair Scheduler may not be suitable for all types of workloads, especially those with varying resource requirements or unpredictable job sizes.
- Capacity Scheduler may have some overhead due to the need to manage multiple queues and their respective capacities.

##### Examples

- Fair Scheduler is used in Apache Hadoop and Hadoop YARN.
- Capacity Scheduler is used in Apache Hadoop and Hadoop YARN, as well as other Hadoop distributions like Cloudera and Hortonworks.

##### Applications

- Fair and Capacity schedulers are widely used in Hadoop ecosystem for resource management and job scheduling.
- They are also used in other distributed systems and cloud computing platforms for similar purposes.