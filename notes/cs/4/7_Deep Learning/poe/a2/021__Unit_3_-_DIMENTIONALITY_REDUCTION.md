 Here is the content in markdown format without any emojis or external links:

## Unit 3 - DIMENTIONALITY REDUCTION

1. Why dimensionality reduction?
- High dimensional data is hard to analyze and visualize.
- Reducing dimensions helps to remove redundancy in data and bring out essential features.
- It helps in faster learning algorithms and reduces training time.
- Prevents overfitting.

2. Feature selection
- Selecting subset of original features.
- Univariate - Select features with high scores like chi-square, information gain, correlation with target.
- Wrapper - Features are selected based on predictive power of the model.
- Embedded - Features selection is part of training process like in LASSO regression.

3. Feature extraction
- Combining features to get new set of features.
- Principal Component Analysis - Orthogonal transformation to convert correlated features into uncorrelated features. Eigenvectors with high eigenvalues are principal components.
- Linear Discriminant Analysis - Projects data onto a line/plane to maximize separation between classes. New features are linear combinations of original features.
- Kernels like polynomial can be used for non-linear dimensionality reduction.

4. Manifold learning
- Non-linear techniques to learn the low-dimensional manifold on which the data lies.
- Locally Linear Embedding - Reconstruct high-dimensional data from low-dimensional data preserving local distances.
- t-Distributed Stochastic Neighbor Embedding - Convert similarities between data points to joint probabilities and minimize Kullback-Leibler divergence.
- Isomap - Preserves geodesic distances (along the manifold) between points.

The content is written in a formal way with points and without any emojis or external links as per the instructions. Please let me know if you would like me to modify or add any other details to the content.