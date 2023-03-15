# Hierarchical Clustering

- Hierarchical clustering is a method of cluster analysis in data mining that creates a hierarchical representation of the clusters in a dataset .
- Cluster analysis is a technique for finding groups of similar objects in a data set, such as customers, products, documents, etc.
- Hierarchical clustering can be either agglomerative or divisive, depending on how the clusters are formed.
  - Agglomerative hierarchical clustering starts with each data point as a separate cluster and then iteratively merges the closest clusters until a stopping criterion is reached.
  - Divisive hierarchical clustering starts with the whole data set as a single cluster and then iteratively splits the cluster into smaller clusters until a stopping criterion is reached.
- The stopping criterion can be based on the number of clusters, the distance between clusters, the size of clusters, or some other measure of cluster quality .
- The result of hierarchical clustering is a tree-like structure called a dendrogram, which shows the nested grouping of clusters and their distances .
- Hierarchical clustering can be useful for exploring the structure of a data set, finding natural groups of data, and identifying outliers or anomalies.
- Hierarchical clustering can be applied to various types of data, such as numerical, categorical, text, image, etc., as long as a suitable similarity or distance measure is defined for the data .
- Hierarchical clustering has some advantages and disadvantages compared to other clustering methods, such as k-means, DBSCAN, etc.
  - Advantages:
    - It does not require specifying the number of clusters in advance.
    - It can capture the hierarchical structure of the data and provide different levels of granularity.
    - It can handle data sets with arbitrary shapes and sizes.
  - Disadvantages:
    - It can be computationally expensive, especially for large data sets.
    - It can be sensitive to noise and outliers.
    - It can produce different results depending on the choice of similarity or distance measure, linkage method, and stopping criterion.