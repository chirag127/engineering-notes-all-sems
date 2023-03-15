## Sort a given set of n integer elements using Merge Sort method and compute its time complexity

Merge Sort is a popular sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. The algorithm works by dividing the input into two halves, recursively sorting each half, and then merging the two sorted halves together to form the final sorted output.

The time complexity of Merge Sort can be computed as follows:

1. The algorithm divides the input into two halves, which takes constant time O(1).
2. The algorithm recursively sorts each half, which takes O(n log n) time for each half.
3. The algorithm merges the two sorted halves together, which takes O(n) time.

Therefore, the overall time complexity of Merge Sort is O(n log n).

To demonstrate the time complexity of Merge Sort, the algorithm can be run on varied values of n > 5000, and the time taken to sort can be recorded. A graph of the time taken versus n can be plotted on a graph sheet to visualize the relationship between the input size and the time taken to sort.

The elements to be sorted can be read from a file or generated using a random number generator.

In terms of its time complexity analysis, Merge Sort has a worst-case, average-case, and best-case time complexity of O(n log n). This is because the algorithm always divides the input into two halves and recursively sorts each half, regardless of the input distribution.

In summary, Merge Sort is an efficient sorting algorithm that uses the divide-and-conquer approach to sort a given set of n integer elements. Its time complexity is O(n log n) in the worst, average, and best cases. The algorithm can be demonstrated by running it on varied values of n > 5000 and plotting a graph of the time taken versus n. The elements to be sorted can be read from a file or generated using a random number generator.