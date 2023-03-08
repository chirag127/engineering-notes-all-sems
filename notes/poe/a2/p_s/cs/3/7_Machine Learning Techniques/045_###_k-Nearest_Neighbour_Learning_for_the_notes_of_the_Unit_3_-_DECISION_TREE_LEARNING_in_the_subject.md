 Here is the content in markdown format for the topic - **k-Nearest Neighbour Learning** for the notes of **Unit 3 - DECISION TREE LEARNING** in the subject of **Machine Learning Techniques**:

### k-Nearest Neighbour Learning

- k-Nearest Neighbour is a simple supervised learning algorithm.
- It classifies a new data point based on the closest training examples in the feature space.
- The training data is stored and a distance metric is used to find the k closest neighbours of the point we want to classify.
- The new point is assigned the most common class among its k nearest neighbours.
- If k = 1, then the point is simply assigned the class of its nearest neighbour.

**Advantages:**
- Simple and easy to implement.
- Generates an intuitive model.
- Can perform reasonably well without pre-processing data (scaling/normalizing) as it relies on distance comparison.

**Disadvantages:**
- Computationally expensive as calculating distances for every point can be time-consuming for large datasets.
- Requires storing all training data as it is based on nearest neighbours.
- Performance can degrade with increase in dimensions of data as distance calculations become problematic (curse of dimensionality).

**Examples:**
- Image classification based on similarity.
- Recommendation systems.

**Code example (Python):**
```
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
```

**ASCII diagram:**

[A diagram showing kNN classification of a data point based on closest neighbours]

Advantages, disadvantages, applications, etc. can be added with more details as required. The content can be modified as needed to suit the requirements.