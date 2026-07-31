### Unit 3 - Map Reduce: Job Scheduling

1. Job scheduling is the process of allocating resources to tasks in a way that meets certain objectives, such as minimizing completion time or maximizing resource utilization.
2. In the context of MapReduce, job scheduling refers to the process of assigning map and reduce tasks to available nodes in the cluster.
3. Several job scheduling algorithms have been proposed for MapReduce, including the Fair Scheduler, the Capacity Scheduler, and the FIFO Scheduler.
4. The Fair Scheduler assigns resources to jobs in a way that ensures that each job gets a fair share of the cluster resources over time.
5. The Capacity Scheduler allows administrators to define multiple queues, each with a guaranteed capacity, and jobs are assigned to queues based on their priority and resource requirements.
6. The FIFO Scheduler assigns resources to jobs in the order in which they were submitted, with the first job in the queue receiving the highest priority.
7. The choice of job scheduling algorithm can have a significant impact on the performance of a MapReduce cluster, and administrators should carefully consider their requirements when selecting an algorithm.