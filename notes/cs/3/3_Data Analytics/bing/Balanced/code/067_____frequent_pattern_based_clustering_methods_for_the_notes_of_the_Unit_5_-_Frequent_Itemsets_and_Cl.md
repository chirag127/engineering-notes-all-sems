### Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be extracted from different types of data, such as transactions, sequences, graphs, or text documents.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data .
- Frequent pattern based clustering methods can be divided into two categories: frequent itemset based clustering and frequent term based clustering.
  - Frequent itemset based clustering uses frequent itemsets (such as sets of products purchased together) to cluster transactional data or relational data. It can be further classified into two subcategories: partitioning based and hierarchical based.
    - Partitioning based methods use a bottom-up approach to find frequent itemsets and then assign data points to clusters based on their similarity to the frequent itemsets. Examples of partitioning based methods are CHARM, CLOPE, and PROCLUS.
    - Hierarchical based methods use a top-down approach to find frequent itemsets and then split the data into clusters based on the frequent itemsets. Examples of hierarchical based methods are BIRCH, ROCK, and CURE.
  - Frequent term based clustering uses frequent terms (such as words or phrases) to cluster text documents. It can be further classified into two subcategories: document based and term based.
    - Document based methods use a bottom-up approach to find frequent terms and then assign documents to clusters based on their similarity to the frequent terms. Examples of document based methods are FIHC, FICIA, and FIKM.
    - Term based methods use a top-down approach to find frequent terms and then split the documents into clusters based on the frequent terms. Examples of term based methods are FTM, FTM-DC, and FTM-TC.