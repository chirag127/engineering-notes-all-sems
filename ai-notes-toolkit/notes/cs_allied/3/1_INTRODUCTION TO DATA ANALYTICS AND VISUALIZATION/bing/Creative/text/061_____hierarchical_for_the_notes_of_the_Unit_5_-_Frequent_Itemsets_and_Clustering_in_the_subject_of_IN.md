### Hierarchical Clustering

- Hierarchical clustering is a method of cluster analysis that seeks to build a hierarchy of clusters.
- There are two main types of hierarchical clustering: agglomerative and divisive.
- Agglomerative clustering is a bottom-up approach that starts with each observation in its own cluster and then merges the closest pairs of clusters until all observations are in one cluster .
- Divisive clustering is a top-down approach that starts with all observations in one cluster and then splits the cluster recursively into smaller clusters until each observation is in its own cluster .
- Hierarchical clustering requires a measure of similarity or distance between observations or clusters.
- Some common distance measures are Euclidean distance, Manhattan distance, Minkowski distance, and cosine similarity.
- Hierarchical clustering can be visualized using a dendrogram, which is a tree-like diagram that shows the nested grouping of clusters and their distances .
- Hierarchical clustering can be useful for exploring the structure of data, finding meaningful patterns, and identifying outliers .
- Hierarchical clustering has some advantages and disadvantages over other clustering methods:
  - Advantages:
    - It does not require specifying the number of clusters in advance.
    - It can capture the natural hierarchy of data and reveal different levels of granularity.
    - It is easy to interpret and explain using a dendrogram.
  - Disadvantages:
    - It can be computationally expensive and slow for large datasets.
    - It is sensitive to the choice of distance measure and linkage method.
    - It does not allow reassigning observations to different clusters once they are merged or split.