# CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

## CLIQUE

- CLIQUE is a **subspace clustering algorithm** that uses a **density and grid-based technique** to find clusters in high-dimensional data. 
- CLIQUE works by dividing each dimension into equal-width intervals and saving those intervals where the density of points is greater than a threshold as clusters. 
- CLIQUE then merges adjacent intervals in each dimension to form **subspaces** of higher dimensionality. 
- CLIQUE repeats this process until no more intervals can be merged or the maximum dimensionality is reached. 
- CLIQUE can find clusters of **any shape** and is able to find **any number of clusters** in **any number of dimensions**, where the number is not predetermined by a parameter. 
- CLIQUE has been criticized for its high sensitivity to the input parameters (the number of bins and the minimal density) which can lead to very different results. 

## ProCLUS

- ProCLUS is a **projected clustering algorithm** that uses a **k-means-like approach** to find clusters in high-dimensional data. 
- ProCLUS works by randomly selecting **k medoids** from the data and assigning each point to the closest medoid. 
- ProCLUS then determines the **relevant dimensions** for each cluster by finding the dimensions with the highest variance among the points in the cluster. 
- ProCLUS then refines the clusters by reassigning points to the closest medoid in the relevant dimensions and updating the medoids and the relevant dimensions. 
- ProCLUS repeats this process until convergence or a maximum number of iterations is reached. 
- ProCLUS can find clusters of **arbitrary shape** and is able to find **k clusters** in **a subset of dimensions**, where k is given by the user. 
- ProCLUS has been criticized for its dependence on the initial selection of medoids and the difficulty of choosing the appropriate value of k. 

: https://rdrr.io/cran/subspace/man/CLIQUE.html
: https://www.geeksforgeeks.org/clique-algorithm-in-data-mining/
: https://towardsdatascience.com/subspace-clustering-7b884e8fff73
: https://theory.stanford.edu/~virgi/combclique-ipl-g.pdf
: https://en.wikipedia.org/wiki/Clique_problem
: https://www.cs.utexas.edu/users/ml/risc/papers/proclus.pdf
: https://www.sciencedirect.com/science/article/pii/S0020025515001120