### CLIQUE and ProCLUS for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

- CLIQUE is a subspace clustering algorithm that can find clusters of any shape and size in any number of dimensions .
- CLIQUE uses a grid-based approach to divide the data space into equal-width intervals and identify dense units that have more than a threshold number of data points  .
- CLIQUE starts from one-dimensional subspaces and merges adjacent dense units to form clusters. It then extends the clusters to higher-dimensional subspaces by joining clusters that share common dense units   .
- CLIQUE can automatically determine the number of clusters and subspaces without requiring user input. It can also handle noise and outliers by ignoring sparse units  .
- ProCLUS is another subspace clustering algorithm that uses a medoid-based approach to find clusters in different subspaces .
- ProCLUS first selects a set of medoids randomly from the data points and assigns each data point to its nearest medoid. It then iteratively refines the medoids and the clusters by computing the average subspace dimensionality and the subspace distance for each cluster  .
- ProCLUS can also automatically determine the number of clusters and subspaces by using a statistical test to filter out irrelevant dimensions and clusters  .
- ProCLUS can find clusters of different shapes and sizes, but it may not be able to handle noise and outliers well. It also requires the user to specify the maximum subspace dimensionality as a parameter  .

: https://www.geeksforgeeks.org/clique-algorithm-in-data-mining/
: https://www.tutorialspoint.com/what-is-clique
: https://github.com/georgekatona/Clique
: https://www.rdocumentation.org/packages/subspace/versions/1.0.4/topics/CLIQUE
: https://www.geeksforgeeks.org/proclus-algorithm-in-data-mining/
: https://www.tutorialspoint.com/what-is-proclus
: https://www.rdocumentation.org/packages/subspace/versions/1.0.4/topics/ProClus