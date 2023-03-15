### Unit 3 - Map Reduce

#### MapReduce Framework and Basics

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is designed to allow for distributed processing of large data sets across a cluster of computers.

1. The MapReduce model is based on two main functions: the Map function and the Reduce function.
2. The Map function takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs).
3. The Reduce function takes the output from the Map function and combines the data tuples into a smaller set of tuples.
4. The MapReduce framework takes care of scheduling tasks, monitoring them, and re-executing any failed tasks.
5. The framework is designed to be fault-tolerant and to scale up from a single server to thousands of machines, each offering local computation and storage.
6. The MapReduce model is widely used for processing large data sets, particularly in the field of big data.