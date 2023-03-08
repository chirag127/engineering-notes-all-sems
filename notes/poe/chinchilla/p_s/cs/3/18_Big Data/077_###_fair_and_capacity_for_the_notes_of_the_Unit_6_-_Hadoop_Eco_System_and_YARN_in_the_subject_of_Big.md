### Fair and Capacity

In Hadoop, Fair and Capacity Scheduler are two important Scheduler algorithms used for scheduling jobs in a Hadoop cluster. These schedulers are used by YARN (Yet Another Resource Negotiator) to allocate resources to different applications running on a Hadoop cluster.

#### Capacity Scheduler

The Capacity Scheduler is a simple and easy-to-use scheduler that provides capacity guarantees. It ensures that each organization or user of the cluster gets a certain percentage of the cluster resources. The Capacity Scheduler divides the cluster resources into queues, and each queue is assigned a certain percentage of the cluster resources. 

##### Advantages of Capacity Scheduler
- Provides guaranteed capacity for each organization or user.
- The resources are allocated based on the percentage of resources allocated to each queue.
- The Capacity Scheduler is easy to set up and configure.

##### Disadvantages of Capacity Scheduler
- It is not very flexible when it comes to handling multiple jobs with varying resource requirements.
- It does not provide any support for sharing resources between queues.

#### Fair Scheduler

The Fair Scheduler is designed to provide fair sharing of cluster resources between different applications. It allocates resources to different applications based on the current workload of the cluster. The Fair Scheduler schedules jobs based on the priority of the job and how long the job has been waiting in the queue.

##### Advantages of Fair Scheduler
- Provides fair sharing of resources between different applications.
- The Fair Scheduler is very flexible and can handle multiple jobs with varying resource requirements.
- It supports sharing resources between queues.

##### Disadvantages of Fair Scheduler
- It does not provide guaranteed capacity for each organization or user.
- The Fair Scheduler is more complex to set up and configure than the Capacity Scheduler.

#### Example

Suppose there are two organizations that are using the same Hadoop cluster, and each organization has its own queue. The Capacity Scheduler will ensure that each organization gets a certain percentage of the cluster resources. For example, if Organization A has been allocated 60% of the cluster resources and Organization B has been allocated 40% of the cluster resources, then the Capacity Scheduler will ensure that each organization gets the resources they have been allocated.

On the other hand, the Fair Scheduler will allocate resources based on the current workload of the cluster. If Organization A has submitted a job that requires a lot of resources, then the Fair Scheduler will allocate more resources to that job, even if it means that Organization B will have to wait longer for their job to start.

#### Conclusion

In conclusion, both the Fair and Capacity Scheduler are important schedulers used in Hadoop to allocate resources to different applications running on a Hadoop cluster. The choice of scheduler depends on the specific requirements of the organization or user. The Capacity Scheduler is ideal for organizations that require guaranteed capacity, while the Fair Scheduler is better suited for organizations that require fair sharing of resources between different applications.