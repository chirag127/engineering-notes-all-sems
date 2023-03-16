## Implementation of K-means clustering using Map Reduce for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

1. K-means clustering is a popular unsupervised machine learning algorithm used to partition a dataset into k clusters.
2. The algorithm works by iteratively assigning each data point to the nearest cluster centroid and then updating the centroid based on the mean of all the points in the cluster.
3. MapReduce is a programming model for processing large datasets in parallel across a distributed computing environment.
4. The implementation of K-means clustering using MapReduce involves dividing the dataset into partitions and processing each partition in parallel using the Map function.
5. The Map function calculates the distance between each data point and the current cluster centroids and assigns the data point to the nearest centroid.
6. The Reduce function aggregates the data points assigned to each cluster and calculates the new cluster centroid based on the mean of all the points in the cluster.
7. The updated cluster centroids are then used in the next iteration of the algorithm until convergence is reached.
8. This implementation allows for efficient processing of large datasets and can be scaled to handle even larger datasets by adding more computing resources.