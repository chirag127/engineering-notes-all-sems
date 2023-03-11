### k-Nearest Neighbour Learning for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques.

k-Nearest Neighbour (k-NN) is a popular supervised learning algorithm that is used for classification and regression problems. It is a non-parametric algorithm that does not require any assumptions about the underlying data distribution. In this algorithm, the input consists of the k closest training examples in the feature space.

#### How does k-NN work?

- The k-NN algorithm works by finding the k nearest neighbours of a test instance from the training dataset based on a distance metric.
- The distance metric can be Euclidean, Manhattan, or any other measure of similarity.
- Once the k nearest neighbours are found, the algorithm assigns the majority class label (in the case of classification) or the mean value (in the case of regression) of these neighbours to the test instance.
- The value of k determines the number of neighbours that are considered for the classification or regression task.

#### Advantages of k-NN

- k-NN is a simple and easy-to-understand algorithm that does not require any training.
- It can be used for both classification and regression tasks.
- It can handle multi-class classification problems easily.
- It can work well with a small number of training instances.

#### Disadvantages of k-NN

- Computationally expensive when dealing with large datasets.
- The choice of distance metric can have a significant impact on the performance of the algorithm.
- The choice of the value of k can also affect the performance of the algorithm.

#### Example

Suppose we have a dataset of flowers with attributes like petal length, petal width, sepal length, and sepal width. We want to classify a new flower based on these attributes. We can use the k-NN algorithm to find the k nearest neighbours of the new flower in the training dataset and assign the majority class label to the new flower.

#### Applications

- k-NN is widely used in recommender systems to recommend products or services based on the preferences of similar users.
- It is also used in image recognition, speech recognition, and natural language processing.
- It can be used in anomaly detection and fraud detection.

In conclusion, k-Nearest Neighbour Learning is a popular and effective algorithm for classification and regression tasks that does not require any assumptions about the underlying data distribution. It may have some limitations, but its simplicity and versatility make it a valuable tool in the field of machine learning.