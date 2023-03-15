### Map Reduce framework and basics

MapReduce is a programming model or pattern within the Hadoop framework that is used to access big data stored in the Hadoop File System (HDFS). It is a core component, integral to the functioning of the Hadoop framework.

The MapReduce framework consists of the following components:

- A single master **ResourceManager**, which manages the resources and the scheduling of the applications.
- One worker **NodeManager** per cluster-node, which runs the tasks and reports the status to the ResourceManager.
- One **MRAppMaster** per application, which coordinates the execution of the map and reduce tasks (see YARN Architecture Guide).

The MapReduce framework operates on the principle of splitting the input data into multiple chunks, processing them in parallel on different nodes, and combining the results into a single output file. The framework follows a two-phase approach: map and reduce.

- The **map** phase takes input pairs (key, value) and applies a user-defined function to each pair, producing a set of intermediate pairs (key, value) as output. The map function can perform operations such as filtering, grouping, counting, or transforming the data.
- The **reduce** phase takes the intermediate pairs from the map phase and groups them by key. Then, it applies another user-defined function to each group of values, producing a final output pair (key, value) for each key. The reduce function can perform operations such as aggregation, summarization, or computation on the data.

The MapReduce framework handles the details of data distribution, parallelization, load balancing, fault tolerance, and network communication, allowing the user to focus on the logic of the application.

Some of the common use cases of MapReduce are:

- Log analysis: MapReduce can be used to analyze log files and extract useful information, such as the number of web pages accessed, the most popular pages, the average session time, etc.
- Full-text indexing: MapReduce can be used to perform full-text indexing of large collections of documents, such as web pages, books, or articles. The map function can tokenize and normalize the text, and the reduce function can create an inverted index that maps each term to the documents that contain it.
- PageRank: MapReduce can be used to calculate the PageRank of web pages, which is a measure of their importance and relevance. The map function can emit the PageRank of each page and the links to other pages, and the reduce function can update the PageRank of each page based on the PageRank of its incoming links.
- Reverse Web-Link Graph: MapReduce can be used to construct a reverse web-link graph, which is a graph that shows which pages link to a given page. The map function can emit the links from each page, and the reduce function can collect the links for each page and create the graph.

The following diagram illustrates the MapReduce framework and its phases:

![MapReduce framework](https://www.edureka.co/blog/wp-content/uploads/2016/12/MapReduce-Tutorial-1.png)