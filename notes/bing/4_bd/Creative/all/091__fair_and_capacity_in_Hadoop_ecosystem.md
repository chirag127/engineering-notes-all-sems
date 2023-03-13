#### Fair and Capacity in Hadoop Ecosystem

- Fair and Capacity are two types of schedulers in Hadoop YARN that are responsible for assigning resources to the applications submitted by users .
- A scheduler is a kind of algorithm that we use to schedule tasks in a Hadoop cluster when we receive requests from different-different clients.
- The main difference between Fair and Capacity schedulers is how they balance the resources among the applications and the users.

##### Fair Scheduler
- Fair Scheduler allows YARN applications to justly share resources in large Hadoop clusters.
- With this scheduler, there is no need for reserving a set amount of capacity because it will dynamically balance resources between all running applications.
- Fair Scheduler supports hierarchical queues, which can have different scheduling policies, such as FIFO, fair sharing, or DRF (dominant resource fairness).
- Fair Scheduler also supports preemption, which means that it can reclaim resources from some applications if they are using more than their fair share and give them to other applications that are under-served.
- Fair Scheduler can be configured by using a file called fair-scheduler.xml, which defines the queues, their weights, minimum and maximum shares, and other properties.

##### Capacity Scheduler
- Capacity Scheduler is designed to run Hadoop applications as a shared, multi-tenant cluster in an operator-friendly manner while maximizing the throughput and the utilization of the cluster.
- With this scheduler, the available resources in the Hadoop cluster are partitioned among multiple organizations who collectively fund the cluster based on computing needs.
- Capacity Scheduler supports multiple queues, each of which is guaranteed a minimum share of the cluster capacity.
- Capacity Scheduler also supports elasticity, which means that an organization can access any excess capacity not being used by others.
- Capacity Scheduler can be configured by using a file called capacity-scheduler.xml, which defines the queues, their capacities, ACLs, and other properties.

##### Mnemonics and Learning Tricks
- A possible mnemonic to remember the difference between Fair and Capacity schedulers is: **F**air **F**or **A**ll, **C**apacity for **C**ompanies.
- A possible learning trick to understand the concept of preemption in Fair Scheduler is to imagine a classroom where the teacher distributes candies to the students based on their performance. If some students get more candies than their fair share, the teacher can take some candies from them and give them to other students who deserve more.
- A possible learning trick to understand the concept of elasticity in Capacity Scheduler is to imagine a hotel where the rooms are allocated to different groups of guests based on their reservation. If some rooms are vacant, the hotel can allow some guests to use them temporarily until they are occupied by other guests who have booked them.