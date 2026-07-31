Job scheduling in MapReduce is the process of assigning tasks to different workers in a cluster, based on the input data, the available resources, and the desired performance. Job scheduling in MapReduce involves six steps:

1. Users submit jobs to a queue, and the cluster runs them in order.
2. Master node distributes Map tasks and Reduce tasks to different workers.
3. Map tasks read the data splits, and run map function on the data which is read in.
4. Map tasks produce intermediate key-value pairs, and partition them by a hash function.
5. Reduce tasks fetch the intermediate key-value pairs from the Map tasks, and sort them by key.
6. Reduce tasks run reduce function on the sorted key-value pairs, and produce the final output.

A possible ASCII diagram for job scheduling in MapReduce is:

#### Job scheduling in MapReduce

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|    Job Queue   |       |   Master Node  |       |   Worker Node  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |----------------------->| Map Task
      |                        |                        | Read Data Split
      |                        |                        | Run Map Function
      |                        |                        | Produce Key-Value Pairs
      |                        |                        | Partition by Hash Function
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |<-----------------------| Map Task Done
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |----------------------->| Reduce Task
      |                        |                        | Fetch Key-Value Pairs
      |                        |                        | Sort by Key
      |                        |                        | Run Reduce Function
      |                        |                        | Produce Final Output
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |<-----------------------| Reduce Task Done
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |<-----------------------| Job Done               |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|    Job Queue   |       |   Master Node  |       |   Worker Node  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```