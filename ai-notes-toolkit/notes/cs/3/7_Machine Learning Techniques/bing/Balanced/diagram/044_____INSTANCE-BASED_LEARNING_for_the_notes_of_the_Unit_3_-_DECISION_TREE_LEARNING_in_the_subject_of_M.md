### INSTANCE-BASED LEARNING

- Instance-based learning is a family of learning algorithms that, instead of performing explicit generalization, compare new problem instances with instances seen in training, which have been stored in memory.
- It is also called memory-based learning or lazy learning, because computation is postponed until a new instance is observed.
- Instance-based learning relies on some similarity measure to find the most relevant instances in memory for a given query.
- Some of the advantages of instance-based learning are:
  - It can handle complex and nonlinear data without making any assumptions about the data distribution.
  - It can adapt to changing data by adding or removing instances from memory.
  - It can learn incrementally and online, without requiring a separate training phase.
- Some of the disadvantages of instance-based learning are:
  - It can be computationally expensive and slow to find the nearest neighbors for a query, especially if the memory is large and high-dimensional.
  - It can be sensitive to noise and outliers, which can affect the similarity measure and the prediction.
  - It can suffer from the curse of dimensionality, which means that the distance between instances becomes less meaningful as the number of features increases.
- Some of the instance-based learning algorithms are:
  - K Nearest Neighbor (KNN): It predicts the class label or the regression value of a query based on the majority vote or the weighted average of its k nearest neighbors in memory.
  - Self-Organizing Map (SOM): It is a type of artificial neural network that maps high-dimensional data into a low-dimensional grid of nodes, where each node represents a prototype of a cluster of similar instances.
  - Learning Vector Quantization (LVQ): It is a supervised learning algorithm that trains a set of codebook vectors that represent the classes, and assigns a query to the class of the nearest codebook vector.
  - Locally Weighted Learning (LWL): It is a regression technique that fits a local model (such as a linear or polynomial function) to a query, using a weighted subset of instances that are close to the query.
  - Case-Based Reasoning (CBR): It is a problem-solving method that retrieves and adapts previous solutions (cases) that are similar to the current problem (query).