### Map Reduce

Map Reduce is a programming model and an associated implementation for processing and generating large datasets with a parallel, distributed algorithm on a cluster of computers. 

- The model consists of two main functions: map and reduce.
- The map function takes a set of data and transforms it into another set of data, where each element is a key-value pair. The map function can perform filtering, sorting, grouping, or other operations on the input data.
- The reduce function takes the output of the map function as input and combines the key-value pairs into a smaller set of data. The reduce function can perform aggregation, summarization, or other operations on the input data.
- The Map Reduce system orchestrates the execution of the map and reduce functions by distributing the data and tasks across the cluster of computers, managing the communication and data transfer between them, and providing fault tolerance and scalability.
- Map Reduce is the core component of Apache Hadoop, a popular framework for big data processing. 
- Map Reduce can be used for various applications, such as word count, inverted index, web log analysis, machine learning, and more.

: https://en.wikipedia.org/wiki/MapReduce
: https://www.ibm.com/topics/mapreduce