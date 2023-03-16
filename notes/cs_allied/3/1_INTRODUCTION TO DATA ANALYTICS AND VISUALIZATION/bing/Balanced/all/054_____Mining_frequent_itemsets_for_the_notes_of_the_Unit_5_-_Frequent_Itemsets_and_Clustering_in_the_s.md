# Mining frequent itemsets

- Frequent itemsets are sets of items that appear together in a transactional database above a certain threshold of support.
- Support is the fraction of transactions that contain an itemset.
- Mining frequent itemsets is the process of finding all the itemsets that have a support greater than or equal to a minimum support.
- Mining frequent itemsets is useful for discovering association rules, which are implications of the form X -> Y, where X and Y are itemsets and X does not contain any item in Y.
- Association rules have two measures of interest: confidence and lift.
- Confidence is the fraction of transactions that contain X and Y among those that contain X.
- Lift is the ratio of the observed support of X and Y to the expected support if X and Y were independent.
- Mining frequent itemsets is also useful for other data mining tasks, such as clustering, classification, and outlier detection.
- Mining frequent itemsets is challenging because the number of possible itemsets is exponential in the number of items, and the support of an itemset can only be computed by scanning the entire database.
- Several algorithms have been proposed to mine frequent itemsets efficiently, such as Apriori, Eclat, FP-Growth, and PrefixSpan.
- Apriori is a level-wise algorithm that generates candidate itemsets of size k from frequent itemsets of size k-1, and prunes the candidates that have infrequent subsets.
- Eclat is a depth-first algorithm that uses a vertical representation of the database, where each item is associated with a tidset, which is the set of transaction ids that contain the item.
- FP-Growth is a divide-and-conquer algorithm that compresses the database into a compact data structure called FP-tree, which preserves the itemset association information.
- PrefixSpan is a pattern-growth algorithm that mines frequent sequential patterns, which are ordered lists of items that appear in a sequence database.