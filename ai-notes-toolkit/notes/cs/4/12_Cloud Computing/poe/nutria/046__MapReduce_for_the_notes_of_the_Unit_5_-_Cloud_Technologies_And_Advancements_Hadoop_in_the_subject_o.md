

### MapReduce for the Notes of Unit 5 - Cloud Technologies and Advancements Hadoop in the Subject of Cloud Computing

1. MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
2. It is a framework for writing applications that process vast amounts of data in-parallel on large clusters of commodity hardware in a reliable and fault-tolerant manner.
3. MapReduce was designed to scale up from single servers to thousands of machines, each offering local computation and storage.
4. The MapReduce framework consists of a single master JobTracker and one or more slaves TaskTracker nodes.
5. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks.
6. The slaves execute the tasks as directed by the master and provide task-status information to the master.
7. The MapReduce programming model is based on the "divide and conquer" method.
8. It divides the input data-set into independent chunks which are processed by the map tasks in a completely parallel manner.
9. The results of all the map tasks are then sorted and shuffled to the reduce tasks.
10. The reduce task then performs a summary operation on the output from the map tasks and produces the final output.