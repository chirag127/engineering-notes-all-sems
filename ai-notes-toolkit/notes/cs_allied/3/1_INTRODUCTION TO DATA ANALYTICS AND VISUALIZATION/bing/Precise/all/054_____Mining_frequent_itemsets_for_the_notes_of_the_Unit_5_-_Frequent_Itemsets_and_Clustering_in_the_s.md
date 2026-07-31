# Mining Frequent Itemsets

Frequent itemset mining is a technique used to identify sets of items that frequently occur together in a given dataset. This technique is commonly used in market basket analysis, where the goal is to find groups of items that are frequently purchased together by customers.

Here are some key points to remember when studying frequent itemset mining:

1. **Support:** The support of an itemset is the proportion of transactions in the dataset that contain the itemset. An itemset is considered frequent if its support is greater than or equal to a specified minimum support threshold.

2. **Apriori Algorithm:** The Apriori algorithm is a popular algorithm for mining frequent itemsets. It uses a bottom-up approach, where it starts by finding frequent individual items and then iteratively combines them to form larger itemsets.

3. **Association Rules:** Association rules are used to identify relationships between items in a dataset. They are typically written in the form "X -> Y", where X and Y are itemsets and the rule indicates that if a transaction contains X, it is likely to also contain Y.

4. **Confidence:** The confidence of an association rule is the proportion of transactions that contain X that also contain Y. It is used to measure the strength of the relationship between the two itemsets.

5. **Lift:** The lift of an association rule is the ratio of the observed support of X and Y together to the expected support if X and Y were independent. It is used to measure the significance of the relationship between the two itemsets.
