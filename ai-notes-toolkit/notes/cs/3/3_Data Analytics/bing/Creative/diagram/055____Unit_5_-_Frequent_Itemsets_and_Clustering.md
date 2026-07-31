## Unit 5 - Frequent Itemsets and Clustering

In this unit, you will learn about two important data mining tasks: finding frequent itemsets and clustering data points.

### Frequent Itemsets

- A frequent itemset is a set of items that occurs together in a dataset above a certain threshold of frequency or support.
- For example, if we have a dataset of supermarket transactions, a frequent itemset could be {bread, butter, milk}, meaning that these three items are often bought together by customers.
- Finding frequent itemsets is useful for discovering associations, correlations, or patterns among items in a dataset.
- For example, we can use frequent itemsets to generate association rules, such as {bread, butter} => {milk}, meaning that customers who buy bread and butter are likely to buy milk as well.
- Association rules can help us understand customer behavior, recommend products, or optimize marketing strategies.

### Clustering

- Clustering is the task of grouping data points into clusters, such that data points in the same cluster are similar to each other, and data points in different clusters are dissimilar to each other.
- For example, if we have a dataset of customers, we can cluster them based on their demographics, preferences, or purchase history, to segment them into different groups for analysis or targeting.
- Clustering is useful for exploring data, finding patterns, or reducing dimensionality.
- For example, we can use clustering to identify outliers, anomalies, or trends in data, or to compress data by representing each cluster by a representative point.

### Algorithms

- There are many algorithms for finding frequent itemsets and clustering data points, each with different advantages and disadvantages.
- Some of the most common algorithms are:

  - Apriori: an algorithm for finding frequent itemsets by iteratively generating and pruning candidate itemsets based on their support.
  - FP-Growth: an algorithm for finding frequent itemsets by constructing a compact data structure called a frequent pattern tree, and mining it recursively.
  - K-Means: an algorithm for clustering data points by randomly initializing k cluster centers, and iteratively assigning data points to the nearest center and updating the centers based on the assigned points.
  - DBSCAN: an algorithm for clustering data points by finding dense regions of data points, and expanding them into clusters based on a distance threshold and a minimum number of points.