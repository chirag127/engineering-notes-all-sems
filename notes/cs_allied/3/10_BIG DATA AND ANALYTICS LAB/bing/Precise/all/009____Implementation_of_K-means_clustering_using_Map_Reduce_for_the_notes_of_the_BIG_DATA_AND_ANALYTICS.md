## Implementation of K-means clustering using Map Reduce for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

1. **K-means clustering** is a popular unsupervised machine learning algorithm used to partition a given set of data points into k clusters, where k is a predefined or user-defined constant.
2. The algorithm iteratively assigns each data point to one of the k clusters based on the feature similarity, and then updates the cluster centroids based on the mean of the data points in the cluster.
3. **MapReduce** is a programming model for processing large datasets in parallel across a distributed computing environment.
4. The implementation of K-means clustering using MapReduce involves dividing the data points into partitions and processing them in parallel using the MapReduce framework.
5. In the **Map** phase, each data point is assigned to the nearest cluster centroid, and the partial sum and count of the data points in each cluster are computed.
6. In the **Reduce** phase, the partial sums and counts from the Map phase are aggregated to compute the new cluster centroids.
7. The algorithm iterates until the cluster assignments no longer change or a maximum number of iterations is reached.
8. The use of MapReduce allows for efficient processing of large datasets and can significantly speed up the K-means clustering algorithm.
