# CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

## CLIQUE Algorithm

- CLIQUE is a **subspace clustering algorithm** that uses a **density and grid-based technique** to find clusters in high-dimensional data. 
- CLIQUE finds clusters by dividing each dimension into equal-width intervals and saving those intervals where the density is greater than a threshold as clusters. 
- CLIQUE can find clusters of any shape and is able to find any number of clusters in any number of dimensions, where the number is not predetermined by a parameter. 
- CLIQUE has four steps: 
  - **Identify dense units**: For each dimension, divide it into a number of intervals and count the number of points in each interval. A unit is an interval that has more points than the density threshold. A dense unit is a unit that is part of a cluster.
  - **Generate candidate subspace clusters**: For each pair of dense units that share all but one dimension, merge them into a candidate subspace cluster of higher dimensionality.
  - **Determine maximal subspace clusters**: A subspace cluster is maximal if it is not contained in any other subspace cluster. Prune the candidate subspace clusters that are not maximal.
  - **Generate minimal descriptions for clusters**: A minimal description for a cluster is the smallest set of dimensions that defines the cluster. Prune the dimensions that are not relevant for the cluster.

## ProCLUS Algorithm

- ProCLUS is a **projected clustering algorithm** that uses a **k-means-like technique** to find clusters in high-dimensional data. 
- ProCLUS finds clusters by randomly selecting k medoids and assigning each point to the nearest medoid. Then, for each medoid, it finds the most relevant dimensions for the cluster and projects the points onto those dimensions. Finally, it refines the medoids and the dimensions until convergence. 
- ProCLUS can find clusters of different shapes and sizes and is able to find the relevant dimensions for each cluster. 
- ProCLUS has four steps: 
  - **Initialization**: Randomly select k medoids and assign each point to the nearest medoid.
  - **Iterative phase**: For each medoid, find the most relevant dimensions for the cluster and project the points onto those dimensions. Then, recompute the medoids and reassign the points to the nearest medoid.
  - **Refinement phase**: Remove the outliers and the bad medoids and repeat the iterative phase.
  - **Final output**: Return the final medoids and the relevant dimensions for each cluster.