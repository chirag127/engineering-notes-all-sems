### INSTANCE-BASED LEARNING

- Instance-based learning is a family of machine learning algorithms that, instead of performing explicit generalization, compare new problem instances with instances seen in training, which have been stored in memory.
- Instance-based learning is also called memory-based learning or lazy learning, because it postpones computation until a new instance is observed.
- Instance-based learning algorithms rely on some similarity measure to find the most relevant instances in memory for a given query.
- Some of the advantages of instance-based learning are:
  - It can handle complex and nonlinear data without making any assumptions about the underlying distribution.
  - It can adapt to changing data by adding or removing instances from memory.
  - It can learn incrementally and online, without requiring a separate training phase.
- Some of the disadvantages of instance-based learning are:
  - It can be computationally expensive and slow to find the nearest neighbors for a query, especially if the memory is large and high-dimensional.
  - It can be sensitive to noise, outliers, and irrelevant features, which can affect the similarity measure and the prediction accuracy.
  - It can suffer from the curse of dimensionality, which means that the distance between instances becomes less meaningful as the number of features increases.
- Some of the instance-based learning algorithms are:
  - K Nearest Neighbor (KNN): It predicts the class label or the regression value of a query based on the majority vote or the weighted average of its k closest neighbors in memory.
  - Self-Organizing Map (SOM): It maps the high-dimensional input space to a low-dimensional output space, where similar instances are clustered together in a grid-like structure.
  - Learning Vector Quantization (LVQ): It learns a set of prototype vectors that represent the different classes, and assigns a query to the class of its nearest prototype.
  - Locally Weighted Learning (LWL): It fits a local model (such as a linear regression) to a query based on a weighted subset of instances in memory, where the weights depend on the distance to the query.
  - Case-Based Reasoning (CBR): It retrieves and adapts the most similar cases (or solutions) from memory to solve a new problem, and updates the memory with the new case and its outcome.