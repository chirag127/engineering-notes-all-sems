# K-means Clustering Algorithm

- K-means clustering is a method of **vector quantization**, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster.
- K-means clustering is an **unsupervised learning algorithm**. There is no labeled data for this clustering, unlike in supervised learning.
- K-means clustering is a simple and elegant approach for partitioning a data set into K distinct, nonoverlapping clusters. To perform K-means clustering, we must first specify the desired number of clusters K; then, the K-means algorithm will assign each observation to exactly one of the K clusters.
- K-means clustering is deployed to discover groups that haven’t been explicitly labeled within the data. It’s being actively used today in a wide variety of business applications such as customer segmentation, market analysis, image compression, etc.

## Steps of K-means Clustering Algorithm

The algorithm works as follows:

1. First, we initialize k points, called means or cluster centroids, randomly.
2. We categorize each item to its closest mean and we update the mean’s coordinates, which are the averages of the items categorized in that mean so far.
3. We repeat the process for a given number of iterations and at the end, we have our clusters.

## Advantages and Disadvantages of K-means Clustering Algorithm

Some of the advantages of K-means clustering are:

- It is easy to implement and understand.
- It is computationally efficient and scalable for large data sets.
- It can produce tight clusters with spherical shapes.

Some of the disadvantages of K-means clustering are:

- It requires the number of clusters K to be specified in advance, which may not be easy to determine.
- It is sensitive to the initial choice of cluster centroids, which may lead to different results for different runs of the algorithm.
- It is not suitable for data sets with clusters of different sizes, densities, or shapes, as it assumes equal variance and spherical clusters.
- It may not converge to the global optimum, but to a local optimum, depending on the initial cluster centroids.