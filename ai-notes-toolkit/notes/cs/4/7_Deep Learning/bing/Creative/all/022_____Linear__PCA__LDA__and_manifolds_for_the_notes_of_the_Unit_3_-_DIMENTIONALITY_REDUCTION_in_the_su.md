# Linear (PCA, LDA) and Manifolds

## PCA (Principal Component Analysis)

- PCA is an unsupervised linear transformation technique that is used for dimensionality reduction.
- PCA aims to find the directions of maximum variance in the data and project the data onto a lower-dimensional subspace.
- PCA can be performed by eigenvalue decomposition or singular value decomposition of the covariance matrix of the data.
- PCA can help to detect patterns, outliers, and correlations in high-dimensional data, as well as to speed up clustering and classification algorithms.
- PCA assumes that the data lies on or close to a linear subspace, and may not be effective for nonlinear data.

## LDA (Linear Discriminant Analysis)

- LDA is a supervised linear transformation technique that is used for dimensionality reduction and classification.
- LDA aims to find the directions that maximize the separation between different classes of data, while minimizing the within-class variance.
- LDA can be performed by solving a generalized eigenvalue problem of the between-class scatter matrix and the within-class scatter matrix.
- LDA can help to improve the classification accuracy and reduce the computational cost of classification algorithms.
- LDA assumes that the data follows a multivariate normal distribution and that the classes have equal covariance matrices, which may not hold in practice.

## Manifolds

- Manifolds are mathematical objects that locally resemble a Euclidean space, but may have a complex global structure.
- Manifolds can be used to model nonlinear data that lies on a low-dimensional surface embedded in a high-dimensional space.
- Manifold learning is a family of nonlinear dimensionality reduction techniques that aim to find the intrinsic geometry of the data and preserve the local distances or angles in the lower-dimensional embedding.
- Manifold learning algorithms include MDS (Multidimensional Scaling), ISOMAP (Isometric Mapping), LLE (Locally Linear Embedding), Laplacian Eigenmaps, and t-SNE (t-distributed Stochastic Neighbor Embedding).
- Manifold learning can help to visualize and explore complex data, as well as to discover the latent features and structure of the data.
- Manifold learning requires a suitable distance metric or similarity measure to capture the local neighborhood structure of the data, and may be sensitive to noise, outliers, and parameter choices.