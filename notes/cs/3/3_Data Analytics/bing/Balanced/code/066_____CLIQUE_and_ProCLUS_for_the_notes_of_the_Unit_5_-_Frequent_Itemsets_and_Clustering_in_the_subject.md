# CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

- CLIQUE and ProCLUS are two algorithms for subspace clustering, which is a technique to find clusters in high-dimensional data by considering only relevant subsets of dimensions for each cluster.
- CLIQUE stands for Clustering In QUEst and uses a density-based and grid-based approach to find clusters of arbitrary shape and size .
- ProCLUS stands for PROjected CLUStering and uses a medoid-based approach to find clusters of spherical shape and similar size.

## CLIQUE Algorithm

- The CLIQUE algorithm works as follows:
  - It divides each dimension into equal-width intervals and identifies the intervals that have a density of points above a given threshold as dense units.
  - It generates candidate clusters by combining adjacent dense units in each dimension.
  - It prunes the candidates that are not dense in the subspace defined by their dimensions.
  - It merges the remaining candidates that share common dense units into maximal clusters.
- The CLIQUE algorithm has the following advantages and disadvantages :
  - It can find clusters of any shape and size without prior knowledge of the number of clusters or the relevant dimensions.
  - It can handle noise and outliers by using density thresholding.
  - It is scalable and efficient as it uses a grid-based structure and avoids distance computations.
  - It is sensitive to the input parameters, such as the number of intervals and the density threshold, which can affect the quality and quantity of the clusters.
  - It can miss clusters that are not aligned with the grid or that have varying densities across dimensions.

## ProCLUS Algorithm

- The ProCLUS algorithm works as follows:
  - It randomly selects a set of medoids that is proportional to the desired number of clusters and assigns each point to its nearest medoid.
  - It removes the medoids that are outliers or that belong to clusters that are better represented by another medoid until the desired number of clusters is reached.
  - It computes the relevant dimensions for each cluster by selecting the dimensions that have low variance among the points assigned to the cluster.
  - It refines the clusters by reassigning the points to their nearest medoid in the subspace defined by the relevant dimensions and recomputing the medoids and the relevant dimensions iteratively until convergence.
- The ProCLUS algorithm has the following advantages and disadvantages:
  - It can find clusters of spherical shape and similar size in the relevant subspaces without prior knowledge of the dimensions.
  - It can handle noise and outliers by using medoid-based clustering and dimension selection.
  - It is scalable and efficient as it uses a small number of medoids and avoids distance computations in the full-dimensional space.
  - It is sensitive to the input parameters, such as the initial number of medoids and the variance threshold, which can affect the quality and quantity of the clusters.
  - It can miss clusters that are not spherical or that have different sizes across dimensions.