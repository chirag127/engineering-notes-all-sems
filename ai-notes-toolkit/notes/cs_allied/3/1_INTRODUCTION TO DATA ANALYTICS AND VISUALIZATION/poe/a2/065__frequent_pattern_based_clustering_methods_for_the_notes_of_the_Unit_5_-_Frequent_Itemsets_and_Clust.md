 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Frequent Pattern Based Clustering Methods

- Apriori algorithm: Used to find frequent itemsets in a dataset. These frequent itemsets are then used to generate association rules. The algorithm uses a bottom-up approach where it starts from finding frequent singleton items and then joining these to find larger frequent itemsets.
- Eclat algorithm: Uses a depth-first search approach to find frequent itemsets. It compresses the database into a frequent pattern tree (FP-tree) which stores itemset frequencies. This makes finding larger frequent itemsets more efficient than Apriori.
- FP-Growth algorithm: Also uses an FP-tree to find frequent itemsets. It is more efficient than Eclat as it does not need to search the tree multiple times for each larger itemset. Only a single scan of the tree is required.
- These frequent itemsets can then be used to cluster data points. Data points containing similar frequent itemsets will be put into the same cluster. This turns out to be an effective clustering technique when the inherent clusters in the data are based on the presence or absence of attributes. For example, clustering customers based on purchased products.

The above points cover the key frequent pattern based clustering methods. The content is written in a formal tone with points and no external links or emojis as specified. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.