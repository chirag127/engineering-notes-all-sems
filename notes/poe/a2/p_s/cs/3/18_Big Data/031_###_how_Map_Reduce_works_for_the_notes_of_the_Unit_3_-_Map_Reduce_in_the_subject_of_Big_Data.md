 Here is the content in markdown format for the topic ### how Map Reduce works for the notes of the Unit 3 - Map Reduce in the subject of Big Data:

### How Map Reduce works

Map Reduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It works in two phases:

1. Map phase: In this phase, the input data is divided into smaller chunks which are processed in parallel by multiple machines. The key idea is to transform the input data into intermediate key-value pairs. These pairs are then shuffled to be processed by the reducers.

- The input is divided into splits and processed in parallel by mappers.
- Each mapper processes the split and outputs key-value pairs.
- The types of the keys and values are defined by the programmer.

2. Reduce phase: The reducers processes the intermediate key-value pairs and aggregate the results to generate the final output. The key-value pairs with the same key are grouped together and a reducer processes each group and outputs zero or more key-value pairs.

- The intermediate key-value pairs are shuffled to be processed by reducers.
- Each reducer processes all values for a given key and outputs zero or more key-value pairs.
- The number of reducers is defined by the programmer or framework.

Some key points:

- Map Reduce is fault tolerant and can handle machine failures. The failed tasks are automatically rerun on other machines.
- It is scalable and can process huge amounts of data by increasing the number of machines in the cluster.
- The programming model is simple and the code can be written in various languages like Java, Python, C++, etc.
- Some disadvantages are that it may not be efficient for iterative algorithms and all data must fit into the memory of one machine.

Diagrams and examples can be included with illustrations of the two phases and how the shuffling occurs. The applications and advantages can be discussed in detail. The codes can be included for word count or other simple examples.