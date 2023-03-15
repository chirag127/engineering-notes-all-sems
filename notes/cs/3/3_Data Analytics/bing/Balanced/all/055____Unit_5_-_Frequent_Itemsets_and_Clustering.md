## Unit 5 - Frequent Itemsets and Clustering

- This unit covers two important topics in data mining: finding frequent itemsets and clustering data points.
- Frequent itemsets are sets of items that occur together frequently in a given dataset, such as products that are often bought together by customers.
- Clustering is the process of grouping data points into clusters based on their similarity or distance, such as customers with similar preferences or behaviors.
- Both topics are useful for discovering patterns and insights from large and complex data.

### Frequent Itemsets

- A frequent itemset is a set of items that has a support value above a given threshold in a dataset.
- The support value of an itemset is the fraction of transactions in the dataset that contain the itemset.
- For example, if the dataset has 100 transactions and 20 of them contain the itemset {bread, butter}, then the support value of {bread, butter} is 0.2.
- The threshold is also called the minimum support and is usually given as a parameter by the user.
- The goal of finding frequent itemsets is to identify the most common associations or co-occurrences among items in the dataset.
- For example, finding frequent itemsets can help a retailer to design effective marketing strategies, such as cross-selling or bundling products that are often bought together.

#### Apriori Algorithm

- The Apriori algorithm is a classic and widely used method for finding frequent itemsets in a dataset.
- The algorithm is based on the following principle: if an itemset is frequent, then all its subsets are also frequent.
- This principle is also called the Apriori property and it allows the algorithm to prune the search space and avoid checking all possible itemsets.
- The algorithm works as follows:

  - Start with the set of all single-item itemsets, called the 1-itemsets, and scan the dataset to compute their support values.
  - Prune the 1-itemsets that have a support value below the minimum support and keep the rest as the frequent 1-itemsets.
  - Generate the candidate 2-itemsets by joining the frequent 1-itemsets with each other, and scan the dataset to compute their support values.
  - Prune the candidate 2-itemsets that have a support value below the minimum support and keep the rest as the frequent 2-itemsets.
  - Repeat the above steps by increasing the size of the itemsets by one at each iteration, until no more frequent itemsets can be generated or the maximum size of the itemsets is reached.

- The output of the algorithm is the set of all frequent itemsets in the dataset, along with their support values.

#### Association Rules

- Association rules are rules that express the relationship between items in a frequent itemset, such as {bread, butter} => {jam}.
- The rule means that if a transaction contains bread and butter, then it is likely to contain jam as well.
- Association rules can be derived from frequent itemsets by splitting them into two parts: the antecedent (left-hand side) and the consequent (right-hand side).
- For example, from the frequent itemset {bread, butter, jam}, we can derive three association rules: {bread, butter} => {jam}, {bread, jam} => {butter}, and {butter, jam} => {bread}.
- Association rules can be evaluated by two measures: confidence and lift.
- The confidence of a rule is the fraction of transactions that contain the antecedent and the consequent among those that contain the antecedent.
- For example, if 20 out of 100 transactions contain {bread, butter, jam} and 30 out of 100 transactions contain {bread, butter}, then the confidence of the rule {bread, butter} => {jam} is 0.67.
- The lift of a rule is the ratio of the confidence of the rule to the support value of the consequent.
- For example, if the support value of {jam} is 0.4, then the lift of the rule {bread, butter} => {jam} is 0.67 / 0.4 = 1.675.
- The lift measures how much the rule is better than a random guess, and a lift value greater than 1 indicates a positive association between the antecedent and the consequent.

### Clustering

- Clustering is the process of partitioning a set of data points into groups or clusters, such that the data points in the same cluster are more similar or closer to each other than to those in other clusters.
- Clustering is an unsupervised learning technique, meaning that the data points do not have any labels or predefined categories, and the