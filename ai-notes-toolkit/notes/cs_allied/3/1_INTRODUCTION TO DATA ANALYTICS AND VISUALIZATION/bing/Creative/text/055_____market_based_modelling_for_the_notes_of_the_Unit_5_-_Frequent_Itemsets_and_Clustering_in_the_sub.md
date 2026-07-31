### Market Based Modelling for Frequent Itemsets and Clustering

- Market based modelling is a data mining technique that assumes that there are two kinds of entities: items and baskets.
- Items are the products or services that are sold or bought in a market, such as books, groceries, movies, etc.
- Baskets are the collections of items that are purchased or consumed together by a customer, such as a shopping cart, a movie ticket, a library loan, etc.
- There is a many-to-many relationship between items and baskets, meaning that a basket can contain multiple items and an item can belong to multiple baskets.
- The goal of market based modelling is to find patterns or associations among the items and baskets, such as which items are frequently bought together, which items are complementary or substitutable, which items are popular or unpopular, etc.
- These patterns or associations can help in various tasks, such as recommendation systems, cross-selling, customer segmentation, market analysis, etc.

- Frequent itemsets are one of the most common and useful patterns that can be discovered from market based modelling  .
- An itemset is a subset of items that occur together in some baskets, such as {bread, butter, milk}, {Harry Potter, Lord of the Rings}, {pizza, coke}, etc.
- A k-itemset is an itemset that contains k items, such as {bread, butter, milk} is a 3-itemset, {Harry Potter, Lord of the Rings} is a 2-itemset, {pizza} is a 1-itemset, etc.
- The frequency of an itemset is the number or proportion of baskets that contain that itemset, such as {bread, butter, milk} has a frequency of 10 if it occurs in 10 baskets out of 100, or 0.1 if it occurs in 10% of the baskets.
- A frequent itemset is an itemset that has a frequency above a given threshold, such as {bread, butter, milk} is a frequent itemset if the threshold is 0.05 and its frequency is 0.1, but not if the threshold is 0.2 and its frequency is 0.1.
- The threshold is usually set by the user or the application, depending on the level of granularity or specificity required.
- Finding frequent itemsets is important because they can reveal the preferences or behaviors of the customers, such as what items they like to buy together, what items they buy frequently, what items they rarely buy, etc.
- Finding frequent itemsets can also help in finding association rules, which are implications or correlations among the items, such as {bread, butter} => {milk}, meaning that customers who buy bread and butter are likely to buy milk as well.
- Association rules can help in making recommendations, predictions, or decisions based on the data, such as suggesting milk to a customer who buys bread and butter, or stocking milk near bread and butter in a store, or offering a discount on milk to a customer who buys bread and butter, etc.

- Clustering is another data mining technique that can be applied to market based modelling.
- Clustering is the process of grouping similar items or baskets into clusters, such that the items or baskets within a cluster are more similar to each other than to those in other clusters, according to some similarity measure, such as Euclidean distance, cosine similarity, Jaccard similarity, etc.
- Clustering can help in finding patterns or associations among the items or baskets, such as which items or baskets are similar or dissimilar, which items or baskets form natural groups or categories, which items or baskets are outliers or anomalies, etc.
- Clustering can help in various tasks, such as recommendation systems, customer segmentation, market analysis, anomaly detection, etc.

- Frequent itemsets and clustering are related but different concepts that can be used for market based modelling.
- Frequent itemsets focus on finding subsets of items that occur together frequently in the baskets, regardless of the similarity or dissimilarity of the items or the baskets.
- Clustering focuses on finding groups of items or baskets that are similar to each other, regardless of the frequency or infrequency of the items or the baskets.
- Frequent itemsets can be considered as a specific form of clustering designed for market basket data, where the similarity measure is based on the frequency of the itemsets, and the number of clusters is determined by the threshold.
- Clustering can be considered as a general form of finding patterns