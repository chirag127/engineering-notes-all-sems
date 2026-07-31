 Here are the notes on Clustering for Streams and Parallelism for Unit 5 - Frequent Itemsets and Clustering:

### Clustering for Streams
- Clustering large data streams in real-time is challenging due to the huge volume of data and limited computational resources.
- Online clustering algorithms process data instances one at a time and update the model on the fly. They have limited memory and time per instance.
- Examples of streaming clustering algorithms:
-- CluStream: Uses micro-clusters to summarize data and performs periodic clustering of micro-clusters.
-- DenStream: Based on density connectivity and uses a grid-based approach to summarize data.
-- BIRCH: Uses a clustering feature tree to hierachically aggregate clusters and perform periodic clustering of the aggregates.

### Parallelism for Clustering
- Large datasets require distributed clustering for efficiency and scalability.
- Some approaches for parallel clustering:
-- Partitioning: Split data across nodes and run a sequential clustering algorithm on each partition in parallel.
-- Agglomerative hierarchical clustering: Bottom-up approach suits parallelism, different levels of the hierarchy can be computed in parallel.
-- K-means: Assignment and update steps can be parallelized but need to handle race conditions for updating cluster centers.
-- Graph-based: Community detection algorithms can be parallelized by operating on different parts of the graph in parallel.

The notes are written in points and in a formal tone without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the notes in any way.