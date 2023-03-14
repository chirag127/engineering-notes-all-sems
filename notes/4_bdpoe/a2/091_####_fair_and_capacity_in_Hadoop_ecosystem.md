 Here is the content in markdown format for the topic #### fair and capacity in Hadoop ecosystem:

#### Fair and Capacity in Hadoop Ecosystem

- **Fair Scheduler**: The Fair Scheduler is a Hadoop scheduler that aims for fair sharing of cluster resources among users and/or groups. It does this by computing a per-task fair share based on weights for users and groups and prioritizing tasks from under-served users/groups. The basic idea is that each job gets a fair share of resources based on its demands and its priority (set by admin). The scheduler will ideally limit any one user from monopolizing the cluster. Some benefits of Fair Scheduler are:
  - Prevent single jobs from taking over the cluster
  - Provide guaranteed capacity to certain jobs or user groups
  - Support for multi-users and multi-groups
- **Capacity Scheduler**: The Capacity Scheduler is a Hadoop scheduler that allows you to set up guaranteed minimum capacity or fair shares for users or user groups in a Hadoop cluster. Some key benefits of Capacity Scheduler are:
  - Guaranteed capacity allocation
  - Priority queues which can be regulated through weights
  - Multi-user and multi-group support
  - Fair bandwidth distribution
- **Advantages of Fair and Capacity Schedulers**:
  - Prevent starvation of jobs and ensure all get fair CPU and memory resources
  - Provide guaranteed capacity and priority to important jobs or groups
  - Support for multi-users and multi-groups in a cluster
- **Disadvantages of Fair and Capacity Schedulers**:
  - Fair sharing can lead to under-utilization of resources in some scenarios
  - Complex configurations required for fair sharing, priorities, and capacities
  - No real-time performance guarantees since scheduling is done in batches

[Additional details, diagrams, examples, etc. can be added here if required for better understanding]