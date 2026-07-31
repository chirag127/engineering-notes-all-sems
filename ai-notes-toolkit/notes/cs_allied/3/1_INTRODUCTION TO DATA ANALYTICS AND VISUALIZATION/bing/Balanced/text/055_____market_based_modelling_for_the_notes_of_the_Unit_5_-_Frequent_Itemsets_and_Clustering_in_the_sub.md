### Market Based Modelling for Frequent Itemsets and Clustering

- Market based modelling is a data mining technique that assumes that there are two kinds of entities: items and baskets.
- Items are the products or services that are sold or offered in a market, such as books, movies, groceries, etc.
- Baskets are the collections of items that are purchased or consumed together by customers, such as shopping carts, movie tickets, restaurant orders, etc.
- There is a many-to-many relationship between items and baskets, meaning that each basket can contain multiple items, and each item can belong to multiple baskets.
- The goal of market based modelling is to find patterns and associations among the items and baskets, such as which items are frequently bought together, which items are complementary or substitutable, which items influence the purchase of other items, etc.
- These patterns and associations can help in various tasks, such as recommendation systems, cross-selling, customer segmentation, market segmentation, etc.

- Frequent itemsets are one of the most common and useful patterns that can be discovered from market based modelling  .
- An itemset is a subset of items that occur together in some baskets.
- A k-itemset is an itemset that contains k items, such as {bread, butter, jam} is a 3-itemset.
- The frequency of an itemset is the number or proportion of baskets that contain that itemset, such as {bread, butter, jam} has a frequency of 0.1 if it occurs in 10% of the baskets.
- A frequent itemset is an itemset that has a frequency above a given threshold, such as {bread, butter, jam} is a frequent itemset if the threshold is 0.05.
- The threshold is usually set by the user or the application, depending on the desired level of specificity and generality.
- Finding frequent itemsets is important because they can reveal the common preferences and behaviors of customers, as well as the relationships and dependencies among items.
- For example, if {bread, butter, jam} is a frequent itemset, it means that many customers like to buy these items together, and that these items are likely to be complementary or substitutable.

- Clustering is another data mining technique that can be applied to market based modelling.
- Clustering is the process of grouping similar items or baskets into clusters, such that the items or baskets within a cluster are more similar to each other than to those in other clusters.
- Clustering can help in finding the hidden structure and diversity of the data, as well as in reducing the complexity and dimensionality of the data.
- For example, clustering can help in identifying different types of customers, products, or markets, based on their purchase or consumption patterns.
- Clustering can also help in finding outliers or anomalies, such as customers who buy unusual combinations of items, or products that are rarely sold or bought.
- Clustering can be done in different ways, depending on the similarity measure, the clustering algorithm, and the number of clusters.
- One way to cluster items or baskets is to use frequent itemsets as a basis for similarity.
- For example, two items can be considered similar if they belong to many frequent itemsets together, and two baskets can be considered similar if they contain many frequent itemsets in common.
- This way, clustering can leverage the information and insights gained from frequent itemset mining, and vice versa.