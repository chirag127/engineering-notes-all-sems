### Linear Dimension Reduction Using Principal Component Analysis (PCA)

- Linear dimension reduction is a technique that aims to reduce the number of variables or features in a data set while preserving as much information as possible.
- Principal component analysis (PCA) is one of the most popular linear dimension reduction algorithms. It is a projection based method that transforms the data by projecting it onto a set of orthogonal (perpendicular) axes .
- The axes are called principal components (PCs) and they are ordered by the amount of variance they explain in the data. The first PC explains the most variance, the second PC explains the most variance among the remaining ones, and so on.
- The PCs are linear combinations of the original variables, and they are uncorrelated with each other. The coefficients of the linear combinations are called loadings and they indicate how much each variable contributes to each PC.
- PCA can be performed by using eigenvalue decomposition or singular value decomposition (SVD) of the covariance matrix or the correlation matrix of the data .
- PCA can be used for various purposes, such as data compression, data visualization, feature extraction, noise reduction, and data analysis  .
- PCA has some limitations, such as being sensitive to outliers, being affected by scaling of the variables, and being unable to capture nonlinear relationships in the data .