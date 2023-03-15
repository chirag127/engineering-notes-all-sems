# Shuffle and Sort for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- Shuffle and sort is the process by which the system performs the sort and transfers the map outputs to the reducers as inputs  .
- Shuffle and sort is the heart of MapReduce and is where the magic happens.
- Shuffle and sort phase in Hadoop occurs simultaneously and is done by the MapReduce framework.

## Shuffle Phase

- Shuffling is the process by which intermediate data from mappers are transferred to 0, 1 or more reducers.
- Each reducer receives 1 or more keys and its associated values depending on the number of reducers (for a balanced load).
- Shuffling involves the following steps :
  - Partitioning: The map outputs are partitioned by a partitioner function based on the key. The default partitioner is a hash function that assigns each key to a reducer in a round-robin fashion.
  - Spilling: The map outputs are buffered in memory until they reach a threshold size. Then they are spilled to the local disk in a sorted order by the key. The spilled files are merged into larger files if there are too many of them.
  - Copying: The spilled files are copied to the reducers over the network. The reducers can start copying the map outputs as soon as they are available, without waiting for all the mappers to finish. This is called the "slow start" of the reducers.
  - Merging: The reducers merge the sorted map outputs from different mappers into a single sorted stream.

## Sort Phase

- Sort phase covers the merging and sorting of map outputs.
- Data from the mapper are grouped by the key, split among reducers and sorted by the key.
- Every reducer obtains all values associated with the same key.
- Sort phase involves the following steps :
  - Grouping: The reducer groups the values by the key using a grouping comparator. The default grouping comparator is the same as the key comparator, which compares the keys by their natural order. The grouping comparator can be customized to group values by a different criterion.
  - Sorting: The reducer sorts the values by the key using a key comparator. The default key comparator is the same as the grouping comparator, which compares the keys by their natural order. The key comparator can be customized to sort values by a different criterion.
  - Reducing: The reducer applies the reduce function to each group of values with the same key and produces the final output. The output is written to the HDFS.