### PCA for the notes of the Unit 3 - BI – DATA PREPARTTION in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS

- Principal Component Analysis (PCA) is a technique that reduces the dimensionality of large data sets by transforming a large set of variables into a smaller one that still contains most of the information in the large set.
- PCA is useful for data analysis, visualization, compression, de-noising, and feature extraction  .
- PCA works by finding the directions of maximum variance in the data, called principal components (PCs), and projecting the data onto a lower-dimensional space spanned by the PCs.
- The PCs are orthogonal to each other and are ordered by the amount of variance they explain. The first PC explains the most variance, the second PC explains the next most variance, and so on.
- The PCs can be represented as linear combinations of the original variables, and the coefficients of these linear combinations are called loadings. The loadings indicate how much each variable contributes to each PC.
- A biplot is a graphical tool that displays both the PCs and the loadings in a single plot. The biplot can help to interpret the PCs and to identify patterns and outliers in the data.
- To perform PCA, the data should be standardized (mean-centered and scaled by the standard deviation) to avoid the influence of different scales and units on the PCs.
- PCA can be implemented in Python using libraries such as scikit-learn, pandas, and matplotlib .