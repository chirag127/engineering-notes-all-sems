### Shuffle and Sort

- Shuffle and sort is the process by which the system performs the sort and transfers the map outputs to the reducers as inputs  .
- Shuffle and sort is the heart of MapReduce and is where the magic happens.
- Shuffle and sort consists of two phases: shuffle phase and sort phase .

#### Shuffle Phase

- In the shuffle phase, the intermediate output of the mappers are transferred to the reducers .
- The shuffle phase occurs simultaneously with the map phase and the reduce phase.
- The shuffle phase involves the following steps :
  - Partitioning: The map output is partitioned into R partitions, where R is the number of reducers. Each partition contains the records with the same key.
  - Spilling: The map output is written to the local disk as intermediate files. The intermediate files are compressed by default to reduce the disk and network I/O.
  - Copying: The reducers pull the intermediate files from the mappers via HTTP. The intermediate files are merged and sorted by the key on the reducer side.
  - Merging: The intermediate files from multiple mappers are merged and sorted by the key on the reducer side. The merged output is the input for the reduce phase.

#### Sort Phase

- The sort phase covers the merging and sorting of the map outputs.
- The sort phase occurs simultaneously with the shuffle phase and the reduce phase.
- The sort phase involves the following steps :
  - Grouping: The records with the same key are grouped together and passed to the same reducer.
  - Sorting: The records within each group are sorted by the key. The sorting order can be customized by implementing a custom comparator.
  - Reducing: The reducer applies the reduce function to each group of records and produces the final output. The output is written to the HDFS.