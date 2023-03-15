### INSTANCE-BASED LEARNING

- Instance-based learning is a family of machine learning algorithms that, instead of performing explicit generalization, compare new problem instances with instances seen in training, which have been stored in memory.
- Instance-based learning is also called memory-based learning or lazy learning, because it postpones computation until a new instance is observed.
- Instance-based learning algorithms rely on some similarity measure to find the most relevant instances in memory and use them to make predictions for new instances.
- Some of the advantages of instance-based learning are:
  - It can handle complex and nonlinear problems without making assumptions about the data distribution or the underlying function.
  - It can adapt to changes in the data over time by adding or deleting instances from memory.
  - It can provide explanations for the predictions by showing the nearest neighbors and their similarity scores.
- Some of the disadvantages of instance-based learning are:
  - It requires a large amount of memory to store all the instances.
  - It can be slow and computationally expensive to find the nearest neighbors for each new instance.
  - It can be sensitive to noise, outliers, and irrelevant features in the data.
- Some of the instance-based learning algorithms are:
  - K Nearest Neighbor (KNN): It assigns a new instance to the most common class among its k nearest neighbors in the training set.
  - Self-Organizing Map (SOM): It maps high-dimensional data to a low-dimensional grid of nodes, where each node represents a prototype of a cluster of similar instances.
  - Learning Vector Quantization (LVQ): It trains a set of prototype vectors that represent different classes, and assigns a new instance to the class of the closest prototype vector.
  - Locally Weighted Learning (LWL): It fits a local model (such as a linear regression) to a subset of instances near the new instance, weighted by their similarity to the new instance.
  - Case-Based Reasoning (CBR): It retrieves and adapts previous solutions (cases) to solve new problems, and updates the case base with new cases and feedback.