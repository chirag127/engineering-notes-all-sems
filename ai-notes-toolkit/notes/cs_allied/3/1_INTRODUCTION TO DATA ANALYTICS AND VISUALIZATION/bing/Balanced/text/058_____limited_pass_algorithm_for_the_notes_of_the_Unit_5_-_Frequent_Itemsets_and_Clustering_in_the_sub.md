### Limited Pass Algorithm for Frequent Itemsets

- The limited pass algorithm is an approximate algorithm that aims to find most of the frequent itemsets in a data set, without making too many passes over the data .
- The algorithm works as follows:
  - First, it takes a random sample of the data and applies the A-Priori algorithm to find the frequent itemsets in the sample, using a lower support threshold than the original one.
  - Then, it uses the frequent itemsets from the sample as candidates for the whole data set, and makes another pass over the data to count their supports.
  - Finally, it outputs the candidates that have support above the original threshold as the frequent itemsets.
- The advantages of the limited pass algorithm are that it reduces the number of passes over the data, and the size of the candidate sets.
- The disadvantages of the limited pass algorithm are that it may miss some frequent itemsets that are not frequent in the sample, or include some infrequent itemsets that are frequent in the sample.
- The accuracy of the limited pass algorithm depends on the size and quality of the sample, and the choice of the lower support threshold.
- The limited pass algorithm is suitable for applications where it is not essential to discover every frequent itemset, but only most of them .