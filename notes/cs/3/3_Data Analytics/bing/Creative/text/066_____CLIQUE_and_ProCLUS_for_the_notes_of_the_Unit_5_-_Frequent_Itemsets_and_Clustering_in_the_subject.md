### CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

- CLIQUE is a **subspace clustering algorithm** that uses a **density and grid-based technique** to find clusters in high-dimensional data. 
- CLIQUE works by dividing each dimension into equal-width intervals and saving those intervals where the density is greater than a threshold as clusters. 
- CLIQUE then merges adjacent intervals in each dimension to form **subspace clusters**, which are clusters that exist in some subset of dimensions. 
- CLIQUE can find clusters of any shape and size, and does not require the number of clusters or dimensions to be predetermined. 
- CLIQUE has been criticized for its high sensitivity to the input parameters, which can lead to very different results. 

- ProCLUS is a **projected clustering algorithm** that uses a **k-means and medoid-based technique** to find clusters in high-dimensional data. 
- ProCLUS works by randomly selecting k medoids and assigning each point to the nearest medoid. 
- ProCLUS then finds the **relevant dimensions** for each cluster, which are the dimensions that have low variance within the cluster and high variance between clusters. 
- ProCLUS then refines the clusters by removing outliers and reassigning points based on the relevant dimensions. 
- ProCLUS can find clusters that are well-separated and have similar shapes, and requires only the number of clusters as an input parameter. 
- ProCLUS has been criticized for its high computational complexity and sensitivity to noise and outliers. 

: https://rdrr.io/cran/subspace/man/CLIQUE.html
: https://www.geeksforgeeks.org/clique-algorithm-in-data-mining/
: https://towardsdatascience.com/subspace-clustering-7b884e8fff73
: https://theory.stanford.edu/~virgi/combclique-ipl-g.pdf
: https://en.wikipedia.org/wiki/Clique_problem
: https://www.cs.umd.edu/~samir/498/10Algorithms-08.pdf
: https://www.sciencedirect.com/science/article/pii/S0020025519308580