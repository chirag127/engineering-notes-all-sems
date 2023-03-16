# Market Based Modelling for Frequent Itemsets and Clustering

- Market based modelling is a data mining technique that assumes that there are two kinds of entities: items and baskets.
- Items are the products or services that are sold or bought in a market, such as books, groceries, movies, etc.
- Baskets are the collections of items that are purchased or consumed together by a customer, such as a shopping cart, a movie ticket, a library loan, etc.
- There is a many-to-many relationship between items and baskets, meaning that a basket can contain multiple items, and an item can belong to multiple baskets.
- The goal of market based modelling is to discover patterns and associations among the items and baskets, such as which items are frequently bought together, which items are complementary or substitutable, which items are popular or unpopular, etc.
- These patterns and associations can help in various tasks, such as recommendation systems, cross-selling, customer segmentation, market segmentation, etc.

## Frequent Itemsets

- A frequent itemset is a subset of items that occurs frequently in the baskets  .
- The frequency of an itemset is the number or proportion of baskets that contain all the items in the itemset.
- For example, if there are 100 baskets in total, and 20 of them contain both bread and butter, then the itemset {bread, butter} has a frequency of 20 or 0.2.
- A frequent itemset is an itemset that has a frequency above a given threshold, called the minimum support.
- The minimum support is a parameter that can be set by the user or the analyst, depending on the problem and the data.
- For example, if the minimum support is 0.1, then only the itemsets that have a frequency of at least 10 or 0.1 are considered frequent.
- Finding frequent itemsets is an important step in market based modelling, as it can reveal the common preferences and behaviors of the customers.
- Frequent itemsets can also be used to generate association rules, which are rules that express the conditional probability of one itemset given another itemset.
- For example, if the itemset {bread, butter} has a frequency of 0.2, and the itemset {bread} has a frequency of 0.5, then the association rule bread -> butter has a confidence of 0.4, meaning that 40% of the baskets that contain bread also contain butter.
- Association rules can help in identifying the relationships and dependencies among the items, such as which items are likely to be bought together, which items are likely to influence the purchase of other items, which items are likely to be bought after or before other items, etc.

## Clustering

- Clustering is a data mining technique that groups similar entities into clusters, such that the entities within a cluster are more similar to each other than to the entities in other clusters .
- Clustering can be applied to both items and baskets in market based modelling, depending on the objective and the data.
- For example, clustering items can help in finding the categories or genres of the items, such as books, movies, music, etc.
- Clustering baskets can help in finding the segments or profiles of the customers, such as loyal, occasional, impulsive, etc.
- Clustering can also be used to reduce the dimensionality or complexity of the data, by replacing the original entities with the cluster labels or centroids.
- Clustering can be performed using various algorithms and methods, such as k-means, hierarchical, density-based, etc.
- The choice of the algorithm and the method depends on the characteristics and the requirements of the data, such as the number, shape, size, and distribution of the clusters, the similarity or distance measure, the scalability and efficiency, etc.
- Clustering can help in discovering the patterns and trends in the data, such as which items or baskets are popular or unpopular, which items or baskets are similar or dissimilar, which items or baskets are outliers or anomalies, etc.
- Clustering can also help in improving the performance and accuracy of other data mining techniques, such as classification, prediction, recommendation, etc.