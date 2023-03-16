# Hierarchical Clustering

- Hierarchical clustering is a method of cluster analysis that seeks to build a hierarchy of clusters.
- Clustering is a technique to create homogeneous groups of entities or objects based on their similarity or dissimilarity.
- Hierarchical clustering can be performed in two ways: agglomerative or divisive.
  - Agglomerative clustering is a bottom-up approach that starts with each observation in its own cluster and then merges the closest pairs of clusters until all observations are in one cluster .
  - Divisive clustering is a top-down approach that starts with all observations in one cluster and then splits the cluster into smaller clusters based on some criterion until each observation is in its own cluster .
- Hierarchical clustering requires a measure of distance or similarity between observations and a linkage method to determine how to merge or split clusters.
  - Distance measures can be Euclidean, Manhattan, Minkowski, or other types depending on the nature and scale of the data.
  - Linkage methods can be single, complete, average, centroid, median, ward, or other types depending on the desired properties of the resulting clusters.
- Hierarchical clustering can be visualized using a dendrogram, which is a tree-like diagram that shows the nested structure of the clusters and the order of merging or splitting .
- Hierarchical clustering can be performed in R using the functions `hclust`, `cutree`, and `plot` from the base package, or using the functions `fviz_dend`, `fviz_cluster`, and `hcut` from the `factoextra` and `cluster` packages.