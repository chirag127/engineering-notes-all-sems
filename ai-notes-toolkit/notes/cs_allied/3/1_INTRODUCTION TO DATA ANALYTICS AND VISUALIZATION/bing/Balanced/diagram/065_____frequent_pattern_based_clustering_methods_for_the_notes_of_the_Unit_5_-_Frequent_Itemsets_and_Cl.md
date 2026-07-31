### Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be extracted from different types of data, such as transactions, sequences, graphs, or text documents, using various algorithms, such as Apriori, FP-Growth, or PrefixSpan.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data, where each subspace is represented by a set of frequent itemsets.
- Frequent pattern based clustering methods can also be used for classification and feature selection, by finding the discriminative frequent patterns that distinguish different classes or clusters of data.
- Frequent pattern based clustering methods can be applied to various domains, such as market basket analysis, web mining, bioinformatics, text mining, and social network analysis.

Some examples of frequent pattern based clustering methods are:

- Frequent term based text clustering: This method clusters text documents based on the frequent terms they contain, using a term-document matrix and a similarity measure. It can also use a hierarchy of frequent terms to capture the semantic structure of the documents.
- Frequent itemset based subspace clustering: This method clusters data points based on the frequent itemsets they share, using a bottom-up approach that starts from single items and grows the itemsets until they become infrequent. It can also use a top-down approach that starts from maximal frequent itemsets and splits them until they become too small.
- Frequent pattern based projected clustering: This method clusters data points based on the frequent patterns they share in different projections of the data, using a two-step approach that first finds the frequent patterns in each projection and then assigns the data points to clusters based on their pattern membership. It can also use a one-step approach that simultaneously finds the frequent patterns and the clusters.