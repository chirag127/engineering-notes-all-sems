#### Job scheduling in MapReduce

- Job scheduling is the process of assigning tasks to workers in a MapReduce cluster, in order to optimize the performance and resource utilization of the system.
- Job scheduling involves six steps:
  - Users submit jobs to a queue, and the cluster runs them in order.
  - Master node distributes Map tasks and Reduce tasks to different workers.
  - Map tasks read the data splits, and run map function on the data which is read in.
  - Map tasks produce intermediate key-value pairs, and partition them by a hash function.
  - Reduce tasks fetch the intermediate data from the Map tasks, and sort them by key.
  - Reduce tasks run reduce function on the sorted data, and write the output to the file system.
- Job scheduling can be done by different algorithms, such as FIFO, Fair, Capacity, Delay, and Learning based  .
  - FIFO (First In First Out) scheduler runs the jobs in the order of submission, and assigns a fixed number of map and reduce slots to each job. It is simple and easy to implement, but it can cause starvation and poor resource utilization for large or small jobs.
  - Fair scheduler assigns tasks to jobs such that each job gets an equal share of resources over time. It can also support priorities and pools to allocate resources to different users or groups. It is more flexible and fair than FIFO, but it can increase the network overhead and reduce the data locality.
  - Capacity scheduler is similar to Fair scheduler, but it allows multiple queues with different capacities and guarantees. It can also support preemption and hierarchical queues to improve resource utilization and fairness. It is suitable for multi-tenant environments, but it can be complex to configure and manage.
  - Delay scheduler is an optimization of Fair scheduler, which delays the assignment of tasks to nodes that do not have local data, in order to increase the data locality. It can improve the performance and reduce the network traffic, but it can also increase the scheduling latency and complexity.
  - Learning based scheduler is a data driven approach that tries to allocate a task to a node if the incoming task does not affect the tasks already running on that node. It uses machine learning techniques to learn the compatibility of different types of tasks, and tries to find a good mix of jobs for each worker node. It can reduce the overall runtime of the jobs, but it can also require more training data and computation.
- Job scheduling can affect the performance and resource utilization of the MapReduce system, and it is important to choose a suitable algorithm for different scenarios and requirements.