### Shuffle and Sort

- Shuffle and sort is the process by which the system performs the sort and transfers the map outputs to the reducers as inputs in MapReduce  .
- Shuffle and sort is the heart of MapReduce and is where the magic happens.
- Shuffle and sort phase in Hadoop occurs simultaneously and is done by the MapReduce framework.
- Shuffle and sort phase consists of the following steps  :
  - Map output is written to the local disk of the mapper node as intermediate files. The output is partitioned by key and each partition corresponds to a reducer.
  - The intermediate files are compressed by default to reduce the amount of data transferred to the reducers.
  - The reducer nodes send HTTP requests to the mapper nodes to fetch the intermediate files for the partitions assigned to them.
  - The mapper nodes transfer the intermediate files to the reducer nodes over the network. This is the shuffle step.
  - The reducer nodes merge and sort the intermediate files by key. This is the sort step.
  - The reducer nodes apply the reduce function to the sorted key-value pairs and write the output to the HDFS.