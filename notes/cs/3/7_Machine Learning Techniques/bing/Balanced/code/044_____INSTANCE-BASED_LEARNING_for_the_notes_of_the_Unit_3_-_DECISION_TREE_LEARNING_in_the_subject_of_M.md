### INSTANCE-BASED LEARNING

- Instance-based learning is a family of learning algorithms that, instead of performing explicit generalization, compare new problem instances with instances seen in training, which have been stored in memory.
- It is called instance-based because it builds the hypotheses from the training instances.
- It is also called memory-based or lazy learning because it postpones the computation until a new instance is observed.
- The main advantages of instance-based learning are:
  - It can adapt to changes in the data distribution over time.
  - It can handle noisy and missing data by using appropriate similarity measures and voting schemes.
  - It can learn complex and nonlinear patterns without making any assumptions about the data distribution.
- The main disadvantages of instance-based learning are:
  - It requires a large amount of memory to store all the training instances.
  - It can be computationally expensive to find the nearest neighbors for each query instance.
  - It can be sensitive to the choice of similarity measure, distance metric, and number of neighbors.
- Some of the instance-based learning algorithms are:
  - K Nearest Neighbor (KNN): It classifies a query instance based on the majority vote of its k nearest neighbors in the training set.
  - Self-Organizing Map (SOM): It maps the high-dimensional input space to a low-dimensional output space using a grid of neurons that learn to represent the input distribution.
  - Learning Vector Quantization (LVQ): It learns a set of prototype vectors that represent the different classes and assigns a query instance to the class of the nearest prototype.
  - Locally Weighted Learning (LWL): It assigns different weights to the training instances based on their distance to the query instance and performs a local regression or classification.
  - Case-Based Reasoning (CBR): It retrieves and reuses the most similar cases from a case base to solve new problems.