## Sort a given set of n integer elements using Merge Sort method and compute its time complexity.

- Merge sort is a sorting algorithm that works by dividing an array of data into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
- It is a divide-and-conquer algorithm, which means that it breaks a complicated problem down into smaller problems that are easier to solve.
- The algorithm can be described as follows:

  - Find the middle point of the array and divide it into two halves.
  - Recursively sort the left half and the right half of the array using merge sort.
  - Merge the two sorted halves into one sorted array using a helper function.

- The time complexity of merge sort depends on the number of comparisons and data movements involved in the algorithm.
- The worst-case time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into log n levels, and each level requires O(n) time to merge the subarrays .
- The average-case time complexity of merge sort is also O(n log n), assuming that the input array is randomly ordered and the comparisons are equally likely to be true or false.
- The best-case time complexity of merge sort is O(n log n), when the input array is already sorted or nearly sorted. This is because the algorithm still needs to divide the array into log n levels, and each level requires O(n) time to merge the subarrays, even if no data movement is needed.
- To run the program for varied values of n > 5000, and record the time taken to sort, one can use a loop to generate random arrays of different sizes, and measure the execution time of the merge sort function using a timer or a clock function.
- To plot a graph of the time taken versus n on a graph sheet, one can use a spreadsheet software or a graphing tool to create a scatter plot or a line chart, with n as the x-axis and time as the y-axis. The graph should show a roughly linear relationship between n and time, with a slope of log n.
- To demonstrate how the divide-and-conquer method works along with its time complexity analysis, one can use an example array and show the steps of the algorithm using a tree diagram or a table, and explain how the number of levels, subarrays, comparisons, and data movements affect the running time of the algorithm. For example, consider the following array of 8 elements:

  ```
  [38, 27, 43, 3, 9, 82, 10, 5]
  ```

  The merge sort algorithm can be illustrated as follows:

  ```
  Level 0: [38, 27, 43, 3, 9, 82, 10, 5] // divide the array into two halves
  Level 1: [38, 27, 43, 3] [9, 82, 10, 5] // divide each half into two halves
  Level 2: [38, 27] [43, 3] [9, 82] [10, 5] // divide each quarter into two halves
  Level 3: [38] [27] [43] [3] [9] [82] [10] [5] // each subarray has one element, no more division
  Level 4: [27, 38] [3, 43] [9, 82] [5, 10] // merge each pair of subarrays by comparing and moving elements
  Level 5: [3, 27, 38, 43] [5, 9, 10, 82] // merge each pair of subarrays by comparing and moving elements
  Level 6: [3, 5, 9, 10, 27, 38, 43, 82] // merge the final two subarrays by comparing and moving elements
  ```

  The time complexity analysis can be done as follows:

  - The algorithm divides the array into log n = log 8 = 3 levels, where each level has 2^k subarrays, where k is the level number starting from 0.
  - Each level requires O(n) time to merge the subarrays, where n is the number of elements in the array. This