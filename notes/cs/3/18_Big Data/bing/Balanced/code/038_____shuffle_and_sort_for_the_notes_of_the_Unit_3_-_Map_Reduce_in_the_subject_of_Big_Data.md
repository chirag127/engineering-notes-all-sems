### Shuffle and Sort for the notes of the Unit 3 - Map Reduce in the subject of Big Data

- Shuffle and sort are two phases that occur between the map and reduce tasks in a MapReduce job.
- Shuffle is the process of transferring data from the mappers to the reducers. It involves grouping, partitioning and sorting the map outputs by their keys.
- Sort is the process of merging and sorting the map outputs by their keys. It ensures that each reducer obtains all values associated with the same key.
- Shuffle and sort are done by the MapReduce framework and are essential for the reducers to perform their computations.
- The programmer can provide custom compare functions for sorting and a partitioner for data split.

Some points to remember about shuffle and sort are:

- Shuffle and sort are done in parallel with the map and reduce tasks, not sequentially.
- Shuffle and sort can be optimized by using combiners, compression and custom partitioners.
- Shuffle and sort can be monitored by using counters and logs.
- Shuffle and sort can affect the performance and scalability of a MapReduce job.