## Unit 3 - Dimensionality Reduction

- Dimensionality reduction is the process of transforming data from a high-dimensional space into a low-dimensional space so that the low-dimensional representation retains some meaningful properties of the original data, ideally close to its intrinsic dimension.
- Dimensionality reduction can be done for various purposes, such as:
  - Reducing the complexity of a model and avoiding overfitting.
  - Improving the performance of a learning algorithm by reducing the computational cost and the noise in the data.
  - Making it easier to visualize and interpret the data by reducing the number of features.
- Dimensionality reduction can be divided into two main categories:
  - Feature selection: selecting a subset of the original features that are most relevant and informative for the task at hand.
  - Feature extraction: creating new features from the original features that capture the most variance or information in the data.
- Some common techniques for dimensionality reduction are :
  - Principal component analysis (PCA): a feature extraction technique that projects the data onto a lower-dimensional space that maximizes the variance of the data.
  - Singular value decomposition (SVD): a feature extraction technique that decomposes the data matrix into three matrices that capture the most important aspects of the data.
  - Linear discriminant analysis (LDA): a feature extraction technique that projects the data onto a lower-dimensional space that maximizes the separability of the classes.
  - Backward feature elimination: a feature selection technique that starts with all the features and iteratively removes the least important ones until a desired number of features is reached.
  - Forward feature selection: a feature selection technique that starts with no features and iteratively adds the most important ones until a desired number of features is reached.
  - Recursive feature elimination (RFE): a feature selection technique that combines backward and forward selection by recursively eliminating and adding features based on a ranking criterion.