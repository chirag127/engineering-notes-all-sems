# CLIQUE and ProCLUS Algorithms

## CLIQUE Algorithm

- CLIQUE is a **subspace clustering** algorithm that finds clusters in high-dimensional data by dividing each dimension into equal-width intervals and saving those intervals where the density is greater than a threshold as clusters .
- CLIQUE uses a **density-based** and **grid-based** technique, which means it does not require a predefined number of clusters or a distance function, and it can find clusters of any shape.
- CLIQUE has four main steps :
  - **Partitioning**: The data space is partitioned into a grid of cells, and the cells with density above the threshold are marked as dense cells.
  - **Identifying**: The dense cells are grouped into connected components, which form the clusters in one-dimensional subspaces.
  - **Merging**: The clusters in lower-dimensional subspaces are merged to form clusters in higher-dimensional subspaces, if they share common dense cells.
  - **Pruning**: The clusters that are contained in other clusters are pruned, and the remaining clusters are the final output.
- CLIQUE has some advantages and disadvantages :
  - Advantages:
    - It can handle high-dimensional data and find clusters of any shape.
    - It is scalable and efficient, as it only scans the data once and uses a grid structure to store the density information.
    - It does not require a distance function or a number of clusters as input parameters, only the density threshold and the number of intervals.
  - Disadvantages:
    - It is sensitive to the input parameters, which can affect the quality and quantity of the clusters.
    - It can only find clusters that are aligned with the grid axes, and it may miss clusters that are skewed or curved.
    - It may produce overlapping clusters, which can be confusing or redundant.

## ProCLUS Algorithm

- ProCLUS is a **projected clustering** algorithm that finds clusters in high-dimensional data by selecting a subset of dimensions (called a projection) for each cluster, and assigning objects to the cluster with the closest projection.
- ProCLUS uses a **k-medoids** approach, which means it chooses representative objects (called medoids) for each cluster, and minimizes the distance between the objects and their medoids.
- ProCLUS has five main steps :
  - **Initialization**: The algorithm randomly selects k potential medoids from the data, and assigns each object to the closest medoid.
  - **Iterative refinement**: The algorithm iteratively updates the medoids and the assignments until convergence or a maximum number of iterations is reached.
  - **Dimension selection**: The algorithm selects a subset of dimensions for each cluster, based on the variance and correlation of the objects in the cluster.
  - **Final refinement**: The algorithm refines the medoids and the assignments using only the selected dimensions for each cluster, and removes outliers and empty clusters.
  - **Output**: The algorithm outputs the final clusters, their medoids, and their projections.
- ProCLUS has some advantages and disadvantages :
  - Advantages:
    - It can handle high-dimensional data and find clusters with different projections.
    - It is robust to noise and outliers, as it uses a k-medoids approach and removes them in the final refinement step.
    - It does not require a distance function, only a number of clusters and a maximum number of dimensions as input parameters.
  - Disadvantages:
    - It is sensitive to the input parameters, which can affect the quality and quantity of the clusters.
    - It can only find clusters that are convex and well-separated, and it may miss clusters that are overlapping or non-convex.
    - It may produce clusters with too many or too few dimensions, which can be misleading or incomplete.

: https://rdrr.io/cran/subspace/man/CLIQUE.html
: https://www.geeksforgeeks.org/clique-algorithm-in-data-mining/
: https://towardsdatascience.com/subspace-clustering-7b884e8fff73
: https://theory.stanford.edu/~virgi/combclique-ipl-g.pdf
: https://www.coursera.org/lecture/cluster-analysis/5-6-clique-grid-based-subspace-clustering-AAHTA
: https://www.cs.utexas.edu/users/ml/risc/papers