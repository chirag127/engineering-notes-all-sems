### Apriori algorithm

- The Apriori algorithm is an algorithm for **frequent itemset mining** and **association rule learning** over relational databases  .
- Frequent itemsets are sets of items that appear together in a database with a minimum frequency or support  .
- Association rules are implications of the form X -> Y, where X and Y are itemsets, meaning that if X is present in a transaction, then Y is likely to be present as well  .
- The Apriori algorithm was proposed by **Agrawal and Srikant** in 1994 .
- The Apriori algorithm is designed to operate on databases containing **transactions** (for example, collections of items bought by customers, or details of a website frequentation or IP addresses)  .
- The Apriori algorithm uses **prior knowledge** of frequent itemset properties to reduce the search space and improve efficiency  .
- The Apriori algorithm applies an **iterative** approach or **level-wise search** where k-frequent itemsets are used to find k+1 itemsets  .
- The Apriori algorithm consists of two main steps: **join** and **prune**  .
- The join step generates candidate itemsets of length k+1 by joining frequent itemsets of length k that have k-1 common items  .
- The prune step eliminates candidate itemsets that have infrequent subsets by using the **Apriori property**, which states that any subset of a frequent itemset must be frequent  .
- The Apriori algorithm repeats the join and prune steps until no more frequent itemsets can be generated or a desired length is reached  .
- The Apriori algorithm can also generate association rules from the frequent itemsets by computing the **confidence** of each rule, which is the ratio of the support of the itemset to the support of the antecedent  .
- The Apriori algorithm can be modified or improved by using different data structures, pruning techniques, candidate generation methods, or parallelization strategies  .