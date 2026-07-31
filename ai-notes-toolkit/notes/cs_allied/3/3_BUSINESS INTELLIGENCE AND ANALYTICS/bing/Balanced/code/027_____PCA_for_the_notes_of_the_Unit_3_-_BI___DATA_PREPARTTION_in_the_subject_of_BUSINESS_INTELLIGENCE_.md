# PCA for the notes of the Unit 3 - BI – DATA PREPARTTION in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS

- PCA stands for Principal Component Analysis, which is a dimensionality reduction technique that transforms a large set of variables into a smaller one that still contains most of the information in the large set.
- PCA is useful for BI and analytics because it can help to simplify the data, reduce noise, identify patterns, and reveal the most important features.
- The main steps of PCA are:
  - Standardize the data to have a mean of zero and a standard deviation of one.
  - Calculate the covariance matrix of the standardized data, which measures the linear relationship between each pair of variables.
  - Calculate the eigenvalues and eigenvectors of the covariance matrix, which represent the magnitude and direction of the principal components, respectively.
  - Choose the number of principal components to retain, based on the proportion of variance explained by each eigenvalue.
  - Project the original data onto the subspace spanned by the selected eigenvectors, which are the principal component scores .
- PCA can be visualized using a biplot, which is a plot that shows both the principal component scores and the principal component loadings. The loadings are the coefficients that relate the original variables to the principal components, and they indicate how much each variable contributes to each component.
- A biplot can help to interpret the PCA results by showing the correlation between the original variables, the clustering of the observations, the outliers, and the most influential features.
- Data preparation is the process of transforming raw data into a format that is suitable for BI and analytics. Data preparation can involve tasks such as cleaning, filtering, aggregating, merging, transforming, and enriching the data .
- Data preparation is essential for BI and analytics because it can improve the quality, accuracy, and usability of the data, as well as reduce the time and effort required for analysis .