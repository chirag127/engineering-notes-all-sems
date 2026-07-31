### Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be extracted from different types of data, such as transactions, sequences, graphs, or text documents, using various algorithms, such as Apriori, FP-Growth, or Eclat.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data, where each subspace is represented by a set of frequent itemsets.
- Frequent pattern based clustering methods can also be used for classification and feature selection, by finding the discriminative frequent patterns that distinguish different classes or groups of data.
- Some examples of frequent pattern based clustering methods are:

  - Frequent term based text clustering: This method clusters text documents based on the frequent terms they contain, using a term-document matrix and a similarity measure. A term can be a single word or a phrase, and the frequency of a term can be measured by its occurrence count or its inverse document frequency (IDF).
  - Frequent itemset based subspace clustering: This method clusters data points based on the frequent itemsets they share, using a transactional database and a minimum support threshold. A frequent itemset is a set of items that appears in at least a certain percentage of transactions. A subspace is a subset of dimensions that contains a frequent itemset.
  - Frequent pattern based projected clustering: This method clusters data points based on the frequent patterns they share, using a projected database and a minimum support threshold. A projected database is a subset of the original database that contains only the items relevant to a frequent pattern. A frequent pattern is a set of items that appears frequently in a projected database.