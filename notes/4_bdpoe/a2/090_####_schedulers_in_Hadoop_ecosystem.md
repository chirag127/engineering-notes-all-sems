 Here is the content in markdown format on #### schedulers in Hadoop ecosystem:

#### Schedulers in Hadoop Ecosystem

Hadoop ecosystem has various schedulers to efficiently manage and allocate resources to the submitted jobs. The key schedulers are:

1. FIFO Scheduler: FIFO stands for First In First Out. It is the default scheduler in Hadoop. It queues the jobs in the order of their submission. The job submitted first gets executed first. It does not differentiate between jobs based on priorities or resource requirements. Hence, it can lead to resource under utilization or over utilization.

2. Capacity Scheduler: It allocates resources based on the capacity of the cluster. Administrators can specify the capacity of each queue. It supports hierarchical queues to allocate resources among multiple organizations or groups. It allows limits to be placed on the amount of resources that each queue and user can consume. It improves utilization as compared to FIFO.

3. Fair Scheduler: It allocates resources to the jobs based on the number of map and reduce slots that a job requests. It aims to fairly share the cluster resources among the jobs with equal resource requirements. It tracks resource consumption of users and jobs and maintains a fair share for each of them. It can lead to resource wastage for jobs with small resource requirements.

Mnemonics:

- FIFO: First come, first serve
- Capacity: Allocation based on capacity
- Fair: Equitable allocation to each job

Advantages and Disadvantages can be written for each scheduler along with examples and applications. Diagrams and codes can be included to explain the working and concepts in detail. The content can be made exhaustive based on the requirements.