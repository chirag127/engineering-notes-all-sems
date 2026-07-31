# Market Based Modelling for Frequent Itemsets and Clustering

- Market based modelling is a data mining technique that assumes that there are two kinds of entities: items and baskets.
- Items are the products or services that are sold or purchased in a market, such as books, groceries, or movies.
- Baskets are the collections of items that are bought or sold together in a transaction, such as a shopping cart, a movie ticket, or a book order.
- There is a many-to-many relationship between items and baskets, meaning that a basket can contain multiple items, and an item can belong to multiple baskets.
- The goal of market based modelling is to discover patterns and associations among the items and baskets, such as which items are frequently bought together, which items are complementary or substitutable, or which items are popular or unpopular.
- Frequent itemsets are sets of items that occur together in a large number of baskets, exceeding a given threshold of frequency or support  .
- For example, if the threshold is 50%, then a frequent itemset is a set of items that appears in at least half of the baskets in the data.
- Finding frequent itemsets is a fundamental task in market based modelling, as it can reveal the preferences and behaviour of the customers, and help in marketing, recommendation, and cross-selling strategies.
- k-itemsets are itemsets that contain exactly k items, where k is a positive integer.
- For example, {bread, butter, cheese} is a 3-itemset, and {milk, eggs} is a 2-itemset.
- The frequency of an itemset is the number or percentage of baskets that contain the itemset.
- For example, if {bread, butter, cheese} appears in 100 out of 1000 baskets, then its frequency is 100 or 10%.
- Clustering is a data mining technique that groups similar items or baskets together based on some measure of similarity or distance.
- Clustering can help in finding the structure and patterns in the data, and segmenting the market into different categories or niches.
- Clustering can also be applied to the frequent itemsets, to find groups of items that are frequently bought together by similar customers.
- For example, one cluster of frequent itemsets might be {bread, butter, cheese, milk, eggs}, {bread, butter, jam, milk, coffee}, and {bread, cheese, ham, eggs, juice}, which represent the breakfast items.
- Another cluster of frequent itemsets might be {pizza, coke, ice cream}, {burger, fries, coke, ketchup}, and {nachos, salsa, cheese, coke}, which represent the fast food items.