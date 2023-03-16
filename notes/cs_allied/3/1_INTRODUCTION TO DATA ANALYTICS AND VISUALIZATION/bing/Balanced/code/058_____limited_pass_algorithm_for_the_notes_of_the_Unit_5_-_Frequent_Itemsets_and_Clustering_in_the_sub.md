### Limited Pass Algorithm for Frequent Itemsets

- The limited pass algorithm is an approximate algorithm that aims to find most of the frequent itemsets in a large data set, using fewer passes than the exact algorithms like A-Priori or PCY .
- The basic idea of the limited pass algorithm is to use a random sample of the data set as the first pass, and then use a lower support threshold for the sample than for the whole data set.
- The sample size should be large enough to capture most of the frequent itemsets, but small enough to fit in the main memory and reduce the I/O cost.
- The second pass of the algorithm scans the whole data set and counts only the candidate itemsets that are frequent in the sample.
- The advantage of the limited pass algorithm is that it can find most of the frequent itemsets with high probability, using only two passes over the data set.
- The disadvantage of the limited pass algorithm is that it may miss some of the frequent itemsets that are not frequent in the sample, or include some of the infrequent itemsets that are frequent in the sample by chance.
- The accuracy of the limited pass algorithm depends on the choice of the sample size and the support threshold for the sample.
- The limited pass algorithm can be extended to find frequent itemsets of any size, by using a recursive approach similar to the A-Priori algorithm.
- The limited pass algorithm can also be combined with other techniques like hashing, bitmap compression, or partitioning to improve its performance and scalability .