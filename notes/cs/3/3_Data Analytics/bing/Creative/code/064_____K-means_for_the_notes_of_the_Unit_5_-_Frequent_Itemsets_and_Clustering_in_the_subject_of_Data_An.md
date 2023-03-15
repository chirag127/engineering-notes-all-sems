### K-means for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

- K-means is a **centroid-based clustering algorithm** that aims to partition a data set into **K distinct, non-overlapping clusters**  .
- K-means is an **unsupervised learning algorithm**, meaning that it does not require labeled data for training .
- K-means can be used for various applications, such as customer segmentation, image compression, anomaly detection, etc .
- The basic steps of the K-means algorithm are :
  - Choose the number of clusters K and randomly initialize K cluster centroids.
  - Assign each data point to the closest cluster centroid based on some distance measure, such as Euclidean distance.
  - Update the cluster centroids by computing the mean of the data points assigned to each cluster.
  - Repeat steps 2 and 3 until the cluster assignments do not change or a maximum number of iterations is reached.
- The main advantages of K-means are :
  - It is simple and easy to implement.
  - It is computationally efficient and scalable to large data sets.
  - It can produce compact and well-separated clusters.
- The main disadvantages of K-means are :
  - It requires the number of clusters K to be specified in advance, which may not be easy to determine.
  - It is sensitive to the initial cluster centroids, which may lead to different results depending on the random initialization.
  - It may not work well for data sets that have non-spherical, overlapping, or noisy clusters.
  - It may get stuck in a local optimum and not converge to the global optimum.