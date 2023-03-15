### Limited Pass Algorithm

- A limited pass algorithm is a technique for finding frequent itemsets in large datasets with fewer passes than the exact algorithms .
- The idea is to trade off accuracy for efficiency by allowing some false positives (infrequent itemsets that are reported as frequent) or false negatives (frequent itemsets that are missed) .
- A limited pass algorithm typically consists of two phases: a sampling phase and a verification phase .
- In the sampling phase, a random subset of the dataset is scanned and the frequent itemsets in the sample are found using an exact algorithm (such as A-Priori, PCY, etc.) .
- In the verification phase, the entire dataset is scanned and the candidate itemsets from the sample are checked for their actual support .
- The advantage of a limited pass algorithm is that it can reduce the number of passes over the dataset and the memory requirements, especially when the dataset is very large and the support threshold is very low .
- The disadvantage of a limited pass algorithm is that it may not find all the frequent itemsets or may report some infrequent itemsets as frequent, depending on the quality of the sample and the verification method .
- A limited pass algorithm can be used for finding frequent patterns in big data analytics, where it is not essential to discover every frequent itemset, but sufficient to discover most of them  .
- A limited pass algorithm can also be used for frequent pattern based clustering methods, where the frequent itemsets are used as features to cluster the data points .
- A limited pass algorithm can also be applied to non-Euclidean spaces, such as graphs, where the distance between two data points is not defined by a metric .