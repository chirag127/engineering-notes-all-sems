#### Job Scheduling in Map Reduce

In a MapReduce system, the scheduling of jobs is a crucial task that needs to be performed efficiently. The following are the points related to job scheduling in MapReduce:

1. MapReduce job scheduler is responsible for assigning tasks to the available TaskTrackers in the cluster.
2. The scheduler considers various factors while scheduling the jobs such as data locality, resource availability, and job priority.
3. Data locality is an important factor that determines the efficiency of job scheduling. The scheduler tries to assign tasks to the TaskTrackers that are closer to the data, to minimize the network transfer time.
4. The scheduler also considers the availability of resources such as CPU, memory, and disk space while scheduling the jobs. It makes sure that the resources are utilized efficiently.
5. Job priority is another factor that determines the order in which jobs are scheduled. The scheduler considers the priority of the jobs and assigns higher priority jobs first.
6. MapReduce system provides two types of schedulers: the default FIFO scheduler and the Capacity Scheduler.
7. The FIFO scheduler schedules the jobs in the order in which they are submitted. The jobs are executed in a first-come, first-served basis.
8. The Capacity Scheduler is a more advanced scheduler that provides guaranteed capacity to each user or group of users. It allows multiple users to share a cluster and provides a fair allocation of resources to each user.
9. In addition to the default and Capacity scheduler, MapReduce also supports other schedulers such as Fair Scheduler and Deadline Scheduler.
10. The Fair Scheduler is a scheduler that provides fairness to all jobs regardless of their priority. It allocates resources to each job based on its fair share.
11. The Deadline Scheduler is a scheduler that schedules jobs based on their deadline. The scheduler makes sure that jobs with earlier deadlines are executed first.

In conclusion, job scheduling is an important task in a MapReduce system. The scheduler considers various factors such as data locality, resource availability, and job priority while scheduling the jobs. MapReduce provides different types of schedulers that can be used based on the requirements of the system.