
#### Job Scheduling in Map Reduce

* Map Reduce is a programming model used for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
* Job scheduling is the process of allocating resources to tasks in order to optimize the completion time of the tasks.
* In Map Reduce, job scheduling involves scheduling the tasks (map and reduce jobs) to be executed on the nodes of a cluster.
* Job scheduling algorithms can be divided into two categories: static and dynamic.
  * Static scheduling algorithms assign tasks to nodes without considering the available resources or the completion time of the tasks.
  * Dynamic scheduling algorithms assign tasks to nodes based on the available resources and the completion time of the tasks.
* Static scheduling algorithms include:
  * First-Come-First-Served (FCFS): Tasks are assigned to nodes in the order they are received.
  * Shortest Job First (SJF): Tasks are assigned to nodes based on their completion time.
* Dynamic scheduling algorithms include:
  * Earliest Deadline First (EDF): Tasks are assigned to nodes based on their deadlines.
  * Least Laxity First (LLF): Tasks are assigned to nodes based on their remaining time.
* Map Reduce job scheduling algorithms can also be divided into two categories: centralized and decentralized.
  * Centralized scheduling algorithms assign tasks to nodes from a centralized location.
  * Decentralized scheduling algorithms assign tasks to nodes from a distributed location.
* Common centralized scheduling algorithms include:
  * Capacity Scheduling: Tasks are assigned to nodes based on their capacity.
  * Load Balancing: Tasks are assigned to nodes to balance the load across the cluster.
* Common decentralized scheduling algorithms include:
  * Backfilling: Tasks are assigned to nodes based on their completion time.
  * Locality-Aware Scheduling: Tasks are assigned to nodes based on their proximity to other nodes.
* Map Reduce job scheduling algorithms can also be divided into two categories: deterministic and non-deterministic.
  * Deterministic scheduling algorithms assign tasks to nodes based on predetermined parameters.
  * Non-deterministic scheduling algorithms assign tasks to nodes based on probabilistic parameters.
* Common deterministic scheduling algorithms include:
  * Priority Scheduling: Tasks are assigned to nodes based on their priority.
  * Round Robin Scheduling: Tasks are assigned to nodes in a cyclic order.
* Common non-deterministic scheduling algorithms include:
  * Random Scheduling: Tasks are assigned to nodes randomly.
  * Stochastic Scheduling: Tasks are assigned to nodes based on their probability of completion.

*In summary, job scheduling in Map Reduce involves assigning tasks to nodes in a cluster in order to optimize the completion time of the tasks. Job scheduling algorithms can be divided into two categories: static and dynamic. Static scheduling algorithms assign tasks to nodes without considering the available resources or the completion time of the tasks. Dynamic scheduling algorithms assign tasks to nodes based on the available resources and the completion time of the tasks. Map Reduce job scheduling algorithms can also be divided into two categories: centralized and decentralized. Centralized scheduling algorithms assign tasks to nodes from a centralized location, while decentralized scheduling algorithms assign tasks to nodes from a distributed location. Finally, Map Reduce job scheduling algorithms can also be divided into two categories: deterministic and non-deterministic. Deterministic scheduling algorithms assign tasks to nodes based on predetermined parameters, while non-deterministic scheduling algorithms assign tasks to nodes based on probabilistic parameters.