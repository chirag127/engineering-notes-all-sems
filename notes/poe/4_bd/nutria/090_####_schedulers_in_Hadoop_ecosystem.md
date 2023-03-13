

### Schedulers in Hadoop Ecosystem

* **FIFO Scheduler**: FIFO (First In First Out) Scheduler is the default scheduler in Hadoop. It treats all jobs equally and executes them in the order in which they were submitted. It is suitable for short jobs and does not support job priorities.

* **Fair Scheduler**: Fair Scheduler is an advanced Hadoop scheduler that allocates resources to jobs based on predefined rules. It supports job priorities, allows jobs to be grouped into pools, and provides a mechanism for sharing resources across pools.

* **Capacity Scheduler**: Capacity Scheduler is used to manage large clusters and provides a mechanism for sharing resources among multiple organizations. It allows administrators to specify minimum and maximum resource allocations for each organization, and it also supports job priorities.

* **Delay Scheduler**: Delay Scheduler is a specialized scheduler that can be used to delay the execution of certain jobs. It can be used to ensure that jobs are not executed until certain conditions are met, such as a certain amount of free disk space being available.

* **Mesos Scheduler**: Mesos Scheduler is a distributed resource manager for Hadoop clusters. It allows administrators to manage resources across multiple clusters and supports job priorities and resource sharing.