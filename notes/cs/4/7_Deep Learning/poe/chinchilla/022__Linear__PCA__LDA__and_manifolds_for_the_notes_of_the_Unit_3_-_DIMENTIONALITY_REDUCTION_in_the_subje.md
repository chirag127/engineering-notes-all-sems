### Linear (PCA, LDA) and Manifolds for the Notes of the Unit 3 - Dimensionality Reduction in the Subject of Deep Learning

In this unit, we will learn about linear techniques for dimensionality reduction, namely Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA), and how they can be used to reduce the dimensionality of high-dimensional datasets. We will also discuss manifolds, which are a higher-level way to think about the structure of data in high-dimensional spaces.

#### Principal Component Analysis (PCA)

PCA is a linear technique that is used to reduce the dimensionality of high-dimensional datasets. It works by finding the principal components, which are the directions in the high-dimensional space along which the data varies the most. PCA then projects the data onto these principal components, which results in a lower-dimensional representation of the data.

The steps involved in PCA are as follows:

1. Standardize the data: This step involves scaling the data such that each feature has zero mean and unit variance.

2. Compute the covariance matrix: This step involves computing the covariance matrix of the standardized data.

3. Compute the eigenvectors and eigenvalues of the covariance matrix: This step involves computing the eigenvectors and eigenvalues of the covariance matrix. The eigenvectors represent the principal components, and the eigenvalues represent the amount of variance explained by each principal component.

4. Select the principal components: This step involves selecting the top k eigenvectors that correspond to the k largest eigenvalues. These k eigenvectors represent the top k principal components.

5. Project the data onto the selected principal components: This step involves projecting the standardized data onto the selected k principal components.

#### Linear Discriminant Analysis (LDA)

LDA is a linear technique that is used for supervised classification problems. It works by finding a linear combination of the features that maximizes the separation between the classes. LDA can also be used for dimensionality reduction by projecting the data onto the linear combination that separates the classes the most.

The steps involved in LDA are as follows:

1. Standardize the data: This step involves scaling the data such that each feature has zero mean and unit variance.

2. Compute the mean vectors for each class: This step involves computing the mean vector for each class.

3. Compute the within-class scatter matrix: This step involves computing the within-class scatter matrix, which measures the spread of the data within each class.

4. Compute the between-class scatter matrix: This step involves computing the between-class scatter matrix, which measures the separation between the classes.

5. Compute the eigenvectors and eigenvalues of the matrix (inv(Sw)Sb): This step involves computing the eigenvectors and eigenvalues of the matrix (inv(Sw)Sb), where Sw is the within-class scatter matrix and Sb is the between-class scatter matrix. The eigenvectors represent the linear combination of features that maximizes the separation between the classes.

6. Select the linear combination of features: This step involves selecting the top k eigenvectors that correspond to the k largest eigenvalues. These k eigenvectors represent the top k features that separate the classes the most.

7. Project the data onto the selected linear combination of features: This step involves projecting the standardized data onto the selected k features.

#### Manifolds

A manifold is a higher-level way to think about the structure of data in high-dimensional spaces. A manifold is a smooth, low-dimensional surface embedded in a high-dimensional space. Manifold learning algorithms attempt to discover this surface by using geometric insights from the data.

Manifold learning algorithms can be divided into two categories:

1. Global methods: Global methods attempt to preserve the global structure of the data. Examples of global methods include Isomap and Laplacian Eigenmaps.

2. Local methods: Local methods attempt to preserve the local structure of the data. Examples of local methods include Locally Linear Embedding (LLE) and t-SNE.

Manifold learning algorithms can be used for a variety of tasks, including visualization, denoising, and clustering.

In conclusion, linear techniques such as PCA and LDA can be used for dimensionality reduction, while manifolds provide a higher-level way to think about the structure of data in high-dimensional spaces. Understanding these concepts is crucial for anyone working with high-dimensional data in the field of deep learning.