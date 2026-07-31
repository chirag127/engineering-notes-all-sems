#### Map Reduce framework and basics

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is a framework for distributed computing on large datasets on clusters of computers. The framework is inspired by the map and reduce functions commonly used in functional programming.

1. **Map** function: The map function takes an input pair and produces a set of intermediate key/value pairs. The MapReduce library groups together all intermediate values associated with the same intermediate key and passes them to the reduce function.

2. **Reduce** function: The reduce function accepts an intermediate key and a set of values for that key. It merges together these values to form a possibly smaller set of values.

3. **Input and Output**: The input and output of the MapReduce framework are both sets of key/value pairs.

4. **Fault Tolerance**: The MapReduce framework is designed to be highly fault-tolerant. It can handle failures of individual machines in the cluster without losing data or interrupting the processing.

5. **Advantages**: MapReduce allows for distributed processing of large datasets, making it possible to process large amounts of data in a reasonable amount of time. It is also highly scalable, allowing for the addition of more machines to the cluster to increase processing power.

6. **Disadvantages**: MapReduce may not be the best solution for all problems. It is not well-suited for tasks that require a lot of communication between nodes or for tasks that require low latency.

7. **Applications**: MapReduce is commonly used for processing large datasets in fields such as data mining, machine learning, and scientific computing.

8. **Example**: An example of a MapReduce task is counting the number of occurrences of each word in a large collection of documents. The map function would take a document as input and output a key/value pair for each word in the document, with the word as the key and the value as 1. The reduce function would then sum up the values for each word, producing a final count for each word.

9. **Mnemonics**: A helpful mnemonic to remember the steps of the MapReduce process is "MRS. FAD" - Map, Reduce, Shuffle, Fault-tolerance, Advantages, Disadvantages.
