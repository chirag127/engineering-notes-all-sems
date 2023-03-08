### Schedulers

Schedulers in Hadoop YARN (Yet Another Resource Negotiator) are responsible for managing resources in a distributed environment. With the help of schedulers, we can allocate resources to different applications running on the cluster. The scheduler decides which application will get how much resource and when.

There are two types of schedulers in Hadoop YARN:

1. Capacity Scheduler - Capacity Scheduler is a pluggable scheduler that allows multiple organizations to share a large cluster. Each organization gets a guaranteed minimum capacity of the cluster, and they can use more resources if those resources are not being used by other organizations.

2. Fair Scheduler - Fair Scheduler is a pluggable scheduler that allows multiple applications to share a cluster in a fair manner. The Fair Scheduler assigns resources to applications based on their demand and fairness policies.

#### Capacity Scheduler

Capacity Scheduler is used when multiple organizations share a large Hadoop cluster. Each organization gets a guaranteed minimum capacity of the cluster, and they can use more resources if those resources are not being used by other organizations. Capacity Scheduler works on the principle of hierarchical queues. Each queue can have multiple sub-queues, and each queue has its own capacity defined in terms of memory and CPU. 

##### Advantages of Capacity Scheduler

- It ensures that each organization gets a guaranteed minimum capacity of the cluster.
- It allows organizations to use more resources if those resources are not being used by other organizations.
- It works on the principle of hierarchical queues, which makes resource allocation more manageable.

##### Disadvantages of Capacity Scheduler

- It can be complex to set up and manage.
- It can lead to underutilization of resources if organizations are not using their allocated capacity.

#### Fair Scheduler

Fair Scheduler is used when multiple applications share a cluster. It assigns resources to applications based on their demand and fairness policies. Applications are categorized based on priority, and resources are allocated fairly to each category. 

##### Advantages of Fair Scheduler

- It ensures that resources are allocated fairly to each application.
- It works on the principle of priority, which makes resource allocation more manageable.

##### Disadvantages of Fair Scheduler

- It can lead to starvation of low-priority applications if high-priority applications are using all the resources.
- It can be complex to set up and manage.

#### Implementation

The implementation of schedulers in Hadoop YARN involves the following steps:

1. Configure the schedulers in yarn-site.xml file.
2. Set the capacity and priority of queues in capacity-scheduler.xml or fair-scheduler.xml file.
3. Submit the application to the cluster.

#### Example

Let's say we have a Hadoop cluster with 100GB of memory and 10 CPUs. We have two organizations, A and B, that need to share this cluster. Organization A needs 70GB of memory and 7 CPUs, and organization B needs 30GB of memory and 3 CPUs. 

With the help of the Capacity Scheduler, we can allocate 70GB of memory and 7 CPUs to organization A and 30GB of memory and 3 CPUs to organization B. If organization A is not using its allocated capacity, organization B can use those resources.

#### Applications

Schedulers are used in Hadoop YARN to manage resources in a distributed environment. They are used in various applications, such as:

- Big Data Analytics
- Machine Learning
- Data Warehousing
- Business Intelligence

In conclusion, schedulers are an essential component of Hadoop YARN, responsible for managing resources in a distributed environment. They allow multiple organizations and applications to share a cluster in a fair and efficient manner. Capacity Scheduler is used when multiple organizations share a cluster, while Fair Scheduler is used when multiple applications share a cluster.