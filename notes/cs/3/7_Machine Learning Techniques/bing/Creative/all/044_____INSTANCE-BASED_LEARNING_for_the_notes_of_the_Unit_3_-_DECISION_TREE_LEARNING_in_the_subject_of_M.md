# Instance-based learning

- Instance-based learning is a family of machine learning algorithms that, instead of performing explicit generalization, compare new problem instances with instances seen in training, which have been stored in memory.
- Instance-based learning is also called memory-based learning or lazy learning, because it postpones computation until a new instance is observed.
- Instance-based learning algorithms rely on some similarity measure to find the most relevant instances in memory and use them to make predictions for new instances.
- Some of the advantages of instance-based learning are:
  - It can handle complex and nonlinear problems without making any assumptions about the data distribution or the underlying function.
  - It can adapt to changes in the data over time by adding or deleting instances from memory.
  - It can provide explanations for the predictions by showing the nearest neighbors and their similarity scores.
- Some of the disadvantages of instance-based learning are:
  - It requires a large amount of memory to store all the instances.
  - It can be slow and inefficient to search for the nearest neighbors in high-dimensional spaces.
  - It can be sensitive to noise, outliers, and irrelevant features in the data.
- Some of the instance-based learning algorithms are:
  - K Nearest Neighbor (KNN): It predicts the class label or the regression value of a new instance by finding the k most similar instances in the training set and taking a majority vote or a weighted average of their labels/values.
  - Self-Organizing Map (SOM): It maps the high-dimensional input data to a low-dimensional grid of neurons, where each neuron represents a prototype of the data and the neighboring neurons have similar prototypes.
  - Learning Vector Quantization (LVQ): It trains a set of codebook vectors that represent the different classes of the data, and assigns a new instance to the class of the nearest codebook vector.
  - Locally Weighted Learning (LWL): It fits a local model (such as a linear regression or a polynomial regression) to a new instance by using a weighted subset of the training instances, where the weights depend on the distance to the new instance.
  - Case-Based Reasoning (CBR): It solves a new problem by retrieving and reusing a similar case (a problem-solution pair) from a case base, and optionally revising and retaining the new case for future use.