### Apriori algorithm

- The Apriori algorithm is an algorithm for **frequent itemset mining** and **association rule learning** over relational databases  .
- Frequent itemsets are sets of items that appear together frequently in a database, such as bread and butter, or milk and cereal.
- Association rules are rules that imply the presence of one item based on the presence of another item, such as {bread, butter} => {jam}, or {milk} => {cereal}.
- The Apriori algorithm was proposed by **Agrawal and Srikant** in 1994 .
- The Apriori algorithm is designed to operate on databases containing **transactions**, such as collections of items bought by customers, or details of a website frequentation.
- The Apriori algorithm uses **prior knowledge** of frequent itemset properties to reduce the search space and improve efficiency .
- The Apriori algorithm applies an **iterative** approach or **level-wise** search, where k-frequent itemsets are used to find k+1 itemsets .
- The Apriori algorithm consists of two main steps: **join** and **prune** .
  - The join step generates candidate itemsets of length k from frequent itemsets of length k-1.
  - The prune step eliminates the candidate itemsets that have a subset that is not frequent.
- The Apriori algorithm requires a user-specified **minimum support threshold** to determine the frequency of an itemset .
- The Apriori algorithm stops when no more frequent itemsets can be generated .
- The Apriori algorithm can be used to generate association rules from the frequent itemsets by applying a **minimum confidence threshold** .
- The Apriori algorithm can be modified or improved by using different data structures, hashing techniques, sampling methods, or parallelization strategies  .