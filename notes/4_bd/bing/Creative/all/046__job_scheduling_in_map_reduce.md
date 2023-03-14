#### Job scheduling in map reduce

- Job scheduling is the process of allocating tasks to different nodes in a distributed system, such as Hadoop, that uses the MapReduce framework for parallel data processing.
- Job scheduling aims to minimize the job execution time and overhead, as well as to maximize the throughput and resource utilization of the system.
- Job scheduling also tries to improve the data locality, which is the distance between the input data node and the processing node. Data locality affects the data transmission through the network and the I/O performance of the system.
- Job scheduling in MapReduce consists of six steps :
  1. Users submit jobs to a queue, and the cluster runs them in order.
  2. The master node, or the JobTracker, distributes Map tasks and Reduce tasks to different workers, or the TaskTrackers.
  3. The Map tasks read the data splits, and run the map function on the data which is read in.
  4. The Map tasks produce intermediate key-value pairs, and partition them by a hash function.
  5. The Reduce tasks fetch the intermediate key-value pairs from the Map tasks, and sort them by the key.
  6. The Reduce tasks run the reduce function on the sorted key-value pairs, and produce the final output.
- Job scheduling in MapReduce can be improved by using different algorithms or techniques, such as:
  - FIFO: The simplest scheduling algorithm that runs the jobs in the order they are submitted to the queue.
  - Delay: A scheduling algorithm that delays the scheduling of a task until a node with local data is available, or a certain timeout is reached.
  - Fair: A scheduling algorithm that assigns resources to jobs such that each job gets, on average, an equal share of resources over time.
  - Capacity: A scheduling algorithm that allows multiple queues with different capacities and guarantees, and supports priorities within each queue.
  - Learning: A scheduling algorithm that uses machine learning or reinforcement learning to select the best task for each node, based on the compatibility and resource balance of the tasks .
  - Cache: A scheduling algorithm that leverages the in-memory caching of HDFS to improve the data locality and availability of the tasks.
- Job scheduling in MapReduce has some challenges and limitations, such as:
  - The heterogeneity of the nodes and the tasks, which may affect the performance and fairness of the scheduling.
  - The unpredictability of the task execution time and the data size, which may cause load imbalance and resource wastage.
  - The scalability and fault tolerance of the scheduling algorithm, which may affect the reliability and efficiency of the system.
  - The trade-off between data locality and load balancing, which may require adaptive and dynamic scheduling strategies.

: HybSMRP: a hybrid scheduling algorithm in Hadoop MapReduce framework | Journal of Big Data | Full Text
: CLQLMRS: improving cache locality in MapReduce job scheduling using Q-learning | Journal of Cloud Computing | Full Text
: Learning Based Job Scheduling Algorithm Based On Map Reduce ... - IJERT
: MapReduce Tutorial - Apache Hadoop