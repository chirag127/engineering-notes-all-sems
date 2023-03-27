### Limited Pass Algorithm for the Notes of Unit 5 - Frequent Itemsets and Clustering in the Subject of Introduction to Data Analytics and Visualization

In this unit, we will learn about the limited pass algorithm which is used in frequent itemset mining. This algorithm is used to find frequent itemsets in a large dataset efficiently. Below are the key points to understand about the limited pass algorithm:

1. The limited pass algorithm is used to find frequent itemsets in a large dataset by making only a limited number of passes through the dataset.

2. In the first pass, the algorithm counts the frequency of each item and removes the items that do not meet the minimum support threshold.

3. In the second pass, the algorithm creates candidate itemsets of size two using the remaining frequent items from the first pass.

4. In the subsequent passes, the algorithm creates candidate itemsets of size k by joining frequent itemsets of size k-1.

5. The algorithm stops when it cannot find any more frequent itemsets or when the maximum itemset size is reached.

6. The limited pass algorithm uses the Apriori principle to reduce the search space by only considering itemsets that are subsets of frequent itemsets.

7. The Apriori principle states that if an itemset is infrequent, then all of its supersets are also infrequent.

8. The limited pass algorithm can be improved by using pruning techniques such as the depth-first search, breadth-first search, or vertical format.

9. The limited pass algorithm can also be used for clustering by treating itemsets as points in a high-dimensional space and using clustering algorithms to group similar itemsets together.

Overall, the limited pass algorithm is a powerful tool for finding frequent itemsets in a large dataset efficiently. By understanding the key points outlined above, you will be well-equipped to apply this algorithm in your data analytics and visualization tasks.