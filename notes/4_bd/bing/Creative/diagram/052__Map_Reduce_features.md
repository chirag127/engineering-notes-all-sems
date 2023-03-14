MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster. It consists of two phases: map and reduce. The map phase applies a user-defined function to each input record and produces a set of intermediate key-value pairs. The reduce phase aggregates the intermediate values associated with the same key and produces the final output. 

Some of the features of MapReduce are:

- Scalability: MapReduce can handle large amounts of data by distributing and storing them across multiple servers. 
- Flexibility: MapReduce can process different types of data, such as structured, unstructured, or semi-structured, and support various formats, such as text, binary, or XML. 
- Security and Authentication: MapReduce can integrate with the Hadoop security framework, which provides authentication, authorization, encryption, and auditing features. 
- Cost-effectiveness: MapReduce can run on commodity hardware, which reduces the cost of infrastructure and maintenance. 
- Fast: MapReduce can parallelize the computation and leverage the locality of data, which reduces the network overhead and improves the performance. 
- Simplicity: MapReduce provides a simple and intuitive programming model, which abstracts the details of parallelization, distribution, and fault-tolerance. 
- Parallel Programming: MapReduce enables concurrent processing of data by splitting them into smaller chunks and processing them in parallel on multiple servers. 
- Availability and Resilience: MapReduce can handle failures and recover from them by replicating the data and re-executing the failed tasks. 

#### Map Reduce features

The following diagram illustrates the basic architecture of a MapReduce program using ASCII characters:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input data 1  +---->+    Mapper 1    +---->+  Intermediate  |
|                |     |                |     |     data 1     |
+----------------+     +----------------+     +----------------+
                                                       |
+----------------+     +----------------+              |
|                |     |                |              |
|  Input data 2  +---->+    Mapper 2    +--------------+----> Shuffle and sort
|                |     |                |              |     by key
+----------------+     +----------------+              |
                                                       |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input data 3  +---->+    Mapper 3    +---->+  Intermediate  |
|                |     |                |     |     data 3     |
+----------------+     +----------------+     +----------------+
                                                       |
                                                       V
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Output data 1 +<----+   Reducer 1    +<----+  Intermediate  |
|                |     |                |     |     data 1     |
+----------------+     +----------------+     +----------------+
                                                       |
+----------------+     +----------------+              |
|                |     |                |              |
|  Output data 2 +<----+   Reducer 2    +--------------+----> Merge by key
|                |     |                |              |
+----------------+     +----------------+              |
                                                       |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Output data 3 +<----+   Reducer 3    +<----+  Intermediate  |
|                |     |                |     |     data 3     |
+----------------+     +----------------+     +----------------+
```

The diagram shows how the input data is split into three parts and fed to three mappers, which apply the map function and produce intermediate key-value pairs. The intermediate data is then shuffled and sorted by key and sent to the reducers, which apply the reduce function and produce the final output. The output data is then merged by key and written to the output file.