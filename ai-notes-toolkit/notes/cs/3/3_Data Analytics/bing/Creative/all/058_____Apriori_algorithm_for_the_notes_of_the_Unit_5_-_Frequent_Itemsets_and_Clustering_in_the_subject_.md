# Apriori Algorithm

- Apriori algorithm is a data mining technique for finding frequent itemsets and association rules in a transactional database  .
- Frequent itemsets are sets of items that appear together in a minimum number of transactions, called the support threshold  .
- Association rules are implications of the form X -> Y, where X and Y are itemsets, meaning that transactions containing X are likely to contain Y as well  .
- Apriori algorithm uses a bottom-up approach, where it starts with finding the frequent 1-itemsets (single items) and then iteratively generates larger and larger itemsets by joining and pruning the previous ones  .
- The join step combines two itemsets of size k to form a candidate itemset of size k+1, if they share the first k-1 items  .
- The prune step eliminates the candidate itemsets that have a subset that is not frequent, based on the Apriori property that all subsets of a frequent itemset must be frequent  .
- The algorithm stops when no more frequent or candidate itemsets can be generated  .
- The algorithm can be summarized as follows:

```
Apriori(T, min_sup)
  L1 = {frequent 1-itemsets};
  k = 2;
  while (Lk-1 is not empty) do
    Ck = apriori-gen(Lk-1); // generate candidates
    for each transaction t in T do
      Ct = subset(Ck, t); // find candidates in t
      for each candidate c in Ct do
        c.count++; // increment count
    Lk = {c in Ck | c.count >= min_sup}; // find frequent itemsets
    k++;
  end
  return U_k Lk; // return all frequent itemsets
```