### CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

#### CLIQUE

- CLIQUE is a **subspace clustering algorithm** that finds clusters in high-dimensional data by dividing each dimension into equal-width intervals and saving those intervals where the density is greater than a threshold as clusters .
- CLIQUE uses a **density and grid-based technique** to identify dense regions in subspaces of different dimensions.
- CLIQUE has four main steps :
  - Partitioning: Divide each dimension into a number of grids and count the number of points in each grid cell.
  - Identification: Identify the dense grid cells that have more points than the density threshold and form one-dimensional clusters.
  - Merging: Merge the adjacent one-dimensional clusters to form higher-dimensional clusters in a bottom-up manner.
  - Pruning: Eliminate the redundant clusters that are contained in other clusters.
- CLIQUE can find clusters of **any shape** and is able to find **any number of clusters** in **any number of dimensions**, where the number is not predetermined by a parameter.
- CLIQUE has been criticized for its **high sensitivity** to the input parameters (the number of bins and the minimal density) which can lead to very different results.

#### ProCLUS

- ProCLUS is a **projected clustering algorithm** that finds clusters in high-dimensional data by selecting a subset of dimensions (called a projection) for each cluster and assigning points to the closest cluster in the projection .
- ProCLUS uses a **k-medoids and dimensionality reduction technique** to identify the most relevant dimensions for each cluster and to reduce the noise and outliers .
- ProCLUS has four main steps :
  - Initialization: Select k medoids randomly from the data points and assign each point to the closest medoid.
  - Iterative Phase: For each medoid, find the best set of dimensions that have the lowest average distance to the medoid and assign points to the closest medoid in the projection.
  - Refinement Phase: Remove the bad medoids that have too few points or too many dimensions and reassign the points to the remaining medoids.
  - Final Phase: Fine-tune the clusters by reassigning the points to the closest medoid in the projection and updating the dimensions accordingly.
- ProCLUS can find clusters of **arbitrary shape** and is able to find **k clusters** in **a subset of dimensions**, where k is given by the user .
- ProCLUS has been praised for its **high accuracy and efficiency** compared to other clustering algorithms, such as k-means, DBSCAN, and CLIQUE .