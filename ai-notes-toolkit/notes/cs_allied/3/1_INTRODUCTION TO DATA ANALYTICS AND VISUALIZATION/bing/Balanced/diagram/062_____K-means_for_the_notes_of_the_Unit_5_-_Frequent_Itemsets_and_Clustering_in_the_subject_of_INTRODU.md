### K-means for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

- K-means is a clustering algorithm that partitions a data set into K distinct, non-overlapping clusters based on the similarity of the data points .
- K-means is an unsupervised learning algorithm, meaning that there is no labeled data for this clustering, unlike in supervised learning.
- K-means aims to assign each data point to the cluster with the nearest mean, which serves as the prototype or centroid of the cluster.
- K-means can be used for various applications, such as customer segmentation, image compression, anomaly detection, etc .

#### Steps of K-means algorithm

1. Initialize K points, called means or cluster centroids, randomly or by some heuristic method.
2. Assign each data point to the cluster with the closest centroid, using some distance measure, such as Euclidean distance.
3. Update the coordinates of the centroids by taking the average of the data points assigned to each cluster.
4. Repeat steps 2 and 3 until the centroids do not change significantly or a maximum number of iterations is reached.

#### Advantages and disadvantages of K-means algorithm

- Advantages:
  - Simple and easy to implement.
  - Scalable and efficient for large data sets.
  - Can produce tight and compact clusters.
- Disadvantages:
  - Sensitive to the initial choice of centroids and outliers.
  - Requires the number of clusters K to be specified in advance.
  - Assumes spherical and equal-sized clusters, which may not hold for real data.