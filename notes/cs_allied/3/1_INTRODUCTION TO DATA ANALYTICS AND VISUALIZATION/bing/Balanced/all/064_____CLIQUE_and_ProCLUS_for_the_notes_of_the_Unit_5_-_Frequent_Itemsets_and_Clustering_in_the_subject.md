# CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

## CLIQUE Algorithm

- CLIQUE is a **subspace clustering** algorithm that finds clusters in high-dimensional data by dividing each dimension into equal-width intervals and saving those intervals where the density is greater than a threshold as clusters .
- CLIQUE uses a **density and grid-based** technique that does not require the number of clusters or the shape of clusters to be predetermined.
- CLIQUE can handle **noise** and **outliers** by ignoring low-density regions.
- CLIQUE has four main steps:
  - **Partitioning**: Divide each dimension into a number of grids and identify the dense units (intervals) that have more points than the density threshold.
  - **Identifying**: Generate candidate clusters of different dimensions by combining adjacent dense units.
  - **Pruning**: Eliminate the candidate clusters that are not dense enough or are contained in larger clusters.
  - **Generating**: Output the final clusters that are maximal and non-redundant.
- CLIQUE has been criticized for its high **sensitivity** to the input parameters (the number of grids and the minimal density) which can lead to very different results. However, it is an essential algorithm in the family of **bottom-up** subspace clustering.

## ProCLUS Algorithm

- ProCLUS is a **projected clustering** algorithm that finds clusters in high-dimensional data by selecting a subset of dimensions (called a projection) for each cluster and assigning points to the closest cluster in the projection .
- ProCLUS uses a **k-means-based** technique that requires the number of clusters to be specified, but not the shape or size of clusters.
- ProCLUS can handle **noise** and **outliers** by using a statistical test to filter out irrelevant dimensions and points.
- ProCLUS has five main steps:
  - **Initialization**: Randomly select k points as cluster centers and k * l points as cluster representatives, where l is a parameter that controls the number of dimensions per cluster.
  - **Iterative Phase**: Repeat until convergence:
    - **Projection**: For each cluster, find the best l dimensions that have the highest average distance between the cluster center and the cluster representatives.
    - **Assignment**: For each point, assign it to the closest cluster in the projection, or mark it as an outlier if it is too far from any cluster.
    - **Refinement**: For each cluster, update the cluster center as the mean of the assigned points, and the cluster representatives as the farthest points from the center in the projection.
  - **Discarding**: Discard the clusters that have fewer than a minimum number of points, and reassign the points in the discarded clusters to the remaining clusters.
  - **Refinement**: For each cluster, remove the points that are farther than a threshold from the cluster center, and reassign them to the closest cluster or mark them as outliers.
  - **Output**: Output the final clusters, their projections, and the outliers.
- ProCLUS has been praised for its high **accuracy** and **efficiency** in finding clusters of different shapes and sizes in various domains. However, it is dependent on the **quality** of the initial cluster centers and representatives, and the **choice** of the parameters l and k.