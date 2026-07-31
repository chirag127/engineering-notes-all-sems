### Shuffle and Sort for the notes of the Unit 3 - Map Reduce in the subject of Big Data

- Shuffle and sort is the process by which the system performs the sort and transfers the map outputs to the reducers as inputs    .
- Shuffle and sort is the heart of MapReduce and is where the magic happens.
- Shuffle and sort phase in Hadoop occurs simultaneously and is done by the MapReduce framework.
- The steps involved in shuffle and sort are as follows  :
  - Map outputs are buffered in memory and periodically written to local disk, partitioned by the partitioner function and sorted by the key.
  - The buffered map outputs are called spill files. They can be compressed to reduce the disk space and network bandwidth usage.
  - When the map task is finished, it notifies the master node about the location of the spill files.
  - The master node assigns the reduce tasks to the worker nodes and informs them about the map output locations.
  - The reduce tasks fetch the map outputs from the local or remote worker nodes using HTTP.
  - The fetched map outputs are merged and sorted by the key. If the map outputs are too large to fit in memory, an external merge sort is performed.
  - The merged and sorted map outputs are then passed to the reduce function, which produces the final output.