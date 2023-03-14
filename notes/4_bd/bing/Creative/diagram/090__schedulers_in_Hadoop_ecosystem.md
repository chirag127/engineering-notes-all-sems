Schedulers in Hadoop ecosystem are algorithms that allocate resources to different applications or jobs in a cluster. There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair schedulers.

#### Schedulers in Hadoop ecosystem

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   FIFO Queue    |     | Capacity Queue  |     |   Fair Queue    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Job 1 (F1)    |     |   Job 1 (C1)    |     |   Job 1 (F1)    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Job 2 (F2)    |     |   Job 2 (C2)    |     |   Job 2 (F2)    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Job 3 (F3)    |     |   Job 3 (C3)    |     |   Job 3 (F3)    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Job 4 (F4)    |     |   Job 4 (C4)    |     |   Job 4 (F4)    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Job 5 (F5)    |     |   Job 5 (C5)    |     |   Job 5 (F5)    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         |                     |                       |
         v                     v                       v
+---------------------------------------------------------------+
|                                                               |
|                        Resource Manager                       |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                        Node Manager 1                         |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                        Node Manager 2                         |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                        Node Manager 3                         |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                        Node Manager 4                         |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                        Node Manager 5                         |
|                                                               |
+---------------------------------------------------------------+
```

The FIFO scheduler executes the jobs in the order of their submission. It does not consider the priority or the size of the jobs. It is simple to execute but not suitable for shared clusters.

The Capacity scheduler allows multiple queues with different capacities and priorities. Each queue has a minimum and a maximum share of the cluster resources. The jobs in the same queue are executed in FIFO order. The Capacity scheduler can also support preemption and hierarchical queues.

The Fair scheduler assigns resources to jobs such that each job gets a fair share of the cluster over time. It can also support multiple queues with different weights and policies. The Fair scheduler can dynamically adjust the share of each job based on the demand and the availability of resources.