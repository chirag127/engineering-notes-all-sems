### Hierarchical Clustering

- Hierarchical clustering is a method of cluster analysis in data mining that creates a hierarchical representation of the clusters in a dataset .
- The method starts by treating each data point as a separate cluster and then iteratively combines the closest clusters until a stopping criterion is reached.
- The result of hierarchical clustering is a tree-like structure called a dendrogram that shows the nested grouping of clusters and their distances .
- There are two main types of hierarchical clustering: agglomerative and divisive.
  - Agglomerative clustering is a bottom-up approach that starts with individual data points and merges them into larger clusters based on their similarity .
  - Divisive clustering is a top-down approach that starts with the whole dataset and splits it into smaller clusters based on their dissimilarity.
- Hierarchical clustering requires a measure of similarity or distance between data points or clusters, such as Euclidean distance, Manhattan distance, cosine similarity, etc  .
- Hierarchical clustering also requires a linkage criterion that determines how the distance between clusters is calculated, such as single linkage, complete linkage, average linkage, Ward's method, etc  .
- Hierarchical clustering has some advantages and disadvantages over other clustering methods :
  - Advantages:
    - It does not require specifying the number of clusters in advance.
    - It can capture the hierarchical structure of the data and reveal different levels of granularity.
    - It is easy to interpret and visualize using a dendrogram.
  - Disadvantages:
    - It is computationally expensive and has a high time and space complexity.
    - It is sensitive to outliers and noise.
    - It is not reversible, meaning that once two clusters are merged or split, they cannot be undone.