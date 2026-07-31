 Here is the formal notes on the topic "linear dimension reduction using principal component analysis (PCA)" in markdown format:

### Linear Dimension Reduction using Principal Component Analysis (PCA)

1. PCA is a unsupervised learning technique used to reduce the dimensionality of large data sets while retaining most of the information.
2. It achieves this by transforming the original dataset into a new reduced dataset using an orthogonal transformation. The new dataset has fewer features but still contains most of the information from the original dataset.
3. The transformation is defined in such a way that the first principal component has the largest possible variance. Each succeeding component has the highest possible variance while being uncorrelated with the preceding components.
4. The core steps in PCA are:
 - Standardize the data (to give equal weightage to features)
 - Calculate the covariance matrix
 - Calculate eigenvectors and eigenvalues of the covariance matrix
 - Select components (eigenvectors) based on the explained variance/eigenvalues
 - Project the original data onto the selected eigenvector components to get the transformed data
5. The number of components to retain can be determined using Scree plot, Kaiser criterion or cumulative explained variance.
6. The advantages of PCA are:
 - Reduces dimensionality and removes correlation between features.
 - Compresses data while retaining most information.
 - Greater computational efficiency and simpler models.
 - Visualization of high dimensional data.

The content is written in points and in a formal tone without any emojis or external links as requested. Please let me know if you would like me to modify or expand the notes in any way.