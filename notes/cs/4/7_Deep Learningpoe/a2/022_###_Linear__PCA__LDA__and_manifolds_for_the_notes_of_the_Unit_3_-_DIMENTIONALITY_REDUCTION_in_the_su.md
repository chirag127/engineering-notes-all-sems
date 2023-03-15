 Here is the content in markdown format for the topic ### Linear (PCA, LDA) and manifolds for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning:

### Linear Dimensionality Reduction

- PCA (Principal Component Analysis): Finds the principal components (directions of maximum variance) of the data and projects it onto a lower dimensional space using these components. Preserves as much of the variance as possible. Useful for visualization and compression.
- LDA (Linear Discriminant Analysis): Finds the projection that maximizes the separation between classes (discriminates between classes). Useful for classification tasks.

Advantages:
- Simple and efficient to compute
- Non-linear relationships in the data may be ignored
- Sensitive to outliers

Disadvantages:
- Only considers linear relationships in the data

### Manifold Learning

- Locally Linear Embedding (LLE): Preserves local neighborhoods and reconstructs data points from neighbors.
- Isomap: Preserves geodesic distances (distances along the manifold)
- t-SNE: Converts similarities between data points to joint probabilities and minimizes the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embeddings and the high-dimensional data. Often produces 2D or 3D visualizations that preserve the "shape" of the data.

Advantages:
- Can capture non-linear structure in the data
- Often produces more visually appealing and interpretable results

Disadvantages:
- Computationally more expensive
- Sensitive to tuning parameters
- Difficult to extend to new data points

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.