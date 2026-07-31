 Here are the notes for Linear (PCA, LDA) and manifolds for the Unit 3 - Dimensionality Reduction in Deep Learning:

### Principal Component Analysis (PCA)

- PCA is a linear dimensionality reduction technique.
- It transforms the data to a new coordinate system such that the greatest variance by any projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on.
- The transformation is defined in such a way that the first few principal components retain most of the variance present in all of the original variables.
- The input data is centered but not scaled before applying PCA.
- PCA can be computed using Singular Value Decomposition (SVD) of the data matrix.

### Linear Discriminant Analysis (LDA)

- LDA is a supervised linear dimensionality reduction technique.
- It projects the input data onto a lower-dimensional space while preserving as much of the class discriminatory information as possible.
- It finds the projection vectors (linear combinations of features) that maximize the separation between multiple classes.
- The goal is to project the data onto a line/plane that separates the different classes.
- LDA assumes that the data from each class follows a Gaussian distribution and uses class means and variances to determine the projection vectors.

### Manifold Learning

- Manifold learning techniques try to preserve the local structure of the data.
- They assume that the high-dimensional data lies on a lower-dimensional manifold and try to uncover the manifold structure.
- Some popular manifold learning techniques are Isomap, Local Linear Embedding (LLE), and t-Distributed Stochastic Neighbor Embedding (t-SNE).
- These techniques try to preserve distances between neighboring points and are typically nonlinear (although some have linear variants too).
- Manifold learning is typically more useful for visualization than linear techniques like PCA and LDA.

The notes are written in points and in a formal tone without any emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the notes in any way.