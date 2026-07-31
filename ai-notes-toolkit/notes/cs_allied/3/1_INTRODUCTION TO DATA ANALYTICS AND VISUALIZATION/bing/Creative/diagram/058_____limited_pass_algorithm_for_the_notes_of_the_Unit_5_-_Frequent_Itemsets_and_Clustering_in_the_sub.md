### Limited Pass Algorithm for Frequent Itemsets

- The limited pass algorithm is an approximate algorithm that aims to find most of the frequent itemsets in a data set, using fewer passes than the exact algorithms like A-Priori or PCY .
- The basic idea of the limited pass algorithm is to use a random sample of the data set and apply an exact algorithm on the sample with a lower support threshold.
- The sample size and the lower threshold are chosen such that the probability of missing a frequent itemset in the original data set is low.
- The algorithm works as follows:
  - Choose a sample size n and a lower support threshold t, where t < s, the desired support threshold for the original data set.
  - Take a random sample of n baskets from the data set and apply an exact algorithm (such as A-Priori or PCY) on the sample with the threshold t. This will produce a set of candidate frequent itemsets from the sample.
  - Make a second pass over the original data set and count the occurrences of the candidate itemsets. Output those itemsets that have at least s occurrences in the original data set as frequent itemsets.
- The advantage of the limited pass algorithm is that it reduces the number of passes and the memory requirement for finding frequent itemsets, especially when the itemsets are large.
- The disadvantage of the limited pass algorithm is that it may miss some frequent itemsets in the original data set, or include some infrequent itemsets in the output, depending on the quality of the sample and the choice of the lower threshold.
- The limited pass algorithm can be used for big data analytics, where the data set is too large to fit in the main memory and the exact algorithms are too slow or impractical.