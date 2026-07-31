### Apriori algorithm

- The Apriori algorithm is an algorithm for **frequent itemset mining** and **association rule learning** over relational databases  .
- Frequent itemsets are sets of items that appear together frequently in a database, such as bread and butter, or milk and cereal .
- Association rules are rules that imply the presence of one item or set of items given another item or set of items, such as {bread, butter} => {jam}, meaning that if a customer buys bread and butter, they are likely to buy jam as well .
- The Apriori algorithm is designed to operate on databases containing transactions, such as collections of items bought by customers, or details of a website frequentation or IP addresses  .
- The Apriori algorithm was proposed by **Agrawal and Srikant** in 1994 .
- The name of the algorithm is Apriori because it uses **prior knowledge** of frequent itemset properties, such as the fact that a subset of a frequent itemset must also be frequent  .
- The Apriori algorithm follows an **iterative** approach or **level-wise search** where k-frequent itemsets are used to find k+1 itemsets, until no more frequent itemsets can be found  .
- The Apriori algorithm consists of two main steps: **join** and **prune**  .
  - The join step generates candidate itemsets of length k from the frequent itemsets of length k-1, by joining them with themselves  .
  - The prune step eliminates the candidate itemsets that have infrequent subsets, by using the Apriori property  .
- The Apriori algorithm also requires a **minimum support threshold** to determine the frequency of an itemset, which is given in the problem or assumed by the user .
- The support of an itemset is the percentage of transactions in the database that contain the itemset .
- The Apriori algorithm can be used to generate association rules from the frequent itemsets, by applying a **minimum confidence threshold** .
- The confidence of a rule is the percentage of transactions that contain the consequent itemset given that they contain the antecedent itemset .
- The Apriori algorithm can be improved by using various techniques, such as hashing, transaction reduction, partitioning, sampling, or dynamic itemset counting .