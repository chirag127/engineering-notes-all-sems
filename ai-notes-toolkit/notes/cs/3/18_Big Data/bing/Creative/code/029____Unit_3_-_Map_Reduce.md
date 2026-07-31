## Unit 3 - Map Reduce

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as in their original forms.
- The key contributions of the Map Reduce framework are not the actual map and reduce functions, but the scalability and fault-tolerance achieved for a variety of applications by optimizing the execution engine once.
- As such, a single Map Reduce program written in Java, Python, or C++ can be run unmodified on any distributed system, whether it is a cluster of a few machines or a larger cluster of thousands of machines.

### Map Reduce Workflow

- The Map Reduce workflow consists of four phases: split, map, shuffle, and reduce.
- Split: The input data set is split into chunks of data, typically 64 MB or 128 MB each, and distributed across the cluster. Each chunk is assigned to a map task that processes it independently.
- Map: The map function takes a key-value pair as input and produces a set of intermediate key-value pairs as output. The intermediate keys do not need to be of the same type as the input keys, and the number of intermediate key-value pairs does not need to match the number of input key-value pairs. The map function is applied to every input key-value pair in parallel.
- Shuffle: The intermediate key-value pairs produced by the map tasks are partitioned, sorted, and transferred to the reduce tasks. The partitioning is done by applying a hash function to the intermediate keys, and the sorting is done by grouping the intermediate key-value pairs by key. The shuffle phase ensures that all the values associated with the same key are sent to the same reduce task.
- Reduce: The reduce function takes an intermediate key and a set of values associated with that key as input and produces a set of output key-value pairs as output. The output keys do not need to be of the same type as the intermediate keys, and the number of output key-value pairs does not need to match the number of input values. The reduce function is applied to each intermediate key and its corresponding values in parallel.

### Map Reduce Example

- A common example of a Map Reduce application is word count, which counts the number of occurrences of each word in a large collection of documents.
- The map function takes a document as input and emits a key-value pair for each word in the document, where the key is the word and the value is 1.
- The reduce function takes a word and a list of values as input and sums up the values to get the total count of the word, and emits a key-value pair where the key is the word and the value is the count.
- The output of the Map Reduce program is a list of words and their counts, sorted by the words.

### Map Reduce Benefits

- Map Reduce offers several benefits for processing large data sets, such as:
  - Scalability: Map Reduce can scale up to thousands of machines and petabytes of data by parallelizing the computation and distributing the data across the cluster.
  - Fault-tolerance: Map Reduce can handle failures of machines, tasks, or network by automatically re-executing the failed tasks on other machines and using replication and checksums to ensure data integrity.
  - Simplicity: Map Reduce abstracts away the details of distributed computing, such as communication, synchronization, load balancing, and fault recovery, and allows the programmer to focus on the logic of the map and reduce functions.
  - Flexibility: Map Reduce can support a wide range of applications, such as text processing, web indexing, machine learning, graph analysis, and image processing, by allowing the programmer to define custom map and reduce functions and data formats.