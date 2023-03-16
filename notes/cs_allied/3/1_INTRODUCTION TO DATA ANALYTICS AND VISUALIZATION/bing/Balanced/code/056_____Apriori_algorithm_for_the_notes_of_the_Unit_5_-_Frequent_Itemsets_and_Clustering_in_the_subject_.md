### Apriori algorithm

- The Apriori algorithm is an algorithm for **frequent itemset mining** and **association rule learning** over relational databases  .
- Frequent itemsets are sets of items that appear together in a database with a frequency above a given threshold  .
- Association rules are rules that imply the presence of some items given the presence of other items in a transaction  .
- The Apriori algorithm was proposed by **Agrawal and Srikant** in 1994 .
- The Apriori algorithm is designed to operate on databases containing **transactions** (for example, collections of items bought by customers, or details of a website frequentation or IP addresses)  .
- The Apriori algorithm uses **prior knowledge** of frequent itemset properties to reduce the search space and improve efficiency  .
- The Apriori algorithm applies an **iterative** approach or **level-wise** search where k-frequent itemsets are used to find k+1 itemsets  .
- The Apriori algorithm consists of two main steps: **join** and **prune**  .
  - The join step generates candidate itemsets of length k from frequent itemsets of length k-1  .
  - The prune step eliminates candidate itemsets that have infrequent subsets using the **Apriori property**  .
- The Apriori property states that **all non-empty subsets of a frequent itemset must also be frequent**  .
- The Apriori algorithm stops when no more frequent itemsets can be generated  .
- The Apriori algorithm can be used to generate association rules by computing the **confidence** and **support** of each rule  .
  - The confidence of a rule is the ratio of the number of transactions that contain both the antecedent and the consequent of the rule to the number of transactions that contain the antecedent of the rule  .
  - The support of a rule is the ratio of the number of transactions that contain both the antecedent and the consequent of the rule to the total number of transactions  .
  - A rule is considered **strong** if its confidence and support are above given thresholds  .
- The Apriori algorithm has some advantages and disadvantages  .
  - Advantages:
    - It is easy to implement and understand  .
    - It can handle large datasets efficiently  .
    - It can be parallelized and distributed  .
  - Disadvantages:
    - It may generate a large number of candidate itemsets, especially when the minimum support threshold is low or the number of items is high  .
    - It may require multiple scans of the database, which can be costly in terms of time and memory  .
    - It may not be suitable for finding rare itemsets or itemsets with variable lengths  .

: Apriori algorithm - Wikipedia
: Apriori Algorithm - GeeksforGeeks
: Apriori Algorithm in Data Mining: Implementation With Examples