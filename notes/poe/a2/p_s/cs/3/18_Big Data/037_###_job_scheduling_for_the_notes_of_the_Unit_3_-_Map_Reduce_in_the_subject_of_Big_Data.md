 Here is the content in markdown format for the topic - Job Scheduling for MapReduce:

### Job Scheduling for MapReduce

MapReduce jobs are divided into two phases - Map and Reduce. The framework schedules these jobs in an efficient manner to utilize the cluster resources optimally:

1. Map Phase:
- The input data is split into multiple splits based on the number of mappers.
- These splits are scheduled on the nodes in the cluster to execute the map tasks in parallel.
- The framework tries to schedule the map tasks on the nodes holding the data to minimize the data transfer overhead.
- If all the nodes are busy, the framework waits for a node to get free and then schedules the task on it.

2. Shuffle and Sort Phase:
- The output of the map tasks is shuffled and sorted to group the intermediate keys.
- This phase is managed by the framework itself. It transfers the intermediate data from mappers to reducers.

3. Reduce Phase:
- The framework schedules the reduce tasks on the nodes in the cluster.
- The reduce inputs are fetched from the nodes holding the intermediate data to minimize the data transfer overhead.
- If the reducers cannot fetch the inputs fast enough, the framework replicates the data on multiple nodes to load balance.

The framework tries to schedule the tasks efficiently to minimize the job execution time. It handles aspects like data locality, load balancing, fault tolerance, speculative execution, etc. internally to utilize the cluster resources optimally.

The diagram below shows the high-level flow of a MapReduce job and how the jobs are scheduled on a cluster:

[Diagram showing the flow of a MapReduce job with the two phases and scheduling of tasks on the cluster nodes]

Advantages:
...

Disadvantages:
...

Applications:
...

Examples:
...