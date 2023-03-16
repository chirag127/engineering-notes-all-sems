# K-means Clustering Algorithm

- K-means clustering is a method of **vector quantization**, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster.
- K-means clustering is an **unsupervised learning algorithm**. There is no labeled data for this clustering, unlike in supervised learning. K-Means performs the division of objects into clusters that share similarities and are dissimilar to the objects belonging to another cluster.
- K-means clustering is a simple and elegant approach for partitioning a data set into K distinct, nonoverlapping clusters. To perform K-means clustering, we must first specify the desired number of clusters K; then, the K-means algorithm will assign each observation to exactly one of the K clusters.
- K-means clustering is widely used in various business applications, such as customer segmentation, image segmentation, anomaly detection, market segmentation, etc.

## Steps of K-means Clustering Algorithm

- The algorithm works as follows:
  - First, we initialize k points, called means or cluster centroids, randomly.
  - We categorize each item to its closest mean and we update the mean’s coordinates, which are the averages of the items categorized in that mean so far.
  - We repeat the process for a given number of iterations and at the end, we have our clusters.
- The algorithm can be summarized as follows:
  - Randomly assign a number, from 1 to K, to each of the observations. These serve as initial cluster assignments for the observations.
  - Iterate until the cluster assignments stop changing:
    - For each of the K clusters, compute the cluster centroid. The kth cluster centroid is the vector of the p feature means for the observations in the kth cluster.
    - Assign each observation to the cluster whose centroid is closest (where closest is defined using Euclidean distance).
- The algorithm can be expressed in pseudocode as follows:
  - Choose the number of clusters, k.
  - Randomly generate k clusters and determine the cluster centers, or directly generate k random points as cluster centers.
  - Assign each point to the nearest cluster center.
  - Recompute the new cluster centers.
  - Repeat the two previous steps until some convergence criterion is met (usually that the assignment hasn't changed).