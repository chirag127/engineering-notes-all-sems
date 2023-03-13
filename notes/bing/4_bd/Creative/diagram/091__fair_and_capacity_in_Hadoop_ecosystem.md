Fair and capacity are two types of schedulers in Hadoop that manage the allocation of resources to different applications running on a cluster. A scheduler is a component of the resource manager that decides how to assign resources to applications based on some criteria.

The fair scheduler allows applications to share resources fairly, meaning that each application gets an equal share of resources over time. The fair scheduler can also support hierarchical queues, weights, and preemption to handle different priorities and demands of applications.

The capacity scheduler allows applications to be grouped into queues, each with a fixed percentage of the cluster capacity. The capacity scheduler can also support hierarchical queues, minimum and maximum capacities, and preemption to handle different priorities and demands of applications.

The following diagram illustrates the basic architecture of a fair and capacity scheduler in Hadoop using ASCII characters:

```
+-----------------+      +-----------------+
|                 |      |                 |
|  Application 1  |      |  Application 2  |
|                 |      |                 |
+-----------------+      +-----------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
+-----------------+      +-----------------+
|                 |      |                 |
|     Queue 1     |      |     Queue 2     |
|                 |      |                 |
+-----------------+      +-----------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
+-----------------+      +-----------------+
|                 |      |                 |
|  Resource Pool  |      |  Resource Pool  |
|                 |      |                 |
+-----------------+      +-----------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
+-----------------+      +-----------------+
|                 |      |                 |
|  Fair Scheduler |      |Capacity Scheduler|
|                 |      |                 |
+-----------------+      +-----------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
+-----------------+      +-----------------+
|                 |      |                 |
|  Resource       |      |  Resource       |
|  Manager        |      |  Manager        |
|                 |      |                 |
+-----------------+      +-----------------+
```