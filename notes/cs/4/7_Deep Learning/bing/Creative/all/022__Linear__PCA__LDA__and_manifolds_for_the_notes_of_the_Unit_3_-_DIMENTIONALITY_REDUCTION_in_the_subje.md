### Linear (PCA, LDA) and manifolds for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- Dimensionality reduction is the process of reducing the number of features to the most relevant ones in simple terms. It can help with data compression, noise reduction, data classification and data visualization.
- Linear dimensionality reduction techniques are based on linear transformations of the original features into a lower-dimensional space. They can be divided into two main approaches: projection and manifold learning.
- Projection techniques find a lower-dimensional subspace that lies closest to the data and preserves the distances between the points. Examples of projection techniques are PCA (Principal Component Analysis) and LDA (Linear Discriminant Analysis).
- Manifold learning techniques assume that the data lie on a lower-dimensional manifold embedded in a higher-dimensional space. They try to model the manifold and unfold it into a lower-dimensional representation. Examples of manifold learning techniques are t-SNE, UMAP and LLE.
- PCA is an unsupervised linear transformation technique that identifies the directions of maximum variance in the data and projects it onto a lower-dimensional feature space. It can be used for data visualization, noise filtering, feature extraction and data compression .
- LDA is a supervised linear transformation technique that finds the feature subspace that optimizes class separability. It can be used for data visualization, feature extraction and data classification .
- SVD (Singular Value Decomposition) is another linear dimensionality reduction technique that is very similar to PCA, but it does not center the data before computing the singular value decomposition. It can work with sparse matrices efficiently and can be used for data compression, noise filtering and feature extraction.
- A mnemonic to remember the difference between PCA and LDA is: PCA preserves variance, LDA preserves class.
- A mnemonic to remember the difference between SVD and PCA is: SVD does not subtract the mean, PCA does.
- A table to compare the main features of PCA, LDA and SVD is:

| Technique | Supervised/Unsupervised | Goal | Centering | Sparse matrices |
|-----------|-------------------------|------|----------|-----------------|
| PCA       | Unsupervised            | Maximize variance | Yes      | No              |
| LDA       | Supervised              | Maximize class separability | Yes      | No              |
| SVD       | Unsupervised            | Decompose matrix | No       | Yes             |