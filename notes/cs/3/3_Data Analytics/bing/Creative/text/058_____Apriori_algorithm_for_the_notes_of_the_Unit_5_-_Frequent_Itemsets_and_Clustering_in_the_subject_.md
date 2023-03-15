### Apriori algorithm

- The Apriori algorithm is an algorithm for **frequent itemset mining** and **association rule learning** over relational databases  .
- Frequent itemsets are sets of items that appear together frequently in a database, such as bread and butter, or milk and cereal .
- Association rules are rules that imply the presence of one item based on the presence of another item, such as {bread} => {butter}, or {milk} => {cereal} .
- The Apriori algorithm was proposed by **Agrawal and Srikant** in 1994 .
- The Apriori algorithm is designed to operate on databases containing **transactions**, such as collections of items bought by customers, or details of a website frequentation  .
- The Apriori algorithm uses **prior knowledge** of frequent itemset properties to reduce the search space and improve the efficiency .
- The Apriori algorithm applies an **iterative approach** or **level-wise search** where k-frequent itemsets are used to find k+1 itemsets .
- The Apriori algorithm consists of two main steps: **join** and **prune** .
  - The join step generates candidate itemsets of length k from the frequent itemsets of length k-1 .
  - The prune step eliminates the candidate itemsets that have a sub-itemset that is not frequent .
- The Apriori algorithm requires a user-specified **minimum support threshold** to determine the frequency of an itemset .
- The Apriori algorithm terminates when no more frequent itemsets can be generated .
- The Apriori algorithm can be used to generate association rules by applying a **minimum confidence threshold** to the frequent itemsets .
- The Apriori algorithm has some limitations, such as:
  - It may generate a large number of candidate itemsets, which can be computationally expensive .
  - It may scan the database multiple times, which can be time-consuming .
  - It may not be suitable for sparse data or data with varying item frequencies .