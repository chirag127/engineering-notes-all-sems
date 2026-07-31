### k-Nearest Neighbour Learning

- k-Nearest Neighbour (k-NN) is a supervised learning algorithm that can be used for both classification and regression tasks .
- k-NN is based on the idea of proximity, which means that the label of a new data point is determined by the labels of its k closest neighbours in the training data set .
- k-NN is a non-parametric algorithm, which means that it does not make any assumptions about the underlying distribution of the data.
- k-NN is also an instance-based or lazy algorithm, which means that it does not learn a generalizable model from the training data, but rather stores the training data and makes predictions based on the similarity between the new data point and the stored instances .
- k-NN can be applied to various types of data, such as numerical, categorical, text, image, etc. However, different types of data may require different ways of measuring the distance or similarity between the data points .
- k-NN has some advantages and disadvantages as a machine learning technique. Some of the advantages are:
  - It is simple and easy to implement and understand .
  - It can handle multi-class problems and non-linear boundaries .
  - It is robust to noisy data and outliers, as long as the number of neighbours is large enough .
- Some of the disadvantages are:
  - It is computationally expensive and slow, as it requires storing and searching the entire training data set for each prediction .
  - It is sensitive to the choice of k, the number of neighbours, which can affect the accuracy and complexity of the algorithm .
  - It is also sensitive to the choice of the distance or similarity metric, which can affect the performance and interpretability of the algorithm .
  - It suffers from the curse of dimensionality, which means that as the number of features or dimensions increases, the distance between the data points becomes less meaningful and the algorithm becomes less effective .