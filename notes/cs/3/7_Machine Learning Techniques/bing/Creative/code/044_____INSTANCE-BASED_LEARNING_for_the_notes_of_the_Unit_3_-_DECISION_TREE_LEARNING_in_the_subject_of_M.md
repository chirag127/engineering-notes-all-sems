### INSTANCE-BASED LEARNING

- Instance-based learning is a family of learning algorithms that, instead of performing explicit generalization, compare new problem instances with instances seen in training, which have been stored in memory.
- It is also called memory-based learning or lazy learning, because computation is postponed until a new instance is observed, and no explicit model is built .
- Instance-based learning relies on some similarity measure to compare new instances with stored instances, and usually uses a weighted combination of the labels or predictions of the most similar instances  .
- Some of the advantages of instance-based learning are:
  - It can handle complex and nonlinear data without making any assumptions about the underlying distribution or structure .
  - It can adapt to changes in the data by adding or removing instances from memory, without retraining the whole model .
  - It can provide explanations for the predictions by showing the most similar instances and their labels .
- Some of the disadvantages of instance-based learning are:
  - It requires a large amount of memory to store all the instances, which can be costly and inefficient .
  - It can be slow to query new instances, especially if the similarity measure is complex or the number of instances is large .
  - It can be sensitive to noise, outliers, and irrelevant features, which can affect the similarity measure and the prediction accuracy  .
- Some of the instance-based learning algorithms are:
  - K Nearest Neighbor (KNN): It predicts the label of a new instance based on the majority vote of its k most similar instances in the training set .
  - Self-Organizing Map (SOM): It maps high-dimensional data into a low-dimensional grid of nodes, where each node represents a prototype of a cluster of similar instances.
  - Learning Vector Quantization (LVQ): It learns a set of prototypes for each class, and assigns a new instance to the class of the closest prototype.
  - Locally Weighted Learning (LWL): It fits a local model (such as a linear regression) to a new instance, using a weighted subset of the training instances that are close to the query point .
  - Case-Based Reasoning (CBR): It retrieves and adapts previous cases (or solutions) that are similar to a new problem, and stores the new case for future use.