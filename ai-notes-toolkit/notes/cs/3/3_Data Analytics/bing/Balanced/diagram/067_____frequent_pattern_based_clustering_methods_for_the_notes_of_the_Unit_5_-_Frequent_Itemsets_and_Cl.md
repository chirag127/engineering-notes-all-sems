### Frequent Pattern Based Clustering Methods

- Frequent pattern based clustering methods are a type of cluster analysis that use frequent patterns (such as sets of items or objects) that occur frequently in large data sets to group similar data points together.
- Frequent patterns can be extracted from different types of data, such as transactions, sequences, graphs, or text documents.
- Frequent pattern based clustering methods can handle high-dimensional data and discover clusters in different subspaces of the data .
- Frequent pattern based clustering methods can be divided into two main categories: frequent itemset based clustering and frequent term based clustering.
  - Frequent itemset based clustering uses frequent itemsets (such as sets of products purchased together) to cluster transactional data or other data that can be represented as binary vectors.
  - Frequent term based clustering uses frequent terms (such as words or phrases) to cluster text documents or other data that can be represented as term vectors.
- Some examples of frequent pattern based clustering algorithms are:
  - FP-Cluster: This algorithm uses the FP-Growth method to mine frequent itemsets and then assigns data points to clusters based on their similarity to the frequent itemsets.
  - FPC-Stream: This algorithm extends FP-Cluster to handle data streams by using a sliding window technique and a pruning strategy to update the frequent itemsets and clusters over time.
  - FPC-Doc: This algorithm applies FP-Cluster to text documents by using a term weighting scheme and a document similarity measure based on the frequent terms.
  - FPC-Graph: This algorithm applies FP-Cluster to graph data by using a graph mining method to extract frequent subgraphs and then clustering the graphs based on their similarity to the frequent subgraphs.
  - FPC-Seq: This algorithm applies FP-Cluster to sequence data by using a sequence mining method to extract frequent subsequences and then clustering the sequences based on their similarity to the frequent subsequences.
  - FPC-Tree: This algorithm applies FP-Cluster to tree data by using a tree mining method to extract frequent subtrees and then clustering the trees based on their similarity to the frequent subtrees.