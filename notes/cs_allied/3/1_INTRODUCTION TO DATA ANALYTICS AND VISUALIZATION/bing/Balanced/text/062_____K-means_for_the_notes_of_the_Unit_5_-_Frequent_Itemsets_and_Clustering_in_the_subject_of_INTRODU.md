### K-means for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

- K-means is a clustering algorithm that aims to partition a data set into K distinct, non-overlapping clusters based on the similarity of the data points.
- K-means is an unsupervised learning algorithm, meaning that there is no labeled data for this clustering, unlike in supervised learning.
- K-means can be used for various applications, such as customer segmentation, image compression, anomaly detection, etc.
- The basic steps of the K-means algorithm are:
  - Initialize K points, called means or cluster centroids, randomly or by some heuristic method.
  - Assign each data point to the cluster with the nearest mean, using some distance measure, such as Euclidean distance.
  - Update the mean coordinates of each cluster, which are the averages of the data points belonging to that cluster.
  - Repeat steps 2 and 3 until the cluster assignments do not change or some convergence criterion is met.
- The main advantages of K-means are:
  - It is simple and easy to implement.
  - It is computationally efficient, with a time complexity of O(n*K*i), where n is the number of data points, K is the number of clusters, and i is the number of iterations.
  - It can handle large data sets and scale well with the number of features.
- The main disadvantages of K-means are:
  - It is sensitive to the initial choice of cluster centroids, which can affect the final clustering result and quality.
  - It requires the user to specify the number of clusters K, which may not be known beforehand or easy to determine.
  - It assumes that the clusters are spherical and have similar sizes and densities, which may not hold true for some data sets.
  - It may get stuck in local optima and not find the global optimal solution.