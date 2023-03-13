## Unit 2 - Hadoop and Map Reduce

- Hadoop is a platform that allows distributed storage and processing of large-scale data using clusters of commodity hardware .
- MapReduce is a programming model that enables massive scalability across hundreds or thousands of servers in a Hadoop cluster. It is the heart of Apache Hadoop.
- The term "MapReduce" refers to two separate and distinct tasks that Hadoop programs perform:
  - The map job: This is where a set of data is converted into another set of data, where individual elements are broken down into tuples (key/value pairs).
  - The reduce job: This is where the output of the map job is combined to produce a smaller set of tuples, which are the final result.
- During a MapReduce job, Hadoop sends the Map and Reduce tasks to the appropriate servers in the cluster. The framework manages all the details of data-passing such as issuing tasks, verifying task completion, and copying data around the cluster between the nodes.
- MapReduce can process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner .
- MapReduce is suitable for applications that have the following characteristics :
  - The input data is large and can be split into independent chunks that can be processed by the map tasks in parallel.
  - The output data can be reduced to a smaller set of key/value pairs that can be combined by the reduce tasks in parallel.
  - The intermediate results of the map tasks can be grouped by key and shuffled across the network to the reduce tasks.
  - The logic of the application can be expressed as a map function and a reduce function.
- Some examples of applications that can use MapReduce are :
  - Word count: Counting the frequency of words in a large collection of documents.
  - Inverted index: Building an index of words and the documents that contain them for a search engine.
  - PageRank: Computing the importance of web pages based on the links between them.
  - K-means clustering: Finding groups of similar data points in a large data set.
  - Matrix multiplication: Performing algebraic operations on large matrices.