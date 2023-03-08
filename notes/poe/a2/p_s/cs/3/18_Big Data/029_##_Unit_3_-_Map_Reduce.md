 Here is the content written in markdown format on the topic ## Unit 3 - Map Reduce:

## Unit 3 - Map Reduce

Map Reduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster.

* It mainly consists of two functions - Map and Reduce.
* The map function processes the input data and generates intermediate key-value pairs.
* The reduce function merges all the intermediate values associated with the same key.

### How it works?

* The input is divided into splits and distributed to worker nodes.
* Each worker node processes its split using the map function and generates intermediate key-value pairs.
* The intermediate pairs are shuffled to reduce the values with the same key onto the same worker node.
* The reduce function is executed per key to generate the final output.

### Advantages

* It is fault tolerant. If a node fails, the job is reassigned to other nodes.
* It is scalable. More nodes can be added easily to process larger datasets.
* It is efficient as it processes the data locally and minimizes data transfer across the network.

### Disadvantages

* Requirement of large clusters of nodes.
* Additional overhead of distributing and shuffling data.
* Not suitable for iterative algorithms.

### Examples and Applications

* Processing log data to find frequent patterns.
* Counting occurrences of words in a document.
* Building indexes.
* Machine Learning algorithms.

[Detailed diagrams and code examples can be added here to illustrate the concepts and showcase applications.]