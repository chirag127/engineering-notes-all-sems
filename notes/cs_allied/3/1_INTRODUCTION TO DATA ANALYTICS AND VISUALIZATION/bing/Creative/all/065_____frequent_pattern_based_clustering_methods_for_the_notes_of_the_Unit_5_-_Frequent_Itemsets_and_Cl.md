# Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be extracted from different types of data, such as transactions, sequences, graphs, or text documents.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data .
- Frequent pattern based clustering methods can be divided into two categories: frequent itemset based clustering and frequent term based clustering.

## Frequent Itemset Based Clustering
- Frequent itemset based clustering methods use frequent itemsets (sets of items that appear together in a minimum number of transactions) to cluster data points that share common itemsets.
- Frequent itemset based clustering methods can be further classified into two types: partitioning methods and hierarchical methods.
- Partitioning methods assign each data point to one of the predefined number of clusters based on the similarity of their frequent itemsets. Examples of partitioning methods are FPC (Frequent Pattern Clustering) and FPC-Stream (Frequent Pattern Clustering for Data Streams).
- Hierarchical methods build a tree-like structure of clusters based on the inclusion relationship of their frequent itemsets. Examples of hierarchical methods are CHARM (Clustering by Hierarchical Association Rule Mining) and ROCK (RObust Clustering using linKs).

## Frequent Term Based Clustering
- Frequent term based clustering methods use frequent terms (sequences of characters that appear frequently in text documents) to cluster text documents that share common terms.
- Frequent term based clustering methods can be further classified into two types: document clustering and feature clustering.
- Document clustering methods group documents based on the similarity of their frequent terms. Examples of document clustering methods are FIHC (Frequent Itemset-based Hierarchical Clustering) and FTM (Frequent Term Mining).
- Feature clustering methods group terms based on the similarity of their co-occurrence in documents. Examples of feature clustering methods are FPF (Frequent Pattern-based Feature) and FPF-Stream (Frequent Pattern-based Feature for Data Streams).