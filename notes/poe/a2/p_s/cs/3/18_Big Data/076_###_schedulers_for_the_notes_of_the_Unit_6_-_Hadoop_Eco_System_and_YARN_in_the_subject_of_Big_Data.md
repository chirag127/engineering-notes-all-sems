 Here is the content in markdown format for the topic ### schedulers for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data:

### Schedulers

- Schedulers are components of the ResourceManager in YARN that are responsible for allocating resources to applications.
- The two main schedulers in YARN are:
	- Capacity Scheduler - Queues jobs and allocates resources based on capacities defined for each queue. Each queue is assigned a guaranteed capacity, and excess capacity is distributed to queues based on weights.
		- Advantages - Simple, prevents clusters from being overwhelmed by a single job.
		- Disadvantages - Inflexible, cannot dynamically grow or shrink queues.
	- Fair Scheduler - Allocates resources in a fair manner by accounting resources used by running applications and trying to allocating resources equally to all running applications.
		- Advantages - Better resource utilization, prioritization of queues possible.
		- Disadvantages - More complex than Capacity Scheduler, difficult to configure.
- Choosing a scheduler depends on workload requirements - Capacity Scheduler for multi-tenant clusters requiring isolation, Fair Scheduler for maximizing throughput.
- Other YARN schedulers - Dominant Resource Fairness (DRF), Centrally Controlled Scheduler.
- Code for Capacity and Fair Schedulers is open source and available in the Hadoop project.

[Detailed diagrams and examples can be added here to help understand the schedulers better.]

The content summarizes the two main YARN schedulers - Capacity Scheduler and Fair Scheduler, lists their advantages and disadvantages, and mentions other schedulers and factors to consider when choosing a scheduler. The points are written in a formal tone with relevant details as would be suitable for exam notes. Please let me know if you would like me to elaborate on any part or add any other details.