### MapReduce

MapReduce is a framework for processing parallelizable problems across large datasets using a large number of computers (nodes), collectively referred to as a cluster or a grid.

- A MapReduce framework (or system) is usually composed of three operations (or steps) :

  - Map: each worker node applies the map function to the local data, and writes the output to a temporary storage. A master node ensures that only one copy of the redundant input data is processed.
  - Shuffle: the worker nodes redistribute the data based on the output keys (produced by the map function), such that all data belonging to one key is located on the same worker node.
  - Reduce: the worker nodes now process each group of output data, per key, in parallel.

- The MapReduce framework orchestrates the processing by marshalling the distributed servers, running the various tasks in parallel, managing all communications and data transfers between the various parts of the system, and providing for redundancy and fault tolerance.

- The MapReduce framework is often associated with Apache Hadoop, which is an open-source implementation of the framework that supports distributed computing on large-scale data. Hadoop consists of a single master ResourceManager, one worker NodeManager per cluster-node, and MRAppMaster per application.

- The MapReduce framework can be used for various applications, such as:

  - Word count: counting the frequency of words in a large corpus of text.
  - Inverted index: building an index of words and their locations in a set of documents.
  - PageRank: computing the importance of web pages based on the link structure.
  - K-means clustering: partitioning a set of points into k clusters based on their distance.