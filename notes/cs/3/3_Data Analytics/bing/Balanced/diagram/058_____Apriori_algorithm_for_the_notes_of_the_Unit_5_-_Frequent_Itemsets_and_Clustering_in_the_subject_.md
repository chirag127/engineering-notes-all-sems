### Apriori algorithm

- Apriori algorithm is an algorithm for **frequent itemset mining** and **association rule learning** over relational databases  .
- Frequent itemset mining is the process of finding the sets of items that occur frequently in a database, and association rule learning is the process of finding the rules that imply the presence of some items given the presence of other items in a database.
- Apriori algorithm is based on the principle that **if an itemset is frequent, then all of its subsets are frequent**  . This is known as the **Apriori property** or the **anti-monotonicity property**.
- Apriori algorithm uses a **bottom-up** or **level-wise** approach, where it starts with the frequent individual items (1-itemsets) and extends them to larger and larger itemsets as long as they appear sufficiently often in the database  .
- Apriori algorithm consists of two main steps: **join** and **prune** .
  - The join step generates candidate itemsets of size k by joining frequent itemsets of size k-1 with themselves .
  - The prune step eliminates the candidate itemsets that have infrequent subsets by using the Apriori property .
- Apriori algorithm requires a user-defined parameter called the **minimum support threshold**, which is the minimum frequency or percentage of transactions that an itemset must satisfy to be considered frequent  .
- Apriori algorithm terminates when no more frequent or candidate itemsets can be generated  .
- Apriori algorithm can be used to generate association rules by computing the **confidence** of each rule, which is the ratio of the support of the itemset containing both the antecedent and the consequent to the support of the itemset containing only the antecedent  .
- Apriori algorithm can be improved by using various techniques, such as **hashing**, **transaction reduction**, **partitioning**, **sampling**, and **dynamic itemset counting**  .

: Apriori algorithm - Wikipedia
: Apriori Algorithm - GeeksforGeeks
: Apriori Algorithm in Data Mining: Implementation With Examples