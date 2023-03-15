#### Map Reduce features

Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments. It consists of two main phases: map and reduce.

- The map phase takes a set of input key-value pairs and transforms them into intermediate key-value pairs. The map function is applied to each input pair independently and can produce zero or more output pairs. The intermediate pairs are then shuffled and sorted by their keys and sent to the reduce phase.

- The reduce phase takes the intermediate key-value pairs with the same key and merges them into a smaller set of output key-value pairs. The reduce function is applied to each group of intermediate pairs with the same key and can produce zero or more output pairs. The output pairs are then written to the final output file or database.

Some of the features of Map Reduce are:

- It is scalable and fault-tolerant, as it can handle large volumes of data and recover from failures of nodes or tasks.
- It is flexible and expressive, as it can support various types of data and operations, such as structured, unstructured, text, binary, filtering, aggregation, join, etc.
- It is simple and declarative, as it abstracts away the details of parallelism, distribution, load balancing, and fault tolerance, and allows the programmer to focus on the logic of the map and reduce functions.
- It is compatible and portable, as it can run on various platforms and languages, such as Java, Python, C++, etc., and can interface with various data sources and sinks, such as HDFS, S3, MongoDB, etc.