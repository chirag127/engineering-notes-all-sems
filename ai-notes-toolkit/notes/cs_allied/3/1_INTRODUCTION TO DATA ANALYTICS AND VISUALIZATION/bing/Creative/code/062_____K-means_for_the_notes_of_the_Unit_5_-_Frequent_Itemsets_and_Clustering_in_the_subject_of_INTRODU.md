### K-means for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

- K-means is a clustering algorithm that aims to partition a data set into K distinct, non-overlapping clusters based on the similarity of the data points.
- K-means is an unsupervised learning algorithm, meaning that there is no labeled data for this clustering, unlike in supervised learning.
- K-means is one of the simplest and most popular machine learning algorithms for data scientists, as it can be applied to a wide variety of business applications, such as customer segmentation, image compression, anomaly detection, etc .
- The basic steps of the K-means algorithm are:
  - Initialize K points, called means or cluster centroids, randomly or using some heuristic.
  - Assign each data point to the cluster with the nearest mean, using some distance measure, such as Euclidean distance.
  - Update the mean coordinates of each cluster, which are the averages of the data points belonging to that cluster.
  - Repeat steps 2 and 3 until convergence, which means that the cluster assignments do not change or the maximum number of iterations is reached.
- The main advantages of K-means are:
  - It is easy to implement and understand.
  - It is computationally efficient, as it has a linear time complexity with respect to the number of data points, clusters, and features.
  - It can produce tight and compact clusters, especially if the data is well-separated.
- The main disadvantages of K-means are:
  - It is sensitive to the initial choice of cluster centroids, which can affect the final clustering result. To overcome this, multiple runs with different initializations are often performed and the best one is chosen based on some criterion, such as the sum of squared errors (SSE).
  - It requires the user to specify the number of clusters K, which can be difficult to determine beforehand. To overcome this, some methods, such as the elbow method or the silhouette method, can be used to evaluate the quality of clustering for different values of K and choose the optimal one.
  - It assumes that the clusters are spherical and have similar sizes and densities, which may not hold true for some data sets. To overcome this, some variants of K-means, such as K-medoids or K-means++, can be used to improve the robustness and stability of the algorithm.