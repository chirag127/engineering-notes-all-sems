#### Anatomy of a Map Reduce job run

1. **Input**: The input data is divided into fixed-size pieces called input splits. Each split is processed independently by a separate map task.
2. **Map**: The map function takes key-value pairs as input and produces a set of intermediate key-value pairs as output. The intermediate key-value pairs are sorted by key and partitioned into a number of reduce tasks.
3. **Shuffle**: The shuffle phase transfers the intermediate key-value pairs from the map tasks to the reduce tasks. The reduce tasks sort the incoming data by key.
4. **Reduce**: The reduce function takes the intermediate key-value pairs for a given key and produces a set of final key-value pairs as output. The output of the reduce function is written to the output file system.
5. **Output**: The final output of the MapReduce job is stored in the output file system, typically HDFS.
