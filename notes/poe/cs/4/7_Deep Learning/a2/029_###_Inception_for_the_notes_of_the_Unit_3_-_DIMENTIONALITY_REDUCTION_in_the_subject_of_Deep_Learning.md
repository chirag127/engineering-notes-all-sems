 Here is the content in markdown format:

### Inception for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

Dimensional reduction is a set of techniques used to reduce the number of features of a dataset. This is done to simplify the learning process and reduce overfitting. Some of the popular techniques are:

- Principal Component Analysis (PCA): PCA finds the "principal components" (directions of maximum variance) of the data and projects the data onto a lower-dimensional space using only the most significant principal components. This helps in removing correlated features and identifying patterns in the data.
- Linear Discriminant Analysis (LDA): LDA finds the projection that maximizes the separation between classes. It works well when the features are normally distributed. It can be seen as a supervised version of PCA.
- t-Distributed Stochastic Neighbor Embedding (t-SNE): t-SNE converts similarities between data points into joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data. It is good for visualizing high-dimensional data.
- Locally Linear Embedding (LLE): LLE preserves the local neighborhood structure of the data by reconstructing each data point using a weighted combination of its neighbors. The low-dimensional embedding is found by minimizing the reconstruction error.
- Isomap: Isomap preserves geodesic distances between points. It connects nearby points to construct a neighborhood graph and then applies MDS (multidimensional scaling) to find the low-dimensional embedding that preserves the geodesic distances.

Some useful mnemonics and learning tricks for Dimensionality Reduction techniques:

- PCA: Maximum variance, Remove correlation
- LDA: Class separation, Normally distributed features
- t-SNE: Probabilities, Minimize KL divergence
- LLE: Local neighbors, Reconstruction error
- Isomap: Geodesic distances, Multidimensional scaling

The techniques can be applied based on the use case and data structure. PCA and LDA are suitable for tabular/numerical data, t-SNE is good for visualization, LLE and Isomap can capture non-linear structures in the data.