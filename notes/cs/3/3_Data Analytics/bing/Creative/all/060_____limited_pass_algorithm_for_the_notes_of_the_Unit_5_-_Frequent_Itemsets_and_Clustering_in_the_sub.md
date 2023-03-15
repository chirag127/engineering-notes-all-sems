# Limited Pass Algorithm

- Limited pass algorithm is a technique for finding frequent itemsets in big data analytics.
- Frequent itemsets are sets of items that appear together in a large number of transactions or data records.
- Finding frequent itemsets is useful for applications such as market basket analysis, association rule mining, and clustering.
- Limited pass algorithm does not compute the exact collection of frequent itemsets of size k in k passes, as done by algorithms such as A-Priori, PCY, Multistage, and Multihash.
- Instead, limited pass algorithm finds all or most of the frequent itemsets in fewer than k passes, by using sampling, sketching, or hashing techniques .
- The advantage of limited pass algorithm is that it reduces the time and space complexity of finding frequent itemsets, especially when the data is large and high-dimensional.
- The disadvantage of limited pass algorithm is that it may miss some of the frequent itemsets or produce some false positives, depending on the accuracy of the approximation methods used .
- Some examples of limited pass algorithms are Toivonen's algorithm, SON algorithm, and Lossy Counting algorithm.