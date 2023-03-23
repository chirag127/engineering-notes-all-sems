### Hierarchical Clustering

Hierarchical clustering is a type of unsupervised learning that groups together similar data points based on their distance from each other. It is a commonly used technique in data analytics for finding patterns and structures in data. In this section, we will discuss how hierarchical clustering works and different types of algorithms used for it.

#### How does Hierarchical Clustering work?

Hierarchical clustering involves building a hierarchy of clusters by recursively dividing data points into smaller clusters until a stopping criterion is met. The two main types of hierarchical clustering are agglomerative and divisive.

- Agglomerative hierarchical clustering starts with each data point as a separate cluster and then merges them together based on the similarity between them. This process continues until all data points are grouped into a single cluster.
- Divisive hierarchical clustering starts with all data points in a single cluster and then recursively splits it into smaller clusters based on the dissimilarity between them. This process continues until each data point is in its own cluster.

#### Different types of Hierarchical Clustering algorithms

There are various algorithms used for hierarchical clustering. Some of them are:

- Single linkage: This algorithm links two clusters based on the distance between their closest points.
- Complete linkage: This algorithm links two clusters based on the distance between their farthest points.
- Average linkage: This algorithm links two clusters based on the average distance between all their points.
- Ward's linkage: This algorithm links two clusters based on the decrease in variance when they are merged.

#### Advantages of Hierarchical Clustering

- It does not require the number of clusters to be specified beforehand.
- It produces a hierarchy of clusters, which can be useful in understanding the relationships between different data points.
- It can handle different types of distance measures and linkage criteria.

#### Disadvantages of Hierarchical Clustering

- It can be computationally expensive for large datasets.
- It may not work well with noisy or high-dimensional data.
- The results may be sensitive to the choice of distance measure and linkage criteria.