### Hierarchical Clustering

- Hierarchical clustering is a method of cluster analysis in data mining that creates a hierarchical representation of the clusters in a dataset .
- Cluster analysis is the process of grouping similar objects into clusters, where each cluster is distinct from other clusters, and the objects within each cluster are broadly similar to each other.
- Hierarchical clustering can be performed in two ways: agglomerative or divisive.
  - Agglomerative hierarchical clustering starts by treating each data point as a separate cluster and then iteratively combines the closest clusters until a stopping criterion is reached.
  - Divisive hierarchical clustering starts by treating the whole dataset as a single cluster and then iteratively splits the cluster into smaller clusters until a stopping criterion is reached.
- The similarity or distance between clusters can be measured by different methods, such as single linkage, complete linkage, average linkage, centroid linkage, or Ward's method.
- The result of hierarchical clustering can be visualized by a dendrogram, which is a tree-like diagram that shows the nested structure of the clusters.
- Hierarchical clustering has some advantages and disadvantages over other clustering methods:
  - Advantages:
    - It does not require specifying the number of clusters in advance.
    - It can capture the hierarchical structure of the data.
    - It is easy to interpret and visualize.
  - Disadvantages:
    - It can be sensitive to outliers and noise.
    - It can be computationally expensive for large datasets.
    - It does not allow reassigning or moving data points between clusters.