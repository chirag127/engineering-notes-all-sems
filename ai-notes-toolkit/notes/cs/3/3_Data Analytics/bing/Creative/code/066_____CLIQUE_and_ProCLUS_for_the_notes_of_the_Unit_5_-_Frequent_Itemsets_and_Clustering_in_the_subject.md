### CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

- CLIQUE is a **subspace clustering algorithm** that uses a **density and grid-based technique** to find clusters in high-dimensional data. 
- CLIQUE works by dividing each dimension into equal-width intervals and saving those intervals where the density is greater than a threshold as clusters. 
- CLIQUE then merges adjacent intervals in each dimension to form **units**, which are the building blocks of subspaces. 
- CLIQUE then finds the maximal units, which are the units that are not contained in any other unit, and generates the candidate subspaces from them. 
- CLIQUE then prunes the candidate subspaces that do not have enough density, and outputs the remaining ones as the final clusters. 
- CLIQUE has some advantages over other clustering algorithms, such as:
  - It can find clusters of any shape and size. 
  - It can handle noise and outliers. 
  - It does not require the number of clusters or the dimensions as input parameters. 
- CLIQUE also has some disadvantages, such as:
  - It is sensitive to the input parameters of the number of intervals and the density threshold, which can affect the quality and quantity of the clusters. 
  - It can generate redundant clusters that overlap in multiple subspaces. 
  - It can miss some clusters that are not dense enough in any subspace. 

- ProCLUS is another **subspace clustering algorithm** that uses a **projected clustering technique** to find clusters in high-dimensional data. 
- ProCLUS works by randomly selecting some points as **medoids**, which are the representatives of the clusters. 
- ProCLUS then assigns each point to the closest medoid, and computes the **dimensional relevance** of each dimension for each cluster, which is a measure of how important that dimension is for that cluster. 
- ProCLUS then prunes the dimensions that have low relevance for each cluster, and projects the points onto the remaining dimensions. 
- ProCLUS then refines the medoids and the assignments of the points, and repeats the process until convergence. 
- ProCLUS then outputs the final clusters and their relevant dimensions. 
- ProCLUS has some advantages over other clustering algorithms, such as:
  - It can find clusters that are arbitrarily oriented and shaped. 
  - It can handle noise and outliers. 
  - It can automatically determine the number of clusters and the relevant dimensions. 
- ProCLUS also has some disadvantages, such as:
  - It is sensitive to the input parameter of the number of medoids, which can affect the quality and quantity of the clusters. 
  - It can generate spurious clusters that are not meaningful in any subspace. 
  - It can miss some clusters that are not well-separated from other clusters. 

: https://rdrr.io/cran/subspace/man/CLIQUE.html
: https://www.geeksforgeeks.org/clique-algorithm-in-data-mining/
: https://towardsdatascience.com/subspace-clustering-7b884e8fff73
: https://theory.stanford.edu/~virgi/combclique-ipl-g.pdf
: https://en.wikipedia.org/wiki/Clique_problem
: https://www.cs.utexas.edu/users/ml/risc/papers/proclus.pdf