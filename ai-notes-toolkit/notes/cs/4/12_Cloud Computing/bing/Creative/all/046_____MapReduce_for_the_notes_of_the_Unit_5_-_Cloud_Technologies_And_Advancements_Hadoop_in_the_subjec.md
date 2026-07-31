# MapReduce

MapReduce is a programming paradigm that enables massive scalability across hundreds or thousands of servers in a Hadoop cluster. As the processing component, MapReduce is the heart of Apache Hadoop. The term "MapReduce" refers to two separate and distinct tasks that Hadoop programs perform:

- The **map** job: A map job takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs).
- The **reduce** job: A reduce job takes the output from a map as input and combines those data tuples into a smaller set of tuples.

MapReduce is a software framework for easily writing applications which process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner .

Some of the features of MapReduce are:

- **Distributed processing**: MapReduce distributes the data and the computation across multiple nodes in a cluster, allowing for parallel and scalable processing.
- **Fault tolerance**: MapReduce handles failures of nodes, network, or disk by automatically re-executing failed tasks on other nodes.
- **Data locality**: MapReduce moves the computation to the data, rather than the other way around, minimizing the network traffic and improving the performance.
- **Simplicity**: MapReduce provides a simple and intuitive programming model, where the developer only needs to specify the map and reduce functions, and the framework takes care of the rest.

Some of the applications of MapReduce are:

- **Word count**: A simple example of counting the frequency of words in a large text file.
- **Inverted index**: A common technique for building search engines, where the output is a mapping of words to the documents that contain them.
- **PageRank**: A famous algorithm for ranking web pages based on their links, used by Google.
- **Machine learning**: Many machine learning algorithms, such as k-means clustering, linear regression, and logistic regression, can be implemented using MapReduce.