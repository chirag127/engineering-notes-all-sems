# Hierarchical Clustering

Hierarchical clustering is a method of cluster analysis which seeks to build a hierarchy of clusters. It is commonly used in the field of data analytics and visualization, particularly in the context of frequent itemsets and clustering.

There are two main approaches to hierarchical clustering: agglomerative and divisive.

1. **Agglomerative hierarchical clustering** involves starting with each data point as a separate cluster and then merging the clusters together iteratively until a single cluster remains. This is done by calculating the distance between clusters and merging the two closest clusters at each step.

2. **Divisive hierarchical clustering** involves starting with all data points in a single cluster and then iteratively splitting the cluster into smaller clusters until each data point is in its own cluster. This is done by calculating the distance between data points and splitting the cluster along the dimension with the greatest variance.

Both approaches can use a variety of distance metrics to determine the distance between clusters or data points, including Euclidean distance, Manhattan distance, and cosine similarity.

Hierarchical clustering can be visualized using a dendrogram, which is a tree-like diagram that shows the hierarchy of clusters and the order in which they were merged or split.

Hierarchical clustering is commonly used in exploratory data analysis to identify patterns and relationships in the data. It can also be used in conjunction with other clustering methods, such as k-means clustering, to improve the accuracy of the clustering results.