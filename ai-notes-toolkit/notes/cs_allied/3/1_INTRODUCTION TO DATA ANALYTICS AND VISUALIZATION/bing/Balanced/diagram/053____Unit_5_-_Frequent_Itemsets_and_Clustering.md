## Unit 5 - Frequent Itemsets and Clustering

- This unit covers two important topics in data mining: finding frequent itemsets and clustering data points.
- Frequent itemsets are sets of items that occur together frequently in a given dataset, such as products that are often bought together by customers.
- Clustering is the process of grouping data points into clusters based on their similarity or distance, such as customers with similar preferences or behaviors.
- Both topics are useful for discovering patterns and insights from large and complex data.

### Frequent Itemsets

- A frequent itemset is a set of items that has a support value above a given threshold in a dataset.
- The support value of an itemset is the fraction of transactions in the dataset that contain the itemset.
- For example, if the dataset has 100 transactions and 10 of them contain the itemset {bread, milk}, then the support value of {bread, milk} is 10/100 = 0.1.
- The threshold is also called the minimum support and is usually given as a parameter by the user.
- The goal of finding frequent itemsets is to identify the most common associations or co-occurrences among items in the dataset.
- For example, finding frequent itemsets from a supermarket dataset can help identify products that are often bought together and suggest cross-selling or marketing strategies.

#### Apriori Algorithm

- The Apriori algorithm is a classic and widely used method for finding frequent itemsets from a transactional dataset.
- The algorithm is based on the following principle: if an itemset is frequent, then all its subsets are also frequent.
- This principle is also called the Apriori property and it allows the algorithm to prune the search space and avoid checking all possible itemsets.
- The algorithm works as follows:

  - Start with the set of all single-item itemsets (called 1-itemsets) and scan the dataset to compute their support values.
  - Prune the itemsets that have a support value below the minimum support and keep the remaining itemsets as the frequent 1-itemsets.
  - Generate the candidate 2-itemsets by joining the frequent 1-itemsets with each other and scan the dataset to compute their support values.
  - Prune the itemsets that have a support value below the minimum support and keep the remaining itemsets as the frequent 2-itemsets.
  - Repeat the above steps by increasing the size of the itemsets by one until no more frequent itemsets can be generated.

- The output of the algorithm is the set of all frequent itemsets in the dataset.

#### Association Rules

- Association rules are rules that express the relationship between items in a frequent itemset, such as {bread, milk} -> {butter}, which means that if a transaction contains bread and milk, then it is likely to contain butter as well.
- Association rules can be derived from frequent itemsets by splitting them into two parts: the antecedent (left-hand side) and the consequent (right-hand side).
- For example, from the frequent itemset {bread, milk, butter}, we can derive three association rules: {bread, milk} -> {butter}, {bread, butter} -> {milk}, and {milk, butter} -> {bread}.
- Association rules can be evaluated by two measures: confidence and lift.
- The confidence of a rule is the fraction of transactions that contain the antecedent and the consequent among those that contain the antecedent.
- For example, the confidence of the rule {bread, milk} -> {butter} is the number of transactions that contain bread, milk, and butter divided by the number of transactions that contain bread and milk.
- The confidence of a rule measures how often the rule is true in the dataset.
- The lift of a rule is the ratio of the confidence of the rule to the expected confidence of the rule if the antecedent and the consequent were independent.
- For example, the lift of the rule {bread, milk} -> {butter} is the confidence of the rule divided by the support value of {butter}.
- The lift of a rule measures how much the rule deviates from the independence assumption and how much the antecedent and the consequent are associated.
- The goal of finding association rules is to identify the most interesting and useful rules from the frequent itemsets that can reveal the hidden patterns and relationships among items in the dataset.

### Clustering

- Clustering is the process of partitioning a set of data points into groups or clusters such that the data points in the same cluster are more similar or closer to each other than to those in other clusters.
- Clustering is an unsupervised learning technique, which means that the data