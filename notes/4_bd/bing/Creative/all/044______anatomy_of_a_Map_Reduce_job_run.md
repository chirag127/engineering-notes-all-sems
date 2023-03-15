#### Anatomy of a Map Reduce job run

- A Map Reduce job run is a process of executing a Map Reduce program on a cluster of machines.
- A Map Reduce program consists of two functions: a map function and a reduce function.
- The map function takes an input key-value pair and produces a set of intermediate key-value pairs.
- The reduce function takes an intermediate key and a set of values associated with that key and produces a set of output key-value pairs.
- The Map Reduce framework handles the distribution of data and computation across the cluster, as well as the fault tolerance and parallelization of the tasks.
- The anatomy of a Map Reduce job run can be divided into four main phases: input, map, shuffle and reduce.

##### Input phase
- In the input phase, the input data is split into fixed-size pieces called input splits.
- Each input split is assigned to a map task, which runs the map function on the input split.
- The map task produces a set of intermediate key-value pairs and writes them to the local disk.
- The input phase is parallelized by running multiple map tasks on different input splits concurrently.

##### Map phase
- In the map phase, the intermediate key-value pairs produced by the map tasks are partitioned by a partition function, which determines which reduce task will receive the values for a given key.
- The partition function is usually a hash function of the key, but it can be customized by the user.
- The map phase is also parallelized by running multiple map tasks on different input splits concurrently.

##### Shuffle phase
- In the shuffle phase, the intermediate key-value pairs are transferred from the map tasks to the reduce tasks, based on the partition function.
- The shuffle phase involves sorting and merging the intermediate key-value pairs by key, so that all the values for a given key are grouped together.
- The shuffle phase is performed by the Map Reduce framework and is transparent to the user.

##### Reduce phase
- In the reduce phase, the reduce tasks receive the sorted and grouped intermediate key-value pairs and run the reduce function on each key and its associated values.
- The reduce function produces a set of output key-value pairs and writes them to the output file system.
- The reduce phase is parallelized by running multiple reduce tasks on different partitions of the intermediate key-value pairs concurrently.

##### Mnemonics and learning tricks
- A possible mnemonic to remember the four phases of a Map Reduce job run is **I MaSh Re** (Input, Map, Shuffle, Reduce).
- A possible learning trick to understand the Map Reduce framework is to compare it to a word count example, where the input data is a set of documents, the map function counts the occurrences of each word in a document and emits a key-value pair of the word and its count, the reduce function sums up the counts of each word across all documents and emits a key-value pair of the word and its total count, and the output data is a list of words and their frequencies in the input data.