## Merge Sort

Merge Sort is an efficient, general-purpose, comparison-based sorting algorithm. It is a divide and conquer algorithm that was invented by John von Neumann in 1945.

### Algorithm

1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

### Time Complexity

The time complexity of Merge Sort is O(n log n) in the worst, average, and best cases. This is because the algorithm always divides the array into two halves and takes linear time to merge the two halves.

### Experiment

To demonstrate the time complexity of Merge Sort, an experiment can be conducted by sorting a given set of n integer elements using the Merge Sort method and computing its time complexity. The program can be run for varied values of n> 5000, and the time taken to sort can be recorded. A graph of the time taken versus n can be plotted on a graph sheet. The elements can be read from a file or can be generated using the random number generator.

### Divide and Conquer

Merge Sort is an example of the divide and conquer method. The algorithm works by dividing the unsorted list into n sublists, each containing one element, and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. The time complexity analysis of the divide and conquer method shows that it has a worst case, average case, and best case time complexity of O(n log n).

### Conclusion

In conclusion, Merge Sort is an efficient sorting algorithm that uses the divide and conquer method. Its time complexity is O(n log n) in the worst, average, and best cases. An experiment can be conducted to demonstrate its time complexity by sorting a given set of n integer elements using the Merge Sort method and computing its time complexity. The results can be plotted on a graph to show the relationship between the time taken to sort and the number of elements being sorted.