 Here is the markdown content for ### metric learning for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning:

### Metric Learning
Metric learning is a set of methods that learn a distance metric from data. The goal is to learn a metric/distance function that can capture the intrinsic similarity between data points. Some of the commonly used metric learning methods are:

- Mahalanobis distance: Learns a linear transformation of the input space. It is parameterized by a positive semidefinite matrix.
- Large margin nearest neighbors (LMNN): Tries to separate samples of the same and different classes by at least a margin. It is trained by semidefinite programming.
- Information theoretic metric learning (ITML): Maximizes the mutual information between the distances and the labels. The metric is parameterized by a positive semidefinite matrix.
- Neighborhood components analysis (NCA): Maximizes the leave-one-out classification accuracy of a nearest neighbor classifier.

Advantages:
- Can lead to nonlinear decision boundaries and non-linear dimensionality reduction.
- The learned metrics can be more suitable for tasks like clustering and classification.

Disadvantages:
- Can be computationally expensive to train depending on the method.
- Risk of overfitting if the number of parameters is large relative to the number of training points.

Examples: Face verification, clustering, classification.

[Diagrams and examples can be added here for better understanding]

The mnemonics/learning tricks for metric learning methods could be:
- Mahalanobis: learns linear transformation (matrix multiplication)
- LMNN: Separates by margin (hyperplane)
- ITML: Maximizes mutual information (classification capability)
- NCA: Maximizes leave-one-out accuracy (neighborhood classification)