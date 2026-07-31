 Here are the notes on Clustering Techniques for Unit 5 - Frequent Itemsets and Clustering:

### K-Means Clustering
- K-Means is a clustering algorithm that groups similar data points into k clusters.
- It works by first randomly initializing k centroids, then iteratively refining the centroids to minimize the total within-cluster sum of squares.
- Pros: Simple and efficient, able to handle large datasets.
- Cons: Sensitive to initial centroid positions, may converge to local optima.

### Hierarchical Agglomerative Clustering
- HAC is a bottom-up clustering approach: each observation starts in its own cluster, and clusters are iteratively merged until all clusters have been merged into one.
- The main steps are:
 1. Assign each data point to its own cluster
 2. Repeat until all clusters have been merged:
 - Find the two closest clusters
 - Merge them into a single cluster
 3. The merges can be represented in a dendrogram, a tree-like diagram showing the merges.
- Pros: Does not require the number of clusters as input, can capture hierarchical relationships.
- Cons: Can be computationally expensive for large datasets, may produce unbalanced clusters.

### DBSCAN
- DBSCAN is a density-based clustering algorithm.
- It groups points that are closely packed together, marking points that lie alone in low-density regions as outliers.
- The two main inputs are:
 - Epsilon (eps): The maximum distance between two points for them to be considered neighbors.
 - MinPts: The minimum number of points required to form a dense region.
- Pros: Can find arbitrary shaped clusters and handle noise effectively.
- Cons: Sensitive to input parameters (eps, MinPts), and cannot handle varying density clusters well.