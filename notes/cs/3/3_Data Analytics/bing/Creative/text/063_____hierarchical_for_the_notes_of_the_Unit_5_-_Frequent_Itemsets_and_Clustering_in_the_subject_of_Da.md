### Hierarchical Clustering

- Hierarchical clustering is a method of cluster analysis in data mining that creates a hierarchical representation of the clusters in a dataset .
- The method starts by treating each data point as a separate cluster and then iteratively combines the closest clusters until a stopping criterion is reached.
- The result of hierarchical clustering is a tree-like structure called a dendrogram that shows the nested grouping of clusters and their distances .
- Hierarchical clustering can be classified into two types: agglomerative and divisive.
  - Agglomerative clustering is a bottom-up approach that starts with individual data points and merges them into larger clusters based on their similarity .
  - Divisive clustering is a top-down approach that starts with the whole dataset and splits it into smaller clusters based on their dissimilarity.
- Hierarchical clustering has some advantages and disadvantages over other clustering methods:
  - Advantages:
    - It does not require specifying the number of clusters in advance.
    - It can capture the structure of the data at different levels of granularity.
    - It is easy to interpret and visualize.
  - Disadvantages:
    - It can be computationally expensive and sensitive to outliers and noise.
    - It is not suitable for large datasets or high-dimensional data.
    - It is not easy to update the clusters when new data points are added.