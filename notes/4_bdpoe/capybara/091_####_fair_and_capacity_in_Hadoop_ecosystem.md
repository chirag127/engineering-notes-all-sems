#### Fair and Capacity in Hadoop Ecosystem

Hadoop is a distributed computing system that allows processing of large data sets across clusters of computers. The Hadoop ecosystem has two important scheduling policies - Fair and Capacity. Let's discuss them in detail.

##### Fair Scheduling

Fair scheduling is a scheduling policy that allows the sharing of resources among multiple jobs in a fair and efficient manner. In Fair scheduling, all jobs are given equal share of cluster resources. If there are idle resources, they are assigned to the jobs that need them the most. This ensures that no job is starved of resources and all jobs are treated equally.

##### Capacity Scheduling

Capacity scheduling is a scheduling policy that allows administrators to allocate a certain percentage of cluster resources to specific users or groups. In Capacity scheduling, each user or group is given a fixed amount of resources, and they can use those resources as they see fit. If there are idle resources, they are not allocated to other users but are kept reserved for the specific user or group.

##### Fair vs Capacity

Both Fair and Capacity scheduling policies have their own advantages and disadvantages. Fair scheduling is more flexible and can adapt to changing workloads, but it may not be suitable for users who require guaranteed resources. Capacity scheduling, on the other hand, provides guaranteed resources to specific users, but it may lead to underutilization of resources if the user does not use all the allocated resources.

Learning Tricks:

One mnemonic that can be helpful is "Fair is for everyone, Capacity is for specific groups". This helps in remembering that Fair scheduling is for sharing resources among all jobs, while Capacity scheduling is for allocating resources to specific users or groups.

Another way to remember is by visualizing a pie chart. Fair scheduling divides the resources equally among all jobs, like a pie chart divided into equal slices. Capacity scheduling allocates resources to specific users or groups, like a pie chart with different sized slices for different users or groups.

In conclusion, both Fair and Capacity scheduling policies have their own advantages and disadvantages, and it is up to the administrators to choose the one that best fits their needs. Understanding these policies and their differences can help in making informed decisions when it comes to scheduling jobs in a Hadoop ecosystem.