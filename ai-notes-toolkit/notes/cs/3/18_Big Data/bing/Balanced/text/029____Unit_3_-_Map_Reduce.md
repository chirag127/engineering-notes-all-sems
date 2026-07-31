## Unit 3 - Map Reduce

- MapReduce is a programming paradigm that runs in the background of Hadoop to provide scalability and easy data-processing solutions.
- MapReduce is designed for processing large volumes of data in parallel by dividing the work into a set of independent tasks.
- MapReduce consists of two phases: Map and Reduce.
  - Map phase: The input data is split into chunks and assigned to different map tasks. Each map task reads the input data, applies a user-defined function, and emits a set of key-value pairs as intermediate output.
  - Reduce phase: The intermediate output is shuffled and sorted by key and assigned to different reduce tasks. Each reduce task reads the key-value pairs, applies another user-defined function, and produces the final output.
- MapReduce framework consists of a single master JobTracker and one slave TaskTracker per cluster-node. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks. The slaves execute the tasks as directed by the master.
- MapReduce provides fault-tolerance, load-balancing, data locality, and scalability features for large-scale data processing.