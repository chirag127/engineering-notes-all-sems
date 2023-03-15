# CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

## CLIQUE

- CLIQUE is a **subspace clustering** algorithm that can find clusters of any shape and size in any number of dimensions .
- Subspace clustering is the task of finding clusters in subsets of dimensions, rather than in the full-dimensional space.
- CLIQUE uses a **grid-based** and **density-based** approach to identify clusters and subspaces  .
- Grid-based methods divide the data space into a grid structure and perform clustering on the grid cells.
- Density-based methods find clusters as maximal sets of connected dense units in the grid.
- CLIQUE has the following advantages  :
  - It does not require the number of clusters or subspaces as input parameters.
  - It can handle high-dimensional data efficiently and robustly.
  - It can find clusters of arbitrary shape and size.
  - It can discover clusters and subspaces simultaneously.
  - It can handle noise and outliers gracefully.
- CLIQUE has the following disadvantages  :
  - It depends on the grid size and the density threshold for finding clusters.
  - It may miss some clusters or subspaces if they are not aligned with the grid.
  - It may produce overlapping clusters or subspaces that are hard to interpret.
  - It may generate too many or too few clusters or subspaces depending on the data distribution.

## ProCLUS

- ProCLUS is a **projected clustering** algorithm that can find clusters in subspaces of the original data space .
- Projected clustering is a variant of subspace clustering that assumes that each cluster is associated with a subspace, rather than each subspace containing one or more clusters .
- ProCLUS uses a **k-means** and **dimension selection** approach to identify clusters and subspaces .
- K-means is a partitioning method that assigns data points to k clusters based on their distance to the cluster centroids.
- Dimension selection is a technique that selects the most relevant dimensions for each cluster based on their variance and correlation .
- ProCLUS has the following advantages :
  - It only requires the number of clusters as an input parameter, not the number or size of subspaces.
  - It can find clusters of different shapes and sizes in different subspaces.
  - It can handle high-dimensional data efficiently and effectively.
  - It can produce non-overlapping clusters and subspaces that are easy to interpret.
- ProCLUS has the following disadvantages :
  - It depends on the initial selection of cluster centroids and dimensions for finding clusters.
  - It may miss some clusters or subspaces if they are not well-separated or well-represented by the selected dimensions.
  - It may produce noisy or redundant clusters or subspaces if the data is sparse or skewed.
  - It may not handle noise and outliers well.

: https://www.geeksforgeeks.org/clique-algorithm-in-data-mining/
: https://www.tutorialspoint.com/what-is-clique
: https://github.com/georgekatona/Clique
: https://www.rdocumentation.org/packages/subspace/versions/1.0.4/topics/CLIQUE
: https://www.cse.unsw.edu.au/~weiw/project/proclus.html
: https://www.rdocumentation.org/packages/subspace/versions/1.0.4/topics/ProClus