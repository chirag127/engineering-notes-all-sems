 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Frequent Pattern Based Clustering Methods

1. Apriori Clustering:
- Uses Apriori algorithm to find frequent itemsets in the data.
- Clusters the transactions that contain the same frequent itemsets.
- Works well when clusters are characterized by shared items.

2. Eclat Clustering:
- Uses Eclat algorithm to find frequent itemsets.
- Clusters the transactions that contain the same frequent itemsets like Apriori clustering.
- Eclat is more efficient than Apriori as it uses a depth-first search approach.

3. Frequent Itemset Based Clustering (FIBC):
- Uses a two-step approach:
- First, find the frequent itemsets using any of the frequent itemset mining algorithms like Apriori or Eclat.
- Second, create clusters from frequent itemsets by assigning transactions that contain an itemset to the same cluster.
- The clusters are characterized by shared frequent itemsets.
- FIBC is flexible to use any frequent itemset mining algorithm.

The above methods create clusters based on finding common frequent itemsets in the transactions. They work well when the clusters in the data can be characterized by shared items or itemsets. The methods differ in the frequent itemset mining algorithm used like Apriori, Eclat, etc. FIBC is a generic approach that can use any frequent itemset mining algorithm.