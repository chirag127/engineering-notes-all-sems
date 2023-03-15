### Apriori algorithm

- Apriori algorithm is a data mining technique for finding frequent itemsets and association rules in a transactional database  .
- Frequent itemsets are sets of items that appear together in a minimum number of transactions, called the support threshold .
- Association rules are implications of the form X -> Y, where X and Y are itemsets, meaning that transactions containing X are likely to contain Y as well  .
- Apriori algorithm uses a bottom-up approach, where it starts with finding the frequent individual items (1-itemsets) and then extends them to larger and larger itemsets until no more frequent itemsets can be found  .
- Apriori algorithm uses two main steps: join and prune .
  - Join step: generate candidate itemsets of size k by combining frequent itemsets of size k-1 .
  - Prune step: eliminate candidate itemsets that have a subset that is not frequent .
- Apriori algorithm uses the property of downward closure, which states that any subset of a frequent itemset must be frequent  .
- Apriori algorithm has some advantages and disadvantages:
  - Advantages: easy to implement, scalable to large datasets, can handle sparse data, can incorporate user-specified constraints.
  - Disadvantages: requires multiple scans of the database, may generate a large number of candidate itemsets, may produce too many or too few rules depending on the support and confidence thresholds.