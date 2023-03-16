# Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be extracted from different types of data, such as transactions, sequences, graphs, texts, images, etc.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data .
- Frequent pattern based clustering methods can be divided into two main categories: frequent itemset based clustering and frequent term based clustering.

## Frequent Itemset Based Clustering
- Frequent itemset based clustering methods use frequent itemsets (sets of items that appear together in a minimum number of transactions) to cluster data points that share common itemsets.
- Frequent itemset based clustering methods can be further classified into two subcategories: partitioning methods and hierarchical methods.
- Partitioning methods divide the data into a predefined number of clusters, such as k-means or k-medoids, based on the similarity or distance between data points and cluster centers, which are represented by frequent itemsets.
- Hierarchical methods build a tree-like structure of clusters, such as agglomerative or divisive, based on the inclusion or exclusion of frequent itemsets in the data points, and then cut the tree at a certain level to obtain the final clusters.

## Frequent Term Based Clustering
- Frequent term based clustering methods use frequent terms (sequences of characters or words that appear frequently in a large collection of text documents) to cluster text documents that share common terms.
- Frequent term based clustering methods can be further classified into two subcategories: document-pivot methods and term-pivot methods.
- Document-pivot methods assign each document to a cluster based on the similarity or distance between the document and the cluster representative, which is a document that contains the most frequent terms in the cluster.
- Term-pivot methods assign each term to a cluster based on the similarity or distance between the term and the cluster representative, which is a term that co-occurs with the most frequent terms in the cluster, and then group the documents that contain the terms in the same cluster.

## Advantages and Disadvantages of Frequent Pattern Based Clustering Methods
- Some advantages of frequent pattern based clustering methods are:
  - They can discover clusters in different subspaces of the data, which can capture the local structures and correlations of the data .
  - They can handle high-dimensional data and reduce the dimensionality by selecting the most relevant features (frequent patterns) for clustering .
  - They can deal with different types of data, such as transactions, sequences, graphs, texts, images, etc., by applying different frequent pattern mining algorithms.
- Some disadvantages of frequent pattern based clustering methods are:
  - They can be computationally expensive and time-consuming, especially when the data is large and the frequent patterns are numerous .
  - They can be sensitive to the choice of parameters, such as the minimum support threshold for frequent pattern mining and the number of clusters for partitioning methods .
  - They can produce overlapping or nested clusters, which may not reflect the true structure of the data or the user's preference .

: https://www.skedsoft.com/books/data-mining-data-warehousing/frequent-pattern-based-clustering-methods
: https://link.springer.com/referenceworkentry/10.1007/978-0-387-39940-9_263
: https://www.geeksforgeeks.org/frequent-pattern-mining-in-data-mining/