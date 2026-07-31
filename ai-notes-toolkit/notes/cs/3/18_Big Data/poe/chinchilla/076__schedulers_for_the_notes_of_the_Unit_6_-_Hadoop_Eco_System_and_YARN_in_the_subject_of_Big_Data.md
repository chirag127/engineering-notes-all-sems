### Schedulers

Schedulers are an important part of the Hadoop ecosystem and YARN. They are responsible for allocating resources to different applications running on the cluster. In this section, we will discuss the different types of schedulers available in Hadoop and their characteristics.

#### 1. FIFO Scheduler

The FIFO (First In First Out) scheduler is the simplest scheduler available in Hadoop. It schedules the jobs in the order they arrive. This means that the job that arrives first is scheduled first. The FIFO scheduler is suitable for small clusters with a low number of jobs.

#### 2. Capacity Scheduler

The Capacity Scheduler is a more advanced scheduler that allows for better resource allocation. It allows multiple organizations or users to share the same cluster resources. The Capacity Scheduler divides the cluster into multiple queues, and each queue is allocated a certain percentage of the cluster resources. This means that each organization or user gets a guaranteed amount of resources.

#### 3. Fair Scheduler

The Fair Scheduler is another scheduler available in Hadoop. It tries to allocate resources fairly among all the jobs running on the cluster. It does not give priority to any particular job or organization. The Fair Scheduler dynamically adjusts the resources allocated to each job based on the number of jobs running on the cluster. This means that if there are more jobs running on the cluster, each job gets a smaller share of the resources.

#### 4. Delay Scheduler

The Delay Scheduler is a scheduler that allows for jobs to be delayed by a certain amount of time before they are executed. This scheduler is useful when there are peak loads on the cluster, and the jobs can be delayed until the load on the cluster has reduced.

#### Conclusion

Schedulers are an important part of the Hadoop ecosystem and YARN. They are responsible for allocating resources to different applications running on the cluster. The different types of schedulers available in Hadoop have different characteristics and are suitable for different scenarios. It is important to choose the right scheduler based on the needs of your organization or application.