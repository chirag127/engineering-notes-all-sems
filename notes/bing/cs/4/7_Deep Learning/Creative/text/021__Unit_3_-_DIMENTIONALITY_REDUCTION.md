## Unit 3 - DIMENTIONALITY REDUCTION

- Dimensionality reduction is the process of reducing the number of features or variables in a dataset, while preserving as much information as possible.
- Dimensionality reduction can be useful for several purposes, such as:
  - Reducing the computational cost and complexity of machine learning algorithms.
  - Improving the performance and accuracy of machine learning algorithms by removing irrelevant or redundant features.
  - Visualizing high-dimensional data in lower-dimensional spaces.
  - Discovering hidden patterns or structures in the data.
- There are two main types of dimensionality reduction techniques: feature selection and feature extraction.
  - Feature selection methods select a subset of the original features based on some criteria, such as correlation, variance, or information gain.
  - Feature extraction methods transform the original features into a new set of features that capture the most important information in the data, such as principal components, latent factors, or embeddings.
- Some of the common dimensionality reduction techniques are:
  - Principal component analysis (PCA): A linear feature extraction method that finds the directions of maximum variance in the data and projects the data onto a lower-dimensional subspace spanned by these directions.
  - Singular value decomposition (SVD): A matrix factorization method that decomposes a data matrix into three matrices: a matrix of left singular vectors, a diagonal matrix of singular values, and a matrix of right singular vectors. The singular vectors can be used as new features that capture the most information in the data.
  - Linear discriminant analysis (LDA): A supervised feature extraction method that finds the directions that maximize the separation between different classes in the data and projects the data onto a lower-dimensional subspace spanned by these directions.
  - Non-negative matrix factorization (NMF): A matrix factorization method that decomposes a non-negative data matrix into two non-negative matrices: a matrix of basis vectors and a matrix of coefficients. The basis vectors can be used as new features that capture the most information in the data.
  - t-distributed stochastic neighbor embedding (t-SNE): A non-linear feature extraction method that preserves the local similarities between data points and maps them to a lower-dimensional space, where similar points are close and dissimilar points are far apart.
  - Autoencoders: A type of neural network that learns to encode the input data into a lower-dimensional representation and then decode it back to the original data. The lower-dimensional representation can be used as new features that capture the most information in the data.