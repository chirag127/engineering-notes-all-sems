## Unit 3 - Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is designed to allow for distributed processing of large data sets across a cluster of computers.

1. The MapReduce model is inspired by the map and reduce functions commonly used in functional programming.
2. The model consists of two main phases: the map phase and the reduce phase.
3. In the map phase, the input data is divided into chunks and processed by map tasks in parallel.
4. Each map task processes a chunk of the input data and produces a set of intermediate key-value pairs.
5. In the reduce phase, the intermediate key-value pairs are grouped by key and processed by reduce tasks in parallel.
6. Each reduce task processes all the values associated with a particular key and produces a set of output values.
7. The output of the reduce phase is the final result of the MapReduce computation.

MapReduce is widely used for processing large data sets in a distributed computing environment. It is particularly useful for tasks such as data analysis, data mining, and machine learning. The model is simple, yet powerful, and can be easily adapted to a wide range of applications.