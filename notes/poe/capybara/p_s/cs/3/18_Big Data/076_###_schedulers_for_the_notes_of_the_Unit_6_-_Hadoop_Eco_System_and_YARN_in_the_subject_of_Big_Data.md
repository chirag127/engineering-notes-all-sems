### Schedulers for the Notes of Unit 6 - Hadoop Eco System and YARN in the Subject of Big Data

Schedulers play a significant role in the Hadoop Eco System and YARN. A scheduler is responsible for allocating resources to different applications running on a cluster. The main objective of the scheduler is to maximize the utilization of cluster resources while maintaining fairness among different applications.

There are three types of schedulers in YARN:

1. Capacity Scheduler:
   - It is a hierarchical scheduler that allows sharing of cluster resources among a number of different queues.
   - Each queue has a configured capacity of resources that can be used by applications.
   - The available resources are shared among the queues based on their configured capacity.
   - When a new application is submitted, it is assigned to a queue based on the user or the application's characteristics.
   - The capacity scheduler is suitable for environments where there are multiple users sharing the cluster.

2. Fair Scheduler:
   - It is a simple and fair scheduler that allows sharing of cluster resources among different applications.
   - It works on the principle of fair share allocation, where each application gets an equal share of resources.
   - If there are idle resources, they are allocated to the applications that need them the most.
   - The fair scheduler is suitable for environments where there is a mix of long-running and short-running applications.

3. Fifo Scheduler:
   - It is a simple scheduler that schedules applications on a first-come-first-serve basis.
   - The applications are executed in the order of their submission time.
   - The Fifo scheduler is suitable for environments where there is a single user or a small group of users.

Advantages of schedulers in Hadoop Eco System and YARN:
- They ensure that the resources of the cluster are utilized effectively.
- They ensure that each application gets its fair share of resources.
- They prioritize the applications based on their importance.
- They prevent any one application from monopolizing the resources of the cluster.

Disadvantages of schedulers in Hadoop Eco System and YARN:
- They can be complex to configure and manage.
- They can lead to contention for resources if the cluster is not properly managed.

Examples of schedulers in Hadoop Eco System and YARN:
- Capacity scheduler is used in Yahoo, Facebook, and LinkedIn.
- Fair scheduler is used in Hadoop, Spark, and Hive.
- Fifo scheduler is used in smaller clusters with a single user or a small group of users.

Applications of schedulers in Hadoop Eco System and YARN:
- They are used in large-scale data processing applications where there are multiple users sharing the same cluster.
- They are used in real-time data processing applications where there is a need for efficient resource allocation. 

Overall, schedulers are an integral part of Hadoop Eco System and YARN. They ensure that cluster resources are used effectively and efficiently while maintaining fairness among different applications.