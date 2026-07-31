 Here is the formal content on how Map Reduce works:

#### How Map Reduce works

1. Map Phase: In the map phase, the input data is split into chunks which are processed by multiple map tasks in parallel. Each map task processes the input chunk and produces intermediate key-value pairs.

2. Shuffling: The intermediate key-value pairs produced by the map tasks are shuffled to the reduce tasks. Pairs with the same key are sent to the same reduce task.

3. Reduce Phase: In the reduce phase, the reduce tasks process the intermediate data they received from the shuffle phase. They aggregate the values for each key and produce the final output.

The main benefits of Map Reduce are:

- It can process huge amounts of data in a scalable manner.
- It is fault tolerant as failed tasks can be re-executed.
- The intermediate data is persisted to disk, allowing the operation to be resumed in case of failures.
- It automatically parallelizes the processing by splitting the input, processing it in parallel and aggregating the results.
- The programmer only needs to specify the map and reduce functions, and the infrastructure handles parallelization, fault-tolerance, etc.

The key points to note are:

1. The input data is split into chunks which are processed in parallel by multiple map tasks.
2. The intermediate outputs from the map phase are shuffled to be sent to the appropriate reduce tasks.
3. The reduce tasks aggregate the intermediate data and produce the final output.
4. Map Reduce is scalable, fault tolerant and automatically parallelizes the processing across multiple nodes.