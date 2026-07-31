## Unit 3 - Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is designed to allow for distributed processing of large data sets across a cluster of computers.

1. The MapReduce model is divided into two main phases: the Map phase and the Reduce phase.
2. In the Map phase, the input data is divided into chunks and distributed across the cluster. Each chunk is then processed by a Map function, which produces a set of intermediate key-value pairs.
3. In the Reduce phase, the intermediate key-value pairs are grouped by key and processed by a Reduce function, which produces the final output.
4. The MapReduce model is designed to be fault-tolerant and scalable, allowing for the processing of large data sets on commodity hardware.
5. MapReduce is commonly used for tasks such as data analysis, data mining, and machine learning.