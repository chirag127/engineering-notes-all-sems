 Here is the content in markdown format on how Map Reduce works:

#### How Map Reduce works

Map Reduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It works in two phases:

**Map phase:** The master node takes the input, partitions it into smaller sub-problems, and distributes them to worker nodes. Each worker node processes its sub-problem(s) independently and produces a set of intermediate key-value pairs.

**Reduce phase:** The worker nodes then shuffle and redistribute the intermediate data, grouping them by the intermediate keys. The master node passes each group to a reduce worker node to produce the final output.

Some key points to remember:

- The input is split into multiple splits which are processed by the map tasks in parallel.
- The outputs of the map tasks are sorted and shuffled to be sent to the reduce tasks.
- The reduce tasks then perform the reduction operation on the values associated with the same key.
- The final output is consolidated from the reduce tasks.

The advantages of Map Reduce are:

- It is fault tolerant. If a node fails, the job is re-executed on another node.
- It is scalable. More nodes can be added to the cluster to process larger data sets.
- It is efficient. The work is distributed and parallelized leading to faster processing.

Common applications of Map Reduce include:

- Counting occurrence of words in a document
- Sorting and aggregating data
- Joining and merging data sets
- Clustering and classification algorithms

[Detailed diagrams and examples can be added here for better understanding.]

The key Mnemonics to remember are:

- Map -> Break down into parts
- Shuffle -> Redistribute and sort
- Reduce -> Aggregate and consolidate

Hope this helps you learn Map Reduce thoroughly! Let me know if you would like me to explain anything in more detail.