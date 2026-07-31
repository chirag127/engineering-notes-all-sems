## Unit 3 - Dimensionality Reduction

- Dimensionality reduction is the process of reducing the number of features or variables in a dataset, while preserving as much information as possible.
- Dimensionality reduction can be useful for several purposes, such as:
  - Improving the performance and efficiency of machine learning algorithms by reducing the computational complexity and the curse of dimensionality.
  - Enhancing the visualization and interpretation of high-dimensional data by projecting it onto a lower-dimensional space.
  - Removing noise and redundancy from the data by extracting the most relevant and informative features.
  - Finding hidden patterns and structures in the data by discovering latent variables or factors.
- Dimensionality reduction can be broadly classified into two categories: feature selection and feature extraction.
  - Feature selection is the process of selecting a subset of the original features that are most relevant and useful for the task at hand, without transforming or modifying them.
  - Feature extraction is the process of transforming or projecting the original features onto a new lower-dimensional space, where each new feature is a combination or function of the original features.
- Some of the common methods and techniques for dimensionality reduction are:
  - Principal Component Analysis (PCA): A feature extraction method that finds the linear combinations of the original features that capture the maximum variance in the data, and uses them as the new features.
  - Linear Discriminant Analysis (LDA): A feature extraction method that finds the linear combinations of the original features that maximize the separation between different classes or categories in the data, and uses them as the new features.
  - Singular Value Decomposition (SVD): A feature extraction method that decomposes a matrix of data into three matrices, such that the product of the three matrices is equal to the original matrix, and uses the singular values and vectors as the new features.
  - Non-negative Matrix Factorization (NMF): A feature extraction method that decomposes a non-negative matrix of data into two non-negative matrices, such that the product of the two matrices is approximately equal to the original matrix, and uses the factors or components as the new features.
  - t-distributed Stochastic Neighbor Embedding (t-SNE): A feature extraction method that maps the high-dimensional data onto a lower-dimensional space, such that the distances or similarities between the data points are preserved as much as possible, and uses the coordinates of the mapped points as the new features.
  - Autoencoders: A feature extraction method that uses a neural network to learn a compressed representation of the data, such that the input can be reconstructed from the output with minimal loss of information, and uses the hidden layer(s) of the network as the new features.