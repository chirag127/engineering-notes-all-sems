# Limited Pass Algorithm

- Limited pass algorithm is a technique for finding frequent itemsets in big data analytics.
- Frequent itemsets are sets of items that appear together in a large number of transactions or data records.
- Finding frequent itemsets is useful for applications such as market basket analysis, association rule mining, and clustering.
- Limited pass algorithm does not compute the exact collection of frequent itemsets of size k in k passes, as done by algorithms such as A-Priori, PCY, Multistage, and Multihash.
- Instead, limited pass algorithm finds all or most of the frequent itemsets in fewer than k passes, by using some approximation or sampling techniques.
- The advantage of limited pass algorithm is that it reduces the number of scans over the data, which can be very expensive for large datasets.
- The disadvantage of limited pass algorithm is that it may miss some frequent itemsets or include some infrequent itemsets, depending on the accuracy of the approximation or sampling method.
- Some examples of limited pass algorithms are SON, Toivonen, and Sampling.
- SON algorithm divides the data into chunks and applies A-Priori algorithm on each chunk to find local frequent itemsets, then combines the results to find global frequent itemsets.
- Toivonen algorithm uses a random sample of the data to find frequent itemsets, then verifies them on the whole data, and repeats the process until no false positives or negatives are found.
- Sampling algorithm uses a random sample of the data to find frequent itemsets, then estimates their support on the whole data using a confidence interval, and discards the ones that are unlikely to be frequent.