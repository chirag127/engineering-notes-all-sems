### Shuffle and Sort for the notes of the Unit 3 - Map Reduce in the subject of Big Data

- Shuffle and sort are two phases that occur between the map and reduce tasks in a MapReduce job.
- The purpose of shuffle and sort is to transfer the map outputs to the reducers as inputs, while grouping and ordering them by key.
- Shuffle and sort happen simultaneously and are done by the MapReduce framework.

#### Shuffle
- Shuffle is the process of transferring data from the mappers to the reducers.
- Shuffle involves copying, merging, and partitioning the map outputs.
- Copying: The map outputs are stored in the local disk of the mapper nodes. The reducers fetch the map outputs from the mappers over the network.
- Merging: The map outputs are sorted by key and merged into larger files. This reduces the number of files and the disk I/O.
- Partitioning: The map outputs are divided into partitions based on a hash function of the key. Each partition corresponds to a reducer. This ensures that all the values for the same key go to the same reducer.

#### Sort
- Sort is the process of ordering the map outputs by key before sending them to the reducers.
- Sort is done at both the map and reduce sides.
- Map side sort: The map outputs are sorted by key as they are written to the local disk. This is done by using a buffer and a spill thread. The buffer holds the map outputs in memory until it reaches a threshold. The spill thread then sorts the buffer contents and writes them to a spill file on disk. Multiple spill files are merged and sorted into a single partitioned and sorted output file.
- Reduce side sort: The reduce inputs are sorted by key as they are fetched from the mappers. This is done by using a merge sort algorithm. The reduce inputs are merged and sorted in rounds until only one stream is left. The final sorted stream is then passed to the reduce function.