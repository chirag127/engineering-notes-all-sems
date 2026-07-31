Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of linear (PCA, LDA) and manifolds for the unit 3 - dimensionality reduction in the subject of deep learning.

### Linear (PCA, LDA) and manifolds

- Dimensionality reduction is the process of reducing the number of features or variables in a dataset, while preserving the essential information or structure.
- Dimensionality reduction can be useful for data visualization, data compression, noise reduction, feature extraction, and computational efficiency.
- Linear dimensionality reduction methods assume that the data lies on or near a linear subspace of the original feature space.
- Principal component analysis (PCA) and linear discriminant analysis (LDA) are two popular linear dimensionality reduction methods.

#### Principal component analysis (PCA)

- PCA is an unsupervised method that aims to find the directions of maximum variance in the data, and project the data onto a lower-dimensional subspace spanned by these directions.
- PCA can be formulated as an eigenvalue problem, where the eigenvectors of the sample covariance matrix correspond to the principal components, and the eigenvalues correspond to the amount of variance explained by each component.
- PCA can also be formulated as an optimization problem, where the objective is to minimize the reconstruction error between the original data and the projected data, subject to an orthogonality constraint on the projection matrix.
- PCA can be computed using various algorithms, such as singular value decomposition (SVD), power iteration, or expectation-maximization (EM).

#### Linear discriminant analysis (LDA)

- LDA is a supervised method that aims to find the directions that best separate the data into different classes, and project the data onto a lower-dimensional subspace spanned by these directions.
- LDA can be formulated as a generalized eigenvalue problem, where the eigenvectors of the ratio of the between-class scatter matrix and the within-class scatter matrix correspond to the linear discriminants, and the eigenvalues correspond to the discriminability of each discriminant.
- LDA can also be formulated as an optimization problem, where the objective is to maximize the ratio of the between-class variance and the within-class variance, subject to an orthogonality constraint on the projection matrix.
- LDA can be computed using various algorithms, such as Fisher's algorithm, QR decomposition, or EM.

#### Manifolds

- Manifolds are mathematical objects that locally resemble a Euclidean space, but may have a more complex global structure.
- Manifolds can be used to model the intrinsic geometry of high-dimensional data that lies on or near a lower-dimensional nonlinear subspace of the original feature space.
- Manifold learning is the process of discovering and representing the manifold structure of the data, and projecting the data onto a lower-dimensional space that preserves the manifold structure.
- Manifold learning methods can be classified into two categories: global and local.

##### Global manifold learning methods

- Global manifold learning methods aim to preserve the global geometric properties of the data, such as distances, angles, or volumes, in the lower-dimensional space.
- Global manifold learning methods often require solving an eigenvalue problem or an optimization problem that involves the entire dataset, which can be computationally expensive and sensitive to noise and outliers.
- Examples of global manifold learning methods are multidimensional scaling (MDS), isometric mapping (Isomap), Laplacian eigenmaps, and spectral embedding.

##### Local manifold learning methods

- Local manifold learning methods aim to preserve the local geometric properties of the data, such as local distances, local linear relationships, or local densities, in the lower-dimensional space.
- Local manifold learning methods often require constructing a neighborhood graph or a local linear model for each data point, which can be computationally efficient and robust to noise and outliers, but may suffer from local minima or boundary effects.
- Examples of local manifold learning methods are locally linear embedding (LLE), local tangent space alignment (LTSA), Hessian LLE, and t-distributed stochastic neighbor embedding (t-SNE).