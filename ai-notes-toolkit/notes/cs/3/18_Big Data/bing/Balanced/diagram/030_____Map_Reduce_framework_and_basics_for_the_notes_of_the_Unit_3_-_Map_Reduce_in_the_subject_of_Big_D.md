### Map Reduce framework and basics

MapReduce is a programming model or pattern within the Hadoop framework that is used to access big data stored in the Hadoop File System (HDFS). It is a core component, integral to the functioning of the Hadoop framework.

The MapReduce framework consists of the following components:

- A single master **ResourceManager**, which manages the resources and the scheduling of the applications.
- One worker **NodeManager** per cluster-node, which runs the tasks and reports the status to the ResourceManager.
- One **MRAppMaster** per application, which coordinates the execution of the map and reduce tasks (see YARN Architecture Guide).

The MapReduce framework operates on the principle of splitting the input data into multiple chunks, processing them in parallel on different nodes, and combining the results into a single output file. The framework follows a two-phase approach: map and reduce.

- The **map** phase takes input pairs (usually key-value pairs), processes them, and produces another set of intermediate pairs as output. The map function is user-defined and can perform any kind of operation on the input, such as filtering, transforming, grouping, etc.
- The **reduce** phase takes the intermediate pairs from the map phase, sorts them by key, and applies a user-defined function to aggregate the values associated with the same key. The reduce function can perform any kind of operation on the values, such as summing, averaging, counting, etc.

The MapReduce framework handles the details of data distribution, parallelization, load balancing, fault tolerance, and network communication, allowing the user to focus on the logic of the map and reduce functions.

Some of the common applications of MapReduce are:

- Log analysis: MapReduce can be used to analyze log files and extract useful information, such as the number of visits, the most accessed pages, the errors encountered, etc.
- Full-text indexing: MapReduce can be used to perform full-text indexing of large collections of documents, such as web pages, books, articles, etc. The map function can tokenize the documents and emit pairs of words and document IDs, while the reduce function can create inverted lists of document IDs for each word.
- PageRank: MapReduce can be used to calculate the PageRank of web pages, which is a measure of their importance and popularity. The map function can emit pairs of web pages and their outgoing links, while the reduce function can update the PageRank of each web page based on the PageRank of its incoming links.
- Reverse Web-Link Graph: MapReduce can also be used to create a reverse web-link graph, which shows the incoming links for each web page. The map function can emit pairs of web pages and their outgoing links, while the reduce function can collect the incoming links for each web page.