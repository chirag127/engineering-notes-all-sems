### k-Nearest Neighbour Learning

k-Nearest Neighbour (k-NN) is a non-parametric and lazy learning algorithm that can be used for classification and regression tasks. It is a simple and easy-to-implement algorithm that is widely used in machine learning applications. In this section, we will discuss the k-NN algorithm and its working in detail.

#### Working of k-NN Algorithm

The k-NN algorithm works based on the concept of similarity between instances. The basic idea is to classify a new instance based on the class labels of its k nearest neighbours in the training set. The algorithm works as follows:

1. Calculate the distance between the new instance and all the instances in the training set using a distance metric (e.g. Euclidean distance, Manhattan distance, etc.).
2. Select the k instances that are closest to the new instance.
3. Classify the new instance based on the majority class label among the k nearest neighbours.

#### Advantages of k-NN Algorithm

1. Simple and easy to implement.
2. No assumptions are made about the underlying data distribution.
3. Can be used for both classification and regression tasks.
4. Robust to noisy data.

#### Disadvantages of k-NN Algorithm

1. Computationally expensive for large datasets.
2. Sensitive to the choice of distance metric.
3. Not suitable for high-dimensional data.
4. Requires a large amount of memory to store the training set.

#### Applications of k-NN Algorithm

1. Image recognition.
2. Recommender systems.
3. Text classification.
4. Medical diagnosis.

#### Example

Suppose we have a dataset of flowers with two features: sepal length and sepal width. The dataset contains three classes of flowers: Setosa, Versicolor, and Virginica. We want to classify a new flower based on its sepal length and sepal width.

We apply the k-NN algorithm with k=3. The algorithm calculates the distance between the new flower and all the flowers in the training set. It selects the three flowers that are closest to the new flower. Suppose the three nearest neighbours are two Setosa and one Versicolor. The algorithm classifies the new flower as Setosa (the majority class label among the three nearest neighbours).

#### Conclusion

k-NN is a popular and effective algorithm for classification and regression tasks. It is a simple and easy-to-implement algorithm that can be used in a wide range of applications. However, it has certain limitations and is not suitable for all types of datasets.