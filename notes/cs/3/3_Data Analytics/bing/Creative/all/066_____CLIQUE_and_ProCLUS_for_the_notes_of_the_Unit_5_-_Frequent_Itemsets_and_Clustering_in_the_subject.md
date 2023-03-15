# CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

## CLIQUE

- CLIQUE is a **subspace clustering algorithm** that uses a **density and grid-based technique** to find clusters in high-dimensional data. 
- CLIQUE works by dividing each dimension into equal-width intervals and saving those intervals where the density of points is greater than a threshold as clusters. 
- CLIQUE then merges adjacent intervals in each dimension to form **units**, which are candidate clusters in one-dimensional subspaces. 
- CLIQUE then generates higher-dimensional candidate clusters by joining units that share common dimensions and have similar density values. 
- CLIQUE finally prunes the candidate clusters that are not dense enough or are contained in larger clusters, and outputs the remaining clusters as the final result. 
- CLIQUE has the following advantages: 
  - It can find clusters of **any shape** and size in any number of dimensions.
  - It does not require the number of clusters as an input parameter.
  - It is **scalable** and **efficient** as it uses a bottom-up approach and avoids redundant computations.
- CLIQUE has the following disadvantages: 
  - It is **sensitive** to the input parameters, such as the number of intervals and the density threshold, which can affect the quality and quantity of the clusters.
  - It can only find clusters that are **axis-parallel**, and may miss clusters that are oriented differently.
  - It may produce **overlapping** clusters that are not well-separated.

## ProCLUS

- ProCLUS is a **projected clustering algorithm** that uses a **k-means-like technique** to find clusters in high-dimensional data. 
- ProCLUS works by randomly selecting k points as **medoids**, which are representative points of the clusters. 
- ProCLUS then assigns each point to the nearest medoid, and computes the **average distance** of each point to its medoid. 
- ProCLUS then selects a subset of dimensions for each medoid, such that the average distance of the points in its cluster is minimized. These dimensions are called the **local dimensions** of the cluster. 
- ProCLUS then refines the medoids and the local dimensions by iteratively reassigning points and recomputing the average distances, until convergence or a maximum number of iterations is reached. 
- ProCLUS finally prunes the clusters that are not dense enough or are outliers, and outputs the remaining clusters as the final result. 
- ProCLUS has the following advantages: 
  - It can find clusters that are **non-axis-parallel**, and may capture the intrinsic structure of the data better.
  - It can find clusters that are **well-separated** and non-overlapping, and may avoid noise and redundancy.
  - It is **robust** to irrelevant dimensions, as it selects only the most relevant dimensions for each cluster.
- ProCLUS has the following disadvantages: 
  - It requires the number of clusters as an input parameter, which may be hard to estimate or vary depending on the application.
  - It relies on **random initialization** of the medoids, which may affect the quality and consistency of the clusters.
  - It may produce **empty clusters** or **small clusters** that are not representative of the data.