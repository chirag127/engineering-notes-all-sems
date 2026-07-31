### Market Based Modelling for Frequent Itemsets and Clustering

- Market based modelling is a data mining technique that assumes that there are two kinds of entities: items and baskets.
- Items are the products or services that are sold or offered in a market, such as books, movies, groceries, etc.
- Baskets are the collections of items that are purchased or consumed by customers, such as shopping carts, orders, transactions, etc.
- There is a many-to-many relationship between items and baskets, meaning that each basket can contain multiple items, and each item can belong to multiple baskets.
- The goal of market based modelling is to find patterns and associations among the items and baskets, such as which items are frequently bought together, which items are complementary or substitutable, which items influence the purchase of other items, etc.
- These patterns and associations can help in various tasks, such as recommendation systems, cross-selling, customer segmentation, market segmentation, etc .

- Frequent itemsets are one of the most common and useful patterns that can be discovered from market based modelling.
- A frequent itemset is a set of items that occur together in a large number of baskets, exceeding a certain threshold.
- For example, if the threshold is 50%, then a frequent itemset is a set of items that appear in more than half of the baskets in the data.
- The threshold is also called the minimum support, and it can be specified by the user or determined by the data characteristics.
- Finding frequent itemsets is important because they can reveal the preferences and behaviors of the customers, and they can also be used to generate association rules, which are conditional statements that imply a relationship between items.
- For example, if {bread, butter} is a frequent itemset, and {bread, butter} -> {jam} is an association rule with high confidence, then it means that customers who buy bread and butter are likely to buy jam as well.
- There are many algorithms for finding frequent itemsets, such as the Apriori algorithm, the FP-growth algorithm, the Eclat algorithm, etc.
- These algorithms differ in how they generate and prune the candidate itemsets, how they count the support of the itemsets, and how they store and access the data.
- The main challenge of finding frequent itemsets is to deal with the combinatorial explosion of the number of possible itemsets, especially when the data is large and sparse.

- Clustering is another data mining technique that can be applied to market based modelling.
- Clustering is the process of grouping similar items or baskets into clusters, such that the items or baskets within a cluster are more similar to each other than to those in other clusters.
- Clustering can help in discovering the underlying structure and diversity of the data, and it can also be used for data summarization, data compression, data visualization, etc.
- There are many types and methods of clustering, such as hierarchical clustering, partitioning clustering, density-based clustering, model-based clustering, etc.
- These methods differ in how they define and measure the similarity or distance between items or baskets, how they determine the number and shape of the clusters, and how they assign items or baskets to clusters.
- The main challenge of clustering is to find a suitable clustering method and parameters that can capture the meaningful and relevant patterns in the data, and that can also handle the noise, outliers, and high dimensionality of the data.

: Cloud Computing Lecture notes - UNIT IV FREQUENT ITEMSETS AND CLUSTERING
: clustering - How can I cluster products based on market basket data
: Frequent Itemsets and it’s applications in data analytics
: Frequent Itemsets (Chapter 6) - Mining of Massive Datasets - Cambridge Core