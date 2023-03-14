#### Anatomy of a Map Reduce job run

- A Map Reduce job run is a process of executing a Map Reduce program on a large-scale distributed data processing system, such as Hadoop.
- A Map Reduce program consists of two functions: a map function and a reduce function.
- The map function takes a key-value pair as input and produces a set of intermediate key-value pairs as output. The intermediate keys are usually different from the input keys.
- The reduce function takes an intermediate key and a set of values associated with that key as input and produces a set of final key-value pairs as output. The final keys are usually the same as the intermediate keys.
- A Map Reduce job run involves the following steps:

  1. The input data is split into fixed-size blocks and distributed across the nodes of the cluster. Each block is replicated for fault tolerance.
  2. The master node assigns a map task to each block of data. A map task runs the map function on the block and writes the intermediate key-value pairs to a local disk.
  3. The master node partitions the intermediate keys into a fixed number of buckets, based on a hash function. Each bucket corresponds to a reduce task.
  4. The master node assigns a reduce task to each bucket of intermediate keys. A reduce task fetches the intermediate values from the local disks of the nodes where the map tasks ran, sorts them by key, and runs the reduce function on each key-value group. The final key-value pairs are written to a distributed file system.
  5. The master node monitors the progress of the map and reduce tasks and handles failures by reassigning the tasks to other nodes.
  6. The output data is stored in the distributed file system and can be accessed by the user or other applications.

- A mnemonic to remember the steps of a Map Reduce job run is: **SMAPIR** (Split, Map, Partition, Reduce, Output).
- A simple example of a Map Reduce program is word count, which counts the frequency of each word in a large text file. The map function emits each word and 1 as a key-value pair, and the reduce function sums up the values for each word and emits the word and the count as a final key-value pair.