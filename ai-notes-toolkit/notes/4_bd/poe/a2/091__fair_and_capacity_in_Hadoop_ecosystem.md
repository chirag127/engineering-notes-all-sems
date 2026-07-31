 Here is the content in Markdown format with formal tone and without any emojis or external links:

#### Fair and Capacity in Hadoop Ecosystem

1. Hadoop employs a master-slave architecture. The JobTracker is the master which coordinates all the jobs and assigns work to slaves i.e. TaskTrackers. This architecture achieves scalability by distributing workload across multiple machines. However, the single JobTracker is a single point of failure and bottleneck for fair resource allocation.

2. Fair Scheduler was introduced to overcome these limitations. It has a pluggable scheduler architecture with multiple queues. Each job is assigned a priority and placed in a queue. The scheduler ensures that higher priority queues get more resources than lower priority queues. This ensures fairness and avoids starvation of jobs.

3. Capacity Scheduler was introduced as an improvement over Fair Scheduler. It allows allocation of capacities to queues in a hierarchical fashion. This provides a more comprehensive way to allocate resources based on organizational priorities. Administrators can allocate capacities to top-level queues and then further sub-divide them. This leads to higher resource utilization and increases throughput.

4. Both Fair Scheduler and Capacity Scheduler enable Hadoop to achieve scalability, fairness, and higher throughput by distributing workload efficiently across a cluster of machines in a multi-tenant environment. The choice between the two depends on the specific requirements and use cases.

The content summarizes the key points around fair scheduling and capacity scheduling in the Hadoop ecosystem in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the content in any way.