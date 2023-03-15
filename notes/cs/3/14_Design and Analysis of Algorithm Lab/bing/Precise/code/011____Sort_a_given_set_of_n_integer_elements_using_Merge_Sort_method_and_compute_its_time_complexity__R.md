## Merge Sort

Merge Sort is a popular sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. The algorithm works by dividing the input into two halves, recursively sorting each half, and then merging the two sorted halves together to form the final sorted output.

The time complexity of Merge Sort can be computed as follows:

- **Worst Case:** The worst case time complexity of Merge Sort is O(n log n). This occurs when the input array is already sorted in reverse order, as the algorithm has to perform the maximum number of comparisons and swaps.

- **Average Case:** The average case time complexity of Merge Sort is also O(n log n), as the algorithm performs a similar number of operations on average.

- **Best Case:** The best case time complexity of Merge Sort is O(n log n), as the algorithm still has to divide the input into two halves and recursively sort each half, even if the input is already sorted.

To demonstrate the time complexity of Merge Sort, the algorithm can be run on varied values of n > 5000 and the time taken to sort can be recorded. A graph can be plotted of the time taken versus n on a graph sheet. The elements to be sorted can be read from a file or generated using a random number generator.

In summary, Merge Sort is an efficient sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. Its time complexity is O(n log n) in the worst, average, and best cases. The algorithm can be demonstrated by running it on varied values of n and plotting a graph of the time taken to sort versus n.