 Here is the content in markdown format:

### Inception for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

Dimensionality reduction is a set of techniques used to reduce the number of features of a dataset. This is done to avoid overfitting and make learning algorithms faster and more efficient.

Some popular dimensionality reduction techniques are:

- Principal Component Analysis (PCA): Finds the principal components (directions of maximum variance) and projects the data onto a lower-dimensional space using only the most important components.
- Linear Discriminant Analysis (LDA): Projects the data onto a lower-dimensional space while preserving as much of the class-discriminatory information as possible.
- t-Distributed Stochastic Neighbor Embedding (t-SNE): Converts similarities between data points into joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data.
- Feature selection: Selects a subset of the original features. Can be done using statistical tests, wrapping methods, etc.

Mnemonics:
- PCA: Principal directions, max variance
- LDA: Preserves class-discriminatory info
- t-SNE: Minimizes KL divergence

Advantages:
- Reduced training time
- Avoid overfitting
- Visualization

Disadvantages:
- Loss of information
- Choosing the right technique and hyperparameter tuning can be difficult

Examples:
- PCA and LDA for face recognition
- t-SNE for visualization of high-dimensional data

Applications:
- Machine Learning
- Pattern Recognition
- Data Visualization
- Bioinformatics