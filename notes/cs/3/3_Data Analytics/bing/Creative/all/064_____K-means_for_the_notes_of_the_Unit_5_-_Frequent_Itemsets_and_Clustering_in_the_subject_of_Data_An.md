# K-means Clustering Algorithm

- K-means clustering is a method of **vector quantization**, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster.
- K-means clustering is an **unsupervised learning algorithm**. There is no labeled data for this clustering, unlike in supervised learning.
- K-means clustering is one of the simplest and most popular unsupervised machine learning algorithms for data scientists.
- K-means clustering is a **centroid-based clustering** algorithm, which organizes the data into non-hierarchical clusters, in contrast to hierarchical clustering.
- K-means clustering is widely used in various business applications, such as customer segmentation, image segmentation, anomaly detection, etc.

## Steps of K-means Clustering Algorithm

- To perform K-means clustering, we must first specify the desired number of clusters K.
- Then, the K-means algorithm will assign each observation to exactly one of the K clusters.
- The algorithm works as follows:
  - Step 1: Randomly assign a number, from 1 to K, to each of the observations. These serve as initial cluster assignments for the observations.
  - Step 2: Iterate until the cluster assignments stop changing:
    - For each of the K clusters, compute the cluster centroid. The kth cluster centroid is the vector of the p feature means for the observations in the kth cluster.
    - Assign each observation to the cluster whose centroid is closest (where closest is defined using Euclidean distance).
- The algorithm converges when the assignments no longer change.
- The result is a partitioning of the data into K clusters.

## Advantages and Disadvantages of K-means Clustering Algorithm

- Some of the advantages of K-means clustering are :
  - It is simple and easy to implement.
  - It is computationally efficient and scalable for large data sets.
  - It can produce tight and compact clusters.
  - It can handle numerical data well.
- Some of the disadvantages of K-means clustering are :
  - It requires the number of clusters K to be specified in advance, which may not be easy to determine.
  - It is sensitive to the initial cluster assignments and may converge to a local optimum.
  - It is not suitable for clusters of different shapes, sizes, and densities.
  - It cannot handle categorical data well.