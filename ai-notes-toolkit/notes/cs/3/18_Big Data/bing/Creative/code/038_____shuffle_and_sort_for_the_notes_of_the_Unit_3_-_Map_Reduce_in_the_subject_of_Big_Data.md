### Shuffle and Sort for the notes of the Unit 3 - Map Reduce in the subject of Big Data

- Shuffle and Sort is the process by which the system performs the sort and transfers the map outputs to the reducers as inputs  .
- Shuffle and Sort is the heart of MapReduce and is where the magic happens.
- Shuffle and Sort covers the merging and sorting of map outputs.
- Shuffle and Sort occurs simultaneously and is done by the MapReduce framework.
- Shuffle and Sort consists of the following steps    :
  - Map outputs are buffered in memory and periodically written to local disk, partitioned by the partitioner function and sorted by the key.
  - The buffered map outputs are spilled to disk when the buffer reaches a threshold size. The spilled files are merged and sorted by the key.
  - The spilled files are optionally compressed to reduce the disk space and network bandwidth usage.
  - The location of the spilled files on the local disk is communicated to the master node, which is responsible for scheduling the reduce tasks.
  - The reduce tasks are assigned to the nodes based on the locality of the map outputs. The reduce tasks fetch the map outputs from the local or remote nodes using HTTP.
  - The map outputs are merged and sorted by the key again on the reduce side. The values associated with each key are grouped together and passed to the reduce function.
  - The output of the reduce function is written to the final output file on the distributed file system.