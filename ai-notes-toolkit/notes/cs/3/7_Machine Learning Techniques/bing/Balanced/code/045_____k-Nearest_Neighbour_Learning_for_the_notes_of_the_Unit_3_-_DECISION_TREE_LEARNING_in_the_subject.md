### k-Nearest Neighbour Learning

- k-Nearest Neighbour (k-NN) is a supervised learning algorithm that can be used for both classification and regression tasks .
- k-NN works by finding the k closest training examples to a given query point and using their labels to make a prediction .
- k-NN is a non-parametric algorithm, meaning that it does not make any assumptions about the underlying distribution of the data .
- k-NN is also an instance-based or lazy algorithm, meaning that it does not learn a generalizable model from the training data, but rather stores the entire training data and performs the prediction at the query time .
- k-NN can be applied to various types of data, such as numerical, categorical, text, image, etc. However, it requires a suitable distance metric to measure the similarity between the query point and the training examples .
- Some common distance metrics for k-NN are Euclidean distance, Manhattan distance, Minkowski distance, Hamming distance, Cosine similarity, etc .
- The choice of k, the number of nearest neighbors, is a crucial parameter for k-NN. A small value of k can lead to overfitting, while a large value of k can lead to underfitting .
- k-NN can be implemented using various data structures, such as brute-force, k-d tree, ball tree, etc. to speed up the search for the nearest neighbors .
- k-NN has some advantages, such as simplicity, flexibility, robustness to noisy data, etc. However, it also has some disadvantages, such as high computational cost, high memory requirement, sensitivity to irrelevant features, curse of dimensionality, etc .