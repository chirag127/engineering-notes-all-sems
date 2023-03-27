### Limited Pass Algorithm for the Notes of the Unit 5 - Frequent Itemsets and Clustering in the Subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

The limited pass algorithm is used for mining frequent itemsets in a large dataset. Here are the key points to understand about the algorithm:

- The algorithm works by scanning the dataset multiple times, with each pass focusing on a different subset of the data.
- In each pass, the algorithm identifies the frequent itemsets that occur within the subset of the data being examined.
- The results of each pass are then combined to determine the complete set of frequent itemsets that occur in the entire dataset.

The limited pass algorithm is particularly useful for large datasets, as it allows for the frequent itemsets to be identified without requiring the entire dataset to be stored in memory at once.

To implement the limited pass algorithm, follow these steps:

1. Divide the dataset into a series of subsets, each of which can be processed independently.
2. Scan each subset of the data, counting the frequency of each itemset within that subset.
3. Combine the results of each pass to identify the complete set of frequent itemsets that occur in the entire dataset.
4. Determine the support threshold for the itemsets, which is the minimum frequency required for an itemset to be considered "frequent."
5. Remove any itemsets that fall below the support threshold.
6. Repeat the process with increasingly smaller subsets of the data until the complete set of frequent itemsets has been identified.

Overall, the limited pass algorithm is a powerful tool for identifying frequent itemsets in large datasets. By breaking the dataset into smaller subsets and processing them independently, the algorithm can efficiently identify the complete set of frequent itemsets without requiring the entire dataset to be stored in memory at once.