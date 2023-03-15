# Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be extracted from different types of data, such as transactions, sequences, graphs, or text documents.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data .
- Frequent pattern based clustering methods can be divided into two main categories: frequent itemset based clustering and frequent term based clustering.

## Frequent Itemset Based Clustering
- Frequent itemset based clustering methods use frequent itemsets (sets of items that appear together in a minimum number of transactions) to cluster data points that share common itemsets.
- Frequent itemset based clustering methods can be further classified into two subcategories: partitioning methods and hierarchical methods.
- Partitioning methods divide the data into a predefined number of clusters, such as k-means or k-medoids, based on the similarity or distance between data points and cluster centers, which are represented by frequent itemsets.
- Hierarchical methods build a tree-like structure of clusters, such as agglomerative or divisive, based on the inclusion or exclusion of frequent itemsets in the clusters.
- Examples of frequent itemset based clustering methods are CLIQUE, MAFIA, PROCLUS, ORCLUS, and FPC.

## Frequent Term Based Clustering
- Frequent term based clustering methods use frequent terms (sequences of characters or words that appear frequently in text documents) to cluster text documents that share common terms.
- Frequent term based clustering methods can be further classified into two subcategories: document-pivot methods and term-pivot methods.
- Document-pivot methods assign each document to a cluster based on the similarity or distance between the document and the cluster center, which is represented by a set of frequent terms.
- Term-pivot methods assign each term to a cluster based on the similarity or distance between the term and the cluster center, which is represented by a set of documents.
- Examples of frequent term based clustering methods are FIHC, FTM, and FSC.

: Frequent Pattern Based Clustering Methods - Skedsoft
: Pattern-Growth Methods | SpringerLink
: Frequent Pattern Mining in Data Mining - GeeksforGeeks