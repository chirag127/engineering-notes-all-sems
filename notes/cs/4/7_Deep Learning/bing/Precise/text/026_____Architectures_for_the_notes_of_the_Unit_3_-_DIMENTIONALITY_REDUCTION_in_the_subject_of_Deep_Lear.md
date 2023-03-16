### Architectures for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

1. **Autoencoder**: An autoencoder is a type of neural network that learns to compress data from the input layer to the latent layer, then decompress it back to the output layer. The goal is to reconstruct the input data as accurately as possible, while reducing the dimensionality of the data in the latent layer.

2. **Principal Component Analysis (PCA)**: PCA is a statistical technique that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components.

3. **t-Distributed Stochastic Neighbor Embedding (t-SNE)**: t-SNE is a nonlinear dimensionality reduction technique that is particularly well-suited for embedding high-dimensional data into a space of two or three dimensions, which can then be visualized in a scatter plot.

4. **Linear Discriminant Analysis (LDA)**: LDA is a method used to find a linear combination of features that characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier or, more commonly, for dimensionality reduction before later classification.

5. **Isomap**: Isomap is a nonlinear dimensionality reduction method that seeks to preserve the geodesic distances between all pairs of data points. It does this by constructing a neighborhood graph, computing the shortest path between all pairs of points, and then using classical multidimensional scaling to embed the data in a lower-dimensional space.

6. **Locally Linear Embedding (LLE)**: LLE is a nonlinear dimensionality reduction technique that seeks to preserve the local structure of the data. It does this by finding a set of weights for each data point that best reconstructs it from its neighbors, and then using these weights to compute a low-dimensional embedding of the data.

7. **Uniform Manifold Approximation and Projection (UMAP)**: UMAP is a dimensionality reduction technique that seeks to preserve both the local and global structure of the data. It does this by constructing a fuzzy simplicial complex from the data, and then optimizing an embedding of this complex in a lower-dimensional space.

These are some of the common architectures used for dimensionality reduction in deep learning. Each method has its own strengths and weaknesses, and the choice of method will depend on the specific needs of the task at hand. It is important to understand the underlying principles of each method in order to make an informed decision about which one to use.