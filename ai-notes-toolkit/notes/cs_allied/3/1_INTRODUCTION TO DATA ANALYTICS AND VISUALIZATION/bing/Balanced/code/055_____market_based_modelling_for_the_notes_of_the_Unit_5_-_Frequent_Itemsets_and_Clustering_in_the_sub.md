# Market Based Modelling for Frequent Itemsets and Clustering

- Market based modelling is a data mining technique that assumes that there are two kinds of entities: items and baskets.
- Items are the products or services that are sold or offered in a market, such as books, movies, groceries, etc.
- Baskets are the collections of items that are purchased or consumed by customers, such as shopping carts, orders, transactions, etc.
- There is a many-to-many relationship between items and baskets, meaning that each basket can contain multiple items, and each item can belong to multiple baskets.
- The goal of market based modelling is to find patterns and associations among the items and baskets, such as which items are frequently bought together, which items are complementary or substitutable, which items influence the purchase of other items, etc.
- These patterns and associations can help in understanding customer behavior, preferences, and needs, as well as in improving marketing strategies, product recommendations, cross-selling, up-selling, etc.

## Frequent Itemsets

- A frequent itemset is a set of items that occurs in a large number of baskets, exceeding a given threshold .
- For example, if the threshold is 50%, then a frequent itemset is a set of items that appears in more than half of the baskets in the data.
- Finding frequent itemsets is the first step in market based modelling, as it helps in identifying the most popular and profitable items and combinations in the market.
- The frequency of an itemset is measured by its support, which is the fraction of baskets that contain the itemset.
- For example, if there are 100 baskets in the data, and 60 of them contain the itemset {bread, butter}, then the support of {bread, butter} is 60/100 = 0.6.
- The support threshold is the minimum support required for an itemset to be considered frequent.
- For example, if the support threshold is 0.5, then only itemsets with support at least 0.5 are frequent.
- The problem of finding frequent itemsets is challenging because there are exponentially many possible itemsets to consider, and scanning the entire data for each itemset is inefficient.
- Therefore, various algorithms have been developed to find frequent itemsets efficiently, such as the A-Priori algorithm, the FP-Growth algorithm, the Eclat algorithm, etc.
- These algorithms exploit the properties of frequent itemsets, such as the downward closure property, which states that if an itemset is frequent, then all its subsets are also frequent.
- This property allows the algorithms to prune the search space by eliminating itemsets that have infrequent subsets, and thus reduce the number of scans and computations.

## Clustering

- Clustering is a data mining technique that groups similar items or baskets together, based on some measure of similarity or distance.
- Clustering can help in discovering the structure and patterns in the data, as well as in segmenting the market into different categories or niches.
- Clustering can also be applied to the frequent itemsets, to find groups of items that are frequently bought together by similar customers.
- For example, clustering can reveal that customers who buy books and movies also buy music and games, while customers who buy groceries and household items also buy health and beauty products.
- Clustering can be performed by various algorithms, such as k-means, hierarchical clustering, density-based clustering, etc.
- These algorithms differ in how they define and measure the similarity or distance between items or baskets, how they initialize and update the clusters, how they determine the number and size of the clusters, etc.
- The choice of the clustering algorithm depends on the characteristics and objectives of the data and the analysis.