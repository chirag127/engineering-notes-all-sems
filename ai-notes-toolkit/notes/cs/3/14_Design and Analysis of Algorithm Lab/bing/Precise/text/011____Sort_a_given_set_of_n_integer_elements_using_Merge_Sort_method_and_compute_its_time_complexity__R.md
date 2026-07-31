## Merge Sort

Merge sort is a sorting algorithm that uses the divide and conquer approach to sort a given set of n integer elements. The algorithm works by dividing the input into two halves, recursively sorting each half, and then merging the two sorted halves together to form the final sorted output.

The time complexity of merge sort can be computed as follows:

- **Worst case:** The worst case time complexity of merge sort is O(n log n). This occurs when the input is such that each merge operation requires the maximum number of comparisons.

- **Average case:** The average case time complexity of merge sort is also O(n log n), since on average, each merge operation requires half the maximum number of comparisons.

- **Best case:** The best case time complexity of merge sort is O(n), which occurs when the input is already sorted, and no merge operations are required.

To demonstrate the time complexity of merge sort, the algorithm can be run on varied values of n > 5000, and the time taken to sort can be recorded. A graph of the time taken versus n can then be plotted on a graph sheet. The elements to be sorted can be read from a file or generated using a random number generator.

In summary, merge sort is an efficient sorting algorithm that uses the divide and conquer approach to sort a given set of n integer elements. Its time complexity is O(n log n) in the worst and average cases, and O(n) in the best case. The algorithm can be demonstrated by running it on varied values of n > 5000 and plotting a graph of the time taken versus n. This can help to illustrate how the divide and conquer method works, along with its time complexity analysis for the worst, average, and best cases. This information can be useful for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.