#### Shuffle and sort in map reduce

- Map reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Map reduce consists of two phases: map and reduce. In the map phase, each input record is transformed into a key-value pair by a user-defined function. In the reduce phase, all the values associated with the same key are combined by another user-defined function.
- Shuffle and sort is an intermediate step between the map and reduce phases. It is responsible for transferring the output of the map tasks to the reduce tasks, and sorting them by key.
- Shuffle and sort has the following steps:
  - Partitioning: The output of each map task is partitioned into R regions, where R is the number of reduce tasks. The partitioning function is usually a hash function of the key, but it can be customized by the user.
  - Sorting: Within each partition, the key-value pairs are sorted by key. This can be done either in memory or on disk, depending on the size of the data and the available resources.
  - Merging: The sorted partitions from different map tasks are merged into a single sorted stream for each reduce task. This can be done either by pulling the data from the map tasks (pull-based shuffle) or by pushing the data to the reduce tasks (push-based shuffle).
  - Grouping: The merged stream of key-value pairs is grouped by key, so that all the values with the same key are passed to the reduce function as an iterator.