## Unit 3 - Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is designed to allow for distributed processing of large data sets across a cluster of computers.

1. The MapReduce model is divided into two main phases: the Map phase and the Reduce phase.
2. In the Map phase, the input data is divided into chunks and processed by a set of map tasks in parallel. Each map task takes a chunk of data and applies a user-defined map function to it, producing a set of intermediate key-value pairs.
3. In the Reduce phase, the intermediate key-value pairs are shuffled and sorted by key, and then processed by a set of reduce tasks in parallel. Each reduce task takes a set of intermediate key-value pairs with the same key and applies a user-defined reduce function to them, producing a set of output key-value pairs.
4. The output of the Reduce phase is the final result of the MapReduce computation.
5. MapReduce is commonly used for processing large data sets, such as log files, web crawl data, and social network data.
6. The MapReduce model is designed to be scalable, fault-tolerant, and easy to use. It can be implemented on a variety of distributed computing systems, including Hadoop, an open-source implementation of MapReduce.
7. MapReduce has been widely adopted in industry and academia, and has inspired the development of many other distributed data processing systems.