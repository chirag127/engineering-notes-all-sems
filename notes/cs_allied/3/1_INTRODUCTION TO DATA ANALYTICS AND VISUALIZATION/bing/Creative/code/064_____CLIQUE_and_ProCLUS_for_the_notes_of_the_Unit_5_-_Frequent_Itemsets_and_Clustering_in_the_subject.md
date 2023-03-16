### CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

- CLIQUE is a **subspace clustering** algorithm that finds clusters in high-dimensional data by dividing each dimension into equal-width intervals and selecting those intervals where the density is greater than a threshold .
- CLIQUE can find clusters of **any shape** and is able to find **any number of clusters** in any number of dimensions, where the number is not predetermined by a parameter.
- CLIQUE is a **bottom-up** approach that starts with one-dimensional clusters and then merges them into higher-dimensional clusters by finding their common intervals.
- CLIQUE has been criticized for its high sensitivity to the input parameters (the number of bins and the minimal density) which can lead to very different results.
- ProCLUS is a **projected clustering** algorithm that finds clusters in high-dimensional data by selecting a subset of dimensions (called medoids) for each cluster and assigning points to the closest cluster based on the distance in the selected dimensions.
- ProCLUS can find clusters of **arbitrary shape** and is able to find **a specified number of clusters** in a subset of dimensions, where the number is given by a parameter.
- ProCLUS is a **top-down** approach that starts with a random set of medoids and then iteratively refines them by finding the best dimensions and the best points for each cluster.
- ProCLUS has been criticized for its dependence on the initial medoids and the difficulty of choosing the optimal number of clusters and dimensions.

: https://rdrr.io/cran/subspace/man/CLIQUE.html
: https://www.geeksforgeeks.org/clique-algorithm-in-data-mining/
: https://towardsdatascience.com/subspace-clustering-7b884e8fff73
: https://www.cs.utexas.edu/~ml/papers/proclus-sigmod-99.pdf