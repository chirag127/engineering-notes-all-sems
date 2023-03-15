### Schedulers in Hadoop Eco System and YARN

Schedulers are algorithms used to schedule tasks in a Hadoop cluster when requests are received from different clients. There are three main types of schedulers in Hadoop: FIFO (First In First Out) Scheduler, Capacity Scheduler, and Fair Scheduler .

- **FIFO Scheduler**: This scheduler processes jobs in the order they are received, with the first job submitted being the first to be processed.

- **Capacity Scheduler**: This scheduler allows multiple queues to be created, each with a guaranteed capacity. Jobs are submitted to the appropriate queue and are processed based on the queue's capacity and the job's priority.

- **Fair Scheduler**: This scheduler assigns resources to jobs in a way that ensures that all jobs get, on average, an equal share of resources over time. It can be configured to balance the needs of multiple users and groups.

YARN (Yet Another Resource Negotiator) is a core component of the Hadoop ecosystem and is responsible for resource management. It significantly expanded Hadoop's potential uses by separating the Hadoop Distributed File System (HDFS) from the batch-oriented MapReduce programming framework and processing engine, which also functioned as the big data platform's resource manager and job scheduler  .

YARN has three built-in schedulers: the FIFO, Fair, and Capacity Scheduler. These schedulers provide users with different methods to allocate resources of a Hadoop cluster to execute their MapReduce jobs, but they do not guarantee that their jobs will be executed within a specific deadline .