
### Schedulers for the Notes of the Unit 6 - Hadoop Eco System and YARN in the Subject of Big Data

1. Hadoop Eco System is an open source software platform which enables distributed storage and processing of large datasets across clusters of computers.
2. YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop. It is responsible for allocating resources to applications running on the Hadoop cluster and scheduling tasks.
3. Hadoop Schedulers are responsible for scheduling jobs on the cluster. They decide which tasks should be run on which nodes, and when they should be run.
4. The most commonly used schedulers in Hadoop are the Capacity Scheduler, Fair Scheduler and the Default Scheduler.
5. The Capacity Scheduler is the default scheduler in Hadoop and is designed to manage resources in a multi-tenant environment. It allows administrators to define queues and assign resources to each queue.
6. The Fair Scheduler is designed to provide a fair allocation of resources across jobs. It uses a fair share policy to allocate resources to jobs based on their past usage.
7. The Default Scheduler is a simple scheduler which does not support queues or resource allocation. It is designed to run a single job at a time.
8. YARN provides a pluggable architecture which allows users to choose their own scheduler. This allows users to choose the scheduler which best fits their needs.