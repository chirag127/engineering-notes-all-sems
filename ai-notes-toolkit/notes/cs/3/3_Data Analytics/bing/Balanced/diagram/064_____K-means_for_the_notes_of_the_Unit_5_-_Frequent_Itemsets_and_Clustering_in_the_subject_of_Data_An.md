### K-means clustering algorithm

- K-means clustering is a method of **vector quantization**, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster.
- K-means clustering is an **unsupervised learning algorithm**. There is no labeled data for this clustering, unlike in supervised learning. K-Means performs the division of objects into clusters that share similarities and are dissimilar to the objects belonging to another cluster.
- K-means clustering is one of the simplest and most popular unsupervised machine learning algorithms for data scientists. It is widely used in various applications, such as customer segmentation, image segmentation, anomaly detection, etc.
- K-means clustering is a **centroid-based clustering** algorithm, which organizes the data into non-hierarchical clusters, in contrast to hierarchical clustering. Centroid-based clustering is a type of clustering that clusters data based on the distance between data points and a cluster centroid.
- K-means clustering algorithm has the following steps:
  - Specify the number of clusters K.
  - Initialize K cluster centroids randomly.
  - Assign each data point to the closest cluster centroid.
  - Recompute the centroids of the new clusters.
  - Repeat steps 3 and 4 until the cluster assignments do not change or a maximum number of iterations is reached.