### Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be mined from different types of data, such as transactions, sequences, graphs, or text documents.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data .
- Frequent pattern based clustering methods can be divided into two categories: frequent itemset based clustering and frequent term based clustering.
  - Frequent itemset based clustering uses frequent itemsets (such as sets of products purchased together) to cluster data points that share common itemsets. For example, customers who buy similar products can be grouped into the same cluster.
  - Frequent term based clustering uses frequent terms (such as words or phrases) to cluster text documents that contain common terms. For example, news articles that cover similar topics can be grouped into the same cluster.
- Frequent pattern based clustering methods can use different algorithms to mine frequent patterns, such as the Apriori algorithm, the FP-growth algorithm, or the Eclat algorithm .
  - The Apriori algorithm uses a bottom-up approach to find frequent itemsets by iteratively generating candidate itemsets and pruning the ones that are not frequent.
  - The FP-growth algorithm uses a tree structure to store the frequent itemsets and grows the tree by adding new transactions. It avoids generating candidate itemsets and scanning the database multiple times.
  - The Eclat algorithm uses a vertical data format to store the transactions and finds frequent itemsets by intersecting the transaction identifiers of the items. It reduces the size of the data and the number of database scans.