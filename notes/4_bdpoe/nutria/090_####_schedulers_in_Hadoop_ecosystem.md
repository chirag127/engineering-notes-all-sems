

# Schedulers in Hadoop Ecosystem

Hadoop is an open-source software framework for distributed storage and distributed processing of large datasets on computer clusters built from commodity hardware. The Hadoop ecosystem consists of several components, including schedulers, which are responsible for resource management and job scheduling.

## FIFO Scheduler

The FIFO (First In First Out) scheduler is the default scheduler in Hadoop. It schedules jobs in the order they are submitted, with no priority assigned to any particular job. The advantage of this scheduler is its simplicity, but the disadvantage is that it does not prioritize jobs based on any criteria.

## Fair Scheduler

The Fair Scheduler is a more advanced scheduler that attempts to allocate resources fairly among all applications. It allows users to define pools of jobs, each with its own priority, and it allocates resources based on the priority of the pool. This allows for better resource utilization and job throughput.

## Capacity Scheduler

The Capacity Scheduler is similar to the Fair Scheduler, but it is designed to run on large clusters with thousands of nodes. It allows users to define queues and assign resources to those queues. It also allows for preemption, which allows jobs with higher priority to preempt jobs with lower priority.

## Other Schedulers

There are other schedulers available in the Hadoop ecosystem, such as the Delay Scheduler, the Fair Call Scheduler, and the Gridmix Scheduler. Each of these schedulers has its own advantages and disadvantages, and they may be more suitable for certain types of workloads than others.