### K-means for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

K-means clustering is a popular unsupervised learning algorithm used for clustering similar data points into K groups. It is an iterative algorithm that partitions a given dataset into K clusters by minimizing the sum of distances between each point and its nearest cluster centroid.

#### The Algorithm
The K-means algorithm follows a simple process:
1. Initialize K centroids randomly.
2. Assign each data point to the nearest centroid.
3. Recalculate the centroids based on the mean of the points assigned to each cluster.
4. Repeat steps 2 and 3 until convergence.

#### Advantages
- Simple and easy to implement.
- Fast and scalable for large datasets.
- Handles high-dimensional data well.
- Results can be easily visualized.

#### Disadvantages
- The output depends on the initial random selection of centroids.
- The algorithm may converge to a local minimum rather than the global minimum.
- The choice of K is subjective and can affect the quality of the clustering.

#### Example
Consider a dataset of customer purchases with two features: amount spent and frequency of purchases. We want to cluster customers into three groups based on their purchasing behavior.
1. Initialize three centroids randomly.
2. Assign each customer to the nearest centroid.
3. Recalculate the centroids based on the mean of the customers assigned to each cluster.
4. Repeat steps 2 and 3 until convergence.

#### Applications
- Customer segmentation for targeted marketing.
- Grouping similar news articles for topic modeling.
- Image segmentation for computer vision.
- Anomaly detection in network traffic.

#### Code Example
```python
from sklearn.cluster import KMeans
import numpy as np

# Generate random data
X = np.random.rand(100, 2)

# Create KMeans model with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fit model to data
kmeans.fit(X)

# Get cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
```