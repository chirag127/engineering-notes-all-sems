# PCA for the notes of the Unit 3 - BI – DATA PREPARTTION in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS

- PCA stands for Principal Component Analysis, a dimensionality-reduction method that is often used to reduce the dimensionality of large data sets, by transforming a large set of variables into a smaller one that still contains most of the information in the large set.
- PCA is based on finding the principal components of the data, which are the directions of maximum variance in the data, and projecting the data onto a lower-dimensional subspace spanned by these principal components.
- PCA can be useful for BI and analytics because it can help to:
  - Simplify the data by reducing the number of variables and removing multicollinearity
  - Enhance the data quality by removing noise and outliers
  - Visualize the data by creating biplots that show the relationships between the variables and the observations
  - Identify the most informative features that explain the variance in the data
  - Perform clustering, classification, regression, or other analytical tasks on the reduced data
- The steps of PCA are:
  - Standardize the data to have zero mean and unit variance
  - Compute the covariance matrix of the data
  - Compute the eigenvalues and eigenvectors of the covariance matrix
  - Sort the eigenvalues in descending order and choose the top k eigenvalues and their corresponding eigenvectors, where k is the desired dimensionality of the reduced data
  - Form a matrix P with the k eigenvectors as columns
  - Transform the data by multiplying it with P, resulting in a k-dimensional matrix T
- The loadings of PCA are the coefficients that relate the original variables to the principal components. They can be computed by multiplying the standardized data with the eigenvectors. The loadings can be used to interpret the meaning of the principal components and to select the most relevant variables for each component.
- A biplot is a graphical display that shows both the principal components and the loadings in a single plot. It can help to visualize the variance in the data, the correlation between the variables, the contribution of each variable to each component, and the clustering of the observations. A biplot can be created by plotting the scores (the transformed data) and the loadings (scaled by a factor) on the same axes.
- An example of a biplot is shown below, using the iris data set:

![biplot](https://miro.medium.com/max/1400/1*0yY7Y0lQ6Z2Q6Z0w6Z2Q2Q.png)

- The biplot shows that the first principal component (PC1) captures the variance between the species, while the second principal component (PC2) captures the variance within the species. It also shows that the variables sepal length, sepal width, and petal length are positively correlated, while petal width is negatively correlated with the other variables. The biplot also shows that petal length and petal width are the most important variables for PC1, while sepal length and sepal width are the most important variables for PC2.
- Data preparation is the process of transforming raw data into a ready-to-use format for BI and analytics . It involves tasks such as cleaning, filtering, aggregating, joining, splitting, reshaping, and transforming the data . Data preparation can help to improve the data quality, consistency, and usability for BI and analytics .
- Data preparation can also incorporate or feed into data curation work that creates and oversees ready-to-use data sets for BI and analytics. Data curation involves tasks such as indexing, cataloging, and maintaining data sets and their associated metadata to help users find and access the data. Data curation can also involve enriching, annotating, and validating the data to ensure its accuracy, completeness, and relevance.