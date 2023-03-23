 Here is the content in markdown format without any emojis or external links and in a formal tone:

### k-Nearest Neighbour Learning

- k-NN is a simple supervised learning algorithm.
- It classifies instances based on closest training examples in the feature space.
- It calculates the distance between the test instance and all the training instances.
- It finds k closest neighbours and classifies the test instance based on the most frequent class among the k nearest neighbours.
- If k = 1, then the test instance is simply assigned the class of its nearest neighbour.
- As k increases, the k-NN classifier smoothes the classification decision and is less affected by noise. But a larger k leads to higher computational cost.
- k-NN can be implemented for both classification and regression problems.
- For regression, the k nearest neighbours determine the value of the test instance. The value is the mean or median of the feature values of the nearest neighbours.
- Advantages:
 - Simple to implement and understand.
 - Non-parametric, minimal assumptions on underlying data distribution.
 - Works well when the classes are well-separated.
 - Can tackle multi-class classification problems.
- Disadvantages:
 - Computational complexity increases with training data size.
 - Requires determining optimal k which is data set dependent.
 - Does not perform scaling/normalization, can be affected by irrelevant features.
 - May overfit if k is too small or variance is too high.