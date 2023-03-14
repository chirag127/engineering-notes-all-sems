Fair and capacity are two types of schedulers in Hadoop ecosystem that are used to allocate resources to different applications or jobs. A scheduler is a component of the resource manager that decides how to assign resources to applications based on some criteria.

The capacity scheduler allows multiple tenants to share a large cluster while giving each tenant a minimum capacity guarantee. The cluster resources are partitioned into multiple queues, each with a certain capacity. Each queue can have sub-queues and different priorities. The capacity scheduler tries to simulate a separate FIFO/priority cluster for each queue, rather than performing fair sharing between all jobs. The capacity scheduler also supports configuring a wait time on each queue after which it is allowed to preempt other queues’ tasks if it is below its fair share.

The fair scheduler is a method of assigning resources to jobs such that all jobs get, on average, an equal share of resources over time. When there is a single job running, that job uses the entire cluster. When other jobs are submitted, tasks slots that free up are assigned to the new jobs, so that each job gets roughly the same amount of CPU time. The fair scheduler also supports job priorities, pools, and preemption .

The following diagram illustrates the basic architecture of a fair and capacity scheduler in Hadoop ecosystem using ASCII art:

```
+-----------------+      +-----------------+
|                 |      |                 |
|    Job Queue    |      |    Job Queue    |
|                 |      |                 |
+-----------------+      +-----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         v                       v
+-----------------+      +-----------------+
|                 |      |                 |
|  Fair Scheduler |      | Capacity        |
|                 |      | Scheduler       |
|                 |      |                 |
+-----------------+      +-----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         v                       v
+-----------------+      +-----------------+
|                 |      |                 |
|  Resource       |      |  Resource       |
|  Manager        |      |  Manager        |
|                 |      |                 |
+-----------------+      +-----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         v                       v
+-----------------+      +-----------------+
|                 |      |                 |
|  Node Manager   |      |  Node Manager   |
|                 |      |                 |
+-----------------+      +-----------------+
```