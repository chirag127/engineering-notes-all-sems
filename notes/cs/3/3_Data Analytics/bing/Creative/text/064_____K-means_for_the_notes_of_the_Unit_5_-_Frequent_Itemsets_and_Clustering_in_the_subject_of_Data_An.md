### K-means for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

- K-means is a **centroid-based clustering algorithm** that aims to partition a data set into **K distinct, non-overlapping clusters** .
- K-means is an **unsupervised learning algorithm**, meaning that it does not require labeled data for training .
- K-means can be used for various applications, such as customer segmentation, image compression, anomaly detection, etc .
- The basic steps of K-means are :
  - Choose the number of clusters K and randomly initialize K cluster centroids.
  - Assign each data point to the closest cluster centroid based on some distance measure, such as Euclidean distance.
  - Update the cluster centroids by computing the mean of the data points assigned to each cluster.
  - Repeat steps 2 and 3 until the cluster assignments do not change or a maximum number of iterations is reached.
- Some advantages of K-means are :
  - It is simple and easy to implement.
  - It is computationally efficient and scalable to large data sets.
  - It can produce compact and spherical clusters that are suitable for some applications.
- Some disadvantages of K-means are :
  - It requires the user to specify the number of clusters K, which may not be known in advance or may not reflect the true structure of the data.
  - It is sensitive to the initial choice of cluster centroids, which may lead to different results or local optima.
  - It is not robust to outliers or noise, which may affect the cluster centroids and assignments.
  - It assumes that the clusters are isotropic and have equal variance, which may not hold for some data sets.