#### Anatomy of a Map Reduce job run

- A Map Reduce job run is a process of executing a Map Reduce program on a cluster of machines.
- A Map Reduce program consists of two functions: a map function and a reduce function.
- The map function takes a key-value pair as input and produces a list of intermediate key-value pairs as output.
- The reduce function takes an intermediate key and a list of values associated with that key as input and produces a list of final key-value pairs as output.
- The Map Reduce framework handles the distribution, parallelization, fault-tolerance, and coordination of the map and reduce tasks on the cluster.
- The anatomy of a Map Reduce job run can be divided into four main phases: input, map, shuffle, and reduce.

##### Input phase

- The input data for a Map Reduce job is typically stored in a distributed file system (DFS) such as Hadoop Distributed File System (HDFS).
- The input data is split into fixed-size blocks (usually 64 MB or 128 MB) and replicated across multiple nodes in the cluster for fault-tolerance.
- Each block is assigned to a map task, which is a unit of work that executes the map function on a subset of the input data.
- The number of map tasks is determined by the number of input blocks and the configuration of the cluster.

##### Map phase

- The map tasks are distributed across the cluster by a master node, which is responsible for scheduling and monitoring the job.
- The master node assigns a map task to a worker node, which is a node that has a copy of the input block for that task.
- The worker node runs the map function on the input block and produces a list of intermediate key-value pairs.
- The intermediate key-value pairs are stored in the local disk of the worker node, partitioned by a hash function based on the intermediate keys.
- The number of partitions is equal to the number of reduce tasks, which is a parameter that can be specified by the user.

##### Shuffle phase

- The shuffle phase is the process of transferring the intermediate key-value pairs from the map tasks to the reduce tasks.
- The master node notifies the worker nodes about the location of the reduce tasks and the partitions they are responsible for.
- The worker nodes send the intermediate key-value pairs to the corresponding reduce tasks over the network, using a pull-based mechanism.
- The reduce tasks sort and merge the intermediate key-value pairs by their keys, and store them in the local disk of the worker node.

##### Reduce phase

- The reduce tasks are distributed across the cluster by the master node, similar to the map tasks.
- The master node assigns a reduce task to a worker node, which is a node that has a copy of the intermediate key-value pairs for that task.
- The worker node runs the reduce function on the intermediate key-value pairs and produces a list of final key-value pairs.
- The final key-value pairs are stored in the DFS, as the output of the Map Reduce job.

##### Mnemonics and learning tricks

- A possible mnemonic to remember the four phases of a Map Reduce job run is **I MaSh ReD** (Input, Map, Shuffle, Reduce).
- A possible learning trick to understand the Map Reduce framework is to compare it to a word count example, where the input data is a collection of documents, the map function counts the occurrence of each word in a document and emits a word-count pair, the shuffle phase groups the word-count pairs by their words, and the reduce function sums up the counts for each word and emits a word-total pair.