# Market Based Modelling

Market based modelling is a technique used in data analytics and visualization to identify patterns and relationships between items in large datasets. This technique is commonly used in market basket analysis, where the goal is to identify items that are frequently purchased together.

In market based modelling, the data is represented as a set of transactions, where each transaction is a set of items. The goal is to identify frequent itemsets, which are sets of items that appear together in a large number of transactions.

There are several algorithms that can be used to identify frequent itemsets, including the Apriori algorithm and the FP-growth algorithm. These algorithms work by iteratively generating candidate itemsets and counting their support in the dataset. The support of an itemset is the number of transactions that contain the itemset.

Once the frequent itemsets have been identified, association rules can be generated to describe the relationships between the items. Association rules are of the form "if X, then Y", where X and Y are itemsets. The strength of an association rule is measured by its confidence, which is the proportion of transactions that contain X that also contain Y.

Market based modelling can also be used for clustering, where the goal is to group similar items together. Clustering can be performed using techniques such as k-means clustering or hierarchical clustering.

In summary, market based modelling is a powerful technique for identifying patterns and relationships in large datasets. It is commonly used in market basket analysis, but can also be applied to other types of data. The key concepts in market based modelling are frequent itemsets, association rules, and clustering.