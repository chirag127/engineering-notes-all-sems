# Limited Pass Algorithm for Frequent Itemsets

- The limited pass algorithm is an approximate algorithm that aims to find most of the frequent itemsets in a data set, using fewer passes than the exact algorithms like A-Priori or PCY .
- The basic idea of the limited pass algorithm is to use a random sample of the data set and lower the support threshold for the sample, so that most of the frequent itemsets in the original data set are also frequent in the sample.
- The algorithm works as follows:
  - Choose a sample size that can fit in main memory, and randomly select that many baskets from the data set.
  - Use the A-Priori algorithm on the sample, but lower the support threshold by a factor of 1.25 (or some other constant) to account for the smaller sample size. For example, if the sample is 1% of the baskets, use s/125 as the support threshold rather than s/100.
  - The output of the A-Priori algorithm on the sample is the set of candidate frequent itemsets for the original data set.
  - Make a second pass over the original data set and count the occurrences of the candidate frequent itemsets. Output those that have at least s occurrences as the frequent itemsets.
- The limited pass algorithm is not guaranteed to find all the frequent itemsets, but it can find most of them with high probability, depending on the sample size and the support threshold .
- The advantages of the limited pass algorithm are that it reduces the number of passes over the data set, and it reduces the number of candidate itemsets that need to be counted in the second pass .
- The disadvantages of the limited pass algorithm are that it may miss some frequent itemsets, and it may output some false positives that are not frequent in the original data set .