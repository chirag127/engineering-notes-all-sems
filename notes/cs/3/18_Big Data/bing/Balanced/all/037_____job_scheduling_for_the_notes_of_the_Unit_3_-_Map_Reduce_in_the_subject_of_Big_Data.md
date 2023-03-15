# Job Scheduling in MapReduce

- Job scheduling is the process of assigning tasks to workers in a distributed system, such as a Hadoop cluster, to process large-scale data in parallel using the MapReduce framework.
- Job scheduling aims to optimize the performance of the system by minimizing the execution time, maximizing the resource utilization, and balancing the workload among the workers .
- Job scheduling in MapReduce involves six steps:
  - Users submit jobs to a queue, and the cluster runs them in order.
  - Master node distributes Map tasks and Reduce tasks to different workers.
  - Map tasks read the data splits, and run map function on the data which is read in.
  - Map tasks produce intermediate key-value pairs, and partition them by a hash function.
  - Reduce tasks fetch the intermediate key-value pairs from the Map tasks, and sort them by key.
  - Reduce tasks run reduce function on the sorted key-value pairs, and write the output to the file system.
- Job scheduling in MapReduce can be classified into two types: static and dynamic.
  - Static scheduling assigns tasks to workers based on predefined rules or policies, such as FIFO, Fair, or Capacity.
  - Dynamic scheduling assigns tasks to workers based on runtime information, such as data locality, resource availability, or task compatibility .
- Job scheduling in MapReduce can be improved by using various techniques, such as:
  - Learning based scheduling, which uses machine learning algorithms to predict the best mix of tasks for each worker node.
  - Cache locality based scheduling, which exploits the data cached in the worker nodes to reduce data transmission and disk I/O.
  - Speculative execution, which launches backup tasks for slow or failed tasks to reduce the straggler effect.