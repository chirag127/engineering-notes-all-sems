# CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

## CLIQUE

- CLIQUE is a **subspace clustering algorithm** that finds clusters in high-dimensional data by dividing each dimension into equal-width intervals and saving those intervals where the density is greater than a threshold as clusters .
- CLIQUE uses a **density and grid-based technique** to identify dense regions in subspaces of different dimensions.
- CLIQUE has the following advantages:
  - It can find clusters of **any shape** and size.
  - It can find clusters in **any number of dimensions**, where the number is not predetermined by a parameter.
  - It can handle **noise and outliers** by ignoring low-density regions.
  - It is **scalable** and **efficient** in both execution time and accuracy.
- CLIQUE has the following disadvantages:
  - It is **highly sensitive** to the input parameters (the number of bins and the minimal density) which can lead to very different results.
  - It may **miss clusters** that span across multiple bins or have varying densities.
  - It may **produce overlapping clusters** that are not well-separated.

## ProCLUS

- ProCLUS is a **projected clustering algorithm** that finds clusters in high-dimensional data by choosing a set of medoids and then removing outliers or redundant medoids until a desired number of clusters is left.
- ProCLUS works in a manner similar to **K-Medoids**, but instead of using all dimensions, it selects a subset of relevant dimensions for each cluster.
- ProCLUS has the following advantages:
  - It can find clusters of **arbitrary shape** and size.
  - It can **reduce the dimensionality** of the data by selecting only the most relevant dimensions for each cluster.
  - It can handle **noise and outliers** by removing them from the medoid set.
- ProCLUS has the following disadvantages:
  - It requires the **number of clusters** and the **average number of dimensions** per cluster as input parameters, which may be hard to estimate.
  - It may **miss clusters** that have different numbers of dimensions or are not well-represented by medoids.
  - It may **produce overlapping clusters** that are not well-separated.