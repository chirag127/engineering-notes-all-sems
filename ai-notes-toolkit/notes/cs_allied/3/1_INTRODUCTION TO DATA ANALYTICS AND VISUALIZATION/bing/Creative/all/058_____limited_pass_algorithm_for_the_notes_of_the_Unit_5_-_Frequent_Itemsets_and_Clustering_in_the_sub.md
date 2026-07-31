# Limited Pass Algorithm for Frequent Itemsets

- The limited pass algorithm is an approximate algorithm that aims to find most of the frequent itemsets in a data set, without making multiple passes over the data.
- The algorithm works as follows:
  - First, it takes a random sample of the data set and applies a lower support threshold to find the candidate frequent itemsets in the sample.
  - Then, it makes one pass over the entire data set and counts the occurrences of the candidate itemsets, filtering out those that do not meet the original support threshold.
  - The remaining itemsets are the approximate frequent itemsets of the data set.
- The advantages of the limited pass algorithm are:
  - It reduces the number of passes over the data set to two, which can save a lot of time and memory for large data sets.
  - It can find most of the frequent itemsets, especially those with high support, with high probability.
- The disadvantages of the limited pass algorithm are:
  - It may miss some of the frequent itemsets, especially those with low support, due to sampling error or lower threshold.
  - It may include some of the infrequent itemsets, due to sampling error or higher threshold.
  - It does not guarantee to find the exact collection of frequent itemsets, which may affect the quality of the association rules or other mining tasks.