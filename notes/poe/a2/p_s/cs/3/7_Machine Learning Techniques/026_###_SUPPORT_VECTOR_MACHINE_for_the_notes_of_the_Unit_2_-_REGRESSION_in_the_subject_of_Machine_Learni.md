 Here is the content in markdown format for the topic ### SUPPORT VECTOR MACHINE for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques:

### SUPPORT VECTOR MACHINE

- SVM is a supervised learning model that uses associated labeling to classify data and regression analysis to estimate continuous variables.
- In SVM, data is plotted as points in an N-dimensional space (where N is the number of features) and an optimal hyperplane is constructed that separates the data points of one class from the other.
- The hyperplane is the line that maximally separates the two classes and is located equidistant from the closest data points of each class, known as support vectors.
- For linearly separable data, the hyperplane is a linear classifier but for non-linear data, the input space is mapped to a higher dimensional feature space using a kernel trick to construct optimal non-linear separating hyperplanes.
- SVM uses an optimization technique to find the hyperplane that gives the largest minimum distance to the closest point of each class, known as the margin. A good separation is achieved by the hyperplane with the largest margin.
- For regression, SVM finds a linear regression function that minimizes the error while maintaining a large margin. The trade-off between margin and error is controlled using a regularization parameter.
- Advantages: Effective in high dimensional spaces, uses a subset of training points in the decision function (support vectors), and memory efficient.
- Disadvantages: Sensitive to outliers, choosing kernel and parameters can be difficult, and cannot directly provide probability estimates.
- Applications: Image classification, object recognition, speaker identification, protein classification, stock prediction, etc.

[Add diagrams, examples, codes, etc if useful for learning]