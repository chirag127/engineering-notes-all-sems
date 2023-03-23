 Here are the notes on Clustering for Streams and Parallelism for Unit 5 - Frequent Itemsets and Clustering in Data Analytics:

### Clustering for Streams
- Clustering large data streams in real-time is challenging due to the massive volume of data and limited processing time.
- Online clustering algorithms process data instances one at a time and update the cluster model immediately. They are suitable for data streams.
- Challenges in stream clustering:
	- Limited memory to store all data instances.
	- Limited time to cluster each instance.
	- Concept drift - underlying data distribution changes over time.
- Approaches:
	- Micro-clustering - cluster instances into temporary micro-clusters and merge them later.
	- Hoeffding trees - useHoeffding bound to detect concept drift and adapt the model.
	- CluStream - divides data into chunks and clusters them in parallel. Uses micro-clustering and Hoeffding trees.

### Parallelism
- For huge data sets, serial execution of clustering algorithms is very time-consuming.
- Parallel and distributed algorithms divide the workload across multiple nodes/processors to improve performance.
- Types of parallelism:
	- Data parallelism - divide data across nodes, each node processes a partition and results are combined.
	- Task parallelism - divide tasks of an algorithm across nodes.
- Challenges:
	- Balancing load across nodes.
	- Reducing inter-node communications.
	- Dealing with node failures.
- Approaches:
	- MapReduce
	- Graph partitioning
	- Shared memory parallelism