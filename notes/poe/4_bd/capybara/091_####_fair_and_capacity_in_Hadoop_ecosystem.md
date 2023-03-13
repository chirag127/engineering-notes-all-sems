#### Fair and Capacity in Hadoop Ecosystem

Hadoop is an open-source framework that is used for distributed storage and processing of large datasets. In Hadoop, the resource management is handled by YARN (Yet Another Resource Negotiator). YARN has two scheduling policies - Fair Scheduler and Capacity Scheduler. In this section, we will discuss the Fair Scheduler and Capacity Scheduler in Hadoop Ecosystem.

##### Fair Scheduler

The Fair Scheduler is a scheduling policy that allows sharing resources among multiple jobs. It ensures that each job gets an equal share of the resources based on its demand. The Fair Scheduler supports multiple queues, and each queue can have a different weight, depending on the priority of the job. The Scheduler ensures that every job gets a fair share of the resources, regardless of the size of the job, and no single job can dominate the resources.

The Fair Scheduler uses the following concepts:

- Queues: Queues are used to group similar jobs together, and they are assigned weights based on their priority.
- Fair share: Fair share is the amount of resources that each queue gets based on its weight.
- Minimum share: Minimum share is the minimum amount of resources that each queue gets, even if it is not using them.
- Preemption: Preemption is used when a queue is not getting its fair share of resources. The Fair Scheduler can preempt resources from a queue that is using more than its fair share and give them to a queue that is not getting its fair share.

##### Capacity Scheduler

The Capacity Scheduler is a scheduling policy that allows allocating resources to queues based on their capacity. It ensures that each queue gets a guaranteed share of the resources, and the resources are allocated based on the capacity of the queue. The Capacity Scheduler supports multiple queues, and each queue is assigned a percentage of the available resources.

The Capacity Scheduler uses the following concepts:

- Queues: Queues are used to group similar jobs together, and they are assigned a percentage of the available resources.
- Capacity: Capacity is the percentage of resources that each queue gets.
- Maximum capacity: Maximum capacity is the maximum percentage of resources that each queue can get.
- Minimum capacity: Minimum capacity is the minimum percentage of resources that each queue can get, even if it is not using them.

Mnemonics and Learning Tricks:
- For Fair Scheduler, remember "fair share," which means that every job gets a fair share of the resources.
- For Capacity Scheduler, remember "capacity," which means that resources are allocated based on the capacity of the queue.

Advantages of Fair Scheduler:
- Better resource utilization
- No job can dominate the resources
- Multiple queues for different jobs

Disadvantages of Fair Scheduler:
- Preemption can cause delays
- Difficult to configure

Advantages of Capacity Scheduler:
- Guaranteed share of resources for each queue
- Better predictability of job completion time
- Easy to configure

Disadvantages of Capacity Scheduler:
- Poor resource utilization
- No sharing of resources between queues

Examples of Fair Scheduler:
- Hadoop MapReduce
- Apache Spark

Examples of Capacity Scheduler:
- Apache HBase
- Apache Storm

Applications of Fair Scheduler:
- Big data processing
- Web analytics
- Data warehousing

Applications of Capacity Scheduler:
- Online transaction processing
- Real-time data processing
- E-commerce websites

In conclusion, both Fair Scheduler and Capacity Scheduler have their advantages and disadvantages. It is important to choose the right scheduling policy based on the requirements of the application.