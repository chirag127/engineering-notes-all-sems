

#### Job Scheduling in Map Reduce

1. Map Reduce is a programming model used for processing and generating large datasets. It is based on the concept of dividing a task into smaller ones, which are then executed in parallel on multiple machines.

2. Job scheduling is the process of allocating resources to tasks in order to meet the requirements of the application. It is a critical component of Map Reduce, as it determines the order in which tasks are executed.

3. In Map Reduce, job scheduling is based on a priority system. Tasks with higher priority are given precedence over those with lower priority. This ensures that the most important tasks are completed first.

4. The scheduling algorithm used in Map Reduce is known as the Fair Scheduler. This algorithm takes into account the size of the task and the resources available on the cluster when making scheduling decisions.

5. The Fair Scheduler also takes into account the amount of time that has elapsed since the task was submitted. This ensures that tasks that have been waiting for a long time are given priority over those that have just been submitted.

6. In addition to the Fair Scheduler, Map Reduce also supports other scheduling algorithms such as the Capacity Scheduler and the FIFO Scheduler. These algorithms can be used to optimize the performance of the system, depending on the requirements of the application.

7. Finally, Map Reduce also supports job scheduling policies such as preemption, which allows tasks to be interrupted if they are taking too long to complete. This ensures that tasks with higher priority are given precedence over those with lower priority.