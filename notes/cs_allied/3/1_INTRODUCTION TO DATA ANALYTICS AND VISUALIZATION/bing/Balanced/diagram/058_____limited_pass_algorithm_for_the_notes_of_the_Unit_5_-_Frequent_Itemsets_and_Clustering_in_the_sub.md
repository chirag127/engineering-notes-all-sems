### Limited Pass Algorithm for Frequent Itemsets

- The limited pass algorithm is an approximate algorithm that aims to find most of the frequent itemsets in a data set, using fewer passes than the exact algorithms like A-Priori or PCY .
- The basic idea of the limited pass algorithm is to use a random sample of the data set and lower the support threshold for the sample, so that most of the frequent itemsets in the original data set are also frequent in the sample.
- The algorithm works as follows:
  - Choose a sample size that can fit in main memory, and randomly select that many baskets from the data set.
  - For each size k of itemsets, use the A-Priori algorithm on the sample with a lowered support threshold s/k, where s is the original support threshold for the data set.
  - Output the frequent itemsets of size k found in the sample as candidate frequent itemsets for the original data set.
  - Repeat the above steps until no more frequent itemsets are found in the sample.
  - Make a second pass over the original data set and count the occurrences of the candidate frequent itemsets. Output those that have at least s occurrences as the final frequent itemsets.
- The advantages of the limited pass algorithm are:
  - It can find most of the frequent itemsets in fewer passes than the exact algorithms, especially when the data set is very large and the support threshold is low.
  - It can handle data sets that do not fit in main memory, as long as the sample size and the number of candidate frequent itemsets are manageable.
- The disadvantages of the limited pass algorithm are:
  - It is not guaranteed to find all the frequent itemsets in the original data set, as some of them may be missed in the sample or have lower support in the sample than in the original data set.
  - It may output some false positives, i.e., itemsets that are frequent in the sample but not in the original data set, due to sampling error or skewed distribution of the data.