# Apriori Algorithm

- Apriori algorithm is a data mining technique for finding frequent itemsets and association rules in a transactional database  .
- Frequent itemsets are sets of items that appear together in a minimum number of transactions, called the support threshold  .
- Association rules are implications of the form X -> Y, where X and Y are itemsets, meaning that transactions containing X are likely to contain Y as well  .
- Apriori algorithm uses a bottom-up approach, where it starts with finding the frequent individual items (1-itemsets) and then extends them to larger and larger itemsets as long as they are frequent  .
- Apriori algorithm uses two main steps: join and prune  .
  - Join step: generate candidate itemsets of size k by joining frequent itemsets of size k-1 with themselves  .
  - Prune step: eliminate candidate itemsets that have infrequent subsets using the Apriori property, which states that all subsets of a frequent itemset must be frequent  .
- Apriori algorithm repeats the join and prune steps until no more frequent or candidate itemsets can be generated  .
- Apriori algorithm can also generate association rules from the frequent itemsets by applying a minimum confidence threshold, which is the ratio of the support of the itemset to the support of its antecedent  .
- Apriori algorithm has some advantages and disadvantages  .
  - Advantages: easy to implement and understand, can handle large datasets, can be parallelized or distributed  .
  - Disadvantages: requires multiple scans of the database, may generate a huge number of candidate itemsets, may suffer from low support or confidence thresholds  .