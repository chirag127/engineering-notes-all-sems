### Map Reduce

Map Reduce is a programming model and an implementation for processing and generating large datasets with a parallel, distributed algorithm on a cluster of computers. 

The main idea of Map Reduce is to divide a big problem into smaller subproblems that can be solved independently and in parallel by multiple machines, and then combine the results to obtain the final solution. 

The Map Reduce framework consists of two main phases: map and reduce. 

- The map phase takes a set of input data and transforms it into intermediate key-value pairs. The map function is applied to each input record and produces zero or more output pairs. The key-value pairs are then shuffled and sorted by the framework and sent to the reduce phase. 

- The reduce phase takes the intermediate key-value pairs and merges them to produce the final output. The reduce function is applied to each group of values that share the same key and produces zero or more output records. 

The Map Reduce framework handles the details of parallelization, fault-tolerance, data distribution, load balancing, and communication between the machines. The programmer only needs to specify the map and reduce functions and some configuration parameters. 

Map Reduce programming offers several benefits for processing large-scale data: 

- Scalability. Map Reduce can process petabytes of data across hundreds or thousands of machines in a cluster or a grid. 

- Flexibility. Map Reduce can handle various types of data, such as structured, unstructured, or semi-structured data, and support different kinds of operations, such as filtering, aggregation, grouping, joining, or sorting. 

- Speed. Map Reduce can achieve fast processing of massive data by exploiting the parallelism and locality of the computation. 

- Simplicity. Map Reduce allows the programmer to write code in a choice of languages, such as Java, Python, or C++, and abstracts away the complexity of distributed computing. 

An example of Map Reduce is to find the maximum temperature for each city from a collection of files that contain the city name and the temperature recorded on different days. 

The map function would take each line of the file as input and emit a key-value pair with the city name as the key and the temperature as the value. For example, the input line (Toronto, 20) would produce the output pair (Toronto, 20).

The reduce function would take a key and a list of values as input and emit a key-value pair with the key and the maximum value from the list. For example, the input pair (Toronto, [20, 18, 32, 22, 31]) would produce the output pair (Toronto, 32).

The Map Reduce framework would run the map function on each input file in parallel and partition the output pairs by the key. Then, it would run the reduce function on each group of values that share the same key and produce the final output. The output would look like this:

(Toronto, 32)
(Whitby, 27)
(New York, 33)
(Rome, 38)

A possible mnemonic to remember the Map Reduce model is:

- Map: Make key-value pairs
- Reduce: Reduce values by key

: https://en.wikipedia.org/wiki/MapReduce
: https://www.ibm.com/topics/mapreduce