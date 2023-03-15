#### Job Scheduling in Map Reduce

In MapReduce, job scheduling is an important aspect that determines the efficiency of the system. The following are some key points to keep in mind when it comes to job scheduling in MapReduce:

- MapReduce follows a master-slave architecture where the master node is responsible for scheduling and managing the MapReduce jobs. The master node is known as the JobTracker.
- The JobTracker maintains a queue of pending jobs and schedules them on available slave nodes known as TaskTrackers.
- The JobTracker uses a scheduling algorithm to determine which job to assign to which TaskTracker based on resource availability and job priority.
- The scheduling algorithm used by JobTracker is called the Fair Scheduler. It assigns resources equally to all jobs when there is no resource contention. When resource contention occurs, the Fair Scheduler assigns more resources to high-priority jobs and fewer resources to low-priority jobs.
- MapReduce supports two types of scheduling: FIFO and Fair Scheduler. FIFO scheduling assigns resources to jobs in the order in which they are submitted while Fair Scheduler assigns resources based on job priority and resource availability.
- MapReduce also supports speculative execution, which means if a TaskTracker is taking longer than expected to complete a task, the JobTracker can assign the same task to another TaskTracker to ensure timely completion. This helps to improve system efficiency.
- In addition to the above scheduling techniques, MapReduce also allows users to specify custom scheduling policies based on their requirements.

In conclusion, job scheduling is a crucial aspect of MapReduce that determines the overall performance of the system. The Fair Scheduler algorithm used by JobTracker ensures that high-priority jobs get the necessary resources to complete on time, while speculative execution and custom scheduling policies further optimize job completion times. Understanding these concepts is important for anyone working in the field of big data and distributed computing.