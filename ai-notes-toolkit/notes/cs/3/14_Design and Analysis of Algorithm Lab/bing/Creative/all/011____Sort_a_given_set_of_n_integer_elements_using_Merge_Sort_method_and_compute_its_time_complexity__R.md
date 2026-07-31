# Merge Sort

Merge sort is a divide-and-conquer algorithm that splits a given set of n integer elements into two halves, recursively sorts each half, and then merges the two sorted halves into a single sorted list. The algorithm can be implemented as follows:

- Base case: If the list has zero or one element, it is already sorted and no further action is required.
- Recursive case: Otherwise, divide the list into two sublists of equal or nearly equal size, and sort each sublist recursively using merge sort.
- Merge step: Combine the two sorted sublists into a single sorted list by repeatedly comparing the smallest elements of each sublist and moving the smaller one to the output list until both sublists are empty.

The time complexity of merge sort is O(n log n) in the worst case, average case and best case, where n is the number of elements in the list. This is because the algorithm divides the list into two halves at each level of recursion, resulting in log n levels, and merges n elements at each level, resulting in n log n operations in total.

To run the program for varied values of n > 5000, and record the time taken to sort, we can use the following pseudocode:

- Generate a random list of n integer elements, where n is a large number greater than 5000.
- Start a timer to measure the execution time of the sorting algorithm.
- Call the merge sort function on the list and store the sorted list in a variable.
- Stop the timer and record the elapsed time in a variable.
- Repeat the above steps for different values of n and store the results in a table or a file.

To plot a graph of the time taken versus n on a graph sheet, we can use the following steps:

- Label the x-axis as n and the y-axis as time taken in seconds.
- Choose a suitable scale for both axes, such as 1000 units for n and 0.1 seconds for time taken.
- Plot the points (n, time taken) for each value of n and time taken from the table or file.
- Draw a smooth curve that passes through the points or use a line of best fit to represent the trend of the data.
- Observe the shape of the curve and compare it with the theoretical time complexity of O(n log n).

To demonstrate how the divide-and-conquer method works along with its time complexity analysis, we can use the following example:

- Suppose we have a list of 8 elements: [38, 27, 43, 3, 9, 82, 10, 14].
- To sort this list using merge sort, we first divide it into two sublists of 4 elements each: [38, 27, 43, 3] and [9, 82, 10, 14].
- We sort each sublist recursively using merge sort, resulting in two sorted sublists: [3, 27, 38, 43] and [9, 10, 14, 82].
- We merge the two sorted sublists into a single sorted list by comparing the smallest elements of each sublist and moving the smaller one to the output list until both sublists are empty, resulting in the final sorted list: [3, 9, 10, 14, 27, 38, 43, 82].
- The time complexity of this algorithm is O(n log n), where n is the number of elements in the list. This is because the algorithm divides the list into two halves at each level of recursion, resulting in log n levels, and merges n elements at each level, resulting in n log n operations in total. In this example, n = 8, log n = 3, and n log n = 24. Therefore, the algorithm performs 24 operations to sort the list of 8 elements.