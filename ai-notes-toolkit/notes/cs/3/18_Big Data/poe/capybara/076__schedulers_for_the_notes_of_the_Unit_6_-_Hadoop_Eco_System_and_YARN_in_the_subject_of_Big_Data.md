### Schedulers for Hadoop Eco System and YARN

Schedulers play a crucial role in managing resources in Hadoop Eco System and YARN. They control the allocation of resources to different applications and ensure that all applications receive the required resources to complete their tasks. Here are some of the popular schedulers used in Hadoop Eco System and YARN:

1. FIFO Scheduler:
The First In, First Out (FIFO) Scheduler is the simplest scheduler in Hadoop Eco System and YARN. It schedules the jobs in the order in which they are submitted to the system. It is suitable for use cases where there is no need for prioritizing jobs and all jobs have equal importance.

2. Capacity Scheduler:
The Capacity Scheduler is a more advanced scheduler that allows multiple applications to share a cluster without any conflicts. It allocates resources based on the configured capacities and priorities of the applications. It is useful in multi-tenant environments where different users or groups may have varying resource requirements.

3. Fair Scheduler:
The Fair Scheduler is another popular scheduler that allows the sharing of resources between multiple applications in a fair and equal manner. It allocates resources based on the demand of the applications and their priority levels. It is useful in a shared environment where resources need to be allocated fairly among different users or groups.

4. Dominant Resource Fairness (DRF) Scheduler:
The Dominant Resource Fairness (DRF) Scheduler is another advanced scheduler that is used to allocate resources in a multi-tenant environment. It allocates resources based on the dominant resource of the application. For example, if an application requires more CPU resources than memory, the DRF Scheduler will allocate more CPU resources to that application. It is useful in environments where applications have varying resource requirements.

In conclusion, schedulers are an important component of Hadoop Eco System and YARN. They help manage resources effectively and ensure that all applications receive the required resources to complete their tasks. The choice of scheduler depends on the specific use case and the requirements of the applications.