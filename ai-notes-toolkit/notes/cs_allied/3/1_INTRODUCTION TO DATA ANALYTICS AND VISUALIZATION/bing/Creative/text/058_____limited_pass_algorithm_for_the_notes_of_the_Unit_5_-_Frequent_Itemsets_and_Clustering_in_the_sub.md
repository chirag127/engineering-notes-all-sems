### Limited Pass Algorithm for Frequent Itemsets

- The limited pass algorithm is an approximate algorithm that aims to find most of the frequent itemsets in a data set, using fewer passes than the exact algorithms like A-Priori or PCY .
- The basic idea of the limited pass algorithm is to use a random sample of the data set and apply an exact algorithm on the sample with a lower support threshold.
- The sample size and the lower threshold are chosen such that the probability of missing a frequent itemset in the original data set is low.
- The algorithm works as follows:
  - Choose a sample size n and a lower support threshold s' such that s' < s, where s is the desired support threshold for the original data set.
  - Take a random sample of n baskets from the data set and apply an exact algorithm (such as A-Priori or PCY) on the sample with the support threshold s'.
  - The output of the exact algorithm is a set of candidate frequent itemsets from the sample.
  - Scan the original data set and count the occurrences of the candidate frequent itemsets.
  - Output the itemsets that have at least s occurrences in the original data set as the frequent itemsets.
- The advantages of the limited pass algorithm are :
  - It reduces the number of passes over the original data set, which can be very large and costly to access.
  - It reduces the memory requirement for counting the candidate itemsets, as the sample size is smaller than the original data set size.
  - It can find most of the frequent itemsets with high probability, if the sample size and the lower threshold are chosen appropriately.
- The disadvantages of the limited pass algorithm are :
  - It is not guaranteed to find all the frequent itemsets, as some of them may be missed in the sample or have lower support in the sample than in the original data set.
  - It may output some false positives, i.e., itemsets that are frequent in the sample but not in the original data set.
  - It may be sensitive to the choice of the sample size and the lower threshold, which depend on the distribution and the characteristics of the data set.