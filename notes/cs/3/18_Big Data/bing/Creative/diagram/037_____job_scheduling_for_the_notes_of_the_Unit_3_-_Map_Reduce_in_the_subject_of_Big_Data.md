### Job Scheduling for Map Reduce

- Job scheduling is the process of assigning tasks to resources in a distributed system to achieve high performance and efficiency.
- Map Reduce is a programming model for processing large-scale data sets in parallel using a cluster of machines.
- Job scheduling for Map Reduce involves two main challenges: 
  - How to partition the input data into splits that can be processed by different mappers.
  - How to allocate the mappers and reducers to the available nodes in the cluster.
- Different job scheduling algorithms have different objectives and trade-offs, such as:
  - Data locality: the degree to which the data is processed near its source, reducing network overhead and improving performance.
  - Fairness: the degree to which the resources are shared equally among different users or jobs, ensuring quality of service and avoiding starvation.
  - Resource awareness: the degree to which the scheduler considers the heterogeneity and availability of the nodes in the cluster, maximizing resource utilization and minimizing waste.
- Some examples of job scheduling algorithms for Map Reduce are:
  - FIFO: the simplest scheduler that assigns jobs in the order of their arrival, without considering data locality or fairness.
  - Fair: a scheduler that assigns resources to jobs based on their weights and demands, ensuring that each job gets a fair share of the cluster over time.
  - Capacity: a scheduler that divides the cluster into multiple queues, each with a predefined capacity and priority, and assigns jobs to the queues based on their requirements and preferences.
  - Delay: a scheduler that delays the launch of a job until it can achieve a high degree of data locality, improving performance and reducing network traffic.
  - EFT: a scheduler that assigns resources to jobs based on their earliest finish time, considering both resource allocation and job scheduling in the cloud, optimizing the completion time and cost of the jobs.